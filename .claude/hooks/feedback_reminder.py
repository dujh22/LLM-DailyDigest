#!/usr/bin/env python3
"""
PreToolUse hook：Claude 读/改 backend/app.py 时，若有未修的日报反馈且距上次提醒 ≥ 7 天，
注入上下文让 Claude 先提醒人类处理这些反馈。注入即确认（claude 通道），一周最多一次。
逻辑与数据见 backend/feedback.py。任何异常都静默放行，绝不阻断工具调用。
"""
import json
import os
import sys
from pathlib import Path


def main():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        return
    if payload.get("agent_id"):
        return  # 子代理读 app.py 时不提醒：其上下文不会直达用户，提醒会被白白确认掉
    path = (payload.get("tool_input") or {}).get("file_path") or ""
    if not path.replace("\\", "/").endswith("backend/app.py"):
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
    sys.path.insert(0, str(root / "backend"))
    import feedback

    due = feedback.claim_reminder("claude")  # 检查+确认原子完成，并行触发只提醒一次
    if not due:
        return
    msg = (feedback.format_reminder(due)
           + "\n\n【给 Claude】这是每周一次的日报反馈提醒：在继续当前任务前，先把上面待修的反馈"
             "列给用户，询问是否先修这些不满意的地方；修完后可调 POST /api/feedback/<id> "
             "{\"status\":\"fixed\",\"resolution\":\"…\"} 或让用户在 /feedback 页标记。")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "additionalContext": msg}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001
        pass
    sys.exit(0)
