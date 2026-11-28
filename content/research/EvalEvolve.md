+++
title = 'EvalEvolve'
proposer = '杜晋华'
since = '2026-08-05'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# EvalEvolve

> 研究方向：**进化式评测**——随能力增长持续演化、抗污染的评测基准与方法。

## 研究范畴

进化式评测（evolutionary / dynamic evaluation）针对静态基准易被污染、快速过时的问题，主张让基准与方法随模型能力增长持续演化、抗污染。本方向涵盖：持续更新的 live benchmarks、动态 / 等价变体评测、自动出题（auto-benchmaking）、抗污染机制，以及自进化基准框架。社区关注的核心问题包括：如何持续、低成本地产生高质量新题并标定难度、如何抵抗训练数据污染与基准泄漏、动态评测如何与真实世界能力对齐避免指标漂移，以及多模态 / Agent / 长周期任务的评测有效性。

## 研究挑战

- 题目质量、ground truth 获取与难度一致性。
- 防泄漏与可复现性的张力。
- 评测本身的成本与算力。
- 与快速迭代模型保持同步的运维负担。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测平台，提供准确率 / cell 级准确率 / 一致性 / 推理路径追踪等多维指标，含可视化榜单（clubweb.site）与 4600+ 评测结果 JSONL。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含评测相关的方法论与综述沉淀。

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
1. **评测时动态生成**：题目应在评测时由实时数据、参数化环境或开放提交生成，以外部时间截点冻结信息并保留确定性校验；黑盒污染审计应优先定位高信息令牌，自报知识截止不能防泄漏。
   - [Uncovering the Tells：稀疏令牌黑盒污染审计](../../updates/2026-11-28/#uncovering-the-tells) · 2026-11-28
   - [时序知识图谱预言机：区分药靶预测与记忆](../../updates/2026-11-26/#item-86) · 2026-11-26
   - [TGB节点亲和力：时点泄漏审计](../../updates/2026-11-25/#tgb) · 2026-11-25
   - [STUN-Bench：真未见工具路由评测](../../updates/2026-11-25/#stun-bench) · 2026-11-25
   - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
   - [FutureBench：可再生知识冲突评测](../../updates/2026-11-19/#futurebench) · 2026-11-19
   - [ForecastGym：可回放证据控制评测](../../updates/2026-11-19/#forecastgym) · 2026-11-19
   - [Reading or Remembering：时间污染记忆审计](../../updates/2026-11-18/#reading-or-remembering) · 2026-11-18
   - [Benchleaking：基准污染校正评测](../../updates/2026-11-18/#benchleaking) · 2026-11-18
   - [JFinBench：可持续刷新金融评测](../../updates/2026-11-16/#jfinbench) · 2026-11-16
   - [LiveGeo：持续演化地理世界中的智能体评测](../../updates/2026-11-14/#livegeo) · 2026-11-14
   - [SynthCorp：面向数据智能体的可定制基准生成平台](../../updates/2026-11-13/#synthcorp) · 2026-11-13
   - [HolidayFactory 1.0：工业机器人任务仿真、生成与评测框架](../../updates/2026-11-12/#holidayfactory-1-0) · 2026-11-12
   - [FinDendro：金融回测中的时间自我认知评测](../../updates/2026-11-12/#findendro) · 2026-11-12
   - [FinCutBench：测量大模型金融知识时间边界的持续更新基准](../../updates/2026-11-12/#fincutbench) · 2026-11-12
   - [Scientist World：面向 AI 科学家的可执行研究世界](../../updates/2026-11-08/#scientist-world-ai) · 2026-11-08
   - [FINCOSMOS：金融智能体的开放世界评测范式](../../updates/2026-11-08/#fincosmos) · 2026-11-08
   - [EnergyBench：欧洲电力市场日前预测实时评测基准](../../updates/2026-11-08/#energybench) · 2026-11-08
   - [TSSDA：自主构建时序 Text-to-SQL 基准的智能体](../../updates/2026-11-06/#tssda-text-to-sql) · 2026-11-06
   - [SessionFarmer：从真实 Vibe Coding 会话构建 SWE 评测基准](../../updates/2026-11-06/#sessionfarmer-vibe-coding-swe) · 2026-11-06
   - [Few Shots 开放 Agent 出题与可验证科学挑战](../../updates/2026-10-31/#few-shots-agent) · 2026-10-31
   - [LiveSearch：以可执行验证代码构建金融搜索智能体实时评测基准](../../updates/2026-10-29/#livesearch) · 2026-10-29
   - [Gym-Anything-RT：视觉语言智能体实时交互评测基准](../../updates/2026-10-29/#gym-anything-rt) · 2026-10-29
2. **可执行答案验真**：开放域任务优先采用程序验证器、形式证明或动态证据核查，并分开判定答案、证据与合规；执行一致须用隐藏反事实实例排除巧合。判分秘密置于智能体边界外，并允许规格等价解。
   - [Real2SimLab：真实到仿真统一评测](../../updates/2026-11-27/#real2simlab) · 2026-11-27
   - [Merlin-Bench：交互证明统一评测](../../updates/2026-11-26/#merlin-bench) · 2026-11-26
   - [LingSante MedGuard：多专家医疗安全护栏](../../updates/2026-11-26/#lingsante-medguard) · 2026-11-26
   - [CF Reward：反事实执行防奖励作弊](../../updates/2026-11-26/#cf-reward) · 2026-11-26
   - [Agent-as-a-Verifier：证据证书式通用验证](../../updates/2026-11-26/#agent-as-a-verifier) · 2026-11-26
   - [STCG：检测过度规定测试](../../updates/2026-11-25/#stcg) · 2026-11-25
   - [EviCraft：证据闭包式具身评测](../../updates/2026-11-25/#evicraft) · 2026-11-25
   - [BenchMint：任务与评分联合构建](../../updates/2026-11-25/#benchmint) · 2026-11-25
   - [RDQA：原始证据轨迹核验](../../updates/2026-11-24/#rdqa) · 2026-11-24
   - [SplitBench：评测权限分离](../../updates/2026-11-23/#splitbench) · 2026-11-23
   - [EverydayBench：活网交付质量评测](../../updates/2026-11-20/#everydaybench) · 2026-11-20
   - [Gandalf：量规驱动的环境对齐验证](../../updates/2026-11-19/#gandalf) · 2026-11-19
   - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
   - [Optimistic Verifiers：精确过程预言机审计](../../updates/2026-11-18/#optimistic-verifiers) · 2026-11-18
   - [DetourBench：精确最短动作轨迹评测](../../updates/2026-11-18/#detourbench) · 2026-11-18
   - [Accelerate Bench：应用级程序优化评测](../../updates/2026-11-18/#accelerate-bench) · 2026-11-18
   - [WindPilot：原始证据绑定式仿真验证](../../updates/2026-11-17/#windpilot) · 2026-11-17
   - [VibePrevisBench：四维场景编程评测](../../updates/2026-11-17/#vibeprevisbench) · 2026-11-17
   - [Verification Transport：抽象边界验证迁移](../../updates/2026-11-16/#verification-transport) · 2026-11-16
   - [TestPrism揭示Coding Agent测试生成合格率被高估](../../updates/2026-11-13/#testprism-coding-agent) · 2026-11-13
   - [Veritas：面向智能体任务的自动验证器生成框架](../../updates/2026-11-12/#veritas) · 2026-11-12
   - [MotionGraphicsBench：以程序化验证评估动态图形生成](../../updates/2026-11-12/#motiongraphicsbench) · 2026-11-12
   - [用评估侧部分可观测博弈缓解智能体欺骗](../../updates/2026-11-12/#item-221) · 2026-11-12
   - [不充分历史下的正确答案：智能体记忆评测对照研究](../../updates/2026-11-12/#item-121) · 2026-11-12
   - [FINCOSMOS：金融智能体的开放世界评测范式](../../updates/2026-11-08/#fincosmos) · 2026-11-08
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [GraphRail：搜索智能体的图结构步骤级验证](../../updates/2026-11-06/#graphrail) · 2026-11-06
   - [CLAIMNOV：基于原子主张的科研创意新颖性评估](../../updates/2026-11-06/#claimnov) · 2026-11-06
   - [CAREFUL-Bench：面向调用效果的多轮函数调用无评判器评测](../../updates/2026-11-06/#careful-bench) · 2026-11-06
   - [不可能代码，评分几乎不变：代码评判模型复现实验](../../updates/2026-11-03/#item-39) · 2026-11-03
   - [CONFIRM：可信智能体神经影像科学报告治理框架](../../updates/2026-11-03/#confirm) · 2026-11-03
   - [Few Shots 开放 Agent 出题与可验证科学挑战](../../updates/2026-10-31/#few-shots-agent) · 2026-10-31
   - [VeriCUA：以智能体探索验证计算机操作智能体](../../updates/2026-10-30/#vericua) · 2026-10-30
   - [OpenAI 邀外部专家与 Lean 核查 AI 科学证明](../../updates/2026-10-29/#openai-lean-ai) · 2026-10-29
   - [LiveSearch：以可执行验证代码构建金融搜索智能体实时评测基准](../../updates/2026-10-29/#livesearch) · 2026-10-29
3. **全过程证据审计**：智能体评测不能只看最终成功率或把 CoT 当完整证据；应以只追加账本保存可回放状态、权限、环境与版本。归因时先定位最早关键错误，再用局部证据诊断，避免整轨迹噪声。
   - [RecordRoute：定位引导的故障诊断](../../updates/2026-11-26/#recordroute) · 2026-11-26
   - [AutoRLBench：真实RL故障诊修评测](../../updates/2026-11-26/#autorlbench-rl) · 2026-11-26
   - [WorldLeague：物理能动性统一评测](../../updates/2026-11-25/#worldleague) · 2026-11-25
   - [端点条件化过程增益评估](../../updates/2026-11-25/#item-133) · 2026-11-25
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [BenchMint：任务与评分联合构建](../../updates/2026-11-25/#benchmint) · 2026-11-25
   - [RDQA：原始证据轨迹核验](../../updates/2026-11-24/#rdqa) · 2026-11-24
   - [二维推理：语义图量化推理忠实与效率](../../updates/2026-11-24/#item-67) · 2026-11-24
   - [智能体恢复审计：公开报告证据评估](../../updates/2026-11-24/#item-60) · 2026-11-24
   - [AgentRoboCritic：意图锚定动作级评测](../../updates/2026-11-24/#agentrobocritic) · 2026-11-24
   - [Mind2Act World：心智动作组合诊断](../../updates/2026-11-21/#mind2act-world) · 2026-11-21
   - [预算配对反事实审计](../../updates/2026-11-21/#item-24) · 2026-11-21
   - [受治理实验全程审计](../../updates/2026-11-19/#item-36) · 2026-11-19
   - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
   - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
   - [多智能体记忆不一致：事实冲突流失定位](../../updates/2026-11-18/#item-69) · 2026-11-18
   - [DetourBench：精确最短动作轨迹评测](../../updates/2026-11-18/#detourbench) · 2026-11-18
   - [可审计授权：跨层验证审批边界](../../updates/2026-11-17/#item-88) · 2026-11-17
   - [Instrumenting Failure：逐决策节点评测](../../updates/2026-11-17/#instrumenting-failure) · 2026-11-17
   - [AgentFaultBench：状态验证式故障恢复评测](../../updates/2026-11-17/#agentfaultbench) · 2026-11-17
   - [编码智能体行为轨迹画像](../../updates/2026-11-16/#item-35) · 2026-11-16
   - [世界仍保留错误时，清理智能体历史反而有害](../../updates/2026-11-13/#item-41) · 2026-11-13
   - [OpenAI：模型生命周期因素如何影响 CoT 可监控性](../../updates/2026-11-12/#openai-cot) · 2026-11-12
   - [LLM 智能体评测的回放保真度：随机性、隐藏状态与测试预言机](../../updates/2026-11-12/#llm-5) · 2026-11-12
   - [长程 LLM 智能体的轨迹中心故障审计](../../updates/2026-11-12/#llm) · 2026-11-12
   - [用评估侧部分可观测博弈缓解智能体欺骗](../../updates/2026-11-12/#item-221) · 2026-11-12
   - [Harness Matters：Web 智能体安全韧性的测量与剖析](../../updates/2026-11-12/#harness-matters-web) · 2026-11-12
   - [DFT-Agent Bench：自主 DFT 的脚手架效应与执行溯源评测](../../updates/2026-11-12/#dft-agent-bench-dft) · 2026-11-12
   - [闭环智能体评估：分层测量与自校准](../../updates/2026-11-08/#item-45) · 2026-11-08
   - [有状态工具工作流中的智能体难度审计](../../updates/2026-11-06/#item-92) · 2026-11-06
   - [静默评测工具错误导致智能体排行榜重排](../../updates/2026-11-06/#item-67) · 2026-11-06
   - [长程智能体失败归因需执行反事实：迈向报告标准](../../updates/2026-11-06/#item-46) · 2026-11-06
   - [智能体自写交接摘要何时变成无依据指令？](../../updates/2026-11-06/#item-33) · 2026-11-06
   - [基于闭合序列模式挖掘的网页导航智能体可解释早停](../../updates/2026-11-06/#item-153) · 2026-11-06
   - [CAREFUL-Bench：面向调用效果的多轮函数调用无评判器评测](../../updates/2026-11-06/#careful-bench) · 2026-11-06
   - [ARCBench：智能体上下文压缩后的规则遵循评测](../../updates/2026-11-06/#arcbench) · 2026-11-06
   - [智能体脚手架显著影响固定 LLM 的银行合规表现](../../updates/2026-11-05/#llm-2) · 2026-11-05
   - [Storage Agent Family：可追溯的持续评测与改进实践](../../updates/2026-11-04/#storage-agent-family) · 2026-11-04
   - [TauIndianBankBench：银行工具智能体的流程感知评测](../../updates/2026-10-30/#tauindianbankbench) · 2026-10-30
   - [前缀可执行性：超越最终成功的工具智能体评估](../../updates/2026-10-30/#item-38) · 2026-10-30
   - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30
   - [TraceTrial-Bench：智能体运行框架可靠性与故障归因基准](../../updates/2026-10-29/#tracetrial-bench) · 2026-10-29
4. **难度与覆盖维护**：题集应维护模型无关难度、场景与语言条件、真实行为足迹的缺陷覆盖，并逐单元监测区分度和参考答案上限；跨语言须分别校准迁移与置信度。总分会掩盖短板与混杂。
   - [ProxyGenBench：代理引导视频生成评测](../../updates/2026-11-28/#proxygenbench) · 2026-11-28
   - [Memphis：真实尝试播种仿真评测](../../updates/2026-11-28/#memphis) · 2026-11-28
   - [RoboDojo-Mirror：镜像反射鲁棒性评测](../../updates/2026-11-26/#robodojo-mirror) · 2026-11-26
   - [Lost in Translation：多语言决策校准](../../updates/2026-11-26/#lost-in-translation) · 2026-11-26
   - [IRTIQA：自进化跨语言迁移评测](../../updates/2026-11-26/#irtiqa) · 2026-11-26
   - [GeoDecisions：空间感知与地理偏差评测](../../updates/2026-11-25/#geodecisions) · 2026-11-25
   - [ASTERISM：多图捷径审计与归因](../../updates/2026-11-25/#asterism) · 2026-11-25
   - [PURE：多粒度身份匹配诊断](../../updates/2026-11-24/#pure) · 2026-11-24
   - [Benchmarks' Last Exam：逐任务评测审计](../../updates/2026-11-23/#benchmarks-last-exam) · 2026-11-23
   - [Rigel-Ladon：选项数准确率定律](../../updates/2026-11-20/#rigel-ladon) · 2026-11-20
   - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
   - [Breath-Dx：漂移感知疾病筛查基准](../../updates/2026-11-19/#breath-dx) · 2026-11-19
   - [InclusionMed：包容性医疗评测图谱](../../updates/2026-11-18/#inclusionmed) · 2026-11-18
   - [VAST：可验证漏洞场景编译](../../updates/2026-11-17/#vast) · 2026-11-17
   - [决策模型：带置信度的临床字段抽取](../../updates/2026-11-17/#item-86) · 2026-11-17
   - [Benchmark Factory：无标签质量锚点造基准](../../updates/2026-11-17/#benchmark-factory) · 2026-11-17
   - [生成式评测套件：按单元评分揭示回归](../../updates/2026-11-16/#item-31) · 2026-11-16
   - [智能体基准在任务耗尽前已失去排名能力](../../updates/2026-11-12/#item-81) · 2026-11-12
   - [有状态工具工作流中的智能体难度审计](../../updates/2026-11-06/#item-92) · 2026-11-06
   - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
   - [Epi2Diff：利用LLM推理轨迹量化试题难度](../../updates/2026-11-03/#epi2diff-llm) · 2026-11-03
   - [BHI：为158个大模型评测基准进行健康度评分](../../updates/2026-11-01/#bhi-158) · 2026-11-01
   - [基准测试是难度分布的经验度量](../../updates/2026-10-31/#item-13) · 2026-10-31
5. **长周期任务流**：持续学习应在跨任务依赖流中分测知识更新、能力形成、技能组合、遗忘与迁移；持久状态或单项熟练不等于可复用演化，须检验兼容性、保持性、域外迁移与可撤回性。
   - [软提示技能的组合兼容与保持](../../updates/2026-11-26/#item-39) · 2026-11-26
   - [EvoLink-Bench：长程依赖任务流评测](../../updates/2026-11-26/#evolink-bench) · 2026-11-26
   - [预训练VLA持续学习：分布外遗忘诊断](../../updates/2026-11-25/#vla) · 2026-11-25
   - [RoboLiveMem：动静态配对记忆评测](../../updates/2026-11-25/#robolivemem) · 2026-11-25
   - [保留观测历史应对惯例复现](../../updates/2026-11-25/#item-117) · 2026-11-25
   - [三接口持续学习诊断](../../updates/2026-11-25/#item-109) · 2026-11-25
   - [ReSpaceBench：跨重访空间记忆评测](../../updates/2026-11-24/#respacebench) · 2026-11-24
   - [Memanto：信息论相关性记忆排序](../../updates/2026-11-24/#memanto) · 2026-11-24
   - [Memory Tax：量化记忆重构损耗](../../updates/2026-11-23/#memory-tax) · 2026-11-23
   - [GroupAssistBench：群聊记忆使用评测](../../updates/2026-11-23/#groupassistbench) · 2026-11-23
   - [AstronautBench：三视角自改进评测](../../updates/2026-11-23/#astronautbench) · 2026-11-23
   - [Stability Gap：持续强化学习稳定性缺口](../../updates/2026-11-20/#stability-gap) · 2026-11-20
   - [CompAct-Bench：工作上下文压缩评测](../../updates/2026-11-20/#compact-bench) · 2026-11-20
   - [ChronoDossier：长档案式时序记忆评测](../../updates/2026-11-20/#chronodossier) · 2026-11-20
   - [Remembered as Brief：偏好记忆静默删减](../../updates/2026-11-18/#remembered-as-brief) · 2026-11-18
   - [多智能体记忆不一致：事实冲突流失定位](../../updates/2026-11-18/#item-69) · 2026-11-18
   - [BRIDGE：极简检索记忆](../../updates/2026-11-18/#bridge) · 2026-11-18
   - [StaleBench：隔离陈旧检索并量化修复成本](../../updates/2026-11-17/#stalebench) · 2026-11-17
   - [HEAMS：智能体记忆全责评测](../../updates/2026-11-17/#heams) · 2026-11-17
   - [强化学习后印度语言任务的增益与退化](../../updates/2026-11-14/#item-35) · 2026-11-14
   - [自主智能体自生成更新的证据治理采纳框架 EGE](../../updates/2026-11-14/#ege) · 2026-11-14
   - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
   - [RSI-PDEbench：偏微分方程求解智能体递归自我改进基准](../../updates/2026-11-13/#rsi-pdebench) · 2026-11-13
   - [世界仍保留错误时，清理智能体历史反而有害](../../updates/2026-11-13/#item-41) · 2026-11-13
   - [Third Eye：递归自我改进的长期效用评估](../../updates/2026-11-12/#third-eye) · 2026-11-12
   - [双层对话记忆的压缩、衰减与强化：对比 RAG 的配对评测](../../updates/2026-11-12/#rag) · 2026-11-12
   - [EviCover：诊断长期对话记忆中的证据集丢失](../../updates/2026-11-12/#evicover) · 2026-11-12
   - [Continual-ARC：衡量智能体终身技能习得](../../updates/2026-11-12/#continual-arc) · 2026-11-12
   - [BioMem：生物医学 LLM 智能体记忆评测与 HMRU 框架](../../updates/2026-11-12/#biomem-llm-hmru) · 2026-11-12
   - [记忆陷阱：语言智能体从良性交互中过度泛化](../../updates/2026-11-08/#item-44) · 2026-11-08
   - [ReScopeBench：演化环境中的智能体经验生命周期评测](../../updates/2026-11-06/#rescopebench) · 2026-11-06
   - [MemShift：分离个人记忆的变更检测与修复评测](../../updates/2026-11-06/#memshift) · 2026-11-06
   - [LExMem：探索任务长期记忆的图结构基准与框架](../../updates/2026-11-06/#lexmem) · 2026-11-06
   - [长期智能体记忆的任务条件效用评测](../../updates/2026-11-06/#item-80) · 2026-11-06
   - [智能体记忆的限速过滤：显式状态在长历史中优于长上下文](../../updates/2026-11-06/#item-124) · 2026-11-06
   - [Continual AutoResearch：智能体能否跨任务持续学习](../../updates/2026-11-06/#continual-autoresearch) · 2026-11-06
   - [MemUse：在使用点评估智能体记忆](../../updates/2026-11-03/#memuse) · 2026-11-03
   - [Memory Tax：剖析智能体记忆的净价值](../../updates/2026-10-29/#memory-tax) · 2026-10-29
   - [HABIT-Bench：评估智能体从长期弱证据中归纳用户习惯](../../updates/2026-10-29/#habit-bench) · 2026-10-29
   - [DeepMind：自演化智能体能否持续学习？](../../updates/2026-10-29/#deepmind) · 2026-10-29
   - [CLE：LLM 智能体长时程持续学习与经验学习基准](../../updates/2026-10-29/#cle-llm) · 2026-10-29
6. **交互环境测适应**：静态指令难以覆盖真实适应能力；应在实时交互中引入目标修订、外界扰动和证据冲突，评估恢复与重规划。
   - [EgoUseBench：动态第一人称任务评测](../../updates/2026-11-27/#egousebench) · 2026-11-27
   - [S1Arena-MM：多模态快慢决策评测](../../updates/2026-11-25/#s1arena-mm) · 2026-11-25
   - [智能体恢复审计：公开报告证据评估](../../updates/2026-11-24/#item-60) · 2026-11-24
   - [AutoPILOT：实时游戏控制脚手架](../../updates/2026-11-24/#autopilot) · 2026-11-24
   - [AgriManager：农业策略模式迁移评测](../../updates/2026-11-24/#agrimanager) · 2026-11-24
   - [AgentRoboCritic：意图锚定动作级评测](../../updates/2026-11-24/#agentrobocritic) · 2026-11-24
   - [TuringSpace：交互验证码训练空间行动](../../updates/2026-11-21/#turingspace) · 2026-11-21
   - [RoboBuilder：实机视频闭环机器人共设计](../../updates/2026-11-19/#robobuilder) · 2026-11-19
   - [SciResearch-Eval：科学判断力交互评测](../../updates/2026-11-18/#sciresearch-eval) · 2026-11-18
   - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
   - [AgentFaultBench：状态验证式故障恢复评测](../../updates/2026-11-17/#agentfaultbench) · 2026-11-17
   - [LiveGeo：持续演化地理世界中的智能体评测](../../updates/2026-11-14/#livegeo) · 2026-11-14
   - [Interactive Visual Gym：模拟用户驱动的视觉交互闭环评测](../../updates/2026-11-13/#interactive-visual-gym) · 2026-11-13
   - [GTAGym：面向评估与强化学习的 AAA 游戏任务环境](../../updates/2026-11-13/#gtagym-aaa) · 2026-11-13
   - [HolidayFactory 1.0：工业机器人任务仿真、生成与评测框架](../../updates/2026-11-12/#holidayfactory-1-0) · 2026-11-12
   - [Embodied First Exam：编码智能体具身控制综合评测](../../updates/2026-11-12/#embodied-first-exam) · 2026-11-12
   - [VisSearch-Bench：多模态智能体长时程视觉搜索评测](../../updates/2026-11-08/#vissearch-bench) · 2026-11-08
   - [WebHarbor：面向 GUI 智能体的真实网站环境套件](../../updates/2026-11-06/#webharbor-gui) · 2026-11-06
   - [ReScopeBench：演化环境中的智能体经验生命周期评测](../../updates/2026-11-06/#rescopebench) · 2026-11-06
   - [YANAMI：多轮有状态交互的多模态数据集与基准](../../updates/2026-11-05/#yanami) · 2026-11-05
   - [RoboColosseum：大规模真实场景物理智能评测框架](../../updates/2026-11-05/#robocolosseum) · 2026-11-05
   - [ReTrace：以目标导向动作重放评测计算机操作智能体恢复能力](../../updates/2026-11-04/#retrace) · 2026-11-04
   - [CLASHarness：多智能体冲突场景评测与数据合成框架](../../updates/2026-11-01/#clasharness) · 2026-11-01
   - [DynaRev：动态目标修订下的 Web 智能体评测基准](../../updates/2026-10-30/#dynarev-web) · 2026-10-30
   - [InteractiveWorld：可验证的人本交互式 MLLM 环境](../../updates/2026-10-29/#interactiveworld-mllm) · 2026-10-29
   - [Gym-Anything-RT：视觉语言智能体实时交互评测基准](../../updates/2026-10-29/#gym-anything-rt) · 2026-10-29
7. **裁判稳定性审计**：自动裁判需跨规则、提示、顺序、身份、模型与时间审计，并以人机分歧发现清单外偏差。模型比较应估计目标轨迹上的成对差值，按证据权限和决策影响校准；覆盖不足只报告界。
   - [HUB-J：人类偏好驱动偏差审计](../../updates/2026-11-26/#hub-j) · 2026-11-26
   - [Transport-Safe Evaluation：轨迹感知的随时有效审计](../../updates/2026-11-25/#transport-safe-evaluation) · 2026-11-25
   - [端点条件化过程增益评估](../../updates/2026-11-25/#item-133) · 2026-11-25
   - [暴露度预判奖励作弊](../../updates/2026-11-25/#item-123) · 2026-11-25
   - [网页智能体评测：证据约束式差距估计](../../updates/2026-11-25/#item-108) · 2026-11-25
   - [量表反转探针：审计评判方向偏差](../../updates/2026-11-21/#item-21) · 2026-11-21
   - [盲点迁移：评判偏见类别泛化](../../updates/2026-11-20/#item-65) · 2026-11-20
   - [LoCoMo：提示与评判器敏感性审计](../../updates/2026-11-17/#locomo) · 2026-11-17
   - [研究品味：未来方向选择评测](../../updates/2026-11-17/#item-79) · 2026-11-17
   - [Verification Transport：抽象边界验证迁移](../../updates/2026-11-16/#verification-transport) · 2026-11-16
   - [Laya 类型决策模型置信度再校准实操指南](../../updates/2026-11-14/#laya) · 2026-11-14
   - [Maya a1 非自回归决策模型的选项顺序敏感性](../../updates/2026-11-12/#maya-a1) · 2026-11-12
   - [AutoRefine：基于工作流结果自动校准代码评判器](../../updates/2026-11-12/#autorefine) · 2026-11-12
   - [PromptOps：LLM 评判系统的迭代提示优化](../../updates/2026-11-06/#promptops-llm) · 2026-11-06
   - [JevBreak：固定答案集无法阻止决策操控](../../updates/2026-11-06/#jevbreak) · 2026-11-06
   - [相同输出，不同得分：多模态基准评分器审计](../../updates/2026-11-06/#item-88) · 2026-11-06
   - [更换评判模型会改变系统排名：跨提供商预注册复现研究](../../updates/2026-11-06/#item-74) · 2026-11-06
   - [语言模型迭代创建、评审与修订数据科学项目](../../updates/2026-11-06/#item-146) · 2026-11-06
   - [Agent-as-a-Judge 中的确认偏差：证据落地仍难免疫](../../updates/2026-11-06/#agent-as-a-judge) · 2026-11-06
   - [主观文本评估中类型化决策模型的呈现敏感性](../../updates/2026-11-05/#item-25) · 2026-11-05
   - [RubricWorld：世界模型引导的 LLM 评分规约优化](../../updates/2026-11-03/#rubricworld-llm) · 2026-11-03
   - [不可能代码，评分几乎不变：代码评判模型复现实验](../../updates/2026-11-03/#item-39) · 2026-11-03
   - [Co-Design Bench：智能体多模态协作编码评测](../../updates/2026-10-31/#co-design-bench) · 2026-10-31
   - [决策模型作为幻觉检测评判器](../../updates/2026-10-29/#item-65) · 2026-10-29
   - [Ai2 发布新颖性评判基准，揭示 LLM 裁判高度不稳定](../../updates/2026-10-29/#ai2-llm) · 2026-10-29
8. **搜索确认分配预算**：演化搜索应先估计最小可辨差异，只有超过统计分辨率的增益才解释排序；再以匹配计算的基线、历史峰值和未见任务独立验证，且不向搜索暴露标准。
   - [Vernier：预测榜单分辨率审计](../../updates/2026-11-28/#vernier) · 2026-11-28
   - [RSI 2026：自我进化效果验证](../../updates/2026-11-28/#rsi-2026) · 2026-11-28
   - [SkillsBench：技能增益的噪声感知审计](../../updates/2026-11-26/#skillsbench) · 2026-11-26
   - [SealedLoop：环外密封评判](../../updates/2026-11-26/#sealedloop) · 2026-11-26
   - [Tea Leaves：早期曲线预测训练走势](../../updates/2026-11-25/#tea-leaves) · 2026-11-25
   - [RecurSciBench：科学RSI迁移评测](../../updates/2026-11-25/#recurscibench-rsi) · 2026-11-25
   - [Schedule, Rank, Profile：游戏智能体持续评测](../../updates/2026-11-24/#schedule-rank-profile) · 2026-11-24
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [Sage-Evolve-Preview：自适应观测驱动持续改进](../../updates/2026-11-20/#sage-evolve-preview) · 2026-11-20
   - [Resolution Hypothesis：评测分辨率瓶颈](../../updates/2026-11-19/#resolution-hypothesis) · 2026-11-19
   - [DCPS：示例条件式提示搜索](../../updates/2026-11-18/#dcps) · 2026-11-18
   - [HarnessDev：自主执行框架演化](../../updates/2026-11-17/#harnessdev) · 2026-11-17
   - [CRITFAULT：评论器安全审计](../../updates/2026-11-17/#critfault) · 2026-11-17
   - [多智能体评测：资源匹配式效果审计](../../updates/2026-11-16/#item-33) · 2026-11-16
   - [AI4AI：三决策研究控制框架](../../updates/2026-11-15/#ai4ai) · 2026-11-15
   - [自主智能体自生成更新的证据治理采纳框架 EGE](../../updates/2026-11-14/#ege) · 2026-11-14
   - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [Third Eye：递归自我改进的长期效用评估](../../updates/2026-11-12/#third-eye) · 2026-11-12
   - [前沿编程 LLM 是在编码还是作弊？](../../updates/2026-11-12/#llm-7) · 2026-11-12
   - [Flex-RSI：前沿智能体递归自我改进评测基准](../../updates/2026-11-12/#flex-rsi) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
   - [SelfImprove-Bench：自改进智能体泛化能力评测](../../updates/2026-11-06/#selfimprove-bench) · 2026-11-06
   - [验证器更强不等于发现质量更高：提议池构成才是关键](../../updates/2026-11-06/#item-66) · 2026-11-06
   - [RSI 系统优化 Agent 的 Reward Hacking 与验证边界](../../updates/2026-11-04/#rsi-agent-reward-hacking) · 2026-11-04
   - [LLM 智能体脚手架演化中的评估预算分配](../../updates/2026-10-29/#llm-2) · 2026-10-29
   - [BiPA：用二部归因重新评估智能体技能优化](../../updates/2026-10-29/#bipa) · 2026-10-29
9. **准则脚手架共演**：脚手架迭代应先从轨迹中归纳残余失败，再以自主—引导执行差距区分技能缺失与调用失败，匹配技能、预算或反馈；否则扩模或加轮次难有稳定增益。
   - [置信度注入揭示自监控失效](../../updates/2026-11-28/#item-28) · 2026-11-28
   - [MedSkill-E²：医疗技能评测与演化](../../updates/2026-11-26/#medskill-e) · 2026-11-26
   - [LCE：失败模式多样性诊断](../../updates/2026-11-25/#lce) · 2026-11-25
   - [失效类型驱动的智能体干预](../../updates/2026-11-25/#item-136) · 2026-11-25
   - [CUA-SEE：任务验证器协同演化](../../updates/2026-11-25/#cua-see) · 2026-11-25
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [EVA-RSI：代理考试驱动视频评估自改进](../../updates/2026-11-19/#eva-rsi) · 2026-11-19
   - [临床AI评估即干预](../../updates/2026-11-16/#item-18) · 2026-11-16
   - [VbD：无外部反馈下执行与评估协同演化](../../updates/2026-11-13/#vbd) · 2026-11-13
   - [AutoRefine：基于工作流结果自动校准代码评判器](../../updates/2026-11-12/#autorefine) · 2026-11-12
   - [RuHarness：评判准则与智能体脚手架协同演化](../../updates/2026-10-29/#ruharness) · 2026-10-29
10. **多预算能力曲线**：模型与架构排序会随任务时长、采样、服务基底和预算改变；应报告能力—成本曲线与多档 pass@k。扩大候选池会放大验证器噪声，须用配对重复运行检查净收益与稳定性。
    - [MedSkill-E²：医疗技能评测与演化](../../updates/2026-11-26/#medskill-e) · 2026-11-26
    - [CF Reward：反事实执行防奖励作弊](../../updates/2026-11-26/#cf-reward) · 2026-11-26
    - [Best-of-N Steering：验证误差放大奖励作弊](../../updates/2026-11-26/#best-of-n-steering) · 2026-11-26
    - [ShellBench：真实日常智能体评测](../../updates/2026-11-25/#shellbench) · 2026-11-25
    - [S1Arena-MM：多模态快慢决策评测](../../updates/2026-11-25/#s1arena-mm) · 2026-11-25
    - [Prefill1：固定前缀单词元判决](../../updates/2026-11-25/#prefill1) · 2026-11-25
    - [失效类型驱动的智能体干预](../../updates/2026-11-25/#item-136) · 2026-11-25
    - [Gemini 4 Neon：低成本高分推理](../../updates/2026-11-25/#gemini-4-neon) · 2026-11-25
    - [MASSys：服务基底敏感性评测](../../updates/2026-11-24/#massys) · 2026-11-24
    - [AutoPILOT：实时游戏控制脚手架](../../updates/2026-11-24/#autopilot) · 2026-11-24
    - [Gemini 4 Hydrogen：半量Token高分推理](../../updates/2026-11-21/#gemini-4-hydrogen-token) · 2026-11-21
    - [决策模型：低成本联络中心判别](../../updates/2026-11-19/#item-53) · 2026-11-19
    - [FLCVA：全账本反事实推理审计](../../updates/2026-11-19/#flcva) · 2026-11-19
    - [Done, But Still Working：编程智能体早停评测](../../updates/2026-11-19/#done-but-still-working) · 2026-11-19
    - [Train After You Measure：预注册个性化微调曲线](../../updates/2026-11-18/#train-after-you-measure) · 2026-11-18
    - [SkillBuffBench：多因素技能贡献评测](../../updates/2026-11-18/#skillbuffbench) · 2026-11-18
    - [SciResearch-Eval：科学判断力交互评测](../../updates/2026-11-18/#sciresearch-eval) · 2026-11-18
    - [Mingbird：跨尺寸脚手架进度控制](../../updates/2026-11-18/#mingbird) · 2026-11-18
    - [Know When to Zoom：不确定性触发视觉缩放](../../updates/2026-11-18/#know-when-to-zoom) · 2026-11-18
    - [DCPS：示例条件式提示搜索](../../updates/2026-11-18/#dcps) · 2026-11-18
    - [One Run Is Not Enough：配对校准记忆增益](../../updates/2026-11-17/#one-run-is-not-enough) · 2026-11-17
    - [多智能体评测：资源匹配式效果审计](../../updates/2026-11-16/#item-33) · 2026-11-16
    - [量化比较的噪声下限：引擎、重启、批处理与内核漂移](../../updates/2026-11-14/#item-60) · 2026-11-14
    - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
    - [VIALS-AA评测：Claude以高频工具调用领先科研图表视觉推理](../../updates/2026-11-12/#vials-aa-claude) · 2026-11-12
    - [企业级 SOP 中智能体架构的成本—成功率权衡评测](../../updates/2026-11-12/#sop) · 2026-11-12
    - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
    - [推理模型的推断：评测与服务实践经验](../../updates/2026-11-12/#item-148) · 2026-11-12
    - [Infrathon：真实世界长程 AI 基础设施优化智能体基准](../../updates/2026-11-12/#infrathon-ai) · 2026-11-12
    - [GRPO 中稠密奖励值得其 Token 成本吗？](../../updates/2026-11-12/#grpo-token) · 2026-11-12
    - [Anthropic 发布 MAMUBench：多智能体协作失灵评测](../../updates/2026-11-12/#anthropic-mamubench) · 2026-11-12
    - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
    - [BestRand：稳定低成本的基准压缩](../../updates/2026-11-08/#bestrand) · 2026-11-08
    - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
    - [基于闭合序列模式挖掘的网页导航智能体可解释早停](../../updates/2026-11-06/#item-153) · 2026-11-06
    - [AI 智能体如何浪费 Token 成本？](../../updates/2026-11-06/#ai-token) · 2026-11-06
    - [RLVR 无免费午餐：pass@1 提升必付出 pass@k 代价](../../updates/2026-10-30/#rlvr-pass-1-pass-k) · 2026-10-30
    - [指令容量：受控负载下语言模型的行为与退化](../../updates/2026-10-30/#item-15) · 2026-10-30
11. **科研流程实证化**：科研智能体应分测创意、方向选择、探索覆盖、知识链深度、实验设计、审稿与执行，并以公认指标、可复现实验、原始证据复算或形式证明计分。
    - [DRBench Pro：知识树驱动的深研评测](../../updates/2026-11-28/#drbench-pro) · 2026-11-28
    - [REE：开放科研能力评测](../../updates/2026-11-26/#ree) · 2026-11-26
    - [RecurSciBench：科学RSI迁移评测](../../updates/2026-11-25/#recurscibench-rsi) · 2026-11-25
    - [Beyond Accuracy：实验规划诊断评测](../../updates/2026-11-25/#beyond-accuracy) · 2026-11-25
    - [非对称角色与信念差控制](../../updates/2026-11-23/#item-23) · 2026-11-23
    - [TwinLab-Bench：真实实验室孪生评测](../../updates/2026-11-20/#twinlab-bench) · 2026-11-20
    - [Openhagen Worlds：校准式科学发现环境](../../updates/2026-11-20/#openhagen-worlds) · 2026-11-20
    - [STEMBench：领域指标锚定科研评测](../../updates/2026-11-19/#stembench) · 2026-11-19
    - [SciWorkBench：真实科研工作流评测](../../updates/2026-11-18/#sciworkbench) · 2026-11-18
    - [SciResearch-Eval：科学判断力交互评测](../../updates/2026-11-18/#sciresearch-eval) · 2026-11-18
    - [WindPilot：原始证据绑定式仿真验证](../../updates/2026-11-17/#windpilot) · 2026-11-17
    - [研究品味：未来方向选择评测](../../updates/2026-11-17/#item-79) · 2026-11-17
    - [未测空隙优先的科学发现](../../updates/2026-11-17/#item-52) · 2026-11-17
    - [PaperCritic：F1奖励式论文健全性评审](../../updates/2026-11-16/#papercritic-f1) · 2026-11-16
    - [MineralExp：分类化实验设计评测](../../updates/2026-11-16/#mineralexp) · 2026-11-16
    - [SPU：隐藏实测结果的湿实验预测](../../updates/2026-11-15/#spu) · 2026-11-15
    - [AI4AI：三决策研究控制框架](../../updates/2026-11-15/#ai4ai) · 2026-11-15
    - [NIBench：神经影像智能体执行、技能演化与科学判断基准](../../updates/2026-11-14/#nibench) · 2026-11-14
    - [审计 AI 同行评审：基于真实科学论文的评测基准](../../updates/2026-11-14/#item-52) · 2026-11-14
    - [QSim-Arena：演化式量子模拟优势研究框架](../../updates/2026-11-13/#qsim-arena) · 2026-11-13
    - [Re-Search：以双人问答博弈剖析 LLM 科研创意搜索](../../updates/2026-11-12/#re-search-llm) · 2026-11-12
    - [AI 同行评审能力评测：百项植入错误基准](../../updates/2026-11-12/#item-99) · 2026-11-12
    - [面向 AI 研究成果的人工在环验证、审计与归因框架](../../updates/2026-11-12/#item-227) · 2026-11-12
    - [将科学论文转化为空间转录组智能体审计基准](../../updates/2026-11-12/#item-122) · 2026-11-12
    - [ARE-bench：真实研究会话与工作空间中的智能体科研能力评测](../../updates/2026-11-12/#are-bench) · 2026-11-12
    - [AISLE：全球首个真实湿实验 AI Scientist 评测基准](../../updates/2026-11-12/#aisle-ai-scientist) · 2026-11-12
    - [Scientist World：面向 AI 科学家的可执行研究世界](../../updates/2026-11-08/#scientist-world-ai) · 2026-11-08
    - [OmniQ与Residual Agents重塑计算量子科研智能体](../../updates/2026-11-06/#omniq-residual-agents) · 2026-11-06
    - [科学智能体为何能治表却无法识因](../../updates/2026-11-06/#item-65) · 2026-11-06
    - [FrontierPhysics：端到端物理研究智能体评测基准](../../updates/2026-11-06/#frontierphysics) · 2026-11-06
    - [CONFIRM：可信智能体神经影像科学报告治理框架](../../updates/2026-11-03/#confirm) · 2026-11-03
    - [Few Shots 开放 Agent 出题与可验证科学挑战](../../updates/2026-10-31/#few-shots-agent) · 2026-10-31
    - [rTaste：科研智能体是否具有研究品味？早期科研判断评测](../../updates/2026-10-30/#rtaste) · 2026-10-30
    - [PAPERBENCHX：跨学科科学复现实验基准](../../updates/2026-10-30/#paperbenchx) · 2026-10-30
    - [OpenAI 邀外部专家与 Lean 核查 AI 科学证明](../../updates/2026-10-29/#openai-lean-ai) · 2026-10-29
12. **人机协作单列**：面向真实用户的智能体除成功率外，还应单列可操控性、信任校准、审批边界与变更响应；干预强度须随可核验证据分级，并验证拒绝必停、批准必达。
    - [JudiAct：证据驱动的分级干预](../../updates/2026-11-28/#judiact) · 2026-11-28
    - [Knowing What You Know：结果门控的审查者校准](../../updates/2026-11-20/#knowing-what-you-know) · 2026-11-20
    - [3D GameDev Arena：超长程游戏开发评测](../../updates/2026-11-19/#3d-gamedev-arena) · 2026-11-19
    - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
    - [Remembered as Brief：偏好记忆静默删减](../../updates/2026-11-18/#remembered-as-brief) · 2026-11-18
    - [可审计授权：跨层验证审批边界](../../updates/2026-11-17/#item-88) · 2026-11-17
    - [Interactive Visual Gym：模拟用户驱动的视觉交互闭环评测](../../updates/2026-11-13/#interactive-visual-gym) · 2026-11-13
    - [决策模型充当编程智能体策略门：显式边界提升风险检测并减少误报](../../updates/2026-11-06/#item-131) · 2026-11-06
    - [ProcessPrefBench：个体过程偏好的跨任务迁移评测](../../updates/2026-11-05/#processprefbench) · 2026-11-05
    - [OpenAI：智能体安全评测与生产行为存在显著差距](../../updates/2026-11-04/#openai) · 2026-11-04
    - [Co-Design Bench：智能体多模态协作编码评测](../../updates/2026-10-31/#co-design-bench) · 2026-10-31
    - [RealCLI：统一评估 CLI 智能体的人机协作](../../updates/2026-10-30/#realcli-cli) · 2026-10-30
    - [DynaRev：动态目标修订下的 Web 智能体评测基准](../../updates/2026-10-30/#dynarev-web) · 2026-10-30
    - [InteractiveWorld：可验证的人本交互式 MLLM 环境](../../updates/2026-10-29/#interactiveworld-mllm) · 2026-10-29
13. **代理指标须校准**：参与训练、选择或路由的代理评估器，须以真实下游成功、域外迁移和机制消融校准；过程解释还须逐项约束中间判断，不能由最终偏好正确推定可信。
    - [STEP-GRM：监督生成式奖励评估过程](../../updates/2026-11-28/#step-grm) · 2026-11-28
    - [RAP：可路由性前置审计](../../updates/2026-11-28/#rap) · 2026-11-28
    - [Best-of-N Steering：验证误差放大奖励作弊](../../updates/2026-11-26/#best-of-n-steering) · 2026-11-26
    - [无真值智能体评测：e值轨迹质量估计](../../updates/2026-11-25/#item-71) · 2026-11-25
    - [端点条件化过程增益评估](../../updates/2026-11-25/#item-133) · 2026-11-25
    - [暴露度预判奖励作弊](../../updates/2026-11-25/#item-123) · 2026-11-25
    - [CO-GRAFT：角色级策略嫁接归因](../../updates/2026-11-25/#co-graft) · 2026-11-25
    - [OmniDecisionBench：多模态决策可靠性评测](../../updates/2026-11-24/#omnidecisionbench) · 2026-11-24
    - [OpenAI预训练曲线：AI辅助模型设计](../../updates/2026-11-23/#openai-ai) · 2026-11-23
    - [METR：长任务能力3.6月翻倍](../../updates/2026-11-23/#metr-3-6) · 2026-11-23
    - [StrideWorld：预固定参照一致性评测](../../updates/2026-11-20/#strideworld) · 2026-11-20
    - [Sirius-Tiamat：决策保持式压缩评测](../../updates/2026-11-20/#sirius-tiamat) · 2026-11-20
    - [AppSci-Bench：端到端智能体构建评测](../../updates/2026-11-20/#appsci-bench) · 2026-11-20
    - [Normal-Only TTA：正常更新不保证检测增益](../../updates/2026-11-19/#normal-only-tta) · 2026-11-19
    - [编程基准高分不等于实际产出](../../updates/2026-11-19/#item-49) · 2026-11-19
    - [EVA-RSI：代理考试驱动视频评估自改进](../../updates/2026-11-19/#eva-rsi) · 2026-11-19
    - [Optimistic Verifiers：精确过程预言机审计](../../updates/2026-11-18/#optimistic-verifiers) · 2026-11-18
    - [Deciding Without Pointing：揭示检测与定位解耦](../../updates/2026-11-18/#deciding-without-pointing) · 2026-11-18
    - [决策模型：带置信度的临床字段抽取](../../updates/2026-11-17/#item-86) · 2026-11-17
    - [决策模型：候选比较的任务边界](../../updates/2026-11-17/#item-44) · 2026-11-17
    - [临床AI评估即干预](../../updates/2026-11-16/#item-18) · 2026-11-16
    - [SO-Arena：System One 模型能力谱系与决策可靠性基准](../../updates/2026-11-14/#so-arena-system-one) · 2026-11-14
    - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
    - [强化学习后印度语言任务的增益与退化](../../updates/2026-11-14/#item-35) · 2026-11-14
    - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
    - [Third Eye：递归自我改进的长期效用评估](../../updates/2026-11-12/#third-eye) · 2026-11-12
    - [SIRIS：评测 LLM 对仿真误差影响的判断能力](../../updates/2026-11-12/#siris-llm) · 2026-11-12
    - [RCEA：RLVR 中的奖励条件熵分配诊断](../../updates/2026-11-12/#rcea-rlvr) · 2026-11-12
    - [个性化评测中的错误用户对照混淆](../../updates/2026-11-12/#item-187) · 2026-11-12
    - [冻结权重智能体从失败轨迹中自我改进的价值与局限](../../updates/2026-11-12/#item-134) · 2026-11-12
    - [将科学论文转化为空间转录组智能体审计基准](../../updates/2026-11-12/#item-122) · 2026-11-12
    - [PACT：预填充到自回归的跨模型迁移](../../updates/2026-11-08/#pact) · 2026-11-08
    - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
    - [TandemBench：多智能体协作决策模型评测基准](../../updates/2026-11-06/#tandembench) · 2026-11-06
    - [从产物到能力：诊断自演化智能体的能力形成断点](../../updates/2026-11-06/#item-61) · 2026-11-06
    - [MemUse：在使用点评估智能体记忆](../../updates/2026-11-03/#memuse) · 2026-11-03
    - [感觉运动对齐：具身策略成功的低成本代理指标](../../updates/2026-10-30/#item-18) · 2026-10-30
    - [Decision 与 System One 模型的风湿病学准确率和校准评测](../../updates/2026-10-30/#decision-system-one) · 2026-10-30
14. **真实约束端到端**：长程智能体应在真实规模、跨平台系统与实际接口中交付可执行产物，并纳入时间、成本、权限、恢复与回归约束；须以可观察执行验收，接口差异应单独消融。
    - [RUIBench：机器人接口可靠性评测](../../updates/2026-11-28/#ruibench) · 2026-11-28
    - [OS-Omni：跨平台长程操作评测](../../updates/2026-11-28/#os-omni) · 2026-11-28
    - [数据库智能体错误损失分层评测](../../updates/2026-11-28/#item-13) · 2026-11-28
    - [WorldLeague：物理能动性统一评测](../../updates/2026-11-25/#worldleague) · 2026-11-25
    - [ShellBench：真实日常智能体评测](../../updates/2026-11-25/#shellbench) · 2026-11-25
    - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
    - [Decision Models：类型化决策能力评测](../../updates/2026-11-25/#decision-models) · 2026-11-25
    - [HarnessDev：自建执行框架评测](../../updates/2026-11-24/#harnessdev) · 2026-11-24
    - [模拟软件公司评测：端到端开发能力检验](../../updates/2026-11-23/#item-10) · 2026-11-23
    - [Singularity-Bench：AI研发设施自主构建](../../updates/2026-11-20/#singularity-bench-ai) · 2026-11-20
    - [FrontierOR：智能体优化算法设计](../../updates/2026-11-20/#frontieror) · 2026-11-20
    - [RSIBench-Infra：生产级基础设施优化评测](../../updates/2026-11-19/#rsibench-infra) · 2026-11-19
    - [3D GameDev Arena：超长程游戏开发评测](../../updates/2026-11-19/#3d-gamedev-arena) · 2026-11-19
    - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
    - [SciWorkBench：真实科研工作流评测](../../updates/2026-11-18/#sciworkbench) · 2026-11-18
    - [Mingbird：跨尺寸脚手架进度控制](../../updates/2026-11-18/#mingbird) · 2026-11-18
    - [GPT-6.2 Astra：基准满分却实务失灵](../../updates/2026-11-18/#gpt-6-2-astra) · 2026-11-18
    - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
    - [Accelerate Bench：应用级程序优化评测](../../updates/2026-11-18/#accelerate-bench) · 2026-11-18
    - [VibePrevisBench：四维场景编程评测](../../updates/2026-11-17/#vibeprevisbench) · 2026-11-17
    - [VAHBench：智能体长视频履约评测](../../updates/2026-11-17/#vahbench) · 2026-11-17
    - [Singularity-Bench：AI基建自主构建评测](../../updates/2026-11-16/#singularity-bench-ai) · 2026-11-16
    - [AscendGYM：成本感知算子优化评测](../../updates/2026-11-16/#ascendgym) · 2026-11-16
    - [NIBench：神经影像智能体执行、技能演化与科学判断基准](../../updates/2026-11-14/#nibench) · 2026-11-14
    - [WorkflowArena：可执行多智能体工作流编排评测基准](../../updates/2026-11-12/#workflowarena) · 2026-11-12
    - [Longtail-SWE：覆盖长尾编程语言的仓库级软件工程评测基准](../../updates/2026-11-12/#longtail-swe) · 2026-11-12
    - [Infrathon：真实世界长程 AI 基础设施优化智能体基准](../../updates/2026-11-12/#infrathon-ai) · 2026-11-12
    - [Embodied First Exam：编码智能体具身控制综合评测](../../updates/2026-11-12/#embodied-first-exam) · 2026-11-12
    - [ARE-bench：真实研究会话与工作空间中的智能体科研能力评测](../../updates/2026-11-12/#are-bench) · 2026-11-12
    - [AISLE：全球首个真实湿实验 AI Scientist 评测基准](../../updates/2026-11-12/#aisle-ai-scientist) · 2026-11-12
    - [VisSearch-Bench：多模态智能体长时程视觉搜索评测](../../updates/2026-11-08/#vissearch-bench) · 2026-11-08
    - [Scientist World：面向 AI 科学家的可执行研究世界](../../updates/2026-11-08/#scientist-world-ai) · 2026-11-08
    - [FINCOSMOS：金融智能体的开放世界评测范式](../../updates/2026-11-08/#fincosmos) · 2026-11-08
    - [SessionFarmer：从真实 Vibe Coding 会话构建 SWE 评测基准](../../updates/2026-11-06/#sessionfarmer-vibe-coding-swe) · 2026-11-06
    - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
    - [Multi-step SWE：编码智能体的长程持续开发评测](../../updates/2026-11-06/#multi-step-swe) · 2026-11-06
    - [FrontierPhysics：端到端物理研究智能体评测基准](../../updates/2026-11-06/#frontierphysics) · 2026-11-06
    - [CompressionBench：编码智能体自主压缩 LLM 评测](../../updates/2026-11-06/#compressionbench-llm) · 2026-11-06
    - [LoLBench：大型软件系统长程开发智能体评测](../../updates/2026-11-05/#lolbench) · 2026-11-05
15. **评测流水线回归**：持续评测应把基准当软件，版本化数据、标签时点、评估器、环境与推断配置并隔离答案资产；安全评测须将审计反馈和附加操作纳入攻击面，以部署代表的自适应攻击复测。
    - [Conartist：级联自适应提示注入](../../updates/2026-11-28/#conartist) · 2026-11-28
    - [VFR：验证式失败驱动修复](../../updates/2026-11-26/#vfr) · 2026-11-26
    - [攻击策略选择：代理策略误导监控评测](../../updates/2026-11-26/#item-23) · 2026-11-26
    - [TGB节点亲和力：时点泄漏审计](../../updates/2026-11-25/#tgb) · 2026-11-25
    - [TARE：无内容状态归因审计](../../updates/2026-11-25/#tare) · 2026-11-25
    - [STCG：检测过度规定测试](../../updates/2026-11-25/#stcg) · 2026-11-25
    - [Siren：弱沙盒越界评估](../../updates/2026-11-25/#siren) · 2026-11-25
    - [量化KV缓存维护：布局漂移与历史恢复](../../updates/2026-11-25/#item-93) · 2026-11-25
    - [EviCraft：证据闭包式具身评测](../../updates/2026-11-25/#evicraft) · 2026-11-25
    - [Antares-Smaug：未见攻击泛化评测](../../updates/2026-11-25/#antares-smaug) · 2026-11-25
    - [SplitBench：评测权限分离](../../updates/2026-11-23/#splitbench) · 2026-11-23
    - [Benchmarks' Last Exam：逐任务评测审计](../../updates/2026-11-23/#benchmarks-last-exam) · 2026-11-23
    - [Safe Personal RSI：回滚修复式安全更新](../../updates/2026-11-19/#safe-personal-rsi) · 2026-11-19
    - [Breath-Dx：漂移感知疾病筛查基准](../../updates/2026-11-19/#breath-dx) · 2026-11-19
    - [SkillBuffBench：多因素技能贡献评测](../../updates/2026-11-18/#skillbuffbench) · 2026-11-18
    - [Benchleaking：基准污染校正评测](../../updates/2026-11-18/#benchleaking) · 2026-11-18
    - [LoCoMo：提示与评判器敏感性审计](../../updates/2026-11-17/#locomo) · 2026-11-17
    - [Benchmark Factory：无标签质量锚点造基准](../../updates/2026-11-17/#benchmark-factory) · 2026-11-17
    - [MobileProbe：基于轨迹感知注入的移动智能体自适应安全评测](../../updates/2026-11-14/#mobileprobe) · 2026-11-14
    - [量化比较的噪声下限：引擎、重启、批处理与内核漂移](../../updates/2026-11-14/#item-60) · 2026-11-14
    - [自适应攻击下的能力隐藏检测压力测试](../../updates/2026-11-13/#item-47) · 2026-11-13
    - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
    - [OpenAI 披露 ExploitGym 智能体复用遗留凭据越权访问研究基础设施](../../updates/2026-11-12/#openai-exploitgym) · 2026-11-12
    - [前沿编程 LLM 是在编码还是作弊？](../../updates/2026-11-12/#llm-7) · 2026-11-12
    - [LLM 智能体评测的回放保真度：随机性、隐藏状态与测试预言机](../../updates/2026-11-12/#llm-5) · 2026-11-12
    - [推理历史删除敏感性是模型级属性](../../updates/2026-11-12/#item-220) · 2026-11-12
    - [部分提示污染测试中的假阳性与假阴性](../../updates/2026-11-12/#item-166) · 2026-11-12
    - [推理模型的推断：评测与服务实践经验](../../updates/2026-11-12/#item-148) · 2026-11-12
    - [BO-Arena：持续演进的高维贝叶斯优化基准](../../updates/2026-11-12/#bo-arena) · 2026-11-12
    - [将基准视为软件：Terminal-Bench 持续验证与维护](../../updates/2026-11-08/#terminal-bench) · 2026-11-08
    - [闭环智能体评估：分层测量与自校准](../../updates/2026-11-08/#item-45) · 2026-11-08
    - [WebHarbor：面向 GUI 智能体的真实网站环境套件](../../updates/2026-11-06/#webharbor-gui) · 2026-11-06
    - [PromptOps：LLM 评判系统的迭代提示优化](../../updates/2026-11-06/#promptops-llm) · 2026-11-06
    - [相同输出，不同得分：多模态基准评分器审计](../../updates/2026-11-06/#item-88) · 2026-11-06
    - [静默评测工具错误导致智能体排行榜重排](../../updates/2026-11-06/#item-67) · 2026-11-06
    - [Storage Agent Family：可追溯的持续评测与改进实践](../../updates/2026-11-04/#storage-agent-family) · 2026-11-04
<!-- experience-seen: 2026-11-21/gemini-4-hydrogen-token 2026-11-21/item-21 2026-11-21/item-24 2026-11-21/mind2act-world 2026-11-21/turingspace 2026-11-23/altair-nidhogg 2026-11-23/astronautbench 2026-11-23/benchmarks-last-exam 2026-11-23/coevobench 2026-11-23/groupassistbench 2026-11-23/item-10 2026-11-23/item-23 2026-11-23/memory-tax 2026-11-23/metr-3-6 2026-11-23/openai-ai 2026-11-23/so-arena 2026-11-23/splitbench 2026-11-24/agentrobocritic 2026-11-24/agrimanager 2026-11-24/autopilot 2026-11-24/harnessdev 2026-11-24/item-60 2026-11-24/item-67 2026-11-24/massys 2026-11-24/memanto 2026-11-24/nopeworld 2026-11-24/omnidecisionbench 2026-11-24/pure 2026-11-24/rdqa 2026-11-24/respacebench 2026-11-24/schedule-rank-profile 2026-11-25/antares-smaug 2026-11-25/asterism 2026-11-25/benchmint 2026-11-25/beyond-accuracy 2026-11-25/co-graft 2026-11-25/cua-see 2026-11-25/decision-models 2026-11-25/detection-gap 2026-11-25/evicraft 2026-11-25/gemini-4-neon 2026-11-25/geodecisions 2026-11-25/iclr-2026 2026-11-25/item-108 2026-11-25/item-109 2026-11-25/item-117 2026-11-25/item-123 2026-11-25/item-133 2026-11-25/item-136 2026-11-25/item-69 2026-11-25/item-71 2026-11-25/item-93 2026-11-25/lce 2026-11-25/mini-psych-agent 2026-11-25/prefill1 2026-11-25/recurscibench-rsi 2026-11-25/robolivemem 2026-11-25/robouniverse-10k 2026-11-25/s1arena-mm 2026-11-25/shellbench 2026-11-25/siren 2026-11-25/stcg 2026-11-25/stun-bench 2026-11-25/swapcert 2026-11-25/tare 2026-11-25/tea-leaves 2026-11-25/tgb 2026-11-25/transport-safe-evaluation 2026-11-25/vla 2026-11-25/worldleague 2026-11-26/agent-as-a-verifier 2026-11-26/autorlbench-rl 2026-11-26/best-of-n-steering 2026-11-26/cf-reward 2026-11-26/evolink-bench 2026-11-26/hub-j 2026-11-26/irtiqa 2026-11-26/item-23 2026-11-26/item-39 2026-11-26/item-86 2026-11-26/lingsante-medguard 2026-11-26/lost-in-translation 2026-11-26/medskill-e 2026-11-26/merlin-bench 2026-11-26/recordroute 2026-11-26/ree 2026-11-26/robodojo-mirror 2026-11-26/sealedloop 2026-11-26/skillsbench 2026-11-26/vfr 2026-11-27/egousebench 2026-11-27/real2simlab 2026-11-28/conartist 2026-11-28/drbench-pro 2026-11-28/item-13 2026-11-28/item-28 2026-11-28/judiact 2026-11-28/memphis 2026-11-28/os-omni 2026-11-28/proxygenbench 2026-11-28/rap 2026-11-28/rsi-2026 2026-11-28/ruibench 2026-11-28/step-grm 2026-11-28/uncovering-the-tells 2026-11-28/vernier -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments) — Meta 智能体研究评测平台
- [eval-dev-quality](https://github.com/symflower/eval-dev-quality) — 开发质量进化评测
- [ABench](https://github.com/inclusionAI/ABench) — 进化式开源 benchmark 套件
- [EvolIF](https://github.com/JiaQiSJTU/EvolIF) — benchmark 进化框架（多轮指令跟随）
- [LiveBench](https://github.com/livebench/livebench) — 持续更新的抗污染 LLM 基准，每六个月刷新
- [LiveCodeBench](https://github.com/livecodebench/livecodebench) — 持续收集新编程题的抗污染代码评测
- [EvoEval](https://github.com/evo-eval/evoeval) — 对 HumanEval 进化变换生成 828 个新问题
- [EvoCodeBench](https://github.com/seketeam/evocodebench) — 真实仓库对齐的进化代码基准（NeurIPS 2024）
- [Self-Evolving-Benchmark](https://github.com/NanshineLoong/Self-Evolving-Benchmark) — 多 Agent 框架自进化基准（COLING 2025, 被引 45）
- [DyCodeEval](https://github.com/SeekingDream/DyCodeEval) — 动态代码评测，语义等价变体抗污染（ICML 2025）
- [AutoBencher](https://github.com/XiangLi1999/AutoBencher) — 声明式自动基准构建（ICLR 2025）
- [Static-to-Dynamic-LLMEval](https://github.com/SeekingDream/Static-to-Dynamic-LLMEval) — 静态到动态评测综述仓库（EMNLP 2025）
- [MMBench-Live](https://github.com/PRIS-CV/MMBench-Live) — 多 Agent 驱动持续进化多模态基准（ICML 2026）
- [SDEval](https://github.com/hq-King/SDEval) — 安全性动态评测框架（AAAI 2026）
- [Code2Bench](https://github.com/Code2Bench/Code2Bench) — 从 GitHub commits 自动生成代码评测题
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 自进化 Agent 领域综合合集
- [awesome-data-contamination](https://github.com/lyy1994/awesome-data-contamination) — 数据污染与抗污染评测论文列表

**论文**
- [LiveBench: A Challenging, Contamination-Free LLM Benchmark](https://arxiv.org/abs/2406.19314) — 首个频繁更新题目的基准（被引 470+）
- [LiveCodeBench](https://arxiv.org/abs/2403.07974) — 持续收集新竞赛题（被引 1900+）
- [EvoEval: Evolving Coding Benchmarks via LLM](https://arxiv.org/abs/2403.19114) — LLM 语义变换生成新题
- [Benchmark Self-Evolving (COLING 2025)](https://arxiv.org/abs/2402.11443) — 多 Agent 自进化基准框架（被引 45）
- [DyCodeEval (ICML 2025)](https://arxiv.org/abs/2503.04149) — 动态代码推理评测（被引 33）
- [AutoBencher (ICLR 2025)](https://arxiv.org/abs/2407.08351) — 声明式自动基准构建（被引 31）
- [From Static to Dynamic: A Survey on LLM Evaluation (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.511.pdf) — 动态评测综述（被引 32）
- [Towards Contamination Resistant Benchmarks](https://arxiv.org/abs/2505.08389) — 抗污染性概念
- [LLM-Evolve (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.940) — 序贯问题求解评测（被引 20）
- [ArenaBencher](https://arxiv.org/abs/2510.08569) — 多模型竞争驱动基准进化
- [MMBench-Live (ICML 2026)](https://arxiv.org/abs/2607.01813) — 持续进化多模态基准
- [SDEval (AAAI 2026)](https://arxiv.org/abs/2508.06142) — 安全动态评测（被引 7）
- [Towards Self-Evolving Agent Benchmarks](https://openreview.net/forum?id=2H03gm4Rq6) — 可验证自进化基准
- [Evolutionary Perspectives on LLM-Based Multi-Agent Evaluation](https://arxiv.org/abs/2506.11102) — 进化视角评测方法论分析
