+++
title = 'AgentEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# AgentEvolve

> 研究方向：**Agent 推理时自进化**——不改参数，Agent 在部署后通过反思、技能库、工作流记忆与上下文演化持续变强。

## 研究范畴

Agent 推理时自进化（inference-time / deployment-time agent self-evolution）研究 Agent 在参数冻结的前提下如何随经验持续改进：把失败反思写回记忆（Reflexion）、把成功轨迹沉淀为可复用技能与工作流（Voyager 技能库、SkillWeaver、Agent Workflow Memory）、按需自造工具与 MCP 能力（Alita）、把经验以"演化中的上下文 / 作弊表"形式积累（Dynamic Cheatsheet、Agentic Context Engineering），乃至以免训练方式实现 GRPO 式的经验学习（Training-Free GRPO）。本方向涵盖：Agent 认知架构（CoALA）、经验记忆与检索、技能发现 / 验证 / 精炼闭环、自动工具构造、上下文与提示的在线演化、多 Agent 间的经验共享，以及推理时自进化与训练时自进化的互补与衔接。社区关注的核心问题包括：经验积累是否会带来"上下文坍缩"与噩梦式膨胀、自我反思信号的可靠性、技能库的泛化与过时淘汰机制、以及如何在不更新参数的情况下保证改进可持续并最终反哺训练。

## 研究挑战

- 经验记忆的膨胀、噪声与检索精度之间的张力（上下文坍缩）。
- 自我反思与自评信号不可靠，错误经验被固化。
- 技能 / 工作流的泛化与过时：何时复用、何时淘汰。
- 推理时自进化缺乏统一评测，难以与训练侧方法公平比较。
- 推理时改进如何回流到参数（经验 → 数据 → 训练）的衔接。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，推理时自进化（反思 / 记忆 / 技能）是自进化机制综述的重要分支。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录自改进 Agent 相关工作。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理智能体评测与自进化平台，可用于检验 Agent 推理时自进化的效果。

## 相关工作

**代码 / 框架**
- [Voyager](https://github.com/MineDojo/Voyager) — Minecraft 开放式具身 Agent，自动课程 + 可增长技能库
- [Reflexion](https://github.com/noahshinn/reflexion) — 语言反思写回记忆的"口头强化学习"
- [SkillWeaver](https://github.com/OSU-NLP-Group/SkillWeaver) — Web Agent 自主发现、打磨技能并沉淀为 API
- [Alita](https://github.com/CharlesQ9/Alita) — 最小预定义、最大自进化的通用 Agent，自造 MCP 工具
- [Dynamic Cheatsheet](https://github.com/suzgunmirac/dynamic-cheatsheet) — 测试时学习的自适应记忆
- [Agent Workflow Memory](https://github.com/zorazrw/agent-workflow-memory) — 从经验归纳可复用工作流
- [Youtu-agent (Training-Free GRPO)](https://github.com/TencentCloudADP/youtu-agent) — 免训练的经验库式 GRPO
- [Letta](https://github.com/letta-ai/letta) — 有状态、带长期记忆的 Agent 平台
- [Self-Evolving-Agents](https://github.com/CharlesQ9/Self-Evolving-Agents) — 自进化 Agent 综述资源库
- [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents) — 自进化 AI Agent 论文清单

**论文**
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) — CoALA 认知架构框架
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
- [Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution](https://arxiv.org/abs/2505.20286)
- [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952)
- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) — 上下文作为演化中的"剧本"
- [Training-Free Group Relative Policy Optimization](https://arxiv.org/abs/2510.08191)
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413)
- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046)
- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)
