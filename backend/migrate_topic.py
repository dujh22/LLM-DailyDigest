"""
主题内容批量迁移脚本（全自动，LLM 驱动）

把 content/topic/<主题>.md 正文里的历史条目，拆分 → 逐条送 LLM 结构化（含日期推断）
→ 按条目日期写入 content/updates/<date>.md 的 [[items]]，自动索引回主题页。

用法：
  python migrate_topic.py --topic 智能体                # 迁移单个主题
  python migrate_topic.py --topic 智能体 --dry         # 预览不写盘
  python migrate_topic.py --topic 智能体 --max 100     # 本次最多处理 100 条（默认）
  python migrate_topic.py --all --workers 4            # 迁移全部主题，4 并发

依赖 backend/app.py 的 LLM 与写入逻辑；API Key 读仓库根目录 api_key.txt。
"""
import sys
import re
import json
import argparse
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).resolve().parent))
import app  # noqa: E402  复用 load_api_key / valid_topics / append_item 等

# 顶级锚点（行首，无缩进）：日期 / 数字列表 / **标题**
ANCHOR_RE = re.compile(
    r'^(\d{4}[-/. ]?\d{1,2}[-/. ]?\d{1,2}'   # 2025-06-09 / 2025.06.09 / 2025 06 09
    r'|\d{8}\b'                                # 20250604
    r'|\d+\.\s'                                # 1. / 2.（顶格）
    r'|\*\*标题\*\*)'                          # **标题**：...
)


def split_entries(body: str):
    """按顶级锚点把正文拆成候选条目块。"""
    chunks, cur = [], []
    for ln in body.split('\n'):
        if ANCHOR_RE.match(ln) and cur:
            chunks.append('\n'.join(cur).strip())
            cur = []
        cur.append(ln)
    if cur:
        chunks.append('\n'.join(cur).strip())
    return [c for c in chunks if len(c) >= 8]  # 过滤过短碎片


def build_prompt(chunk: str, topic: str, topics: list, research: list) -> str:
    return (
        "你是大模型研究日报的结构化迁移助手。下面是从主题页「"
        f"{topic}」截取的一段原始文本，可能含一条消息（论文/新闻/工具/洞察）。"
        "把它抽取为结构化字段，严格返回 JSON（不要代码块、不要解释）；若不是一条有效消息（如纯章节标题、感悟散文、无实质内容），返回 {\"skip\": true}。\n"
        "字段：\n"
        "- title: 标题（中文为主）\n"
        "- subtopic: 子主题（2~6 字），用于主题页栏目\n"
        f"- topics: 主题数组，必须包含 \"{topic}\"，并可从已有列表补充：{json.dumps(topics, ensure_ascii=False)}\n"
        "- date: 从文本推断的日期，格式 YYYY-MM-DD；无法判断返回 null\n"
        "- source: 来源（公众号/arxiv 分类/站点），未知填 \"未知\"\n"
        "- summary: 一句话中文摘要\n"
        "- paper / code / dataset / link: 论文/代码/数据集/原文链接，无则 \"\"\n"
        "- content: 正文，中文 3~5 句，可用 markdown\n"
        "- purpose: 用途与启示，markdown 无序列表\n"
        "只输出 JSON 对象。"
    )


def llm_structure(chunk: str, topic: str, topics: list, research: list, client) -> dict:
    """调用 LLM 把一个块结构化为 item（或 skip）。"""
    resp = client.chat.completions.create(
        model=app.LLM_MODEL,
        messages=[
            {"role": "system", "content": build_prompt(chunk, topic, topics, research)},
            {"role": "user", "content": chunk[:4000]},  # 截断超长块
        ],
    )
    text = (resp.choices[0].message.content or '').strip()
    text = re.sub(r'^```(?:json)?\s*', '', text)
    text = re.sub(r'\s*```$', '', text)
    return json.loads(text)


def process_topic(topic: str, args, client, topics, research, write_lock):
    path = app.TOPIC_DIR / f'{topic}.md'
    if not path.exists():
        print(f'[跳过] {topic}：文件不存在'); return
    raw = path.read_text(encoding='utf-8')
    parts = raw.split('+++', 2)            # parts[1]=front matter, parts[2]=body
    front = parts[1] if len(parts) >= 3 else ''
    body = parts[2] if len(parts) >= 3 else raw
    entries = split_entries(body)
    entries = entries[:args.max]
    print(f'\n=== {topic}：拆出 {len(entries)} 条候选（上限 {args.max}）===')

    valid_set = set(topics)
    results = {}  # idx -> (status, payload)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        fut = {ex.submit(llm_structure, c, topic, topics, research, client): i
               for i, c in enumerate(entries)}
        for f in as_completed(fut):
            i = fut[f]
            try:
                results[i] = ('ok', f.result())
            except Exception as e:  # noqa: BLE001
                results[i] = ('err', str(e))

    written = skipped = nodate = err = 0
    kept_chunks = []   # 保留在 topic 正文里的（笔记/无日期/错误，不丢失）
    for i in range(len(entries)):
        chunk = entries[i]
        status, payload = results.get(i, ('err', '未执行'))
        if status == 'err':
            err += 1; kept_chunks.append(chunk)
            print(f'  [{i}] ⚠ LLM 失败（保留原文）：{payload[:60]}'); continue
        if payload.get('skip'):
            skipped += 1; kept_chunks.append(chunk)   # 笔记/洞察，原样保留
            continue
        d = payload.get('date')
        try:
            iso = app.parse_target_date(d) if d else None
        except ValueError:
            iso = None
        if not iso:
            nodate += 1; kept_chunks.append(chunk)    # 无日期无法落位，保留原文
            print(f'  [{i}] · 无日期（保留原文）：{(payload.get("title") or "")[:30]!r}')
            continue
        its_topics = [topic]
        for t in (payload.get('topics') or []):
            if t in valid_set and t not in its_topics:
                its_topics.append(t)
        vr = set(research)
        its_research = [r for r in (payload.get('research') or []) if r in vr]
        item = {
            'id': '', 'title': payload.get('title', '').strip(),
            'subtopic': (payload.get('subtopic') or '').strip(),
            'topics': its_topics, 'research': its_research,
            'source': (payload.get('source') or '未知').strip(),
            'summary': (payload.get('summary') or '').strip(),
            'paper': (payload.get('paper') or '').strip(),
            'code': (payload.get('code') or '').strip(),
            'dataset': (payload.get('dataset') or '').strip(),
            'link': (payload.get('link') or '').strip(),
            'content': (payload.get('content') or '').strip(),
            'purpose': (payload.get('purpose') or '').strip(),
            'notes': chunk,   # 原始逐字笔记，原样保留进 item
        }
        if not item['title']:
            skipped += 1; kept_chunks.append(chunk); continue
        if args.dry:
            print(f'  [{i}] [DRY→迁出] {iso} | {item["title"][:36]} | topics={its_topics}')
            continue
        with write_lock:
            built = app.build_item_from_form({'date': iso, **item})
            built.pop('_target_date', None)
            app.append_item(built, iso)
        written += 1   # 已迁出：不保留进 topic 正文
        print(f'  [{i}] ✓ {iso} | {item["title"][:36]}')

    # 重写 topic 正文：只保留笔记/未迁出部分
    if not args.dry and len(parts) >= 3:
        new_body = '\n\n'.join(kept_chunks).strip()
        new_text = f'+++{front}+++\n\n' + (new_body + '\n' if new_body else '')
        path.write_text(new_text, encoding='utf-8')
        print(f'  -- {topic} 正文已精简：保留 {len(kept_chunks)} 块笔记，移除 {written} 条已迁出条目')
    print(f'  -- {topic} 汇总：写入 {written}，无日期保留 {nodate}，笔记保留 {skipped}，错误 {err}')


def main():
    ap = argparse.ArgumentParser(description='批量迁移主题内容到结构化日报')
    ap.add_argument('--topic', help='单个主题名（文件名）')
    ap.add_argument('--all', action='store_true', help='迁移全部主题')
    ap.add_argument('--max', type=int, default=100, help='每个主题本次最多处理条数（默认 100）')
    ap.add_argument('--workers', type=int, default=4, help='LLM 并发数（默认 4）')
    ap.add_argument('--dry', action='store_true', help='只预览不写盘')
    args = ap.parse_args()

    key = app.load_api_key()
    if not key:
        print(f'✗ 未找到 {app.API_KEY_FILE.relative_to(app.REPO_ROOT)}，请先创建并填入 api_key。')
        sys.exit(1)
    from openai import OpenAI
    client = OpenAI(api_key=key, base_url=app.LLM_BASE_URL)
    topics, research = app.valid_topics(), app.valid_research()

    if args.all:
        names = app.valid_topics()
    elif args.topic:
        names = [args.topic]
    else:
        ap.error('请指定 --topic <名称> 或 --all')

    write_lock = threading.Lock()
    for t in names:
        process_topic(t, args, client, topics, research, write_lock)


if __name__ == '__main__':
    main()
