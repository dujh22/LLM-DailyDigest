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

## 自研洞察

<!-- human-only:start 自研洞察｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->
*（待人工补充）*
<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->
*（待人工补充）*
<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->
1. **可执行性先验**：将文字意图绑定真实资源与状态依赖，再经探测运行、缺陷修复和结果验收生成任务；语义合理不能替代可执行性。
   - [CrossEnv：跨环境可验证任务合成](../../updates/2026-11-19/#crossenv) · 2026-11-19
   - [ScenarioForge：资源锚定与执行验证](../../updates/2026-11-18/#scenarioforge) · 2026-11-18
   - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
2. **结构化原生引擎**：生成可迭代作品时，应让智能体直接读写结构化状态，并以专业化角色交叉审查，降低黑盒运行后的定位与修复成本。
   - [VibeGame：AI 原生引擎与自进化智能体团队实现提示词生成游戏](../../updates/2026-10-31/#vibegame-ai) · 2026-10-31
3. **依赖深度度量**：长程难度应按必要顺序交互、工作量和需求依赖衡量，而非模型轮数；评测需在同一产物上串联依赖任务。
   - [Multi-step SWE：编码智能体的长程持续开发评测](../../updates/2026-11-06/#multi-step-swe) · 2026-11-06
   - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
4. **跨轮证据积累**：持续开发应保存版本状态、测试证据与未决缺陷，并让独立验收约束后续规划；单轮通过不能代表长期可维护。
   - [Harness-of-Harness：证据驱动持续开发](../../updates/2026-11-17/#harness-of-harness) · 2026-11-17
   - [Multi-step SWE：编码智能体的长程持续开发评测](../../updates/2026-11-06/#multi-step-swe) · 2026-11-06
5. **功能体验双验收**：游戏等开放作品应先用功能测试守住可运行底线，再以跨熟练度试玩和真人偏好评价技巧成长与交互乐趣。
   - [PlayCraft：基于游玩经验的游戏迭代](../../updates/2026-11-20/#playcraft) · 2026-11-20
   - [3D GameDev Arena：超长程游戏开发评测](../../updates/2026-11-19/#3d-gamedev-arena) · 2026-11-19
6. **快慢执行解耦**：实时任务中应把慢速反思放在尝试之间，并将经验编译为可执行程序供快速运行，避免在线推理延迟阻塞行动。
   - [SIGame：代码策略自我改进](../../updates/2026-11-20/#sigame) · 2026-11-20
7. **成功裕度评估**：二元成功率会掩盖脆弱方案；应记录成功轨迹的剩余预算或容错余量，以预测跨场景失败并优先修复。
   - [MARGIN：近失裕度驱动程序修复](../../updates/2026-11-25/#margin) · 2026-11-25
8. **前沿自适应刷新**：任务提出与求解应协同演化，并按优势、正确率和证据覆盖刷新题池；只增加难度会产生无效或错误监督。
   - [Search-RSI：能力前沿驱动搜索扩展](../../updates/2026-11-23/#search-rsi) · 2026-11-23
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [ZEST-Search：零标签异构协同演化训练工具高效搜索智能体](../../updates/2026-10-30/#zest-search) · 2026-10-30
9. **内生经验防投毒**：自生成任务可能把恶意行为固化为持久技能；经验入库前应隔离来源、审计行为并执行跨任务回归测试。
   - [BadEvolve：通过失败感知任务优化投毒自进化智能体](../../updates/2026-11-12/#badevolve) · 2026-11-12
10. **目标奖励解耦**：开放式探索中，应分别决定探索目标与奖励实现；职责解耦比直接改写奖励更易形成多样且可迁移的行为库。
    - [Habitats：开放式智能体目标演化](../../updates/2026-11-25/#habitats) · 2026-11-25
<!-- experience-seen: 2026-11-18/scenarioforge 2026-11-19/3d-gamedev-arena 2026-11-19/crossenv 2026-11-20/playcraft 2026-11-20/sigame 2026-11-23/search-rsi 2026-11-25/habitats 2026-11-25/margin -->
<!-- research-experience:end -->

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
