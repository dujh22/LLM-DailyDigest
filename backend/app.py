"""
LLM-DailyDigest 单条消息提交后端（本地工具）

功能：
  GET  /              交互式填写表单
  GET  /api/topics    返回 content/topic/ 下的合法主题名
  POST /api/extract   用 LLM 从原始文本抽取结构化字段（JSON）
  POST /api/submit    把一条 item 追加到当日日报 content/updates/<date>.md 的 [[items]]
  POST /api/batch/<id>/auto_submit  一键自动处理批次：抽取后跳过人工核对直接提交；疑似重复自动归并
  GET  /recommend     当日推荐页（采集公众号 + arXiv 最近 24h 内容，LLM 相关性筛选）
  GET  /dedup         条目去重归并页（URL 判重，预览 + 应用两步）
  POST /api/dedup/preview|apply  去重扫描 / 执行（days 默认 7，可指定 14、30 等更大窗口）

API Key：读取仓库根目录 api_key.txt；不存在则禁用 LLM 抽取并提示用户。
运行：python backend/app.py  （然后浏览器打开 http://localhost:5050）
"""
import os
import re
import json
import glob
import time
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
from flask import Flask, request, jsonify, render_template

# 自动部署：写入 content/ 后防抖 commit+push 触发 CI 重建（见 backend/deploy.py）。
# 导入失败时降级为空操作，绝不影响内容写入本身。
try:
    from deploy import trigger_deploy, deploy_now
except Exception:  # noqa: BLE001
    def trigger_deploy(*a, **k):
        pass

    def deploy_now(*a, **k):
        return {"ok": False, "message": "deploy 模块未加载"}

# 当日推荐采集模块（见 backend/recommend.py）。导入失败时相关路由返回 503。
try:
    import recommend as recommend_mod
except Exception:  # noqa: BLE001
    recommend_mod = None

# ---- 路径 ----
REPO_ROOT = Path(__file__).resolve().parents[1]
UPDATES_DIR = REPO_ROOT / "content" / "updates"
TOPIC_DIR = REPO_ROOT / "content" / "topic"
RESEARCH_DIR = REPO_ROOT / "content" / "research"
API_KEY_FILE = REPO_ROOT / "api_key.txt"
BATCH_DIR = REPO_ROOT / ".batch_sessions"  # 批处理会话（运行时产物，已 gitignore）

# ---- LLM 配置（可被环境变量覆盖）----
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api-gateway.glm.ai/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-5.6-sol")

# ---- 批处理并发配置 ----
# 同时处理的条目数（每条可能触发 1 次链接抓取 + 1 次 LLM 调用）。
# 该 LLM 网关并发上限可达 100，默认即用满；可用环境变量 BATCH_WORKERS 覆盖。
BATCH_WORKERS = max(1, int(os.environ.get("BATCH_WORKERS", "100")))

app = Flask(__name__)


# ============================================================
# 辅助函数
# ============================================================
def valid_topics():
    """读取 content/topic/ 下的主题文件名作为合法主题集合。"""
    names = []
    for f in glob.glob(str(TOPIC_DIR / "*.md")):
        names.append(Path(f).stem)
    return sorted(names)


def valid_research():
    """读取 content/research/ 下的研究项目名（固定集合，不自动扩展）。"""
    names = []
    for f in glob.glob(str(RESEARCH_DIR / "*.md")):
        names.append(Path(f).stem)
    return sorted(names)


def load_api_key():
    """读取根目录 api_key.txt，返回 key 或 None。"""
    if not API_KEY_FILE.exists():
        return None
    key = API_KEY_FILE.read_text(encoding="utf-8").strip()
    return key or None


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:40]


def parse_target_date(s: str):
    """解析目标日期字符串为 'YYYY-MM-DD'；无效或为空返回 None（=今天）。"""
    if not s:
        return None
    s = str(s).strip()
    # 支持 YYYY-MM-DD / YYYYMMDD / YYYY/MM/DD
    m = re.match(r"^(\d{4})[-/.]?(\d{1,2})[-/.]?(\d{1,2})$", s)
    if not m:
        raise ValueError(f"日期格式无法识别：{s!r}（期望 YYYY-MM-DD 或 YYYYMMDD）")
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    iso = f"{y:04d}-{mo:02d}-{d:02d}"
    date(y, mo, d)  # 校验合法性（非法会抛 ValueError）
    return iso


def count_items(text: str) -> int:
    return len(re.findall(r"^\[\[items\]\]", text, flags=re.MULTILINE))


def create_topic(name: str) -> Path:
    """主题不存在时自动新建 content/topic/<name>.md。"""
    safe = re.sub(r"[\\/]+", "", name.strip()).replace("'", "").replace('"', "")
    if not safe or safe in (".", ".."):
        raise ValueError(f"非法主题名：{name!r}")
    path = TOPIC_DIR / f"{safe}.md"
    if path.exists():
        return path
    d = date.today().isoformat()
    content = (
        "+++\n"
        f"title = '{safe}'\n"
        f"date = {d}T00:00:00+08:00\n"
        "draft = false\n"
        "toc = true\n"
        "+++\n\n"
        f"# {safe}\n\n"
        "> 本主题由提交工具自动创建，可在此补充洞察与资料。\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


# ============================================================
# 主题/子主题归并：索引 + 安全改写
# ============================================================
_MERGE_LOCK = threading.Lock()  # 保护归并写盘，避免与批次提交并发改同一文件
_ITEMS_RE = re.compile(r"^\[\[items\]\]", re.MULTILINE)
# 主题页样板特征：正文（去 front matter）只剩标题行/自动提示行
_TOPIC_BOILERPLATE_RE = re.compile(
    r"^(?:#\s.*|>\s.*本主题由提交工具自动创建.*|>\s.*历史条目已迁入.*|>\s.*本页「相关消息」自动聚合.*|\s*)$"
)


def split_front_matter(text: str):
    """把文件文本切成 (前缀含开头+++, front matter 正文, 后缀含闭合+++及之后)。
    返回 (pre, fm_body, post)；找不到闭合 +++ 时 fm_body=None。"""
    lines = text.split("\n")
    open_idx = close_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "+++":
            if open_idx is None:
                open_idx = i
            else:
                close_idx = i
                break
    if open_idx is None or close_idx is None:
        return text, None, None
    pre = "\n".join(lines[:open_idx + 1]) + "\n"
    fm_body = "\n".join(lines[open_idx + 1:close_idx])
    post = "\n".join(lines[close_idx:])
    return pre, fm_body, post


def split_item_blocks(fm_body: str):
    """把 front matter 正文切成 (prelude, [item_block_text...])。
    prelude 为第一个 [[items]] 之前的内容；每个 block 从 [[items]] 行到下一个 [[items]] 或末尾。"""
    matches = list(_ITEMS_RE.finditer(fm_body))
    if not matches:
        return fm_body, []
    prelude = fm_body[:matches[0].start()]
    blocks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(fm_body)
        blocks.append(fm_body[start:end])
    return prelude, blocks


def _parse_item_block(block: str):
    """解析单个 [[items]] 块为 item dict（失败返回 None）。"""
    import tomli
    try:
        return tomli.loads(block).get("items", [{}])[0]
    except Exception:  # noqa: BLE001
        return None


def _reserialize_item_block(item: dict) -> str:
    """按固定键顺序重写单个 item 块（与 serialize_item_block 一致，复用 tomli_w）。"""
    import tomli_w
    ordered = {
        "id": item.get("id", ""),
        "title": item.get("title", ""),
        "subtopic": item.get("subtopic", ""),
        "topics": item.get("topics", []),
        "research": item.get("research", []),
        "source": item.get("source", ""),
        "summary": item.get("summary", ""),
        "paper": item.get("paper", ""),
        "code": item.get("code", ""),
        "dataset": item.get("dataset", ""),
        "link": item.get("link", ""),
        "content": item.get("content", ""),
        "purpose": item.get("purpose", ""),
        "notes": item.get("notes", ""),
    }
    return tomli_w.dumps({"items": [ordered]}).rstrip("\n")


def apply_merge_to_file(path: Path, topic_map: dict, sub_map: dict) -> int:
    """对单个日报文件套用主题/子主题映射，仅原位替换发生变化的 item 块
    （未变化块逐字保留，diff 最小）。返回改动 item 数。"""
    text = path.read_text(encoding="utf-8")
    pre, fm_body, post = split_front_matter(text)
    if not fm_body:
        return 0
    spans = [m.span() for m in _ITEMS_RE.finditer(fm_body)]
    if not spans:
        return 0
    changed = 0
    new_fm = fm_body
    # 从后往前替换，保持前面偏移有效
    for i in range(len(spans) - 1, -1, -1):
        start, _ = spans[i]
        end = spans[i + 1][0] if i + 1 < len(spans) else len(fm_body)
        block = new_fm[start:end]
        item = _parse_item_block(block)
        if item is None:
            continue
        # 主题：替换 + 去重保序
        new_topics, seen, topics_changed = [], set(), False
        for t in item.get("topics", []):
            nt = topic_map.get(t, t)
            if nt not in seen:
                seen.add(nt)
                new_topics.append(nt)
            if nt != t:
                topics_changed = True
        # 子主题：全局字符串替换
        old_sub = item.get("subtopic", "")
        new_sub = sub_map.get(old_sub, old_sub)
        if not (topics_changed or new_sub != old_sub):
            continue
        item["topics"] = new_topics
        item["subtopic"] = new_sub
        # 保留原 block 的尾部空白（块间空行），只替换核心内容
        core = block.rstrip()
        trailing = block[len(core):]
        new_fm = new_fm[:start] + _reserialize_item_block(item) + trailing + new_fm[end:]
        changed += 1
    if changed:
        path.write_text(pre + new_fm + "\n" + post, encoding="utf-8")
    return changed


def parse_updates_index():
    """扫描全部 content/updates/*.md，构建：
    tree: {topic: {subtopic: [{file,id,title}]}}
    topic_freq / sub_freq: {name: count}
    orphan_topics: [存在 content/topic/<name>.md 但无 item 引用的主题名]
    """
    tree, topic_freq, sub_freq = {}, {}, {}
    files = sorted(glob.glob(str(UPDATES_DIR / "*.md")))
    # 排除模板/摘要类文件
    files = [f for f in files if re.match(r"^\d{4}-\d{2}-\d{2}", Path(f).name)]
    for f in files:
        path = Path(f)
        text = path.read_text(encoding="utf-8")
        _, fm_body, _ = split_front_matter(text)
        if not fm_body:
            continue
        _, blocks = split_item_blocks(fm_body)
        for block in blocks:
            item = _parse_item_block(block)
            if not item:
                continue
            topics = item.get("topics", []) or []
            sub = item.get("subtopic", "") or "(无)"
            entry = {"file": path.name, "id": item.get("id", ""),
                     "title": item.get("title", "")}
            sub_freq[sub] = sub_freq.get(sub, 0) + 1
            for t in topics:
                topic_freq[t] = topic_freq.get(t, 0) + 1
                tree.setdefault(t, {}).setdefault(sub, []).append(entry)
    # 孤立主题页
    topic_files = {p.stem for p in TOPIC_DIR.glob("*.md")}
    orphan_topics = sorted(topic_files - set(topic_freq.keys()))
    return {"tree": tree, "topic_freq": topic_freq,
            "sub_freq": sub_freq, "orphan_topics": orphan_topics}


def topic_page_is_boilerplate(path: Path) -> bool:
    """主题页正文（front matter 之后）是否仅含自动样板 → 可安全删除。"""
    if not path.exists():
        return True
    lines = path.read_text(encoding="utf-8").split("\n")
    seen = 0
    body_start = None
    for i, ln in enumerate(lines):
        if ln.strip() == "+++":
            seen += 1
            if seen == 2:
                body_start = i + 1
                break
    if body_start is None:
        return True
    body = "\n".join(lines[body_start:]).strip()
    if not body:
        return True
    return all(_TOPIC_BOILERPLATE_RE.match(l) for l in body.split("\n"))


def _maps_from_groups(topic_groups=None, sub_groups=None):
    """从 [{sources, target}, ...] 构建合并映射 {src: target}。
    自动忽略 target 为空、src==target 的项；同一 src 出现多次以后者为准。"""
    def build(groups):
        m = {}
        for g in groups or []:
            tgt = (g.get("target") or "").strip()
            if not tgt:
                continue
            for s in (g.get("sources") or []):
                s = (s or "").strip()
                if s and s != tgt:
                    m[s] = tgt
        return m
    return build(topic_groups), build(sub_groups)


# ============================================================
# 条目级去重归并：URL 规范化 + 扫描分组 + 吸收合并
# ============================================================
_URL_FIELDS = ("paper", "code", "dataset", "link")
_ARXIV_PATH_RE = re.compile(
    r"^/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5}|[a-z-]+/[0-9]{7})(?:v\d+)?$", re.I)
_TRACKING_PARAM_PREFIXES = ("utm_", "spm", "vd_source", "share_", "ref", "source")
# 提交时自动查重窗口（今天 + 向前 7 天）
DEDUP_SUBMIT_DAYS = 7
# 归并时可交给 LLM 智能整合的解析字段（notes 原始笔记逐字保留，不经 LLM）
_LLM_MERGE_FIELDS = ("summary", "content", "purpose")


def normalize_url(url: str) -> str:
    """规范化 URL 用于重复判定：纯字符串确定性变换，不联网。
    非 http(s) 链接返回 ""（空值永不参与匹配）。"""
    u = (url or "").strip()
    if not re.match(r"^https?://", u, re.I):
        return ""
    parts = urllib.parse.urlsplit(u)
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    if scheme == "http" and netloc.endswith(":80"):
        netloc = netloc[:-3]
    elif scheme == "https" and netloc.endswith(":443"):
        netloc = netloc[:-4]
    path = parts.path or "/"
    if len(path) > 1:
        path = path.rstrip("/") or "/"
    # arXiv 归一：abs/pdf/html 统一为 abs，去版本号
    if netloc == "arxiv.org":
        m = _ARXIV_PATH_RE.match(path)
        if m:
            return f"https://arxiv.org/abs/{m.group(1).lower()}"
    # 丢弃跟踪参数（utm_* / spm / ref 等），其余按原序重编码；fragment 整体丢弃
    q = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
         if not k.lower().startswith(_TRACKING_PARAM_PREFIXES)]
    query = urllib.parse.urlencode(q) if q else ""
    return urllib.parse.urlunsplit((scheme, netloc, path, query, ""))


def item_url_keys(item: dict) -> set:
    """item 四个 URL 字段的规范化非空值集合；空集合的条目永不参与去重。"""
    keys = set()
    for f in _URL_FIELDS:
        k = normalize_url(item.get(f, "") or "")
        if k:
            keys.add(k)
    return keys


def daily_files_in_window(days: int, end_date=None):
    """窗口内存在的日报文件 [(date_str, Path)...]，按日期旧→新排序。
    窗口 = end_date（默认今天）向前 days 天（含当日共 days+1 个日期）。"""
    end = date.fromisoformat(end_date) if end_date else date.today()
    out = []
    for i in range(days, -1, -1):
        d = (end - timedelta(days=i)).isoformat()
        p = today_daily_path(d)
        if p.exists():
            out.append((d, p))
    return out


def absorb_items(kept: dict, dup: dict, dup_date: str) -> dict:
    """吸收合并：kept 吸收 dup 的更完整字段，返回新 dict（不改入参）。
    确定性规则：标量字段 kept 非空优先；列表字段并集保序；
    长文本取更长方，较短方有独立信息时以 [合并自 …] 标记追加；notes 差异永不丢弃。"""
    merged = dict(kept)
    tag = f"[合并自 {dup_date} {dup.get('id', '')}]"
    for f in ("title", "subtopic", "source", "paper", "code", "dataset", "link"):
        if not (merged.get(f) or "").strip() and (dup.get(f) or "").strip():
            merged[f] = dup[f].strip()
    for f in ("topics", "research"):
        base = list(merged.get(f) or [])
        seen = set(base)
        for v in (dup.get(f) or []):
            if v not in seen:
                seen.add(v)
                base.append(v)
        merged[f] = base
    for f in ("summary", "content", "purpose"):
        a, b = (merged.get(f) or "").strip(), (dup.get(f) or "").strip()
        if not b or b == a:
            continue
        if not a:
            merged[f] = b
            continue
        longer, shorter = (a, b) if len(a) >= len(b) else (b, a)
        if len(shorter) >= 30 and shorter not in longer:
            merged[f] = f"{longer}\n\n{tag}\n{shorter}"
        else:
            merged[f] = longer
    an, bn = (merged.get("notes") or "").strip(), (dup.get("notes") or "").strip()
    if bn and bn != an:
        merged["notes"] = f"{an}\n\n{tag}\n{bn}" if an else bn
    return merged


def _iter_window_items(days: int, end_date=None):
    """遍历窗口内所有日报条目，产出 {"date","file","index","item","keys"}。"""
    for d, path in daily_files_in_window(days, end_date):
        _, fm_body, _ = split_front_matter(path.read_text(encoding="utf-8"))
        if not fm_body:
            continue
        _, blocks = split_item_blocks(fm_body)
        for idx, block in enumerate(blocks):
            item = _parse_item_block(block)
            if not item:
                continue
            keys = item_url_keys(item)
            if not keys:
                continue
            yield {"date": d, "file": path.name, "index": idx, "item": item, "keys": keys}


def scan_duplicate_groups(days: int = 7, end_date=None):
    """扫描窗口内重复条目组（纯读不写）。组 = 任意共享规范化 URL 的条目集合
    （多个 key 命中不同组时用并查集合并）。每组保留最早出现条目（最早文件日期，
    同文件则最早位置），并预演吸收合并结果。返回按保留条目出现位置排序的组列表。"""
    occurrences = list(_iter_window_items(days, end_date))
    # ---- URL key 上的小型并查集 ----
    parent = {}

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    members = {}  # root key -> [occurrence 下标]（按出现顺序）
    for i, occ in enumerate(occurrences):
        roots = set()
        for k in occ["keys"]:
            if k not in parent:
                parent[k] = k
            roots.add(find(k))
        root = min(roots)  # 固定以字符串最小 key 为组代表，保证确定性
        for r in roots:
            if r != root:
                parent[r] = root
                members[root] = members.get(root, []) + members.pop(r, [])
        members.setdefault(root, []).append(i)

    groups = []
    for idxs in members.values():
        if len(idxs) < 2:
            continue
        idxs = sorted(idxs)  # occurrences 本身按 日期→文件内位置 有序
        occs = [occurrences[i] for i in idxs]
        keep, dups = occs[0], occs[1:]
        merged = dict(keep["item"])
        for dup in dups:
            merged = absorb_items(merged, dup["item"], dup["date"])
        # 吸收 diff 预览（keep 原值 → 合并后新值）
        absorb = []
        for f in ("title", "subtopic", "source", "paper", "code", "dataset", "link",
                  "topics", "research", "summary", "content", "purpose", "notes"):
            old, new = keep["item"].get(f), merged.get(f)
            if old != new:
                absorb.append({"field": f, "old": old, "new": new})
        groups.append({
            "keys": sorted({k for occ in occs for k in occ["keys"]}),
            "keep": {"date": keep["date"], "file": keep["file"],
                     "index": keep["index"], "item": keep["item"]},
            "dups": [{"date": d["date"], "file": d["file"],
                      "index": d["index"], "item": d["item"]} for d in dups],
            "absorb": absorb,
            "merged": merged,  # 仅供 apply 使用，preview 路由返回前剔除
        })
    groups.sort(key=lambda g: (g["keep"]["date"], g["keep"]["file"], g["keep"]["index"]))
    return groups


def rewrite_daily_items(path: Path, replace=None, delete=None) -> int:
    """对单个日报文件做条目级改写：replace 为 {块下标: 新 item}，delete 为待删块下标集合。
    与 apply_merge_to_file 同机制（span 从后往前处理，未变化块逐字保留）；
    删除时连同块自身尾部空白一起移除。返回改动块数。"""
    replace, delete = replace or {}, delete or set()
    if not replace and not delete:
        return 0
    text = path.read_text(encoding="utf-8")
    pre, fm_body, post = split_front_matter(text)
    if not fm_body:
        return 0
    spans = [m.span() for m in _ITEMS_RE.finditer(fm_body)]
    if not spans:
        return 0
    changed = 0
    new_fm = fm_body
    for i in range(len(spans) - 1, -1, -1):
        start, _ = spans[i]
        end = spans[i + 1][0] if i + 1 < len(spans) else len(fm_body)
        block = new_fm[start:end]
        if i in delete:
            # 块 span 已含自身尾部空行；前一块的尾随 \n\n 成为与下一块的分隔
            new_fm = new_fm[:start] + new_fm[end:]
            changed += 1
            continue
        if i in replace:
            item = replace[i]
            core = block.rstrip()
            trailing = block[len(core):]
            new_block = _reserialize_item_block(item) + trailing
            if new_block != block:
                new_fm = new_fm[:start] + new_block + new_fm[end:]
                changed += 1
    if changed:
        if delete:
            # 删除可能让 fm_body 末尾残留多余空行（如删掉最后一个块），归一为单个换行
            new_fm = new_fm.rstrip("\n") + "\n" if new_fm.strip() else new_fm
        path.write_text(pre + new_fm + "\n" + post, encoding="utf-8")
    return changed


def _plan_dedup_writes(groups: list):
    """把分组结果转成按文件的改写计划 {file: (replace, delete)}。"""
    per_file = {}
    removed = 0
    for g in groups:
        kf = g["keep"]["file"]
        rep, dele = per_file.setdefault(kf, ({}, set()))
        rep[g["keep"]["index"]] = g["merged"]
        for dup in g["dups"]:
            drep, ddele = per_file.setdefault(dup["file"], ({}, set()))
            ddele.add(dup["index"])
            removed += 1
    return per_file, removed


def apply_dedup_groups(days: int, only=None, use_llm=False) -> dict:
    """执行条目去重归并写盘。only=[{file,id}] 时仅归并保留条目匹配的组；
    use_llm=True 时先用 LLM 合并各组的解析字段（summary/content/purpose），
    失败的组回退规则合并。锁序固定 _SUBMIT_LOCK → _MERGE_LOCK（do_submit 只取
    前者、merge_apply 只取后者，无环不死锁）。LLM 调用慢，在锁外完成；
    锁内重新扫描并校验各组未被并发修改（签名不一致的组跳过）。"""
    groups = scan_duplicate_groups(days)
    if only:
        sel = {(g["file"], g["id"]) for g in only}
        groups = [g for g in groups
                  if (g["keep"]["file"], g["keep"]["item"].get("id")) in sel]
    if not groups:
        return {"ok": False, "errors": ["窗口内没有可归并的重复条目"]}

    llm_merged, llm_errors = 0, []
    if use_llm:
        api_key = load_api_key()
        if not api_key:
            return {"ok": False, "errors": [
                f"未找到 API Key：请在仓库根目录创建 {API_KEY_FILE.relative_to(REPO_ROOT)}，"
                "或取消勾选 LLM 合并。"]}
        with ThreadPoolExecutor(max_workers=8, thread_name_prefix="dedup-llm") as ex:
            futures = [(g, ex.submit(llm_merge_group, g)) for g in groups]
            for g, fu in futures:
                try:
                    vals = fu.result()
                except Exception as e:  # noqa: BLE001
                    llm_errors.append(f"{g['keep']['item'].get('id', '')}: {e}")
                    continue
                hit = False
                for f in _LLM_MERGE_FIELDS:
                    v = (vals.get(f) or "").strip() if isinstance(vals.get(f), str) else ""
                    if v:
                        g["merged"][f] = v
                        hit = True
                if hit:
                    llm_merged += 1

    def sig(x):
        keep = (x["keep"]["file"], x["keep"]["item"].get("id", ""))
        dups = tuple(sorted((d["file"], d["item"].get("id", "")) for d in x["dups"]))
        return keep + dups

    prepared = {sig(g): g for g in groups}
    with _SUBMIT_LOCK, _MERGE_LOCK:
        fresh_sigs = {sig(x) for x in scan_duplicate_groups(days)}
        usable = [g for s, g in prepared.items() if s in fresh_sigs]
        skipped = len(prepared) - len(usable)
        if not usable:
            return {"ok": False, "errors": [
                "预览后条目已被修改（组结构变化），请重新扫描后再执行"]}
        per_file, removed = _plan_dedup_writes(usable)
        files_touched = []
        for fname, (rep, dele) in sorted(per_file.items()):
            n = rewrite_daily_items(UPDATES_DIR / fname, replace=rep, delete=dele)
            if n:
                files_touched.append(fname)
    if files_touched:
        reason = f"条目去重归并：{len(usable)} 组 / 删除 {removed} 条"
        if llm_merged:
            reason += f"（LLM 合并 {llm_merged} 组解析字段）"
        trigger_deploy(reason)
    res = {"ok": True, "groups": len(usable), "removed": removed,
           "files": files_touched, "llm_merged": llm_merged,
           "skipped_stale": skipped}
    if llm_errors:
        res["llm_errors"] = llm_errors[:5]
    return res


def llm_merge_group(group: dict) -> dict:
    """对单个重复组调用 LLM 把各条目的解析字段（summary/content/purpose）
    整合为一份连贯结果。返回 {"summary","content","purpose"}；失败抛异常，
    由调用方回退规则合并。notes/title 等字段不经 LLM（原始笔记逐字保留）。"""
    from openai import OpenAI
    api_key = load_api_key()
    if not api_key:
        raise RuntimeError("未找到 API Key")
    occs = [dict(group["keep"], role="保留")] + \
           [dict(d, role="重复") for d in group["dups"]]
    entries = []
    for occ in occs:
        it = occ["item"]
        entries.append({
            "出现日期": occ["date"], "角色": occ["role"],
            "id": it.get("id", ""), "标题": it.get("title", ""),
            "summary": it.get("summary", "") or "",
            "content": it.get("content", "") or "",
            "purpose": it.get("purpose", "") or "",
        })
    system_prompt = (
        "你是大模型研究日报的条目合并助手。同一工作的多个重复日报条目需要合并为一条，"
        "只合并以下解析字段：\n"
        "- summary: 一句话中文摘要。\n"
        "- content: 正文要点，中文 3~5 句，可用 markdown。\n"
        "- purpose: 用途与启示，markdown 无序列表（每条以 - 开头）。\n"
        "要求：以「保留」条目为基础，整合「重复」条目的补充信息，语义去重、信息补全，"
        "不虚构事实，保持中文为主、术语风格一致；某字段所有条目均为空时返回空字符串。"
        "严格返回 JSON 对象（不要代码块、不要解释）："
        '{"summary": "...", "content": "...", "purpose": "..."}'
    )
    client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(entries, ensure_ascii=False)},
        ],
    )
    cleaned = (resp.choices[0].message.content or "").strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    parsed = json.loads(cleaned)
    return {f: (parsed.get(f) or "") for f in _LLM_MERGE_FIELDS}


def find_dup_for_item(item: dict, days: int = DEDUP_SUBMIT_DAYS, target_date=None):
    """提交前查重：返回窗口内最早的重条目描述（含 matched_url）或 None。
    窗口 = min(target_date, today) - days .. today（补录历史日期时也查其后已有条目）。"""
    keys = item_url_keys(item)
    if not keys:
        return None
    base = target_date or date.today().isoformat()
    start = date.fromisoformat(base) - timedelta(days=days)
    end = date.today()
    cur = start
    while cur <= end:
        ds = cur.isoformat()
        p = today_daily_path(ds)
        if p.exists():
            _, fm_body, _ = split_front_matter(p.read_text(encoding="utf-8"))
            if fm_body:
                _, blocks = split_item_blocks(fm_body)
                for idx, block in enumerate(blocks):
                    ex = _parse_item_block(block)
                    if not ex:
                        continue
                    hit = keys & item_url_keys(ex)
                    if hit:
                        return {"date": ds, "file": p.name, "index": idx,
                                "item": ex, "matched_url": sorted(hit)[0]}
        cur += timedelta(days=1)
    return None


def merge_report_maps(topic_map: dict, sub_map: dict):
    """dry-run：基于映射表返回影响范围，不写盘。"""
    # item 级影响统计
    items_affected = 0
    files_affected = []
    for f in sorted(glob.glob(str(UPDATES_DIR / "*.md"))):
        p = Path(f)
        if not re.match(r"^\d{4}-\d{2}-\d{2}", p.name):
            continue
        _, fm_body, _ = split_front_matter(p.read_text(encoding="utf-8"))
        if not fm_body:
            continue
        _, blocks = split_item_blocks(fm_body)
        file_hit = 0
        for block in blocks:
            item = _parse_item_block(block)
            if not item:
                continue
            hit = (topic_map and any(t in topic_map for t in item.get("topics", []))) \
                  or (sub_map and item.get("subtopic", "") in sub_map)
            if hit:
                file_hit += 1
        if file_hit:
            files_affected.append(p.name)
            items_affected += file_hit

    # 主题页：源页删除分类 + 目标页是否需新建
    to_delete, with_content, to_create = [], [], []
    for t in topic_map:
        tp = TOPIC_DIR / f"{t}.md"
        if tp.exists():
            if topic_page_is_boilerplate(tp):
                to_delete.append(t)
            else:
                with_content.append(t)
    for tgt in sorted(set(topic_map.values())):
        if not (TOPIC_DIR / f"{tgt}.md").exists():
            to_create.append(tgt)

    def pairs(m):
        return [{"src": k, "tgt": v} for k, v in sorted(m.items())]

    return {
        "items_affected": items_affected,
        "files_affected": files_affected,
        "files_count": len(files_affected),
        "topic_pairs": pairs(topic_map),
        "sub_pairs": pairs(sub_map),
        "topic_files_to_delete": sorted(to_delete),
        "topic_files_with_content": sorted(with_content),
        "topic_files_to_create": to_create,
    }


def merge_apply_maps(topic_map: dict, sub_map: dict):
    """基于映射表执行归并写盘。返回 report + ok/deleted。"""
    if not topic_map and not sub_map:
        return {"ok": False, "errors": ["未提供任何有效的归并映射（source==target 或目标为空已忽略）"]}
    report = merge_report_maps(topic_map, sub_map)
    if report["items_affected"] == 0 and not report["topic_files_to_delete"]:
        return {"ok": False, "errors": ["没有命中的条目，无需归并"], "summary": report}
    with _MERGE_LOCK:
        for fname in report["files_affected"]:
            apply_merge_to_file(UPDATES_DIR / fname, topic_map, sub_map)
        for tgt in report["topic_files_to_create"]:
            create_topic(tgt)
        deleted = []
        for t in report["topic_files_to_delete"]:
            tp = TOPIC_DIR / f"{t}.md"
            if tp.exists():
                tp.unlink()
                deleted.append(t)
    report["deleted_topic_pages"] = deleted
    report["ok"] = True
    return report


def merge_preview(topic_sources, topic_target, sub_sources, sub_target):
    """单组归并的 dry-run（向后兼容）。"""
    topic_map, sub_map = _maps_from_groups(
        [{"sources": topic_sources, "target": topic_target}] if topic_target else None,
        [{"sources": sub_sources, "target": sub_target}] if sub_target else None)
    report = merge_report_maps(topic_map, sub_map)
    # 附加单组语义字段（前端兼容）
    report["topic_sources"] = sorted(topic_map)
    report["topic_target"] = topic_target if topic_map else ""
    report["sub_sources"] = sorted(sub_map)
    report["sub_target"] = sub_target if sub_map else ""
    report["target_topic_exists"] = topic_target not in report["topic_files_to_create"] if topic_map else True
    return report


def merge_apply(topic_sources, topic_target, sub_sources, sub_target):
    """单组归并执行（向后兼容）。"""
    topic_map, sub_map = _maps_from_groups(
        [{"sources": topic_sources, "target": topic_target}] if topic_target else None,
        [{"sources": sub_sources, "target": sub_target}] if sub_target else None)
    res = merge_apply_maps(topic_map, sub_map)
    if res.get("ok"):
        res["topic_sources"] = sorted(topic_map)
        res["topic_target"] = topic_target if topic_map else ""
        res["sub_sources"] = sorted(sub_map)
        res["sub_target"] = sub_target if sub_map else ""
    return res


def merge_suggest():
    """调用 LLM 对全部主题/子主题做近义聚类，返回归并推荐。"""
    api_key = load_api_key()
    if not api_key:
        return {"ok": False, "errors": ["未找到 API Key，无法调用 LLM"]}
    idx = parse_updates_index()
    topics = sorted(idx["topic_freq"].keys(), key=lambda k: -idx["topic_freq"][k])
    subs = sorted(idx["sub_freq"].keys(), key=lambda k: -idx["sub_freq"][k])
    prompt = (
        "你是数据清洗助手。下面是科研日报的【主题】和【子主题】标签列表（带出现频次）。"
        "请找出其中【语义近义、重复、应归并】的标签组，每组给出推荐归并后的标准名与一句理由。"
        "只合并真正同义/重复的；不要把语义不同的合并；单孤立标签不要输出。严格返回 JSON：\n"
        '{"topics":[{"sources":["标签a","标签b"],"target":"标准名","reason":"..."}],'
        '"subtopics":[{"sources":[...],"target":"...","reason":"..."}]}\n'
        "不要代码块、不要解释。\n\n"
        f"主题（name:频次）：{json.dumps([(t, idx['topic_freq'][t]) for t in topics], ensure_ascii=False)}\n\n"
        f"子主题（name:频次）：{json.dumps([(s, idx['sub_freq'][s]) for s in subs], ensure_ascii=False)}"
    )
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "system", "content": "你是严谨的数据清洗助手，只输出 JSON。"},
                      {"role": "user", "content": prompt}],
        )
        raw = (resp.choices[0].message.content or "").strip()
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "errors": [f"LLM 调用失败：{e}"]}
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return {"ok": False, "errors": ["LLM 返回无法解析为 JSON"], "raw": raw}
    # 规范化
    def norm(group):
        out = []
        for g in (group or []):
            src = g.get("sources", [])
            if isinstance(src, str):
                src = [src]
            src = [str(x).strip() for x in src if str(x).strip()]
            tgt = str(g.get("target", "")).strip()
            if len(src) >= 2 and tgt:
                out.append({"sources": src, "target": tgt,
                            "reason": str(g.get("reason", ""))})
        return out
    return {"ok": True,
            "topics": norm(parsed.get("topics")),
            "subtopics": norm(parsed.get("subtopics"))}


def today_daily_path(d=None) -> Path:
    d = d or date.today().isoformat()
    return UPDATES_DIR / f"{d}.md"


def ensure_daily(d=None) -> Path:
    """当日日报不存在则按基础模板创建（item 之后插入到 +++ 之前）。"""
    path = today_daily_path(d)
    if not path.exists():
        d = d or date.today().isoformat()
        template = (
            "+++\n"
            f"title = '{d} 科研追新'\n"
            f"date = {d}T00:00:00+08:00\n"
            "draft = false\n"
            "toc = true\n"
            "+++\n\n"
            "> 当日精选（由提交工具自动创建）。\n"
        )
        path.write_text(template, encoding="utf-8")
    return path


def serialize_item_block(item: dict) -> str:
    """用 tomli_w 序列化单条 item 为 [[items]] 文本块（保证转义正确）。"""
    import tomli_w
    # 按可读顺序构建（Python dict 保持插入顺序）
    ordered = {
        "id": item.get("id", ""),
        "title": item.get("title", ""),
        "subtopic": item.get("subtopic", ""),
        "topics": item.get("topics", []),
        "research": item.get("research", []),
        "source": item.get("source", ""),
        "summary": item.get("summary", ""),
        "paper": item.get("paper", ""),
        "code": item.get("code", ""),
        "dataset": item.get("dataset", ""),
        "link": item.get("link", ""),
        "content": item.get("content", ""),
        "purpose": item.get("purpose", ""),
        "notes": item.get("notes", ""),
    }
    return tomli_w.dumps({"items": [ordered]}).rstrip("\n")


def append_item(item: dict, target_date=None) -> Path:
    """把 item 追加到指定日期日报 front matter 内（target_date=None 表示今天）。"""
    path = ensure_daily(target_date)
    # 保证 id 在该日报内唯一（冲突时追加 -2/-3）
    existing = set(re.findall(r'^id\s*=\s*["\']([^"\']+)', path.read_text(encoding="utf-8"), re.M))
    base = item.get("id") or "item"
    nid, n = base, 2
    while nid in existing:
        nid = f"{base}-{n}"; n += 1
    item["id"] = nid
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    # 找到第二个 +++ （闭合 front matter 的那一行）
    seen = 0
    close_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "+++":
            seen += 1
            if seen == 2:
                close_idx = i
                break
    if close_idx is None:
        raise RuntimeError(f"未在 {path} 找到闭合 +++ front matter 分隔符")
    block = serialize_item_block(item)
    new_lines = lines[:close_idx] + ["", block, ""] + lines[close_idx:]
    path.write_text("\n".join(new_lines), encoding="utf-8")
    return path


def build_item_from_form(data: dict) -> dict:
    """从前端表单数据组装 item，自动补 id。data['date'] 指定目标日报日期。"""
    target_date = None
    try:
        target_date = parse_target_date(data.get("date"))
    except ValueError as e:
        raise ValueError(str(e)) from None
    topics = data.get("topics", [])
    if isinstance(topics, str):
        topics = [t.strip() for t in topics.split(",") if t.strip()]
    research = data.get("research", [])
    if isinstance(research, str):
        research = [t.strip() for t in research.split(",") if t.strip()]
    item = {
        "id": (data.get("id") or "").strip(),
        "title": (data.get("title") or "").strip(),
        "subtopic": (data.get("subtopic") or "").strip(),
        "topics": topics,
        "research": research,
        "source": (data.get("source") or "").strip(),
        "summary": (data.get("summary") or "").strip(),
        "paper": (data.get("paper") or "").strip(),
        "code": (data.get("code") or "").strip(),
        "dataset": (data.get("dataset") or "").strip(),
        "link": (data.get("link") or "").strip(),
        "content": (data.get("content") or "").strip(),
        "purpose": (data.get("purpose") or "").strip(),
        "notes": data.get("notes", ""),
    }
    # 自动生成 id（纯中文/过短标题无法 slug 时，退化为 item-N，避免冲突）
    if not item["id"]:
        slug = slugify(item["title"])
        if len(slug) >= 3:
            item["id"] = slug
        else:
            path = today_daily_path(target_date)
            n = count_items(path.read_text(encoding="utf-8")) if path.exists() else 0
            item["id"] = f"item-{n + 1}"
    item["_target_date"] = target_date  # 仅供提交路由使用，不写入 item
    return item


# ============================================================
# 链接抓取（github / arxiv / 微信公众号 / 通用网页）
# 抓取内容仅供 LLM 抽取增强上下文，绝不写入 notes 原始笔记。
# ============================================================
_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_LINK_TIMEOUT = (10, 30)  # (连接超时, 读取超时)，连接超时单独收紧以便快速重试
_LINK_CACHE: dict = {}  # url -> {"t": ts, "data": result dict}
_LINK_CACHE_TTL = 300

_URL_RE = re.compile(r"https?://[^\s)\"'<>，。、；：）】\]]+")


def classify_link(url: str) -> str:
    u = url.lower()
    if "github.com" in u:
        return "github"
    if "arxiv.org" in u:
        return "arxiv"
    if "huggingface.co" in u:
        return "hf"
    if "mp.weixin.qq.com" in u:
        return "wechat"
    return "web"


def detect_links(text: str):
    """从文本中提取去重后的 (url, kind) 列表。"""
    out, seen = [], set()
    for m in _URL_RE.finditer(text or ""):
        url = m.group(0).rstrip(".,;)]\"'")
        if url in seen:
            continue
        seen.add(url)
        out.append((url, classify_link(url)))
    return out


def _http_get(url: str, retries: int = 3, **kw):
    """带重试的 GET：本地代理瞬断（ProxyError/超时）时退避重试后可自愈。"""
    headers = {"User-Agent": _UA}
    headers.update(kw.pop("headers", {}))
    last_exc = None
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=headers, timeout=_LINK_TIMEOUT, **kw)
            r.raise_for_status()
            return r
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code < 500:
                raise  # 4xx 重试无意义
            last_exc = e
        except requests.RequestException as e:  # ProxyError / 连接与读取超时
            last_exc = e
        if attempt < retries - 1:
            time.sleep(1.5 * (attempt + 1))
    raise last_exc


def _clean_text(s: str, limit: int = 6000) -> str:
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    return s[:limit]


def fetch_arxiv(url: str) -> dict:
    """通过 arxiv Atom API 取标题/作者/摘要。"""
    m = re.search(r"(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?|[a-z\-]+/[0-9]{7}(?:v\d+)?)", url)
    if not m:
        m = re.search(r"/([^/?#]+(?:v\d+)?)$", url)
    if not m:
        raise ValueError("无法从 URL 解析 arxiv id")
    arxiv_id = m.group(1)
    api = f"https://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"
    soup = BeautifulSoup(_http_get(api).text, "html.parser")
    entry = soup.find("entry")
    if not entry:
        raise ValueError("arxiv 未返回条目（id 可能无效）")
    title = entry.find("title").get_text(strip=True)
    summary = entry.find("summary").get_text(strip=True)
    authors = [a.find("name").get_text(strip=True)
               for a in entry.find_all("author") if a.find("name")]
    link = entry.find("link", attrs={"title": "pdf"})
    pdf = link.get("href") if link else ""
    text = (f"标题：{title}\n作者：{', '.join(authors)}\n"
            f"PDF：{pdf}\n摘要：{summary}")
    return {"title": title, "text": text}


def fetch_github(url: str) -> dict:
    """GitHub API 取仓库描述 + raw README（节选）。"""
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)", url)
    if not m:
        raise ValueError("非标准 github 仓库 URL")
    owner, repo = m.group(1), m.group(2).rstrip(".git")
    headers = {"Accept": "application/vnd.github+json"}
    resp = _http_get(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
    resp.raise_for_status()
    meta = resp.json()
    desc = meta.get("description") or ""
    topics = meta.get("topics") or []
    stars = meta.get("stargazers_count")
    homepage = meta.get("homepage") or ""
    readme = ""
    try:
        rr = _http_get(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md")
        if rr.status_code == 200:
            readme = _clean_text(rr.text, 4000)
    except Exception:  # noqa: BLE001
        pass
    text = (f"仓库：{owner}/{repo}\n描述：{desc}\nStars：{stars}\n"
            f"Topics：{', '.join(topics)}\nHomepage：{homepage}\nREADME（节选）：\n{readme}")
    return {"title": f"{owner}/{repo}", "text": text}


def fetch_wechat(url: str) -> dict:
    """微信公众号文章：定位 #js_content 正文。"""
    r = _http_get(url)
    r.encoding = r.apparent_encoding or "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    h = soup.find("h1") or soup.find("title")
    title = h.get_text(strip=True) if h else ""
    body = soup.select_one("#js_content") or soup.select_one(".rich_media_content")
    if body is None:
        raise ValueError("未定位到微信正文（可能需要验证或非文章页）")
    text = _clean_text(body.get_text("\n", strip=True), 6000)
    return {"title": title, "text": f"标题：{title}\n正文：{text}"}


def fetch_hf(url: str) -> dict:
    """HuggingFace 链接：
    - /papers/<arxiv_id> → 复用 arxiv 抓取器（取标题/作者/摘要）
    - 其他（模型/数据集页等）→ 通用 HTML 正文抽取
    """
    m = re.search(r"huggingface\.co/papers/([^/?#]+)", url, re.IGNORECASE)
    if m:
        arxiv_id = m.group(1)
        return fetch_arxiv(f"https://arxiv.org/abs/{arxiv_id}")
    return fetch_generic(url)


def fetch_generic(url: str) -> dict:
    """通用网页正文抽取。"""
    r = _http_get(url)
    r.encoding = r.apparent_encoding or "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    for s in soup(["script", "style", "noscript", "nav", "footer", "header"]):
        s.decompose()
    t = soup.find("title")
    title = t.get_text(strip=True) if t else ""
    # 优先取 <article> / <main>，否则整页正文
    node = soup.find("article") or soup.find("main") or soup
    text = _clean_text(node.get_text("\n", strip=True), 6000)
    if len(text) < 120:
        text = _clean_text(soup.get_text("\n", strip=True), 6000)
    return {"title": title, "text": f"标题：{title}\n正文：{text}"}


_FETCHERS = {"github": fetch_github, "arxiv": fetch_arxiv, "hf": fetch_hf,
             "wechat": fetch_wechat, "web": fetch_generic}


def resolve_link(url: str, kind: str, use_cache: bool = True) -> dict:
    """抓取单个链接，返回带 ok 标记的结果（带 5 分钟缓存）。"""
    if use_cache and url in _LINK_CACHE:
        ent = _LINK_CACHE[url]
        if time.time() - ent["t"] < _LINK_CACHE_TTL:
            return dict(ent["data"])
    fn = _FETCHERS.get(kind, fetch_generic)
    try:
        res = fn(url)
        data = {"url": url, "kind": kind, "ok": True,
                "title": res.get("title", ""), "chars": len(res.get("text", "")),
                "text": res.get("text", "")}
    except Exception as e:  # noqa: BLE001
        data = {"url": url, "kind": kind, "ok": False,
                "reason": str(e) or "抓取失败", "text": ""}
    if use_cache:
        _LINK_CACHE[url] = {"t": time.time(), "data": data}
    return data


def resolve_all(text: str):
    """抓取文本中所有链接，返回 (resolved_list, unresolved_list, fetched_texts)。"""
    resolved, unresolved, fetched_texts = [], [], []
    for url, kind in detect_links(text):
        r = resolve_link(url, kind)
        if r["ok"]:
            resolved.append({"url": url, "kind": kind,
                             "title": r["title"], "chars": r["chars"]})
            fetched_texts.append(f"【来自链接 {url}（{kind}）】\n{r['text']}")
        else:
            unresolved.append({"url": url, "kind": kind, "reason": r.get("reason", "")})
    return resolved, unresolved, fetched_texts


# ============================================================
# 批处理会话（txt 多条录入，逐条交互）
# ============================================================
def parse_batch_entries(text: str):
    """按空行分段解析为条目列表；去掉每段开头的列表标记（1. / - / * / 数字、）。"""
    blocks = re.split(r"\n[ \t]*\n", text or "")
    entries = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        # 去掉行首的列表标记
        b = re.sub(r"(?m)^\s*(?:\d+[.)、]|[-*•·]\s*)+", "", b)
        b = b.strip()
        if b:
            entries.append(b)
    return entries


def new_batch_id() -> str:
    import secrets
    return date.today().isoformat() + "-" + secrets.token_hex(3)


def save_batch(batch: dict) -> Path:
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    p = BATCH_DIR / f"{batch['batch_id']}.json"
    p.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
    return p


def load_batch(batch_id: str):
    if not re.fullmatch(r"[A-Za-z0-9_\-]+", batch_id or ""):
        app.logger.warning("load_batch 拒绝非法 id: %r", batch_id)
        return None
    p = BATCH_DIR / f"{batch_id}.json"
    if not p.exists():
        app.logger.warning("load_batch 文件不存在: %s (BATCH_DIR=%s)", p, BATCH_DIR)
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        app.logger.warning("load_batch 解析失败 %s: %s", p, e)
        return None


def update_batch_entry(batch_id: str, idx: int, **fields):
    """原子地更新某条目（加锁，避免并发写竞争）。"""
    with _BATCH_FILE_LOCK:
        batch = load_batch(batch_id)
        if not batch:
            return None
        for e in batch.get("entries", []):
            if e.get("idx") == idx:
                e.update(fields)
                break
        save_batch(batch)
        return batch


# 正在后台处理的批次 id 集合（防止重复启动）
_RUNNING_BATCHES: set = set()
_RUNNING_LOCK = threading.Lock()          # 保护 _RUNNING_BATCHES
_BATCH_FILE_LOCK = threading.Lock()       # 保护批次 JSON 的读-改-写


# ============================================================
# LLM 抽取核心（单条与批处理共用）
# ============================================================
def llm_extract(raw: str, extra: str = "") -> dict:
    """对单条 raw 执行：链接抓取 + LLM 抽取。返回标准结果字典（非 Flask 响应）。
    成功：{"ok": True, "data": parsed, "resolved_links": [...], "unresolved_links": [...]}
    失败：{"ok": False, "errors": [...], (可选) "raw": ...}
    抓取内容与 extra 仅用于本次抽取，绝不写入 notes。
    """
    raw = (raw or "").strip()
    if not raw:
        return {"ok": False, "errors": ["raw 不能为空"]}
    extra = (extra or "").strip()

    resolved, unresolved, fetched_texts = resolve_all(raw)

    api_key = load_api_key()
    if not api_key:
        return {"ok": False, "errors": [
            f"未找到 API Key：请在仓库根目录创建 {API_KEY_FILE.relative_to(REPO_ROOT)} "
            f"并填入你的 GLM/OpenAI 兼容 api_key。"]}

    topics = valid_topics()
    research = valid_research()
    system_prompt = (
        "你是大模型研究日报的结构化信息抽取助手。"
        "从用户提供的原始文本中抽取【一条消息】的结构化字段，严格返回 JSON（不要代码块、不要额外解释）。"
        "若文本中包含「来自链接」「用户补充内容」等参考区块，请充分利用其中信息填充字段。"
        "字段定义：\n"
        "- title: 标题，中文为主，可含英文术语，简洁。\n"
        "- subtopic: 子主题，简短标签（2~6 字），用于在该主题页里归入栏目。\n"
        f"- topics: 所属主题数组，优先从下面【已有】列表选取：{json.dumps(topics, ensure_ascii=False)}\n"
        "- suggested_topics: 额外推断【最多 3 个尚不存在的新主题名】（每个 2~4 字中文），"
        "作为候选供用户决定是否新建；不要与已有列表重复；无可推断时返回空数组 []。\n"
        f"- research: 归属的研究项目数组，只能从下面列表选取，无匹配返回空数组 []：{json.dumps(research, ensure_ascii=False)}\n"
        "- source: 来源（公众号名 / arxiv 分类 / 站点名），无法判断填 \"未知\"。\n"
        "- summary: 一句话中文摘要。\n"
        "- paper: 论文链接（arxiv URL），无则 \"\"。\n"
        "- code: 代码链接（github URL），无则 \"\"。\n"
        "- dataset: 数据集链接，无则 \"\"。\n"
        "- link: 原文链接（非论文类消息，如微信文章），无则 \"\"。\n"
        "- content: 正文，中文 3~5 句要点，可用 markdown。\n"
        "- purpose: 用途与启示，markdown 无序列表（每条以 - 开头）。\n"
        "只输出 JSON 对象。"
    )

    augmented = raw
    if fetched_texts:
        augmented += ("\n\n===== 以下为自动读取的链接内容（仅供抽取，不会写入原始笔记）=====\n\n"
                      + "\n\n".join(fetched_texts))
    if extra:
        augmented += ("\n\n===== 以下为用户补充内容（仅供抽取，不会写入原始笔记）=====\n\n" + extra)

    content_str, errors = "", []
    for attempt in range(3):  # 限流/瞬断/偶发坏输出：退避重试，避免一有问题就待介入
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
            resp = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": augmented},
                ],
            )
            content_str = resp.choices[0].message.content or ""
        except Exception as e:  # noqa: BLE001
            errors = [f"LLM 调用失败：{e}"]
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            return {"ok": False, "errors": errors}
        cleaned = content_str.strip()
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
        try:
            parsed = json.loads(cleaned)
            break
        except json.JSONDecodeError:
            errors = ["LLM 返回无法解析为 JSON"]
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            return {"ok": False, "errors": errors, "raw": content_str}

    # 规范化
    t = parsed.get("topics", [])
    parsed["topics"] = [str(x) for x in ([t] if isinstance(t, str) else t)]
    s = parsed.get("suggested_topics", [])
    parsed["suggested_topics"] = [str(x).strip() for x in ([s] if isinstance(s, str) else s) if str(x).strip()]
    r = parsed.get("research", [])
    parsed["research"] = [str(x).strip() for x in ([r] if isinstance(r, str) else r) if str(x).strip()]

    return {"ok": True, "data": parsed,
            "resolved_links": resolved, "unresolved_links": unresolved}


# ============================================================
# 批处理自动处理（链接抓取 + LLM 抽取 → 待核对/待介入）
# ============================================================
def process_one_entry(batch_id: str, idx: int):
    """处理单条：链接抓取 →（视情况）LLM 抽取，并更新状态。
    状态流转：pending → processing → review(待核对) / intervention(待介入)。
    有抓取失败的链接时，先不消耗 LLM，置为 intervention 等用户补充后手动抽取。
    已 done 的条目不覆盖。"""
    batch = load_batch(batch_id)
    if not batch:
        return
    entry = next((e for e in batch["entries"] if e.get("idx") == idx), None)
    if not entry or entry.get("status") == "done":
        return
    update_batch_entry(batch_id, idx, status="processing", error="")
    raw = entry.get("raw", "")
    resolved, unresolved, _ = resolve_all(raw)

    if unresolved:
        # 瞬时抖动（代理断连/反爬限流）重抓几轮再判死；成功结果会进缓存，
        # 供下方 llm_extract 内部的 resolve_all 直接复用。
        for attempt in range(2):
            time.sleep(2 * (attempt + 1))
            still = []
            for u in unresolved:
                r = resolve_link(u["url"], u["kind"], use_cache=False)
                if r["ok"]:
                    resolved.append({"url": u["url"], "kind": u["kind"],
                                     "title": r["title"], "chars": r["chars"]})
                else:
                    still.append(u)
            unresolved = still
            if not unresolved:
                break
    if unresolved:
        # 仍有链接抓不到 → 待介入（保存链接状态供前端展示，跳过 LLM 抽取）
        update_batch_entry(batch_id, idx,
                           status="intervention",
                           resolved_links=resolved,
                           unresolved_links=unresolved,
                           data={},
                           error="",
                           processed_at=datetime.now().isoformat(timespec="seconds"))
        return

    res = llm_extract(raw)
    if res["ok"]:
        update_batch_entry(batch_id, idx,
                           status="review",
                           data=res.get("data", {}),
                           resolved_links=res.get("resolved_links", resolved),
                           unresolved_links=[],
                           error="",
                           processed_at=datetime.now().isoformat(timespec="seconds"))
    else:
        update_batch_entry(batch_id, idx,
                           status="intervention",
                           resolved_links=resolved,
                           unresolved_links=[],
                           data={},
                           error="；".join(res.get("errors", [])),
                           processed_at=datetime.now().isoformat(timespec="seconds"))


def process_batch_background(batch_id: str) -> bool:
    """并发处理批次内所有 pending 条目（线程池，并发上限 BATCH_WORKERS）。
    已在运行则返回 False。并发写状态由 _BATCH_FILE_LOCK 保护。"""
    with _RUNNING_LOCK:
        if batch_id in _RUNNING_BATCHES:
            return False
        _RUNNING_BATCHES.add(batch_id)

    def run():
        try:
            batch = load_batch(batch_id)
            if not batch:
                return
            pending = [e["idx"] for e in batch["entries"] if e.get("status") == "pending"]
            with ThreadPoolExecutor(max_workers=BATCH_WORKERS,
                                    thread_name_prefix=f"batch-{batch_id[:8]}") as ex:
                # map 会按提交顺序调度并在全部完成/异常后返回；逐个触发即可
                list(ex.map(lambda i: process_one_entry(batch_id, i), pending))
        finally:
            with _RUNNING_LOCK:
                _RUNNING_BATCHES.discard(batch_id)

    threading.Thread(target=run, daemon=True).start()
    return True


# ============================================================
# 一键自动处理：跳过人工核对，抽取结果直接提交
# ============================================================
def _auto_absorb_into_dup(payload: dict, dup: dict) -> str:
    """把被查重拦截的新条目自动吸收归并进已有日报条目，返回归并描述。
    复用 /dedup 的 absorb_items 确定性规则：旧条目非空字段优先、列表字段
    取并集、长文本取更完整方、notes 差异以 [合并自 …] 标记追加。"""
    item = build_item_from_form(payload)
    item.pop("_target_date", None)
    merged = absorb_items(dup["item"], item, date.today().isoformat())
    path = today_daily_path(dup["date"])
    with _SUBMIT_LOCK:
        changed = rewrite_daily_items(path, replace={dup["index"]: merged})
    if changed:
        trigger_deploy(f"自动归并条目 {item['id']} → {path.name}")
    return f"已自动归并到 {dup['date']} 日报（{dup['file']}，id={dup['item'].get('id', '')}）"


def submit_review_entry(batch_id: str, idx: int) -> dict:
    """把一条 review（待核对）条目的抽取结果直接提交写入日报。
    组装逻辑与人工核对页的默认行为一致：
    - notes 逐字保留原始信息 raw；
    - suggested_topics（候选新主题）在人工页默认勾选，此处同样并入 topics 一并提交。
    命中查重时不阻断：自动吸收归并进已有条目并标记 done（归并说明记入 note）。
    其余提交失败则保留 review 状态并记录 error。"""
    batch = load_batch(batch_id)
    if not batch:
        return {"ok": False, "errors": ["批次不存在"]}
    entry = next((e for e in batch["entries"] if e.get("idx") == idx), None)
    if not entry or entry.get("status") != "review":
        return {"ok": False, "errors": ["条目不在待核对状态"]}
    data = entry.get("data") or {}
    topics = [t for t in (data.get("topics") or []) if str(t).strip()]
    for t in (data.get("suggested_topics") or []):
        t = str(t).strip()
        if t and t not in topics:
            topics.append(t)
    payload = {k: data.get(k) or "" for k in
               ("title", "subtopic", "source", "summary", "paper",
                "code", "dataset", "link", "content", "purpose")}
    payload.update({
        "id": "",
        "topics": topics,
        "research": data.get("research") or [],
        "notes": entry.get("raw", ""),
    })
    ok, res = do_submit(payload)
    if ok:
        update_batch_entry(batch_id, idx, status="done", error="",
                           item_id=res["item"]["id"], file=res["file"])
        return res
    if res.get("dup"):
        # 疑似重复：不阻断一键流程，自动吸收归并进旧条目
        try:
            note = _auto_absorb_into_dup(payload, res["dup"])
        except Exception as e:  # noqa: BLE001
            update_batch_entry(batch_id, idx,
                               error="自动归并失败：" + str(e))
            return res
        update_batch_entry(batch_id, idx, status="done", error="", note=note,
                           item_id=res["dup"]["item"].get("id", ""),
                           file=res["dup"]["file"])
        return {"ok": True, "message": note, "merged": True}
    update_batch_entry(batch_id, idx,
                       error="自动提交失败：" + "；".join(res.get("errors", [])))
    return res


def auto_submit_batch_background(batch_id: str) -> bool:
    """后台一键自动处理：先并发跑完所有 pending（抓取+LLM 抽取），
    再把全部 review 条目逐条直接提交（跳过人工核对）。
    命中查重的条目自动吸收归并进已有日报条目后标记 done；
    intervention（待介入）条目不自动提交，仍需人工处理。已在运行则返回 False。"""
    with _RUNNING_LOCK:
        if batch_id in _RUNNING_BATCHES:
            return False
        _RUNNING_BATCHES.add(batch_id)

    def run():
        try:
            batch = load_batch(batch_id)
            if not batch:
                return
            pending = [e["idx"] for e in batch["entries"] if e.get("status") == "pending"]
            with ThreadPoolExecutor(max_workers=BATCH_WORKERS,
                                    thread_name_prefix=f"batch-{batch_id[:8]}") as ex:
                list(ex.map(lambda i: process_one_entry(batch_id, i), pending))
            # 重新加载：抽取完成后把全部 review 条目逐条提交
            # （同一日报文件为读-改-写，必须串行；do_submit 内部有 _SUBMIT_LOCK）
            batch = load_batch(batch_id) or {"entries": []}
            for e in batch["entries"]:
                if e.get("status") == "review":
                    submit_review_entry(batch_id, e["idx"])
        finally:
            with _RUNNING_LOCK:
                _RUNNING_BATCHES.discard(batch_id)

    threading.Thread(target=run, daemon=True).start()
    return True


# ============================================================
# 路由
# ============================================================
@app.route("/")
def index():
    # 支持 /?batch=<bid>&idx=<i>：从批处理会话预填某条 raw
    batch_id = (request.args.get("batch") or "").strip()
    idx_raw = (request.args.get("idx") or "").strip()
    batch_ctx = None
    if batch_id and idx_raw.isdigit():
        batch = load_batch(batch_id)
        if batch:
            idx = int(idx_raw)
            entry = next((e for e in batch["entries"] if e.get("idx") == idx), None)
            if entry:
                # 打开页时若仍是 pending，则同步自动处理一次 → review/intervention
                if entry.get("status") == "pending":
                    process_one_entry(batch_id, idx)
                    entry = next((e for e in (load_batch(batch_id) or {}).get("entries", [])
                                  if e.get("idx") == idx), entry)
                total = len(batch["entries"])
                batch_ctx = {
                    "batch_id": batch_id,
                    "idx": idx,
                    "total": total,
                    "raw": entry.get("raw", ""),
                    "status": entry.get("status", "pending"),
                    "data": entry.get("data") or {},
                    "error": entry.get("error") or "",
                    "resolved_links": entry.get("resolved_links") or [],
                    "unresolved_links": entry.get("unresolved_links") or [],
                }
    return render_template("index.html", topics=valid_topics(),
                           research=valid_research(), batch=batch_ctx)


@app.route("/api/topics")
def api_topics():
    return jsonify({"topics": valid_topics()})


@app.route("/api/research")
def api_research():
    return jsonify({"research": valid_research()})


_SUBMIT_LOCK = threading.Lock()  # 串行化日报文件的读-改-写（自动提交与手动提交并发时）


def do_submit(data: dict):
    """执行单条提交（校验 → 建主题 → 写入日报），返回 (ok, 响应 dict)。"""
    try:
        item = build_item_from_form(data)
    except ValueError as e:
        return False, {"ok": False, "errors": [str(e)]}
    target_date = item.pop("_target_date", None)

    # 校验
    errors = []
    if not item["title"]:
        errors.append("title 不能为空")
    if not item["topics"]:
        errors.append("topics 不能为空（至少选一个主题）")
    if errors:
        return False, {"ok": False, "errors": errors}

    # 主题自动扩展：选中的主题若 content/topic/ 里不存在，则自动新建
    valid = set(valid_topics())
    created_topics = []
    for t in list(item["topics"]):
        if t not in valid:
            try:
                create_topic(t)
                created_topics.append(t)
                valid.add(t)
            except Exception as e:  # noqa: BLE001
                errors.append(f"无法创建主题「{t}」：{e}")
    if errors:
        return False, {"ok": False, "errors": errors}

    # 研究项目：固定集合，过滤掉未知项（不自动新建）
    vr = set(valid_research())
    item["research"] = [r for r in item["research"] if r in vr]

    try:
        allow_dup = bool(data.get("allow_dup"))
        with _SUBMIT_LOCK:
            # 提交前查重（与写入同锁，保证检查-追加原子性）；命中则硬阻断，可勾选允许重复放行
            dup = find_dup_for_item(item, target_date=target_date)
            if dup and not allow_dup:
                return False, {"ok": False, "errors": [
                    f"疑似重复：与 {dup['date']} 日报（{dup['file']}，id={dup['item'].get('id', '')}"
                    f"「{dup['item'].get('title', '')}」）共享链接 {dup['matched_url']}。"
                    "可到 /dedup 页归并；确要保留请勾选「允许重复提交」。"], "dup": dup}
            path = append_item(item, target_date)
    except Exception as e:  # noqa: BLE001
        return False, {"ok": False, "errors": [f"写入失败：{e}"]}

    rel = path.relative_to(REPO_ROOT)
    msg = f"已追加到 {rel}（id={item['id']}）"
    if created_topics:
        msg += f"；新建主题：{created_topics}"
    if dup and allow_dup:
        msg += f"；⚠ 已允许与 {dup['date']}（id={dup['item'].get('id', '')}）重复提交"
    # 防抖触发部署：内容已落库，稍后自动 commit+push 触发 CI 重建索引
    trigger_deploy(f"提交条目 {item['id']} → {rel}")
    return True, {
        "ok": True,
        "item": item,
        "file": str(rel),
        "created_topics": created_topics,
        "message": msg,
    }


@app.route("/api/submit", methods=["POST"])
def api_submit():
    data = request.get_json(force=True, silent=True) or {}
    ok, res = do_submit(data)
    return jsonify(res), (200 if ok else 400)


@app.route("/api/resolve_links", methods=["POST"])
def api_resolve_links():
    """解析原始文本中的链接并尝试抓取，返回每个链接的状态。
    抓取到的正文不在此处返回（避免前端意外写入笔记），仅返回标题/字数等元信息；
    抓取失败的链接由前端引导用户手动补充。"""
    data = request.get_json(force=True, silent=True) or {}
    raw = (data.get("raw") or "").strip()
    if not raw:
        return jsonify({"ok": False, "errors": ["raw 不能为空"]}), 400
    resolved, unresolved, _ = resolve_all(raw)
    status = []
    for u, k in detect_links(raw):
        hit = next((r for r in resolved if r["url"] == u), None)
        miss = next((r for r in unresolved if r["url"] == u), None)
        if hit:
            status.append({"url": u, "kind": k, "ok": True,
                           "title": hit["title"], "chars": hit["chars"]})
        else:
            status.append({"url": u, "kind": k, "ok": False,
                           "reason": (miss["reason"] if miss else "抓取失败")})
    return jsonify({
        "ok": True,
        "links": status,
        "resolved": resolved,
        "unresolved": unresolved,
    })


@app.route("/merge")
def merge_page():
    return render_template("merge.html")


@app.route("/api/merge/index")
def api_merge_index():
    return jsonify({"ok": True, **parse_updates_index()})


def _merge_payload():
    data = request.get_json(force=True, silent=True) or {}
    return (data.get("topic_sources") or [], (data.get("topic_target") or "").strip(),
            data.get("sub_sources") or [], (data.get("sub_target") or "").strip())


@app.route("/api/merge/preview", methods=["POST"])
def api_merge_preview():
    ts, tt, ss, st = _merge_payload()
    if not ((ts and tt) or (ss and st)):
        return jsonify({"ok": False, "errors": ["请至少选择若干主题或子主题并填写对应目标名"]}), 400
    return jsonify({"ok": True, "summary": merge_preview(ts, tt, ss, st)})


@app.route("/api/merge/apply", methods=["POST"])
def api_merge_apply():
    ts, tt, ss, st = _merge_payload()
    res = merge_apply(ts, tt, ss, st)
    if res.get("ok"):
        trigger_deploy(f"主题归并 → {tt or st}")
    code = 200 if res.get("ok") else 400
    return jsonify(res), code


def _merge_multi_payload():
    """从请求读取批量归并组：{topic_groups:[{sources,target}], sub_groups:[...]}。"""
    data = request.get_json(force=True, silent=True) or {}
    return data.get("topic_groups") or [], data.get("sub_groups") or []


@app.route("/api/merge/preview_multi", methods=["POST"])
def api_merge_preview_multi():
    tg, sg = _merge_multi_payload()
    topic_map, sub_map = _maps_from_groups(tg, sg)
    if not topic_map and not sub_map:
        return jsonify({"ok": False, "errors": ["未提供有效归并组（每组需 ≥2 source 且有 target）"]}), 400
    return jsonify({"ok": True, "summary": merge_report_maps(topic_map, sub_map)})


@app.route("/api/merge/apply_multi", methods=["POST"])
def api_merge_apply_multi():
    tg, sg = _merge_multi_payload()
    topic_map, sub_map = _maps_from_groups(tg, sg)
    res = merge_apply_maps(topic_map, sub_map)
    if res.get("ok"):
        trigger_deploy("批量主题归并")
    code = 200 if res.get("ok") else 400
    return jsonify(res), code


@app.route("/api/merge/suggest", methods=["POST"])
def api_merge_suggest():
    return jsonify(merge_suggest())


@app.route("/dedup")
def dedup_page():
    return render_template("dedup.html")


def _dedup_days_param(data: dict):
    """解析并校验 days 参数（缺省 7，clamp 1..90）。返回 (days, None) 或 (None, 错误响应)。"""
    raw = data.get("days")
    if raw is None or raw == "":
        days = 7
    else:
        try:
            days = int(raw)
        except (TypeError, ValueError):
            return None, (jsonify({"ok": False, "errors": ["days 必须是整数"]}), 400)
    if not 1 <= days <= 90:
        return None, (jsonify({"ok": False, "errors": ["days 需在 1..90 之间"]}), 400)
    return days, None


@app.route("/api/dedup/preview", methods=["POST"])
def api_dedup_preview():
    """扫描窗口内重复条目组（纯读不写）。body: {days}，窗口 = 今天向前 days 天。"""
    data = request.get_json(force=True, silent=True) or {}
    days, err = _dedup_days_param(data)
    if err:
        return err
    files = daily_files_in_window(days)
    groups = scan_duplicate_groups(days)
    for g in groups:
        g.pop("merged", None)  # 内部字段，不暴露给前端
    return jsonify({
        "ok": True,
        "days": days,
        "window": {"from": files[0][0] if files else None,
                   "to": files[-1][0] if files else None,
                   "files_scanned": len(files)},
        "groups": groups,
        "group_count": len(groups),
    })


@app.route("/api/dedup/apply", methods=["POST"])
def api_dedup_apply():
    """执行去重归并。body: {days, groups?: [{file, id}], llm?: bool} ——
    groups 用于「仅执行选中组」；llm=true 时先用 LLM 合并解析字段（失败回退规则合并）。"""
    data = request.get_json(force=True, silent=True) or {}
    days, err = _dedup_days_param(data)
    if err:
        return err
    only = data.get("groups") or None
    res = apply_dedup_groups(days, only, use_llm=bool(data.get("llm")))
    code = 200 if res.get("ok") else 400
    return jsonify(res), code


@app.route("/api/rebuild", methods=["POST"])
def api_rebuild():
    """手动触发部署：立即 commit+push 触发 CI 重建站点。
    body: {force: bool} —— force=true 时即使无内容变更也空提交强制重建（改了配置/模板后用）。"""
    data = request.get_json(silent=True) or {}
    force = bool(data.get("force"))
    res = deploy_now("手动触发重建", force=force)
    return jsonify(res), (200 if res.get("ok") else 500)


@app.route("/batch/new")
def batch_new():
    """空的批处理创建页。"""
    return render_template("batch.html", batch=None)


@app.route("/batch/<batch_id>")
def batch_overview(batch_id):
    batch = load_batch(batch_id)
    if not batch:
        return ("批次不存在或已删除", 404)
    return render_template("batch.html", batch=batch)


@app.route("/api/batch/create", methods=["POST"])
def api_batch_create():
    """创建批处理会话。接受 JSON {text} 或 multipart 文件上传（字段名 file）。"""
    text = ""
    if request.content_type and "multipart/form-data" in request.content_type:
        f = request.files.get("file")
        if not f or not f.filename:
            return jsonify({"ok": False, "errors": ["未收到文件"]}), 400
        raw_bytes = f.read()
        for enc in ("utf-8", "utf-8-sig", "gbk"):
            try:
                text = raw_bytes.decode(enc)
                break
            except UnicodeDecodeError:
                continue
        else:
            return jsonify({"ok": False, "errors": ["无法识别文件编码（请存为 UTF-8）"]}), 400
    else:
        data = request.get_json(force=True, silent=True) or {}
        text = data.get("text") or ""

    entries_raw = parse_batch_entries(text)
    if not entries_raw:
        return jsonify({"ok": False, "errors": ["未解析到任何条目（用空行分隔每条）"]}), 400

    batch_id = new_batch_id()
    batch = {
        "batch_id": batch_id,
        "created_at": batch_id.split("-")[0],  # YYYY-MM-DD
        "title": f"批次 {batch_id}",
        "entries": [{"idx": i, "raw": r, "status": "pending",
                     "item_id": "", "file": ""} for i, r in enumerate(entries_raw)],
    }
    save_batch(batch)
    return jsonify({"ok": True, "batch_id": batch_id,
                    "count": len(batch["entries"])})


@app.route("/api/batch/<batch_id>")
def api_batch_status(batch_id):
    batch = load_batch(batch_id)
    if not batch:
        return jsonify({"ok": False, "errors": ["批次不存在"]}), 404
    # 返回精简状态（不含 raw / data 全文，避免总览页过大）
    return jsonify({
        "ok": True,
        "batch_id": batch["batch_id"],
        "running": batch_id in _RUNNING_BATCHES,
        "entries": [{"idx": e["idx"],
                     "preview": (e["raw"].splitlines()[0][:60] if e.get("raw") else ""),
                     "chars": len(e.get("raw", "")),
                     "status": e.get("status", "pending"),
                     "item_id": e.get("item_id", ""),
                     "file": e.get("file", ""),
                     "error": e.get("error", ""),
                     "has_unresolved": bool(e.get("unresolved_links"))}
                    for e in batch["entries"]],
    })


@app.route("/api/batch/<batch_id>/process", methods=["POST"])
def api_batch_process(batch_id):
    """后台处理批次内所有 pending 条目。"""
    if not load_batch(batch_id):
        return jsonify({"ok": False, "errors": ["批次不存在"]}), 404
    started = process_batch_background(batch_id)
    return jsonify({"ok": True, "started": started,
                    "running": batch_id in _RUNNING_BATCHES})


@app.route("/api/batch/<batch_id>/process_one", methods=["POST"])
def api_batch_process_one(batch_id):
    """同步处理单条（重置并重跑：用于「重新处理」或链接已修复后）。"""
    data = request.get_json(force=True, silent=True) or {}
    try:
        idx = int(data.get("idx"))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "errors": ["idx 无效"]}), 400
    if not load_batch(batch_id):
        return jsonify({"ok": False, "errors": ["批次不存在"]}), 404
    process_one_entry(batch_id, idx)
    return jsonify({"ok": True})


@app.route("/api/batch/<batch_id>/auto_submit", methods=["POST"])
def api_batch_auto_submit(batch_id):
    """一键自动处理：pending 条目先自动抽取，然后全部待核对条目跳过人工核对直接提交。
    待介入条目不自动提交，仍需人工处理。后台异步执行，前端轮询进度。"""
    if not load_batch(batch_id):
        return jsonify({"ok": False, "errors": ["批次不存在"]}), 404
    if batch_id in _RUNNING_BATCHES:
        return jsonify({"ok": False, "errors": ["批次正在处理中，请稍候再试"]}), 409
    started = auto_submit_batch_background(batch_id)
    return jsonify({"ok": True, "started": started,
                    "running": batch_id in _RUNNING_BATCHES})


@app.route("/api/batch/mark", methods=["POST"])
def api_batch_mark():
    """标记某条目为已提交（由单条提交成功后调用）。"""
    data = request.get_json(force=True, silent=True) or {}
    batch_id = (data.get("batch_id") or "").strip()
    idx = data.get("idx")
    try:
        idx = int(idx)
    except (TypeError, ValueError):
        return jsonify({"ok": False, "errors": ["idx 无效"]}), 400
    batch = update_batch_entry(batch_id, idx,
                               status="done",
                               item_id=(data.get("item_id") or ""),
                               file=(data.get("file") or ""))
    if not batch:
        return jsonify({"ok": False, "errors": ["批次不存在"]}), 404
    return jsonify({"ok": True})


@app.route("/api/extract", methods=["POST"])
def api_extract():
    data = request.get_json(force=True, silent=True) or {}
    res = llm_extract(data.get("raw") or "", data.get("extra") or "")
    if not res["ok"]:
        # 兼容 503（无 api_key）/ 502（LLM 调用或解析失败）/ 400（空 raw）
        errs = res.get("errors", [])
        if any("API Key" in e for e in errs):
            return jsonify({"ok": False, "errors": errs}), 503
        if any(e == "raw 不能为空" for e in errs):
            return jsonify({"ok": False, "errors": errs}), 400
        out = {"ok": False, "errors": errs}
        if "raw" in res:
            out["raw"] = res["raw"]
        return jsonify(out), 502
    return jsonify(res)


# ============================================================
# 当日推荐（逻辑在 recommend.py；模块未加载时全部 503）
# ============================================================
def _recommend_or_503():
    if recommend_mod is None:
        return jsonify({"ok": False,
                        "errors": ["recommend 模块未加载（检查 backend/recommend.py）"]}), 503
    return None


@app.route("/recommend")
def recommend_page():
    return render_template("recommend.html")


@app.route("/api/recommend/status")
def api_recommend_status():
    err = _recommend_or_503()
    if err:
        return err
    state = recommend_mod.get_state()
    cache = recommend_mod.load_cache()
    return jsonify({
        "ok": True,
        "running": state["running"],
        "phase": state["phase"],
        "has_cache": cache is not None,
        "generated_at": (cache or {}).get("generated_at", ""),
        "sources": (cache or {}).get("sources", {}),
        "errors": (cache or {}).get("errors", []),
        "credentials": recommend_mod.credentials_status(),
        "items": (cache or {}).get("items", []),
    })


@app.route("/api/recommend/collect", methods=["POST"])
def api_recommend_collect():
    """启动一次采集（公众号 + arXiv + LLM 判定，后台异步）。body: {force: bool}。"""
    err = _recommend_or_503()
    if err:
        return err
    data = request.get_json(silent=True) or {}
    started = recommend_mod.start_collection(bool(data.get("force")))
    state = recommend_mod.get_state()
    return jsonify({"ok": True, "started": started,
                    "running": state["running"]}), (409 if not started and state["running"] else 200)


@app.route("/api/recommend/credentials", methods=["GET", "POST"])
def api_recommend_credentials():
    err = _recommend_or_503()
    if err:
        return err
    if request.method == "GET":
        # 不回显 cookie 内容
        return jsonify({"ok": True, **recommend_mod.credentials_status()})
    data = request.get_json(force=True, silent=True) or {}
    res = recommend_mod.save_credentials(data.get("cookie") or "", data.get("token") or "")
    return jsonify(res), (200 if res["ok"] else 400)


@app.route("/api/recommend/to_batch", methods=["POST"])
def api_recommend_to_batch():
    """把选中的候选条目生成为批处理会话（复用现有批次基础设施与流程）。"""
    err = _recommend_or_503()
    if err:
        return err
    data = request.get_json(force=True, silent=True) or {}
    keys = data.get("keys") or []
    if not keys:
        return jsonify({"ok": False, "errors": ["未选择任何条目"]}), 400
    cache = recommend_mod.load_cache()
    if not cache:
        return jsonify({"ok": False, "errors": ["无当日推荐缓存，请先采集"]}), 400
    by_key = {it["key"]: it for it in cache.get("items", [])}
    picked = [by_key[k] for k in keys if k in by_key]
    if not picked:
        return jsonify({"ok": False, "errors": ["所选条目不在缓存中"]}), 400
    # raw 文本格式：URL 独立成行，便于批处理 llm_extract 的链接正则命中重新抓取；
    # 摘要已在 raw 中，链接抓取失败时（待介入）也有兜底信息。
    def to_raw(it):
        src = it["source"] if it["source"] == "arXiv" else f"{it['source']}（微信公众号）"
        return (f"标题：{it.get('title', '')}\n"
                f"来源：{src}\n"
                f"链接：{it.get('link', '')}\n"
                f"摘要：{(it.get('summary') or '').strip()[:800]}")
    batch_id = new_batch_id()
    batch = {
        "batch_id": batch_id,
        "created_at": batch_id.split("-")[0],
        "title": f"当日推荐 {batch_id.split('-')[0]}",
        "entries": [{"idx": i, "raw": to_raw(it), "status": "pending",
                     "item_id": "", "file": ""} for i, it in enumerate(picked)],
    }
    save_batch(batch)
    return jsonify({"ok": True, "batch_id": batch_id,
                    "count": len(batch["entries"])})


if __name__ == "__main__":
    print("=" * 60)
    if load_api_key():
        print(f"✓ 已加载 API Key（{API_KEY_FILE.relative_to(REPO_ROOT)}），LLM 抽取可用")
    else:
        print(f"✗ 未找到 {API_KEY_FILE.relative_to(REPO_ROOT)}：LLM 抽取不可用，")
        print("  请在仓库根目录创建该文件并填入 api_key（已被 git 忽略）。")
    print(f"✓ 合法主题 {len(valid_topics())} 个")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5050, debug=True)
