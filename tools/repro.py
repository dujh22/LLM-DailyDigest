#!/usr/bin/env python3
"""相关工作复现注册工具（规范见 content/papers/README.md）。

用法：
  python3 tools/repro.py new <研究> <data|method|eval|other> <短语> [--title 标题] [--paper URL] [--code URL]
  python3 tools/repro.py check        # 校验目录结构与 reused_by，并打印各工作进度

只用标准库（兼容 Python 3.9），进度口径与 layouts/partials/papers/progress.html 一致。
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "content" / "papers"
RESEARCH = ROOT / "content" / "research"
CATEGORIES = ("data", "method", "eval", "other")
CATEGORY_DESC = {"data": "数据", "method": "方法", "eval": "评测", "other": "其他"}
SUBDIRS = ("paper", "resources", "repro", "cache")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")

NOTE_TEMPLATE = """+++
title = '{title}'
date = {date}
draft = false
toc = true
layout = 'repro'
paper = '{paper}'          # 论文主页（arXiv abs 等）
code = '{code}'           # 官方代码仓库
paper_en = ''      # 可选：英文原文外链（不入库时填，如网盘）
paper_zh = ''      # 可选：中文译文外链
reused_by = []     # 被哪些 content/research 研究二次利用，如 ['EvolveLLM']（填写即达 80%）
[build]
  publishResources = false   # 只发布页面引用到的资源（PDF 站内打开），代码等跳 GitHub
+++

> **一句话速读**：*（待补充）*

## 论文信息

- **论文**：{paper}
- **代码**：{code}
- **作者 / 机构 / 发表**：
- **所属研究**：[{research}](/research/{research_lower}/) · {category}（{category_desc}）

## 论文要点

### 解决什么问题

### 核心方法

### 关键结果

### 局限

## 可复用资源

> 详见 `resources/`。大文件不入库，写明来源与下载命令（下载到 `cache/`，已被 git / Hugo 忽略）。

| 资源 | 类型 | 来源 / 下载方式 | 版本（commit / 哈希） | 备注 |
|---|---|---|---|---|

## 复现记录

### 环境

- 硬件：
- 依赖：（锁定文件放 `repro/`，如 `requirements.txt` / `environment.yml`）
- 上游代码 commit：

### 运行命令

### 结果对照

| 指标 | 论文报告 | 本人复现 | 差异原因 |
|---|---|---|---|

### 踩坑

## 二次利用

> 记录本工作被哪些研究用到、用在哪里（同步维护 front matter `reused_by`）。

## 进展日志

- {today}：注册
"""

SECTION_TEMPLATE = """+++
title = '{title}'
date = {date}
draft = false
+++
"""


def research_names():
    return {p.stem for p in RESEARCH.glob("*.md") if not p.name.startswith("_")}


def now_str():
    return dt.datetime.now().astimezone().replace(microsecond=0).isoformat()


def ensure_section(path: Path, title: str):
    idx = path / "_index.md"
    if not idx.exists():
        path.mkdir(parents=True, exist_ok=True)
        idx.write_text(SECTION_TEMPLATE.format(title=title, date=now_str()), encoding="utf-8")


def cmd_new(a):
    if a.research not in research_names():
        sys.exit(f"未知研究：{a.research}（须为 content/research/ 下的文件名，区分大小写）")
    if a.category not in CATEGORIES:
        sys.exit(f"类别须为 {'/'.join(CATEGORIES)}")
    if not SLUG_RE.match(a.slug):
        sys.exit("短语只用小写字母、数字、连字符，如 self-rewarding-lm")
    work = PAPERS / a.research / a.category / a.slug
    if work.exists():
        sys.exit(f"已存在：{work.relative_to(ROOT)}")
    ensure_section(PAPERS / a.research, a.research)
    ensure_section(PAPERS / a.research / a.category, f"{a.research} · {a.category}（{CATEGORY_DESC[a.category]}）")
    for d in SUBDIRS:
        (work / d).mkdir(parents=True)
        (work / d / ".gitkeep").touch()
    (work / "index.md").write_text(NOTE_TEMPLATE.format(
        title=(a.title or a.slug).replace("'", "’"), date=now_str(), paper=a.paper, code=a.code,
        research=a.research, research_lower=a.research.lower(), category=a.category,
        category_desc=CATEGORY_DESC[a.category], today=dt.date.today().isoformat(),
    ), encoding="utf-8")
    print(f"已注册：{work.relative_to(ROOT)}")


def real_files(d: Path):
    return [p for p in d.rglob("*") if p.is_file() and not p.name.startswith(".")] if d.is_dir() else []


def front_value(text, key):
    m = re.search(rf"^{key}\s*=\s*(.+?)\s*(#.*)?$", text, re.M)
    return m.group(1) if m else ""


def git_lastmod(path: Path):
    out = subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(path)],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return dt.datetime.fromtimestamp(int(out)) if out else dt.datetime.now()


def progress(work: Path):
    text = (work / "index.md").read_text(encoding="utf-8")
    paper = [p.stem for p in real_files(work / "paper")]
    en = any(s.endswith("en") for s in paper) or front_value(text, "paper_en") not in ("", "''", '""')
    zh = any(s.endswith("zh") for s in paper) or front_value(text, "paper_zh") not in ("", "''", '""')
    reused = re.findall(r"['\"]([^'\"]+)['\"]", front_value(text, "reused_by"))
    days = (dt.datetime.now() - git_lastmod(work / "index.md")).days
    steps = [(20, en and zh), (40, bool(real_files(work / "resources"))),
             (60, bool(real_files(work / "repro"))), (80, bool(reused)), (100, bool(reused) and days >= 365)]
    pct = 0
    for p, ok in steps:
        if not ok:
            break
        pct = p
    return pct, reused


def cmd_check(_):
    names, errors = research_names(), []
    for work in sorted(PAPERS.glob("*/*/*/index.md")):
        work = work.parent
        research, category = work.parts[-3], work.parts[-2]
        rel = work.relative_to(ROOT)
        if research not in names:
            errors.append(f"{rel}：研究名 {research} 不在 content/research/")
        if category not in CATEGORIES:
            errors.append(f"{rel}：类别 {category} 不合法")
        for d in ("paper", "resources", "repro"):
            if not (work / d).is_dir():
                errors.append(f"{rel}：缺少 {d}/")
        pct, reused = progress(work)
        errors += [f"{rel}：reused_by 中 {r} 不在 content/research/" for r in reused if r not in names]
        print(f"{pct:>3}%  {rel}")
    for e in errors:
        print("✗", e)
    sys.exit(1 if errors else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new", help="注册一个复现工作")
    n.add_argument("research")
    n.add_argument("category")
    n.add_argument("slug")
    n.add_argument("--title", default="")
    n.add_argument("--paper", default="")
    n.add_argument("--code", default="")
    n.set_defaults(func=cmd_new)
    sub.add_parser("check", help="校验并打印进度").set_defaults(func=cmd_check)
    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
