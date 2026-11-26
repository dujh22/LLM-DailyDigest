"""
日报阅读反馈：记录 + 每周提醒（纯标准库，供 app.py 与 .claude/hooks 共用）。

数据：
  data/feedback/feedback.json  反馈列表（新认识 / 不满意 / 建议），纳入 git 备份
  data/feedback/state.json     各提醒通道上次确认时间 {"app": iso, "claude": iso}

提醒规则：存在未处理（status=open）的「不满意 / 建议」，且该通道距上次确认
≥ REMIND_DAYS 天（默认 7）→ 到期。通道：
  app     启动 app.py 时终端打印 + 首页横幅；在 /feedback 页点「本周已查看」才确认
  claude  Claude Code 读/改 backend/app.py 时由 hook 注入提醒，注入即确认
"""
import fcntl
import json
import os
import secrets
import tempfile
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FEEDBACK_DIR = REPO_ROOT / "data" / "feedback"
FEEDBACK_FILE = FEEDBACK_DIR / "feedback.json"
STATE_FILE = FEEDBACK_DIR / "state.json"
try:
    REMIND_DAYS = max(1, int(os.environ.get("FEEDBACK_REMIND_DAYS", "7")))
except ValueError:
    REMIND_DAYS = 7

KINDS = {"insight": "新认识", "complaint": "不满意", "idea": "建议"}
ACTIONABLE = ("complaint", "idea")       # 需要「修」的类型，参与提醒
STATUSES = ("open", "fixed", "wontfix")

_LOCK = threading.Lock()


@contextmanager
def _locked():
    """进程内锁 + 跨进程文件锁（app.py 与 Claude hook 是不同进程，会同时读改写）。"""
    with _LOCK:
        FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
        with open(FEEDBACK_DIR / ".lock", "w") as lf:
            fcntl.flock(lf, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(lf, fcntl.LOCK_UN)


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def _write_json(path: Path, data) -> None:
    """先写临时文件再原子替换，避免写一半崩溃留下坏文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    os.replace(tmp, path)


def load_all() -> list:
    data = _read_json(FEEDBACK_FILE, [])
    return [x for x in data if isinstance(x, dict)] if isinstance(data, list) else []


def add(kind: str, text: str, digest_date: str = "", item_id: str = "",
        item_title: str = "") -> dict:
    kind = kind if isinstance(kind, str) and kind in KINDS else "complaint"
    text = str(text or "").strip()
    digest_date, item_id, item_title = (str(v or "") for v in (digest_date, item_id, item_title))
    if not text:
        raise ValueError("反馈内容不能为空")
    rec = {
        "id": datetime.now().strftime("%Y%m%d") + "-" + secrets.token_hex(3),
        "created_at": _now(),
        "kind": kind,
        "digest_date": (digest_date or "").strip(),
        "item_id": (item_id or "").strip(),
        "item_title": (item_title or "").strip(),
        "text": text,
        "status": "open" if kind in ACTIONABLE else "noted",
        "resolution": "",
        "resolved_at": "",
    }
    with _locked():
        items = load_all()
        items.append(rec)
        _write_json(FEEDBACK_FILE, items)
    return rec


def update(fid: str, status: str = None, resolution: str = None) -> dict:
    with _locked():
        items = load_all()
        rec = next((x for x in items if x.get("id") == fid), None)
        if rec is None:
            raise KeyError(f"反馈 {fid} 不存在")
        if status is not None:
            if not isinstance(status, str) or status not in STATUSES:
                raise ValueError(f"非法状态：{status}")
            rec["status"] = status
            rec["resolved_at"] = "" if status == "open" else _now()
        if resolution is not None:
            rec["resolution"] = str(resolution).strip()
        _write_json(FEEDBACK_FILE, items)
    return rec


def open_actionable() -> list:
    """未处理的「不满意 / 建议」，按提交时间升序（最早的最该先修）。"""
    return [x for x in load_all()
            if x.get("kind") in ACTIONABLE and x.get("status") == "open"]


def _last_ack(channel: str):
    state = _read_json(STATE_FILE, {})
    v = state.get(channel) if isinstance(state, dict) else None
    try:
        return datetime.fromisoformat(v) if v else None
    except ValueError:
        return None


def claim_reminder(channel: str) -> list:
    """原子地「检查到期 + 确认」：并发调用只有一个拿到列表（hook 并行触发时不重复提醒）。"""
    with _locked():
        due = reminder_due(channel)
        if due:
            state = _read_json(STATE_FILE, {})
            state = state if isinstance(state, dict) else {}
            state[channel] = _now()
            _write_json(STATE_FILE, state)
        return due


def reminder_due(channel: str) -> list:
    """到期返回待修反馈列表，否则返回 []。从未确认过的通道视为到期。"""
    pending = open_actionable()
    if not pending:
        return []
    last = _last_ack(channel)
    if last and datetime.now() - last < timedelta(days=REMIND_DAYS):
        return []
    return pending


def ack(channel: str) -> None:
    with _locked():
        state = _read_json(STATE_FILE, {})
        if not isinstance(state, dict):
            state = {}
        state[channel] = _now()
        _write_json(STATE_FILE, state)


def format_reminder(items: list) -> str:
    """多行纯文本提醒（终端 / hook 共用）。"""
    lines = [f"📮 有 {len(items)} 条日报反馈待修（每 {REMIND_DAYS} 天提醒一次，请先处理再做新功能）："]
    for x in items:
        where = x.get("digest_date") or "-"
        if x.get("item_title") or x.get("item_id"):
            where += f" · {x.get('item_title') or x.get('item_id')}"
        kind = x.get("kind", "")
        lines.append(f"  [{KINDS.get(kind, kind)}] {x.get('id', '?')}（{where}）：{x.get('text', '')}")
    lines.append("  处理页：http://localhost:5050/feedback（修完后标记「已修复」）")
    return "\n".join(lines)
