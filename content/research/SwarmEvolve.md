+++
title = 'SwarmEvolve'
proposer = '杜晋华'
since = '2026-03-12'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# SwarmEvolve

> 研究方向：**多智能体群体的自进化**——群体/社会模拟中的智能体协同与演化（本站已 fork casevo）。

## 研究范畴

多智能体群体自进化（swarm / multi-agent self-evolution）研究由多个 LLM 智能体组成的群体如何通过交互、协作与竞争实现整体能力的持续演化，超越单体自改进的上限。本方向涵盖：多智能体协同自进化（角色分工、共同进化 / co-evolution）、群体社会模拟（社会规范、合作与博弈的涌现）、多智能体系统结构的自动优化（通信拓扑、协作网络的自进化）、群体智能基准评测。社区关注的核心问题包括：群体交互能否产生单体无法获得的进化信号、协作结构与通信协议如何自动演化而非人工设计、大规模社会模拟中涌现行为的可控性与可解释性、多智能体间能力与知识如何传播扩散，以及群体进化的评测基准与度量方法。

## 研究挑战

- 进化信号稀疏：群体交互产生的反馈如何转化为有效的个体 / 群体改进信号。
- 协作结构自动化：通信拓扑与角色分工的搜索空间巨大，人工设计难以泛化。
- 涌现行为可控性：大规模模拟中合谋、退化、同质化等非预期动态的检测与干预。
- 成本与可复现性：多智能体交互的 token 开销随规模爆炸，实验难以复现。
- 评测缺口：缺少衡量"群体进化增益"（相对单体基线）的标准基准。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含多智能体自进化机制的综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [casevo](https://github.com/rgCASS/casevo) — 认知智能体与社会进化模拟器（本站已 fork）
- [awesome-agent-evolution (EvoMap)](https://github.com/EvoMap/awesome-agent-evolution) — 智能体进化精选清单
- [awesome-agent-evolution (Shiyao-Huang)](https://github.com/Shiyao-Huang/awesome-agent-evolution) — 自进化智能体综述与证据图
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统框架
- [Awesome-Self-Evolving-Agents (XMUDeepLIT)](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 厦大自进化 Agent 综述列表
- [CORAL](https://github.com/Human-Agent-Society/CORAL) — 面向开放式问题的自主多智能体进化框架
- [AgentSociety](https://github.com/tsinghua-fib-lab/agentsociety) — 清华 FIB Lab 城市场景 LLM Agent 社会模拟
- [SwarmBench (YuLan-SwarmIntell)](https://github.com/RUC-GSAI/YuLan-SwarmIntell) — 人民大学群体智能基准测试
- [CAMEL-AI](https://www.camel-ai.org/) — 开源 Agent 进化社区
- [awesome-multi-agent (WeiChengTseng)](https://github.com/WeiChengTseng/awesome-multi-agent) — 多智能体学习资源汇总
- [ai-agent-papers (masamasa59)](https://github.com/masamasa59/ai-agent-papers) — 双周更新 Agent 论文合集
- [MARL-Papers (LantaoYu)](https://github.com/LantaoYu/MARL-Papers) — 经典多智能体强化学习论文列表

**论文**
- [Survey of Multi-Agent Deep RL with Communication](https://arxiv.org/abs/2203.08975)
- [Multi-Agent Evolve: LLM Self-Improve through Co-evolution](https://arxiv.org/abs/2510.23595) — MAE 框架，三角色协同自进化
- [Evolution of Cooperation in LLM-Agent Societies](https://arxiv.org/abs/2504.19487) — LLM 多智能体复现博弈论合作演化
- [CORAL: Towards Autonomous Multi-Agent Evolution](https://arxiv.org/abs/2604.01658) — 开放式自主多智能体进化
- [Self-Evolving Multi-Agent Collaboration Networks (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf) — MAC 网络自进化
- [SE-Agent: Self-Evolution Trajectory Optimization (NeurIPS 2025)](https://neurips.cc/virtual/2025/poster/116517) — 迭代轨迹优化增强多步推理
- [AgentSociety: Large-Scale Simulation of LLM-Driven Social Agents](https://arxiv.org/abs/2502.08691) — 大规模社会智能体模拟
- [OASIS: Open Agent Social Interaction Simulations](https://arxiv.org/abs/2411.11581) — 开放式社交互动模拟
- [CAMEL: Communicative Agents for "Mind" Exploration](https://arxiv.org/abs/2303.17760) — 经典自主协作 Agent（被引 2500+）
- [Evolving Interpretable Constitutions for Multi-Agent LLM Systems](https://arxiv.org/pdf/2602.00755) — Constitutional Evolution 框架
- [A Survey on Automated Optimization of LLM-Based Multi-Agent Systems](https://www.preprints.org/manuscript/202605.2011) — 自动化优化方法综述

**博客 / 其他**
- [Self-Evolving LLM Agents (EmergentMind)](https://www.emergentmind.com/topics/self-evolving-llm-agents) — 自进化 Agent 主题聚合页
- [Self-Evolved Agents (Eigent.ai)](https://www.eigent.ai/blog/self-evolved-agents) — 递归自我改进方法介绍
