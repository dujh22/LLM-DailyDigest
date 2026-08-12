+++
title = 'EvolveLRM'
proposer = '杜晋华'
since = '2026-01-09'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# EvolveLRM

> 研究方向：**大推理模型（LRM）的自我进化**——通过 RL / 自我博弈等让推理模型持续提升。

## 研究范畴

大推理模型（Large Reasoning Model, LRM）的自我进化，聚焦于通过强化学习 / 自我博弈 / 过程奖励 / 树搜索等范式，让"System 2"式长链推理模型在推理质量上持续提升。本方向涵盖：RL 后训练、自我博弈、过程 / 结果奖励、搜索增强训练、长思维链与推理时计算。社区关注的核心问题包括：RL 训练带来的能力提升能否泛化到分布外任务、奖励稀疏 / 奖励作弊与"伪推理"如何识别与缓解、探索—利用的平衡与思维链忠实度（faithfulness），以及训练效率与推理时算力的权衡。

## 研究挑战

- 训练稳定性、奖励设计与奖励黑客。
- 高昂的算力与数据成本。
- 评测上限（benchmark saturation）与防污染。
- 推理安全（越狱、长链中的错误累积）。

## 自研项目

- [LogicGLM](https://github.com/dujh22/LogicGLM)

## 相关工作

**代码 / 框架**
- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 从零数据自进化的推理 LLM（ICLR 2026）
- [SE-Agent](https://github.com/JARVIS-Xs/SE-Agent) — 智能体自进化框架
- [DeepScaleR](https://github.com/agentica-project/deepscaler) — 小模型大推理 RL 训练框架，1.5B 模型在 AIME 超越 o1
- [Reasoning-Self-Evolution-Survey](https://github.com/cs-holder/Reasoning-Self-Evolution-Survey) — 配套复杂推理自进化综述的资源仓库
- [Awesome-Agentic-Reasoning](https://github.com/weitianxin/Awesome-Agentic-Reasoning) — Agent 推理论文分类整理（含自我进化专题）
- [self-improvement-llm](https://github.com/Zesearch/self-improvement-llm) — 系统级自我改进语言模型技术整理

**论文**
- [LLM Reasoning Abilities Under Non-Ideal Conditions After RL-Fine-Tuning](https://arxiv.org/abs/2508.04848)
- [The Impact of Quantization on Large Reasoning Model RL](https://arxiv.org/abs/2511.15694)
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化方法综述
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM 作为自身裁判生成偏好数据自我改进（被引 996+）
- [STaR: Bootstrapping Reasoning With Self-Taught Reasoning](https://arxiv.org/abs/2203.14465) — 经典自我推理引导方法（被引 1959+）
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) — 零数据自进化推理（被引 157）
- [Debate, Train, Evolve (DTE)](https://arxiv.org/abs/2505.15734) — 多 Agent 辩论轨迹训练实现推理自进化（EMNLP 2025）
- [ALIVE: Awakening LLM Reasoning via Adversarial Self-Evolution](https://arxiv.org/abs/2602.05472) — 对抗性自我进化激活推理能力
- [A Survey of Reasoning Large Language Models](https://arxiv.org/abs/2502.17419) — System 1 到 System 2 视角的推理 LLM 综述（被引 415）
- [Towards Large Reasoning Models: A Survey of Reinforced Self-Training](https://arxiv.org/abs/2501.09686) — 强化自我训练方法综述
- [On the Limits of Self-Improving in Large Language Models](https://arxiv.org/abs/2601.05280) — 自我改进理论极限分析
