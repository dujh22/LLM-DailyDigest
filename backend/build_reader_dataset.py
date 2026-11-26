"""
读后感数据集导出：从日报条目直接构建「读者兴趣点抽取」数据集。

每条带 reader_note 的日报条目即一个样本：
  query         notes（批处理录入的原始信息正文，已剥离读后感）
  ground_truth  reader_note（读者读后自述的关键认识）
  model_output  当时 LLM 抽取写入日报的字段（summary / content / purpose / insight…），
                可作为基线预测与 ground_truth 对比，评估/优化抽取 prompt
抽取时 LLM 看不到读后感（见 app.split_reader_note / llm_extract），因此不存在标签泄漏。

用法（在 backend/ 下）：
  ./venv/bin/python build_reader_dataset.py                    # 统计 + 导出 records 格式
  ./venv/bin/python build_reader_dataset.py --since 2026-12-01
  ./venv/bin/python build_reader_dataset.py --format sft       # chat messages 格式，可直接用于 SFT
  ./venv/bin/python build_reader_dataset.py --fetch            # 额外抓取链接正文作为 sources（还原抽取时模型的输入）
输出：仓库根 data/reader_dataset/reader_notes.<format>.jsonl（派生产物，已 gitignore，随时可重建）
"""
import argparse
import json
import sys
from pathlib import Path

import app

OUT_DIR = app.REPO_ROOT / "data" / "reader_dataset"
MODEL_FIELDS = ("title", "subtopic", "topics", "keywords", "summary", "content", "purpose", "insight")
SFT_SYSTEM = ("你是大模型研究日报的读者兴趣点抽取助手。阅读一条资讯原文（及其链接内容），"
              "写出这位读者读完后最可能获得的关键认识：只写对读者有增量的信息与判断，不复述常识。")


def iter_samples(since: str = "", until: str = ""):
    """遍历日报，产出带读后感的样本 dict（按日期升序）。"""
    for path in sorted(app.UPDATES_DIR.glob("????-??-??.md")):
        d = path.stem
        if (since and d < since) or (until and d > until):
            continue
        for _, item in app.parse_day_items(d):
            note = (item.get("reader_note") or "").strip()
            if not note:
                continue
            yield {
                "sample_id": f"{d}/{item.get('id', '')}",
                "date": d,
                "item_id": item.get("id", ""),
                "query": (item.get("notes") or "").strip(),
                "ground_truth": note,
                "links": {k: item.get(k, "") for k in ("paper", "code", "dataset", "link")
                          if item.get(k)},
                "model_output": {k: item[k] for k in MODEL_FIELDS if item.get(k)},
                "research": item.get("research", []),
                "score": item.get("score"),
                # 去重归并过的条目：读后感/解析字段是多条拼接或 LLM 整合的，训练时可按需过滤
                "merged": any(app._MERGE_TAG_PREFIX in (item.get(f) or "")
                              for f in ("notes", "reader_note")),
            }


def attach_sources(sample: dict) -> None:
    """抓取 query 中的链接正文（与抽取时 resolve_all 同一套抓取器）。"""
    _, _, texts = app.resolve_all(sample["query"])
    sample["sources"] = texts


def to_sft(sample: dict) -> dict:
    user = sample["query"]
    if sample.get("sources"):
        user += "\n\n===== 链接内容 =====\n\n" + "\n\n".join(sample["sources"])
    return {"sample_id": sample["sample_id"],
            "messages": [{"role": "system", "content": SFT_SYSTEM},
                         {"role": "user", "content": user},
                         {"role": "assistant", "content": sample["ground_truth"]}]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="从日报条目导出读后感数据集")
    ap.add_argument("--since", default="", help="起始日期 YYYY-MM-DD（含）")
    ap.add_argument("--until", default="", help="截止日期 YYYY-MM-DD（含）")
    ap.add_argument("--format", choices=("records", "sft"), default="records")
    ap.add_argument("--fetch", action="store_true", help="抓取链接正文写入 sources（慢，需网络）")
    ap.add_argument("--out", default="", help="输出文件路径（默认 data/reader_dataset/reader_notes.<format>.jsonl）")
    args = ap.parse_args(argv)

    samples = list(iter_samples(args.since, args.until))
    if args.fetch:
        for i, s in enumerate(samples, 1):
            attach_sources(s)
            print(f"\r抓取链接 {i}/{len(samples)}", end="", file=sys.stderr)
        print(file=sys.stderr)
    rows = [to_sft(s) for s in samples] if args.format == "sft" else samples

    out = Path(args.out) if args.out else OUT_DIR / f"reader_notes.{args.format}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    days = sorted({s["date"] for s in samples})
    span = f"{days[0]} ~ {days[-1]}，{len(days)} 天" if days else "无"
    merged = sum(1 for s in samples if s["merged"])
    print(f"✓ {len(rows)} 个样本（{span}；其中 {merged} 个来自归并条目，records 中 merged=true）→ {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
