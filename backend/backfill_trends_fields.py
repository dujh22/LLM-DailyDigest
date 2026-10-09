"""为历史日报条目回填趋势栏目字段 keywords / orgs（见 .omc/plans/trends-contract.md）。

用法（在 backend/ 下）：
    ./venv/bin/python backfill_trends_fields.py --dry-run --limit 5 --only keywords
    ./venv/bin/python backfill_trends_fields.py --only all --since 2026-09-01 --workers 4
    ./venv/bin/python backfill_trends_fields.py --only orgs --orgs-source openalex
    ./venv/bin/python backfill_trends_fields.py --force --until 2025-12-31

参数：
    --only keywords|orgs|all   回填哪些字段（默认 all）
    --since/--until YYYY-MM-DD 按日报日期过滤（闭区间）
    --limit N                  最多处理 N 个条目（按日期顺序，便于分批）
    --force                    已有字段也重算
    --workers N                LLM / OpenAlex 并发数（默认 4）
    --orgs-source openalex|llm|both
                               orgs 来源：openalex 只查有 arXiv 链接的条目；llm 只对无 arXiv
                               链接的条目用 LLM；both（默认）= 两者都做，且 OpenAlex 未命中的
                               arXiv 条目再退回 LLM
    --dry-run                  不调 LLM、不联网、不写盘；打印将发送的分块与将访问的 OpenAlex URL
    --allow-today              也处理今天的日报（默认跳过：服务端可能正在追加条目）

行为：
    - keywords：每 30 条一次 LLM 调用（标题 + 摘要 + 子主题 + 主题），解析 {key: [..]} 写回。
    - orgs：arXiv 条目查 OpenAlex（≤ 8 req/s，429/5xx 退避重试；404 记入缓存下次跳过），
      取 authorships[].institutions[].display_name 去重保序前 8 个，经 normalize_orgs 归一；
      无 arXiv 链接的条目用 LLM，严格要求文本未明示机构时返回 []（空结果也记入缓存）。
    - 幂等、可续跑：已有字段的条目跳过；Ctrl-C 中断时把已拿到的结果写盘并保存缓存。
    - 写盘用 app.rewrite_daily_items：只重写被改动的 item 块，其余逐字保留。
    - 缓存文件 backend/.trends_backfill_cache.json（已 gitignore）。
"""
import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import requests

import app

CACHE_PATH = Path(__file__).resolve().parent / ".trends_backfill_cache.json"
DATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
KEYWORDS_CHUNK = 30
ORGS_LLM_CHUNK = 30
OPENALEX_MIN_INTERVAL = 1.0 / 8  # ≤ 8 req/s
OPENALEX_MAILTO = os.environ.get("OPENALEX_MAILTO", "llm-dailydigest@example.com")
OPENALEX_MAX_ORGS = 8
LLM_TEXT_LIMIT = 1500  # 每条喂给 LLM 的 content/notes 截断长度

_KEYWORDS_PROMPT = (
    "你是大模型研究日报的关键词标注助手。用户给出一批条目（每条含 key、标题、摘要、子主题、主题），"
    "请为每条给出 3~5 个规范技术术语作为 keywords：中文或公认英文缩写（如 \"强化学习\"、\"RLVR\"、"
    "\"工具调用\"、\"过程奖励模型\"），优先复用条目自身子主题/主题以及下面【常用词表】中的写法；"
    "禁止泛词（大模型、人工智能、方法、研究、模型、论文、技术、框架）；不要编造条目中没有的内容。"
    "严格返回 JSON 对象（不要代码块、不要解释）：{\"<key>\": [\"词1\", \"词2\", ...], ...}，"
    "key 必须与输入一一对应。\n"
)
_ORGS_PROMPT = (
    "你是大模型研究日报的机构标注助手。用户给出一批条目（每条含 key、标题、摘要、正文、原始笔记），"
    "请抽取每条【作者或发布方】的机构规范名作为 orgs（如 \"清华大学\"、\"OpenAI\"、\"Google DeepMind\"、"
    "\"上海人工智能实验室\"）。严格规则：仅当文本中明确写出机构名（含公司/高校/实验室/团队名）时才填写；"
    "仅被提及、被比较、被引用的机构不算；文本未明示机构的条目必须返回空数组 []，禁止根据模型名、"
    "产品名或常识推测。每条最多 6 个。"
    "严格返回 JSON 对象（不要代码块、不要解释）：{\"<key>\": [\"机构1\", ...], ...}，key 必须与输入一一对应。"
)


# ------------------------------------------------------------
# 缓存
# ------------------------------------------------------------
def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("openalex_miss", {})
                data.setdefault("llm_orgs_empty", {})
                return data
        except Exception as e:  # noqa: BLE001
            print(f"[warn] 缓存文件损坏，忽略：{e}")
    return {"openalex_miss": {}, "llm_orgs_empty": {}}


def save_cache(cache: dict) -> None:
    tmp = CACHE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(CACHE_PATH)


# ------------------------------------------------------------
# 读取日报条目
# ------------------------------------------------------------
def arxiv_id_of(item: dict):
    """从 paper 字段取 arXiv id（去版本号）；没有返回 None。"""
    m = app._ARXIV_ID_IN_TEXT_RE.search(item.get("paper") or "")
    return m.group(1).lower() if m else None


def collect_records(since, until, allow_today):
    """扫描 content/updates/<date>.md，返回 [{"date","path","idx","item"}]（按日期、块序）。"""
    today = date.today().isoformat()
    records = []
    for p in sorted(app.UPDATES_DIR.glob("*.md")):
        m = DATE_FILE_RE.match(p.name)
        if not m:
            continue
        d = m.group(1)
        if since and d < since or until and d > until:
            continue
        if d == today and not allow_today:
            print(f"[skip] {p.name} 是今天的日报（服务可能正在写入），需要时加 --allow-today")
            continue
        _, fm_body, _ = app.split_front_matter(p.read_text(encoding="utf-8"))
        if not fm_body:
            continue
        _, blocks = app.split_item_blocks(fm_body)
        for idx, block in enumerate(blocks):
            item = app._parse_item_block(block)
            if item is None:
                print(f"[warn] {p.name} 第 {idx} 块解析失败，跳过")
                continue
            records.append({"date": d, "path": p, "idx": idx, "item": item,
                            "key": f"{d}#{idx}"})
    return records


# ------------------------------------------------------------
# keywords（LLM 分块）
# ------------------------------------------------------------
def keywords_payload(rec: dict) -> dict:
    it = rec["item"]
    return {"key": rec["key"], "title": it.get("title", ""), "summary": it.get("summary", ""),
            "subtopic": it.get("subtopic", ""), "topics": list(it.get("topics") or [])}


def run_keywords_chunk(chunk: list, vocab_subs: list) -> dict:
    """一次 LLM 调用处理一个分块，返回 {key: [keywords]}（只含非空结果）。"""
    prompt = _KEYWORDS_PROMPT + "【常用词表】：" + json.dumps(vocab_subs, ensure_ascii=False)
    resp = app._llm_chat(prompt, [keywords_payload(r) for r in chunk], want_json=True)
    out = {}
    if not isinstance(resp, dict):
        raise ValueError("LLM 返回不是 JSON 对象")
    for r in chunk:
        kws = app._norm_str_list(resp.get(r["key"]))[:5]
        if kws:
            out[r["key"]] = kws
    return out


# ------------------------------------------------------------
# orgs（OpenAlex + LLM）
# ------------------------------------------------------------
class OpenAlexClient:
    def __init__(self):
        self._lock = threading.Lock()
        self._last = 0.0
        self.hits = self.misses = self.errors = 0
        self._session = requests.Session()  # trust_env=True：自动读取 HTTPS_PROXY/HTTP_PROXY

    @staticmethod
    def url_for(arxiv_id: str) -> str:
        return (f"https://api.openalex.org/works/doi:10.48550/arXiv.{arxiv_id}"
                f"?mailto={OPENALEX_MAILTO}&select=authorships")

    def _pace(self):
        with self._lock:
            wait = self._last + OPENALEX_MIN_INTERVAL - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()

    def fetch_orgs(self, arxiv_id: str, retries: int = 4):
        """返回 (status, orgs)：status ∈ hit / miss / error。miss = 404 或无机构信息。"""
        url = self.url_for(arxiv_id)
        last = None
        for attempt in range(retries):
            self._pace()
            try:
                r = self._session.get(url, timeout=(10, 30),
                                      headers={"User-Agent": f"LLM-DailyDigest backfill ({OPENALEX_MAILTO})"})
            except requests.RequestException as e:
                last = e
            else:
                if r.status_code == 404:
                    self.misses += 1
                    return "miss", []
                if r.status_code == 429 or r.status_code >= 500:
                    last = RuntimeError(f"HTTP {r.status_code}")
                elif r.status_code != 200:
                    self.errors += 1
                    return "error", []
                else:
                    names = []
                    for a in (r.json().get("authorships") or []):
                        for inst in (a.get("institutions") or []):
                            n = (inst.get("display_name") or "").strip()
                            if n and n not in names:
                                names.append(n)
                    names = names[:OPENALEX_MAX_ORGS]
                    orgs = app.normalize_orgs(names)
                    if orgs:
                        self.hits += 1
                        return "hit", orgs
                    self.misses += 1
                    return "miss", []
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
        self.errors += 1
        print(f"[openalex] {arxiv_id} 失败：{last}")
        return "error", []


def orgs_llm_payload(rec: dict) -> dict:
    it = rec["item"]
    return {"key": rec["key"], "title": it.get("title", ""), "summary": it.get("summary", ""),
            "content": (it.get("content") or "")[:LLM_TEXT_LIMIT],
            "notes": (it.get("notes") or "")[:LLM_TEXT_LIMIT]}


def run_orgs_llm_chunk(chunk: list) -> dict:
    """返回 {key: [orgs]}，空结果也带上（值为 []），便于记缓存。"""
    resp = app._llm_chat(_ORGS_PROMPT, [orgs_llm_payload(r) for r in chunk], want_json=True)
    if not isinstance(resp, dict):
        raise ValueError("LLM 返回不是 JSON 对象")
    return {r["key"]: app.normalize_orgs(resp.get(r["key"]))[:6] for r in chunk}


# ------------------------------------------------------------
# 写盘
# ------------------------------------------------------------
def write_back(records_by_key: dict, results: dict, dry_run: bool):
    """results: key -> {"keywords": [...], "orgs": [...]}（只含要改的字段）。按文件一次性改写。"""
    per_file = {}
    for key, upd in results.items():
        if not upd:
            continue
        rec = records_by_key[key]
        item = dict(rec["item"])
        item.update(upd)
        per_file.setdefault(rec["path"], {})[rec["idx"]] = item
    touched_files = changed_items = 0
    for path in sorted(per_file):
        if dry_run:
            touched_files += 1
            changed_items += len(per_file[path])
            continue
        # 写前重读：文件可能在采集期间被服务端改写（追加/去重），按 id 校验索引仍指向同一条，
        # 对不上的条目跳过并提示（下次运行会重新处理）
        _, fm_body, _ = app.split_front_matter(Path(path).read_text(encoding="utf-8"))
        _, blocks = app.split_item_blocks(fm_body or "")
        safe = {}
        for idx, item in per_file[path].items():
            cur = app._parse_item_block(blocks[idx]) if idx < len(blocks) else None
            if cur and cur.get("id") == item.get("id"):
                safe[idx] = item
            else:
                print(f"[skip] {Path(path).name} 第 {idx} 块已变动（id 不匹配），本次不写入 {item.get('id')}")
        if not safe:
            continue
        n = app.rewrite_daily_items(path, replace=safe)
        if n:
            touched_files += 1
            changed_items += n
    return touched_files, changed_items


# ------------------------------------------------------------
# 主流程
# ------------------------------------------------------------
def parse_args(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=("keywords", "orgs", "all"), default="all")
    ap.add_argument("--since")
    ap.add_argument("--until")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--orgs-source", choices=("openalex", "llm", "both"), default="both")
    ap.add_argument("--allow-today", action="store_true")
    args = ap.parse_args(argv)
    for k in ("since", "until"):
        v = getattr(args, k)
        if v and not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            ap.error(f"--{k} 需为 YYYY-MM-DD")
    return args


def main(argv):
    args = parse_args(argv)
    do_kw = args.only in ("keywords", "all")
    do_orgs = args.only in ("orgs", "all")
    app.trigger_deploy = lambda *a, **k: None  # 离线脚本不触发部署

    cache = load_cache()
    records = collect_records(args.since, args.until, args.allow_today)
    total = len(records)
    before_kw = sum(1 for r in records if r["item"].get("keywords"))
    before_orgs = sum(1 for r in records if r["item"].get("orgs"))
    arxiv_total = sum(1 for r in records if arxiv_id_of(r["item"]))
    print(f"扫描 {total} 条（keywords 已有 {before_kw}，orgs 已有 {before_orgs}，arXiv 条目 {arxiv_total}）")

    # 选出需要处理的条目
    kw_todo, oa_todo, llm_orgs_todo = [], [], []
    oa_cached_skip = llm_cached_skip = 0
    picked = 0
    for r in records:
        need_kw = do_kw and (args.force or not r["item"].get("keywords"))
        need_orgs = do_orgs and (args.force or not r["item"].get("orgs"))
        aid = arxiv_id_of(r["item"])
        oa = llm = False
        if need_orgs:
            if aid and args.orgs_source in ("openalex", "both"):
                if aid in cache["openalex_miss"] and not args.force:
                    oa_cached_skip += 1
                    # 曾未命中：both 模式下退回 LLM
                    llm = args.orgs_source == "both"
                else:
                    oa = True
            elif not aid and args.orgs_source in ("llm", "both"):
                llm = True
            if llm and r["key"] in cache["llm_orgs_empty"] and not args.force:
                llm_cached_skip += 1
                llm = False
        if not (need_kw or oa or llm):
            continue
        picked += 1
        if args.limit and picked > args.limit:
            break
        if need_kw:
            kw_todo.append(r)
        if oa:
            oa_todo.append(r)
        if llm:
            llm_orgs_todo.append(r)
    print(f"待处理：keywords {len(kw_todo)} 条 / OpenAlex {len(oa_todo)} 条 / LLM orgs {len(llm_orgs_todo)} 条"
          f"（缓存跳过：OpenAlex 未命中 {oa_cached_skip}，LLM 空结果 {llm_cached_skip}）")

    records_by_key = {r["key"]: r for r in records}
    results = {}      # key -> {"keywords": [...], "orgs": [...]}
    stats = {"kw_chunks_ok": 0, "kw_chunks_fail": 0, "orgs_chunks_ok": 0, "orgs_chunks_fail": 0}
    oa_client = OpenAlexClient()
    lock = threading.Lock()

    def put(key, field, value):
        with lock:
            results.setdefault(key, {})[field] = value

    kw_chunks = [kw_todo[i:i + KEYWORDS_CHUNK] for i in range(0, len(kw_todo), KEYWORDS_CHUNK)]

    if args.dry_run:
        print("\n[dry-run] 不调 LLM、不联网、不写盘。")
        for n, chunk in enumerate(kw_chunks, 1):
            print(f"\n[dry-run] keywords 分块 {n}/{len(kw_chunks)}（{len(chunk)} 条）：")
            for r in chunk:
                print(f"    {r['key']}  {r['item'].get('title', '')[:60]}")
        if oa_todo:
            print(f"\n[dry-run] 将访问 OpenAlex {len(oa_todo)} 次：")
            for r in oa_todo:
                print(f"    {r['key']}  {OpenAlexClient.url_for(arxiv_id_of(r['item']))}")
        llm_chunks = [llm_orgs_todo[i:i + ORGS_LLM_CHUNK] for i in range(0, len(llm_orgs_todo), ORGS_LLM_CHUNK)]
        for n, chunk in enumerate(llm_chunks, 1):
            print(f"\n[dry-run] orgs LLM 分块 {n}/{len(llm_chunks)}（{len(chunk)} 条）：")
            for r in chunk:
                print(f"    {r['key']}  {r['item'].get('title', '')[:60]}")
        print(f"\n[dry-run] 预计改动条目 ≤ {len({r['key'] for r in kw_todo + oa_todo + llm_orgs_todo})}，"
              f"涉及文件 ≤ {len({r['path'] for r in kw_todo + oa_todo + llm_orgs_todo})}")
        return 0

    vocab_subs = app.label_vocab()["subs"][:300] if kw_chunks else []
    interrupted = False
    try:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
            futs = {}
            for chunk in kw_chunks:
                futs[ex.submit(run_keywords_chunk, chunk, vocab_subs)] = ("kw", chunk)
            for r in oa_todo:
                futs[ex.submit(oa_client.fetch_orgs, arxiv_id_of(r["item"]))] = ("oa", r)
            # OpenAlex 未命中的 arXiv 条目在 both 模式下补进 LLM 队列（第二阶段提交）
            oa_fallback = []
            for fut in as_completed(futs):
                kind, ref = futs[fut]
                try:
                    res = fut.result()
                except Exception as e:  # noqa: BLE001
                    if kind == "kw":
                        stats["kw_chunks_fail"] += 1
                        print(f"[keywords] 分块失败（{len(ref)} 条，首条 {ref[0]['key']}）：{e}")
                    else:
                        print(f"[openalex] {ref['key']} 异常：{e}")
                    continue
                if kind == "kw":
                    stats["kw_chunks_ok"] += 1
                    for key, kws in res.items():
                        put(key, "keywords", kws)
                    print(f"[keywords] 分块完成：{len(res)}/{len(ref)} 条有结果")
                else:
                    status, orgs = res
                    aid = arxiv_id_of(ref["item"])
                    if status == "hit":
                        put(ref["key"], "orgs", orgs)
                    elif status == "miss":
                        with lock:
                            cache["openalex_miss"][aid] = date.today().isoformat()
                        if args.orgs_source == "both" and ref["key"] not in cache["llm_orgs_empty"]:
                            oa_fallback.append(ref)
            llm_queue = llm_orgs_todo + oa_fallback
            llm_chunks = [llm_queue[i:i + ORGS_LLM_CHUNK] for i in range(0, len(llm_queue), ORGS_LLM_CHUNK)]
            futs = {ex.submit(run_orgs_llm_chunk, chunk): chunk for chunk in llm_chunks}
            for fut in as_completed(futs):
                chunk = futs[fut]
                try:
                    res = fut.result()
                except Exception as e:  # noqa: BLE001
                    stats["orgs_chunks_fail"] += 1
                    print(f"[orgs-llm] 分块失败（{len(chunk)} 条，首条 {chunk[0]['key']}）：{e}")
                    continue
                stats["orgs_chunks_ok"] += 1
                n_hit = 0
                for key, orgs in res.items():
                    if orgs:
                        n_hit += 1
                        put(key, "orgs", orgs)
                    else:
                        with lock:
                            cache["llm_orgs_empty"][key] = date.today().isoformat()
                print(f"[orgs-llm] 分块完成：{n_hit}/{len(chunk)} 条有机构")
    except KeyboardInterrupt:
        interrupted = True
        print("\n[中断] 取消未开始的任务，把已获得的结果写盘并保存缓存…")
        try:
            ex.shutdown(wait=False, cancel_futures=True)
        except Exception:  # noqa: BLE001
            pass
    finally:
        touched_files, changed_items = write_back(records_by_key, results, dry_run=False)
        save_cache(cache)

    kw_added = sum(1 for v in results.values() if v.get("keywords"))
    orgs_added = sum(1 for v in results.values() if v.get("orgs"))
    after_kw = sum(1 for r in records if r["item"].get("keywords") or results.get(r["key"], {}).get("keywords"))
    after_orgs = sum(1 for r in records if r["item"].get("orgs") or results.get(r["key"], {}).get("orgs"))
    arxiv_with_orgs = sum(1 for r in records if arxiv_id_of(r["item"]) and
                          (r["item"].get("orgs") or results.get(r["key"], {}).get("orgs")))

    def pct(n):
        return f"{n}/{total} ({(100.0 * n / total if total else 0):.1f}%)"

    print("\n==================== 回填汇总 ====================")
    print(f"{'改动文件':<22}{touched_files}")
    print(f"{'改动条目':<22}{changed_items}（keywords +{kw_added}，orgs +{orgs_added}）")
    print(f"{'keywords 覆盖 前→后':<20}{pct(before_kw)} → {pct(after_kw)}")
    print(f"{'orgs 覆盖 前→后':<21}{pct(before_orgs)} → {pct(after_orgs)}")
    print(f"{'arXiv 条目含 orgs':<21}{arxiv_with_orgs}/{arxiv_total}")
    print(f"{'OpenAlex 命中/未命中/错误':<16}{oa_client.hits}/{oa_client.misses}/{oa_client.errors}"
          f"（缓存跳过 {oa_cached_skip}）")
    print(f"{'LLM 分块 keywords':<22}成功 {stats['kw_chunks_ok']} / 失败 {stats['kw_chunks_fail']}")
    print(f"{'LLM 分块 orgs':<24}成功 {stats['orgs_chunks_ok']} / 失败 {stats['orgs_chunks_fail']}"
          f"（缓存跳过 {llm_cached_skip}）")
    print("==================================================")
    return 130 if interrupted else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
