"""
趋势栏目数据生成器：汇总全部日报条目 → content/trends/trends.json（契约见 .omc/plans/trends-contract.md）。

纯聚合：不调 LLM、不联网；只依赖 tomllib/tomli。约 3k 条目 1 秒内完成。
时间轴以【日报日期】（文件名）为准，反映「我们关注到的时间」；周 = ISO 周（周一起），月 = YYYY-MM。

用法：python3 tools/trends_build.py [--out PATH] [--quiet]
部署：backend/deploy.py 提交前自动调用；也可手动运行后 hugo 预览。
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    import tomllib as toml  # py311+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as toml

REPO_ROOT = Path(__file__).resolve().parents[1]
UPDATES_DIR = REPO_ROOT / "content" / "updates"
RESEARCH_DIR = REPO_ROOT / "content" / "research"
TRACKS_FILE = REPO_ROOT / "tools" / "trends" / "tracks.json"
DEFAULT_OUT = REPO_ROOT / "content" / "trends" / "trends.json"

OTHER_TRACK = "其他"
RISING_WINDOW_WEEKS = 4
RECENT_DAYS = 30
GAP_MIN_DAYS = 3
# 泛化词：不进词云 / 升降温榜（无技术含义）
GENERIC_TERMS = {"人工智能", "大模型", "大语言模型", "LLM", "AI", "研究", "方法", "模型", "技术", "论文", "智能"}

# source 字段写法混乱（公众号名 / 站点名 / 分类名混用），归到少数「来源族」
# 规则按顺序匹配（小写包含），首个命中生效；都不命中 → 其他；空/未知 → 未知
SOURCE_FAMILIES = [
    ("arXiv", ["arxiv"]),
    ("Hugging Face Papers", ["hugging face", "huggingface", "hf papers"]),
    ("新智元 ASI爆点", ["asi爆点", "asi 爆点", "aiera"]),
    ("AIHOT", ["aihot"]),
    ("AIbase", ["aibase"]),
    ("AI工具集", ["ai工具集", "ai-bot"]),
    ("智源社区", ["智源"]),
    ("小红书", ["小红书", "xiaohongshu"]),
    ("微信公众号", ["公众号", "微信", "量子位", "机器之心", "新智元", "datawhale", "模智空间", "语鲸",
                "智猩猩", "夕小瑶", "paperweekly", "深度学习自然语言处理", "nlp工作站", "甲子光年",
                "硅星人", "zhuanzhi", "专知", "akshare", "青稞", "开源ai", "appso", "差评", "极客公园",
                "海外独角兽", "飞桨", "魔搭", "通义", "deepseek", "mlnlp", "赛博禅心", "数字生命卡兹克",
                "智东西", "ai前线", "infoq", "虎嗅", "deeptech", "paperagent", "具身智能之心", "yar师",
                "你说的完全正确", "36氪", "量子位", "机器之心pro", "新浪", "腾讯", "澎湃"]),
    ("GitHub", ["github"]),
    ("社交媒体", ["twitter", "x.com", "推特", "reddit", "知乎", "bilibili", "b站", "youtube", "linkedin"]),
    ("博客/官网", ["blog", "博客", "官网", "openai", "anthropic", "google", "deepmind", "meta", "microsoft",
                 "nvidia", "官方", "moonshot", "智谱", "面壁", "百度", "阿里", "字节", "kimi", "qwen"]),
]


# ------------------------------------------------------------------ 读取
def front_matter(text: str):
    """按行取 TOML front matter（首尾单独成行的 +++ 之间），正文含 '+++' 字符串也不受影响；没有返回 None。"""
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
        return None
    return "\n".join(lines[open_idx + 1:close_idx])


def load_items():
    """读取全部日报，返回 (items, digest_dates)。每条 item 附 _date(date)。"""
    items, dates = [], []
    for p in sorted(UPDATES_DIR.glob("*.md")):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", p.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        body = front_matter(p.read_text(encoding="utf-8"))
        if body is None:
            print(f"[trends] skip {p.name}: 缺少 +++ front matter", file=sys.stderr)
            continue
        try:
            fm = toml.loads(body)
        except Exception as e:  # noqa: BLE001
            print(f"[trends] skip {p.name}: {e}", file=sys.stderr)
            continue
        if fm.get("draft") is True:
            continue
        dates.append(d)
        for it in fm.get("items", []) or []:
            it = dict(it)
            it["_date"] = d
            items.append(it)
    return items, sorted(dates)


def load_research():
    """研究项目：{name: {"proposed": "YYYY-MM"|None}}，proposed 取 front matter 的 since。"""
    out = {}
    if not RESEARCH_DIR.exists():
        return out
    for p in sorted(RESEARCH_DIR.glob("*.md")):
        if p.name.startswith("_"):
            continue
        body = front_matter(p.read_text(encoding="utf-8"))
        proposed = None
        if body is not None:
            try:
                fm = toml.loads(body)
                since = fm.get("since")
                if isinstance(since, (date, datetime)):
                    proposed = since.strftime("%Y-%m")
                elif isinstance(since, str) and len(since) >= 7:
                    proposed = since[:7]
            except Exception:  # noqa: BLE001
                pass
        out[p.stem] = {"proposed": proposed}
    return out


def load_tracks():
    if not TRACKS_FILE.exists():
        print(f"[trends] warning: {TRACKS_FILE} 不存在，所有主题归入「{OTHER_TRACK}」", file=sys.stderr)
        return [], {}
    data = json.loads(TRACKS_FILE.read_text(encoding="utf-8"))
    return list(data.get("tracks", [])), dict(data.get("map", {}))


# ------------------------------------------------------------------ 工具
def as_list(v):
    if v is None:
        return []
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    return [str(x).strip() for x in v if str(x).strip()]


def source_family(src: str) -> str:
    s = (src or "").strip()
    if not s or s == "未知":
        return "未知"
    low = s.lower()
    for fam, keys in SOURCE_FAMILIES:
        if any(k in low for k in keys):
            return fam
    return "其他"


def week_start(d: date) -> date:
    return d - timedelta(days=d.weekday())


def month_key(d: date) -> str:
    return d.strftime("%Y-%m")


def month_range(a: date, b: date):
    out, y, m = [], a.year, a.month
    while (y, m) <= (b.year, b.month):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            y, m = y + 1, 1
    return out


def moving_avg(xs, n=4):
    out = []
    for i in range(len(xs)):
        win = xs[max(0, i - n + 1):i + 1]
        out.append(round(sum(win) / len(win), 2))
    return out


def top(cnt: Counter, n: int) -> list:
    """确定性 Top-N：按计数降序、名称升序（Counter.most_common 的并列顺序取决于插入/哈希顺序，
    会让每次生成的 JSON 不一样，进而让部署误判「内容有变」）。"""
    return [[k, v] for k, v in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[:n]]


def shares(counts, totals):
    return [round(c / t, 4) if t else 0.0 for c, t in zip(counts, totals)]


def series(per_week: Counter, weeks, per_month: Counter, months, totals_w):
    counts = [per_week.get(w, 0) for w in weeks]
    return {"counts": counts, "share": shares(counts, totals_w), "ma4": moving_avg(counts),
            "total": sum(counts), "monthly": [per_month.get(m, 0) for m in months]}


def rising_list(recent: Counter, prev: Counter, recent_total: int, prev_total: int,
                top=15, min_total=3):
    """升温/降温：按【占比】比较（该名称条目数 ÷ 窗口内全部条目数），抵消采集量本身的增长；
    delta 为占比变化的百分点（×100），ratio 为占比倍数。两窗口合计 < min_total 的名称不参与。"""
    rows = []
    for n in sorted(set(recent) | set(prev)):
        r, p = recent.get(n, 0), prev.get(n, 0)
        if r + p < min_total:
            continue
        rs = r / recent_total if recent_total else 0.0
        ps = p / prev_total if prev_total else 0.0
        rows.append({"name": n, "recent": r, "prev": p,
                     "recent_share": round(rs, 4), "prev_share": round(ps, 4),
                     "delta": round((rs - ps) * 100, 2),
                     "ratio": round(rs / ps, 2) if ps else None})
    rows.sort(key=lambda x: (x["delta"], x["recent"]), reverse=True)
    up = [x for x in rows if x["delta"] > 0][:top]
    down = sorted([x for x in rows if x["delta"] < 0], key=lambda x: (x["delta"], -x["prev"]))[:top]
    return up + down


KEYWORD_COVERAGE_MIN = 0.5  # keywords 字段覆盖率达到此值后，词云/升降温只用 keywords ∪ subtopic


def item_terms(it, use_topics: bool) -> set:
    """条目的术语集合：keywords ∪ subtopic；keywords 覆盖不足时再并入粗粒度 topics 兜底。"""
    terms = set(as_list(it.get("keywords")))
    if use_topics:
        terms |= set(as_list(it.get("topics")))
    sub = (it.get("subtopic") or "").strip()
    if sub:
        terms.add(sub)
    return {t for t in terms if t and t not in GENERIC_TERMS}


# ------------------------------------------------------------------ 主流程
def build(items, digest_dates, research_meta, track_names, track_map):
    if not items:
        raise SystemExit("[trends] 没有可用日报条目")
    first, last = digest_dates[0], digest_dates[-1]
    w0, w1 = week_start(first), week_start(last)
    weeks = []
    w = w0
    while w <= w1:
        weeks.append(w)
        w += timedelta(days=7)
    week_keys = [w.isoformat() for w in weeks]
    months = month_range(first, last)

    tot_w, tot_m = Counter(), Counter()
    res_w, res_m = defaultdict(Counter), defaultdict(Counter)
    trk_w, trk_m = defaultdict(Counter), defaultdict(Counter)
    src_w, src_m = defaultdict(Counter), defaultdict(Counter)
    org_w_total = Counter()
    org_m = defaultdict(Counter)
    org_res = Counter()
    kw_all, kw_month = Counter(), defaultdict(Counter)
    kw_recent, kw_prev = Counter(), Counter()
    sub_recent, sub_prev = Counter(), Counter()
    trk_recent, trk_prev = Counter(), Counter()
    kw_recent_w, kw_prev_w = Counter(), Counter()
    unrecognized = Counter()
    unmapped_topics = Counter()
    mapped_items = unmapped_items = 0
    with_kw = with_orgs = arxiv_items = arxiv_with_orgs = 0
    proj_seen = defaultdict(list)

    kw_items = sum(1 for it in items if as_list(it.get("keywords")))
    use_topics = kw_items / len(items) < KEYWORD_COVERAGE_MIN
    rw_total = pw_total = 0

    recent_from = last - timedelta(days=RECENT_DAYS - 1)
    prev_from = recent_from - timedelta(days=RECENT_DAYS)
    rw_from = w1 - timedelta(days=7 * (RISING_WINDOW_WEEKS - 1))
    pw_from = rw_from - timedelta(days=7 * RISING_WINDOW_WEEKS)

    for it in items:
        d = it["_date"]
        wk, mk = week_start(d).isoformat(), month_key(d)
        tot_w[wk] += 1
        tot_m[mk] += 1
        in_recent = d >= recent_from
        in_prev = prev_from <= d < recent_from
        in_rw = d >= rw_from
        in_pw = pw_from <= d < rw_from
        if in_rw:
            rw_total += 1
        elif in_pw:
            pw_total += 1

        # 研究项目
        for r in as_list(it.get("research")):
            res_w[r][wk] += 1
            res_m[r][mk] += 1
            proj_seen[r].append(d)

        # 赛道
        topics = as_list(it.get("topics"))
        tracks = set()
        for t in topics:
            trk = track_map.get(t)
            if trk:
                tracks.add(trk)
            else:
                unmapped_topics[t] += 1
        if tracks:
            mapped_items += 1
        else:
            unmapped_items += 1
            tracks = {OTHER_TRACK}
        for trk in tracks:
            trk_w[trk][wk] += 1
            trk_m[trk][mk] += 1
            if in_rw:
                trk_recent[trk] += 1
            elif in_pw:
                trk_prev[trk] += 1

        # 来源
        fam = source_family(it.get("source", ""))
        if fam == "其他":
            unrecognized[(it.get("source") or "").strip()] += 1
        src_w[fam][wk] += 1
        src_m[fam][mk] += 1

        # 关键词（keywords ∪ topics ∪ subtopic）
        kws = as_list(it.get("keywords"))
        if kws:
            with_kw += 1
        terms = item_terms(it, use_topics)
        for t in terms:
            kw_all[t] += 1
            kw_month[mk][t] += 1
            if in_recent:
                kw_recent[t] += 1
            elif in_prev:
                kw_prev[t] += 1
            if in_rw:
                kw_recent_w[t] += 1
            elif in_pw:
                kw_prev_w[t] += 1
        sub = (it.get("subtopic") or "").strip()
        if sub:
            if in_rw:
                sub_recent[sub] += 1
            elif in_pw:
                sub_prev[sub] += 1

        # 机构
        orgs = as_list(it.get("orgs"))
        is_arxiv = "arxiv.org" in (it.get("paper") or "") or fam == "arXiv"
        if is_arxiv:
            arxiv_items += 1
        if orgs:
            with_orgs += 1
            if is_arxiv:
                arxiv_with_orgs += 1
            for o in dict.fromkeys(orgs):
                org_w_total[o] += 1
                org_m[o][mk] += 1
                for r in as_list(it.get("research")):
                    org_res[(o, r)] += 1

    totals_w = [tot_w.get(w, 0) for w in week_keys]
    totals_m = [tot_m.get(m, 0) for m in months]

    research_names = sorted(set(research_meta) | set(res_w), key=lambda n: (n not in research_meta, n))
    research = {}
    projects = {}
    for r in research_names:
        s = series(res_w[r], week_keys, res_m[r], months, totals_w)
        s["proposed"] = research_meta.get(r, {}).get("proposed")
        research[r] = s
        seen = sorted(proj_seen.get(r, []))
        projects[r] = {"proposed": s["proposed"], "total": s["total"],
                       "first_seen": seen[0].isoformat() if seen else None,
                       "last_seen": seen[-1].isoformat() if seen else None,
                       "monthly": s["monthly"]}

    track_order = [t for t in track_names if t in trk_w] + \
                  [t for t in trk_w if t not in track_names and t != OTHER_TRACK]
    if OTHER_TRACK in trk_w:
        track_order.append(OTHER_TRACK)
    tracks = {t: series(trk_w[t], week_keys, trk_m[t], months, totals_w) for t in track_order}

    top_orgs = top(org_w_total, 40)
    top15 = [o for o, _ in top_orgs[:15]]
    top20 = [o for o, _ in top_orgs[:20]]
    res_idx = {r: i for i, r in enumerate(research_names)}
    org_idx = {o: i for i, o in enumerate(top20)}
    matrix = [[org_idx[o], res_idx[r], c] for (o, r), c in org_res.items()
              if o in org_idx and r in res_idx]

    # 日报空档（连续 ≥ GAP_MIN_DAYS 天无日报）
    gaps = []
    for a, b in zip(digest_dates, digest_dates[1:]):
        missing = (b - a).days - 1
        if missing >= GAP_MIN_DAYS:
            gaps.append([(a + timedelta(days=1)).isoformat(), (b - timedelta(days=1)).isoformat()])

    fam_order = [f for f, _ in SOURCE_FAMILIES if f in src_w] + \
                [f for f in ("其他", "未知") if f in src_w]
    n = len(items)
    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "range": {"from": first.isoformat(), "to": last.isoformat()},
        "week_starts": week_keys,
        "months": months,
        "totals": {"items_per_week": totals_w, "items_per_month": totals_m,
                   "items": n, "digests": len(digest_dates)},
        "research": research,
        "tracks": tracks,
        "track_coverage": {"mapped_items": mapped_items, "unmapped_items": unmapped_items,
                           "unmapped_topics_top": top(unmapped_topics, 30)},
        "rising": {"window_weeks": RISING_WINDOW_WEEKS,
                   "recent_from": rw_from.isoformat(), "prev_from": pw_from.isoformat(),
                   "recent_total": rw_total, "prev_total": pw_total,
                   "tracks": rising_list(trk_recent, trk_prev, rw_total, pw_total),
                   "keywords": rising_list(kw_recent_w, kw_prev_w, rw_total, pw_total),
                   "subtopics": rising_list(sub_recent, sub_prev, rw_total, pw_total)},
        "keywords": {"source": ("keywords 字段 ∪ subtopic" if not use_topics
                                else "topics ∪ subtopic（keywords 覆盖不足，暂以粗粒度主题兜底）"),
                     "recent_days": RECENT_DAYS,
                     "recent_from": recent_from.isoformat(), "prev_from": prev_from.isoformat(),
                     "all": top(kw_all, 150),
                     "recent30": top(kw_recent, 150),
                     "prev30": top(kw_prev, 150),
                     "by_month": {m: top(kw_month[m], 60) for m in months if kw_month.get(m)},
                     "coverage": {"items_with_keywords": with_kw, "total": n}},
        "orgs": {"top": top_orgs,
                 "monthly": {o: [org_m[o].get(m, 0) for m in months] for o in top15},
                 "research_matrix": {"orgs": top20, "research": research_names, "values": matrix},
                 "coverage": {"items_with_orgs": with_orgs, "total": n,
                              "arxiv_items": arxiv_items, "arxiv_with_orgs": arxiv_with_orgs}},
        "sources": {"families": fam_order,
                    "per_week": {f: [src_w[f].get(w, 0) for w in week_keys] for f in fam_order},
                    "per_month": {f: [src_m[f].get(m, 0) for m in months] for f in fam_order},
                    "unrecognized_top": top(unrecognized, 20)},
        "projects": projects,
        "digests": {"count": len(digest_dates), "dates": [d.isoformat() for d in digest_dates],
                    "gaps": gaps},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    items, dates = load_items()
    track_names, track_map = load_tracks()
    data = build(items, dates, load_research(), track_names, track_map)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # 内容（除 generated_at 外）未变时不写盘，避免部署把纯时间戳变化当成内容更新
    if out.exists():
        try:
            old = json.loads(out.read_text(encoding="utf-8"))
            old_gen = old.pop("generated_at", None)
            if old == {k: v for k, v in data.items() if k != "generated_at"}:
                if not args.quiet:
                    print(f"[trends] 数据未变化（上次生成 {old_gen}），跳过写入")
                return
        except Exception:  # noqa: BLE001
            pass
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    out.write_text(text, encoding="utf-8")
    if not args.quiet:
        cov = data["track_coverage"]
        print(f"[trends] {out} 写入 {len(text) / 1024:.0f} KB：{data['totals']['items']} 条 / "
              f"{data['totals']['digests']} 期（{data['range']['from']} ~ {data['range']['to']}），"
              f"{len(data['week_starts'])} 周，研究 {len(data['research'])}，赛道 {len(data['tracks'])}，"
              f"赛道覆盖 {cov['mapped_items']}/{cov['mapped_items'] + cov['unmapped_items']}，"
              f"keywords 覆盖 {data['keywords']['coverage']['items_with_keywords']}，"
              f"orgs 覆盖 {data['orgs']['coverage']['items_with_orgs']}，"
              f"来源未识别 {sum(c for _, c in data['sources']['unrecognized_top'])}")


if __name__ == "__main__":
    main()
