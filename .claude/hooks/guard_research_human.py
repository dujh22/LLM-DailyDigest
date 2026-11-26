#!/usr/bin/env python3
"""Claude Code PreToolUse 守卫：研究页「自研洞察 / 自研经验」只允许人类手动修改。

- Edit / MultiEdit / Write 目标是 content/research/*.md 时，推演改动后的全文，
  与当前文件比对两个人类专属栏目的完整原文（规则见 backend/research_sections.human_violations）；
  有改动 → permissionDecision=ask，强制弹窗询问人类，人类同意才放行。
- Bash 命令涉及研究页且像是写操作（重定向 / sed -i / tee / mv / cp / rm / 脚本…）、或是可能丢弃未提交
  改动的 git 命令（checkout / restore / reset / stash / clean，不论路径）→ 同样询问，
  因为 shell 改写无法事先推演结果。Bash 守卫是尽力而为的启发式，不保证覆盖所有写法。
- 执行任意代码的 MCP 工具（python_repl / executeCode）代码中涉及研究页时询问。
- 改动守卫自身（本 hook、backend/research_sections.py、.claude/settings*.json）时询问，防止被关闭。
- 其余情况不输出任何内容，交给正常权限流程。hook 自身出错时：涉及研究页则询问，否则放行。
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "backend"))
import research_sections  # noqa: E402

RESEARCH_DIR = (ROOT / "content" / "research").resolve()
GUARD_FILES = [ROOT / ".claude" / "hooks" / "guard_research_human.py",
               ROOT / "backend" / "research_sections.py",
               ROOT / ".claude" / "settings.json", ROOT / ".claude" / "settings.local.json"]
_BASH_WRITE_RE = re.compile(
    r"(>|\btee\b|\bsed\b.*(\s-[a-zA-Z]*i|--in-place)|\bperl\b.*\s-[a-zA-Z]*i|\bawk\b.*inplace|"
    r"\b(mv|cp|rm|truncate|dd|rsync|ln|install|python3?|node|ruby|bash|sh|zsh)\b|"
    r"\bgit\s+(mv|rm|apply|am|merge|rebase|pull|cherry-pick|revert))")
_GIT_DISCARD_RE = re.compile(r"\bgit\s+(checkout|restore|reset|stash|clean|switch)\b")
_RESEARCH_HINT_RE = re.compile(r"research", re.I)


def _norm(p) -> str:
    """macOS 文件系统不区分大小写且路径可能是 NFD：比较前统一 NFC + 小写。"""
    return unicodedata.normalize("NFC", str(p)).lower()


def ask(reason: str):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": reason,
    }}, ensure_ascii=False))
    sys.exit(0)


def research_path(p: str):
    if not p:
        return None
    path = Path(p)
    if not path.is_absolute():
        path = Path(os.getcwd()) / path
    path = path.resolve()
    return path if _norm(path.parent) == _norm(RESEARCH_DIR) and _norm(path.suffix) == ".md" else None


def is_guard_file(p: str) -> bool:
    if not p:
        return False
    path = Path(p) if Path(p).is_absolute() else Path(os.getcwd()) / p
    return _norm(path.resolve()) in {_norm(g.resolve()) for g in GUARD_FILES}


def apply_edit(text: str, old: str, new: str, replace_all: bool) -> str:
    if old not in text:
        # Edit 工具可能做引号 / 换行归一化后再匹配，无法精确推演 → 交给人类判断
        ask("无法精确推演本次编辑对研究页的影响（old_string 未逐字命中）。"
            "研究页「自研洞察 / 自研经验」只允许人类修改，请确认本次编辑不涉及这两个栏目。")
    return text.replace(old, new) if replace_all else text.replace(old, new, 1)


def main():
    data = json.load(sys.stdin)
    tool, inp = data.get("tool_name", ""), data.get("tool_input", {}) or {}
    if tool == "Bash":
        cmd = inp.get("command", "")
        if _GIT_DISCARD_RE.search(cmd):
            ask("该 git 命令可能丢弃工作区未提交改动，其中可能包含人类在研究页「自研洞察 / 自研经验」"
                "中的手写内容。请人类确认后再放行。")
        if _RESEARCH_HINT_RE.search(cmd) and _BASH_WRITE_RE.search(cmd):
            ask("该命令可能改写 content/research/ 研究页；其中「自研洞察 / 自研经验」只允许人类修改。"
                "请人类确认本次操作不会改动这两个栏目（或明确同意改动）后再放行。")
        return
    if tool.startswith("mcp__"):
        code = json.dumps(inp, ensure_ascii=False)
        if _RESEARCH_HINT_RE.search(code):
            ask("该代码执行可能改写 content/research/ 研究页；其中「自研洞察 / 自研经验」只允许人类修改。"
                "请人类确认后再放行。")
        return
    if tool not in ("Edit", "MultiEdit", "Write"):
        return
    if is_guard_file(inp.get("file_path", "")):
        ask("本次编辑会改动研究页人类专属栏目的守卫（hook / research_sections.py / settings），"
            "可能削弱「自研洞察 / 自研经验」的保护。请人类确认后再放行。")
    path = research_path(inp.get("file_path", ""))
    if not path:
        return
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if tool == "Write":
        new = inp.get("content", "")
    elif tool == "Edit":
        new = apply_edit(old, inp.get("old_string", ""), inp.get("new_string", ""),
                         bool(inp.get("replace_all")))
    else:
        new = old
        for e in inp.get("edits", []) or []:
            new = apply_edit(new, e.get("old_string", ""), e.get("new_string", ""),
                             bool(e.get("replace_all")))
    bad = research_sections.human_violations(old, new)
    if bad:
        ask(f"{path.name}：" + "；".join(bad) + "。「自研洞察 / 自研经验」只允许人类手动修改，"
            "AI 必须先征得人类同意——同意请放行，否则拒绝。")


if __name__ == "__main__":
    raw = sys.stdin.read()
    try:
        sys.stdin = __import__("io").StringIO(raw)
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        if _RESEARCH_HINT_RE.search(raw):
            ask(f"研究页守卫 hook 出错（{e}），无法判断本次操作是否改动人类专属栏目，请人类确认。")
        sys.exit(0)
