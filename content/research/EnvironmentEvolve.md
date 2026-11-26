+++
title = 'EnvironmentEvolve'
proposer = '杜晋华'
since = '2026-09-24'
date = 2026-09-24T00:00:00+08:00
draft = false
toc = true
+++

# EnvironmentEvolve

> 研究方向：**环境自进化**——智能体训练环境的自动合成、难度进化与智能体—环境协同演化。

## 研究范畴

环境自进化（environment self-evolution / environment engineering）把训练环境本身当作可进化对象：环境 E 由任务生成器、执行载体和验证器组成，是一台可扩展的经验数据生产机器（d = (E, q, τ, v)）。本方向涵盖：训练环境与任务的自动合成（API 池 / 工具图 / 代码化环境）、环境逐组件自纠错、同一策略兼任环境生成器与求解器的协同进化（EvoEnv 类）、存量 benchmark 的插件化改装复用，以及 Environment-as-a-Service 等基础设施形态。社区关注的核心问题包括：环境必须同时满足可执行与可验证这一质量底线、任务难度如何持续对准模型能力边界（自动课程）、环境规模是否存在 scaling law，以及智能体进化与环境进化如何形成稳定的共同进化闭环。

## 研究挑战

- 可执行性与可验证性保障：破坏任一条，环境产出的就不是数据而是噪声。
- 全自动环境生成的质量控制——LLM 直接造环境的可靠性仍不过关，需逐组件自纠错与验证棘轮。
- 难度对准能力边界：自进化可行的关键是模型能为"自己解不出的题"写出可靠验证代码。
- 验证器被钻空子（reward hacking）：奖励作弊会随环境规模放大。
- 环境池与策略协同进化的非平稳性、多样性坍缩与成本膨胀。
- 合成环境与真实任务分布的对齐（sim-to-real gap）。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 元数据驱动的可验证任务合成平台（Sudoku/迷宫/Knights&Knaves/Zebra/代码推理等），任务生成器＋验证器的可编程环境雏形。
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
1. **执行验证共设计**：规模化合成任务时应同步保证环境可执行、结果可验证；只扩任务数量会放大坏环境与奖励噪声。
   - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
   - [CrossEnv：跨环境可验证任务合成](../../updates/2026-11-19/#crossenv) · 2026-11-19
   - [ScenarioForge：资源锚定与执行验证](../../updates/2026-11-18/#scenarioforge) · 2026-11-18
   - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
   - [VAST：可验证漏洞场景编译](../../updates/2026-11-17/#vast) · 2026-11-17
   - [奖励驱动的对撞机物理挑战：强化学习推动科研智能体自我改进](../../updates/2026-11-14/#item-42) · 2026-11-14
   - [WildAWM：用合成“个人电脑”训练计算机使用智能体](../../updates/2026-11-08/#wildawm) · 2026-11-08
   - [Scientist World：面向 AI 科学家的可执行研究世界](../../updates/2026-11-08/#scientist-world-ai) · 2026-11-08
   - [ToolSpace：面向长程智能体的工具中心环境合成](../../updates/2026-11-05/#toolspace) · 2026-11-05
   - [LegoEnv：通过模块化重组实现智能体环境自演化](../../updates/2026-11-03/#legoenv) · 2026-11-03
   - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
   - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
2. **先探索后生成**：先执行 API、轨迹或工具图以识别真实依赖，再反向生成任务，比从文本意图直接出题更易获得长程接地交互。
   - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
   - [ToolSpace：面向长程智能体的工具中心环境合成](../../updates/2026-11-05/#toolspace) · 2026-11-05
   - [Trajectory2Gym：面向工具智能体的决策接地交互合成](../../updates/2026-11-03/#trajectory2gym) · 2026-11-03
   - [Trajectory2Gym：面向工具使用智能体的决策驱动交互合成](../../updates/2026-10-29/#trajectory2gym) · 2026-10-29
3. **组件化环境重组**：将意图、规则、数据、服务与工具拆成可复用原子，通过重组扩展环境，比逐任务手工搭建更易维护和演化。
   - [LegoEnv：通过模块化重组实现智能体环境自演化](../../updates/2026-11-03/#legoenv) · 2026-11-03
   - [从手工到自进化：Agent 环境扩展五篇论文](../../updates/2026-10-30/#agent) · 2026-10-30
4. **闭环环境修复**：环境上线前应用探测执行、强弱模型质量锚点和对抗审计排查缺陷；训练中还应异步修补被策略利用的验证器。
   - [Online Environment Repair：在线修复验证环境](../../updates/2026-11-25/#online-environment-repair) · 2026-11-25
   - [Openhagen Worlds：校准式科学发现环境](../../updates/2026-11-20/#openhagen-worlds) · 2026-11-20
   - [Benchmark Factory：无标签质量锚点造基准](../../updates/2026-11-17/#benchmark-factory) · 2026-11-17
   - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
   - [Gym-Anything：用编程智能体规模化构建机器人仿真](../../updates/2026-10-30/#gym-anything) · 2026-10-30
   - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
5. **生成求解协同演化**：让任务提出者、求解器、验证器与演化器分工，并用执行反馈同步更新任务分布和证据边界，可在少标注下持续扩展能力边界。
   - [CUA-SEE：任务验证器协同演化](../../updates/2026-11-25/#cua-see) · 2026-11-25
   - [Search-RSI：能力前沿驱动搜索扩展](../../updates/2026-11-23/#search-rsi) · 2026-11-23
   - [PlayCraft：基于游玩经验的游戏迭代](../../updates/2026-11-20/#playcraft) · 2026-11-20
   - [Game2Player：环境玩家协同演化](../../updates/2026-11-20/#game2player) · 2026-11-20
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [ZEST-Search：零标签异构协同演化训练工具高效搜索智能体](../../updates/2026-10-30/#zest-search) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
6. **学习信号驱动课程**：课程应依据覆盖度、优势信号和正确率变化动态选题；优先低覆盖高信息任务，并在收益停滞时刷新题池。
   - [SPG-Select：潜在画像引导任务选择](../../updates/2026-11-17/#spg-select) · 2026-11-17
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [EnvSched：面向高效 Rollout 的环境感知智能体强化学习调度](../../updates/2026-10-29/#envsched-rollout) · 2026-10-29
7. **自适应课程防退化**：自适应环境课程不保证优于简单起点，还可能导致参数膨胀、价值排序退化与表征坍缩；需用稳定学习器和统一预算对照。
   - [自适应课程下的强化学习训练稳定性](../../updates/2026-11-12/#item-209) · 2026-11-12
   - [四足机器人无监督环境设计与课程学习基准](../../updates/2026-10-30/#item-41) · 2026-10-30
8. **内在结构度量难度**：长程任务难度宜用必要工作量、依赖组合和最短顺序交互深度度量，避免采用随模型策略变化的轮数标签。
   - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
   - [RepoFactory：代码训练环境演化](../../updates/2026-11-18/#repofactory) · 2026-11-18
   - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
   - [Trajectory2Gym：面向工具使用智能体的决策驱动交互合成](../../updates/2026-10-29/#trajectory2gym) · 2026-10-29
9. **可控多样性缩放**：分别控制工具、任务和数据库多样性，才能归因环境规模带来的泛化收益，并建立可用于预算规划的缩放关系。
   - [可控环境合成揭示工具使用智能体缩放定律](../../updates/2026-10-29/#item-58) · 2026-10-29
10. **动态证据验证**：动态环境中应组合 GUI 探索、代码检查和领域规则收集证据，并区分智能体失误、环境漂移与评分器错误。
    - [CUA-SEE：任务验证器协同演化](../../updates/2026-11-25/#cua-see) · 2026-11-25
    - [BenchMint：任务与评分联合构建](../../updates/2026-11-25/#benchmint) · 2026-11-25
    - [Gandalf：量规驱动的环境对齐验证](../../updates/2026-11-19/#gandalf) · 2026-11-19
    - [LiveGeo：持续演化地理世界中的智能体评测](../../updates/2026-11-14/#livegeo) · 2026-11-14
    - [SynthCorp：面向数据智能体的可定制基准生成平台](../../updates/2026-11-13/#synthcorp) · 2026-11-13
    - [Veritas：面向智能体任务的自动验证器生成框架](../../updates/2026-11-12/#veritas) · 2026-11-12
    - [VeriCUA：以智能体探索验证计算机操作智能体](../../updates/2026-10-30/#vericua) · 2026-10-30
    - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30
11. **真实来源合成**：从真实服务轨迹、职业工作流和多格式文件抽取结构再合成，可兼顾规模与真实性，并支持合成训练向分布外任务迁移。
    - [VADE：专业源可验证任务合成](../../updates/2026-11-25/#vade) · 2026-11-25
    - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
    - [BenchMint：任务与评分联合构建](../../updates/2026-11-25/#benchmint) · 2026-11-25
    - [WildAWM：用合成“个人电脑”训练计算机使用智能体](../../updates/2026-11-08/#wildawm) · 2026-11-08
    - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
    - [Agent-R²：基于真实来源数据合成扩展生产力智能体](../../updates/2026-11-08/#agent-r) · 2026-11-08
    - [ToolSpace：面向长程智能体的工具中心环境合成](../../updates/2026-11-05/#toolspace) · 2026-11-05
    - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
12. **状态化服务底座**：用容器或微虚拟机解耦任务、训练与评测，并统一管理隔离、持久化、分岔、回滚和迁移；状态生命周期与预算都需显式约束。
    - [γ-Scape：智能体中心具身世界](../../updates/2026-11-24/#scape) · 2026-11-24
    - [SiliconGym：跨工具链EDA强化学习环境](../../updates/2026-11-21/#silicongym-eda) · 2026-11-21
    - [CubeSandbox：状态化微虚拟机沙箱](../../updates/2026-11-18/#cubesandbox) · 2026-11-18
    - [WebHarbor：面向 GUI 智能体的真实网站环境套件](../../updates/2026-11-06/#webharbor-gui) · 2026-11-06
    - [RSIGym：面向递归自我改进的真实训练环境](../../updates/2026-11-05/#rsigym) · 2026-11-05
13. **可验证奖励闭环**：长程任务应以客观结果或行为证据构造奖励，并把终局结果归因到回合。目标探索与奖励实现宜解耦，避免稀疏或可利用的模型裁判。
    - [多玩家社交游戏：可验证社会智能训练](../../updates/2026-11-25/#item-63) · 2026-11-25
    - [Habitats：开放式智能体目标演化](../../updates/2026-11-25/#habitats) · 2026-11-25
    - [WATERFALL：进化式奖励发现](../../updates/2026-11-19/#waterfall) · 2026-11-19
    - [奖励驱动的对撞机物理挑战：强化学习推动科研智能体自我改进](../../updates/2026-11-14/#item-42) · 2026-11-14
    - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
14. **持续状态评测**：静态终态任务不足以评估适应性；应让前序动作持续影响后续状态，并加入实时反馈、相对动态目标与持久规则，检验动态改计划能力。
    - [γ-Scape：智能体中心具身世界](../../updates/2026-11-24/#scape) · 2026-11-24
    - [TuringSpace：交互验证码训练空间行动](../../updates/2026-11-21/#turingspace) · 2026-11-21
    - [WorldRuler：可配置规则世界建模](../../updates/2026-11-20/#worldruler) · 2026-11-20
    - [相对动态目标生成驾驶场景](../../updates/2026-11-20/#item-73) · 2026-11-20
    - [RoboFinals RL Envs：物理可信长程仿真](../../updates/2026-11-17/#robofinals-rl-envs) · 2026-11-17
    - [LiveGeo：持续演化地理世界中的智能体评测](../../updates/2026-11-14/#livegeo) · 2026-11-14
    - [TSSDA：自主构建时序 Text-to-SQL 基准的智能体](../../updates/2026-11-06/#tssda-text-to-sql) · 2026-11-06
    - [GameVerse：面向长时程交互式世界建模的分钟级游戏数据集](../../updates/2026-11-06/#gameverse) · 2026-11-06
    - [Gym-Anything-RT：视觉语言智能体实时交互评测基准](../../updates/2026-10-29/#gym-anything-rt) · 2026-10-29
15. **固定环境优化**：固定环境可裁剪无关功能以降本，但必须保留完整搜索空间、奖励路径与应用数据；预过滤会泄露答案并高估能力。
    - [MobileGym-Lite：完整覆盖与功能裁剪](../../updates/2026-11-19/#mobilegym-lite) · 2026-11-19
    - [RISE：全图交互环境扩展](../../updates/2026-11-17/#rise) · 2026-11-17
    - [EnvOpt：自动优化智能体的固定环境](../../updates/2026-11-06/#envopt) · 2026-11-06
<!-- experience-seen: 2026-11-18/cubesandbox 2026-11-18/embedgym 2026-11-18/repofactory 2026-11-18/scenarioforge 2026-11-19/crossenv 2026-11-19/gandalf 2026-11-19/mobilegym-lite 2026-11-19/waterfall 2026-11-20/buggymle 2026-11-20/game2player 2026-11-20/gemini-4-neon-genie-4 2026-11-20/item-73 2026-11-20/openhagen-worlds 2026-11-20/playcraft 2026-11-20/worldruler 2026-11-21/silicongym-eda 2026-11-21/turingspace 2026-11-23/search-rsi 2026-11-24/scape 2026-11-25/benchmint 2026-11-25/cua-see 2026-11-25/habitats 2026-11-25/item-63 2026-11-25/online-environment-repair 2026-11-25/robouniverse-10k 2026-11-25/vade -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [AgentGym](https://github.com/WooooDyy/AgentGym) — 跨多样环境进化 LLM 智能体的框架与环境套件
- [meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments) — Meta 智能体研究环境平台
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统，含任务/环境自主构造
- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 零数据自进化：同一模型兼任出题者与求解者
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含环境进化专题的自进化 Agent 合集

**论文**
- [EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents](https://arxiv.org/abs/2403.12014) — LLM 按智能体弱项动态生成训练环境
- [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://arxiv.org/abs/2405.15568) — 代码化环境的开放式生成
- [Eurekaverse: Environment Curriculum Generation via LLM](https://arxiv.org/abs/2411.01775) — LLM 环境课程生成
- [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) — 神经路线的可交互生成环境（世界模型）
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) — 自博弈出题—求解闭环，任务分布随能力进化
- [CogEvol：迈向高效可靠的学习环境生成](https://huggingface.co/papers/2608.30968) — 交互式学习环境单次生成 + GRPO 训练，修复"视觉逼真但不可玩"的奖励作弊

**综述 / 报道**
- [Agentic Environment Engineering：智能体环境工程综述](https://mp.weixin.qq.com/s/FAqFpQw6MZoM9iph9Fu_4w) — 以环境生命周期为主线，提出智能体—环境共同进化闭环与 Environment-as-a-Service
- [从手工构建到自进化：Agent 环境扩展五篇论文（RLVE / AgentScaler / AWM / EvoEnv / EnvHarness）](https://mp.weixin.qq.com/s/zEge9AxeQXJFxjmYOD74FA) — 统一形式化框架下的环境扩展演进线：人工构建 → 自动合成 → 自纠错生成 → 协同进化 → 存量改装
