"""
生成「主题 → 赛道」映射表 tools/trends/tracks.json（趋势栏目用，见 .omc/plans/trends-contract.md）。

content/topic/ 下有一千多个细粒度主题，直接按主题画热度曲线全是噪声；本脚本用 LLM 把每个
主题归入下方固定的少数赛道（TRACKS），结果落盘为可人工维护的 JSON：
  {"tracks": [...], "map": {"<topic>": "<track>", ...}}
- 增量：已在 map 里的主题不再询问 LLM，只对新主题补映射（--force 全量重算）。
- 主题来源：全部日报条目的 topics 字段（按出现次数降序，出现 1 次的主题也映射，便于长尾归并）。
- LLM 复用 backend/app.py 的 _llm_chat（api_key.txt + LLM_BASE_URL/LLM_MODEL）。

用法：backend/venv/bin/python tools/trends/build_tracks.py [--force] [--dry-run] [--chunk 150]
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
UPDATES_DIR = REPO_ROOT / "content" / "updates"
TRACKS_FILE = Path(__file__).resolve().parent / "tracks.json"
sys.path.insert(0, str(REPO_ROOT / "backend"))

try:
    import tomllib as toml  # py311+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as toml

# 赛道定义：名称 → 一句话说明（给 LLM 看的判定依据）。顺序即页面展示顺序。
TRACKS = {
    "推理与思维链": "推理、逻辑/数学推理、思维链、测试时计算、形式化验证、推理模型",
    "强化学习与后训练": "RL/RLHF/RLVR、策略优化、奖励建模、后训练、蒸馏、对齐训练方法",
    "预训练与模型架构": "预训练、模型架构、长上下文、注意力/MoE、缩放律、基础模型研发",
    "智能体系统": "单智能体框架、任务规划、工具调用、脚手架/harness、长程任务、浏览器/电脑操作智能体",
    "多智能体系统": "多智能体协作、通信、组织、群体/集群智能",
    "记忆与持续学习": "智能体记忆、状态持久化、持续学习、经验积累、知识更新",
    "自演化与自我改进": "自演化、递归自我改进、自动提示/代码/技能演化、技能库、自动化 ML 研究",
    "评估与基准": "模型/智能体评估、基准、过程评估、执行验证、LLM 判官、评测方法学",
    "数据工程与合成": "数据合成、数据策展、数据质量、数据集构建、数据飞轮",
    "可靠性与安全": "可靠性、幻觉、不确定性、安全治理、红队、审计、可解释性、对齐风险",
    "多模态与具身": "视觉/语音/视频多模态、具身智能、机器人、世界模型",
    "代码与软件工程": "AI 辅助编程、代码生成、软件工程智能体、代码评测",
    "科学发现与科研智能体": "自动化科学研究、科研智能体、科学发现、文献/实验自动化",
    "推理系统与效率": "推理加速、系统优化、成本优化、量化、服务/部署、算力",
    "检索与知识": "RAG、检索、知识图谱、知识注入、搜索增强",
    "人机协作与应用": "人在回路、产品/应用、行业落地、框架/工具链、教育/医疗等垂直应用",
    "产业与生态动态": "公司/产品发布、融资、开源生态、政策、行业观点（非技术方法本身）",
}
OTHER = "其他"


def collect_topics() -> Counter:
    cnt = Counter()
    for p in sorted(UPDATES_DIR.glob("2*.md")):
        parts = p.read_text(encoding="utf-8").split("+++")
        if len(parts) < 3:
            continue
        try:
            d = toml.loads(parts[1])
        except Exception as e:  # noqa: BLE001
            print(f"[skip] {p.name}: {e}", file=sys.stderr)
            continue
        for it in d.get("items", []) or []:
            for t in it.get("topics", []) or []:
                t = str(t).strip()
                if t:
                    cnt[t] += 1
    return cnt


def load_tracks() -> dict:
    if TRACKS_FILE.exists():
        try:
            return json.loads(TRACKS_FILE.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            pass
    return {"tracks": list(TRACKS), "map": {}}


def assign(topics: list, chunk: int, dry_run: bool) -> dict:
    from app import _llm_chat  # noqa: WPS433
    system = (
        "你是大模型研究日报的主题归类助手。给定若干细粒度【主题】标签，把每个主题归入下面的固定【赛道】之一；"
        "无法归入任何赛道、或主题过于泛化/无技术含义（如「人工智能」「研究」）时归入「其他」。\n"
        "赛道定义：\n" + "\n".join(f"- {k}：{v}" for k, v in TRACKS.items()) + f"\n- {OTHER}：以上都不合适\n"
        "规则：只能输出赛道名称原文；每个主题恰好一个赛道；优先按主题的核心技术对象判断，而不是应用场景。"
        '严格返回 JSON 对象 {"<主题>": "<赛道>", ...}，不要代码块、不要解释。'
    )
    out = {}
    for i in range(0, len(topics), chunk):
        part = topics[i:i + chunk]
        if dry_run:
            print(f"[dry-run] chunk {i // chunk + 1}: {len(part)} topics, e.g. {part[:5]}")
            continue
        try:
            res = _llm_chat(system, {"主题": part}, want_json=True, retries=3)
        except Exception as e:  # noqa: BLE001
            print(f"[fail] chunk {i // chunk + 1}: {e}", file=sys.stderr)
            continue
        valid = set(TRACKS) | {OTHER}
        got = 0
        for t in part:
            v = str(res.get(t, "")).strip() if isinstance(res, dict) else ""
            if v in valid:
                out[t] = v
                got += 1
        print(f"chunk {i // chunk + 1}: {got}/{len(part)} mapped")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="忽略已有映射，全量重算")
    ap.add_argument("--dry-run", action="store_true", help="只打印将询问的主题分块，不调 LLM、不写文件")
    ap.add_argument("--chunk", type=int, default=150)
    args = ap.parse_args()

    cnt = collect_topics()
    data = load_tracks()
    data["tracks"] = list(TRACKS)
    mapping = {} if args.force else dict(data.get("map", {}))
    todo = [t for t, _ in cnt.most_common() if t not in mapping]
    print(f"topics total={len(cnt)} mapped={len(mapping)} todo={len(todo)}")
    if todo:
        mapping.update(assign(todo, args.chunk, args.dry_run))
    if args.dry_run:
        return
    # 只保留仍在使用的主题 + 新映射；按出现次数降序写出便于人工校对
    ordered = {t: mapping[t] for t, _ in cnt.most_common() if t in mapping}
    data["map"] = ordered
    TRACKS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    dist = Counter(ordered.values())
    print(f"written {TRACKS_FILE} ({len(ordered)} topics); unmapped={len(cnt) - len(ordered)}")
    for k, v in dist.most_common():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
