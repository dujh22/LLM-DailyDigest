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
1. **持续学习多维评测**：连续任务流应分开评估知识更新与能力形成，并测可塑性、稳定性、遗忘、技能组合、故障诊修及跨语言等未见迁移；持久状态提效不等于可追溯泛化。
   - [软提示技能的组合兼容与保持](../../updates/2026-11-26/#item-39) · 2026-11-26
   - [IRTIQA：自进化跨语言迁移评测](../../updates/2026-11-26/#irtiqa) · 2026-11-26
   - [EvoLink-Bench：长程依赖任务流评测](../../updates/2026-11-26/#evolink-bench) · 2026-11-26
   - [AutoRLBench：真实RL故障诊修评测](../../updates/2026-11-26/#autorlbench-rl) · 2026-11-26
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [AstronautBench：三视角自改进评测](../../updates/2026-11-23/#astronautbench) · 2026-11-23
   - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
   - [NIBench：神经影像智能体执行、技能演化与科学判断基准](../../updates/2026-11-14/#nibench) · 2026-11-14
   - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
   - [RSI-PDEbench：偏微分方程求解智能体递归自我改进基准](../../updates/2026-11-13/#rsi-pdebench) · 2026-11-13
   - [冻结权重智能体从失败轨迹中自我改进的价值与局限](../../updates/2026-11-12/#item-134) · 2026-11-12
   - [Flex-RSI：前沿智能体递归自我改进评测基准](../../updates/2026-11-12/#flex-rsi) · 2026-11-12
   - [Continual-ARC：衡量智能体终身技能习得](../../updates/2026-11-12/#continual-arc) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [SelfImprove-Bench：自改进智能体泛化能力评测](../../updates/2026-11-06/#selfimprove-bench) · 2026-11-06
   - [ReScopeBench：演化环境中的智能体经验生命周期评测](../../updates/2026-11-06/#rescopebench) · 2026-11-06
   - [从产物到能力：诊断自演化智能体的能力形成断点](../../updates/2026-11-06/#item-61) · 2026-11-06
   - [Continual AutoResearch：智能体能否跨任务持续学习](../../updates/2026-11-06/#continual-autoresearch) · 2026-11-06
   - [DeepMind：自演化智能体能否持续学习？](../../updates/2026-10-29/#deepmind) · 2026-10-29
   - [CLE：LLM 智能体长时程持续学习与经验学习基准](../../updates/2026-10-29/#cle-llm) · 2026-10-29
2. **外部状态优先演化**：参数冻结时优先更新外部记忆与Harness；在可验证任务上可比测试时训练更省算力且更易部署。
   - [SpatialCraft：经验技能双流自进化](../../updates/2026-11-25/#spatialcraft) · 2026-11-25
   - [Harness2：跨任务框架优化经验库](../../updates/2026-11-25/#harness2) · 2026-11-25
   - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
   - [自主自学习：智能体自建改进算法](../../updates/2026-11-19/#item-48) · 2026-11-19
   - [MIGRO：跨模型可移植的解耦长期记忆系统](../../updates/2026-11-13/#migro) · 2026-11-13
   - [WICL：面向智能体机器人操作的世界上下文学习](../../updates/2026-11-12/#wicl) · 2026-11-12
   - [SimplEvo：通过文本记忆演化提升具身智能体](../../updates/2026-11-12/#simplevo) · 2026-11-12
   - [GEAR：Scikit-learn 式模块化 RSI 框架推动 Agent 持续进化](../../updates/2026-11-12/#gear-scikit-learn-rsi-agent) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [具身双脑协同：让机器人跨任务复用经验](../../updates/2026-11-08/#item-19) · 2026-11-08
   - [Evolver：将智能体探索转化为持续演化能力](../../updates/2026-11-08/#evolver) · 2026-11-08
   - [Meta²：为长程智能体在线脚手架演化预计算可复用知识](../../updates/2026-11-06/#meta) · 2026-11-06
   - [VERSE：面向智能体 Harness 的可验证自进化优化器](../../updates/2026-11-05/#verse-harness) · 2026-11-05
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [CMU开源Hermit：统一Harness层RSI与持续学习框架](../../updates/2026-10-30/#cmu-hermit-harness-rsi) · 2026-10-30
   - [TTME：测试时记忆演化以更低成本助力科学发现](../../updates/2026-10-29/#ttme) · 2026-10-29
3. **经验验真再入库**：经验准入须经执行、溯源、留出证伪与对照行为核验；上线后按实际效用持续修正，并保留原轨迹和旧版以防污染与回退。
   - [SIM：经验记忆驱动持续改进](../../updates/2026-11-26/#sim) · 2026-11-26
   - [SED：单次注入毒化安全策略](../../updates/2026-11-26/#sed) · 2026-11-26
   - [Leto：效用导向智能体记忆](../../updates/2026-11-26/#leto) · 2026-11-26
   - [EGSE：证据溯源式技能演化](../../updates/2026-11-26/#egse) · 2026-11-26
   - [ReHarness：结果驱动的经验反向修正](../../updates/2026-11-25/#reharness) · 2026-11-25
   - [Notary门控回顾环：规则准入效用验证](../../updates/2026-11-25/#notary) · 2026-11-25
   - [ExpGuard：经验风险预测与在线修复](../../updates/2026-11-25/#expguard) · 2026-11-25
   - [DoppelVet：对照式更新安全验证](../../updates/2026-11-25/#doppelvet) · 2026-11-25
   - [ZhuLong-SE：执行轨迹驱动自进化](../../updates/2026-11-23/#zhulong-se) · 2026-11-23
   - [DriftGuard：因果归因式记忆漂移检测](../../updates/2026-11-20/#driftguard) · 2026-11-20
   - [SCAFFOLD：担保保持式证据迁移](../../updates/2026-11-19/#scaffold) · 2026-11-19
   - [ARISE：留出验证式记忆演化](../../updates/2026-11-19/#arise) · 2026-11-19
   - [StaleBench：隔离陈旧检索并量化修复成本](../../updates/2026-11-17/#stalebench) · 2026-11-17
   - [ReHarness：反向修订式持续学习](../../updates/2026-11-17/#reharness) · 2026-11-17
   - [Matrix with Steps：外部验真式双层记忆](../../updates/2026-11-17/#matrix-with-steps) · 2026-11-17
   - [AdMem：期望对齐的程序记忆](../../updates/2026-11-17/#admem) · 2026-11-17
   - [RSI综述：四组件七步自进化框架](../../updates/2026-11-16/#rsi) · 2026-11-16
   - [自主智能体自生成更新的证据治理采纳框架 EGE](../../updates/2026-11-14/#ege) · 2026-11-14
   - [WikiTrace：证据关联记忆减少智能体性能退化](../../updates/2026-11-12/#wikitrace) · 2026-11-12
   - [TRUST：具备统计保证的可信递归自我改进](../../updates/2026-11-12/#trust) · 2026-11-12
   - [SoMem：LLM 智能体自主组织持久记忆](../../updates/2026-11-12/#somem-llm) · 2026-11-12
   - [openJiuwen发布TTSE双轨经验学习框架](../../updates/2026-11-12/#openjiuwen-ttse) · 2026-11-12
   - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
   - [反馈投毒如何形成文本技能后门](../../updates/2026-11-12/#item-195) · 2026-11-12
   - [何时应让智能体记忆？基于证伪门控的自进化框架 FGSE](../../updates/2026-11-12/#fgse) · 2026-11-12
   - [BadEvolve：通过失败感知任务优化投毒自进化智能体](../../updates/2026-11-12/#badevolve) · 2026-11-12
   - [WASP-Mem：智能体自主组织过程记忆，人类专注失败诊断](../../updates/2026-11-06/#wasp-mem) · 2026-11-06
   - [EvoML：验证门控的自进化机器学习流水线合成](../../updates/2026-11-06/#evoml) · 2026-11-06
   - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
   - [EvoGuard：缓解在线技能演化中的性能退化](../../updates/2026-11-05/#evoguard) · 2026-11-05
   - [ProactMem：面向事件驱动 LLM 智能体的主动记忆](../../updates/2026-10-29/#proactmem-llm) · 2026-10-29
   - [GEPA-Curator：面向自改进智能体的经验策展学习](../../updates/2026-10-29/#gepa-curator) · 2026-10-29
4. **经验需要结构化**：将经验表示为任务状态、动作前置条件与效果、定量干预关系，比自由文本更利于复用、恢复和组合。
   - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
   - [MMMem：任务感知多模态经验固化](../../updates/2026-11-25/#mmmem) · 2026-11-25
   - [LCE：失败模式多样性诊断](../../updates/2026-11-25/#lce) · 2026-11-25
   - [AutoSECO：可迁移求解技能演化](../../updates/2026-11-25/#autoseco) · 2026-11-25
   - [Engram：异构调优的多阶段记忆](../../updates/2026-11-24/#engram) · 2026-11-24
   - [BRIDGE：极简检索记忆](../../updates/2026-11-18/#bridge) · 2026-11-18
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [Matrix with Steps：外部验真式双层记忆](../../updates/2026-11-17/#matrix-with-steps) · 2026-11-17
   - [HyperSkill：基于超图技能库演化的免训练全模态 GRPO](../../updates/2026-11-13/#hyperskill-grpo) · 2026-11-13
   - [SMO：将自然语言技能编译为可复用状态-操作-结果图](../../updates/2026-11-12/#smo) · 2026-11-12
   - [Sage-Taiyi：面向科学发现的元认知架构](../../updates/2026-11-12/#sage-taiyi) · 2026-11-12
   - [openJiuwen发布TTSE双轨经验学习框架](../../updates/2026-11-12/#openjiuwen-ttse) · 2026-11-12
   - [Evolver：将智能体探索转化为持续演化能力](../../updates/2026-11-08/#evolver) · 2026-11-08
   - [MDSKILL：多视图蒸馏实现技能记忆内化与智能体自进化](../../updates/2026-11-06/#mdskill) · 2026-11-06
   - [HTCE：受同胚启发的跨场景导航经验规范化与复用](../../updates/2026-11-06/#htce) · 2026-11-06
   - [EvoMemState：面向个人智能体的演化记忆状态](../../updates/2026-11-06/#evomemstate) · 2026-11-06
   - [SwarmRSI：共享失败经验驱动科研智能体群递归自我改进](../../updates/2026-11-05/#swarmrsi) · 2026-11-05
   - [SPAR：多轮 B2B 销售智能体的经验驱动策略演化](../../updates/2026-11-03/#spar-b2b) · 2026-11-03
   - [MEMIG：面向抗体优化的自演化结构化记忆](../../updates/2026-11-02/#memig) · 2026-11-02
   - [CausGround：基于因果交互定位的自适应具身规划](../../updates/2026-10-30/#causground) · 2026-10-30
   - [TAM：以任务推进状态与监督增强 GUI 智能体能力](../../updates/2026-10-29/#tam-gui) · 2026-10-29
5. **按状态路由资源**：按任务、进度、环境动力学和组件可接管边界路由记忆、技能与模型，并控制注入量；边界外不交接可减少失败、干扰与词元成本。
   - [Boundary-Aware Policy Learning：策略交接边界塑形](../../updates/2026-11-28/#boundary-aware-policy-learning) · 2026-11-28
   - [PRECEPT：失误驱动的安全原则演化](../../updates/2026-11-26/#precept) · 2026-11-26
   - [MetaDecomp：程序记忆驱动自适应分解](../../updates/2026-11-26/#metadecomp) · 2026-11-26
   - [STUN-Bench：真未见工具路由评测](../../updates/2026-11-25/#stun-bench) · 2026-11-25
   - [STRIDE：策略战术分层技能披露](../../updates/2026-11-24/#stride) · 2026-11-24
   - [F³：形适融经验利用](../../updates/2026-11-20/#item-76) · 2026-11-20
   - [自蒸馏记忆：按模型能力调节记忆量](../../updates/2026-11-20/#item-34) · 2026-11-20
   - [ENA：物理索引式专家记忆](../../updates/2026-11-18/#ena) · 2026-11-18
   - [TokenEconomizer：仓库经验驱动降本](../../updates/2026-11-17/#tokeneconomizer) · 2026-11-17
   - [Skill Adapter：通用技能的个性化适配与在线路由](../../updates/2026-11-14/#skill-adapter) · 2026-11-14
   - [Synapse-Control：以轻量运行时控制激活智能体经验](../../updates/2026-11-12/#synapse-control) · 2026-11-12
   - [SCALE：小模型优先的概念抽象与 LLM 引导经验内化](../../updates/2026-11-12/#scale-llm) · 2026-11-12
   - [MIRIX-2.0：多智能体长期记忆系统](../../updates/2026-11-12/#mirix-2-0) · 2026-11-12
   - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
   - [Decision Context：智能体持久化行为学习](../../updates/2026-11-12/#decision-context) · 2026-11-12
   - [AgentBaton：长程智能体任务中的高效模型接力](../../updates/2026-11-12/#agentbaton) · 2026-11-12
   - [ScienceCUA：科学软件智能体的资源转技能与执行引导技能演化](../../updates/2026-11-06/#sciencecua) · 2026-11-06
   - [主动式 LLM 智能体的前瞻记忆](../../updates/2026-11-06/#llm-2) · 2026-11-06
   - [OMCE：经验增强智能体的在线记忆演化与元控制](../../updates/2026-11-03/#omce) · 2026-11-03
   - [Meta提出路由式持续学习架构Routed CL](../../updates/2026-11-03/#meta-routed-cl) · 2026-11-03
   - [JitSkill：基于长程状态追踪的即时技能检索](../../updates/2026-11-03/#jitskill) · 2026-11-03
   - [检索即遍历：面向有状态长上下文智能体的价值索引记忆](../../updates/2026-10-30/#item-68) · 2026-10-30
6. **经验系统联合演化**：内容趋于饱和时，应联合搜索表示、写入、组织、检索、遗忘与变换策略，并区分成败经验的维护目标；固定架构和统一更新算子会限制收益并放大错误。
   - [Knowledge-Base Gradient Descent：问答驱动知识库重构](../../updates/2026-11-26/#knowledge-base-gradient-descent) · 2026-11-26
   - [DualPM：双极性记忆定期维护](../../updates/2026-11-26/#dualpm) · 2026-11-26
   - [MLEvolver：上下文折叠与技能删汰](../../updates/2026-11-24/#mlevolver) · 2026-11-24
   - [EvoSkill-S1：遗传算子驱动技能演化](../../updates/2026-11-18/#evoskill-s1) · 2026-11-18
   - [EvoDisco：策略发现式记忆演化](../../updates/2026-11-18/#evodisco) · 2026-11-18
   - [Dreaming：选择性记忆与离线纠错](../../updates/2026-11-17/#dreaming) · 2026-11-17
   - [MAPE：通过程序进化发现高效智能体记忆设计](../../updates/2026-11-14/#mape) · 2026-11-14
   - [SoMem：LLM 智能体自主组织持久记忆](../../updates/2026-11-12/#somem-llm) · 2026-11-12
   - [MIRIX-2.0：多智能体长期记忆系统](../../updates/2026-11-12/#mirix-2-0) · 2026-11-12
   - [Anthropic公开Claude离线“做梦”长期记忆架构](../../updates/2026-11-08/#anthropic-claude) · 2026-11-08
   - [智能体需要睡眠吗？睡眠启发的记忆巩固](../../updates/2026-11-06/#item-129) · 2026-11-06
   - [MemEvolve：智能体记忆架构的元进化](../../updates/2026-11-02/#memevolve) · 2026-11-02
7. **确定性技能程序化**：将确定性步骤编译为带适用条件的可验证程序，只把歧义决策留给模型，可提升稳定性、审计性和复用率。
   - [ToolSmith：自动生成可复用工具](../../updates/2026-11-25/#toolsmith) · 2026-11-25
   - [SpatialCraft：经验技能双流自进化](../../updates/2026-11-25/#spatialcraft) · 2026-11-25
   - [HarnessMM：决策图复用免回调](../../updates/2026-11-25/#harnessmm) · 2026-11-25
   - [StarTV-Agent：快慢双路工具编排](../../updates/2026-11-21/#startv-agent) · 2026-11-21
   - [System-One RSI：引导练习式肌肉记忆](../../updates/2026-11-20/#system-one-rsi) · 2026-11-20
   - [SIGame：代码策略自我改进](../../updates/2026-11-20/#sigame) · 2026-11-20
   - [MetaAct：可执行动作约束自演化](../../updates/2026-11-17/#metaact) · 2026-11-17
   - [MEM-SQL：分层复用历史查询](../../updates/2026-11-17/#mem-sql) · 2026-11-17
   - [EvoX：将智能体脚手架重构为运行时策略](../../updates/2026-11-13/#evox) · 2026-11-13
   - [SMO：将自然语言技能编译为可复用状态-操作-结果图](../../updates/2026-11-12/#smo) · 2026-11-12
   - [PASE：程序辅助的可修补技能演化](../../updates/2026-11-12/#pase) · 2026-11-12
   - [CPU-ARC：可在 CPU 上复用的智能体推理缓存](../../updates/2026-11-12/#cpu-arc-cpu) · 2026-11-12
   - [Strategist：用智能体演化推理策略](../../updates/2026-11-06/#strategist) · 2026-11-06
   - [ScienceCUA：科学软件智能体的资源转技能与执行引导技能演化](../../updates/2026-11-06/#sciencecua) · 2026-11-06
   - [面向 LLM 智能体安全的累积式可审计护栏工具演化](../../updates/2026-11-06/#llm-3) · 2026-11-06
   - [LIBRA：程序化归纳可执行工具库](../../updates/2026-11-06/#libra) · 2026-11-06
   - [SeaFlow：基于语义任务分解的自演化智能体工作流](../../updates/2026-11-03/#seaflow) · 2026-11-03
   - [腾讯混元发布 Hyra 2.0：通用 Agent 研发可复用科学工具](../../updates/2026-11-03/#hyra-2-0-agent) · 2026-11-03
   - [SkillCompiler：以程序化编译降低自演化智能体技能的不确定性](../../updates/2026-10-30/#skillcompiler) · 2026-10-30
8. **组件配对协同演化**：固定评分或独立升级组件易固化盲点并造成接口错配；应让模型、评判、改进器与脚手架协同演化，并归档历史版本以搜索最佳配对。
   - [CoEvo-RSI：模型与脚手架协同演化](../../updates/2026-11-28/#coevo-rsi) · 2026-11-28
   - [RoboEvo²：脚手架策略协同进化](../../updates/2026-11-26/#roboevo) · 2026-11-26
   - [Semantic PID-RSI：语义PID控制自改进](../../updates/2026-11-24/#semantic-pid-rsi-pid) · 2026-11-24
   - [MedicalRSI：临床模型与脚手架协同演化](../../updates/2026-11-23/#medicalrsi) · 2026-11-23
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [GRAFT：执行证据引导遗传重组](../../updates/2026-11-19/#graft) · 2026-11-19
   - [ELITE：无评估机制整合](../../updates/2026-11-18/#elite) · 2026-11-18
   - [VbD：无外部反馈下执行与评估协同演化](../../updates/2026-11-13/#vbd) · 2026-11-13
   - [闭环智能体评估：分层测量与自校准](../../updates/2026-11-08/#item-45) · 2026-11-08
   - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
   - [VERSE：面向智能体 Harness 的可验证自进化优化器](../../updates/2026-11-05/#verse-harness) · 2026-11-05
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [LegalEvolver：量规引导自进化的法律判决预测智能体](../../updates/2026-11-05/#legalevolver) · 2026-11-05
   - [RuHarness：评判准则与智能体脚手架协同演化](../../updates/2026-10-29/#ruharness) · 2026-10-29
9. **闭环必须可验证**：自进化闭环须先将趣味等主观目标拆成可诊断维度并可靠发现故障，再由执行器、硬件或独立审计器提供可复核反馈；否则会加速收敛到错误行为。
   - [Play2Evolve：趣味反馈驱动游戏演化](../../updates/2026-11-27/#play2evolve) · 2026-11-27
   - [PartAgent：专家集成与闭环分割](../../updates/2026-11-26/#partagent) · 2026-11-26
   - [AutoRLBench：真实RL故障诊修评测](../../updates/2026-11-26/#autorlbench-rl) · 2026-11-26
   - [VISE：工具实现反馈驱动技能演化](../../updates/2026-11-25/#vise) · 2026-11-25
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [γ-Scape：智能体中心具身世界](../../updates/2026-11-24/#scape) · 2026-11-24
   - [Space-X：证据链驱动空间自进化](../../updates/2026-11-21/#space-x) · 2026-11-21
   - [Cyber-Physical RSI：物理反馈闭环自改进](../../updates/2026-11-20/#cyber-physical-rsi) · 2026-11-20
   - [QDA：智能体闭环量化设计](../../updates/2026-11-19/#qda) · 2026-11-19
   - [SPILLWAY：目标准入与净化分离](../../updates/2026-11-18/#spillway) · 2026-11-18
   - [书生·S2.1 Flash：统一表征与递归进化](../../updates/2026-11-17/#s2-1-flash) · 2026-11-17
   - [Craftax：续程反馈引导策略进化](../../updates/2026-11-17/#craftax) · 2026-11-17
   - [AGPV：智能体引导过程验证](../../updates/2026-11-17/#agpv) · 2026-11-17
   - [Verifiable pXRD：验证器引导的爬山解析](../../updates/2026-11-16/#verifiable-pxrd) · 2026-11-16
   - [TRUST：具备统计保证的可信递归自我改进](../../updates/2026-11-12/#trust) · 2026-11-12
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [Enmo Safety：现成语言模型的外置非侵入式安全监督](../../updates/2026-11-12/#enmo-safety) · 2026-11-12
   - [闭环智能体评估：分层测量与自校准](../../updates/2026-11-08/#item-45) · 2026-11-08
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [自主研究智能体优化 MSA 以提升蛋白质复合物结构预测](../../updates/2026-11-06/#msa) · 2026-11-06
   - [AI适应过程：达尔文式、拉马克式与智能体定向演化](../../updates/2026-11-06/#item-23) · 2026-11-06
   - [EvoML：验证门控的自进化机器学习流水线合成](../../updates/2026-11-06/#evoml) · 2026-11-06
   - [RSIGym：面向递归自我改进的真实训练环境](../../updates/2026-11-05/#rsigym) · 2026-11-05
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [ForgeKernel零样本自进化生成算子，性能超越DeepSeek FlashMLA 9.8%](../../updates/2026-10-31/#forgekernel-deepseek-flashmla-9-8) · 2026-10-31
   - [Gym-Anything：用编程智能体规模化构建机器人仿真](../../updates/2026-10-30/#gym-anything) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
   - [无问芯穹算子优化Agent斩获SOL-ExecBench 88项第一](../../updates/2026-10-29/#agent-sol-execbench-88) · 2026-10-29
10. **长程上下文分段**：长程执行应分离可寻址的完整记录与决策用紧凑状态，让模型按任务语义选择压缩时机和范围，并以检查点、缓存复用和重置控长；压缩不得覆盖当前证据。
    - [模型自主上下文管理：按需压缩与缓存复用](../../updates/2026-11-26/#item-87) · 2026-11-26
    - [紧凑状态抽象：递归程序压缩历史](../../updates/2026-11-25/#item-64) · 2026-11-25
    - [DMC-5：双模型缓存感知压缩](../../updates/2026-11-25/#dmc-5) · 2026-11-25
    - [MLEvolver：上下文折叠与技能删汰](../../updates/2026-11-24/#mlevolver) · 2026-11-24
    - [EvoViM：递归自演化视觉程序](../../updates/2026-11-24/#evovim) · 2026-11-24
    - [GrepMem：无损免索引长期记忆](../../updates/2026-11-20/#grepmem) · 2026-11-20
    - [SCoRe：停机突发式上下文压缩](../../updates/2026-11-19/#score) · 2026-11-19
    - [SCH：状态证据分离式上下文交接](../../updates/2026-11-19/#sch) · 2026-11-19
    - [世界仍保留错误时，清理智能体历史反而有害](../../updates/2026-11-13/#item-41) · 2026-11-13
    - [WAAC：面向工作流的智能体轨迹压缩](../../updates/2026-11-12/#waac) · 2026-11-12
    - [千问 Personal Agent：模型、记忆与生态的协同架构](../../updates/2026-11-06/#personal-agent) · 2026-11-06
    - [智能体自写交接摘要何时变成无依据指令？](../../updates/2026-11-06/#item-33) · 2026-11-06
    - [CoworkOS：面向真实世界自动化的长程智能体协作框架](../../updates/2026-11-04/#coworkos) · 2026-11-04
    - [CORAL：面向长程智能体的认知资源自分配](../../updates/2026-10-30/#coral) · 2026-10-30
11. **增益归因控制噪声**：评估更新须用配对重复、置换对照与样本外验证校准方差，并分别测自主与引导执行；统一基线与成本，诊断残余失败并分解模型、技能和脚手架的边际贡献。
    - [SkillsBench：技能增益的噪声感知审计](../../updates/2026-11-26/#skillsbench) · 2026-11-26
    - [Scalpel and Brush：智能体稀疏权重编辑](../../updates/2026-11-26/#scalpel-and-brush) · 2026-11-26
    - [MedSkill-E²：医疗技能评测与演化](../../updates/2026-11-26/#medskill-e) · 2026-11-26
    - [失效类型驱动的智能体干预](../../updates/2026-11-25/#item-136) · 2026-11-25
    - [Retriever–Perceiver–Reasoner：诊断反馈协同进化](../../updates/2026-11-19/#retriever-perceiver-reasoner) · 2026-11-19
    - [Resolution Hypothesis：评测分辨率瓶颈](../../updates/2026-11-19/#resolution-hypothesis) · 2026-11-19
    - [SkillBuffBench：多因素技能贡献评测](../../updates/2026-11-18/#skillbuffbench) · 2026-11-18
    - [SkillMaster：策略内生技能进化](../../updates/2026-11-17/#skillmaster) · 2026-11-17
    - [One Run Is Not Enough：配对校准记忆增益](../../updates/2026-11-17/#one-run-is-not-enough) · 2026-11-17
    - [MemCredit：以决策效用优化长程 Web 智能体记忆](../../updates/2026-11-14/#memcredit-web) · 2026-11-14
    - [CoReMem：面向连续编程任务的成本内化记忆框架](../../updates/2026-11-14/#coremem) · 2026-11-14
    - [RSI Tax：递归自我改进何时得不偿失](../../updates/2026-11-12/#rsi-tax) · 2026-11-12
    - [EARN：冻结 LLM 智能体的测试时适应与路径固化](../../updates/2026-11-12/#earn-llm) · 2026-11-12
    - [Top-k 检索下的记忆价值不可识别](../../updates/2026-11-06/#top-k) · 2026-11-06
    - [EvoGuard：缓解在线技能演化中的性能退化](../../updates/2026-11-05/#evoguard) · 2026-11-05
    - [下一轮部署前：诊断策略更新引发的技能效用变化](../../updates/2026-10-30/#item-72) · 2026-10-30
    - [BiPA：用二部归因重新评估智能体技能优化](../../updates/2026-10-29/#bipa) · 2026-10-29
12. **群体共享演化资产**：多智能体应按用户与作用域区分抽象知识与可执行技能，并以对本地任务的实效而非表面相似度决定共享；限制检索边界并在经验隔离下评测。
    - [P-FedSkill：个性化联邦技能学习](../../updates/2026-11-26/#p-fedskill) · 2026-11-26
    - [STUN-Bench：真未见工具路由评测](../../updates/2026-11-25/#stun-bench) · 2026-11-25
    - [OpenKAGE：知识共享式群体演化](../../updates/2026-11-19/#openkage) · 2026-11-19
    - [MixUA：面向多用户多智能体交互的多粒度记忆提取](../../updates/2026-11-12/#mixua) · 2026-11-12
    - [EvolveNet：协作式 Harness 演化推动智能体自我改进](../../updates/2026-11-12/#evolvenet-harness) · 2026-11-12
    - [SwarmRSI：共享失败经验驱动科研智能体群递归自我改进](../../updates/2026-11-05/#swarmrsi) · 2026-11-05
    - [Group-Evolving Agents：经验共享驱动的开放式群体自进化](../../updates/2026-11-04/#group-evolving-agents) · 2026-11-04
    - [EvoTeam：通过团队演化增强多智能体协作](../../updates/2026-10-30/#evoteam) · 2026-10-30
13. **版本化原子更新**：生产系统应将经验改动拆成可回滚的局部编辑，绑定环境与接口版本及失效条件；每次更新须检查新增退化并保护先验外知识。
    - [Sports Agent：反馈驱动闭环自进化](../../updates/2026-11-26/#sports-agent) · 2026-11-26
    - [SkillLens：人机协同技能诊断优化](../../updates/2026-11-24/#skilllens) · 2026-11-24
    - [Semantic PID-RSI：语义PID控制自改进](../../updates/2026-11-24/#semantic-pid-rsi-pid) · 2026-11-24
    - [SkillPlumber：覆盖引导技能进化](../../updates/2026-11-20/#skillplumber) · 2026-11-20
    - [SkillDiff：标记先验外专家知识](../../updates/2026-11-20/#skilldiff) · 2026-11-20
    - [GUARD：后悔引导脚手架演化](../../updates/2026-11-19/#guard) · 2026-11-19
    - [选择性维护：运行时修复过时技能](../../updates/2026-11-18/#item-33) · 2026-11-18
    - [Experience Rot：静默变更引发经验腐化](../../updates/2026-11-18/#experience-rot) · 2026-11-18
    - [SPLICE：分块约束式提示演化](../../updates/2026-11-17/#splice) · 2026-11-17
    - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
    - [PASE：程序辅助的可修补技能演化](../../updates/2026-11-12/#pase) · 2026-11-12
    - [快慢双环：长程智能体部署的控制论监督框架](../../updates/2026-11-12/#item-210) · 2026-11-12
    - [EvolveNet：协作式 Harness 演化推动智能体自我改进](../../updates/2026-11-12/#evolvenet-harness) · 2026-11-12
    - [Enmo Safety：现成语言模型的外置非侵入式安全监督](../../updates/2026-11-12/#enmo-safety) · 2026-11-12
    - [Meta²：为长程智能体在线脚手架演化预计算可复用知识](../../updates/2026-11-06/#meta) · 2026-11-06
    - [面向 LLM 智能体安全的累积式可审计护栏工具演化](../../updates/2026-11-06/#llm-3) · 2026-11-06
    - [KARMA：工业广告智能体的免训练知识原子化脚手架演化](../../updates/2026-10-30/#karma) · 2026-10-30
14. **世界模型预筛搜索**：真实执行昂贵时，可先用世界模型预测报错、日志和得分以筛选候选，再把执行预算留给高价值方案。
    - [WICL：面向智能体机器人操作的世界上下文学习](../../updates/2026-11-12/#wicl) · 2026-11-12
    - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
    - [MLE-World：用世界模型预测机器学习实验结果](../../updates/2026-10-29/#mle-world) · 2026-10-29
15. **感知先于规划**：交互环境中应先定位任务相关证据，并按环境变化主动刷新状态；低成本持续同步常比加深规划更有效，外部先验不得覆盖当前观测。
    - [NightWatch：主动流式界面感知](../../updates/2026-11-26/#nightwatch) · 2026-11-26
    - [Bel：动作落点可视化重排](../../updates/2026-11-23/#bel) · 2026-11-23
    - [PriorSplit：外部顺序记忆与在策略自蒸馏驱动的自进化 VLM 智能体](../../updates/2026-11-14/#priorsplit-vlm) · 2026-11-14
    - [智能体机器人自学习中的模型、技能、反馈与课程控制研究](../../updates/2026-11-12/#item-202) · 2026-11-12
    - [SARBLOH：空间感知主导 ARC-AGI-3 交互推理](../../updates/2026-11-06/#sarbloh-arc-agi-3) · 2026-11-06
    - [Reviso：面向视频字幕生成的优先级引导主动观察](../../updates/2026-11-04/#reviso) · 2026-11-04
<!-- experience-seen: 2026-11-21/space-x 2026-11-21/startv-agent 2026-11-23/alps-lab 2026-11-23/astronautbench 2026-11-23/bel 2026-11-23/coevobench 2026-11-23/embodied-harness 2026-11-23/medicalrsi 2026-11-23/zhulong-se 2026-11-24/don-t-train-it-write-it 2026-11-24/engram 2026-11-24/evovim 2026-11-24/io-ai 2026-11-24/mlevolver 2026-11-24/scape 2026-11-24/semantic-pid-rsi-pid 2026-11-24/skilllens 2026-11-24/stride 2026-11-25/agl-skill 2026-11-25/autoseco 2026-11-25/detection-gap 2026-11-25/dmc-5 2026-11-25/doppelvet 2026-11-25/expguard 2026-11-25/fin-rsi 2026-11-25/habitats 2026-11-25/harness2 2026-11-25/harnessmm 2026-11-25/item-136 2026-11-25/item-64 2026-11-25/lce 2026-11-25/mmmem 2026-11-25/mxi-memicl 2026-11-25/notary 2026-11-25/reharness 2026-11-25/self-upgrading-embodied-agents 2026-11-25/sleep 2026-11-25/spatialcraft 2026-11-25/stun-bench 2026-11-25/toolsmith 2026-11-25/vise 2026-11-25/wactorz 2026-11-26/agnes-harness 2026-11-26/autorlbench-rl 2026-11-26/cogentic 2026-11-26/dualpm 2026-11-26/egse 2026-11-26/evolink-bench 2026-11-26/irtiqa 2026-11-26/item-39 2026-11-26/item-87 2026-11-26/knowledge-base-gradient-descent 2026-11-26/leto 2026-11-26/medskill-e 2026-11-26/metadecomp 2026-11-26/nightwatch 2026-11-26/p-fedskill 2026-11-26/partagent 2026-11-26/precept 2026-11-26/roboevo 2026-11-26/scalpel-and-brush 2026-11-26/sed 2026-11-26/sim 2026-11-26/skillsbench 2026-11-26/sports-agent 2026-11-26/vsft 2026-11-27/play2evolve 2026-11-28/autosft 2026-11-28/boundary-aware-policy-learning 2026-11-28/coevo-rsi -->
<!-- research-experience:end -->

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
