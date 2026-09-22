"""
LLM-DailyDigest 单条消息提交后端（本地工具）

功能：
  GET  /              交互式填写表单
  GET  /api/topics    返回 content/topic/ 下的合法主题名
  POST /api/extract   用 LLM 从原始文本抽取结构化字段（JSON）
  POST /api/submit    把一条 item 追加到当日日报 content/updates/<date>.md 的 [[items]]
  POST /api/batch/<id>/auto_submit  一键自动处理批次：抽取后跳过人工核对直接提交；疑似重复自动归并
  GET  /recommend     当日推荐页（采集公众号 + arXiv 指定时间窗口内容，默认最近 24h，LLM 相关性筛选）
  GET  /dedup         条目去重归并页（URL 判重，预览 + 应用两步）
  POST /api/dedup/preview|apply  去重扫描 / 执行（days 默认 7，可指定 14、30 等更大窗口）
  POST /api/finalize  当日整备：URL+语义去重（LLM 判同一工作，自动应用）→ 重生成日报头部摘要
                      （幂等，可重复执行）。批次自动提交完成后自动执行一次；
                      单条提交后防抖执行（FINALIZE_DEBOUNCE 秒，默认 600）
  GET  /merge         主题/子主题归并页；LLM 推荐为主题、子主题分开的全量分批遍历
  POST /api/merge/suggest/start  启动一种标签（topics/subtopics）的推荐后台任务
  GET  /api/merge/suggest/status 查询推荐任务进度与结果（人工采纳后才写盘）
  POST /api/export/link     抓取链接完整内容并保存为 md 文件（body: {url, out_dir}）
  POST /api/export/research 研究介绍页 + 全部相关日报条目集成导出为单个 md
                            （body: {name, out_dir}；name 不区分大小写，
                             不存在的研究名 → 全部研究统一集成导出）
  外部项目也可直接 import 本模块调用 export_link_to_md / export_research_to_md。

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


# 抽取 prompt 用的常用标签词表（带频次、短 TTL 缓存：批处理并发高，避免每条都全量扫盘）
_VOCAB_CACHE = {"ts": 0.0, "data": None}
_VOCAB_TTL = 300  # 秒；归并执行后会主动失效
_VOCAB_LOCK = threading.Lock()


def label_vocab():
    """返回 {"topics": [名称,...], "subs": [名称,...]}，均按使用频次降序。
    只收出现 ≥2 次的标签：一次性标签多为待归并噪声，不应鼓励模型复用。"""
    now = time.time()
    with _VOCAB_LOCK:
        cached = _VOCAB_CACHE["data"]
        if cached is not None and now - _VOCAB_CACHE["ts"] < _VOCAB_TTL:
            return cached
    idx = parse_updates_index()

    def common(freq):
        pairs = [(k, v) for k, v in freq.items() if v >= 2 and k and k != "(无)"]
        pairs.sort(key=lambda kv: (-kv[1], kv[0]))
        return [k for k, _ in pairs[:800]]

    data = {"topics": common(idx["topic_freq"]), "subs": common(idx["sub_freq"])}
    with _VOCAB_LOCK:
        _VOCAB_CACHE["ts"] = now
        _VOCAB_CACHE["data"] = data
    return data


def invalidate_label_vocab():
    with _VOCAB_LOCK:
        _VOCAB_CACHE["ts"] = 0.0
        _VOCAB_CACHE["data"] = None


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
# absorb_items 规则拼接标记的前缀；解析字段出现它说明需要 LLM 整合
_MERGE_TAG_PREFIX = "[合并自"


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


# notes 原始笔记内的 arXiv / GitHub 链接提取（信源常把论文链接留在正文而未填入
# paper 字段，提取后可让「同一工作、不同信源」的条目共享硬证据 key）
_ARXIV_ID_IN_TEXT_RE = re.compile(
    r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5}|[a-z-]+/[0-9]{7})", re.I)
_GITHUB_REPO_IN_TEXT_RE = re.compile(r"github\.com/([\w.-]+)/([\w.-]+)", re.I)
_GITHUB_NON_REPO_OWNERS = {"features", "topics", "orgs", "search", "settings",
                           "site", "about", "collections", "sponsors", "marketplace"}


def item_url_keys(item: dict) -> set:
    """item 参与去重的规范化 key 集合：四个 URL 字段 + notes 里出现的
    arXiv / GitHub 链接。空集合的条目永不参与去重。"""
    keys = set()
    for f in _URL_FIELDS:
        k = normalize_url(item.get(f, "") or "")
        if k:
            keys.add(k)
    notes = item.get("notes", "") or ""
    for m in _ARXIV_ID_IN_TEXT_RE.finditer(notes):
        keys.add(f"https://arxiv.org/abs/{m.group(1).lower()}")
    for m in _GITHUB_REPO_IN_TEXT_RE.finditer(notes):
        owner = m.group(1)
        repo = re.sub(r"\.git$", "", m.group(2)).rstrip(".")
        if repo and owner.lower() not in _GITHUB_NON_REPO_OWNERS:
            keys.add(f"https://github.com/{owner}/{repo}")
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


def apply_dedup_groups(days: int, only=None, use_llm=True, end_date=None) -> dict:
    """执行条目去重归并写盘。only=[{file,id}] 时仅归并保留条目匹配的组；
    use_llm=True 时先用 LLM 合并各组的解析字段（summary/content/purpose），
    失败的组回退规则合并；end_date 指定窗口截止日（默认今天）。
    锁序固定 _SUBMIT_LOCK → _MERGE_LOCK（do_submit 只取
    前者、merge_apply 只取后者，无环不死锁）。LLM 调用慢，在锁外完成；
    锁内重新扫描并校验各组未被并发修改（签名不一致的组跳过）。"""
    groups = scan_duplicate_groups(days, end_date)
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
        fresh_sigs = {sig(x) for x in scan_duplicate_groups(days, end_date)}
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


# ============================================================
# 当日整备（finalize）：URL 去重 → LLM 语义去重 → 重生成头部摘要
# 幂等设计：每步基于文件当前状态全量重算（去重收敛、摘要整块替换），
# 一天内批处理 / 当日推荐多次提交后重复执行，结果自然收敛。
# ============================================================
_SUMMARY_START = "<!-- daily-summary:start -->"
_SUMMARY_END = "<!-- daily-summary:end -->"
_FINALIZE_DEBOUNCE = float(os.environ.get("FINALIZE_DEBOUNCE", "600"))
_FINALIZE_RUN_LOCK = threading.Lock()   # 同一时刻只跑一个 finalize，避免重复 LLM 开销
_FINALIZE_STATE = {"timer": None, "dates": set()}
_FINALIZE_STATE_LOCK = threading.Lock()


def parse_day_items(d: str):
    """解析某日日报的全部条目，返回 [(块下标, item), ...]（解析失败的块跳过）。"""
    path = today_daily_path(d)
    if not path.exists():
        return []
    _, fm_body, _ = split_front_matter(path.read_text(encoding="utf-8"))
    if not fm_body:
        return []
    _, blocks = split_item_blocks(fm_body)
    out = []
    for idx, block in enumerate(blocks):
        item = _parse_item_block(block)
        if item:
            out.append((idx, item))
    return out


def _llm_chat(system_prompt: str, user_payload, want_json=False, retries: int = 2):
    """调用 LLM 返回文本（want_json=True 时解析为 JSON）。去代码块围栏；
    调用失败或 JSON 解析失败均退避重试，仍失败上抛。"""
    from openai import OpenAI
    api_key = load_api_key()
    if not api_key:
        raise RuntimeError("未找到 API Key")
    client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
    user = user_payload if isinstance(user_payload, str) \
        else json.dumps(user_payload, ensure_ascii=False)
    last = None
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[{"role": "system", "content": system_prompt},
                          {"role": "user", "content": user}],
            )
            raw = (resp.choices[0].message.content or "").strip()
            raw = re.sub(r"^```(?:json|markdown)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            return json.loads(raw) if want_json else raw
        except Exception as e:  # noqa: BLE001
            last = e
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
    raise last


def llm_semantic_day_groups(day_items: list) -> list:
    """LLM 对单日条目做语义查重：找出「同一工作/事件因不同信源被重复收录」的条目组。
    返回 [{"ids": [...], "evidence": "..."}]；失败抛异常。"""
    entries = []
    for _idx, it in day_items:
        entries.append({
            "id": it.get("id", ""),
            "标题": it.get("title", ""),
            "摘要": it.get("summary", "") or "",
            "来源": it.get("source", "") or "",
            "论文": it.get("paper", "") or "",
            "代码": it.get("code", "") or "",
            "原文": it.get("link", "") or "",
        })
    system_prompt = (
        "你是大模型研究日报的查重助手。输入为同一天日报的全部条目（id、标题、摘要、来源、链接）。"
        "任务：找出「指向同一项工作或同一事件」的条目组——同一篇论文、同一模型/系统发布、"
        "同一开源项目、同一新闻事件，因来自不同信源、表述不同而被重复收录。\n"
        "判定规则：\n"
        "1. 只有确信是同一项工作/事件才归为一组；相关、相似、同方向、同机构的【不同】工作绝不归组。\n"
        "2. 链接是硬证据：论文链接指向不同 arXiv 论文的条目不是同一工作。\n"
        "3. 综述、周报、多工作合辑类条目一律不参与归组。\n"
        "4. 拿不准就不归组：宁可漏合，不可错合。\n"
        "5. 每组给出 evidence：一句话说明判定依据（如共同的论文名/模型名/事件）。\n"
        '严格返回 JSON（不要代码块、不要解释）：{"groups": [{"ids": ["id1", "id2"], "evidence": "..."}]}；'
        '没有重复时返回 {"groups": []}。ids 只能取自输入条目的 id，每组至少 2 个。'
    )
    parsed = _llm_chat(system_prompt, entries, want_json=True)
    groups = parsed.get("groups")
    if not isinstance(groups, list):
        raise ValueError("LLM 返回缺少 groups 字段")
    return groups


def apply_semantic_groups(d: str) -> dict:
    """对某日日报执行 LLM 语义去重归并（自动应用）。
    流程：LLM 分组（锁外）→ 组内规则吸收合并 + LLM 整合解析字段（锁外）→
    锁内按 id 重新定位、基于最新条目重算合并后写盘（成员缺失的组跳过）。
    防错并护栏：组内条目 paper 字段指向 ≥2 篇不同论文时整组拒绝。"""
    path = today_daily_path(d)
    day = parse_day_items(d)
    if len(day) < 2:
        return {"ok": True, "groups": 0, "removed": 0}
    by_id = {}
    for idx, it in day:
        iid = it.get("id", "")
        if iid and iid not in by_id:
            by_id[iid] = (idx, it)
    proposals = llm_semantic_day_groups(day)
    used, groups, rejected = set(), [], []
    for g in proposals:
        ids = [i for i in dict.fromkeys(g.get("ids") or [])
               if i in by_id and i not in used]
        if len(ids) < 2:
            continue
        papers = {k for i in ids
                  for k in [normalize_url(by_id[i][1].get("paper", "") or "")] if k}
        if len(papers) >= 2:
            rejected.append({"ids": ids, "reason": "组内 paper 指向不同论文，拒绝合并"})
            continue
        used.update(ids)
        ids.sort(key=lambda i: by_id[i][0])
        keep_id, dup_ids = ids[0], ids[1:]
        groups.append({
            "keep_id": keep_id, "dup_ids": dup_ids,
            "evidence": (str(g.get("evidence") or ""))[:200],
            "keep": {"date": d, "item": by_id[keep_id][1]},
            "dups": [{"date": d, "item": by_id[i][1]} for i in dup_ids],
            "llm_fields": {},
        })
    if not groups:
        return {"ok": True, "groups": 0, "removed": 0, "rejected": rejected}
    # LLM 整合解析字段（锁外、慢调用），失败回退规则合并结果
    llm_errors = []
    for g in groups:
        try:
            vals = llm_merge_group(g)
            for f in _LLM_MERGE_FIELDS:
                v = (vals.get(f) or "").strip() if isinstance(vals.get(f), str) else ""
                if v and _MERGE_TAG_PREFIX not in v:
                    g["llm_fields"][f] = v
        except Exception as e:  # noqa: BLE001
            llm_errors.append(f"{g['keep_id']}: {e}")
    applied, removed, skipped, evidences = 0, 0, 0, []
    with _SUBMIT_LOCK, _MERGE_LOCK:
        fresh = {}
        for idx, it in parse_day_items(d):
            iid = it.get("id", "")
            if iid and iid not in fresh:
                fresh[iid] = (idx, it)
        replace, delete = {}, set()
        for g in groups:
            member_ids = [g["keep_id"]] + g["dup_ids"]
            if any(i not in fresh for i in member_ids):
                skipped += 1
                continue
            # 基于最新条目重算规则合并，再覆盖 LLM 整合的解析字段
            merged = dict(fresh[g["keep_id"]][1])
            for i in g["dup_ids"]:
                merged = absorb_items(merged, fresh[i][1], d)
            merged.update(g["llm_fields"])
            replace[fresh[g["keep_id"]][0]] = merged
            delete |= {fresh[i][0] for i in g["dup_ids"]}
            applied += 1
            removed += len(g["dup_ids"])
            evidences.append(f"{g['keep_id']} ← {'、'.join(g['dup_ids'])}（{g['evidence']}）")
        changed = rewrite_daily_items(path, replace=replace, delete=delete) \
            if (replace or delete) else 0
    if changed:
        trigger_deploy(f"语义去重归并 {d}：{applied} 组 / 删除 {removed} 条")
    res = {"ok": True, "groups": applied, "removed": removed,
           "skipped_stale": skipped, "evidence": evidences}
    if rejected:
        res["rejected"] = rejected
    if llm_errors:
        res["llm_errors"] = llm_errors[:5]
    return res


def llm_daily_summary(d: str, day_items: list) -> str:
    """生成日报头部摘要 markdown（两节：今日概览 / 对当前研究的启发）。失败抛异常。"""
    entries = []
    for _idx, it in day_items:
        entries.append({
            "id": it.get("id", ""),
            "标题": it.get("title", ""),
            "摘要": it.get("summary", "") or "",
            "子主题": it.get("subtopic", "") or "",
            "主题": it.get("topics", []) or [],
            "研究标签": it.get("research", []) or [],
        })
    intros = []
    for n in valid_research():
        p = RESEARCH_DIR / f"{n}.md"
        body = ""
        if p.exists():
            body = _md_body_after_front_matter(p.read_text(encoding="utf-8"))
            body = re.sub(r"\s+", " ", body).strip()[:400]
        intros.append({"研究": n, "简介": body})
    system_prompt = (
        "你是大模型研究日报的每日摘要撰写助手。输入为当天日报全部条目"
        "（id、标题、摘要、主题、研究标签）和我们团队各研究项目的简介。"
        "生成放在日报最上方的摘要，markdown 格式，恰好包含以下两节：\n"
        "## 今日概览\n"
        "3~6 个要点（- 开头）：按主线聚类概括今天发生了什么，每个要点点明方向并举代表性工作，"
        "可注明条目数量；提到具体条目时用 [标题](#条目id) 锚点链接。不要逐条流水账。\n"
        "## 对当前研究的启发\n"
        "若干要点（- 开头），格式：**研究名**：一句话启发。只列今天条目确实带来关键启发的研究，"
        "无关的研究不要出现、不要硬凑；启发必须具体（哪项工作、能为该研究带来什么），一句话说清。"
        "条目的研究标签是主要依据，也可指出未打标签条目与某研究的关联。\n"
        "只输出这两节 markdown 本身：以「## 今日概览」开头，不要额外解释、不要代码块。"
    )
    out = _llm_chat(system_prompt, {"日期": d, "条目": entries, "研究项目": intros})
    if "## 今日概览" not in out:
        raise ValueError("LLM 摘要输出缺少「## 今日概览」小节")
    return out


def write_daily_summary(d: str, block_md: str) -> bool:
    """把摘要块写入日报正文（front matter 之后）：已有标记对则整块替换，
    否则追加到文末。整块替换保证幂等：重复生成时摘要始终只有一份最新版。"""
    path = today_daily_path(d)
    if not path.exists():
        return False
    body = block_md.strip().replace(_SUMMARY_START, "").replace(_SUMMARY_END, "").strip()
    block = f"{_SUMMARY_START}\n\n{body}\n\n{_SUMMARY_END}"
    with _SUBMIT_LOCK:
        text = path.read_text(encoding="utf-8")
        if _SUMMARY_START in text and _SUMMARY_END in text:
            new = re.sub(re.escape(_SUMMARY_START) + r".*?" + re.escape(_SUMMARY_END),
                         lambda _m: block, text, count=1, flags=re.S)
        else:
            new = text.rstrip("\n") + "\n\n" + block + "\n"
        if new == text:
            return False
        path.write_text(new, encoding="utf-8")
    return True


def finalize_day(d=None, use_llm=True) -> dict:
    """当日整备（幂等，可重复执行）：
    ① 当日 URL 去重（含 notes 内 arXiv/GitHub 链接提取）→ ② LLM 语义去重 →
    ③ 重生成头部摘要。先去重后摘要，保证摘要不统计重复条目；
    无 API Key 时仅做规则 URL 去重。"""
    d = d or date.today().isoformat()
    path = today_daily_path(d)
    if not path.exists():
        return {"ok": False, "date": d, "errors": [f"日报不存在：{path.name}"]}
    res = {"ok": True, "date": d, "errors": []}
    has_llm = use_llm and bool(load_api_key())
    with _FINALIZE_RUN_LOCK:
        try:
            r = apply_dedup_groups(0, use_llm=has_llm, end_date=d)
            if r.get("ok"):
                res["url_dedup"] = {"groups": r.get("groups", 0),
                                    "removed": r.get("removed", 0)}
            else:
                res["url_dedup"] = {"groups": 0, "removed": 0}
                res["errors"] += [e for e in r.get("errors", []) if "没有可归并" not in e]
        except Exception as e:  # noqa: BLE001
            res["errors"].append(f"URL 去重失败：{e}")
        if has_llm:
            try:
                res["semantic"] = apply_semantic_groups(d)
            except Exception as e:  # noqa: BLE001
                res["errors"].append(f"语义去重失败：{e}")
            try:
                day = parse_day_items(d)
                if day:
                    md = llm_daily_summary(d, day)
                    if write_daily_summary(d, md):
                        res["summary"] = "updated"
                        trigger_deploy(f"重生成日报摘要 {d}")
                    else:
                        res["summary"] = "unchanged"
            except Exception as e:  # noqa: BLE001
                res["errors"].append(f"摘要生成失败：{e}")
        else:
            res["errors"].append("无 API Key 或已禁用 LLM：跳过语义去重与摘要生成")
    return res


def _run_pending_finalize():
    with _FINALIZE_STATE_LOCK:
        dates = sorted(_FINALIZE_STATE["dates"])
        _FINALIZE_STATE["dates"].clear()
        _FINALIZE_STATE["timer"] = None
    for d in dates:
        try:
            finalize_day(d)
        except Exception as e:  # noqa: BLE001
            app.logger.warning("当日整备 %s 失败: %s", d, e)


def trigger_finalize(d=None):
    """防抖触发当日整备：短时间内多次提交合并为一次（最后一次提交后静默
    FINALIZE_DEBOUNCE 秒执行）。批次自动提交结束时会直接 finalize_now，
    并顺带清掉该日期的防抖待办，不会重复执行。"""
    d = d or date.today().isoformat()
    with _FINALIZE_STATE_LOCK:
        _FINALIZE_STATE["dates"].add(d)
        if _FINALIZE_STATE["timer"] is not None:
            _FINALIZE_STATE["timer"].cancel()
        t = threading.Timer(_FINALIZE_DEBOUNCE, _run_pending_finalize)
        t.daemon = True
        t.start()
        _FINALIZE_STATE["timer"] = t


def finalize_now(d=None) -> dict:
    """立即执行当日整备，并清除该日期的防抖待办。"""
    d = d or date.today().isoformat()
    with _FINALIZE_STATE_LOCK:
        _FINALIZE_STATE["dates"].discard(d)
        if not _FINALIZE_STATE["dates"] and _FINALIZE_STATE["timer"] is not None:
            _FINALIZE_STATE["timer"].cancel()
            _FINALIZE_STATE["timer"] = None
    return finalize_day(d)


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
    invalidate_label_vocab()  # 标签已改写，抽取词表立即重建
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


# ---- LLM 归并推荐：主题 / 子主题分开、每次全量分批遍历、映射到标准术语 ----
# 每批交给 LLM 的标签数。批内互相归并 + 复用已确立标准词表，
# 顺序遍历完所有批次即保证每个标签都被 LLM 审视过一次（完整遍历）。
_SUGGEST_CHUNK = 120
_SUGGEST_JOBS = {}        # kind("topics"/"subtopics") -> 任务状态字典
_SUGGEST_JOBS_LOCK = threading.Lock()

_SUGGEST_KIND_DESC = {
    "topics": (
        "主题（topic）标签：条目的研究方向 / 技术领域标签，一条内容可带多个，粒度较宽",
        "「强化学习」「多模态」「智能体」「检索增强生成」「模型评估」「数据合成」",
    ),
    "subtopics": (
        "子主题（subtopic）标签：比主题细一级的具体方向，每条内容只有一个，粒度较细",
        "「数学推理」「奖励建模」「形式化证明」「视频生成」「模型发布」",
    ),
}


def _suggest_chunk_call(client, kind: str, vocab: set, chunk_pairs: list) -> dict:
    """单批调用：把本批每个标签映射到标准词。返回 {标签: 标准词}，失败抛异常。"""
    desc, examples = _SUGGEST_KIND_DESC[kind]
    system_prompt = (
        f"你是科研日报的标签标准化助手。下面是{desc}。"
        "任务：把【本批标签】逐一映射到规范的标准词。规则：\n"
        f"1. 标准词必须是专用技术名词或学界公认的研究方向代名词（如 {examples}），"
        "避免口语化、含糊或自造的说法。\n"
        "2. 同义、近义、中英混写、繁简、单复数、写法差异的标签必须映射到同一个标准词；"
        "优先复用【已确立标准词】里已有的词。\n"
        "3. 标签本身已是规范术语且无同义词时，映射到它自己。\n"
        "4. 标签不够规范但存在公认术语时，映射到该术语（词表里还没有也可以）。\n"
        "5. 含义确实不同（哪怕相关）的标签不要合并；宁可保留，不要错并。\n"
        '严格返回 JSON（不要代码块、不要解释）：{"map": {"标签": "标准词", ...}}。'
        "map 必须覆盖【本批标签】中的每一个标签，一个都不能漏。"
    )
    user_prompt = (
        f"【已确立标准词】{json.dumps(sorted(vocab), ensure_ascii=False)}\n\n"
        f"【本批标签】（名称, 出现次数）：{json.dumps(chunk_pairs, ensure_ascii=False)}"
    )
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": user_prompt}],
    )
    raw = (resp.choices[0].message.content or "").strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    parsed = json.loads(raw)
    m = parsed.get("map")
    if not isinstance(m, dict):
        raise ValueError("LLM 返回缺少 map 字段")
    return {str(k): str(v) for k, v in m.items()}


def _clean_canonical(label: str, tgt: str) -> str:
    """清洗 LLM 给出的标准词；不可用时回退为原标签（等于不改）。"""
    tgt = re.sub(r"\s+", " ", (tgt or "").strip())
    tgt = re.sub(r"[\\/]+", "", tgt).replace("'", "").replace('"', "")
    if not tgt or tgt in (".", "..") or len(tgt) > 40:
        return label
    return tgt


def _resolve_chains(mapping: dict) -> dict:
    """消解链式映射（A→B、B→C ⇒ A→C），遇环则保持原标签不动。"""
    def final(label, seen):
        tgt = mapping.get(label, label)
        if tgt == label or tgt in seen:
            return tgt
        seen.add(label)
        return final(tgt, seen)
    return {src: final(src, set()) for src in mapping}


def _suggest_groups(mapping: dict, freq: dict) -> list:
    """把 标签→标准词 映射整理成按目标聚合的推荐组，按影响条目数降序。"""
    mapping = _resolve_chains(mapping)
    by_tgt = {}
    for src, tgt in mapping.items():
        if src != tgt:
            by_tgt.setdefault(tgt, set()).add(src)
    groups = []
    for tgt, srcs in by_tgt.items():
        srcs = sorted(srcs, key=lambda s: (-freq.get(s, 0), s))
        refs = sum(freq.get(s, 0) for s in srcs) + freq.get(tgt, 0)
        is_new = tgt not in freq
        reason = ("统一为标准词（当前尚无此标签）" if is_new else "归并到既有标准词") \
            + f"，合计 {refs} 次引用"
        groups.append({"sources": srcs, "target": tgt, "reason": reason,
                       "new_target": is_new, "refs": refs})
    groups.sort(key=lambda g: -g["refs"])
    return groups


def _run_suggest_job(kind: str):
    """后台线程：对某一种标签做全量分批遍历，结果写回 _SUGGEST_JOBS[kind]。"""
    job = _SUGGEST_JOBS[kind]
    try:
        from openai import OpenAI
        api_key = load_api_key()
        if not api_key:
            raise RuntimeError("未找到 API Key，无法调用 LLM")
        idx = parse_updates_index()
        freq = idx["topic_freq"] if kind == "topics" else idx["sub_freq"]
        freq = {k: v for k, v in freq.items() if k and k != "(无)"}
        # 高频在前：先确立高频锚点词，低频/孤立标签在后续批次向其靠拢
        labels = sorted(freq, key=lambda k: (-freq[k], k))
        chunks = [labels[i:i + _SUGGEST_CHUNK]
                  for i in range(0, len(labels), _SUGGEST_CHUNK)]
        job["progress"] = {"done": 0, "total": len(chunks)}
        client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
        mapping, vocab, warnings = {}, set(), []
        for ci, chunk in enumerate(chunks):
            pairs = [(l, freq[l]) for l in chunk]
            m, err = None, None
            for _attempt in range(2):
                try:
                    m = _suggest_chunk_call(client, kind, vocab, pairs)
                    break
                except Exception as e:  # noqa: BLE001
                    err = e
            if m is None:
                warnings.append(f"第 {ci + 1} 批 LLM 调用失败，该批标签按原样保留：{err}")
                m = {}
            missing = sum(1 for l in chunk if l not in m)
            if m and missing:
                warnings.append(f"第 {ci + 1} 批有 {missing} 个标签未被 LLM 覆盖，按原样保留")
            for l in chunk:
                tgt = _clean_canonical(l, m.get(l, l))
                mapping[l] = tgt
                vocab.add(tgt)
            job["progress"]["done"] = ci + 1
        groups = _suggest_groups(mapping, freq)
        job["result"] = {
            "groups": groups,
            "total_labels": len(labels),
            "changed_labels": sum(1 for s, t in _resolve_chains(mapping).items() if s != t),
        }
        job["warnings"] = warnings
        job["status"] = "done"
    except Exception as e:  # noqa: BLE001
        job["errors"] = [f"{e}"]
        job["status"] = "error"


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
    if "aiera.com.cn" in u:
        return "aiera"
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
            code = e.response.status_code if e.response is not None else 0
            if code and code < 500 and code != 429:
                raise  # 4xx 重试无意义（429 限流除外，退避后可自愈）
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


# arXiv 全局限速：API 官方要求 ≥3 秒/请求，abs 网页也按 1 秒/请求自我约束
# （批处理 100 并发同时打同一主机会触发限流封禁，封禁期直连+代理同封）。
# 锁内只做起跑间隔控制后立即释放，不在锁内等待响应，避免慢请求拖住整个队列。
_ARXIV_API_LOCK = threading.Lock()
_ARXIV_API_LAST = [0.0]
_ARXIV_WEB_LOCK = threading.Lock()
_ARXIV_WEB_LAST = [0.0]

# arXiv API 熔断：连续失败达到阈值后，冷却期内直接走 abs 页面降级。
# 计数竞态最多导致熔断早/晚触发一次，无碍正确性，不加锁。
_ARXIV_API_BREAKER = {"fails": 0, "until": 0.0}
_ARXIV_BREAKER_THRESHOLD = 3
_ARXIV_BREAKER_COOLDOWN = 600.0


def _paced_get(url: str, lock: threading.Lock, last: list, interval: float,
               retries: int = 3, **kw):
    """全局限速 GET：同一 (lock, last) 组的请求起跑间隔 ≥ interval 秒。"""
    with lock:
        wait = interval - (time.monotonic() - last[0])
        if wait > 0:
            time.sleep(wait)
        last[0] = time.monotonic()
    return _http_get(url, retries=retries, **kw)


def _arxiv_api_get(api_url: str, retries: int = 3):
    return _paced_get(api_url, _ARXIV_API_LOCK, _ARXIV_API_LAST, 3.0, retries=retries)


def fetch_arxiv_abs_page(arxiv_id: str) -> dict:
    """直接解析 arxiv.org/abs 页面的 citation_* meta 标签，
    作为 Atom API 被限流/封禁时的降级通道（网页与 API 是不同基础设施，
    API 封禁期间 abs 页面通常仍可达）。"""
    r = _paced_get(f"https://arxiv.org/abs/{arxiv_id}",
                   _ARXIV_WEB_LOCK, _ARXIV_WEB_LAST, 1.0)
    soup = BeautifulSoup(r.text, "html.parser")

    def meta(name):
        t = soup.find("meta", attrs={"name": name})
        return (t.get("content") or "").strip() if t else ""

    title = meta("citation_title")
    abstract = re.sub(r"\s+", " ", meta("citation_abstract"))
    if not title or not abstract:
        raise ValueError("arXiv abs 页未解析出标题/摘要（可能被反爬拦截或 id 无效）")
    authors = [(t.get("content") or "").strip()
               for t in soup.find_all("meta", attrs={"name": "citation_author"})]
    pdf = meta("citation_pdf_url")
    text = (f"标题：{title}\n作者：{', '.join(authors)}\n"
            f"PDF：{pdf}\n摘要：{abstract}")
    return {"title": title, "text": text}


def fetch_arxiv(url: str, retries: int = 3) -> dict:
    """通过 arxiv Atom API 取标题/作者/摘要；API 失败（限流/封禁）时
    降级解析 arxiv.org/abs 页面。连续失败触发熔断后一段时间内直接走降级，
    避免封禁期每条链接死等 API 超时、且持续请求延长封禁。"""
    m = re.search(r"(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?|[a-z\-]+/[0-9]{7}(?:v\d+)?)", url)
    if not m:
        m = re.search(r"/([^/?#]+(?:v\d+)?)$", url)
    if not m:
        raise ValueError("无法从 URL 解析 arxiv id")
    arxiv_id = m.group(1)
    api = f"https://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"
    br = _ARXIV_API_BREAKER
    if time.monotonic() < br["until"]:
        return fetch_arxiv_abs_page(arxiv_id)
    try:
        resp = _arxiv_api_get(api, retries=retries)
    except Exception:  # noqa: BLE001  # 仅网络/HTTP 层失败计入熔断
        br["fails"] += 1
        if br["fails"] >= _ARXIV_BREAKER_THRESHOLD:
            br["until"] = time.monotonic() + _ARXIV_BREAKER_COOLDOWN
            br["fails"] = 0
        return fetch_arxiv_abs_page(arxiv_id)
    br["fails"] = 0
    soup = BeautifulSoup(resp.text, "html.parser")
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


def fetch_github(url: str, readme_limit: int = 4000) -> dict:
    """GitHub API 取仓库描述 + raw README（默认节选，可调大 readme_limit 取全文）。
    环境变量 GITHUB_TOKEN 存在时带上鉴权（未鉴权 API 限额仅 60 次/小时）；
    API 失败（限流等）但 README 已到手时，降级为仅用 README。"""
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)", url)
    if not m:
        raise ValueError("非标准 github 仓库 URL")
    owner, repo = m.group(1), m.group(2).rstrip(".git")
    readme = ""
    try:
        rr = _http_get(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md")
        readme = _clean_text(rr.text, readme_limit)
    except Exception:  # noqa: BLE001
        pass
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        resp = _http_get(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
        meta = resp.json()
    except Exception:  # noqa: BLE001
        if not readme:
            raise
        return {"title": f"{owner}/{repo}",
                "text": f"仓库：{owner}/{repo}\nREADME（节选）：\n{readme}"}
    desc = meta.get("description") or ""
    topics = meta.get("topics") or []
    stars = meta.get("stargazers_count")
    homepage = meta.get("homepage") or ""
    text = (f"仓库：{owner}/{repo}\n描述：{desc}\nStars：{stars}\n"
            f"Topics：{', '.join(topics)}\nHomepage：{homepage}\nREADME（节选）：\n{readme}")
    return {"title": f"{owner}/{repo}", "text": text}


def fetch_wechat(url: str, limit: int = 6000) -> dict:
    """微信公众号文章：定位 #js_content 正文。"""
    r = _http_get(url)
    r.encoding = r.apparent_encoding or "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    h = soup.find("h1") or soup.find("title")
    title = h.get_text(strip=True) if h else ""
    body = soup.select_one("#js_content") or soup.select_one(".rich_media_content")
    if body is None:
        raise ValueError("未定位到微信正文（可能需要验证或非文章页）")
    text = _clean_text(body.get_text("\n", strip=True), limit)
    return {"title": title, "text": f"标题：{title}\n正文：{text}"}


def fetch_hf_paper_page(url: str, limit: int = 6000) -> dict:
    """直接解析 HF 论文页（h1 标题 + p.text-gray-600 完整摘要），
    作为 arXiv API 被限流/封禁时的降级通道。"""
    r = _http_get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else ""
    abs_p = soup.find("p", class_="text-gray-600")
    abstract = abs_p.get_text(" ", strip=True) if abs_p else ""
    if not title or not abstract:
        raise ValueError("HF 论文页未解析出标题/摘要（页面结构可能已变化）")
    text = _clean_text(f"标题：{title}\n摘要：{abstract}", limit)
    return {"title": title, "text": text}


def fetch_hf(url: str, limit: int = 6000) -> dict:
    """HuggingFace 链接：
    - /papers/<arxiv_id> → 复用 arxiv 抓取器（取标题/作者/摘要）；
      arXiv API 失败（限流/封禁）时降级为直接解析 HF 论文页
    - 其他（模型/数据集页等）→ 通用 HTML 正文抽取
    """
    m = re.search(r"huggingface\.co/papers/([^/?#]+)", url, re.IGNORECASE)
    if m:
        arxiv_id = m.group(1)
        try:
            return fetch_arxiv(f"https://arxiv.org/abs/{arxiv_id}", retries=1)
        except Exception:  # noqa: BLE001
            return fetch_hf_paper_page(f"https://huggingface.co/papers/{arxiv_id}", limit)
    return fetch_generic(url, limit)


_AIERA_FEED_JSON = "https://aiera.com.cn/asi-preview/feed.json"


def fetch_aiera(url: str, limit: int = 6000) -> dict:
    """新智元 aiera.com.cn「ASI 爆点」条目（asi-item.html?id=<id>）：
    详情页是 JS 壳，全文存于同目录 feed.json，按 id 提取。
    条目结构 {t:标题, d:[摘要], s:信源, b:[[块类型,内容],...]}，
    块类型 h=小标题 / p=段落 / i=图片（跳过）。"""
    m = re.search(r"[?&]id=([A-Za-z0-9_-]+)", url)
    if not m:
        return fetch_generic(url, limit)  # 非条目页（首页等）走通用抽取
    item_id = m.group(1)
    db = _http_get(_AIERA_FEED_JSON).json()
    it = db.get(item_id)
    if not it:
        raise ValueError(f"feed.json 中无该条目（id={item_id}，可能已滚出保留窗口）")
    title = (it.get("t") or "").strip()
    parts = []
    for blk in it.get("b") or []:
        if not (isinstance(blk, list) and len(blk) >= 2):
            continue
        kind, val = blk[0], str(blk[1]).strip()
        if kind == "h" and val:
            parts.append(f"## {val}")
        elif kind == "p" and val:
            parts.append(val)
    body = "\n\n".join(parts) or "\n".join(str(d) for d in (it.get("d") or []))
    src = (it.get("s") or "").strip()
    text = _clean_text(body, limit)
    return {"title": title,
            "text": f"标题：{title}\n来源：新智元 ASI爆点（信源：{src}）\n正文：\n{text}"}


def fetch_generic(url: str, limit: int = 6000) -> dict:
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
    text = _clean_text(node.get_text("\n", strip=True), limit)
    if len(text) < 120:
        text = _clean_text(soup.get_text("\n", strip=True), limit)
    return {"title": title, "text": f"标题：{title}\n正文：{text}"}


_FETCHERS = {"github": fetch_github, "arxiv": fetch_arxiv, "hf": fetch_hf,
             "wechat": fetch_wechat, "aiera": fetch_aiera, "web": fetch_generic}


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

    vocab = label_vocab()
    research = valid_research()
    system_prompt = (
        "你是大模型研究日报的结构化信息抽取助手。"
        "从用户提供的原始文本中抽取【一条消息】的结构化字段，严格返回 JSON（不要代码块、不要额外解释）。"
        "若文本中包含「来自链接」「用户补充内容」等参考区块，请充分利用其中信息填充字段。"
        "字段定义：\n"
        "- title: 标题，中文为主，可含英文术语，简洁。\n"
        "- subtopic: 子主题，单个短标签（2~6 字）。必须优先复用下面【已有子主题】中语义匹配的词；"
        "确实无匹配才可新建，新建必须是专用技术名词或公认的研究方向代名词，"
        "禁止口语化表述、含糊大词或自造缩写。\n"
        f"  【已有子主题】（按使用频次降序）：{json.dumps(vocab['subs'], ensure_ascii=False)}\n"
        "- topics: 所属主题数组（1~5 个），【只能】从下面常用主题词表中选取，不得自造；"
        f"按相关度从高到低排列：{json.dumps(vocab['topics'], ensure_ascii=False)}\n"
        "- suggested_topics: 仅当常用主题词表确实覆盖不了内容的核心方向时，提名最多 2 个候选新主题"
        "（须为专用技术名词或公认研究方向代名词，2~6 字中文，不与词表重复），供用户决定是否新建；"
        "绝大多数情况应返回空数组 []。\n"
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

    # 规范化 + 词表校验：模型自造的主题一律降级为候选，由人决定是否新建
    t = parsed.get("topics", [])
    t = [str(x).strip() for x in ([t] if isinstance(t, str) else t) if str(x).strip()]
    s = parsed.get("suggested_topics", [])
    s = [str(x).strip() for x in ([s] if isinstance(s, str) else s) if str(x).strip()]
    allowed = set(vocab["topics"]) | set(valid_topics())
    topics_ok, seen = [], set()
    suggested = []
    for x in t + s:
        if x in seen:
            continue
        seen.add(x)
        (topics_ok if x in allowed else suggested).append(x)
    parsed["topics"] = topics_ok
    parsed["suggested_topics"] = suggested
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
    链接抓取失败时不硬性卡死：原文本身有足够上下文（标题/摘要等）就照常
    LLM 抽取并进 review（未抓到的链接记入 note 供回看）；只有原文近乎
    光秃 URL、无内容可抽时才置 intervention 等用户补充。已 done 的条目不覆盖。"""
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
        # 原文去掉 URL 后剩余内容太少 → 无从抽取，待介入（保存链接状态供前端展示）
        context = _URL_RE.sub("", raw).strip()
        if len(context) < 40:
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
        fields = {"status": "review",
                  "data": res.get("data", {}),
                  "resolved_links": res.get("resolved_links", resolved),
                  "unresolved_links": res.get("unresolved_links", unresolved),
                  "error": "",
                  "processed_at": datetime.now().isoformat(timespec="seconds")}
        if unresolved:
            fields["note"] = ("部分链接未抓取成功，抽取仅基于原文与已抓到内容："
                              + "、".join(u["url"] for u in unresolved))
        update_batch_entry(batch_id, idx, **fields)
    else:
        update_batch_entry(batch_id, idx,
                           status="intervention",
                           resolved_links=resolved,
                           unresolved_links=unresolved,
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
    先用 /dedup 的 absorb_items 确定性规则合并；解析字段若发生拼接
    （出现 [合并自 …] 标记），与 /dedup 默认行为一致，交给 LLM 整合为
    一份连贯内容，失败回退规则结果。notes 逐字保留不经 LLM。
    LLM 调用慢，在 _SUBMIT_LOCK 外完成。"""
    item = build_item_from_form(payload)
    item.pop("_target_date", None)
    today_s = date.today().isoformat()
    merged = absorb_items(dup["item"], item, today_s)
    llm_note = ""
    if any(_MERGE_TAG_PREFIX in (merged.get(f) or "") for f in _LLM_MERGE_FIELDS):
        try:
            vals = llm_merge_group({
                "keep": {"date": dup["date"], "item": dup["item"]},
                "dups": [{"date": today_s, "item": item}],
            })
            for f in _LLM_MERGE_FIELDS:
                v = (vals.get(f) or "").strip()
                if v and _MERGE_TAG_PREFIX not in v:
                    merged[f] = v
            llm_note = "；LLM 已整合解析字段"
        except Exception as e:  # noqa: BLE001
            llm_note = f"；LLM 整合失败已回退规则合并：{e}"
    path = today_daily_path(dup["date"])
    with _SUBMIT_LOCK:
        changed = rewrite_daily_items(path, replace={dup["index"]: merged})
    if changed:
        trigger_deploy(f"自动归并条目 {item['id']} → {path.name}")
    return (f"已自动归并到 {dup['date']} 日报（{dup['file']}，"
            f"id={dup['item'].get('id', '')}）{llm_note}")


def submit_review_entry(batch_id: str, idx: int) -> dict:
    """把一条 review（待核对）条目的抽取结果直接提交写入日报。
    - notes 逐字保留原始信息 raw；
    - suggested_topics（候选新主题）自动流程默认【不】采纳，避免每条消息都扩充
      主题词表、抬高归并成本；未采纳的候选记入条目 note 供人工回看。
      仅当已有主题为空（提交会被拒）时才兜底并入候选。
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
    suggested = [str(t).strip() for t in (data.get("suggested_topics") or [])
                 if str(t).strip() and str(t).strip() not in topics]
    skipped_note = ""
    if not topics and suggested:
        topics = suggested  # 兜底：没有任何已有主题时才采纳候选，保证可提交
    elif suggested:
        skipped_note = "候选新主题未自动采纳：" + "、".join(suggested)
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
        fields = {"status": "done", "error": "",
                  "item_id": res["item"]["id"], "file": res["file"]}
        if skipped_note:
            prev = (entry.get("note") or "").strip()
            fields["note"] = f"{prev}；{skipped_note}" if prev else skipped_note
        update_batch_entry(batch_id, idx, **fields)
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
            # 全部提交完成后立即做当日整备：URL+语义去重 → 重生成摘要（幂等）
            try:
                finalize_now()
            except Exception as e:  # noqa: BLE001
                app.logger.warning("批次 %s 当日整备失败: %s", batch_id, e)
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
    # 防抖触发当日整备（语义去重 + 摘要）：零散提交静默一段时间后统一整备
    trigger_finalize(target_date)
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


@app.route("/api/merge/suggest/start", methods=["POST"])
def api_merge_suggest_start():
    """启动一种标签（topics/subtopics）的全量遍历归并推荐后台任务。"""
    data = request.get_json(force=True, silent=True) or {}
    kind = (data.get("kind") or "").strip()
    if kind not in ("topics", "subtopics"):
        return jsonify({"ok": False, "errors": ["kind 需为 topics 或 subtopics"]}), 400
    if not load_api_key():
        return jsonify({"ok": False, "errors": ["未找到 API Key，无法调用 LLM"]}), 400
    with _SUGGEST_JOBS_LOCK:
        job = _SUGGEST_JOBS.get(kind)
        if job and job.get("status") == "running":
            return jsonify({"ok": True, "already_running": True})
        _SUGGEST_JOBS[kind] = {"status": "running",
                               "progress": {"done": 0, "total": 0},
                               "result": None, "errors": [], "warnings": []}
    threading.Thread(target=_run_suggest_job, args=(kind,), daemon=True,
                     name=f"merge-suggest-{kind}").start()
    return jsonify({"ok": True})


@app.route("/api/merge/suggest/status")
def api_merge_suggest_status():
    """查询归并推荐任务状态：idle / running（含进度）/ done（含结果）/ error。"""
    kind = (request.args.get("kind") or "").strip()
    if kind not in ("topics", "subtopics"):
        return jsonify({"ok": False, "errors": ["kind 需为 topics 或 subtopics"]}), 400
    job = _SUGGEST_JOBS.get(kind)
    if not job:
        return jsonify({"ok": True, "status": "idle"})
    return jsonify({"ok": True, **job})


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
    groups 用于「仅执行选中组」；llm 默认 true，用 LLM 合并解析字段（失败回退规则合并），
    显式传 false 才纯规则合并。"""
    data = request.get_json(force=True, silent=True) or {}
    days, err = _dedup_days_param(data)
    if err:
        return err
    only = data.get("groups") or None
    res = apply_dedup_groups(days, only, use_llm=bool(data.get("llm", True)))
    code = 200 if res.get("ok") else 400
    return jsonify(res), code


@app.route("/api/finalize", methods=["POST"])
def api_finalize():
    """当日整备：URL+语义去重 → 重生成日报头部摘要（幂等，可重复执行）。
    body: {date?: "YYYY-MM-DD", llm?: bool}；date 缺省为今天。
    同步执行（含多次 LLM 调用，可能需要 1~2 分钟）。"""
    data = request.get_json(silent=True) or {}
    try:
        d = parse_target_date(data.get("date") or "")
    except ValueError as e:
        return jsonify({"ok": False, "errors": [str(e)]}), 400
    if data.get("llm", True):
        res = finalize_now(d)
    else:
        res = finalize_day(d, use_llm=False)
    return jsonify(res), (200 if res.get("ok") else 400)


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
        "window": (cache or {}).get("window", {}),
        "sources": (cache or {}).get("sources", {}),
        "errors": (cache or {}).get("errors", []),
        "credentials": recommend_mod.credentials_status(),
        "items": (cache or {}).get("items", []),
    })


@app.route("/api/recommend/collect", methods=["POST"])
def api_recommend_collect():
    """启动一次采集（公众号 + arXiv + LLM 判定，后台异步）。
    body: {force: bool, start: str, end: str}。
    start/end 为 ISO 时间（如 2026-09-06T10:00，无时区按本地），指定采集窗口；
    默认 end=当前时间、start=end 前 24h；任一指定即忽略当日缓存重新采集。"""
    err = _recommend_or_503()
    if err:
        return err
    data = request.get_json(silent=True) or {}

    def parse_dt(key):
        raw = (data.get(key) or "").strip()
        if not raw:
            return None
        try:
            dt = datetime.fromisoformat(raw)
        except ValueError:
            raise ValueError(f"{key} 时间格式无效：{raw}（应为 ISO 格式，如 2026-09-06T10:00）")
        return dt.astimezone()  # 无时区标记按本地时区

    try:
        since_dt, until_dt = parse_dt("start"), parse_dt("end")
    except ValueError as e:
        return jsonify({"ok": False, "errors": [str(e)]}), 400
    now = datetime.now().astimezone()
    if until_dt is None and since_dt is not None:
        until_dt = now
    if since_dt is not None and since_dt >= until_dt:
        return jsonify({"ok": False, "errors": ["起始时间必须早于截止时间"]}), 400
    if since_dt is not None and since_dt > now:
        return jsonify({"ok": False, "errors": ["起始时间不能晚于当前时间"]}), 400
    started = recommend_mod.start_collection(bool(data.get("force")),
                                             since_dt=since_dt, until_dt=until_dt)
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
        if it["source"] == "arXiv":
            src = it["source"]
        else:
            src = recommend_mod.SOURCE_RAW_LABELS.get(
                it["source"], f"{it['source']}（微信公众号）")
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


# ============================================================
# 导出功能（供外部项目调用：HTTP API 或直接 import 本模块调函数）
#   export_link_to_md(url, out_dir)       抓取链接完整内容并保存为 md
#   export_research_to_md(name, out_dir)  研究介绍页 + 全部相关日报条目集成为单个 md
# ============================================================
_EXPORT_FETCH_LIMIT = 200_000  # 导出时的正文截断上限（约等于不截断）


def _out_dir_path(out_dir: str) -> Path:
    """校验并创建导出目录，返回绝对 Path；不可用时抛 ValueError。"""
    if not (out_dir or "").strip():
        raise ValueError("out_dir 不能为空")
    p = Path(out_dir).expanduser()
    if not p.is_absolute():
        p = REPO_ROOT / p
    p = p.resolve()
    if p.exists() and not p.is_dir():
        raise ValueError(f"out_dir 不是目录：{p}")
    p.mkdir(parents=True, exist_ok=True)
    return p


def _export_filename_slug(title: str, url: str) -> str:
    """标题优先生成文件名 slug；纯中文标题 slug 为空时退化为 URL 路径。"""
    s = slugify(title)
    if len(s) >= 3:
        return s
    parts = urllib.parse.urlsplit(url)
    return slugify(f"{parts.netloc}-{parts.path}") or "page"


def fetch_link_full(url: str) -> dict:
    """按链接类型抓取完整内容（不走 LLM 抽取用的 6000 字符截断）。
    返回 {"kind", "title", "text"}；失败抛异常。"""
    kind = classify_link(url)
    if kind == "github":
        res = fetch_github(url, readme_limit=_EXPORT_FETCH_LIMIT)
    elif kind == "arxiv":
        res = fetch_arxiv(url)
    elif kind == "hf":
        res = fetch_hf(url, limit=_EXPORT_FETCH_LIMIT)
    elif kind == "wechat":
        res = fetch_wechat(url, limit=_EXPORT_FETCH_LIMIT)
    elif kind == "aiera":
        res = fetch_aiera(url, limit=_EXPORT_FETCH_LIMIT)
    else:
        res = fetch_generic(url, limit=_EXPORT_FETCH_LIMIT)
    return {"kind": kind, "title": res.get("title", ""), "text": res.get("text", "")}


def export_link_to_md(url: str, out_dir: str) -> dict:
    """功能一：抓取链接内容并完整保存为 md 文件。
    输入：url（http/https 链接）、out_dir（导出目录，相对路径按仓库根解析）。
    输出：{"ok": True, "file": 文件绝对路径, "kind", "title", "chars"}；
    失败：{"ok": False, "errors": [...]}。"""
    url = (url or "").strip()
    if not re.match(r"^https?://", url, re.I):
        return {"ok": False, "errors": [f"url 必须是 http(s) 链接：{url!r}"]}
    try:
        target = _out_dir_path(out_dir)
    except ValueError as e:
        return {"ok": False, "errors": [str(e)]}
    try:
        res = fetch_link_full(url)
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "errors": [f"抓取失败：{e}"]}
    import hashlib
    slug = _export_filename_slug(res["title"], url)
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
    path = target / f"link-{slug}-{digest}.md"
    fetched_at = datetime.now().isoformat(timespec="seconds")
    md = (
        f"# {res['title'] or url}\n\n"
        f"- 链接：{url}\n"
        f"- 类型：{res['kind']}\n"
        f"- 抓取时间：{fetched_at}\n\n"
        "---\n\n"
        f"{res['text']}\n"
    )
    path.write_text(md, encoding="utf-8")
    return {"ok": True, "file": str(path), "kind": res["kind"],
            "title": res["title"], "chars": len(res["text"])}


def _md_body_after_front_matter(text: str) -> str:
    """返回 md 文件 front matter 之后的正文（无 front matter 时原样返回）。"""
    _, fm_body, post = split_front_matter(text)
    if fm_body is None:
        return text.strip()
    # post 首行是闭合 +++，正文从下一行开始
    return post.split("\n", 1)[1].strip() if "\n" in post else ""


def _collect_research_items(names: list) -> dict:
    """扫描全部日报，按研究名收集相关条目：{研究名: [(日期, item), ...]}。
    匹配不区分大小写；条目按日期→文件内顺序排列。"""
    wanted = {n.lower(): n for n in names}
    out = {n: [] for n in names}
    files = sorted(glob.glob(str(UPDATES_DIR / "*.md")))
    files = [f for f in files if re.match(r"^\d{4}-\d{2}-\d{2}", Path(f).name)]
    for f in files:
        path = Path(f)
        d = path.name[:10]
        _, fm_body, _ = split_front_matter(path.read_text(encoding="utf-8"))
        if not fm_body:
            continue
        _, blocks = split_item_blocks(fm_body)
        for block in blocks:
            item = _parse_item_block(block)
            if not item:
                continue
            for r in item.get("research", []) or []:
                canon = wanted.get(str(r).strip().lower())
                if canon:
                    out[canon].append((d, item))
    return out


def _render_item_md(d: str, item: dict) -> str:
    """把单条日报 item 渲染为 markdown 小节（### 级）。"""
    lines = [f"### {item.get('title') or '(无标题)'}", ""]
    lines.append(f"- 日期：{d}")
    if item.get("id"):
        lines.append(f"- 条目 id：{item['id']}")
    if item.get("source"):
        lines.append(f"- 来源：{item['source']}")
    if item.get("subtopic"):
        lines.append(f"- 子主题：{item['subtopic']}")
    if item.get("topics"):
        lines.append("- 主题：" + "、".join(item["topics"]))
    if item.get("research"):
        lines.append("- 研究：" + "、".join(item["research"]))
    for label, f in (("论文", "paper"), ("代码", "code"),
                     ("数据集", "dataset"), ("原文", "link")):
        if (item.get(f) or "").strip():
            lines.append(f"- {label}：{item[f].strip()}")
    for label, f in (("摘要", "summary"), ("要点", "content"), ("用途与启示", "purpose")):
        v = (item.get(f) or "").strip()
        if v:
            lines += ["", f"**{label}**", "", v]
    notes = (item.get("notes") or "").strip()
    if notes:
        quoted = "\n".join("> " + ln for ln in notes.split("\n"))
        lines += ["", "**原始笔记**", "", quoted]
    return "\n".join(lines)


def export_research_to_md(name: str, out_dir: str) -> dict:
    """功能二：把某研究的介绍页 + 全部相关日报条目集成导出为单个 md。
    输入：name（研究名，不区分大小写，如 dataevolve）、out_dir（导出目录）。
    研究不存在时不报错，改为把全部研究统一集成导出为一个文件。
    输出：{"ok": True, "file": 文件绝对路径, "research": [导出的研究名],
          "matched": 是否精确命中, "items": 条目总数}；
    失败：{"ok": False, "errors": [...]}。"""
    try:
        target = _out_dir_path(out_dir)
    except ValueError as e:
        return {"ok": False, "errors": [str(e)]}
    all_names = valid_research()
    if not all_names:
        return {"ok": False, "errors": ["content/research/ 下没有任何研究页"]}
    query = (name or "").strip()
    canon = next((n for n in all_names if n.lower() == query.lower()), None) \
        if query else None
    matched = canon is not None
    selected = [canon] if matched else all_names

    items_by_research = _collect_research_items(selected)
    today = date.today().isoformat()
    sections = []
    total = 0
    for n in selected:
        page = RESEARCH_DIR / f"{n}.md"
        body = _md_body_after_front_matter(page.read_text(encoding="utf-8")) \
            if page.exists() else f"# {n}\n\n（未找到研究介绍页）"
        items = items_by_research.get(n, [])
        total += len(items)
        sec = body + f"\n\n---\n\n## 相关日报条目（{len(items)} 条）\n"
        if items:
            sec += "\n" + "\n\n---\n\n".join(_render_item_md(d, it) for d, it in items)
        else:
            sec += "\n（暂无相关日报条目）"
        sections.append(sec)

    if matched:
        path = target / f"research-{canon}-{today}.md"
        head = ""
    else:
        path = target / f"research-all-{today}.md"
        head = "# 全部研究内容汇总\n\n"
        if query:
            head += f"> 未找到研究「{query}」，已统一集成全部 {len(selected)} 个研究。\n\n"
        head += f"> 导出日期：{today}；收录研究：{'、'.join(selected)}\n\n---\n\n"
    path.write_text(head + "\n\n---\n\n".join(sections) + "\n", encoding="utf-8")
    return {"ok": True, "file": str(path), "research": selected,
            "matched": matched, "items": total}


@app.route("/api/export/link", methods=["POST"])
def api_export_link():
    """抓取链接完整内容并保存为 md。body: {url, out_dir} → {ok, file, ...}。"""
    data = request.get_json(force=True, silent=True) or {}
    res = export_link_to_md(data.get("url") or "", data.get("out_dir") or "")
    return jsonify(res), (200 if res.get("ok") else 400)


@app.route("/api/export/research", methods=["POST"])
def api_export_research():
    """研究完整内容导出。body: {name, out_dir} → {ok, file, research, matched, items}。
    name 不区分大小写；不存在的研究名 → 全部研究统一集成导出。"""
    data = request.get_json(force=True, silent=True) or {}
    res = export_research_to_md(data.get("name") or "", data.get("out_dir") or "")
    return jsonify(res), (200 if res.get("ok") else 400)


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
