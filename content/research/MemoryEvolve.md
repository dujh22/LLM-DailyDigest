+++
title = 'MemoryEvolve'
proposer = '杜晋华'
since = '2026-08-30'
date = 2026-08-30T00:00:00+08:00
draft = false
toc = true
+++

# MemoryEvolve

> 研究方向：**记忆自进化**——让智能体自主构建、组织、巩固并持续演化长期记忆。

## 研究范畴

记忆自进化（memory self-evolution）以"记忆"为核心驱动，让模型 / 智能体在交互与任务执行中自主完成记忆的写入、检索、压缩、巩固、遗忘与重组，从而突破上下文窗口限制、支撑长周期任务与持续学习。本方向涵盖：智能体长期记忆架构（分层记忆 / 记忆操作系统）、情景记忆与语义记忆的组织与索引（含时序知识图谱）、记忆巩固与反思（reflection / consolidation）、参数化记忆与非参数化记忆的协同、记忆驱动的经验复用与技能沉淀。社区关注的核心问题包括：记忆的写入 / 淘汰策略如何自动学习而非人工规则、长期记忆如何抗噪声与防止错误记忆累积、记忆检索与推理如何深度耦合、多智能体 / 多会话间记忆如何共享与隔离，以及如何评测记忆系统在长周期任务上的真实收益。

## 研究挑战

- 记忆质量随时间漂移：错误、过时与冲突记忆的检测与修正。
- 写入 / 遗忘策略的自动化学习，避免记忆膨胀与检索退化。
- 记忆与推理的耦合：何时检索、检索什么、如何融合进当前决策。
- 长周期评测困难：缺少可复现、可量化记忆收益的基准。
- 隐私与安全：跨会话记忆的泄漏、污染与投毒风险。

## 自研项目

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
1. **决策效用选忆**：固定预算下应按记忆对后续决策的边际贡献筛选，而非仅看语义相似度或保存数量，并用反事实结果校准信用。
   - [XMind：跨记忆反事实复核](../../updates/2026-11-25/#xmind) · 2026-11-25
   - [ReHarness：结果驱动的经验反向修正](../../updates/2026-11-25/#reharness) · 2026-11-25
   - [Memanto：信息论相关性记忆排序](../../updates/2026-11-24/#memanto) · 2026-11-24
   - [F³：形适融经验利用](../../updates/2026-11-20/#item-76) · 2026-11-20
   - [自蒸馏记忆：按模型能力调节记忆量](../../updates/2026-11-20/#item-34) · 2026-11-20
   - [DriftGuard：因果归因式记忆漂移检测](../../updates/2026-11-20/#driftguard) · 2026-11-20
   - [RegimeCouncil：配对证据路由记忆冲突](../../updates/2026-11-18/#regimecouncil) · 2026-11-18
   - [Jetriever：效用驱动记忆检索](../../updates/2026-11-18/#jetriever) · 2026-11-18
   - [Dreaming：选择性记忆与离线纠错](../../updates/2026-11-17/#dreaming) · 2026-11-17
   - [AdMem：期望对齐的程序记忆](../../updates/2026-11-17/#admem) · 2026-11-17
   - [MemCredit：以决策效用优化长程 Web 智能体记忆](../../updates/2026-11-14/#memcredit-web) · 2026-11-14
   - [CoReMem：面向连续编程任务的成本内化记忆框架](../../updates/2026-11-14/#coremem) · 2026-11-14
   - [ACE-RL：基于经验交接强化学习的递归自我改进](../../updates/2026-11-14/#ace-rl) · 2026-11-14
2. **写入期结构化**：在写入时完成事件绑定、层级切分与跨模态对齐，比查询时再拼接松散片段更易获得低成本、可复用的证据。
   - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
   - [ReSpaceBench：跨重访空间记忆评测](../../updates/2026-11-24/#respacebench) · 2026-11-24
   - [NavTTT：导航条件式分层参数记忆](../../updates/2026-11-23/#navttt) · 2026-11-23
   - [STARK：事件作边的双图记忆](../../updates/2026-11-20/#stark) · 2026-11-20
   - [MEM-SQL：分层复用历史查询](../../updates/2026-11-17/#mem-sql) · 2026-11-17
   - [Looki 发布第一视角多模态模型系列 Loom](../../updates/2026-11-14/#looki-loom) · 2026-11-14
   - [浙大与联想提出 EM²Mem 事件中心多模态长期记忆方案](../../updates/2026-11-14/#em-mem) · 2026-11-14
3. **证据溯源与验真**：长期记忆应保留来源、时态、派生谱系和外部执行结果；修正须回溯源头并让冲突证据汇合，不能只改错误出现处。
   - [MMMem：任务感知多模态经验固化](../../updates/2026-11-25/#mmmem) · 2026-11-25
   - [lumimax：深度证据链知识网络](../../updates/2026-11-25/#lumimax) · 2026-11-25
   - [ExpGuard：经验风险预测与在线修复](../../updates/2026-11-25/#expguard) · 2026-11-25
   - [Epistemic Guard：收据绑定运行时验证](../../updates/2026-11-23/#epistemic-guard) · 2026-11-23
   - [MemDoctor：分阶段记忆归因修复](../../updates/2026-11-18/#memdoctor) · 2026-11-18
   - [多智能体记忆不一致：事实冲突流失定位](../../updates/2026-11-18/#item-69) · 2026-11-18
   - [Matrix with Steps：外部验真式双层记忆](../../updates/2026-11-17/#matrix-with-steps) · 2026-11-17
   - [CarryOn：源链接证据自适应保留](../../updates/2026-11-16/#carryon) · 2026-11-16
   - [DISCERN：写入时保留、读取时消解的持久化智能体记忆](../../updates/2026-11-14/#discern) · 2026-11-14
   - [世界仍保留错误时，清理智能体历史反而有害](../../updates/2026-11-13/#item-41) · 2026-11-13
4. **可恢复记忆压缩**：压缩应保留多分辨率索引并允许按需恢复原始证据；固定容量状态可承载长期信息，但需约束递归更新的一致性。
   - [Motion Mamba 2.0：持久记忆式长时控制](../../updates/2026-11-25/#motion-mamba-2-0) · 2026-11-25
   - [Integral DeltaNet：双状态自适应记忆](../../updates/2026-11-25/#integral-deltanet) · 2026-11-25
   - [EvoViM：递归自演化视觉程序](../../updates/2026-11-24/#evovim) · 2026-11-24
   - [Memory Tax：量化记忆重构损耗](../../updates/2026-11-23/#memory-tax) · 2026-11-23
   - [MemOnce：稀疏解码式可扩展记忆](../../updates/2026-11-23/#memonce) · 2026-11-23
   - [MemFolder：结构引导记忆折叠](../../updates/2026-11-20/#memfolder) · 2026-11-20
   - [GrepMem：无损免索引长期记忆](../../updates/2026-11-20/#grepmem) · 2026-11-20
   - [MoE-Context：按需分块上下文掩码](../../updates/2026-11-19/#moe-context) · 2026-11-19
   - [KV-LTM：会话KV缓存长期记忆](../../updates/2026-11-18/#kv-ltm-kv) · 2026-11-18
   - [RecMem：递归式推荐记忆压缩](../../updates/2026-11-16/#recmem) · 2026-11-16
   - [Folio：面向长程智能体的可恢复多分辨率上下文折叠](../../updates/2026-11-14/#folio) · 2026-11-14
   - [CoMem：面向选择性上下文压缩的对比记忆学习](../../updates/2026-11-14/#comem) · 2026-11-14
5. **版本感知更新**：记忆更新须显式管理版本、适用边界、强度与期限，淘汰旧值并隔离陈旧知识；局部失效优先局部修复和重验，避免整体重写。
   - [RoboLiveMem：动静态配对记忆评测](../../updates/2026-11-25/#robolivemem) · 2026-11-25
   - [MemMend：选择性记忆答案修订](../../updates/2026-11-20/#memmend) · 2026-11-20
   - [参数记忆：可控持久与衰减](../../updates/2026-11-20/#item-63) · 2026-11-20
   - [HabitusMem：信念式动态偏好记忆](../../updates/2026-11-20/#habitusmem) · 2026-11-20
   - [RegimeCouncil：配对证据路由记忆冲突](../../updates/2026-11-18/#regimecouncil) · 2026-11-18
   - [选择性维护：运行时修复过时技能](../../updates/2026-11-18/#item-33) · 2026-11-18
   - [Experience Rot：静默变更引发经验腐化](../../updates/2026-11-18/#experience-rot) · 2026-11-18
   - [StaleBench：隔离陈旧检索并量化修复成本](../../updates/2026-11-17/#stalebench) · 2026-11-17
   - [ReHarness：反向修订式持续学习](../../updates/2026-11-17/#reharness) · 2026-11-17
   - [场景记忆选择性更新](../../updates/2026-11-17/#item-85) · 2026-11-17
6. **技能化经验复用**：可复用经验应组织为带执行顺序、适用边界和验证证据的技能结构；仅召回文本不保证智能体会正确执行。
   - [SpatialCraft：经验技能双流自进化](../../updates/2026-11-25/#spatialcraft) · 2026-11-25
   - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
   - [HyperHarness：历史驱动的个性化脚手架生成](../../updates/2026-11-24/#hyperharness) · 2026-11-24
   - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
   - [StarTV-Agent：快慢双路工具编排](../../updates/2026-11-21/#startv-agent) · 2026-11-21
   - [F³：形适融经验利用](../../updates/2026-11-20/#item-76) · 2026-11-20
   - [Brain：会话驱动的个性化技能演化](../../updates/2026-11-20/#brain) · 2026-11-20
   - [OpenKAGE：知识共享式群体演化](../../updates/2026-11-19/#openkage) · 2026-11-19
   - [BRIDGE：极简检索记忆](../../updates/2026-11-18/#bridge) · 2026-11-18
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [MEM-SQL：分层复用历史查询](../../updates/2026-11-17/#mem-sql) · 2026-11-17
   - [HyperSkill：基于超图技能库演化的免训练全模态 GRPO](../../updates/2026-11-13/#hyperskill-grpo) · 2026-11-13
7. **情境分区防遗忘**：持续学习中先识别任务情境或环境动力学，再分区复用策略与成败轨迹，比单一策略覆盖所有环境更能隔离更新干扰。
   - [ENA：物理索引式专家记忆](../../updates/2026-11-18/#ena) · 2026-11-18
   - [R2A：成败记忆驱动在线适应](../../updates/2026-11-17/#r2a) · 2026-11-17
   - [SPIRE：基于情境推断与因果运动基元复用的具身持续学习](../../updates/2026-11-13/#spire) · 2026-11-13
8. **双形态记忆协同**：保真情景证据宜留在外部记忆，隐含规律可固化为潜在状态或模块化参数；两者分工可兼顾可审计性与固定推理成本。
   - [MMMem：任务感知多模态经验固化](../../updates/2026-11-25/#mmmem) · 2026-11-25
   - [VaW：视频编译为权重记忆](../../updates/2026-11-24/#vaw) · 2026-11-24
   - [MemT-1.0-Pro：记忆原生模型](../../updates/2026-11-24/#memt-1-0-pro) · 2026-11-24
   - [MemOnce：稀疏解码式可扩展记忆](../../updates/2026-11-23/#memonce) · 2026-11-23
   - [参数记忆：可控持久与衰减](../../updates/2026-11-20/#item-63) · 2026-11-20
   - [BiSpace：双空间解耦知识编辑](../../updates/2026-11-20/#bispace) · 2026-11-20
   - [KV-LTM：会话KV缓存长期记忆](../../updates/2026-11-18/#kv-ltm-kv) · 2026-11-18
   - [Microfitting：文档隔离式缓存适配](../../updates/2026-11-17/#microfitting) · 2026-11-17
   - [CLAM：单次前向权重记忆固化](../../updates/2026-11-17/#clam) · 2026-11-17
   - [Recursive SALM：基于持久潜在状态的预训练语言模型适配](../../updates/2026-11-14/#recursive-salm) · 2026-11-14
   - [PriorSplit：外部顺序记忆与在策略自蒸馏驱动的自进化 VLM 智能体](../../updates/2026-11-14/#priorsplit-vlm) · 2026-11-14
   - [MindMem：心理状态驱动的长期角色对话记忆](../../updates/2026-11-14/#mindmem) · 2026-11-14
9. **记忆策略自动优化**：写入、反思、压缩和检索策略可按任务增益联合学习、程序搜索或分别蒸馏；分训模块组合前须验证行为接口兼容性。
   - [独立蒸馏记忆检索策略](../../updates/2026-11-25/#item-105) · 2026-11-25
   - [EvoDisco：策略发现式记忆演化](../../updates/2026-11-18/#evodisco) · 2026-11-18
   - [MAPE：通过程序进化发现高效智能体记忆设计](../../updates/2026-11-14/#mape) · 2026-11-14
   - [ACE-RL：基于经验交接强化学习的递归自我改进](../../updates/2026-11-14/#ace-rl) · 2026-11-14
10. **成本内化决策**：记忆策略应联合优化成功率、步骤、词元和服务成本；同一环境内积累的经验可逐步形成比统一策略更有效的资源调度。
   - [DMC-5：双模型缓存感知压缩](../../updates/2026-11-25/#dmc-5) · 2026-11-25
   - [MemT-1.0-Pro：记忆原生模型](../../updates/2026-11-24/#memt-1-0-pro) · 2026-11-24
   - [HyperHarness：历史驱动的个性化脚手架生成](../../updates/2026-11-24/#hyperharness) · 2026-11-24
   - [Memory Tax：量化记忆重构损耗](../../updates/2026-11-23/#memory-tax) · 2026-11-23
   - [MemOnce：稀疏解码式可扩展记忆](../../updates/2026-11-23/#memonce) · 2026-11-23
   - [StarTV-Agent：快慢双路工具编排](../../updates/2026-11-21/#startv-agent) · 2026-11-21
   - [RAA：分辨率式记忆注意](../../updates/2026-11-20/#raa) · 2026-11-20
   - [MemMend：选择性记忆答案修订](../../updates/2026-11-20/#memmend) · 2026-11-20
   - [MemFolder：结构引导记忆折叠](../../updates/2026-11-20/#memfolder) · 2026-11-20
   - [KV-LTM：会话KV缓存长期记忆](../../updates/2026-11-18/#kv-ltm-kv) · 2026-11-18
   - [TokenEconomizer：仓库经验驱动降本](../../updates/2026-11-17/#tokeneconomizer) · 2026-11-17
   - [Folio：面向长程智能体的可恢复多分辨率上下文折叠](../../updates/2026-11-14/#folio) · 2026-11-14
   - [CoReMem：面向连续编程任务的成本内化记忆框架](../../updates/2026-11-14/#coremem) · 2026-11-14
11. **跨模型记忆接口**：将经验状态与宿主模型解耦，并记录适配边界和验证环境，可使长期记忆在模型更换后迁移而无需重建。
   - [Engram：异构调优的多阶段记忆](../../updates/2026-11-24/#engram) · 2026-11-24
   - [Memory Tax：量化记忆重构损耗](../../updates/2026-11-23/#memory-tax) · 2026-11-23
   - [OpenKAGE：知识共享式群体演化](../../updates/2026-11-19/#openkage) · 2026-11-19
   - [认知共生体：关系可迁移的终身增强](../../updates/2026-11-19/#item-1) · 2026-11-19
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [MIGRO：跨模型可移植的解耦长期记忆系统](../../updates/2026-11-13/#migro) · 2026-11-13
12. **评测链路校准**：记忆增益须用配对重复、朴素RAG基线及链路分解验证，并审计提示与评判器敏感性；单次总分无法区分运行方差、召回、压缩和使用误差。
   - [RoboLiveMem：动静态配对记忆评测](../../updates/2026-11-25/#robolivemem) · 2026-11-25
   - [Memory Tax：量化记忆重构损耗](../../updates/2026-11-23/#memory-tax) · 2026-11-23
   - [GroupAssistBench：群聊记忆使用评测](../../updates/2026-11-23/#groupassistbench) · 2026-11-23
   - [CompAct-Bench：工作上下文压缩评测](../../updates/2026-11-20/#compact-bench) · 2026-11-20
   - [ChronoDossier：长档案式时序记忆评测](../../updates/2026-11-20/#chronodossier) · 2026-11-20
   - [One Run Is Not Enough：配对校准记忆增益](../../updates/2026-11-17/#one-run-is-not-enough) · 2026-11-17
   - [LoCoMo：提示与评判器敏感性审计](../../updates/2026-11-17/#locomo) · 2026-11-17
   - [Conversation ESAA 中的智能体记忆整合：RRR 能与不能解释什么](../../updates/2026-11-14/#conversation-esaa-rrr) · 2026-11-14
13. **责任化记忆治理**：个人记忆系统除准确率外还需评测隐私、抗滥用、完整性、可撤回和用户控制；撤回须沿谱系清除派生提示、技能与学习状态并验证不可再用。
   - [MIMPA：协作记忆投毒](../../updates/2026-11-25/#mimpa) · 2026-11-25
   - [跨载体隐私记忆治理](../../updates/2026-11-23/#item-45) · 2026-11-23
   - [认知共生体：关系可迁移的终身增强](../../updates/2026-11-19/#item-1) · 2026-11-19
   - [Remembered as Brief：偏好记忆静默删减](../../updates/2026-11-18/#remembered-as-brief) · 2026-11-18
   - [持续在线个人智能：三模块持续闭环](../../updates/2026-11-17/#item-1) · 2026-11-17
   - [HEAMS：智能体记忆全责评测](../../updates/2026-11-17/#heams) · 2026-11-17
14. **状态证据分离**：长程任务应以紧凑结构保存可执行状态、独立寻址原始证据，并以续行能力而非行为模仿判定状态充分性；这比不可逆摘要更利于验真与恢复。
   - [紧凑状态抽象：递归程序压缩历史](../../updates/2026-11-25/#item-64) · 2026-11-25
   - [保留观测历史应对惯例复现](../../updates/2026-11-25/#item-117) · 2026-11-25
   - [DMC-5：双模型缓存感知压缩](../../updates/2026-11-25/#dmc-5) · 2026-11-25
   - [SKILL.state：结构化状态转移](../../updates/2026-11-24/#skill-state) · 2026-11-24
   - [HoH：双状态长程编码代理](../../updates/2026-11-24/#hoh) · 2026-11-24
   - [CompAct-Bench：工作上下文压缩评测](../../updates/2026-11-20/#compact-bench) · 2026-11-20
   - [SCH：状态证据分离式上下文交接](../../updates/2026-11-19/#sch) · 2026-11-19
15. **验收后再巩固**：失败反思或提炼规则不应直接固化；先用留出任务或真实执行验收，未通过则回滚隔离，可减少有害纠错累积。
   - [Notary门控回顾环：规则准入效用验证](../../updates/2026-11-25/#notary) · 2026-11-25
   - [ZhuLong-SE：执行轨迹驱动自进化](../../updates/2026-11-23/#zhulong-se) · 2026-11-23
   - [Epistemic Guard：收据绑定运行时验证](../../updates/2026-11-23/#epistemic-guard) · 2026-11-23
   - [ARISE：留出验证式记忆演化](../../updates/2026-11-19/#arise) · 2026-11-19
<!-- experience-seen: 2026-11-19/kra 2026-11-19/toaster 2026-11-20/clonact 2026-11-25/sleep -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [Letta (MemGPT)](https://github.com/letta-ai/letta) — 将操作系统分页思想引入 LLM 记忆管理的智能体记忆框架
- [mem0](https://github.com/mem0ai/mem0) — 面向生产的智能体可扩展长期记忆层
- [Graphiti (Zep)](https://github.com/getzep/graphiti) — 基于时序知识图谱的智能体记忆
- [A-mem](https://github.com/agiresearch/A-mem) — 受 Zettelkasten 启发的智能体自组织记忆系统
- [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) — 受海马体记忆索引理论启发的长期记忆检索框架
- [MemOS](https://github.com/MemTensor/MemOS) — 把记忆作为一等资源调度的"记忆操作系统"

**论文**
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 分层虚拟上下文与记忆分页管理
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 记忆流 + 反思 + 检索的经典智能体记忆架构
- [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 基于遗忘曲线的长期记忆更新机制
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — 动态链接与演化的自组织智能体记忆
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 可扩展记忆抽取与更新管线
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — LLM 智能体记忆机制综述
