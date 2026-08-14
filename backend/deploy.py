"""
站点自动部署：commit + push → 触发 GitHub Actions 重建（见 .github/workflows/deploy.yml）。

为什么需要：站点的搜索索引 index.json 由 Hugo 在「构建时」自动生成，线上部署由 CI 在
push 到 main 时触发。后端写入 content/ 之后，必须有一次 commit+push 才能让线上索引更新。

对外接口：
- trigger_deploy(reason)   防抖触发。短时间内多次调用（如连续录入多条）会合并为一次 commit+push，
                           在最后一次调用后静默 DEBOUNCE_SEC 秒再执行。永不阻塞、永不上抛异常。
- deploy_now(reason, force) 立即同步执行，供「重建并部署」按钮使用。force=True 时即使无内容变更
                           也创建一次空提交，强制触发 CI（用于改了配置/模板后重建）。

安全说明：所有 git 操作以 GIT_TERMINAL_PROMPT=0 运行，未配置凭据时快速失败而非交互挂起；
只暂存 content/ 目录，不会误提交 .omc/ 等运行时产物；部署失败绝不阻断内容写入。
"""
import os
import time
import threading
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEBOUNCE_SEC = float(os.environ.get("DEPLOY_DEBOUNCE", "30"))
PUSH_TIMEOUT = int(os.environ.get("DEPLOY_PUSH_TIMEOUT", "120"))

_deploy_lock = threading.Lock()       # 同一时刻只允许一个 commit+push
_cond = threading.Condition()
_pending = []                          # 累积的触发原因
_last_trigger = [time.monotonic()]
_started = False
_start_lock = threading.Lock()


def _env():
    e = dict(os.environ)
    e["GIT_TERMINAL_PROMPT"] = "0"    # 无凭据时直接失败，不交互挂起
    return e


def _git(args):
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT)] + args,
        capture_output=True, text=True, env=_env(), timeout=PUSH_TIMEOUT,
    )


def _has_content_changes():
    r = _git(["status", "--porcelain", "--", "content/"])
    return r.returncode == 0 and bool(r.stdout.strip())


def _commit_and_push(reasons, force=False):
    """暂存 content/ 并 commit + push。返回结果 dict，永不抛异常。"""
    try:
        _git(["add", "--", "content/"])
        changed = _has_content_changes()
        if not changed and not force:
            return {"ok": True, "changed": False,
                    "message": "无内容变更，跳过提交（如改了配置/模板，勾选「强制重建」再试）"}

        msg = "auto(content): 更新日报内容\n\n" + "\n".join(f"- {r}" for r in reasons)
        cargs = ["commit"]
        if not changed and force:
            cargs.append("--allow-empty")
        cargs += ["-m", msg]
        c = _git(cargs)
        if c.returncode != 0:
            return {"ok": False, "changed": changed, "pushed": False,
                    "message": "提交失败：" + (c.stderr or c.stdout).strip()}

        p = _git(["push", "origin", "HEAD"])
        if p.returncode != 0:
            hint = ""
            if "not fast-forward" in (p.stderr or "") or "non-fast-forward" in (p.stderr or ""):
                hint = "（远端有新提交，请先 git pull --rebase）"
            return {"ok": False, "changed": True, "pushed": False,
                    "message": "推送失败：" + (p.stderr or p.stdout).strip() + hint}

        sha = _git(["rev-parse", "--short", "HEAD"]).stdout.strip()
        return {"ok": True, "changed": True, "pushed": True, "sha": sha,
                "message": "已提交并推送，CI 将自动重建站点（约 1-2 分钟后线上生效）"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "changed": False, "pushed": False,
                "message": "git 操作超时（凭据未配置或网络问题）"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "changed": False, "pushed": False,
                "message": f"部署异常：{e}"}


def _worker():
    """后台 worker：收集触发原因，静默防抖后批量 commit+push。"""
    while True:
        with _cond:
            while not _pending:
                _cond.wait()
            # 静默防抖：距最后一次触发不足 DEBOUNCE_SEC 就继续等（新触发会延后窗口）
            while time.monotonic() - _last_trigger[0] < DEBOUNCE_SEC:
                _cond.wait(DEBOUNCE_SEC)
            reasons = list(_pending)
            _pending.clear()
        with _deploy_lock:
            _commit_and_push(reasons)


def _ensure_worker():
    global _started
    with _start_lock:
        if not _started:
            threading.Thread(target=_worker, daemon=True, name="deploy-worker").start()
            _started = True


def trigger_deploy(reason="content updated"):
    """防抖触发部署。合并短时间内的多次调用为一次 commit+push。"""
    _ensure_worker()
    with _cond:
        _pending.append(reason)
        _last_trigger[0] = time.monotonic()
        _cond.notify_all()


def deploy_now(reason="手动触发", force=False):
    """立即同步部署。force=True 时即使无变更也空提交强制触发 CI。"""
    _ensure_worker()
    with _cond:
        reasons = [reason] + list(_pending)
        _pending.clear()
    with _deploy_lock:
        return _commit_and_push(reasons, force=force)


# 仅用于自测/调试：直接运行本文件可打印当前内容变更状态，不做任何提交。
if __name__ == "__main__":
    print("REPO_ROOT:", REPO_ROOT)
    print("content has changes:", _has_content_changes())
