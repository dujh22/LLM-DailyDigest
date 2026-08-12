+++
title = 'DataEvolve'
proposer = '杜晋华'
since = '2026-08-05'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# DataEvolve

> 研究方向：**数据自进化**——以数据为中心的自进化训练数据 / 合成与迭代。

## 研究范畴

数据自进化（data-centric self-evolution）以"数据"为核心驱动，让模型自主生成、筛选、配比并迭代训练数据，从而在尽量少依赖人工标注的情况下持续提升。本方向涵盖：合成数据生成、指令进化（Evol-Instruct 类）、自奖励 / 自评判偏好数据、数据飞轮（data flywheel）、以数据为中心的 Agent 自进化。社区关注的核心问题包括：合成数据的质量 / 多样性 / 覆盖度如何度量与保证、自迭代是否会引发模型崩溃（model collapse）或分布坍缩、数据污染与配比对下游能力的边际影响，以及如何量化"数据价值"并据此做主动筛选。

## 研究挑战

- 偏差与错误在迭代中累积放大。
- 真实性与事实性控制（幻觉随合成数据传播）。
- 大规模数据治理与自动化精炼的成本。
- 长期迭代稳定性与可复现性。

## 自研项目

- [CLUB-benchmark](https://github.com/dujh22/CLUB-benchmark)
- [EvolveLLM](https://github.com/dujh22/EvolveLLM)

## 相关工作

**代码 / 框架**
- [agents (aiwaves-cn)](https://github.com/aiwaves-cn/agents) — 数据中心的自进化自主语言智能体框架
- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 零数据自进化推理
- [autosynth](https://github.com/Ahmad8864/autosynth) — 仿 Meta Autodata 的合成数据生成框架
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统，支持训练数据自主生成
- [Evol-Instruct](https://github.com/nlpxucan/WizardLM) — WizardLM 的进化指令数据生成方法
- [Self-Rewarding-LM](https://github.com/metaillusion/Self-Rewarding-LM) — 自奖赏语言模型偏好数据生成与迭代
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含数据进化专题的自进化 Agent 合集

**论文**
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — Meta/NYU LLM-as-a-Judge 自我改进（被引 996）
- [Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) — Meta-Rewarding 高层级自我改进（被引 223）
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化方法综述（含数据进化模块）
- [Adaptive Data Flywheel: MAPE Control Loops for AI Agent Improvement](https://arxiv.org/abs/2510.27051) — 数据飞轮控制环路
- [Evolving Knowledge: Towards Explanatory Evolution](https://arxiv.org/abs/2405.05122) — 知识进化与数据迭代
- [Self-Evolving Multi-Agent Collaboration Networks (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf) — Agent 影响力驱动的协作进化
