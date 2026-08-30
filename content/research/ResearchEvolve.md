+++
title = 'ResearchEvolve'
proposer = '杜晋华'
since = '2026-08-30'
date = 2026-08-30T00:00:00+08:00
draft = false
toc = true
+++

# ResearchEvolve

> 研究方向：**研究自进化**——AI 自主科研：让智能体自主提出假设、设计实验、迭代改进研究本身。

## 研究范畴

研究自进化（research self-evolution / autonomous scientific discovery）让 AI 系统承担科研全流程或关键环节——文献调研、假设生成、实验设计与执行、结果分析、论文撰写与同行评审——并通过闭环反馈持续改进自身的科研能力。本方向涵盖：端到端 AI Scientist 系统、科研多智能体协作（研究员 / 评审 / 工程师角色分工）、假设生成与实验规划、自动机器学习研究（MLE / 科研代码自动化）、AI 同行评审与科研评测基准。社区关注的核心问题包括：如何保证自动产出研究的新颖性与正确性（而非平庸组合或错误结论）、实验闭环的可复现性与算力成本、AI 评审能否可靠替代人类质量把关、长周期科研目标如何分解与自我纠错，以及自主科研的学术伦理与署名规范。

## 研究挑战

- 新颖性与严谨性的平衡：避免"看似合理"的错误结论与幻觉引用。
- 实验闭环成本高：自动实验的算力预算、失败恢复与可复现性。
- 评价困难：缺乏对 AI 生成研究质量的可靠自动评测。
- 长周期目标分解：从模糊科学问题到可执行实验的规划与自我纠错。
- 伦理与规范：署名、同行评审污染与学术不端风险。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) — Sakana AI 端到端全自动科研系统（想法→实验→论文→评审）
- [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) — 基于智能体树搜索的第二代自动科研系统
- [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) — 以人类研究者为中心的 LLM 科研助理流水线
- [AI-Researcher](https://github.com/HKUDS/AI-Researcher) — 全自主科学创新框架（文献→创意→实现→论文）
- [SciAgents](https://github.com/lamm-mit/SciAgentsDiscovery) — 知识图谱驱动的多智能体科学发现
- [paper-qa](https://github.com/Future-House/paper-qa) — FutureHouse 面向科学文献的高保真检索问答

**论文**
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) — 首个端到端自动科研系统
- [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227) — 科研流水线多智能体分工
- [Towards an AI Co-Scientist](https://arxiv.org/abs/2502.18864) — Google 多智能体假设生成与"科研共导"系统
- [ResearchAgent: Iterative Research Idea Generation over Scientific Literature](https://arxiv.org/abs/2404.07738) — 文献驱动的研究想法迭代生成
- [CycleResearcher: Improving Automated Research via Automated Review](https://arxiv.org/abs/2411.00816) — 研究生成与自动评审的强化闭环（ICLR 2025）
- [SciAgents: Automating Scientific Discovery through Multi-Agent Intelligent Graph Reasoning](https://arxiv.org/abs/2409.05556) — 图推理驱动的跨领域假设发现
