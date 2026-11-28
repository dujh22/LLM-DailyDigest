+++
title = 'SystemEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# SystemEvolve

> 研究方向：**AI 系统级自进化**——不止改模型权重，而是让 Agent 系统的架构、工作流、工具链与自身代码成为被进化的对象。

## 研究范畴

系统级自进化（system-level self-evolution）把优化对象从单个模型扩展到整个 AI 系统：Agent 的编排结构、工作流图、提示与工具配置、运行时 harness，乃至系统自身的源代码，都可以由系统自己提出修改、实验验证并择优保留，形成达尔文-哥德尔机式的开放式演化。本方向涵盖：自动化 Agent 系统设计（ADAS / AFlow 类元搜索）、以文本或执行轨迹为"梯度"的生成式优化（TextGrad / Trace / DSPy）、自指式递归自改进框架（Gödel Agent、Darwin Gödel Machine）、程序进化型发现系统（AlphaEvolve / ShinkaEvolve / OpenEvolve），以及系统演化的档案管理、分支选择与回滚机制。社区关注的核心问题包括：系统级改动的搜索空间巨大且不可微，如何高效评估与择优；进化出的系统是否只在基准上过拟合；自修改系统的可解释性、可审计性与安全边界；以及如何让"改进改进机制本身"的元层也被纳入闭环而不失控。

## 研究挑战

- 搜索空间组合爆炸，每次评估都需真实运行，样本效率低、算力成本高。
- 评估基准被进化过程"攻陷"（目标作弊、基准过拟合）。
- 自修改代码的正确性与安全性：错误改动可能破坏系统自身。
- 演化档案（archive）管理：多样性保持、分支选择与回滚。
- 可解释与可审计：难以追溯系统为何演化成当前形态。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，系统级自进化是其"自进化机制"综述的核心层次之一。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，系统自重写 / 自修复相关工作均在收录范围。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站本身是一个"爬取 → 抽取 → 归并 → 推荐"的多 Agent 流水线，是系统自进化方法的试验床。

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
1. **冻结模型进化外层**：模型权重冻结时，优先改写提示、工具、记忆与控制流；外置脚手架成本低且易回滚，但模型—框架耦合需经跨模型重验。
   - [Harness Learning：反馈驱动的框架元学习](../../updates/2026-11-26/#harness-learning) · 2026-11-26
   - [AGL-SKILL：编码智能体自优化技能](../../updates/2026-11-25/#agl-skill) · 2026-11-25
   - [智能体脚手架演化：冻结策略领域适配](../../updates/2026-11-20/#item-60) · 2026-11-20
   - [Harness：模块化自改运行框架](../../updates/2026-11-20/#harness) · 2026-11-20
   - [自改进智能体脚手架：门控模块化演化](../../updates/2026-11-18/#item-38) · 2026-11-18
   - [RiseHarness：双轨迹驱动脚手架进化](../../updates/2026-11-17/#riseharness) · 2026-11-17
   - [HarnessDev：自主执行框架演化](../../updates/2026-11-17/#harnessdev) · 2026-11-17
   - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
   - [VbD：无外部反馈下执行与评估协同演化](../../updates/2026-11-13/#vbd) · 2026-11-13
   - [EvoX：将智能体脚手架重构为运行时策略](../../updates/2026-11-13/#evox) · 2026-11-13
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [Enmo Safety：现成语言模型的外置非侵入式安全监督](../../updates/2026-11-12/#enmo-safety) · 2026-11-12
   - [EmoHarness：元脚手架演化增强多模态情绪理解](../../updates/2026-11-12/#emoharness) · 2026-11-12
   - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [EnvOpt：自动优化智能体的固定环境](../../updates/2026-11-06/#envopt) · 2026-11-06
   - [VERSE：面向智能体 Harness 的可验证自进化优化器](../../updates/2026-11-05/#verse-harness) · 2026-11-05
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [HarnessPro：兼顾性能与成本的智能体脚手架自进化框架](../../updates/2026-11-05/#harnesspro) · 2026-11-05
   - [HarnessFlow：MCTS 引导的 LLM 智能体脚手架优化](../../updates/2026-11-05/#harnessflow-mcts-llm) · 2026-11-05
   - [KARMA：工业广告智能体的免训练知识原子化脚手架演化](../../updates/2026-10-30/#karma) · 2026-10-30
   - [Harness 自进化研究进展与趋势盘点](../../updates/2026-10-30/#harness) · 2026-10-30
   - [CMU开源Hermit：统一Harness层RSI与持续学习框架](../../updates/2026-10-30/#cmu-hermit-harness-rsi) · 2026-10-30
   - [Evo²：冻结执行器权重，协同进化工作流与演化策略](../../updates/2026-10-29/#evo) · 2026-10-29
2. **优化器同步进化**：不要只搜索任务工作流；将提议策略、反思器和搜索脚手架也纳入迭代，并维持模型与候选的机制多样性，减少局部最优和改进停滞。
   - [MOSAIC：记忆组织式反模仿搜索](../../updates/2026-11-25/#mosaic) · 2026-11-25
   - [MetaRSI/RSI²：双轴元递归自改进](../../updates/2026-11-24/#metarsi-rsi) · 2026-11-24
   - [DiVE：小模型多样性递归改进](../../updates/2026-11-24/#dive) · 2026-11-24
   - [MedicalRSI：临床模型与脚手架协同演化](../../updates/2026-11-23/#medicalrsi) · 2026-11-23
   - [Meta-RTL：演化式RTL优化脚手架](../../updates/2026-11-20/#meta-rtl-rtl) · 2026-11-20
   - [自我改进分支混合：动态目标与路由组合](../../updates/2026-11-18/#item-5) · 2026-11-18
   - [EvoDisco：策略发现式记忆演化](../../updates/2026-11-18/#evodisco) · 2026-11-18
   - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
   - [RSI综述：四组件七步自进化框架](../../updates/2026-11-16/#rsi) · 2026-11-16
   - [HEMO：面向多目标组合优化的脚手架自演化](../../updates/2026-10-30/#hemo) · 2026-10-30
   - [Evo²：冻结执行器权重，协同进化工作流与演化策略](../../updates/2026-10-29/#evo) · 2026-10-29
3. **任务条件化编排**：同质企业SOP优先单智能体；异构任务再动态合成团队，并以失败轨迹更新组织规则。组件交接须落在接管方可控边界内，避免错误状态切换。
   - [Boundary-Aware Policy Learning：策略交接边界塑形](../../updates/2026-11-28/#boundary-aware-policy-learning) · 2026-11-28
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [企业级 SOP 中智能体架构的成本—成功率权衡评测](../../updates/2026-11-12/#sop) · 2026-11-12
   - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
   - [IAPO：面向高阶交互的多智能体编排策略优化](../../updates/2026-11-08/#iapo) · 2026-11-08
   - [SeaFlow：基于语义任务分解的自演化智能体工作流](../../updates/2026-11-03/#seaflow) · 2026-11-03
   - [EvoTeam：通过团队演化增强多智能体协作](../../updates/2026-10-30/#evoteam) · 2026-10-30
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
   - [DynaFlow：学习自由形式的多智能体编排](../../updates/2026-10-29/#dynaflow) · 2026-10-29
4. **执行反馈闭环**：代码与基础设施进化应以真实执行、硬件约束和领域约束作适应度与硬门槛；扩大并行搜索前先扩展可靠测量吞吐。
   - [TabbyML多智能体团队：契约驱动系统优化](../../updates/2026-11-27/#tabbyml) · 2026-11-27
   - [位置跳跃蒸馏：短训长服稀疏索引](../../updates/2026-11-25/#item-150) · 2026-11-25
   - [Hopper 4-bit KV解码：访存计算重叠](../../updates/2026-11-25/#hopper-4-bit-kv) · 2026-11-25
   - [EDAGoat：EDA约束验证式GPU优化](../../updates/2026-11-23/#edagoat-eda-gpu) · 2026-11-23
   - [Performance Factory：Codex自动修复性能回归](../../updates/2026-11-20/#performance-factory-codex) · 2026-11-20
   - [DeltaHarness：执行反馈式脚手架演化](../../updates/2026-11-18/#deltaharness) · 2026-11-18
   - [Claude Docs：混沌循环压测自修复](../../updates/2026-11-18/#claude-docs) · 2026-11-18
   - [Mobile AI Factory：手机感知式模型定制](../../updates/2026-11-17/#mobile-ai-factory) · 2026-11-17
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [AscendGYM：成本感知算子优化评测](../../updates/2026-11-16/#ascendgym) · 2026-11-16
   - [KernelMosaic：CUDA Kernel 生成数据集与智能体框架](../../updates/2026-11-13/#kernelmosaic-cuda-kernel) · 2026-11-13
   - [面向自主 RTL 与综合优化的基准和自改进智能体](../../updates/2026-11-12/#rtl) · 2026-11-12
   - [NCCL-BOT：用在线多臂老虎机闭环优化 NCCL 成本决策](../../updates/2026-11-12/#nccl-bot-nccl) · 2026-11-12
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [百度披露 ERNIE Evolve 递归自我改进进展，已用于文心 5.5 Flash 研发](../../updates/2026-11-12/#ernie-evolve-5-5-flash) · 2026-11-12
   - [EngineAgent：感知推理栈层级与硬件能力的端侧推理引擎智能体](../../updates/2026-11-12/#engineagent) · 2026-11-12
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [ModelBlaster：跨模型、内核与硬件后端的学习增强优化智能体](../../updates/2026-11-06/#modelblaster) · 2026-11-06
   - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
   - [IQuestRT 推理提速近 3 倍，Agent 两周反超人工精调](../../updates/2026-11-06/#iquestrt-3-agent) · 2026-11-06
   - [ForgeKernel零样本自进化生成算子，性能超越DeepSeek FlashMLA 9.8%](../../updates/2026-10-31/#forgekernel-deepseek-flashmla-9-8) · 2026-10-31
   - [Formulaic：智能体驱动的 AI 基础设施软硬件协同设计](../../updates/2026-10-30/#formulaic-ai) · 2026-10-30
   - [ForgeKernel 登顶华为与英伟达算子评测榜](../../updates/2026-10-29/#forgekernel) · 2026-10-29
   - [无问芯穹算子优化Agent斩获SOL-ExecBench 88项第一](../../updates/2026-10-29/#agent-sol-execbench-88) · 2026-10-29
5. **高分辨率分层评估**：评测分辨率不足时，扩充候选只会放大噪声；先提升信号可检测性，再分层筛选，并按质量—成本保留帕累托前沿。
   - [HarnessPro：成本感知式脚手架优化](../../updates/2026-11-25/#harnesspro) · 2026-11-25
   - [Resolution Hypothesis：评测分辨率瓶颈](../../updates/2026-11-19/#resolution-hypothesis) · 2026-11-19
   - [QDA：智能体闭环量化设计](../../updates/2026-11-19/#qda) · 2026-11-19
   - [ELITE：无评估机制整合](../../updates/2026-11-18/#elite) · 2026-11-18
   - [AscendGYM：成本感知算子优化评测](../../updates/2026-11-16/#ascendgym) · 2026-11-16
   - [AutoQS：大语言模型自动设计量化策略](../../updates/2026-11-12/#autoqs) · 2026-11-12
   - [SwarmEvolve：潜空间智能体群的进化发现与优化](../../updates/2026-11-08/#swarmevolve) · 2026-11-08
   - [ParetoSaddler：面向质量与成本的智能体脚手架帕累托优化](../../updates/2026-11-06/#paretosaddler) · 2026-11-06
   - [HarnessPro：兼顾性能与成本的智能体脚手架自进化框架](../../updates/2026-11-05/#harnesspro) · 2026-11-05
   - [HarnessFlow：MCTS 引导的 LLM 智能体脚手架优化](../../updates/2026-11-05/#harnessflow-mcts-llm) · 2026-11-05
   - [System-1 门控 System-2：以条件交互提升 AGI 扩展效率](../../updates/2026-10-30/#system-1-system-2-agi) · 2026-10-30
   - [LLM 智能体脚手架演化中的评估预算分配](../../updates/2026-10-29/#llm-2) · 2026-10-29
   - [批处理反思优化循环：并行候选让 GEPA 更快更优](../../updates/2026-10-29/#gepa) · 2026-10-29
6. **验证随搜索加严**：搜索预算越大，指标漏洞、偶然收益与遗忘越易放大；先监测可修复故障，再用候选冻结、重放、独立审计和旧任务回归设置晋升门。
   - [Sports Agent：反馈驱动闭环自进化](../../updates/2026-11-26/#sports-agent) · 2026-11-26
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [Semantic PID-RSI：语义PID控制自改进](../../updates/2026-11-24/#semantic-pid-rsi-pid) · 2026-11-24
   - [MASSys：服务基底敏感性评测](../../updates/2026-11-24/#massys) · 2026-11-24
   - [智能体恢复审计：公开报告证据评估](../../updates/2026-11-24/#item-60) · 2026-11-24
   - [Epistemic Guard：收据绑定运行时验证](../../updates/2026-11-23/#epistemic-guard) · 2026-11-23
   - [OpenAI RSI：智能体驱动研发闭环](../../updates/2026-11-20/#openai-rsi) · 2026-11-20
   - [Weight Space Programming：低位痕迹引导权重修复](../../updates/2026-11-19/#weight-space-programming) · 2026-11-19
   - [GUARD：后悔引导脚手架演化](../../updates/2026-11-19/#guard) · 2026-11-19
   - [Data to Valves：端侧自学习暖通控制](../../updates/2026-11-19/#data-to-valves) · 2026-11-19
   - [自改进智能体脚手架：门控模块化演化](../../updates/2026-11-18/#item-38) · 2026-11-18
   - [Terminal-RSI：递归改写与策略精炼](../../updates/2026-11-17/#terminal-rsi) · 2026-11-17
   - [SPLICE：分块约束式提示演化](../../updates/2026-11-17/#splice) · 2026-11-17
   - [HarnessDev：自主执行框架演化](../../updates/2026-11-17/#harnessdev) · 2026-11-17
   - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
   - [自主智能体自生成更新的证据治理采纳框架 EGE](../../updates/2026-11-14/#ege) · 2026-11-14
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [AutoAssumption：搜索算法假设以发现 ML 系统新算法](../../updates/2026-11-13/#autoassumption-ml) · 2026-11-13
   - [WorkflowArena：可执行多智能体工作流编排评测基准](../../updates/2026-11-12/#workflowarena) · 2026-11-12
   - [TRUST：具备统计保证的可信递归自我改进](../../updates/2026-11-12/#trust) · 2026-11-12
   - [AI 智能体自主优化原子模拟数值算法](../../updates/2026-11-12/#item-94) · 2026-11-12
   - [推理模型的推断：评测与服务实践经验](../../updates/2026-11-12/#item-148) · 2026-11-12
   - [Flex-RSI：前沿智能体递归自我改进评测基准](../../updates/2026-11-12/#flex-rsi) · 2026-11-12
   - [Enmo Safety：现成语言模型的外置非侵入式安全监督](../../updates/2026-11-12/#enmo-safety) · 2026-11-12
   - [EmoHarness：元脚手架演化增强多模态情绪理解](../../updates/2026-11-12/#emoharness) · 2026-11-12
   - [bf16 循环状态舍入导致混合推理模型过度思考](../../updates/2026-11-12/#bf16) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [编程智能体能否在持续演化中避免遗忘？](../../updates/2026-11-06/#item-94) · 2026-11-06
   - [VERSE：面向智能体 Harness 的可验证自进化优化器](../../updates/2026-11-05/#verse-harness) · 2026-11-05
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [RSI 系统优化 Agent 的 Reward Hacking 与验证边界](../../updates/2026-11-04/#rsi-agent-reward-hacking) · 2026-11-04
   - [HarnessEvolve：基于参考轨迹的可靠智能体自我进化](../../updates/2026-11-02/#harnessevolve) · 2026-11-02
7. **评判准则协同演化**：将提案、治理与评判置于独立边界；评判器可持续演化，但须以验证过的用户需求、类型契约和留出任务锚定真实目标。
   - [TabbyML多智能体团队：契约驱动系统优化](../../updates/2026-11-27/#tabbyml) · 2026-11-27
   - [MetaRSI/RSI²：双轴元递归自改进](../../updates/2026-11-24/#metarsi-rsi) · 2026-11-24
   - [AppSci-Bench：端到端智能体构建评测](../../updates/2026-11-20/#appsci-bench) · 2026-11-20
   - [AHE-Beta：需求中心式脚手架演化](../../updates/2026-11-20/#ahe-beta) · 2026-11-20
   - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
   - [VbD：无外部反馈下执行与评估协同演化](../../updates/2026-11-13/#vbd) · 2026-11-13
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [Veritas：面向智能体任务的自动验证器生成框架](../../updates/2026-11-12/#veritas) · 2026-11-12
   - [RSI 系统优化 Agent 的 Reward Hacking 与验证边界](../../updates/2026-11-04/#rsi-agent-reward-hacking) · 2026-11-04
   - [RuHarness：评判准则与智能体脚手架协同演化](../../updates/2026-10-29/#ruharness) · 2026-10-29
8. **证据归因式修复**：结合成败轨迹、工具实现与反事实检验，把反馈归因到首个偏离点或具体开发决策；局部修复比整段反思更易控制副作用。
   - [TransHarness：可迁移脚手架演化](../../updates/2026-11-26/#transharness) · 2026-11-26
   - [VISE：工具实现反馈驱动技能演化](../../updates/2026-11-25/#vise) · 2026-11-25
   - [LeanNeXt：假设驱动架构发现](../../updates/2026-11-25/#leannext) · 2026-11-25
   - [AutoSECO：可迁移求解技能演化](../../updates/2026-11-25/#autoseco) · 2026-11-25
   - [RoHa-SGG：根因引导式脚手架优化](../../updates/2026-11-23/#roha-sgg) · 2026-11-23
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [GUARD：后悔引导脚手架演化](../../updates/2026-11-19/#guard) · 2026-11-19
   - [GRAFT：执行证据引导遗传重组](../../updates/2026-11-19/#graft) · 2026-11-19
   - [RiseHarness：双轨迹驱动脚手架进化](../../updates/2026-11-17/#riseharness) · 2026-11-17
   - [HarnessEvolve：基于参考轨迹的可靠智能体自我进化](../../updates/2026-11-02/#harnessevolve) · 2026-11-02
9. **持久状态促进迁移**：跨轮次保存结构化状态、修改理由、来源与适用边界，并分离不可变全局记录和决策视图；避免完整历史造成成本与语义漂移。
   - [SIM：经验记忆驱动持续改进](../../updates/2026-11-26/#sim) · 2026-11-26
   - [PRECEPT：失误驱动的安全原则演化](../../updates/2026-11-26/#precept) · 2026-11-26
   - [HoMe：评测驱动的记忆脚手架优化](../../updates/2026-11-26/#home) · 2026-11-26
   - [NoeVera：证据演化式配置搜索](../../updates/2026-11-25/#noevera) · 2026-11-25
   - [Motion Mamba 2.0：持久记忆式长时控制](../../updates/2026-11-25/#motion-mamba-2-0) · 2026-11-25
   - [Harness2：跨任务框架优化经验库](../../updates/2026-11-25/#harness2) · 2026-11-25
   - [DMC-5：双模型缓存感知压缩](../../updates/2026-11-25/#dmc-5) · 2026-11-25
   - [SKILL.state：结构化状态转移](../../updates/2026-11-24/#skill-state) · 2026-11-24
   - [Agnes Harness：双系统决策与双层自进化](../../updates/2026-11-20/#agnes-harness) · 2026-11-20
   - [EvoDisco：策略发现式记忆演化](../../updates/2026-11-18/#evodisco) · 2026-11-18
   - [TokenEconomizer：仓库经验驱动降本](../../updates/2026-11-17/#tokeneconomizer) · 2026-11-17
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [RSI综述：四组件七步自进化框架](../../updates/2026-11-16/#rsi) · 2026-11-16
   - [MAPE：通过程序进化发现高效智能体记忆设计](../../updates/2026-11-14/#mape) · 2026-11-14
   - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [GEAR：Scikit-learn 式模块化 RSI 框架推动 Agent 持续进化](../../updates/2026-11-12/#gear-scikit-learn-rsi-agent) · 2026-11-12
   - [EvolveNet：协作式 Harness 演化推动智能体自我改进](../../updates/2026-11-12/#evolvenet-harness) · 2026-11-12
   - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
   - [QRAE：面向深度搜索智能体的查询相关注意力熵上下文压缩](../../updates/2026-11-08/#qrae) · 2026-11-08
   - [Strategist：用智能体演化推理策略](../../updates/2026-11-06/#strategist) · 2026-11-06
   - [ModelBlaster：跨模型、内核与硬件后端的学习增强优化智能体](../../updates/2026-11-06/#modelblaster) · 2026-11-06
   - [Meta²：为长程智能体在线脚手架演化预计算可复用知识](../../updates/2026-11-06/#meta) · 2026-11-06
   - [EvoGroup：面向共享上下文群体智能体的自演化脚手架](../../updates/2026-11-06/#evogroup) · 2026-11-06
   - [CoworkOS：面向真实世界自动化的长程智能体协作框架](../../updates/2026-11-04/#coworkos) · 2026-11-04
   - [MoLRSI：面向分子发现的递归自我改进智能体](../../updates/2026-10-30/#molrsi) · 2026-10-30
   - [HEMO：面向多目标组合优化的脚手架自演化](../../updates/2026-10-30/#hemo) · 2026-10-30
   - [EvoTeam：通过团队演化增强多智能体协作](../../updates/2026-10-30/#evoteam) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
10. **能力课程驱动进化**：递归改进应主动生成可验证环境或选择当前可学习任务，让失败逐步内化为技能，而非只在固定基准上反复搜索。
    - [R²Orch：通过技能内化与自博弈实现智能体编排的递归自我改进](../../updates/2026-11-03/#r-orch) · 2026-11-03
    - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
11. **多层协同进化**：规划、执行、工作流、模型结构、关键权重与记忆相互耦合时，应联合优化多个层级；只改提示或单一模块易受系统瓶颈限制。
    - [Kolpona：无梯度神经元编程](../../updates/2026-11-28/#kolpona) · 2026-11-28
    - [RoboEvo²：脚手架策略协同进化](../../updates/2026-11-26/#roboevo) · 2026-11-26
    - [Weight Coding：智能体直接编辑模型权重](../../updates/2026-11-25/#weight-coding) · 2026-11-25
    - [HookEvo：协同插件演化](../../updates/2026-11-23/#hookevo) · 2026-11-23
    - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
    - [Evo²：权重与Harness协同进化](../../updates/2026-11-20/#evo-harness) · 2026-11-20
    - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
    - [FastFrames：轻量组件实现交互视频生成](../../updates/2026-11-19/#fastframes) · 2026-11-19
    - [WeVisForensics：自演化多模态取证](../../updates/2026-11-18/#wevisforensics) · 2026-11-18
    - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
    - [ModHarness-RL：可学习演化脚手架](../../updates/2026-11-16/#modharness-rl) · 2026-11-16
    - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
    - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
    - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
    - [JoMoHa：强化学习驱动的模型—脚手架联合优化](../../updates/2026-11-12/#jomoha) · 2026-11-12
    - [机制干预：AI动态改写Transformer架构实现自我改进](../../updates/2026-11-12/#ai-transformer) · 2026-11-12
    - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
    - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
    - [MoLRSI：面向分子发现的递归自我改进智能体](../../updates/2026-10-30/#molrsi) · 2026-10-30
12. **代码化工作流**：将高频决策沉淀为带适用条件的可执行子程序或工具资产；先用契约和沙箱验证依赖，可提升复用、审计与组合可靠性。
    - [ToolSmith：自动生成可复用工具](../../updates/2026-11-25/#toolsmith) · 2026-11-25
    - [AnyS1：技能编译式快速决策](../../updates/2026-11-19/#anys1) · 2026-11-19
    - [Code Mode：脚本化工具编排](../../updates/2026-11-18/#code-mode) · 2026-11-18
    - [SPLICE：分块约束式提示演化](../../updates/2026-11-17/#splice) · 2026-11-17
    - [MetaAct：可执行动作约束自演化](../../updates/2026-11-17/#metaact) · 2026-11-17
    - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
    - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
    - [腾讯混元发布终端智能体递归自我改进框架 Terminal-RSI](../../updates/2026-11-12/#terminal-rsi) · 2026-11-12
    - [Synapse-Control：以轻量运行时控制激活智能体经验](../../updates/2026-11-12/#synapse-control) · 2026-11-12
    - [面向自主 RTL 与综合优化的基准和自改进智能体](../../updates/2026-11-12/#rtl) · 2026-11-12
    - [机制干预：AI动态改写Transformer架构实现自我改进](../../updates/2026-11-12/#ai-transformer) · 2026-11-12
    - [Strategist：用智能体演化推理策略](../../updates/2026-11-06/#strategist) · 2026-11-06
    - [面向 LLM 智能体安全的累积式可审计护栏工具演化](../../updates/2026-11-06/#llm-3) · 2026-11-06
    - [LIBRA：程序化归纳可执行工具库](../../updates/2026-11-06/#libra) · 2026-11-06
    - [SeaFlow：基于语义任务分解的自演化智能体工作流](../../updates/2026-11-03/#seaflow) · 2026-11-03
    - [LangChain 开源设计智能体 Content Studio 的 harness](../../updates/2026-10-29/#langchain-content-studio-harness) · 2026-10-29
13. **长时运行系统基座**：持续在线的自进化智能体需要持久运行时、故障隔离、状态迁移、最小权限授权、变更审查、自动验收、看门狗自愈与人工兜底，不能依赖整系统重启。
    - [dots：常驻智能体自建系统](../../updates/2026-11-26/#dots) · 2026-11-26
    - [Wactorz：自编写边缘智能体运行时](../../updates/2026-11-25/#wactorz) · 2026-11-25
    - [SKILL.state：结构化状态转移](../../updates/2026-11-24/#skill-state) · 2026-11-24
    - [ClonAct：无路由上下文虚拟化](../../updates/2026-11-20/#clonact) · 2026-11-20
    - [SCH：状态证据分离式上下文交接](../../updates/2026-11-19/#sch) · 2026-11-19
    - [Data to Valves：端侧自学习暖通控制](../../updates/2026-11-19/#data-to-valves) · 2026-11-19
    - [Claude Docs：混沌循环压测自修复](../../updates/2026-11-18/#claude-docs) · 2026-11-18
    - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
    - [Folio：面向长程智能体的可恢复多分辨率上下文折叠](../../updates/2026-11-14/#folio) · 2026-11-14
    - [快慢双环：长程智能体部署的控制论监督框架](../../updates/2026-11-12/#item-210) · 2026-11-12
    - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
    - [CoworkOS：面向真实世界自动化的长程智能体协作框架](../../updates/2026-11-04/#coworkos) · 2026-11-04
    - [LobeHub 的 Super-agent 组织协作实验](../../updates/2026-11-02/#lobehub-super-agent) · 2026-11-02
    - [DeepSeek提出下一代 Super-agent Harness 架构](../../updates/2026-11-02/#deepseek-super-agent-harness) · 2026-11-02
14. **条件化资源路由**：按任务阶段、不确定性、中间状态与上下文距离门控模型、推理、工具和服务资源；低延迟交互可预计算候选动作并缩小提交粒度，但须限制分支成本。
    - [Yggdrasil：树路由循环专家](../../updates/2026-11-28/#yggdrasil) · 2026-11-28
    - [ShowNow：细粒度推测式流生成](../../updates/2026-11-28/#shownow) · 2026-11-28
    - [AdaptRouter：演化任务自适应路由](../../updates/2026-11-28/#adaptrouter) · 2026-11-28
    - [MoLT：KV记忆式循环复用](../../updates/2026-11-27/#molt-kv) · 2026-11-27
    - [模型自主上下文管理：按需压缩与缓存复用](../../updates/2026-11-26/#item-87) · 2026-11-26
    - [DFly2：共享目标稀疏性的推测解码](../../updates/2026-11-26/#dfly2) · 2026-11-26
    - [Prefill1：固定前缀单词元判决](../../updates/2026-11-25/#prefill1) · 2026-11-25
    - [NFA：近远分区稀疏检索](../../updates/2026-11-25/#nfa) · 2026-11-25
    - [层级执行控制：中间状态驱动计算分配](../../updates/2026-11-25/#item-128) · 2026-11-25
    - [RefineKV：误差界驱动的KV缓存压缩](../../updates/2026-11-24/#refinekv-kv) · 2026-11-24
    - [DisSparse：流水化Top-p稀疏注意力](../../updates/2026-11-24/#dissparse-top-p) · 2026-11-24
    - [Declarative Attention：自主声明注意力范围](../../updates/2026-11-24/#declarative-attention) · 2026-11-24
    - [Turnout：自适应注意力切换](../../updates/2026-11-23/#turnout) · 2026-11-23
    - [Contexture：工具感知式上下文驱逐](../../updates/2026-11-23/#contexture) · 2026-11-23
    - [RoCoKV：置信冗余感知缓存压缩](../../updates/2026-11-20/#rocokv) · 2026-11-20
    - [LAQ：潜变量感知四比特量化](../../updates/2026-11-20/#laq) · 2026-11-20
    - [FrontierReplay：无切分精确前缀缓存](../../updates/2026-11-20/#frontierreplay) · 2026-11-20
    - [Vanguard：截图感知式草稿判别](../../updates/2026-11-19/#vanguard) · 2026-11-19
    - [MoE-Context：按需分块上下文掩码](../../updates/2026-11-19/#moe-context) · 2026-11-19
    - [AnyS1：技能编译式快速决策](../../updates/2026-11-19/#anys1) · 2026-11-19
    - [JevRSI：递归改进决策脚手架](../../updates/2026-11-18/#jevrsi) · 2026-11-18
    - [TokenEconomizer：仓库经验驱动降本](../../updates/2026-11-17/#tokeneconomizer) · 2026-11-17
    - [LuthorSQL：单遍置信路由](../../updates/2026-11-16/#luthorsql) · 2026-11-16
    - [Callo：失效KV投机解码](../../updates/2026-11-16/#callo-kv) · 2026-11-16
    - [Gemini 4 Hydrogen：高效模型与动态路由](../../updates/2026-11-15/#gemini-4-hydrogen) · 2026-11-15
    - [通过自适应计算将 LLM 转化为高效 System One 决策模型](../../updates/2026-11-14/#llm-system-one) · 2026-11-14
    - [小语言模型能力路由：容量与提示优化对质量和效率的影响](../../updates/2026-11-14/#item-30) · 2026-11-14
    - [Folio：面向长程智能体的可恢复多分辨率上下文折叠](../../updates/2026-11-14/#folio) · 2026-11-14
    - [Ballad：基于多臂老虎机的自动启发式发现模型路由](../../updates/2026-11-14/#ballad) · 2026-11-14
    - [SparseRead：面向 AI 智能体的高效稀疏读取层](../../updates/2026-11-13/#sparseread-ai) · 2026-11-13
    - [PISA-E：面向提示自适应与成本感知推理的集成路由](../../updates/2026-11-13/#pisa-e) · 2026-11-13
    - [静态图 NPU 多模型智能体工作流中的 KV 缓存恢复与重计算](../../updates/2026-11-13/#npu-kv) · 2026-11-13
    - [Evolving Infra：面向智能体负载的自适应 LLM 服务](../../updates/2026-11-13/#evolving-infra-llm) · 2026-11-13
    - [按需精度：不确定解码步骤动态升至 8-bit](../../updates/2026-11-13/#8-bit) · 2026-11-13
    - [WAAC：面向工作流的智能体轨迹压缩](../../updates/2026-11-12/#waac) · 2026-11-12
    - [Think or Remember：智能体推理中的思考与记忆成本交换率](../../updates/2026-11-12/#think-or-remember) · 2026-11-12
    - [Synapse-Control：以轻量运行时控制激活智能体经验](../../updates/2026-11-12/#synapse-control) · 2026-11-12
    - [Scout 路由：用小模型预填充预测任务成功率与 Token 成本](../../updates/2026-11-12/#scout-token) · 2026-11-12
    - [OpenRouter 实测 MCP、CLI 与 Skills 的上下文 Token 成本](../../updates/2026-11-12/#openrouter-mcp-cli-skills-token) · 2026-11-12
    - [QRAE：面向深度搜索智能体的查询相关注意力熵上下文压缩](../../updates/2026-11-08/#qrae) · 2026-11-08
    - [PACT：预填充到自回归的跨模型迁移](../../updates/2026-11-08/#pact) · 2026-11-08
    - [HST：混合线性注意力 LLM 的跨模型状态移交](../../updates/2026-11-08/#hst-llm) · 2026-11-08
    - [Route Anything：通用人工智能系统的模型与策略路由](../../updates/2026-11-05/#route-anything) · 2026-11-05
    - [REA：异步脑-小脑控制的路由式具身智能体运行时](../../updates/2026-11-03/#rea) · 2026-11-03
    - [实时全双工语音模型的后训练专家路由](../../updates/2026-11-03/#item-41) · 2026-11-03
    - [System-1 门控 System-2：以条件交互提升 AGI 扩展效率](../../updates/2026-10-30/#system-1-system-2-agi) · 2026-10-30
15. **高成本流程局部闭环**：预训练、科学计算等高成本流程不宜整链试错；用可独立验收的局部闭环和经校准的精度—性能预测替代目标规模反复执行。
    - [MakoBORN：前瞻式量化程序合成](../../updates/2026-11-19/#makoborn) · 2026-11-19
    - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
    - [801-30B：将 RSI 引入前沿预训练](../../updates/2026-11-05/#801-30b-rsi) · 2026-11-05
<!-- experience-seen: 2026-11-23/coevobench 2026-11-23/contexture 2026-11-23/ctrl-gpu 2026-11-23/edagoat-eda-gpu 2026-11-23/epistemic-guard 2026-11-23/hookevo 2026-11-23/lrsa 2026-11-23/medicalrsi 2026-11-23/memonce 2026-11-23/roha-sgg 2026-11-23/turnout 2026-11-24/cmhc 2026-11-24/declarative-attention 2026-11-24/dissparse-top-p 2026-11-24/dive 2026-11-24/hyperharness 2026-11-24/item-60 2026-11-24/massys 2026-11-24/metarsi-rsi 2026-11-24/nohaircache 2026-11-24/refinekv-kv 2026-11-24/semantic-pid-rsi-pid 2026-11-24/shirudo-ebpf 2026-11-24/skill-state 2026-11-25/agl-skill 2026-11-25/autoseco 2026-11-25/detection-gap 2026-11-25/dmc-5 2026-11-25/harness2 2026-11-25/harnesspro 2026-11-25/hopper-4-bit-kv 2026-11-25/item-128 2026-11-25/item-150 2026-11-25/leannext 2026-11-25/loomkv-kv 2026-11-25/mosaic 2026-11-25/motion-mamba-2-0 2026-11-25/nfa 2026-11-25/noevera 2026-11-25/prefill1 2026-11-25/toolsmith 2026-11-25/vise 2026-11-25/wactorz 2026-11-25/weight-coding 2026-11-26/dfly2 2026-11-26/dots 2026-11-26/harness-learning 2026-11-26/home 2026-11-26/item-87 2026-11-26/precept 2026-11-26/qwen-image-hd 2026-11-26/roboevo 2026-11-26/sim 2026-11-26/sports-agent 2026-11-26/transharness 2026-11-27/molt-kv 2026-11-27/tabbyml 2026-11-28/adaptrouter 2026-11-28/ars-vlm 2026-11-28/boundary-aware-policy-learning 2026-11-28/kolpona 2026-11-28/shownow 2026-11-28/yggdrasil -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [Darwin Gödel Machine (dgm)](https://github.com/jennyzzt/dgm) — 开放式进化的自改进编码 Agent，自己修改自己的代码并经基准验证
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) — AlphaEvolve 的开源复现，进化式代码优化框架
- [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) — Sakana AI 开放式、样本高效的程序进化框架
- [ADAS](https://github.com/ShengranHu/ADAS) — Automated Design of Agentic Systems：元 Agent 在代码空间搜索新 Agent 设计
- [AFlow](https://github.com/FoundationAgents/AFlow) — MCTS 自动生成 Agent 工作流
- [DSPy](https://github.com/stanfordnlp/dspy) — 声明式 LM 程序框架，可对提示与模块进行自动优化
- [TextGrad](https://github.com/zou-group/textgrad) — 以自然语言反馈为"梯度"自动优化复合 AI 系统
- [Trace](https://github.com/microsoft/Trace) — 基于执行轨迹的生成式优化（"下一代 AutoDiff"）
- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) — 自指式递归自改进 Agent 框架
- [EvoAgentX](https://github.com/ANative-Lab/EvoAgentX) — 自进化 Agent 生态系统，自动演化工作流
- [Self-Evolving-Agents](https://github.com/CharlesQ9/Self-Evolving-Agents) — 自进化 Agent 综述配套资源库
- [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents) — 自进化 AI Agent 综述与论文清单

**论文**
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) — 自修改代码 + 开放式档案，SWE-bench 从 20% 提升到 50%
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) — DeepMind 进化式编码 Agent，改进矩阵乘法等算法
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349)
- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) — 元 Agent 搜索 Agent 设计空间
- [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762)
- [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444)
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496)
- [Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://arxiv.org/abs/2406.16218)
- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046)
- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)
