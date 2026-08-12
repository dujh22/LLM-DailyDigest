+++
title = 'Awesome-RSI'
proposer = '杜晋华'
since = '2026-06-12'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# Awesome-RSI

> 研究方向：**递归自我改进（Recursive Self-Improvement, RSI）**方向的精选资源与论文清单。

## 研究范畴

递归自我改进（RSI）指一个系统能够持续改进自身，且其"改进机制"本身也被纳入改进对象，从而形成自指式的提升闭环。本方向涵盖：自我改进 Agent、自我重写 / 自我修复、LLM-as-a-Judge 自迭代、开放式 RSI 任务，以及面向 RSI 的治理与安全框架。社区关注的核心问题包括：自我改进能否持续近似单调地提升、是否存在上限或退化、自我奖励 / 自评判信号是否存在系统性偏差、如何度量"改进"本身以避免被优化目标作弊，以及 RSI 与对齐、可控性的协同。

## 研究挑战

- 奖励作弊（reward hacking）与退化解、捷径行为。
- 长期迭代的稳定性与灾难性遗忘。
- 评测有效性：如何在快速自进化的系统中持续评估真实能力。
- 安全治理：失控风险、红队、披露与审计。
- 计算与数据成本随迭代轮次快速膨胀。

## 自研项目

- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 面向 RSI 的持续研究项目：维护综述、整理论文与资源、沉淀自动化采集/归并工具，先跑通"采集 → 去重归并论文库 → AI/人工笔记 → 综述引用位置"的最小可检查闭环。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI / 走向真正的 ASI》承载仓库，含开题材料与综述《大语言模型复杂推理的自我进化机制》。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — LLM 论文/工具/资讯每日自动聚合系统（爬取→翻译→摘要），Hugo+FixIt 网站 + topic/research 双聚合 + Flask/LLM 抽取后端。
- [LLMDailyDigestWeb](https://github.com/dujh22/LLMDailyDigestWeb) — LLM-DailyDigest 的线上静态站点（GitHub Pages 构建产物）。
- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》（唐杰、杜晋华，清华）配套仓库，Word+LaTeX，覆盖深度学习/Transformer/预训练/SFT/RLHF/评测对齐/Agent/安全/多模态/生成模型等章节。

## 相关工作

**代码 / 框架**
- [awesome_Recursive_Self-Improving_LLM](https://github.com/robert-lee2016/awesome_Recursive_Self-Improving_LLM) — RSI 精选清单（同名方向）
- [letta](https://github.com/letta-ai/letta) — 有状态、可自进化的智能体平台
- [ai-redteam-recursive-self-improvement](https://github.com/lihouwenbin/ai-redteam-recursive-self-improvement) — RSI 治理红队框架
- [recursive-improve (kayba-ai)](https://github.com/kayba-ai/recursive-improve) — 捕获 LLM 调用 trace，递归修复自身
- [recursive-self-improvement-suite (keskival)](https://github.com/keskival/recursive-self-improvement-suite) — 面向 LLM 的开放式 RSI 任务集
- [self-improvement-llm (Zesearch)](https://github.com/Zesearch/self-improvement-llm) — LLM 自我改进技术综述仓库
- [Awesome-Self-Improving-Agents (selfimproving-agent)](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) — 自我改进 Agent 系统合集
- [Awesome-Self-Improving-Agents (FrontisAI)](https://github.com/FrontisAI/Awesome-Self-Improving-Agents) — RL、skill library 等方向的另一合集
- [Awesome-Self-Evolving-Agents (XMUDeepLIT)](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 厦大自进化 Agent 综述
- [awesome-agent-harness (RUCAIBox)](https://github.com/RUCAIBox/awesome-agent-harness) — Agent harness 与自我改进

**论文**
- [Foundations of GenIR](https://arxiv.org/abs/2501.02842)
- [Adaptive Data Flywheel: MAPE Control Loops for AI Agent Improvement](https://arxiv.org/abs/2510.27051)
- [Gödel Agent: A Self-Referential Framework for Agents](https://arxiv.org/abs/2410.04444) — Gödel Machine 启发的递归自改写 Agent（被引 19+）
- [LADDER: Self-Improving LLMs Through Recursive Problem Decomposition](https://arxiv.org/abs/2503.00735) — 递归问题分解自主提升（被引 24）
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM-as-a-Judge 自我改进（被引 996）
- [Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) — Meta-Rewarding（被引 223）
- [ReST meets ReAct (ICLR 2024)](https://arxiv.org/abs/2312.10003) — 强化学习+自蒸馏多步推理改进（被引 96）
- [Noise-to-Meaning Recursive Self-Improvement](https://arxiv.org/abs/2505.02888) — RSI 系统性框架
- [On the Limits of Self-Improving in Large Language Models](https://arxiv.org/abs/2601.05280) — 自我改进理论极限
- [Recursive Self-Improvement in AI (Survey)](https://arxiv.org/abs/2607.07663) — 综述 1250 篇论文
- [How to Realize Recursively Self-Improving Agents](https://arxiv.org/abs/2607.12254) — 治理式多 Agent RSI 架构
- [Self Rewarding Self Improving](https://arxiv.org/abs/2505.08827) — 无参考答案的自评判自我改进
- [RISE (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf) — 多轮交互自我提升推理（被引 214）
- [SPC: Evolving Self-Play Critic (NeurIPS 2025)](https://neurips.cc/virtual/2025/poster/118706) — 对抗自博弈 Critic 进化

**研讨会 / 课程 / 报告**
- [ICLR 2026 Workshop on Recursive Self-Improvement](https://recursive-workshop.github.io/) — RSI 专题研讨会
- [Stanford CS329A: Self-Improving AI Agents](https://cs329a.stanford.edu/) — 斯坦福自我改进 Agent 课程
- [CSA: RSI Security Implications](https://labs.cloudsecurityalliance.org/research/ai-recursive-self-improvement-security-implications-v1-0-csa) — 云安全联盟 RSI 安全报告
