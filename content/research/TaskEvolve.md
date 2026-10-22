+++
title = 'TaskEvolve'
proposer = '杜晋华'
since = '2026-10-22'
date = 2026-10-22T00:00:00+08:00
draft = false
toc = true
+++

# TaskEvolve

> 研究方向：**任务级自进化**——智能体自主产出可运行的任务 / 作品（游戏、软件、交互式内容），再通过试玩、反思与修复持续迭代，使任务本身成为进化的载体。

## 研究范畴

任务级自进化（task-level self-evolution）把「任务实例」而非模型参数、提示或数据当作进化的基本单位：智能体先生成一个可执行、可验证的产物（游戏、程序、交互式应用或仿真环境），再主动试玩 / 运行、诊断缺陷、修复并重新验收，形成生成—试玩—反思—修复的闭环。与 LogicEvolve（推理范式进化）、DataEvolve（数据进化）、EnvironmentEvolve（环境进化）相比，本方向关注的是**成品层面**的长期改进质量，以及经验如何跨任务沉淀复用。本方向涵盖：自然语言到可玩游戏的生成与迭代、Agent 原生引擎 / 可读写状态的交互环境、演化检查表与经验库、多角色对抗式开发（生成者与检验者分离）、基于执行反馈的自动修 Bug、递归自我改进的长程开发与经验内化。社区关注的核心问题包括：如何自动判定「能玩 / 可用」而非仅「能跑」、如何避免对少量测试用例过拟合、经验复用与模型能力内化的边界，以及长程迭代中的质量饱和、回退与评审主观性。

## 研究挑战

- 可玩性 / 可用性缺乏可自动验证的 ground truth，评审依赖模拟试玩与启发式检查。
- 迭代会过拟合少量测试用例，产生脆弱产物与交互泛化不足。
- 缺陷分层（规则冲突、数值失衡、关卡不可达、代码错误）需要不同的诊断与修复策略。
- 长程递归改进易出现质量饱和、能力回退与上下文膨胀。
- 经验复用与参数内化的接口尚不清晰，非参数化经验的可迁移性验证困难。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测与自进化平台，提供可程序化验证的任务族与生成器—验证器流水线，可作为任务级自进化的任务源与验收基线。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [VibeGame](https://github.com/tettethu/VibeGame) — 南大 & 南洋理工的 AI 原生游戏引擎与八角色 Agent 团队：Prompt-to-Game，试玩、反思、经验复用闭环
- [Voyager](https://github.com/MineDojo/Voyager) — Minecraft 开放世界中的技能库自进化智能体
- [Cradle](https://github.com/BAAI-Agents/Cradle) — 通用计算机控制智能体的交互式任务执行框架
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) — 面向代码仓库的自动修复智能体（Agent-Computer Interface）
- [OSWorld](https://github.com/xlang-ai/OSWorld) — 真实操作系统交互任务的可执行评测环境
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 自进化 Agent 资源合集（含经验 / 环境进化专题）

**论文**
- [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045) — 局部探索—诊断—改进循环 + 全局质量控制 + 经验内化，27B 组合超越 GPT-5.5 单次生成
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 自动课程 + 技能库 + 迭代提示的开放式自进化（被引 1500+）
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 语言化反思驱动智能体自我改进（被引 1900+）
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — 自我反馈迭代细化范式（被引 1800+）
- [Cradle: Empowering Foundation Agents Towards General Computer Control](https://arxiv.org/abs/2403.03186) — 通用计算机控制与交互式任务闭环
- [JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal LLMs](https://arxiv.org/abs/2311.05997) — 记忆增强的开放世界多任务智能体
- [Balrog: A General-Nonlinear Game Playing Agent](https://arxiv.org/abs/2402.13978) — NetHack 长时程游戏智能体
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 真实环境中的开放式任务评测
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — 执行反馈驱动的自动软件修复
- [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — 多环境智能体能力评测基准
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 可执行、可验证的长期交互环境
