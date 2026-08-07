"""
LLM-DailyDigest 单条消息提交后端（本地工具）

功能：
  GET  /              交互式填写表单
  GET  /api/topics    返回 content/topic/ 下的合法主题名
  POST /api/extract   用 LLM 从原始文本抽取结构化字段（JSON）
  POST /api/submit    把一条 item 追加到当日日报 content/updates/<date>.md 的 [[items]]

API Key：读取仓库根目录 api_key.txt；不存在则禁用 LLM 抽取并提示用户。
运行：python backend/app.py  （然后浏览器打开 http://localhost:5050）
"""
import os
import re
import json
import glob
from datetime import date
from pathlib import Path

from flask import Flask, request, jsonify, render_template

# ---- 路径 ----
REPO_ROOT = Path(__file__).resolve().parents[1]
UPDATES_DIR = REPO_ROOT / "content" / "updates"
TOPIC_DIR = REPO_ROOT / "content" / "topic"
RESEARCH_DIR = REPO_ROOT / "content" / "research"
API_KEY_FILE = REPO_ROOT / "api_key.txt"

# ---- LLM 配置（可被环境变量覆盖）----
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api-gateway.glm.ai/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-5.6-sol")

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
# 路由
# ============================================================
@app.route("/")
def index():
    return render_template("index.html", topics=valid_topics(), research=valid_research())


@app.route("/api/topics")
def api_topics():
    return jsonify({"topics": valid_topics()})


@app.route("/api/research")
def api_research():
    return jsonify({"research": valid_research()})


@app.route("/api/submit", methods=["POST"])
def api_submit():
    data = request.get_json(force=True, silent=True) or {}
    try:
        item = build_item_from_form(data)
    except ValueError as e:
        return jsonify({"ok": False, "errors": [str(e)]}), 400
    target_date = item.pop("_target_date", None)

    # 校验
    errors = []
    if not item["title"]:
        errors.append("title 不能为空")
    if not item["topics"]:
        errors.append("topics 不能为空（至少选一个主题）")
    if errors:
        return jsonify({"ok": False, "errors": errors}), 400

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
        return jsonify({"ok": False, "errors": errors}), 400

    # 研究项目：固定集合，过滤掉未知项（不自动新建）
    vr = set(valid_research())
    item["research"] = [r for r in item["research"] if r in vr]

    try:
        path = append_item(item, target_date)
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "errors": [f"写入失败：{e}"]}), 500

    rel = path.relative_to(REPO_ROOT)
    msg = f"已追加到 {rel}（id={item['id']}）"
    if created_topics:
        msg += f"；新建主题：{created_topics}"
    return jsonify({
        "ok": True,
        "item": item,
        "file": str(rel),
        "created_topics": created_topics,
        "message": msg,
    })


@app.route("/api/extract", methods=["POST"])
def api_extract():
    data = request.get_json(force=True, silent=True) or {}
    raw = (data.get("raw") or "").strip()
    if not raw:
        return jsonify({"ok": False, "errors": ["raw 不能为空"]}), 400

    api_key = load_api_key()
    if not api_key:
        return jsonify({
            "ok": False,
            "errors": [
                f"未找到 API Key：请在仓库根目录创建 {API_KEY_FILE.relative_to(REPO_ROOT)} "
                f"并填入你的 GLM/OpenAI 兼容 api_key（该文件已被 .gitignore 忽略，不会上传 git）。"
            ],
        }), 503

    topics = valid_topics()
    research = valid_research()
    system_prompt = (
        "你是大模型研究日报的结构化信息抽取助手。"
        "从用户提供的原始文本中抽取【一条消息】的结构化字段，严格返回 JSON（不要代码块、不要额外解释）。"
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

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key, base_url=LLM_BASE_URL)
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": raw},
            ],
        )
        content_str = resp.choices[0].message.content or ""
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "errors": [f"LLM 调用失败：{e}"]}), 502

    # 鲁棒解析 JSON（去掉可能的 ```json 代码块围栏）
    cleaned = content_str.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        return jsonify({
            "ok": False,
            "errors": ["LLM 返回无法解析为 JSON"],
            "raw": content_str,
        }), 502

    # 规范化 topics / suggested_topics
    t = parsed.get("topics", [])
    if isinstance(t, str):
        t = [t]
    parsed["topics"] = [str(x) for x in t]
    s = parsed.get("suggested_topics", [])
    if isinstance(s, str):
        s = [s]
    parsed["suggested_topics"] = [str(x).strip() for x in s if str(x).strip()]
    r = parsed.get("research", [])
    if isinstance(r, str):
        r = [r]
    parsed["research"] = [str(x).strip() for x in r if str(x).strip()]
    return jsonify({"ok": True, "data": parsed})


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
