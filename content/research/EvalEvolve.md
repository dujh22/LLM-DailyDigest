+++
title = 'EvalEvolve'
proposer = '杜晋华'
since = '2026-08-05'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# EvalEvolve

> 研究方向：**进化式评测**——随能力增长持续演化、抗污染的评测基准与方法。

## 研究范畴

进化式评测（evolutionary / dynamic evaluation）针对静态基准易被污染、快速过时的问题，主张让基准与方法随模型能力增长持续演化、抗污染。本方向涵盖：持续更新的 live benchmarks、动态 / 等价变体评测、自动出题（auto-benchmaking）、抗污染机制，以及自进化基准框架。社区关注的核心问题包括：如何持续、低成本地产生高质量新题并标定难度、如何抵抗训练数据污染与基准泄漏、动态评测如何与真实世界能力对齐避免指标漂移，以及多模态 / Agent / 长周期任务的评测有效性。

## 研究挑战

- 题目质量、ground truth 获取与难度一致性。
- 防泄漏与可复现性的张力。
- 评测本身的成本与算力。
- 与快速迭代模型保持同步的运维负担。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测平台，提供准确率 / cell 级准确率 / 一致性 / 推理路径追踪等多维指标，含可视化榜单（clubweb.site）与 4600+ 评测结果 JSONL。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含评测相关的方法论与综述沉淀。

## 相关工作

**代码 / 框架**
- [meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments) — Meta 智能体研究评测平台
- [eval-dev-quality](https://github.com/symflower/eval-dev-quality) — 开发质量进化评测
- [ABench](https://github.com/inclusionAI/ABench) — 进化式开源 benchmark 套件
- [EvolIF](https://github.com/JiaQiSJTU/EvolIF) — benchmark 进化框架（多轮指令跟随）
- [LiveBench](https://github.com/livebench/livebench) — 持续更新的抗污染 LLM 基准，每六个月刷新
- [LiveCodeBench](https://github.com/livecodebench/livecodebench) — 持续收集新编程题的抗污染代码评测
- [EvoEval](https://github.com/evo-eval/evoeval) — 对 HumanEval 进化变换生成 828 个新问题
- [EvoCodeBench](https://github.com/seketeam/evocodebench) — 真实仓库对齐的进化代码基准（NeurIPS 2024）
- [Self-Evolving-Benchmark](https://github.com/NanshineLoong/Self-Evolving-Benchmark) — 多 Agent 框架自进化基准（COLING 2025, 被引 45）
- [DyCodeEval](https://github.com/SeekingDream/DyCodeEval) — 动态代码评测，语义等价变体抗污染（ICML 2025）
- [AutoBencher](https://github.com/XiangLi1999/AutoBencher) — 声明式自动基准构建（ICLR 2025）
- [Static-to-Dynamic-LLMEval](https://github.com/SeekingDream/Static-to-Dynamic-LLMEval) — 静态到动态评测综述仓库（EMNLP 2025）
- [MMBench-Live](https://github.com/PRIS-CV/MMBench-Live) — 多 Agent 驱动持续进化多模态基准（ICML 2026）
- [SDEval](https://github.com/hq-King/SDEval) — 安全性动态评测框架（AAAI 2026）
- [Code2Bench](https://github.com/Code2Bench/Code2Bench) — 从 GitHub commits 自动生成代码评测题
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 自进化 Agent 领域综合合集
- [awesome-data-contamination](https://github.com/lyy1994/awesome-data-contamination) — 数据污染与抗污染评测论文列表

**论文**
- [LiveBench: A Challenging, Contamination-Free LLM Benchmark](https://arxiv.org/abs/2406.19314) — 首个频繁更新题目的基准（被引 470+）
- [LiveCodeBench](https://arxiv.org/abs/2403.07974) — 持续收集新竞赛题（被引 1900+）
- [EvoEval: Evolving Coding Benchmarks via LLM](https://arxiv.org/abs/2403.19114) — LLM 语义变换生成新题
- [Benchmark Self-Evolving (COLING 2025)](https://arxiv.org/abs/2402.11443) — 多 Agent 自进化基准框架（被引 45）
- [DyCodeEval (ICML 2025)](https://arxiv.org/abs/2503.04149) — 动态代码推理评测（被引 33）
- [AutoBencher (ICLR 2025)](https://arxiv.org/abs/2407.08351) — 声明式自动基准构建（被引 31）
- [From Static to Dynamic: A Survey on LLM Evaluation (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.511.pdf) — 动态评测综述（被引 32）
- [Towards Contamination Resistant Benchmarks](https://arxiv.org/abs/2505.08389) — 抗污染性概念
- [LLM-Evolve (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.940) — 序贯问题求解评测（被引 20）
- [ArenaBencher](https://arxiv.org/abs/2510.08569) — 多模型竞争驱动基准进化
- [MMBench-Live (ICML 2026)](https://arxiv.org/abs/2607.01813) — 持续进化多模态基准
- [SDEval (AAAI 2026)](https://arxiv.org/abs/2508.06142) — 安全动态评测（被引 7）
- [Towards Self-Evolving Agent Benchmarks](https://openreview.net/forum?id=2H03gm4Rq6) — 可验证自进化基准
- [Evolutionary Perspectives on LLM-Based Multi-Agent Evaluation](https://arxiv.org/abs/2506.11102) — 进化视角评测方法论分析
