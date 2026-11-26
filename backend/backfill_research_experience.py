"""用历史日报为研究页回填「研究经验」栏目（日常由当日整备 finalize 自动增量更新）。

用法：
    ./venv/bin/python backfill_research_experience.py --days 30            # 最近 30 天日报，全部研究
    ./venv/bin/python backfill_research_experience.py --days 30 MemoryEvolve DataEvolve
    ./venv/bin/python backfill_research_experience.py --all MemoryEvolve   # 全部历史日报
    ./venv/bin/python backfill_research_experience.py --deploy ...         # 写完后触发自动部署（默认不触发）

条目按日期升序、每 EXPERIENCE_CHUNK 条一批送 LLM 增量合并；已判定过的条目自动跳过，可重复执行。
只改各研究页 research-experience 标记对之间的块，「自研洞察 / 自研经验」人类专属栏目逐字不动。
默认不触发 git 提交/部署，便于先用 hugo server 预览再手动提交。
"""
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

import app


def main(argv):
    deploy = "--deploy" in argv
    use_all = "--all" in argv
    argv = [a for a in argv if a not in ("--deploy", "--all")]
    days = None
    if "--days" in argv:
        i = argv.index("--days")
        days = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if days is None and not use_all:
        print(__doc__)
        return 1
    names = app.valid_research()
    if argv:
        unknown = [n for n in argv if n not in names]
        if unknown:
            print("未知研究：" + "、".join(unknown))
            return 1
        names = argv
    since = "" if use_all else (date.today() - timedelta(days=days - 1)).isoformat()
    items = app._collect_research_items(names)

    def run(n):
        dated = [(d, it) for d, it in items[n] if d >= since]
        return n, app.update_research_experience(n, dated)

    updated = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for f in [ex.submit(run, n) for n in names]:
            try:
                n, r = f.result()
            except Exception as e:  # noqa: BLE001
                print(f"失败：{e}")
                continue
            print(f"[{n}] 新判定 {r['fresh']} 条 → 经验 {r['experiences']} 条"
                  f"{'（已写入）' if r['changed'] else '（无变化）'}")
            if r["changed"]:
                updated.append(n)
    if updated and deploy:
        # 独立进程马上退出，防抖的 trigger_deploy 来不及执行，这里同步部署
        print(app.deploy_now("回填研究经验：" + "、".join(updated)).get("message"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
