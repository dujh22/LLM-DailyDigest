+++
title = 'HarnessEvolve'
proposer = '杜晋华'
since = '2026-03-12'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# HarnessEvolve

> 研究方向：**评测 harness 的演进**——围绕 lm-evaluation-harness / SWE-bench 类工具的扩展与进化（本站已 fork 相关仓库）。

## 研究范畴

评测 / Agent harness 的演进，围绕 lm-evaluation-harness、SWE-bench 类工具及其扩展与进化展开。harness（含 Agent-Computer Interface、运行环境、工具与提示约定）显著影响甚至主导模型在 Agent 任务上的表现，因此其工程化与标准化日益重要。本方向涵盖：harness engineering、ACI 设计、真实运行环境构建，以及 harness 效应的度量和披露。社区关注的核心问题包括：harness 设计在多大程度上改变了模型间的相对排名、如何标准化披露 harness 配置以保证可比与可复现、环境真实度（realism）与隔离 / 安全的权衡，以及动态 / 长周期环境下的 harness 演进。

## 研究挑战

- 环境搭建与维护成本高、易腐化。
- 跨模型公平性与配置漂移。
- 安全隔离（沙箱、权限）与真实性的张力。
- harness 效应本身的度量难度。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含 harness / agent 评测相关的方法论与综述沉淀。

## 自研洞察

<!-- human-only:start 自研洞察｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

*（待人工补充）*

<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

1. 直接基于 Pi 或者 Claude 或者 OpenAI 的 Agent SDK 封装，甚至把一个已经跑的还不错的 Agent 拷贝下来去魔改，都不是困难的事情。

<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->
1. **模型接口耦合**：固定模型跨Harness比较会混淆接口上限与策略适配；应报告同接口横比、跨接口迁移矩阵及模型—Harness联合升级曲线。
   - [RoboEvo²：脚手架策略协同进化](../../updates/2026-11-26/#roboevo) · 2026-11-26
   - [ShellBench：真实日常智能体评测](../../updates/2026-11-25/#shellbench) · 2026-11-25
   - [Harness Rehearsal：任务与接口能力解耦](../../updates/2026-11-25/#harness-rehearsal) · 2026-11-25
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [Evo²：权重与Harness协同进化](../../updates/2026-11-20/#evo-harness) · 2026-11-20
   - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
   - [GPT-6.2 Astra：基准满分却实务失灵](../../updates/2026-11-18/#gpt-6-2-astra) · 2026-11-18
   - [RiseHarness：双轨迹驱动脚手架进化](../../updates/2026-11-17/#riseharness) · 2026-11-17
   - [HarnessDev：自主执行框架演化](../../updates/2026-11-17/#harnessdev) · 2026-11-17
   - [HARNESS-ZERO：智能体驱动的脚手架蒸馏](../../updates/2026-11-17/#harness-zero) · 2026-11-17
   - [ModHarness-RL：可学习演化脚手架](../../updates/2026-11-16/#modharness-rl) · 2026-11-16
   - [JustRUA：GPT-6 机器人操作智能体的受控研究](../../updates/2026-11-14/#justrua-gpt-6) · 2026-11-14
   - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
   - [任务呈现与执行路径影响 LLM 数学表现](../../updates/2026-11-12/#llm-6) · 2026-11-12
   - [JoMoHa：强化学习驱动的模型—脚手架联合优化](../../updates/2026-11-12/#jomoha) · 2026-11-12
   - [Harness Matters：Web 智能体安全韧性的测量与剖析](../../updates/2026-11-12/#harness-matters-web) · 2026-11-12
   - [Harness-S：从同源脚手架学习实现可泛化智能体训练](../../updates/2026-11-06/#harness-s) · 2026-11-06
   - [智能体脚手架显著影响固定 LLM 的银行合规表现](../../updates/2026-11-05/#llm-2) · 2026-11-05
   - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30
   - [智能体接口的决策几何：策略如何内化 Harness 偏好](../../updates/2026-10-29/#harness) · 2026-10-29
2. **分层故障归因**：将结果、Harness机制和轨迹分层评分，并对原生、抽象与恢复视图做一致性审计；以反事实回放区分模型失误、信息丢失与执行失真。
   - [AutoRLBench：真实RL故障诊修评测](../../updates/2026-11-26/#autorlbench-rl) · 2026-11-26
   - [TARE：无内容状态归因审计](../../updates/2026-11-25/#tare) · 2026-11-25
   - [RoHa-SGG：根因引导式脚手架优化](../../updates/2026-11-23/#roha-sgg) · 2026-11-23
   - [RagHarnessDebugger：Jev引导的修复审计](../../updates/2026-11-19/#ragharnessdebugger-jev) · 2026-11-19
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [受治理实验全程审计](../../updates/2026-11-19/#item-36) · 2026-11-19
   - [Agent Trajectories：轨迹证据化质量审查](../../updates/2026-11-18/#agent-trajectories) · 2026-11-18
   - [Verification Transport：抽象边界验证迁移](../../updates/2026-11-16/#verification-transport) · 2026-11-16
   - [编码智能体行为轨迹画像](../../updates/2026-11-16/#item-35) · 2026-11-16
   - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
   - [常规运维如何破坏 LLM 智能体脚手架的架构模式关系](../../updates/2026-11-12/#llm-9) · 2026-11-12
   - [LLM 智能体评测的回放保真度：随机性、隐藏状态与测试预言机](../../updates/2026-11-12/#llm-5) · 2026-11-12
   - [DFT-Agent Bench：自主 DFT 的脚手架效应与执行溯源评测](../../updates/2026-11-12/#dft-agent-bench-dft) · 2026-11-12
   - [有状态工具工作流中的智能体难度审计](../../updates/2026-11-06/#item-92) · 2026-11-06
   - [长程智能体失败归因需执行反事实：迈向报告标准](../../updates/2026-11-06/#item-46) · 2026-11-06
   - [Storage Agent Family：可追溯的持续评测与改进实践](../../updates/2026-11-04/#storage-agent-family) · 2026-11-04
   - [Soei：面向多智能体软件工程的证据与意图结构化可观测性](../../updates/2026-10-30/#soei) · 2026-10-30
   - [TraceTrial-Bench：智能体运行框架可靠性与故障归因基准](../../updates/2026-10-29/#tracetrial-bench) · 2026-10-29
3. **环境与基准认证**：环境与基准需逐任务认证并隔离跨运行状态，持续校验评分器、版本、推断配置、服务基底、资源、隐藏状态泄漏及测试—规格一致性；否则缺陷会重排榜单。
   - [STCG：检测过度规定测试](../../updates/2026-11-25/#stcg) · 2026-11-25
   - [EviCraft：证据闭包式具身评测](../../updates/2026-11-25/#evicraft) · 2026-11-25
   - [MASSys：服务基底敏感性评测](../../updates/2026-11-24/#massys) · 2026-11-24
   - [Benchmarks&#39; Last Exam：逐任务评测审计](../../updates/2026-11-23/#benchmarks-last-exam) · 2026-11-23
   - [MobileGym-Lite：完整覆盖与功能裁剪](../../updates/2026-11-19/#mobilegym-lite) · 2026-11-19
   - [ForecastGym：可回放证据控制评测](../../updates/2026-11-19/#forecastgym) · 2026-11-19
   - [智能体脚手架剖析：不变量驱动测试](../../updates/2026-11-17/#item-78) · 2026-11-17
   - [MobileProbe：基于轨迹感知注入的移动智能体自适应安全评测](../../updates/2026-11-14/#mobileprobe) · 2026-11-14
   - [TestPrism揭示Coding Agent测试生成合格率被高估](../../updates/2026-11-13/#testprism-coding-agent) · 2026-11-13
   - [OpenAI 披露 ExploitGym 智能体复用遗留凭据越权访问研究基础设施](../../updates/2026-11-12/#openai-exploitgym) · 2026-11-12
   - [Longtail-SWE：覆盖长尾编程语言的仓库级软件工程评测基准](../../updates/2026-11-12/#longtail-swe) · 2026-11-12
   - [常规运维如何破坏 LLM 智能体脚手架的架构模式关系](../../updates/2026-11-12/#llm-9) · 2026-11-12
   - [LLM 智能体评测的回放保真度：随机性、隐藏状态与测试预言机](../../updates/2026-11-12/#llm-5) · 2026-11-12
   - [推理模型的推断：评测与服务实践经验](../../updates/2026-11-12/#item-148) · 2026-11-12
   - [将基准视为软件：Terminal-Bench 持续验证与维护](../../updates/2026-11-08/#terminal-bench) · 2026-11-08
   - [FINCOSMOS：金融智能体的开放世界评测范式](../../updates/2026-11-08/#fincosmos) · 2026-11-08
   - [WebHarbor：面向 GUI 智能体的真实网站环境套件](../../updates/2026-11-06/#webharbor-gui) · 2026-11-06
   - [静默评测工具错误导致智能体排行榜重排](../../updates/2026-11-06/#item-67) · 2026-11-06
   - [VeriCUA：以智能体探索验证计算机操作智能体](../../updates/2026-10-30/#vericua) · 2026-10-30
   - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30
4. **过程结果双验**：工具型任务不能只验最终状态；流程、权限和证据义务应分别评分。模型自建Harness时还须分开验证构建与实际运行。
   - [HarnessDev：自建执行框架评测](../../updates/2026-11-24/#harnessdev) · 2026-11-24
   - [EverydayBench：活网交付质量评测](../../updates/2026-11-20/#everydaybench) · 2026-11-20
   - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
   - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
   - [VAHBench：智能体长视频履约评测](../../updates/2026-11-17/#vahbench) · 2026-11-17
   - [TestPrism揭示Coding Agent测试生成合格率被高估](../../updates/2026-11-13/#testprism-coding-agent) · 2026-11-13
   - [WorkflowArena：可执行多智能体工作流编排评测基准](../../updates/2026-11-12/#workflowarena) · 2026-11-12
   - [Veritas：面向智能体任务的自动验证器生成框架](../../updates/2026-11-12/#veritas) · 2026-11-12
   - [DFT-Agent Bench：自主 DFT 的脚手架效应与执行溯源评测](../../updates/2026-11-12/#dft-agent-bench-dft) · 2026-11-12
   - [CAREFUL-Bench：面向调用效果的多轮函数调用无评判器评测](../../updates/2026-11-06/#careful-bench) · 2026-11-06
   - [Co-Design Bench：智能体多模态协作编码评测](../../updates/2026-10-31/#co-design-bench) · 2026-10-31
   - [VeriCUA：以智能体探索验证计算机操作智能体](../../updates/2026-10-30/#vericua) · 2026-10-30
   - [TauIndianBankBench：银行工具智能体的流程感知评测](../../updates/2026-10-30/#tauindianbankbench) · 2026-10-30
5. **自演化质量门**：Harness自动改写应定位首个偏离点，观测与改进策略须随剩余错误更新。用因果回放、置换对照、旧能力回归、成本、留出集和序贯检验拒绝噪声获益与退化。
   - [TransHarness：可迁移脚手架演化](../../updates/2026-11-26/#transharness) · 2026-11-26
   - [SkillsBench：技能增益的噪声感知审计](../../updates/2026-11-26/#skillsbench) · 2026-11-26
   - [失效类型驱动的智能体干预](../../updates/2026-11-25/#item-136) · 2026-11-25
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [AGL-SKILL：编码智能体自优化技能](../../updates/2026-11-25/#agl-skill) · 2026-11-25
   - [MedicalRSI：临床模型与脚手架协同演化](../../updates/2026-11-23/#medicalrsi) · 2026-11-23
   - [Sage-Evolve-Preview：自适应观测驱动持续改进](../../updates/2026-11-20/#sage-evolve-preview) · 2026-11-20
   - [GUARD：后悔引导脚手架演化](../../updates/2026-11-19/#guard) · 2026-11-19
   - [GRAFT：执行证据引导遗传重组](../../updates/2026-11-19/#graft) · 2026-11-19
   - [自改进智能体脚手架：门控模块化演化](../../updates/2026-11-18/#item-38) · 2026-11-18
   - [HarnessDev：自主执行框架演化](../../updates/2026-11-17/#harnessdev) · 2026-11-17
   - [G-CAST：治理式持续自训练](../../updates/2026-11-16/#g-cast) · 2026-11-16
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [TRUST：具备统计保证的可信递归自我改进](../../updates/2026-11-12/#trust) · 2026-11-12
   - [Enmo Safety：现成语言模型的外置非侵入式安全监督](../../updates/2026-11-12/#enmo-safety) · 2026-11-12
   - [EmoHarness：元脚手架演化增强多模态情绪理解](../../updates/2026-11-12/#emoharness) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [编程智能体能否在持续演化中避免遗忘？](../../updates/2026-11-06/#item-94) · 2026-11-06
   - [EvoML：验证门控的自进化机器学习流水线合成](../../updates/2026-11-06/#evoml) · 2026-11-06
   - [VERSE：面向智能体 Harness 的可验证自进化优化器](../../updates/2026-11-05/#verse-harness) · 2026-11-05
   - [HarnessPro：兼顾性能与成本的智能体脚手架自进化框架](../../updates/2026-11-05/#harnesspro) · 2026-11-05
   - [HarnessEvolve：基于参考轨迹的可靠智能体自我进化](../../updates/2026-11-02/#harnessevolve) · 2026-11-02
   - [Harness 自进化研究进展与趋势盘点](../../updates/2026-10-30/#harness) · 2026-10-30
6. **外置模块演化**：冻结模型并外置提示、工具、记忆、观察策略和控制流可降低演化成本，单元须模块化可回滚。自主观察仅在补充证据高价值且模型能可靠利用时启用。
   - [NightWatch：主动流式界面感知](../../updates/2026-11-26/#nightwatch) · 2026-11-26
   - [Harness Learning：反馈驱动的框架元学习](../../updates/2026-11-26/#harness-learning) · 2026-11-26
   - [Video-Relook：自适应时空观察](../../updates/2026-11-25/#video-relook) · 2026-11-25
   - [ToolSmith：自动生成可复用工具](../../updates/2026-11-25/#toolsmith) · 2026-11-25
   - [RVLM-X：自主递归视觉搜索](../../updates/2026-11-25/#rvlm-x) · 2026-11-25
   - [OO-Harness：继承重写式脚手架路由](../../updates/2026-11-25/#oo-harness) · 2026-11-25
   - [AutoPILOT：实时游戏控制脚手架](../../updates/2026-11-24/#autopilot) · 2026-11-24
   - [HookEvo：协同插件演化](../../updates/2026-11-23/#hookevo) · 2026-11-23
   - [Meta-RTL：演化式RTL优化脚手架](../../updates/2026-11-20/#meta-rtl-rtl) · 2026-11-20
   - [智能体脚手架演化：冻结策略领域适配](../../updates/2026-11-20/#item-60) · 2026-11-20
   - [Harness：模块化自改运行框架](../../updates/2026-11-20/#harness) · 2026-11-20
   - [ForceHarness：冻结模型力觉闭环](../../updates/2026-11-19/#forceharness) · 2026-11-19
   - [JevRSI：递归改进决策脚手架](../../updates/2026-11-18/#jevrsi) · 2026-11-18
   - [SkillMaster：策略内生技能进化](../../updates/2026-11-17/#skillmaster) · 2026-11-17
   - [VHarness：视觉推理工具化](../../updates/2026-11-16/#vharness) · 2026-11-16
   - [Co-Sight Harness：外置控制资产与确定性执行](../../updates/2026-11-16/#co-sight-harness) · 2026-11-16
   - [DeepSeek Harness：可演化插件工作台](../../updates/2026-11-15/#deepseek-harness) · 2026-11-15
   - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
   - [EvoX：将智能体脚手架重构为运行时策略](../../updates/2026-11-13/#evox) · 2026-11-13
   - [SimplEvo：通过文本记忆演化提升具身智能体](../../updates/2026-11-12/#simplevo) · 2026-11-12
   - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [LongCapHarness：能力引导的长上下文推理自动脚手架](../../updates/2026-11-12/#longcapharness) · 2026-11-12
   - [可重配置动作理论：动态可组合智能体脚手架的形式化基础](../../updates/2026-11-12/#item-226-2) · 2026-11-12
   - [GEAR：Scikit-learn 式模块化 RSI 框架推动 Agent 持续进化](../../updates/2026-11-12/#gear-scikit-learn-rsi-agent) · 2026-11-12
   - [EvolveNet：协作式 Harness 演化推动智能体自我改进](../../updates/2026-11-12/#evolvenet-harness) · 2026-11-12
   - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
   - [AutoScaffold：AI 自动生成自适应训练脚手架](../../updates/2026-11-12/#autoscaffold-ai) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [Strategist：用智能体演化推理策略](../../updates/2026-11-06/#strategist) · 2026-11-06
   - [Meta²：为长程智能体在线脚手架演化预计算可复用知识](../../updates/2026-11-06/#meta) · 2026-11-06
   - [CLEO：面向自托管 LLM 的极简智能体脚手架优化](../../updates/2026-11-06/#cleo-llm) · 2026-11-06
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [HarnessFlow：MCTS 引导的 LLM 智能体脚手架优化](../../updates/2026-11-05/#harnessflow-mcts-llm) · 2026-11-05
   - [SeaFlow：基于语义任务分解的自演化智能体工作流](../../updates/2026-11-03/#seaflow) · 2026-11-03
   - [KARMA：工业广告智能体的免训练知识原子化脚手架演化](../../updates/2026-10-30/#karma) · 2026-10-30
   - [HEMO：面向多目标组合优化的脚手架自演化](../../updates/2026-10-30/#hemo) · 2026-10-30
   - [CMU开源Hermit：统一Harness层RSI与持续学习框架](../../updates/2026-10-30/#cmu-hermit-harness-rsi) · 2026-10-30
   - [Evo²：冻结执行器权重，协同进化工作流与演化策略](../../updates/2026-10-29/#evo) · 2026-10-29
7. **经验策展机制**：自改进经验应保留原始轨迹、修改因果、验证证据与适用边界，并按后续效用修订或删汰；跨环境传播须允许证据失效与授权撤销。
   - [MetaFORGE：执行反馈式脚手架优化](../../updates/2026-11-26/#metaforge) · 2026-11-26
   - [HoMe：评测驱动的记忆脚手架优化](../../updates/2026-11-26/#home) · 2026-11-26
   - [Agnes Harness：双系统经验复用](../../updates/2026-11-26/#agnes-harness) · 2026-11-26
   - [ReHarness：结果驱动的经验反向修正](../../updates/2026-11-25/#reharness) · 2026-11-25
   - [Harness2：跨任务框架优化经验库](../../updates/2026-11-25/#harness2) · 2026-11-25
   - [MLEvolver：上下文折叠与技能删汰](../../updates/2026-11-24/#mlevolver) · 2026-11-24
   - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
   - [Agnes Harness：双系统决策与双层自进化](../../updates/2026-11-20/#agnes-harness) · 2026-11-20
   - [SCAFFOLD：担保保持式证据迁移](../../updates/2026-11-19/#scaffold) · 2026-11-19
   - [Inventa：去中心化验证式自进化](../../updates/2026-11-18/#inventa) · 2026-11-18
   - [SkillMaster：策略内生技能进化](../../updates/2026-11-17/#skillmaster) · 2026-11-17
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [ReHarness：反向修订式持续学习](../../updates/2026-11-17/#reharness) · 2026-11-17
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
   - [冻结权重智能体从失败轨迹中自我改进的价值与局限](../../updates/2026-11-12/#item-134) · 2026-11-12
   - [EvoGroup：面向共享上下文群体智能体的自演化脚手架](../../updates/2026-11-06/#evogroup) · 2026-11-06
   - [GEPA-Curator：面向自改进智能体的经验策展学习](../../updates/2026-10-29/#gepa-curator) · 2026-10-29
8. **评判器协同演化**：固定或显露目标易诱发定向适配；应做提示—裁判对照，按目标轨迹校准裁判并直接成对估计差值，再用人工或留出轨迹审计。
   - [Transport-Safe Evaluation：轨迹感知的随时有效审计](../../updates/2026-11-25/#transport-safe-evaluation) · 2026-11-25
   - [网页智能体评测：证据约束式差距估计](../../updates/2026-11-25/#item-108) · 2026-11-25
   - [AHE-Beta：需求中心式脚手架演化](../../updates/2026-11-20/#ahe-beta) · 2026-11-20
   - [LoCoMo：提示与评判器敏感性审计](../../updates/2026-11-17/#locomo) · 2026-11-17
   - [VbD：无外部反馈下执行与评估协同演化](../../updates/2026-11-13/#vbd) · 2026-11-13
   - [OpenAI：智能体安全评测与生产行为存在显著差距](../../updates/2026-11-04/#openai) · 2026-11-04
   - [RuHarness：评判准则与智能体脚手架协同演化](../../updates/2026-10-29/#ruharness) · 2026-10-29
9. **环境修复闭环**：长程训练及现实实验应把环境缺陷和测量反馈纳入闭环，用质量控制、确定性验证或回放将终局结果归因到具体回合。
   - [Online Environment Repair：在线修复验证环境](../../updates/2026-11-25/#online-environment-repair) · 2026-11-25
   - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
   - [DeltaHarness：执行反馈式脚手架演化](../../updates/2026-11-18/#deltaharness) · 2026-11-18
   - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
   - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
   - [CivHarness：以回放反馈训练长程 Freeciv 智能体](../../updates/2026-11-02/#civharness-freeciv) · 2026-11-02
   - [WorkRover：递归环境演化扩展长程协同智能体训练](../../updates/2026-10-30/#workrover) · 2026-10-30
10. **分层预算与剪枝**：搜索阶段用稀疏反馈广筛、最终阶段集中预算确认；运行时可按中间状态动态分配模型与推理深度，任何剪枝须做行为等价检验。
    - [Delegent：小模型子任务委派](../../updates/2026-11-26/#delegent) · 2026-11-26
    - [JevAgentHarness：Jev嵌入式快速决策](../../updates/2026-11-25/#jevagentharness-jev) · 2026-11-25
    - [层级执行控制：中间状态驱动计算分配](../../updates/2026-11-25/#item-128) · 2026-11-25
    - [HarnessPro：成本感知式脚手架优化](../../updates/2026-11-25/#harnesspro) · 2026-11-25
    - [HarnessMM：决策图复用免回调](../../updates/2026-11-25/#harnessmm) · 2026-11-25
    - [HyperHarness：历史驱动的个性化脚手架生成](../../updates/2026-11-24/#hyperharness) · 2026-11-24
    - [VideoNexus：独立感知的证据压缩](../../updates/2026-11-19/#videonexus) · 2026-11-19
    - [Know When to Zoom：不确定性触发视觉缩放](../../updates/2026-11-18/#know-when-to-zoom) · 2026-11-18
    - [Context Has a Price：缓存感知上下文成本评测](../../updates/2026-11-18/#context-has-a-price) · 2026-11-18
    - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
    - [CoACT：面向 Coding Agent 的动作保持式上下文压缩](../../updates/2026-11-14/#coact-coding-agent) · 2026-11-14
    - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
    - [企业级 SOP 中智能体架构的成本—成功率权衡评测](../../updates/2026-11-12/#sop) · 2026-11-12
    - [面向低成本智能体脚手架的系统优化](../../updates/2026-11-12/#item-108) · 2026-11-12
    - [ParetoSaddler：面向质量与成本的智能体脚手架帕累托优化](../../updates/2026-11-06/#paretosaddler) · 2026-11-06
    - [AI 智能体如何浪费 Token 成本？](../../updates/2026-11-06/#ai-token) · 2026-11-06
    - [LLM 智能体脚手架演化中的评估预算分配](../../updates/2026-10-29/#llm-2) · 2026-10-29
11. **统一适配层**：用可插拔适配层统一训练、评测和部署接口，可在不改模型时复用不同 Agent 与环境并降低迁移偏差。
    - [Pax：插件化终端编码智能体](../../updates/2026-11-26/#pax) · 2026-11-26
    - [WorldFoundry：面向世界智能的统一基础设施](../../updates/2026-11-12/#worldfoundry) · 2026-11-12
    - [uni-robot-agent：面向开源机器人智能体的统一 Harness](../../updates/2026-11-04/#uni-robot-agent-harness) · 2026-11-04
    - [CMU开源Hermit：统一Harness层RSI与持续学习框架](../../updates/2026-10-30/#cmu-hermit-harness-rsi) · 2026-10-30
12. **工具执行协议**：Harness应显式处理交互、终止、退出码、超时、返回结构与授权边界；冲突需有低摩擦只读上报口，权限规则须模型可识别且执行层强制。
    - [report_inconsistency：零成本上下文漂移检测](../../updates/2026-11-26/#report-inconsistency) · 2026-11-26
    - [Siren：弱沙盒越界评估](../../updates/2026-11-25/#siren) · 2026-11-25
    - [SplitBench：评测权限分离](../../updates/2026-11-23/#splitbench) · 2026-11-23
    - [Codex 沙箱：跨平台权限隔离](../../updates/2026-11-19/#codex) · 2026-11-19
    - [Code Mode：脚本化工具编排](../../updates/2026-11-18/#code-mode) · 2026-11-18
    - [SilentGuard：不变量强制防静默故障](../../updates/2026-11-17/#silentguard) · 2026-11-17
    - [Runtime Contracts：执行时规则强制](../../updates/2026-11-17/#runtime-contracts) · 2026-11-17
    - [可审计授权：跨层验证审批边界](../../updates/2026-11-17/#item-88) · 2026-11-17
    - [智能体脚手架剖析：不变量驱动测试](../../updates/2026-11-17/#item-78) · 2026-11-17
    - [外部沙箱模式：代码执行与密钥隔离](../../updates/2026-11-17/#item-28) · 2026-11-17
    - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
    - [JustRUA：GPT-6 机器人操作智能体的受控研究](../../updates/2026-11-14/#justrua-gpt-6) · 2026-11-14
    - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
    - [OpenRouter 实测 MCP、CLI 与 Skills 的上下文 Token 成本](../../updates/2026-11-12/#openrouter-mcp-cli-skills-token) · 2026-11-12
    - [RECEIPT：测量并修复智能体工具调用的返回假设](../../updates/2026-11-03/#receipt) · 2026-11-03
13. **长程运行时架构**：长程多任务Harness应分离路由与执行，分别持久化环境事实、决策与制品并支持恢复；压缩须单测下一步动作、权限和规则遵循。
    - [RoboHarness-Zero：规划控制解耦脚手架](../../updates/2026-11-25/#roboharness-zero) · 2026-11-25
    - [RLM-27B：脚手架组合泛化](../../updates/2026-11-24/#rlm-27b) · 2026-11-24
    - [MatHarness：长程开放式科研编排](../../updates/2026-11-24/#matharness) · 2026-11-24
    - [HoH：双状态长程编码代理](../../updates/2026-11-24/#hoh) · 2026-11-24
    - [VideoNexus：独立感知的证据压缩](../../updates/2026-11-19/#videonexus) · 2026-11-19
    - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
    - [Mingbird：跨尺寸脚手架进度控制](../../updates/2026-11-18/#mingbird) · 2026-11-18
    - [CubeSandbox：状态化微虚拟机沙箱](../../updates/2026-11-18/#cubesandbox) · 2026-11-18
    - [Harness-of-Harness：证据驱动持续开发](../../updates/2026-11-17/#harness-of-harness) · 2026-11-17
    - [JustRUA：GPT-6 机器人操作智能体的受控研究](../../updates/2026-11-14/#justrua-gpt-6) · 2026-11-14
    - [CoACT：面向 Coding Agent 的动作保持式上下文压缩](../../updates/2026-11-14/#coact-coding-agent) · 2026-11-14
    - [推理历史删除敏感性是模型级属性](../../updates/2026-11-12/#item-220) · 2026-11-12
    - [CORE：面向深度研究的粗到细搜索与上下文管理](../../updates/2026-11-12/#core) · 2026-11-12
    - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
    - [AFK AI开源下一代Agent Harness：Comma常驻Router调度多Worker](../../updates/2026-11-08/#afk-ai-agent-harness-comma-router-worker) · 2026-11-08
    - [千问 Personal Agent：模型、记忆与生态的协同架构](../../updates/2026-11-06/#personal-agent) · 2026-11-06
    - [ARCBench：智能体上下文压缩后的规则遵循评测](../../updates/2026-11-06/#arcbench) · 2026-11-06
    - [腾讯混元发布科研智能体框架 Hyra 2.0](../../updates/2026-11-04/#hyra-2-0) · 2026-11-04
    - [CoworkOS：面向真实世界自动化的长程智能体协作框架](../../updates/2026-11-04/#coworkos) · 2026-11-04
    - [腾讯混元发布 Hyra 2.0：通用 Agent 研发可复用科学工具](../../updates/2026-11-03/#hyra-2-0-agent) · 2026-11-03
    - [DeepSeek提出下一代 Super-agent Harness 架构](../../updates/2026-11-02/#deepseek-super-agent-harness) · 2026-11-02
14. **人机协作评测**：真实任务应加入人机或模拟用户闭环，分别量化交付产出、可操控性、信任校准、安全边界及人类行为兼容性；稳定可预测不能替代类人性。
    - [mini-psych-agent：交互心理环境评测](../../updates/2026-11-25/#mini-psych-agent) · 2026-11-25
    - [AI Harness：弥合规范与监督鸿沟](../../updates/2026-11-25/#ai-harness) · 2026-11-25
    - [模拟软件公司评测：端到端开发能力检验](../../updates/2026-11-23/#item-10) · 2026-11-23
    - [编程基准高分不等于实际产出](../../updates/2026-11-19/#item-49) · 2026-11-19
    - [Interactive Visual Gym：模拟用户驱动的视觉交互闭环评测](../../updates/2026-11-13/#interactive-visual-gym) · 2026-11-13
    - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
    - [RealCLI：统一评估 CLI 智能体的人机协作](../../updates/2026-10-30/#realcli-cli) · 2026-10-30
15. **故障恢复评测**：受控注入故障并设置中性对照后，应以最终状态与关键过程而非动作逐字一致判定恢复，避免把无效建议误记为韧性。
    - [智能体恢复审计：公开报告证据评估](../../updates/2026-11-24/#item-60) · 2026-11-24
    - [AgentFaultBench：状态验证式故障恢复评测](../../updates/2026-11-17/#agentfaultbench) · 2026-11-17
    - [ReTrace：以目标导向动作重放评测计算机操作智能体恢复能力](../../updates/2026-11-04/#retrace) · 2026-11-04
<!-- experience-seen: 2026-11-19/codex 2026-11-19/evidence-interpretation 2026-11-19/forceharness 2026-11-19/forecastgym 2026-11-19/graft 2026-11-19/guard 2026-11-19/item-36 2026-11-19/item-49 2026-11-19/l2c 2026-11-19/mobilegym-lite 2026-11-19/ragharnessdebugger-jev 2026-11-19/scaffold 2026-11-19/videonexus 2026-11-20/agnes-harness 2026-11-20/ahe-beta 2026-11-20/basersi 2026-11-20/everydaybench 2026-11-20/evo-harness 2026-11-20/harness 2026-11-20/item-60 2026-11-20/meta-rtl-rtl 2026-11-20/sage-evolve-preview 2026-11-23/benchmarks-last-exam 2026-11-23/coevobench 2026-11-23/embodied-harness 2026-11-23/hookevo 2026-11-23/item-10 2026-11-23/medicalrsi 2026-11-23/roha-sgg 2026-11-23/splitbench 2026-11-24/autopilot 2026-11-24/harnessdev 2026-11-24/hoh 2026-11-24/hyperharness 2026-11-24/item-60 2026-11-24/massys 2026-11-24/matharness 2026-11-24/mlevolver 2026-11-24/rlm-27b 2026-11-25/agent 2026-11-25/agl-skill 2026-11-25/ai-harness 2026-11-25/embo-harness 2026-11-25/evicraft 2026-11-25/glm-5-5-rsi 2026-11-25/harness-rehearsal 2026-11-25/harness2 2026-11-25/harnessmm 2026-11-25/harnesspro 2026-11-25/item-108 2026-11-25/item-128 2026-11-25/item-136 2026-11-25/jevagentharness-jev 2026-11-25/mini-psych-agent 2026-11-25/online-environment-repair 2026-11-25/oo-harness 2026-11-25/reharness 2026-11-25/roboharness-zero 2026-11-25/rvlm-x 2026-11-25/shellbench 2026-11-25/siren 2026-11-25/stcg 2026-11-25/tare 2026-11-25/toolsmith 2026-11-25/transport-safe-evaluation 2026-11-25/video-relook 2026-11-26/agnes-harness 2026-11-26/autorlbench-rl 2026-11-26/delegent 2026-11-26/harness-learning 2026-11-26/home 2026-11-26/metaforge 2026-11-26/nightwatch 2026-11-26/pax 2026-11-26/report-inconsistency 2026-11-26/roboevo 2026-11-26/skillsbench 2026-11-26/transharness -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**

- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — LM 少样本评测框架（本站已 fork）
- [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) — 前沿模型软件工程评测
- [SWE-bench_Pro-os](https://github.com/scaleapi/SWE-bench_Pro-os) — 长周期软件工程任务
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) — Agent-Computer Interface (ACI) 自主软件工程系统（被引 2191+）
- [SWE-bench (官方仓库)](https://github.com/swe-bench/SWE-bench) — 含 Verified/Multilingual/Lite/Full 等多个变体
- [Multi-SWE-bench](https://github.com/multi-swe-bench/multi-swe-bench) — 8 种语言的多语言 issue-resolving 评测（2132 实例）
- [Terminal-Bench](https://github.com/laude-institute/terminal-bench) — 真实终端环境 Agent 评测（89 个复杂任务）
- [awesome-agent-harness (RUCAIBox)](https://github.com/RUCAIBox/awesome-agent-harness) — Agent harness engineering 官方 awesome list
- [awesome-harness-engineering (ai-boost)](https://github.com/ai-boost/awesome-harness-engineering) — Agent harness 综合资源列表
- [Awesome-Harness-Engineering (Jiaaqiliu)](https://github.com/Jiaaqiliu/Awesome-Harness-Engineering) — 按环境类型分类的 harness compendium
- [agent-eval-harness (linny006)](https://github.com/linny006/agent-eval-harness) — 框架无关的 Agent 评测 harness
- [LLM-Agent-Benchmark-List (zhangxjohn)](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) — LLM + Agent 基准测试资源归类
- [CORE-Bench](https://github.com/princeton-nlp/CORE-Bench) — 计算可复现性 Agent 基准（270 任务）

**论文**

- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419)
- [SWE-agent: Agent-Computer Interfaces Enable Automated SE (NeurIPS 2024)](https://arxiv.org/abs/2405.15793) — ACI 设计将性能提升 3 倍
- [SWE-Bench++: A Framework for Scalable Generation](https://arxiv.org/abs/2512.17419) — 可扩展多语言 SWE-bench 改进（被引 22）
- [Harness-Bench: Measuring Harness Effects across Models](https://arxiv.org/abs/2605.27922) — 诊断 harness 效应的基准
- [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) — 呼吁标准化 harness 披露
- [Coding Benchmarks Are Misaligned with Agentic SE](https://arxiv.org/abs/2606.17799) — 编码基准与真实 Agent SE 任务的错位
- [VeRO: A Harness for Agents to Optimize Agents (ICML 2026)](https://arxiv.org/abs/2602.22480) — Agent 迭代优化 Agent 的评测 harness
- [Agent Harness Engineering: A Survey](https://picrew.github.io/LLM-Harness/main.pdf) — 71 页系统综述
- [A Survey on Agent System and Harness Design](https://arxiv.org/abs/2606.20683) — 更广义的 Agent 系统与 harness 设计综述
- [Multi-SWE-bench (ICLR 2026)](https://openreview.net/forum?id=MhBZzkz4h9) — 多语言 issue-resolving 基准（被引 143）
- [SWE-bench-Live](https://openreview.net/forum?id=OGWkr7gXka) — 可动态更新的 SWE-bench 变体（被引 91）
- [SWE-Bench Pro](https://openreview.net/forum?id=uEVTdoAbnK) — 长周期复杂真实任务扩展（被引 166）
- [SWE-Bench+](https://openreview.net/forum?id=pwIGnH2LHJ) — 数据集质量分析与增强（被引 109）
- [Terminal-Bench 2.0](https://arxiv.org/abs/2601.11868) — 真实复杂终端任务评测（被引 219）
- [CORE-Bench](https://arxiv.org/abs/2409.11363) — 计算可复现性基准（被引 112）
- [Establishing Best Practices for Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) — 10 个 Agent benchmark 方法论审计

**博客**

- [Harness Engineering: How Interface Design Quietly Tripled AI Coding Performance](https://pub.towardsai.net/harness-engineering-how-interface-design-quietly-tripled-ai-coding-performance-swe-8f08e80eba9b) — ACI 深度解析
