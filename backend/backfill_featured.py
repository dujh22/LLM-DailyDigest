"""为历史日报补生成「重点条目」featured 列表（并同步重生成头部摘要）。

用法：
    ./venv/bin/python backfill_featured.py 2026-09-29 2026-09-30 2026-10-01
    ./venv/bin/python backfill_featured.py --days 3        # 最近 3 天（含今天）
    ./venv/bin/python backfill_featured.py --deploy ...    # 写完后触发自动部署（默认不触发）
    ./venv/bin/python backfill_featured.py --allow-today 2026-10-01

只调用 LLM 摘要 + 写 featured / 摘要块，不做去重归并；默认不触发 git 提交/部署，
便于先用 hugo server 预览再手动提交。本脚本是独立进程，不受服务端 _SUBMIT_LOCK 保护，
因此默认跳过「今天」的日报（服务可能正在追加条目），确有需要加 --allow-today。
"""
import sys
from datetime import date, timedelta

import app


def main(argv):
    deploy = "--deploy" in argv
    allow_today = "--allow-today" in argv
    argv = [a for a in argv if a not in ("--deploy", "--allow-today")]
    if "--days" in argv:
        n = int(argv[argv.index("--days") + 1])
        days = [(date.today() - timedelta(days=i)).isoformat() for i in range(n)]
    else:
        days = argv
    if not days:
        print(__doc__)
        return 1
    if not deploy:
        app.trigger_deploy = lambda *a, **k: None
    for d in sorted(days):
        if d == date.today().isoformat() and not allow_today:
            print(f"[{d}] 是今天的日报，默认跳过（服务可能正在写入）；需要时加 --allow-today")
            continue
        items = app.parse_day_items(d)
        if not items:
            print(f"[{d}] 无条目或日报不存在，跳过")
            continue
        try:
            md, featured = app.llm_daily_summary(d, items)
        except Exception as e:  # noqa: BLE001
            print(f"[{d}] 摘要生成失败：{e}")
            continue
        changed = app.write_daily_summary(d, md, featured)
        if featured is None:
            print(f"[{d}] 条目 {len(items)} → 摘要{'已更新' if changed else '无变化'}；"
                  "LLM 未给出重点列表，featured 保持原状")
        else:
            print(f"[{d}] 条目 {len(items)} → 重点 {len(featured)} 条 "
                  f"{'（已写入）' if changed else '（无变化）'}：{', '.join(featured)}")
        if changed and deploy:
            app.trigger_deploy(f"补生成重点条目 {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
