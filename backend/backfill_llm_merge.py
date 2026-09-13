"""
一次性回填脚本：把此前「未勾选 LLM 合并」的去重归并条目补做 LLM 字段整合。

背景：/dedup 执行时未勾选 LLM 合并的组，summary/content/purpose 按规则合并，
会留下 "[合并自 <日期> <id>]" 标记拼接的多段文本。本脚本扫描 content/updates/
全部日报，找出解析字段（summary/content/purpose）中含该标记的条目，逐条调用
LLM 整合为一份连贯内容后原位改写。notes 原始笔记逐字保留，永不改动。

用法：
  python backend/backfill_llm_merge.py            # 全量执行
  python backend/backfill_llm_merge.py --dry-run  # 只扫描并打印将处理的条目
  python backend/backfill_llm_merge.py --limit 3  # 只处理前 N 条（试跑）

安全性：写盘前重读文件并校验条目 id 与待改字段值仍与扫描时一致，
不一致的条目跳过；LLM 失败或返回仍含标记的字段保持原样。不触发自动部署。
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import app

MERGE_TAG = "[合并自"
WORKERS = 8

_SYSTEM_PROMPT = (
    "你是大模型研究日报的条目整理助手。此前多个重复条目按规则合并，"
    "字段里残留了以「[合并自 日期 id]」标记拼接的多段文本，现在需要你把每个字段"
    "整合为一份连贯内容：\n"
    "- summary: 一句话中文摘要。\n"
    "- content: 正文要点，中文 3~5 句，可用 markdown。\n"
    "- purpose: 用途与启示，markdown 无序列表（每条以 - 开头）。\n"
    "要求：语义去重、信息补全，不虚构事实，不丢失任何独有信息，"
    "删除所有「[合并自 …]」标记，保持中文为主、术语风格一致；"
    "输入中某字段为空时该字段返回空字符串。"
    "严格返回 JSON 对象（不要代码块、不要解释）："
    '{"summary": "...", "content": "...", "purpose": "..."}'
)


def scan_tagged_items():
    """扫描全部日报，返回 [{path, index, item, fields}]，fields 为含标记的字段名列表。"""
    out = []
    for path in sorted(app.UPDATES_DIR.glob("*.md")):
        _, fm_body, _ = app.split_front_matter(path.read_text(encoding="utf-8"))
        if not fm_body:
            continue
        _, blocks = app.split_item_blocks(fm_body)
        for idx, block in enumerate(blocks):
            item = app._parse_item_block(block)
            if not item:
                continue
            fields = [f for f in app._LLM_MERGE_FIELDS
                      if MERGE_TAG in (item.get(f) or "")]
            if fields:
                out.append({"path": path, "index": idx, "item": item,
                            "fields": fields})
    return out


def llm_consolidate(entry, api_key) -> dict:
    """对单条目调用 LLM 整合三个解析字段，返回 {字段: 新值}（仅含通过校验的字段）。"""
    from openai import OpenAI
    it = entry["item"]
    payload = {
        "标题": it.get("title", ""),
        "summary": it.get("summary", "") or "",
        "content": it.get("content", "") or "",
        "purpose": it.get("purpose", "") or "",
    }
    client = OpenAI(api_key=api_key, base_url=app.LLM_BASE_URL)
    resp = client.chat.completions.create(
        model=app.LLM_MODEL,
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    cleaned = (resp.choices[0].message.content or "").strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    parsed = json.loads(cleaned)
    # 只替换扫描时含标记的字段；新值必须非空且不再含标记，否则保持原样
    result = {}
    for f in entry["fields"]:
        v = parsed.get(f)
        v = v.strip() if isinstance(v, str) else ""
        if v and MERGE_TAG not in v:
            result[f] = v
    return result


def apply_updates(entries_with_values):
    """按文件分组写盘。写前重读校验：条目 id 与待改字段值仍与扫描时一致才改。"""
    by_file = {}
    for entry, vals in entries_with_values:
        by_file.setdefault(entry["path"], []).append((entry, vals))
    written, skipped_stale = [], 0
    for path, pairs in sorted(by_file.items()):
        _, fm_body, _ = app.split_front_matter(path.read_text(encoding="utf-8"))
        _, blocks = app.split_item_blocks(fm_body) if fm_body else (None, [])
        replace = {}
        for entry, vals in pairs:
            idx = entry["index"]
            fresh = app._parse_item_block(blocks[idx]) if idx < len(blocks) else None
            if (not fresh
                    or fresh.get("id") != entry["item"].get("id")
                    or any(fresh.get(f) != entry["item"].get(f)
                           for f in entry["fields"])):
                skipped_stale += 1
                continue
            new_item = dict(fresh)
            new_item.update(vals)
            replace[idx] = new_item
        if replace and app.rewrite_daily_items(path, replace=replace):
            written.append((path.name, len(replace)))
    return written, skipped_stale


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    entries = scan_tagged_items()
    print(f"扫描到 {len(entries)} 条含 [合并自] 标记的条目")
    if args.limit:
        entries = entries[:args.limit]
        print(f"--limit：只处理前 {len(entries)} 条")
    if args.dry_run:
        for e in entries:
            print(f"  {e['path'].name} 块#{e['index']} id={e['item'].get('id', '')} "
                  f"字段={','.join(e['fields'])}")
        return
    if not entries:
        return

    api_key = app.load_api_key()
    if not api_key:
        sys.exit("未找到 API Key（仓库根目录 api_key.txt）")

    ok_pairs, failed = [], []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [(e, ex.submit(llm_consolidate, e, api_key)) for e in entries]
        for e, fu in futures:
            label = f"{e['path'].name}#{e['index']} {e['item'].get('id', '')}"
            try:
                vals = fu.result()
            except Exception as err:  # noqa: BLE001
                failed.append(f"{label}: {err}")
                continue
            if vals:
                ok_pairs.append((e, vals))
                print(f"✓ {label} 整合字段：{','.join(vals)}")
            else:
                failed.append(f"{label}: LLM 返回为空或仍含标记，保持原样")

    written, skipped_stale = apply_updates(ok_pairs)
    print(f"\n完成：LLM 成功 {len(ok_pairs)} 条 / 失败 {len(failed)} 条 / "
          f"写盘前校验跳过 {skipped_stale} 条")
    for name, n in written:
        print(f"  改写 {name}：{n} 条")
    if failed:
        print("失败明细（保持原样，可重跑本脚本）：")
        for line in failed:
            print(f"  ✗ {line}")


if __name__ == "__main__":
    main()
