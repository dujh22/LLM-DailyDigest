"""
研究页（content/research/*.md）的特殊栏目：解析、补齐、守卫、研究经验渲染。纯标准库实现，
后端（app.py 日报整备）与 Claude Code 守卫 hook（.claude/hooks/guard_research_human.py）共用。

三个栏目：
- 「## 自研洞察」「## 自研经验」：人类专属。整个小节（标题到下一个二级标题）AI 与自动化流程
  不得修改；后端写研究页前后逐字比对，hook 在 AI 编辑会改动它们时强制询问人类。
  human-only 标记仅作提示，保护范围以标题为准。
- 「## 研究经验」：随日报整备自动更新。每条经验 = 一条面向整个研究社区的洞察或方法论 +
  支撑它的具体工作列表（链接到日报条目锚点），包在 research-experience 标记对之间整块替换。

机器可读格式（不要改动标记与列表结构）：

    1. **经验标题**：经验正文
       - [工作标题](../../updates/2026-11-25/#item-id) · 2026-11-25
"""
import re

HUMAN_SECTIONS = ("自研洞察", "自研经验")
HUMAN_PLACEHOLDER = "*（待人工补充）*"
EXP_SECTION = "研究经验"
EXP_START = ("<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的"
             "洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->")
EXP_END = "<!-- research-experience:end -->"
EXP_EMPTY = "*（暂无，随日报自动积累）*"
# 新栏目插在「## 相关工作」之前；没有该小节时追加到文末
_ANCHOR_HEADING = "## 相关工作"


def human_start(name: str) -> str:
    return (f"<!-- human-only:start {name}｜仅限人类手动编辑：AI 与自动化流程不得修改，"
            "确需修改必须先询问人类并获得同意 -->")


def human_end(name: str) -> str:
    return f"<!-- human-only:end {name} -->"


_HUMAN_MARK_RE = re.compile(r"<!-- human-only:(?:start|end) .*?-->", re.S)
_EXP_RE = re.compile(r"<!-- research-experience:start.*?-->(.*?)<!-- research-experience:end -->",
                     re.S)


def human_sections(text: str) -> dict:
    """返回 {栏目名: [该栏目每次出现的完整原文, ...]}。受保护范围 = 从「## 栏目名」标题行到下一个
    二级标题（或文末），含标题、human-only 标记及标记外的文字；末尾空白不计。
    按列表记录同名栏目的每次出现，复制一份原样栏目再篡改另一份也能被发现。"""
    text = text or ""
    heads = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^## (.+?)[ \t]*$", text, re.M)]
    out = {}
    for i, (pos, name) in enumerate(heads):
        if name in HUMAN_SECTIONS:
            end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
            out.setdefault(name, []).append(text[pos:end].rstrip())
    return out


def _is_blank_section(span: str) -> bool:
    body = _HUMAN_MARK_RE.sub("", span.split("\n", 1)[1] if "\n" in span else "")
    return body.strip() in ("", HUMAN_PLACEHOLDER)


def human_violations(old: str, new: str) -> list:
    """比对改动前后人类专属栏目，返回违规说明列表（空列表 = 未触碰）。
    规则：old 中已有的栏目（含出现次数）必须逐字不变且不能被删除；new 中新出现的栏目只能是
    空白或占位符（即只允许「补齐空栏目」，不允许替人类填写内容）。"""
    before, after = human_sections(old), human_sections(new)
    out = []
    for name in HUMAN_SECTIONS:
        b, a = before.get(name, []), after.get(name, [])
        if b:
            if not a:
                out.append(f"删除了人类专属栏目「{name}」（或改动了其标题）")
            elif a != b:
                out.append(f"修改了人类专属栏目「{name}」的内容（或增删了同名栏目）")
        elif len(a) > 1 or any(not _is_blank_section(x) for x in a):
            out.append(f"新建的人类专属栏目「{name}」中写入了内容")
    return out


def _human_block(name: str) -> str:
    return f"## {name}\n\n{human_start(name)}\n{HUMAN_PLACEHOLDER}\n{human_end(name)}\n"


def _exp_block(body: str = "") -> str:
    return f"## {EXP_SECTION}\n\n{EXP_START}\n{body.strip() or EXP_EMPTY}\n{EXP_END}\n"


def ensure_sections(text: str) -> str:
    """补齐缺失的三个栏目（只新增空栏目，不改动任何已有内容），插在「## 相关工作」之前。
    已有同名标题但缺标记的不重复插入（避免与人工写法冲突，交由人类自行整理）。"""
    missing = []
    have = human_sections(text)
    for name in HUMAN_SECTIONS:
        if name not in have:
            missing.append(_human_block(name))
    if not _EXP_RE.search(text) and not re.search(rf"^## {EXP_SECTION}\s*$", text, re.M):
        missing.append(_exp_block())
    if not missing:
        return text
    blob = "\n".join(missing)
    m = re.search(rf"^{re.escape(_ANCHOR_HEADING)}\s*$", text, re.M)
    if m:
        return text[:m.start()] + blob + "\n" + text[m.start():]
    return text.rstrip("\n") + "\n\n" + blob


# ---------------- 研究经验：解析 / 渲染 ----------------
_EXP_ITEM_RE = re.compile(r"^\d+\.\s+\*\*(.+?)\*\*\s*[：:]\s*(.*)$")
_EXP_WORK_RE = re.compile(
    r"^\s+-\s+\[(.*)\]\(\.\./\.\./updates/(\d{4}-\d{2}-\d{2})/#([^)\s]+)\)")


def experience_block(text: str):
    """研究经验标记对之间的原文；无标记时返回 None。"""
    m = _EXP_RE.search(text or "")
    return m.group(1) if m else None


def parse_experiences(text: str) -> list:
    """从研究页解析研究经验列表：[{"title", "insight", "works": [{"date", "id", "title"}]}]。"""
    m = _EXP_RE.search(text or "")
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        mi = _EXP_ITEM_RE.match(line)
        if mi:
            out.append({"title": mi.group(1).strip(), "insight": mi.group(2).strip(),
                        "works": []})
            continue
        mw = _EXP_WORK_RE.match(line)
        if mw and out:
            out[-1]["works"].append({"title": mw.group(1).strip(), "date": mw.group(2),
                                     "id": mw.group(3)})
    return out


def clean_line(s: str) -> str:
    """经验标题 / 正文规整为单行纯文本：去换行与 ** 加粗、中和 HTML 注释，
    保证渲染后能原样解析回来，且不会提前闭合标记块或吞掉后续页面。"""
    s = re.sub(r"\s+", " ", str(s or "")).replace("**", "")
    return s.replace("<!--", "&lt;!--").replace("-->", "--&gt;").strip()


def _md_link_text(s: str) -> str:
    return clean_line((s or "").replace("[", "［").replace("]", "］")) or "（无标题）"


_SEEN_RE = re.compile(r"<!-- experience-seen:(.*?)-->", re.S)


def parse_seen(text: str) -> set:
    """已送 LLM 判定过的条目 {"日期/id"}（含未挂接到任何经验的），避免重复整备时反复判定。"""
    m = _EXP_RE.search(text or "")
    ms = _SEEN_RE.search(m.group(1)) if m else None
    return set(ms.group(1).split()) if ms else set()


def render_experiences(exps: list, seen=None) -> str:
    """渲染为编号列表；工作按日期倒序（最新在前），研究页位于 /research/<名>/，
    相对链接 ../../updates/<日期>/#<id> 在任意 baseURL 子路径下都成立。
    seen 以 HTML 注释附在末尾（页面不可见）。"""
    tail = f"\n<!-- experience-seen: {' '.join(sorted(seen))} -->" if seen else ""
    if not exps:
        return EXP_EMPTY + tail
    lines = []
    for i, e in enumerate(exps, 1):
        lines.append(f"{i}. **{clean_line(e['title'])}**：{clean_line(e['insight'])}")
        for w in sorted(e["works"], key=lambda w: (w["date"], w["id"]), reverse=True):
            lines.append(f"   - [{_md_link_text(w['title'])}](../../updates/{w['date']}/#{w['id']})"
                         f" · {w['date']}")
    return "\n".join(lines) + tail


def replace_experiences(text: str, exps: list, seen=None) -> str:
    """把研究经验块整块替换为 exps 的渲染结果（缺栏目时先补齐）。"""
    text = ensure_sections(text)
    body = render_experiences(exps, seen)
    if _EXP_RE.search(text):
        return _EXP_RE.sub(lambda _m: f"{EXP_START}\n{body}\n{EXP_END}", text, count=1)
    # 有「## 研究经验」标题但缺标记（人工写法）：不覆盖，原样返回
    return text
