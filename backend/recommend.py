"""
当日推荐采集模块（无 Flask 依赖，被 backend/app.py 导入）。

功能：
  - 微信公众号（量子位 / 机器之心 / 新智元）最近 24h 文章列表采集，四级通道按序兜底：
    1. mp.weixin.qq.com appmsg 接口（凭据存仓库根目录 wechat_credentials.json，手动更新，实时）
    2. 量子位官网直采（免凭据，实时）
    3. Wechat-Scholar RSS（免凭据，≤12h 延迟）
    4. wechat2rss 公共 RSS（免凭据，~24h 内收录）
    各 RSS/官网通道之间按标题去重
  - arXiv 最近 24h cs.CL / cs.AI / cs.LG 论文采集（export.arxiv.org Atom API）
  - 基于 content/research/*.md 的研究画像构建
  - LLM 相关性批量判定（候选分 chunk 并发打分）
  - 按日缓存到 .recommend_cache/recommend-<date>.json

各采集源相互独立：单个源失败只记录 error，不影响其他源。
"""
import json
import re
import glob
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

REPO_ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = REPO_ROOT / "content" / "research"
WECHAT_CRED_FILE = REPO_ROOT / "wechat_credentials.json"
RECOMMEND_DIR = REPO_ROOT / ".recommend_cache"

# 公众号（名称, fakeid）——fakeid 稳定不变，来自 co_learner/spider_lib/gzh.py
WECHAT_ACCOUNTS = [
    ("量子位", "MzIzNjc1NzUzMw=="),
    ("机器之心", "MzA3MzI4MjgzMw=="),
    ("新智元", "MzI3MTA0MTk1MA=="),
]
# Wechat-Scholar 学术公众号 RSS 托管服务（osnsyc/Wechat-Scholar，每日三次更新，≤12h 延迟）。
# 免凭据兜底通道；如需增删公众号，改这里即可（channels.json 见项目仓库）。
WECHAT_SCHOLAR_FEEDS = {
    "量子位": "https://raw.githubusercontent.com/osnsyc/Wechat-Scholar/main/channels/gh_114e76fd6e5d.xml",
    "机器之心": "https://raw.githubusercontent.com/osnsyc/Wechat-Scholar/main/channels/gh_dbc0a5474692.xml",
    "新智元": "https://raw.githubusercontent.com/osnsyc/Wechat-Scholar/main/channels/gh_108f2a2a27f4.xml",
}
# wechat2rss 公共托管服务（tttmr/Wechat2RSS，免凭据，~24h 内收录）。
# 与 Wechat-Scholar 相互独立的第二 RSS 兜底，两家同时断供才报警；
# feed id 来自 https://wechat2rss.xlab.app/list/all.html，私有部署见项目仓库。
WECHAT2RSS_FEEDS = {
    "量子位": "https://wechat2rss.xlab.app/feed/7131b577c61365cb47e81000738c10d872685908.xml",
    "机器之心": "https://wechat2rss.xlab.app/feed/51e92aad2728acdd1fda7314be32b16639353001.xml",
    "新智元": "https://wechat2rss.xlab.app/feed/ede30346413ea70dbef5d485ea5cbb95cca446e7.xml",
}
ARXIV_CATEGORIES = ["cs.CL", "cs.AI", "cs.LG"]
ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_PAGE_SIZE = 100
ARXIV_MAX_TOTAL = 500
# arXiv API 礼仪：UA 需含身份标识，请求间隔 ≥3s（下方分页 sleep）
ARXIV_UA = "LLM-DailyDigest/1.0 (recommendation collector; github.com/dujh22/LLM-DailyDigest)"

# LLM 配置与 app.py 保持一致（环境变量可覆盖）
import os
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api-gateway.glm.ai/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-5.6-sol")

FILTER_CHUNK = 40          # 每次 LLM 判定的候选数
FILTER_WORKERS = 8         # 判定并发数

_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_TIMEOUT = (10, 30)  # (连接超时, 读取超时)，连接超时单独收紧以便快速重试

# 采集运行状态（仿 app.py 的 _RUNNING_LOCK / _RUNNING_BATCHES 模式）
_STATE_LOCK = threading.Lock()
_RECOMMEND_RUNNING = False
_STATE = {"phase": "idle", "counts": {}, "errors": []}


def _set_state(phase=None, **kw):
    with _STATE_LOCK:
        if phase is not None:
            _STATE["phase"] = phase
        _STATE.update(kw)


def get_state() -> dict:
    with _STATE_LOCK:
        return {"running": _RECOMMEND_RUNNING, **_STATE}


def _get(url: str, params=None, headers=None, retries: int = 3):
    """带重试的 GET：本地代理瞬断（ProxyError/超时）时退避重试后可自愈。
    429（arXiv 等限速）按 Retry-After / 递增退避重试，其余 4xx 不重试。"""
    h = {"User-Agent": _UA}
    h.update(headers or {})
    last_exc = None
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, headers=h, timeout=_TIMEOUT)
            r.raise_for_status()
            return r
        except requests.HTTPError as e:
            status = e.response.status_code if e.response is not None else 0
            if status == 429:
                # 限速：优先遵守 Retry-After，缺省时递增退避（5s/15s/30s）
                wait = int(e.response.headers.get("Retry-After", 0) or 0)
                if not wait:
                    wait = 5 * (attempt + 1)
                if attempt < retries - 1:
                    time.sleep(min(wait, 60))
                    last_exc = e
                    continue
                raise
            if status < 500:
                raise  # 其余 4xx 重试无意义
            last_exc = e
        except requests.RequestException as e:  # ProxyError / 连接与读取超时
            last_exc = e
        if attempt < retries - 1:
            time.sleep(1.5 * (attempt + 1))
    raise last_exc


# ============================================================
# 微信公众号凭据
# ============================================================
def load_credentials():
    """读取 wechat_credentials.json，返回 dict 或 None。"""
    if not WECHAT_CRED_FILE.exists():
        return None
    try:
        cred = json.loads(WECHAT_CRED_FILE.read_text(encoding="utf-8"))
        if cred.get("cookie") and cred.get("token"):
            return cred
    except Exception:  # noqa: BLE001
        pass
    return None


def _appmsg_request(cred: dict, fakeid: str, begin: int, count: int):
    """调用 appmsg list_ex 接口，返回 (ret, app_msg_list, raw_json)。"""
    params = {
        "token": cred["token"], "lang": "zh_CN", "f": "json", "ajax": "1",
        "action": "list_ex", "begin": str(begin), "count": str(count),
        "query": "", "fakeid": fakeid, "type": "9",
    }
    headers = {"Cookie": cred["cookie"],
               "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3866.75 Mobile Safari/537.36"}
    r = requests.get("https://mp.weixin.qq.com/cgi-bin/appmsg",
                     params=params, headers=headers, timeout=_TIMEOUT)
    r.raise_for_status()
    j = r.json()  # 非 JSON 响应（登录页 HTML）会抛异常 → 上层按凭据失效处理
    ret = (j.get("base_resp") or {}).get("ret", -1)
    return ret, j.get("app_msg_list") or [], j


def _ret_message(ret: int, err_msg: str = "") -> str:
    """把平台 ret 码翻译成人话，区分限流与凭据过期。"""
    if ret == 200013 or "freq control" in (err_msg or ""):
        return ("接口限流（freq control）：稍等几分钟在页面重试；"
                "若持续出现，到浏览器里刷新一次公众号文章列表（触发真实 appmsg 请求）后重新复制 cookie/token")
    return f"平台返回 ret={ret}（cookie/token 大概率已过期，请重新复制）"


def test_credentials(cred: dict):
    """用一个小请求验证凭据是否有效。返回 (ok, message)。"""
    try:
        ret, msg_list, j = _appmsg_request(cred, WECHAT_ACCOUNTS[0][1], 0, 5)
    except Exception as e:  # noqa: BLE001
        return False, f"请求失败：{e}"
    if ret != 0:
        err_msg = (j.get("base_resp") or {}).get("err_msg", "")
        return False, _ret_message(ret, err_msg)
    if not msg_list:
        return False, "接口通但不返回文章列表（cookie/token 可能不完整）"
    return True, "凭据有效"


def save_credentials(cookie: str, token: str) -> dict:
    """保存并测试凭据。返回 {ok, tested_ok, message}。"""
    cookie = (cookie or "").strip()
    token = (token or "").strip()
    if not cookie or not token:
        return {"ok": False, "tested_ok": False, "message": "cookie 与 token 均不能为空"}
    cred = {"cookie": cookie, "token": token,
            "updated_at": datetime.now().isoformat(timespec="seconds")}
    ok, msg = test_credentials(cred)
    cred["tested_ok"] = ok
    WECHAT_CRED_FILE.write_text(json.dumps(cred, ensure_ascii=False, indent=2),
                                encoding="utf-8")
    return {"ok": True, "tested_ok": ok, "message": msg}


def credentials_status() -> dict:
    cred = load_credentials()
    if not cred:
        return {"configured": False, "tested_ok": False, "updated_at": ""}
    return {"configured": True,
            "tested_ok": bool(cred.get("tested_ok")),
            "updated_at": cred.get("updated_at", "")}


# ============================================================
# 采集：微信公众号
# ============================================================
def collect_wechat(cred: dict, since_ts: int) -> dict:
    """采集三个公众号最近 24h 的文章列表。
    返回 {"items": [...], "errors": [ {source, error} ]}。
    凭据失效时 errors 里带 credentials_expired=True，items 为空。"""
    items, errors = [], []
    for name, fakeid in WECHAT_ACCOUNTS:
        try:
            begin, pages = 0, 0
            while pages < 3:  # 每号每天 ~5-15 篇，3 页(×10)足够覆盖 24h
                ret, msg_list, j = _appmsg_request(cred, fakeid, begin, 10)
                if ret != 0:
                    err_msg = (j.get("base_resp") or {}).get("err_msg", "")
                    errors.append({"source": name, "error": _ret_message(ret, err_msg),
                                   "credentials_expired": ret != 200013})
                    break
                if not msg_list:
                    break
                stopped = False
                for m in msg_list:
                    ct = int(m.get("create_time") or 0)
                    if ct < since_ts:
                        stopped = True  # 列表按新→旧排序，越界即停
                        break
                    link = m.get("link") or ""
                    if not link:
                        continue
                    items.append({
                        "key": link,
                        "source": name,
                        "title": re.sub(r"<[^>]+>", "", m.get("title") or "").strip(),
                        "summary": re.sub(r"<[^>]+>", "", m.get("digest") or "").strip(),
                        "link": link,
                        "published": datetime.fromtimestamp(ct).isoformat(timespec="seconds"),
                    })
                if stopped or len(msg_list) < 10:
                    break
                begin += 10
                pages += 1
                time.sleep(2)  # 页间隔，避免触发风控
        except Exception as e:  # noqa: BLE001
            errors.append({"source": name, "error": f"采集失败：{e}",
                           "credentials_expired": True})
    return {"items": items, "errors": errors}


# ============================================================
# 采集：量子位官网（无需凭据，始终可用）
# ============================================================
QBITAI_HOME = "https://www.qbitai.com/"
_QBITAI_LINK_RE = re.compile(
    r'<a[^>]+href="(https://www\.qbitai\.com/\d{4}/\d{2}/\d+\.html)"[^>]*>(.*?)</a>', re.S)
_QBITAI_MAX = 30          # 首页最多检查的候选文章数
_QBITAI_WORKERS = 4


def _fetch_qbitai_meta(url: str):
    """抓单篇官网文章页，返回 (published_iso, summary) 或抛异常。
    日期优先取 <span class="date">(+<span class="time">)，退回 article:published_time meta。"""
    r = _get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    pub = ""
    d_span = soup.find("span", class_="date")
    if d_span:
        d = re.search(r"20\d{2}-\d{2}-\d{2}", d_span.get_text() or "")
        if d:
            pub = d.group(0)
            t_span = soup.find("span", class_="time")
            t = re.search(r"\d{1,2}:\d{2}", t_span.get_text() or "") if t_span else None
            if t:
                pub += " " + t.group(0)
    if not pub:
        m = soup.find("meta", attrs={"property": "article:published_time"})
        if m and m.get("content"):
            pub = m["content"].strip()
    summ = ""
    d_meta = soup.find("meta", attrs={"property": "og:description"}) or \
        soup.find("meta", attrs={"name": "description"})
    if d_meta and d_meta.get("content"):
        summ = re.sub(r"\s+", " ", d_meta["content"]).strip()
    return pub, summ


def collect_qbitai(since_dt: datetime) -> dict:
    """从量子位官网首页提取最近文章，抓正文页取发布时间与摘要，过滤出 since 之后。
    返回 {"items": [...], "errors": [...]}。"""
    try:
        r = _get(QBITAI_HOME)
    except Exception as e:  # noqa: BLE001
        return {"items": [], "errors": [{"source": "量子位（官网）",
                                         "error": f"官网请求失败：{e}"}]}
    # 首页提取 链接→标题（保序去重）
    seen, cands = set(), []
    for m in _QBITAI_LINK_RE.finditer(r.text):
        url, title = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if url in seen or not title or len(title) < 8:
            continue
        seen.add(url)
        cands.append({"url": url, "title": title})
    cands = cands[:_QBITAI_MAX]

    def work(c):
        try:
            pub, summ = _fetch_qbitai_meta(c["url"])
        except Exception:  # noqa: BLE001
            return None
        if not pub:
            return None
        try:
            # 形如 "YYYY-MM-DD" 或 "YYYY-MM-DD HH:MM"（官网本地时间，无时区标记 → 按本地时区）
            pub_dt = datetime.fromisoformat(pub).astimezone()
        except ValueError:
            return None
        # 只有日期（无时刻）时按日粒度比较，避免整天的文章被误排除
        has_time = ":" in pub
        if pub_dt < since_dt and not (not has_time and
                                      pub_dt.date() >= since_dt.astimezone().date()):
            return None
        return {"key": c["url"], "source": "量子位",
                "title": c["title"], "summary": summ, "link": c["url"],
                "published": pub_dt.isoformat(timespec="seconds")}

    items = []
    with ThreadPoolExecutor(max_workers=_QBITAI_WORKERS,
                            thread_name_prefix="qbitai") as ex:
        for it in ex.map(work, cands):
            if it:
                items.append(it)
    return {"items": items, "errors": []}


def _norm_title(t: str) -> str:
    """标题归一化（去空白与标点、小写），用于跨源去重。"""
    return re.sub(r"[^\w一-鿿]+", "", (t or "")).lower()


# ============================================================
# 采集：公众号 RSS 兜底（Wechat-Scholar / wechat2rss，均免凭据）
# ============================================================
def _collect_rss(feeds: dict, since_dt: datetime, label: str) -> dict:
    """拉取公众号 RSS 2.0 订阅源（stdlib ElementTree 解析），
    过滤出 since_dt 之后发布的文章。返回 {"items": [...], "errors": [...]}。"""
    import xml.etree.ElementTree as ET
    from email.utils import parsedate_to_datetime
    items, errors = [], []
    for name, url in feeds.items():
        try:
            r = _get(url)
            root = ET.fromstring(r.text)
            for it in root.iter("item"):
                t = (it.findtext("title") or "").strip()
                link = (it.findtext("link") or "").strip()
                if not t or not link:
                    continue
                pub = ""
                try:
                    pd = parsedate_to_datetime(it.findtext("pubDate") or "")
                    if pd is not None:
                        if pd.tzinfo is None:
                            pd = pd.astimezone()  # 无时区标记按本地
                        if pd < since_dt:
                            continue
                        pub = pd.isoformat(timespec="seconds")
                except (TypeError, ValueError):
                    pass  # 日期解析失败 → 不按时间过滤，保留（宁多勿漏）
                # description 可能无正文（取决于服务是否输出全文），留空由批处理阶段重抓
                items.append({"key": link, "source": name,
                              "title": t, "summary": "", "link": link,
                              "published": pub})
        except Exception as e:  # noqa: BLE001
            errors.append({"source": f"{name}（{label}）", "error": f"RSS 拉取失败：{e}"})
    return {"items": items, "errors": errors}


def collect_wechat_scholar(since_dt: datetime) -> dict:
    """Wechat-Scholar 托管源（每日三次更新，≤12h 延迟）。"""
    return _collect_rss(WECHAT_SCHOLAR_FEEDS, since_dt, "RSS")


def collect_wechat2rss(since_dt: datetime) -> dict:
    """wechat2rss 公共托管源（~24h 内收录），与 Wechat-Scholar 相互独立。"""
    return _collect_rss(WECHAT2RSS_FEEDS, since_dt, "RSS2")


# ============================================================
# arXiv（Atom API，分类全量 + 提交时间窗口）
# ============================================================
def _arxiv_window(since_dt: datetime, now_dt: datetime):
    f = "%Y%m%d%H%M"
    return (since_dt.astimezone(timezone.utc).strftime(f),
            now_dt.astimezone(timezone.utc).strftime(f))


def collect_arxiv(since_dt: datetime, now_dt: datetime = None) -> dict:
    """采集 arXiv 最近 24h（cs.CL/cs.AI/cs.LG）论文，按 id 去重。
    返回 {"items": [...], "errors": [...]}。"""
    now_dt = now_dt or datetime.now(timezone.utc)
    lo, hi = _arxiv_window(since_dt, now_dt)
    cats = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    query = f"({cats}) AND submittedDate:[{lo} TO {hi}]"
    items, errors, seen = [], [], set()
    start = 0
    while start < ARXIV_MAX_TOTAL:
        try:
            r = _get(ARXIV_API, params={
                "search_query": query, "start": start,
                "max_results": ARXIV_PAGE_SIZE,
                "sortBy": "submittedDate", "sortOrder": "descending"},
                headers={"User-Agent": ARXIV_UA})
        except Exception as e:  # noqa: BLE001
            errors.append({"source": "arXiv", "error": f"arXiv API 请求失败：{e}"})
            break
        soup = BeautifulSoup(r.text, "html.parser")
        entries = soup.find_all("entry")
        if not entries:
            break
        for e in entries:
            id_tag = e.find("id")
            raw_id = id_tag.get_text(strip=True) if id_tag else ""
            if not raw_id or raw_id in seen:
                continue  # 同一篇可能挂多个分类
            seen.add(raw_id)
            # http://arxiv.org/abs/2408.12345v1 → https://arxiv.org/abs/2408.12345
            abs_url = re.sub(r"^http://", "https://", raw_id)
            abs_url = re.sub(r"v\d+$", "", abs_url)
            title = re.sub(r"\s+", " ", e.find("title").get_text(strip=True)) if e.find("title") else ""
            summary = re.sub(r"\s+", " ", e.find("summary").get_text(strip=True)) if e.find("summary") else ""
            pub = e.find("published")
            items.append({
                "key": abs_url,
                "source": "arXiv",
                "title": title,
                "summary": summary,
                "link": abs_url,
                "published": pub.get_text(strip=True) if pub else "",
            })
        if len(entries) < ARXIV_PAGE_SIZE:
            break
        start += ARXIV_PAGE_SIZE
        time.sleep(3)  # arXiv API 礼仪间隔
    return {"items": items, "errors": errors}


# ============================================================
# 研究画像：content/research/*.md → 方向 + 范畴
# ============================================================
_DIRECTION_RE = re.compile(r"^>\s*研究方向[：:]\s*(.+)$", re.MULTILINE)


def build_research_profile():
    """读取全部研究页，返回 [{name, direction, scope}]。
    direction 取「> 研究方向：」行（去 ** 强调），scope 取「## 研究范畴」段（截 400 字）。"""
    profile = []
    for f in sorted(glob.glob(str(RESEARCH_DIR / "*.md"))):
        name = Path(f).stem
        text = Path(f).read_text(encoding="utf-8")
        m = _DIRECTION_RE.search(text)
        direction = re.sub(r"\*+", "", m.group(1)).strip() if m else ""
        scope = ""
        sm = re.search(r"^##\s*研究范畴\s*$(.*?)(?=^##\s|\Z)", text,
                       flags=re.MULTILINE | re.DOTALL)
        if sm:
            scope = re.sub(r"\s+", " ", sm.group(1)).strip()[:400]
        profile.append({"name": name, "direction": direction, "scope": scope})
    return profile


def _load_api_key():
    key_file = REPO_ROOT / "api_key.txt"
    if not key_file.exists():
        return None
    key = key_file.read_text(encoding="utf-8").strip()
    return key or None


# ============================================================
# LLM 相关性判定
# ============================================================
def _filter_chunk(profile, chunk, api_key):
    """对一批候选（全局 idx 带在 item 里）调用 LLM 判定，返回 {idx: verdict}。"""
    from openai import OpenAI
    prof_text = "\n".join(
        f"- {p['name']}：{p['direction']}" + (f"（范畴：{p['scope']}）" if p["scope"] else "")
        for p in profile)
    cand_text = "\n".join(
        f"{it['_i']} | {it['title']} | {(it.get('summary') or '')[:300]}"
        for it in chunk)
    prompt = (
        "你是科研日报的相关性判定助手。下面是用户的【研究项目列表】和【候选内容列表】"
        "（每行格式：编号 | 标题 | 摘要）。请判断每条候选与任一研究项目是否相关。"
        "判定标准：内容的方法、问题、领域与研究方向有实质关联才算相关；"
        "仅同为 AI/LLM 泛泛新闻不算相关。严格返回 JSON 数组，不要代码块：\n"
        '[{"idx":编号,"relevant":true/false,"research":["匹配的研究项目名",...],"reason":"一句中文理由"}]\n'
        "research 只能从研究项目列表中选，无匹配给空数组。\n\n"
        f"研究项目列表：\n{prof_text}\n\n候选内容列表：\n{cand_text}"
    )
    client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "system", "content": "你是严谨的相关性判定助手，只输出 JSON。"},
                  {"role": "user", "content": prompt}])
    raw = (resp.choices[0].message.content or "").strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    parsed = json.loads(raw)
    if not isinstance(parsed, list):
        raise ValueError("LLM 返回非 JSON 数组")
    valid_names = {p["name"] for p in profile}
    out = {}
    for v in parsed:
        try:
            idx = int(v.get("idx"))
        except (TypeError, ValueError):
            continue
        research = [str(r) for r in (v.get("research") or []) if str(r) in valid_names]
        out[idx] = {"relevant": bool(v.get("relevant")),
                    "research": research,
                    "reason": str(v.get("reason") or "")[:120]}
    return out


def filter_relevance(candidates, api_key=None):
    """对全部候选做 LLM 相关性判定（分 chunk 并发）。
    就地把结果合并进每个候选：relevant(True/False/None)、research、reason。
    chunk 级失败 → 该批候选保持 relevant=None（前端显示「未判定」）。"""
    api_key = api_key or _load_api_key()
    if not api_key:
        for c in candidates:
            c.setdefault("relevant", None)
            c.setdefault("research", [])
            c.setdefault("reason", "无 API Key，未判定")
        return candidates
    if not candidates:
        return candidates
    profile = build_research_profile()
    # 打全局序号，分 chunk
    for i, c in enumerate(candidates):
        c["_i"] = i
    chunks = [candidates[i:i + FILTER_CHUNK]
              for i in range(0, len(candidates), FILTER_CHUNK)]
    verdicts = {}
    with ThreadPoolExecutor(max_workers=FILTER_WORKERS,
                            thread_name_prefix="rec-filter") as ex:
        results = list(ex.map(lambda ch: _safe_filter_chunk(profile, ch, api_key), chunks))
    for r in results:
        verdicts.update(r)
    for c in candidates:
        v = verdicts.get(c["_i"])
        if v:
            c["relevant"] = v["relevant"]
            c["research"] = v["research"]
            c["reason"] = v["reason"]
        else:
            c["relevant"] = None
            c["research"] = []
            c["reason"] = c.get("reason") or "LLM 判定失败，未判定"
        del c["_i"]
    return candidates


def _safe_filter_chunk(profile, chunk, api_key):
    try:
        return _filter_chunk(profile, chunk, api_key)
    except Exception:  # noqa: BLE001
        return {}


# ============================================================
# 缓存 + 采集编排
# ============================================================
def cache_path(day: str) -> Path:
    return RECOMMEND_DIR / f"recommend-{day}.json"


def load_cache():
    """加载今日缓存，无/损坏返回 None。"""
    p = cache_path(date_str())
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def save_cache(payload: dict) -> None:
    RECOMMEND_DIR.mkdir(parents=True, exist_ok=True)
    payload["date"] = date_str()
    payload["generated_at"] = datetime.now().isoformat(timespec="seconds")
    cache_path(date_str()).write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                                      encoding="utf-8")


def date_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def run_collection():
    """完整采集编排（在后台线程执行）：公众号 → arXiv → LLM 判定 → 写缓存。
    由路由层负责防重入（_RECOMMEND_RUNNING），缓存命中判断在 start_collection。"""
    global _RECOMMEND_RUNNING
    now = datetime.now(timezone.utc)
    since_ts = int(now.timestamp()) - 24 * 3600
    all_items, source_errors = [], []

    try:
        # 1) 微信公众号·appmsg 接口（需凭据，实时；限流/未配置时由下两级兜底）
        _set_state("wechat", counts={}, errors=[])
        cred = load_credentials()
        wechat_items, _appmsg_errors = [], []
        if cred:
            res = collect_wechat(cred, since_ts)
            wechat_items = res["items"]
            _appmsg_errors = res["errors"]

        # 2) 量子位官网（无需凭据，实时）
        qbitai = collect_qbitai(now - timedelta(hours=24))
        seen_titles = {_norm_title(w["title"]) for w in wechat_items}
        qbitai_items = [q for q in qbitai["items"]
                        if _norm_title(q["title"]) not in seen_titles]
        seen_titles |= {_norm_title(q["title"]) for q in qbitai_items}
        source_errors.extend(qbitai["errors"])

        # 3) Wechat-Scholar RSS（免凭据兜底之一，≤12h 延迟；与前两级按标题去重）
        scholar = collect_wechat_scholar(now - timedelta(hours=24))
        scholar_items = [s for s in scholar["items"]
                         if _norm_title(s["title"]) not in seen_titles]
        seen_titles |= {_norm_title(s["title"]) for s in scholar_items}
        source_errors.extend(scholar["errors"])

        # 4) wechat2rss 公共 RSS（免凭据兜底之二，与前三级按标题去重）
        w2r = collect_wechat2rss(now - timedelta(hours=24))
        w2r_items = [w for w in w2r["items"]
                     if _norm_title(w["title"]) not in seen_titles]
        source_errors.extend(w2r["errors"])

        all_items.extend(wechat_items)
        all_items.extend(qbitai_items)
        all_items.extend(scholar_items)
        all_items.extend(w2r_items)

        # appmsg 降级提示：仅在其本该覆盖的公众号没有被任何通道取到时才报警，
        # 已由官网/RSS 兜底的号不再重复提示（避免限流错误刷屏）
        covered = {i["source"] for i in all_items}
        source_errors.extend(e for e in _appmsg_errors if e["source"] not in covered)
        if not wechat_items and not _appmsg_errors:
            uncovered = [n for n, _ in WECHAT_ACCOUNTS if n not in covered]
            if uncovered:
                source_errors.append({"source": "、".join(uncovered),
                                      "error": "最近 24h 所有通道均未取到文章"
                                               "（大概率该号未发文；appmsg 未配置，无法实时核实）"})

        # 3) arXiv（24h 窗口为空时逐级放宽到 48h/72h：arXiv 按公告批次入库，
        #    刚公告的论文 submittedDate 常在 1~2 天前，严格 24h 会漏掉最新批次）
        _set_state("arxiv", counts=_count_by_source(all_items))
        for hours in (24, 48, 72):
            res = collect_arxiv(now - timedelta(hours=hours), now)
            all_items.extend(res["items"])
            source_errors.extend(res["errors"])
            if res["items"]:
                if hours != 24:
                    source_errors.append({
                        "source": "arXiv",
                        "error": f"最近 24h 无新提交（公告批次未覆盖），已回退到 {hours}h 窗口（{len(res['items'])} 篇）"})
                break
            if any("429" in e["error"] for e in res["errors"]):
                time.sleep(10)  # 刚被限速，放宽窗口前先冷却

        # 3) LLM 相关性判定
        _set_state("filter", counts=_count_by_source(all_items))
        filter_relevance(all_items)

        # 4) 写缓存
        save_cache({"sources": _count_by_source(all_items),
                    "errors": source_errors,
                    "items": all_items})
        _set_state("done", counts=_count_by_source(all_items),
                   errors=source_errors)
    except Exception as e:  # noqa: BLE001
        _set_state("error", errors=source_errors + [{"source": "编排", "error": str(e)}])
    finally:
        with _STATE_LOCK:
            _RECOMMEND_RUNNING = False


def _count_by_source(items):
    out = {}
    for it in items:
        out[it["source"]] = out.get(it["source"], 0) + 1
    return out


def start_collection(force: bool = False) -> bool:
    """后台启动一次采集（今日缓存存在且非 force 时直接复用）。已在运行返回 False。"""
    global _RECOMMEND_RUNNING
    if not force and load_cache():
        return True  # 缓存命中，无需采集
    with _STATE_LOCK:
        if _RECOMMEND_RUNNING:
            return False
        _RECOMMEND_RUNNING = True
    threading.Thread(target=run_collection, daemon=True).start()
    return True
