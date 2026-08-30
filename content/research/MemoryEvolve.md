+++
title = 'MemoryEvolve'
proposer = '杜晋华'
since = '2026-08-30'
date = 2026-08-30T00:00:00+08:00
draft = false
toc = true
+++

# MemoryEvolve

> 研究方向：**记忆自进化**——让智能体自主构建、组织、巩固并持续演化长期记忆。

## 研究范畴

记忆自进化（memory self-evolution）以"记忆"为核心驱动，让模型 / 智能体在交互与任务执行中自主完成记忆的写入、检索、压缩、巩固、遗忘与重组，从而突破上下文窗口限制、支撑长周期任务与持续学习。本方向涵盖：智能体长期记忆架构（分层记忆 / 记忆操作系统）、情景记忆与语义记忆的组织与索引（含时序知识图谱）、记忆巩固与反思（reflection / consolidation）、参数化记忆与非参数化记忆的协同、记忆驱动的经验复用与技能沉淀。社区关注的核心问题包括：记忆的写入 / 淘汰策略如何自动学习而非人工规则、长期记忆如何抗噪声与防止错误记忆累积、记忆检索与推理如何深度耦合、多智能体 / 多会话间记忆如何共享与隔离，以及如何评测记忆系统在长周期任务上的真实收益。

## 研究挑战

- 记忆质量随时间漂移：错误、过时与冲突记忆的检测与修正。
- 写入 / 遗忘策略的自动化学习，避免记忆膨胀与检索退化。
- 记忆与推理的耦合：何时检索、检索什么、如何融合进当前决策。
- 长周期评测困难：缺少可复现、可量化记忆收益的基准。
- 隐私与安全：跨会话记忆的泄漏、污染与投毒风险。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [Letta (MemGPT)](https://github.com/letta-ai/letta) — 将操作系统分页思想引入 LLM 记忆管理的智能体记忆框架
- [mem0](https://github.com/mem0ai/mem0) — 面向生产的智能体可扩展长期记忆层
- [Graphiti (Zep)](https://github.com/getzep/graphiti) — 基于时序知识图谱的智能体记忆
- [A-mem](https://github.com/agiresearch/A-mem) — 受 Zettelkasten 启发的智能体自组织记忆系统
- [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) — 受海马体记忆索引理论启发的长期记忆检索框架
- [MemOS](https://github.com/MemTensor/MemOS) — 把记忆作为一等资源调度的"记忆操作系统"

**论文**
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 分层虚拟上下文与记忆分页管理
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 记忆流 + 反思 + 检索的经典智能体记忆架构
- [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 基于遗忘曲线的长期记忆更新机制
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — 动态链接与演化的自组织智能体记忆
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 可扩展记忆抽取与更新管线
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — LLM 智能体记忆机制综述
