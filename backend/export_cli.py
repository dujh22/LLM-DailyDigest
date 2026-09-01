"""
LLM-DailyDigest 导出命令行入口 —— 供外部项目以子进程方式调用（推荐）。

外部项目无需安装本仓库依赖、无 import 命名冲突风险：用本仓库自带的 venv python
执行本脚本即可，与调用方项目的环境完全隔离。

用法：
  <仓库>/backend/venv/bin/python <仓库>/backend/export_cli.py link <url> <out_dir>
  <仓库>/backend/venv/bin/python <仓库>/backend/export_cli.py research <name> <out_dir>

输出：stdout 打印一行 JSON（成功时含 file = 导出文件绝对路径）。
退出码：0 成功；1 导出失败（JSON 里有 errors）；2 参数用法错误。
抓取走进程继承的网络环境；直连不通时请在调用前设置 https_proxy。
"""
import json
import sys
from pathlib import Path

# 保证无论从哪个目录调用，都能 import 到同目录的 app 模块
sys.path.insert(0, str(Path(__file__).resolve().parent))
import app  # noqa: E402


def main(argv):
    if len(argv) != 3 or argv[0] not in ("link", "research"):
        print(json.dumps({"ok": False, "errors": [
            "用法：export_cli.py link <url> <out_dir> 或 export_cli.py research <name> <out_dir>"
        ]}, ensure_ascii=False))
        return 2
    cmd, arg, out_dir = argv
    fn = app.export_link_to_md if cmd == "link" else app.export_research_to_md
    res = fn(arg, out_dir)
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
