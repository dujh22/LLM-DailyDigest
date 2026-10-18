+++
title = 'GeneralizeEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# GeneralizeEvolve

> 研究方向：**自进化中的泛化**——自进化带来的提升能否跨任务、跨分布迁移而非基准过拟合，以及测试时学习与持续学习如何不遗忘。

## 研究范畴

自进化中的泛化（generalization in self-evolution）追问一个核心问题：模型 / Agent 通过自迭代获得的能力，究竟是真实的能力扩展，还是对训练分布与评测基准的记忆与过拟合。本方向涵盖：SFT 与 RL 后训练的泛化差异（"SFT 记忆、RL 泛化"）、RLVR 是否扩展了基座模型的推理边界、在线 RL 为何遗忘更少、无外部奖励的自信号学习（Intuitor 类）、测试时训练与自适应（TTT、SEAL 自生成微调数据）、测试时记忆与长上下文架构（Titans）、持续学习与灾难性遗忘、弱到强泛化，以及 ARC-AGI 类强调流体智能而非知识回忆的评测。社区关注的核心问题包括：如何在自进化闭环中设计分布外（OOD）与组合泛化的检验、如何区分"学到的算法"与"记住的模式"（grokking 现象）、持续自进化下能力增益与遗忘的权衡，以及测试时计算与测试时学习在多大程度上能替代参数规模。

## 研究挑战

- 基准过拟合与数据污染：自迭代容易把评测集"学进去"。
- 持续自进化下的灾难性遗忘与能力退化。
- 自生成信号（自信度、自评）可能强化已有偏差而非扩展边界。
- OOD / 组合泛化缺乏公认且不易被攻陷的度量。
- 测试时学习的算力成本与稳定性。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，自进化的泛化边界是综述《大语言模型复杂推理的自我进化机制》讨论的核心科学问题。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 元数据驱动的可控逻辑推理任务生成，可按难度 / 规模 / 规则维度构造 OOD 测试，检验自进化带来的泛化。

## 相关工作

**代码 / 框架**
- [SEAL](https://github.com/Continual-Intelligence/SEAL) — Self-Adapting Language Models：模型自生成微调数据与更新指令
- [marc](https://github.com/ekinakyurek/marc) — ARC 上测试时训练（TTT）的参考实现
- [ttt-lm-pytorch](https://github.com/test-time-training/ttt-lm-pytorch) — 测试时训练层（Learning to Learn at Test Time）
- [ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) — 强调流体智能的抽象推理基准
- [limit-of-RLVR](https://github.com/LeapLabTHU/limit-of-RLVR) — "RL 是否真正扩展推理边界"的实验代码
- [Intuitor](https://github.com/sunblaze-ucb/Intuitor) — 以自信度为内在奖励、无外部奖励的 RL
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 弱到强泛化实验代码
- [Avalanche](https://github.com/ContinualAI/avalanche) — 持续学习端到端库

**论文**
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](https://arxiv.org/abs/2501.17161)
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837) — RLVR 的能力边界
- [RL's Razor: Why Online Reinforcement Learning Forgets Less](https://arxiv.org/abs/2509.04259) — 在线 RL 偏向 KL 最小解因而遗忘更少
- [Learning to Reason without External Rewards](https://arxiv.org/abs/2505.19590) — Intuitor，自信度驱动的泛化
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) — SEAL
- [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://arxiv.org/abs/2411.07279) — ARC 上 TTT 大幅提升
- [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620)
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390)
- [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) — 记忆到泛化的相变
- [Continual Learning of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2404.16789)
