+++
title = 'AgentTrainEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# AgentTrainEvolve

> 研究方向：**Agent 训练侧自进化**——通过多轮 Agentic RL、自博弈与自生成课程，让 Agent 的参数在与环境交互中持续进化。

## 研究范畴

Agent 训练侧自进化（training-time agent self-evolution）关注如何把 Agent 在环境中的交互经验稳定地转化为参数更新：从早期的轨迹蒸馏 / 指令微调（AgentTuning），走向多轮、长程、带工具调用的 Agentic 强化学习，再到由 Agent 自己提出任务、构造课程、合成经验并自我博弈的零数据训练范式（Absolute Zero、SPIRAL、WebRL 的自进化在线课程）。本方向涵盖：面向 Agent 的 RL 训练框架与基础设施（verl、SkyRL、rLLM、Agent Lightning）、多轮交互下的信用分配与回合级奖励、自博弈与对抗式课程生成、经验合成与模拟环境放大（DreamGym 类）、训练-评测环境生态（AgentGym），以及 Agent RL 中的自进化动力学诊断（RAGEN 揭示的"回声陷阱"等失败模式）。社区关注的核心问题包括：长程稀疏奖励下训练是否稳定、自生成任务的难度与多样性如何自适应、训练出的能力能否跨环境迁移、以及 Agent RL 的算力与环境吞吐瓶颈如何突破。

## 研究挑战

- 多轮长程交互的信用分配与稀疏 / 延迟奖励。
- 自博弈与自生成课程的难度失控、多样性坍缩与"回声陷阱"。
- 环境吞吐与 rollout 成本成为训练瓶颈，异步与解耦训练框架仍在演进。
- 训练环境过拟合：在训练环境上提升但跨环境泛化差。
- 奖励作弊与评估器被攻陷（尤其在使用 LLM 作为奖励时）。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，训练侧自进化是《大语言模型复杂推理的自我进化机制》综述的核心路线之一。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理智能体评测与自进化平台，提供可程序化验证的任务族，可作为 Agent RL 训练环境。

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
1. **可验证环境闭环**：扩展训练任务前，先保证环境可执行，并用反事实实例或执行证据验证语义、自动修复缺陷；否则规模只会放大奖励巧合与噪声。
   - [CF Reward：反事实执行防奖励作弊](../../updates/2026-11-26/#cf-reward) · 2026-11-26
   - [VADE：专业源可验证任务合成](../../updates/2026-11-25/#vade) · 2026-11-25
   - [SWE-Gym-Verified：执行证据式数据审计](../../updates/2026-11-25/#swe-gym-verified) · 2026-11-25
   - [Online Environment Repair：在线修复验证环境](../../updates/2026-11-25/#online-environment-repair) · 2026-11-25
   - [Search-RSI：能力前沿驱动搜索扩展](../../updates/2026-11-23/#search-rsi) · 2026-11-23
   - [Game2Player：环境玩家协同演化](../../updates/2026-11-20/#game2player) · 2026-11-20
   - [Let Execution Do the Teaching：执行反馈驱动代码训练](../../updates/2026-11-17/#let-execution-do-the-teaching) · 2026-11-17
   - [奖励驱动的对撞机物理挑战：强化学习推动科研智能体自我改进](../../updates/2026-11-14/#item-42) · 2026-11-14
   - [SLIC：强化微调小语言模型实现多轮模拟电路优化](../../updates/2026-11-12/#slic) · 2026-11-12
   - [WildAWM：用合成“个人电脑”训练计算机使用智能体](../../updates/2026-11-08/#wildawm) · 2026-11-08
   - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
   - [WebHarbor：面向 GUI 智能体的真实网站环境套件](../../updates/2026-11-06/#webharbor-gui) · 2026-11-06
   - [ToolSpace：面向长程智能体的工具中心环境合成](../../updates/2026-11-05/#toolspace) · 2026-11-05
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [LegoEnv：通过模块化重组实现智能体环境自演化](../../updates/2026-11-03/#legoenv) · 2026-11-03
   - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
   - [VeriCUA：以智能体探索验证计算机操作智能体](../../updates/2026-10-30/#vericua) · 2026-10-30
   - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
2. **环境结构扩展**：数据扩展应优先增加工具、任务与环境覆盖，并保持跨服务实体、状态依赖及真实搜索和停止选择；重复轨迹或无结构堆量易造成泄漏和浅交互。
   - [智能体强化学习：三轴数据缩放定律](../../updates/2026-11-25/#item-20) · 2026-11-25
   - [SiliconGym：跨工具链EDA强化学习环境](../../updates/2026-11-21/#silicongym-eda) · 2026-11-21
   - [CrossEnv：跨环境可验证任务合成](../../updates/2026-11-19/#crossenv) · 2026-11-19
   - [RepoFactory：代码训练环境演化](../../updates/2026-11-18/#repofactory) · 2026-11-18
   - [RISE：全图交互环境扩展](../../updates/2026-11-17/#rise) · 2026-11-17
   - [WildAWM：用合成“个人电脑”训练计算机使用智能体](../../updates/2026-11-08/#wildawm) · 2026-11-08
   - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
   - [Agent-R²：基于真实来源数据合成扩展生产力智能体](../../updates/2026-11-08/#agent-r) · 2026-11-08
   - [ToolSpace：面向长程智能体的工具中心环境合成](../../updates/2026-11-05/#toolspace) · 2026-11-05
   - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
   - [Trajectory2Gym：面向工具使用智能体的决策驱动交互合成](../../updates/2026-10-29/#trajectory2gym) · 2026-10-29
   - [可控环境合成揭示工具使用智能体缩放定律](../../updates/2026-10-29/#item-58) · 2026-10-29
3. **信息增益课程**：优先采样能力边界、低覆盖或仍可能改变结果的任务，并为弱能力保留机会配额；从关键状态分支，用中间进度定位瓶颈，同时监测价值排序与表征多样性退化。
   - [FEAST：公平高效自适应采样](../../updates/2026-11-26/#feast) · 2026-11-26
   - [ReFocus：进度引导式瓶颈加练](../../updates/2026-11-25/#refocus) · 2026-11-25
   - [WEIR：分水岭探索与前缀收缩](../../updates/2026-11-23/#weir) · 2026-11-23
   - [Depth Before Breadth：反向课程与优势分解](../../updates/2026-11-20/#depth-before-breadth) · 2026-11-20
   - [SPG-Select：潜在画像引导任务选择](../../updates/2026-11-17/#spg-select) · 2026-11-17
   - [自适应课程下的强化学习训练稳定性](../../updates/2026-11-12/#item-209) · 2026-11-12
   - [ICRPM以前瞻风险预测优化Rollout任务采样](../../updates/2026-11-08/#icrpm-rollout) · 2026-11-08
   - [FADE：面向在线 RLVR 的能力—难度分解调度](../../updates/2026-11-06/#fade-rlvr) · 2026-11-06
   - [SWE-Trail：历史引导的编码智能体轨迹收集](../../updates/2026-11-04/#swe-trail) · 2026-11-04
   - [R²Orch：通过技能内化与自博弈实现智能体编排的递归自我改进](../../updates/2026-11-03/#r-orch) · 2026-11-03
   - [GUI 智能体的高效自适应训练：学习位置与 rollout 范围联合优化](../../updates/2026-10-30/#gui-rollout) · 2026-10-30
   - [EnvSched：面向高效 Rollout 的环境感知智能体强化学习调度](../../updates/2026-10-29/#envsched-rollout) · 2026-10-29
4. **轨迹分支复用**：保留环境或工作区检查点、共享续程与KV状态，在关键状态分支探索，可减少重复前缀执行并提高单位预算的轨迹价值。
   - [WEIR：分水岭探索与前缀收缩](../../updates/2026-11-23/#weir) · 2026-11-23
   - [BunshinRL：面向智能体强化学习的低内存工作空间分叉系统](../../updates/2026-11-12/#bunshinrl) · 2026-11-12
   - [TriGRPO：面向智能体强化学习的树上后见信用分配](../../updates/2026-11-06/#trigrpo) · 2026-11-06
   - [Octopus：基于潜在 KV 分支的单模型多智能体强化学习框架](../../updates/2026-11-06/#octopus-kv) · 2026-11-06
   - [SWE-Trail：历史引导的编码智能体轨迹收集](../../updates/2026-11-04/#swe-trail) · 2026-11-04
   - [GUI 智能体的高效自适应训练：学习位置与 rollout 范围联合优化](../../updates/2026-10-30/#gui-rollout) · 2026-10-30
   - [ConCal：通过续程共享校准长程智能体动作价值](../../updates/2026-10-29/#concal) · 2026-10-29
5. **长程信用细化**：终局奖励应按证据增益、语义阶段或责任模块下沉到关键动作。全局失败时可用当前策略续跑估值局部选项，并以过程判断或反事实结果校准。
   - [SPLICE：学习者条件选项拼接](../../updates/2026-11-26/#splice) · 2026-11-26
   - [RLVB：可验证信念奖励决策时机](../../updates/2026-11-25/#rlvb) · 2026-11-25
   - [MSPO：模块特定信用分配](../../updates/2026-11-25/#mspo) · 2026-11-25
   - [FGL：修复器似然引导代码定位](../../updates/2026-11-25/#fgl) · 2026-11-25
   - [SH-PRM：语义分段短程监督](../../updates/2026-11-23/#sh-prm) · 2026-11-23
   - [DM-PRM：决策模型零样本过程奖励](../../updates/2026-11-23/#dm-prm) · 2026-11-23
   - [ECA：证据增益式信用分配](../../updates/2026-11-19/#eca) · 2026-11-19
   - [OPSD4MAS：将多智能体通信转化为词元级信用](../../updates/2026-11-14/#opsd4mas) · 2026-11-14
   - [OMA：控制多轮智能体强化学习中的长度依赖轨迹影响](../../updates/2026-11-14/#oma) · 2026-11-14
   - [行动者、评判者还是教师？长时程智能体中的决策模型](../../updates/2026-11-14/#item-11) · 2026-11-14
   - [TreeOPSD：树式信用分配提升深度研究智能体准确率](../../updates/2026-11-13/#treeopsd) · 2026-11-13
   - [TACA：面向工具调用转移的信用分配](../../updates/2026-11-12/#taca) · 2026-11-12
   - [MCPO：基于边际犹豫度的 Token 信用分配](../../updates/2026-11-12/#mcpo-token) · 2026-11-12
   - [即插即用验证器解耦过程奖励，稳定长程智能体推理](../../updates/2026-11-12/#item-167) · 2026-11-12
   - [AgentOPSD：递归信念修正实现轮次级信用分配](../../updates/2026-11-12/#agentopsd) · 2026-11-12
   - [AttnSR：基于注意力的长程智能体步级奖励分配](../../updates/2026-11-08/#attnsr) · 2026-11-08
   - [TurnWise：回合级信用分配推进流式视频强化学习](../../updates/2026-11-06/#turnwise) · 2026-11-06
   - [TriGRPO：面向智能体强化学习的树上后见信用分配](../../updates/2026-11-06/#trigrpo) · 2026-11-06
   - [SGR-OPSD：基于子目标规划与图正则信用分配的智能体强化学习](../../updates/2026-11-06/#sgr-opsd) · 2026-11-06
   - [ORSD：动态过程准则驱动的特权词元级信用分配](../../updates/2026-11-06/#orsd) · 2026-11-06
   - [Octopus：基于潜在 KV 分支的单模型多智能体强化学习框架](../../updates/2026-11-06/#octopus-kv) · 2026-11-06
   - [BLPO：面向长程 LLM 智能体的跨任务策略优化](../../updates/2026-11-06/#blpo-llm) · 2026-11-06
   - [CREDO：面向时序推理智能体的证据条件信用分配](../../updates/2026-11-03/#credo) · 2026-11-03
   - [CivHarness：以回放反馈训练长程 Freeciv 智能体](../../updates/2026-11-02/#civharness-freeciv) · 2026-11-02
   - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
   - [ConCal：通过续程共享校准长程智能体动作价值](../../updates/2026-10-29/#concal) · 2026-10-29
6. **训练要素共演**：开放式任务中，观测、数据、奖励与脚手架应随策略能力共演；分解目标发现与奖励实现，并门控失活信号，避免固定结构耗尽优化空间。
   - [Sports Agent：反馈驱动闭环自进化](../../updates/2026-11-26/#sports-agent) · 2026-11-26
   - [Habitats：开放式智能体目标演化](../../updates/2026-11-25/#habitats) · 2026-11-25
   - [Sage-Evolve-Preview：自适应观测驱动持续改进](../../updates/2026-11-20/#sage-evolve-preview) · 2026-11-20
   - [Piccolo：模型数据协同自进化](../../updates/2026-11-20/#piccolo) · 2026-11-20
   - [Evo²：权重与Harness协同进化](../../updates/2026-11-20/#evo-harness) · 2026-11-20
   - [WATERFALL：进化式奖励发现](../../updates/2026-11-19/#waterfall) · 2026-11-19
   - [ModHarness-RL：可学习演化脚手架](../../updates/2026-11-16/#modharness-rl) · 2026-11-16
   - [RuACT：将失活评分准则转化为自适应批评者与教师](../../updates/2026-11-12/#ruact) · 2026-11-12
   - [ORSD：动态过程准则驱动的特权词元级信用分配](../../updates/2026-11-06/#orsd) · 2026-11-06
   - [Self-Evolving Rubrics：自进化准则驱动强化学习](../../updates/2026-11-02/#self-evolving-rubrics) · 2026-11-02
   - [RACE：策略与评分准则的奖励自适应协同演化](../../updates/2026-10-30/#race) · 2026-10-30
7. **分工通信共演**：多智能体训练可用客观共享结果与时限让分工、通信和评审自主涌现；零数据可让异构角色共演，但长期互审须奖励验证证据，防止结果奖励诱发合谋。
   - [PROVE：证据驱动的协议强化](../../updates/2026-11-26/#prove) · 2026-11-26
   - [多玩家社交游戏：可验证社会智能训练](../../updates/2026-11-25/#item-63) · 2026-11-25
   - [Avalon-M1：集体奖励组织训练](../../updates/2026-11-25/#avalon-m1) · 2026-11-25
   - [s³：通过协作式多智能体强化学习扩展智能体群体](../../updates/2026-11-12/#item-215) · 2026-11-12
   - [R²Orch：通过技能内化与自博弈实现智能体编排的递归自我改进](../../updates/2026-11-03/#r-orch) · 2026-11-03
   - [ZEST-Search：零标签异构协同演化训练工具高效搜索智能体](../../updates/2026-10-30/#zest-search) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
8. **失败恢复训练**：多轮RL的主要增益常是错误恢复而非单步知识；应把失败现场、恢复示范和续跑结果显式纳入训练。
   - [SPLICE：学习者条件选项拼接](../../updates/2026-11-26/#splice) · 2026-11-26
   - [DeLoop：重复动作自监督脱环](../../updates/2026-11-17/#deloop) · 2026-11-17
   - [SteerDistill：闭环教师引导的 LLM 智能体量化](../../updates/2026-11-13/#steerdistill-llm) · 2026-11-13
   - [TopoVerus：基于学习反例与课程奖励的形式化证明修复](../../updates/2026-11-12/#topoverus) · 2026-11-12
   - [AutoScaffold：AI 自动生成自适应训练脚手架](../../updates/2026-11-12/#autoscaffold-ai) · 2026-11-12
   - [Harness-S：从同源脚手架学习实现可泛化智能体训练](../../updates/2026-11-06/#harness-s) · 2026-11-06
   - [多轮强化学习究竟提升了 LLM 智能体的什么能力？](../../updates/2026-11-05/#llm-3) · 2026-11-05
   - [ReTerm：让Code Agent从失败恢复中递归自我改进](../../updates/2026-11-04/#reterm-code-agent) · 2026-11-04
9. **预算混合训练**：长程或跨域策略要混合交互预算与渐进式rollout范围，并按领域和掌握程度配额梯度与探索样本；单一预算或强域主导会损害部署稳健性。
   - [Maco-RL：配额调度与三缓冲采样](../../updates/2026-11-26/#maco-rl) · 2026-11-26
   - [多轮强化学习究竟提升了 LLM 智能体的什么能力？](../../updates/2026-11-05/#llm-3) · 2026-11-05
   - [GUI 智能体的高效自适应训练：学习位置与 rollout 范围联合优化](../../updates/2026-10-30/#gui-rollout) · 2026-10-30
10. **在策略经验蒸馏**：蒸馏应在学生实际访问的状态上，以执行证据校准动作或自然语言监督，并确保轨迹只依赖部署可见信息；无需复制隐藏思维链，逐词拟合教师反而会掩盖退化。
    - [CoT-Proxy：跨格式长程策略蒸馏](../../updates/2026-11-26/#cot-proxy) · 2026-11-26
    - [CARE-OPD：覆盖采集与证据回放](../../updates/2026-11-26/#care-opd) · 2026-11-26
    - [CGSI：上下文对齐技能内化](../../updates/2026-11-25/#cgsi) · 2026-11-25
    - [Tool-to-Self：视觉工具能力内化](../../updates/2026-11-24/#tool-to-self) · 2026-11-24
    - [ADAPT：成本感知求助后训练](../../updates/2026-11-24/#adapt) · 2026-11-24
    - [SEED：自进化在策略蒸馏](../../updates/2026-11-19/#seed) · 2026-11-19
    - [COPD：通信式黑箱在策略蒸馏](../../updates/2026-11-19/#copd) · 2026-11-19
    - [SWE-OPD：仓库交互式在策略蒸馏](../../updates/2026-11-18/#swe-opd) · 2026-11-18
    - [HARNESS-ZERO：智能体驱动的脚手架蒸馏](../../updates/2026-11-17/#harness-zero) · 2026-11-17
    - [JudgeMix：评判器引导的混合轨迹智能体数据合成](../../updates/2026-11-14/#judgemix) · 2026-11-14
    - [Reframe：观测对齐的多教师在策略蒸馏提升智能体视觉推理](../../updates/2026-11-12/#reframe) · 2026-11-12
    - [哪些成功轨迹适合作为参考？面向多轮在策略蒸馏的动作序列对齐](../../updates/2026-11-12/#item-95) · 2026-11-12
    - [ECOS：环境校准的智能体在策略自蒸馏](../../updates/2026-11-12/#ecos) · 2026-11-12
    - [CAMP-II：通过在策略蒸馏释放文件操作的长期记忆潜力](../../updates/2026-11-12/#camp-ii) · 2026-11-12
    - [SCOPE：从局部技能渐进探索长程网页任务](../../updates/2026-11-06/#scope) · 2026-11-06
    - [RLiD：在决策平面强化学习语言智能体](../../updates/2026-11-06/#rlid) · 2026-11-06
    - [MDSKILL：多视图蒸馏实现技能记忆内化与智能体自进化](../../updates/2026-11-06/#mdskill) · 2026-11-06
    - [稳定智能体强化学习中的在策略定向引导](../../updates/2026-11-06/#item-53) · 2026-11-06
    - [ActionOPD：面向智能体决策的动作级在策略蒸馏](../../updates/2026-11-01/#actionopd) · 2026-11-01
11. **轨迹预热强化**：先用可执行、技能塑形且覆盖部署接口的轨迹SFT建立行为先验，工具样本须保留体现调用优势的调用前推理；筛除成功轨迹中的坏习惯后再做执行奖励RL。
    - [PRIOR：调用前推理保留工具能力](../../updates/2026-11-26/#prior) · 2026-11-26
    - [Harness Rehearsal：任务与接口能力解耦](../../updates/2026-11-25/#harness-rehearsal) · 2026-11-25
    - [AutoMaster：技能引导式自主后训练](../../updates/2026-11-20/#automaster) · 2026-11-20
    - [RSI-Prime：决策级损失掩码训练](../../updates/2026-11-19/#rsi-prime) · 2026-11-19
    - [Agent-R²：基于真实来源数据合成扩展生产力智能体](../../updates/2026-11-08/#agent-r) · 2026-11-08
    - [Axion 1.0：简化训练的开放智能体基础模型](../../updates/2026-11-05/#axion-1-0) · 2026-11-05
    - [HarnessSQL：面向真实数据库的长程交互 SQL Agent 训练框架](../../updates/2026-11-04/#harnesssql-sql-agent) · 2026-11-04
    - [Trajectory2Gym：面向工具智能体的决策接地交互合成](../../updates/2026-11-03/#trajectory2gym) · 2026-11-03
    - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
12. **递归更新审计**：每轮更新前后应审计能力骤降、表征多样性、验证器盲区及训练—执行错位；异常时由专门化监督验证并回滚或收缩更新，按不确定性调组规模。
    - [AutoRL：多智能体自治强化学习](../../updates/2026-11-28/#autorl) · 2026-11-28
    - [U-Statistics-Powered LLM Reasoning：悲观估计自适应组规模](../../updates/2026-11-26/#u-statistics-powered-llm-reasoning) · 2026-11-26
    - [Online Environment Repair：在线修复验证环境](../../updates/2026-11-25/#online-environment-repair) · 2026-11-25
    - [EPRO：不完美预测下的鲁棒策略优化](../../updates/2026-11-25/#epro) · 2026-11-25
    - [AgriManager：农业策略模式迁移评测](../../updates/2026-11-24/#agrimanager) · 2026-11-24
    - [SiliconGym：跨工具链EDA强化学习环境](../../updates/2026-11-21/#silicongym-eda) · 2026-11-21
    - [Stability Gap：持续强化学习稳定性缺口](../../updates/2026-11-20/#stability-gap) · 2026-11-20
    - [Optimistic Verifiers：精确过程预言机审计](../../updates/2026-11-18/#optimistic-verifiers) · 2026-11-18
    - [Jev-as-a-Reward：概率安全评判验证](../../updates/2026-11-18/#jev-as-a-reward) · 2026-11-18
    - [TrainExplorer：规划解耦式后训练探索](../../updates/2026-11-17/#trainexplorer) · 2026-11-17
    - [G-CAST：治理式持续自训练](../../updates/2026-11-16/#g-cast) · 2026-11-16
    - [AutoRL：多智能体闭环强化学习](../../updates/2026-11-16/#autorl) · 2026-11-16
    - [前沿编程 LLM 是在编码还是作弊？](../../updates/2026-11-12/#llm-7) · 2026-11-12
    - [自适应课程下的强化学习训练稳定性](../../updates/2026-11-12/#item-209) · 2026-11-12
    - [基于监控器的强化学习奖励作弊干预设计](../../updates/2026-11-12/#item-177) · 2026-11-12
    - [RL 后训练为何失效：实战教训与排障指南](../../updates/2026-11-12/#item-149) · 2026-11-12
    - [Continual-ARC：衡量智能体终身技能习得](../../updates/2026-11-12/#continual-arc) · 2026-11-12
    - [Agentic-OPD：通过在策略蒸馏恢复智能体遗忘能力](../../updates/2026-11-12/#agentic-opd) · 2026-11-12
    - [群体依赖奖励下，GRPO会演变为零和锦标赛](../../updates/2026-11-06/#grpo) · 2026-11-06
    - [RSI-Master：受控实验驱动的自主模型改进](../../updates/2026-10-30/#rsi-master) · 2026-10-30
    - [RSI Arena：基于人类反馈的递归自我改进实验](../../updates/2026-10-30/#rsi-arena) · 2026-10-30
    - [下一轮部署前：诊断策略更新引发的技能效用变化](../../updates/2026-10-30/#item-72) · 2026-10-30
13. **一致参数扰动**：RLVR探索不足时，可对整条轨迹保持一致的参数扰动，以增加解法多样性和分布外泛化。
    - [PSN-RLVR：参数空间噪声恢复强化学习模型探索能力](../../updates/2026-10-30/#psn-rlvr) · 2026-10-30
14. **去模型化深度**：用任务工作量、结构复杂度和必要顺序交互深度标注长程难度，不用模型轮数或成功率，避免课程随基座变化而失真。
    - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
    - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
15. **部署经验飞轮**：将真实执行与用户反馈按后续轨迹增益及对当前优化的边际贡献策展，经技能验证、修复和分阶段再训练形成飞轮；仅内化验证通过且梯度方向有益的经验。
    - [vSFT：语言监督式测试时调优](../../updates/2026-11-26/#vsft) · 2026-11-26
    - [E2L：梯度对齐经验演化](../../updates/2026-11-25/#e2l) · 2026-11-25
    - [From Acting to Learning：优化器感知梯度选样](../../updates/2026-11-23/#from-acting-to-learning) · 2026-11-23
    - [Terminal-RSI：递归改写与策略精炼](../../updates/2026-11-17/#terminal-rsi) · 2026-11-17
    - [ACE-RL：基于经验交接强化学习的递归自我改进](../../updates/2026-11-14/#ace-rl) · 2026-11-14
    - [知识在脚手架、可靠性在权重：无教师智能体协同演化](../../updates/2026-11-13/#item-26) · 2026-11-13
    - [NeoHorse-1.5-Flash Preview开启Agent模型RSI第二轮迭代](../../updates/2026-11-12/#neohorse-1-5-flash-preview-agent-rsi) · 2026-11-12
    - [ENGRAM：通过验证式巩固将智能体经验内化为权重](../../updates/2026-11-12/#engram) · 2026-11-12
    - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
    - [ReTerm：让Code Agent从失败恢复中递归自我改进](../../updates/2026-11-04/#reterm-code-agent) · 2026-11-04
    - [NorthCUA：以规模化经验加速计算机操作智能体](../../updates/2026-11-04/#northcua) · 2026-11-04
    - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
    - [百度搜索通过在线反馈闭环实现递归自我进化](../../updates/2026-11-01/#item-1) · 2026-11-01
<!-- experience-seen: 2026-11-21/silicongym-eda 2026-11-21/zerovln 2026-11-23/ctrl-gpu 2026-11-23/dm-prm 2026-11-23/from-acting-to-learning 2026-11-23/search-rsi 2026-11-23/sh-prm 2026-11-23/weir 2026-11-24/adapt 2026-11-24/agrimanager 2026-11-24/duopra 2026-11-24/stride 2026-11-24/tool-to-self 2026-11-25/avalon-m1 2026-11-25/cgsi 2026-11-25/co-graft 2026-11-25/e2l 2026-11-25/epro 2026-11-25/fgl 2026-11-25/habitats 2026-11-25/harness-rehearsal 2026-11-25/item-20 2026-11-25/item-63 2026-11-25/jko-grpo-wasserstein 2026-11-25/mspo 2026-11-25/online-environment-repair 2026-11-25/refocus 2026-11-25/rlvb 2026-11-25/swe-gym-verified 2026-11-25/vade 2026-11-26/care-opd 2026-11-26/cf-reward 2026-11-26/cot-proxy 2026-11-26/feast 2026-11-26/maco-rl 2026-11-26/prior 2026-11-26/prove 2026-11-26/splice 2026-11-26/sports-agent 2026-11-26/u-statistics-powered-llm-reasoning 2026-11-26/vsft 2026-11-28/autorl -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [verl](https://github.com/verl-project/verl) — 字节跳动开源的 LLM RL 训练框架，Agentic RL 主流基础设施
- [SkyRL](https://github.com/NovaSky-AI/SkyRL) — 面向长程多轮 Agent 任务的模块化 RL 框架
- [rLLM](https://github.com/rllm-org/rllm) — Agentica 面向语言 Agent 后训练的 RL 框架
- [Agent Lightning](https://github.com/microsoft/agent-lightning) — 微软"训练任意 Agent"的 RL 框架，训练与 Agent 实现解耦
- [ART](https://github.com/OpenPipe/ART) — Agent Reinforcement Trainer，多轮 Agent 的 GRPO 训练
- [AgentGym](https://github.com/WooooDyy/AgentGym) — 多环境 Agent 训练-评测平台与自进化方法 AgentEvol
- [WebRL](https://github.com/THUDM/WebRL) — 自进化在线课程 RL 训练 Web Agent
- [RAGEN](https://github.com/mll-lab-nu/RAGEN) — 多轮 RL 训练 Agent 并诊断自进化失败模式
- [Absolute Zero Reasoner](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) — 零数据自博弈：模型自己出题、自己解题
- [SPIRAL](https://github.com/spiral-rl/spiral) — 零和博弈自博弈激发推理能力
- [AgentTuning](https://github.com/THUDM/AgentTuning) — 轨迹微调赋予 LLM 通用 Agent 能力
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 自进化 Agent 系统：自问、自导航、自归因

**论文**
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) — Agentic RL 全景综述
- [AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823)
- [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151)
- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337)
- [RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073) — StarPO 框架与"回声陷阱"
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)
- [SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2506.24119)
- [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) — SPIN
- [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) — 多轮信用分配
- [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680)
- [Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773) — DreamGym：合成经验放大 Agent RL
- [AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395)
