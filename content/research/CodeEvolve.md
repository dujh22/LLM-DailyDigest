+++
title = 'CodeEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# CodeEvolve

> 研究方向：**代码自进化**——以代码为载体的自进化：进化式程序搜索与算法发现、自改进编码 Agent、以及软件工程 Agent 的自训练闭环。

## 研究范畴

代码自进化（code self-evolution）把"代码"同时视为自进化的对象与手段：一方面，LLM 驱动的进化式程序搜索（FunSearch、AlphaEvolve、ShinkaEvolve、OpenEvolve、CodeEvolve）在可自动验证的问题上发现新算法与更优实现；另一方面，编码 Agent 可以修改自身的脚手架与工具（Self-Improving Coding Agent、Darwin Gödel Machine、Live-SWE-agent），形成"写代码的 Agent 改进写代码的 Agent"的递归闭环；再一方面，软件工程 Agent 的训练数据与环境本身也在自动生成与规模化（SWE-smith、SWE-Gym、R2E-Gym、SWE-RL 从开源演化历史学习）。本方向涵盖：自调试与自修复、流程工程（AlphaCodium）、进化式代码优化与算法发现、自改进编码 Agent 的档案与择优策略、可验证奖励下的代码 RL、以及软件工程环境的程序化合成。代码天然具备可执行、可测试、可度量的特点，是自进化闭环最易闭合也最易被作弊的领域，社区关注的核心问题包括：测试用例被"针对性通过"而非真正正确、进化出的代码可读性与可维护性、自修改 Agent 的安全边界，以及从竞赛题到真实仓库级任务的泛化。

## 研究挑战

- 评估作弊：针对测试用例硬编码、绕过验证器而非真正解决问题。
- 进化出的代码可读性、可维护性与安全性难以保证。
- 自修改编码 Agent 的失控与回滚：错误改动破坏自身能力。
- 从算法竞赛 / 函数级任务到仓库级真实软件工程的泛化。
- 进化搜索的算力与采样成本高，样本效率是关键瓶颈。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，代码自进化是自进化机制综述中最易闭环验证的方向。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，自重写 / 自修复编码 Agent 为重点收录对象。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 含代码推理任务族的智能体评测与自进化平台。

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
1. **可执行验证优先**：自进化优先用于可自动执行验证的任务；代码应在无密钥隔离环境运行。验证器须与生成器权限分离、不可由其篡改，并以强制约束门控搜索，对漏洞异步审计修补。
   - [TabbyML多智能体团队：契约驱动系统优化](../../updates/2026-11-27/#tabbyml) · 2026-11-27
   - [3DCodeFactory：实机验证式3D数据合成](../../updates/2026-11-26/#3dcodefactory-3d) · 2026-11-26
   - [Online Environment Repair：在线修复验证环境](../../updates/2026-11-25/#online-environment-repair) · 2026-11-25
   - [SplitBench：评测权限分离](../../updates/2026-11-23/#splitbench) · 2026-11-23
   - [Grok Bot：约束验证驱动开发](../../updates/2026-11-23/#grok-bot) · 2026-11-23
   - [EDAGoat：EDA约束验证式GPU优化](../../updates/2026-11-23/#edagoat-eda-gpu) · 2026-11-23
   - [SWE-OPD：仓库交互式在策略蒸馏](../../updates/2026-11-18/#swe-opd) · 2026-11-18
   - [Let Execution Do the Teaching：执行反馈驱动代码训练](../../updates/2026-11-17/#let-execution-do-the-teaching) · 2026-11-17
   - [外部沙箱模式：代码执行与密钥隔离](../../updates/2026-11-17/#item-28) · 2026-11-17
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [AI 智能体自主优化原子模拟数值算法](../../updates/2026-11-12/#item-94) · 2026-11-12
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
2. **证据边界校准**：代码评判不能只看单一参考、模型分或可执行性；应按任务校准规格、测试、实现与产品质量维度的证据边界，并检查错误通过、泄漏、越权和过度规定。
   - [GameAnything：灵感驱动可玩世界生成](../../updates/2026-11-28/#gameanything) · 2026-11-28
   - [Play2Evolve：趣味反馈驱动游戏演化](../../updates/2026-11-27/#play2evolve) · 2026-11-27
   - [SWE-Gym-Verified：执行证据式数据审计](../../updates/2026-11-25/#swe-gym-verified) · 2026-11-25
   - [STCG：检测过度规定测试](../../updates/2026-11-25/#stcg) · 2026-11-25
   - [MARGIN：近失裕度驱动程序修复](../../updates/2026-11-25/#margin) · 2026-11-25
   - [FormalFixer：规格断言与RTL联合修复](../../updates/2026-11-21/#formalfixer-rtl) · 2026-11-21
   - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
   - [VibePrevisBench：四维场景编程评测](../../updates/2026-11-17/#vibeprevisbench) · 2026-11-17
   - [TestPrism揭示Coding Agent测试生成合格率被高估](../../updates/2026-11-13/#testprism-coding-agent) · 2026-11-13
   - [前沿编程 LLM 是在编码还是作弊？](../../updates/2026-11-12/#llm-7) · 2026-11-12
   - [AutoRefine：基于工作流结果自动校准代码评判器](../../updates/2026-11-12/#autorefine) · 2026-11-12
   - [不可能代码，评分几乎不变：代码评判模型复现实验](../../updates/2026-11-03/#item-39) · 2026-11-03
3. **目标硬件闭环**：系统性能搜索须闭环到目标硬件实测；跨后端迁移还需显式建模硬件能力、栈级依赖与成本。
   - [芯片PPA优化：模型挖掘成熟设计余量](../../updates/2026-11-19/#ppa) · 2026-11-19
   - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
   - [Accelerate Bench：应用级程序优化评测](../../updates/2026-11-18/#accelerate-bench) · 2026-11-18
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [KernelMosaic：CUDA Kernel 生成数据集与智能体框架](../../updates/2026-11-13/#kernelmosaic-cuda-kernel) · 2026-11-13
   - [面向自主 RTL 与综合优化的基准和自改进智能体](../../updates/2026-11-12/#rtl) · 2026-11-12
   - [EngineAgent：感知推理栈层级与硬件能力的端侧推理引擎智能体](../../updates/2026-11-12/#engineagent) · 2026-11-12
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [ModelBlaster：跨模型、内核与硬件后端的学习增强优化智能体](../../updates/2026-11-06/#modelblaster) · 2026-11-06
   - [KernelSeek：问题驱动的 GPU 内核优化智能体](../../updates/2026-11-06/#kernelseek-gpu) · 2026-11-06
   - [ForgeKernel零样本自进化生成算子，性能超越DeepSeek FlashMLA 9.8%](../../updates/2026-10-31/#forgekernel-deepseek-flashmla-9-8) · 2026-10-31
   - [ForgeKernel 登顶华为与英伟达算子评测榜](../../updates/2026-10-29/#forgekernel) · 2026-10-29
4. **脚手架共同演化**：不要只搜索最终代码；将工具、工作流和干预策略纳入可修改脚手架，并用成败轨迹锚定修改、在留出任务检验迁移，固定权重也能获得能力增益。
   - [TransHarness：可迁移脚手架演化](../../updates/2026-11-26/#transharness) · 2026-11-26
   - [Pax：插件化终端编码智能体](../../updates/2026-11-26/#pax) · 2026-11-26
   - [Meta-RTL：演化式RTL优化脚手架](../../updates/2026-11-20/#meta-rtl-rtl) · 2026-11-20
   - [automodel：可移植模型发现技能](../../updates/2026-11-19/#automodel) · 2026-11-19
   - [VHarness：视觉推理工具化](../../updates/2026-11-16/#vharness) · 2026-11-16
   - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
   - [腾讯混元发布终端智能体递归自我改进框架 Terminal-RSI](../../updates/2026-11-12/#terminal-rsi) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [HEMO：面向多目标组合优化的脚手架自演化](../../updates/2026-10-30/#hemo) · 2026-10-30
5. **持久记忆复用**：开放式演化应保存结构化经验、轨迹与工具，并按任务检索；经验须经真实执行和留出任务持续证伪，及时回滚泄漏或无效规则。
   - [GameAnything：灵感驱动可玩世界生成](../../updates/2026-11-28/#gameanything) · 2026-11-28
   - [TabbyML多智能体团队：契约驱动系统优化](../../updates/2026-11-27/#tabbyml) · 2026-11-27
   - [PRECEPT：失误驱动的安全原则演化](../../updates/2026-11-26/#precept) · 2026-11-26
   - [Notary门控回顾环：规则准入效用验证](../../updates/2026-11-25/#notary) · 2026-11-25
   - [MOSAIC：记忆组织式反模仿搜索](../../updates/2026-11-25/#mosaic) · 2026-11-25
   - [AutoSECO：可迁移求解技能演化](../../updates/2026-11-25/#autoseco) · 2026-11-25
   - [ZhuLong-SE：执行轨迹驱动自进化](../../updates/2026-11-23/#zhulong-se) · 2026-11-23
   - [TokenEconomizer：仓库经验驱动降本](../../updates/2026-11-17/#tokeneconomizer) · 2026-11-17
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [CoReMem：面向连续编程任务的成本内化记忆框架](../../updates/2026-11-14/#coremem) · 2026-11-14
   - [CAMP-II：通过在策略蒸馏释放文件操作的长期记忆潜力](../../updates/2026-11-12/#camp-ii) · 2026-11-12
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [ModelBlaster：跨模型、内核与硬件后端的学习增强优化智能体](../../updates/2026-11-06/#modelblaster) · 2026-11-06
   - [Group-Evolving Agents：经验共享驱动的开放式群体自进化](../../updates/2026-11-04/#group-evolving-agents) · 2026-11-04
   - [HEMO：面向多目标组合优化的脚手架自演化](../../updates/2026-10-30/#hemo) · 2026-10-30
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
6. **群体保多样性**：固定单智能体容易陷入局部最优；并行群体、动态重组与经验共享可维持候选多样性并扩大搜索边界。
   - [TabbyML多智能体团队：契约驱动系统优化](../../updates/2026-11-27/#tabbyml) · 2026-11-27
   - [PDE元求解器：多智能体帕累托演化](../../updates/2026-11-25/#pde) · 2026-11-25
   - [MOSAIC：记忆组织式反模仿搜索](../../updates/2026-11-25/#mosaic) · 2026-11-25
   - [DiVE：小模型多样性递归改进](../../updates/2026-11-24/#dive) · 2026-11-24
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [SwarmEvolve：潜空间智能体群的进化发现与优化](../../updates/2026-11-08/#swarmevolve) · 2026-11-08
   - [Group-Evolving Agents：经验共享驱动的开放式群体自进化](../../updates/2026-11-04/#group-evolving-agents) · 2026-11-04
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
7. **代码化任务分解**：长程或实时任务可将慢速推理得到的策略分解为带适用条件的可执行子程序，再依运行反馈修订工作流，以降低延迟并保留审计路径。
   - [SIGame：代码策略自我改进](../../updates/2026-11-20/#sigame) · 2026-11-20
   - [Option-GRPO：代码选项分层强化学习](../../updates/2026-11-19/#option-grpo) · 2026-11-19
   - [SeaFlow：基于语义任务分解的自演化智能体工作流](../../updates/2026-11-03/#seaflow) · 2026-11-03
8. **执行轨迹自训练**：轨迹自训练不必依赖同题群组比较；可从高价值检查点分支，或提取单条执行轨迹的直接反馈，将失败现场和恢复示范转为训练信号。
   - [DFPO：单轨迹直接反馈优化](../../updates/2026-11-28/#dfpo) · 2026-11-28
   - [SWE-Trail：历史引导的编码智能体轨迹收集](../../updates/2026-11-04/#swe-trail) · 2026-11-04
   - [ReTerm：让Code Agent从失败恢复中递归自我改进](../../updates/2026-11-04/#reterm-code-agent) · 2026-11-04
9. **持续演化防漂移**：长程执行与脚手架连续改写都会漂移或遗忘；应以独立监控和可靠中间提示纠偏，并用工程指标、历史回归集和非退化档案约束更新。
   - [OOAS：聚合反馈驱动的动态转向](../../updates/2026-11-28/#ooas) · 2026-11-28
   - [Wactorz：自编写边缘智能体运行时](../../updates/2026-11-25/#wactorz) · 2026-11-25
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [Metrics-in-the-Loop：指标闭环代码纠偏](../../updates/2026-11-19/#metrics-in-the-loop) · 2026-11-19
   - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
   - [Multi-step SWE：编码智能体的长程持续开发评测](../../updates/2026-11-06/#multi-step-swe) · 2026-11-06
   - [编程智能体能否在持续演化中避免遗忘？](../../updates/2026-11-06/#item-94) · 2026-11-06
10. **真实长程环境**：评测与自训练环境应覆盖状态化、多步骤、资源受限且上下文不完整的端到端任务；用真实记录或结构指标分级构建，并在未见实例检验可行性、质量与时延。
    - [GameAnything：灵感驱动可玩世界生成](../../updates/2026-11-28/#gameanything) · 2026-11-28
    - [3DCodeFactory：实机验证式3D数据合成](../../updates/2026-11-26/#3dcodefactory-3d) · 2026-11-26
    - [模拟软件公司评测：端到端开发能力检验](../../updates/2026-11-23/#item-10) · 2026-11-23
    - [FrontierOR：智能体优化算法设计](../../updates/2026-11-20/#frontieror) · 2026-11-20
    - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
    - [3D GameDev Arena：超长程游戏开发评测](../../updates/2026-11-19/#3d-gamedev-arena) · 2026-11-19
    - [SWE-CoWork：数字员工式编程评测](../../updates/2026-11-18/#swe-cowork) · 2026-11-18
    - [RepoFactory：代码训练环境演化](../../updates/2026-11-18/#repofactory) · 2026-11-18
    - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
    - [Accelerate Bench：应用级程序优化评测](../../updates/2026-11-18/#accelerate-bench) · 2026-11-18
    - [VibePrevisBench：四维场景编程评测](../../updates/2026-11-17/#vibeprevisbench) · 2026-11-17
    - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
    - [面向自主 RTL 与综合优化的基准和自改进智能体](../../updates/2026-11-12/#rtl) · 2026-11-12
    - [Longtail-SWE：覆盖长尾编程语言的仓库级软件工程评测基准](../../updates/2026-11-12/#longtail-swe) · 2026-11-12
    - [SessionFarmer：从真实 Vibe Coding 会话构建 SWE 评测基准](../../updates/2026-11-06/#sessionfarmer-vibe-coding-swe) · 2026-11-06
    - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
    - [Multi-step SWE：编码智能体的长程持续开发评测](../../updates/2026-11-06/#multi-step-swe) · 2026-11-06
    - [CompressionBench：编码智能体自主压缩 LLM 评测](../../updates/2026-11-06/#compressionbench-llm) · 2026-11-06
11. **全链路可观测**：多智能体长程开发需分离记录代码事实与任务决策，并追踪事件、归属、证据和状态变更；用防篡改账本与溯源图核验轨迹和产物。
    - [AutoRLBench：真实RL故障诊修评测](../../updates/2026-11-26/#autorlbench-rl) · 2026-11-26
    - [HoH：双状态长程编码代理](../../updates/2026-11-24/#hoh) · 2026-11-24
    - [Claude Docs：混沌循环压测自修复](../../updates/2026-11-18/#claude-docs) · 2026-11-18
    - [Agent Trajectories：轨迹证据化质量审查](../../updates/2026-11-18/#agent-trajectories) · 2026-11-18
    - [Harness-of-Harness：证据驱动持续开发](../../updates/2026-11-17/#harness-of-harness) · 2026-11-17
    - [Soei：面向多智能体软件工程的证据与意图结构化可观测性](../../updates/2026-10-30/#soei) · 2026-10-30
12. **机制引导搜索**：用机制假设定位少量可干预结构，并以领域语言、方向性问题、层级知识或结构化反例约束搜索，比在任意代码或权重空间试错更省预算且便于迁移。
    - [Kolpona：无梯度神经元编程](../../updates/2026-11-28/#kolpona) · 2026-11-28
    - [LeanNeXt：假设驱动架构发现](../../updates/2026-11-25/#leannext) · 2026-11-25
    - [量子纠错解码：DSL语法进化](../../updates/2026-11-20/#dsl) · 2026-11-20
    - [TabDAG：图程序约束进化搜索](../../updates/2026-11-19/#tabdag) · 2026-11-19
    - [Option-GRPO：代码选项分层强化学习](../../updates/2026-11-19/#option-grpo) · 2026-11-19
    - [MakoBORN：前瞻式量化程序合成](../../updates/2026-11-19/#makoborn) · 2026-11-19
    - [ELITE：无评估机制整合](../../updates/2026-11-18/#elite) · 2026-11-18
    - [Craftax：续程反馈引导策略进化](../../updates/2026-11-17/#craftax) · 2026-11-17
    - [TopoVerus：基于学习反例与课程奖励的形式化证明修复](../../updates/2026-11-12/#topoverus) · 2026-11-12
    - [EngineAgent：感知推理栈层级与硬件能力的端侧推理引擎智能体](../../updates/2026-11-12/#engineagent) · 2026-11-12
    - [RecRSI：机制引导的推荐算法自动发现框架](../../updates/2026-11-06/#recrsi) · 2026-11-06
    - [KernelSeek：问题驱动的 GPU 内核优化智能体](../../updates/2026-11-06/#kernelseek-gpu) · 2026-11-06
13. **端到端收益核算**：比较上下文或工具时，应固定脚手架与强基线、跨智能体重复运行，并按后续行为和有效状态变化核算成本与方差。
    - [FGL：修复器似然引导代码定位](../../updates/2026-11-25/#fgl) · 2026-11-25
    - [软件热力学：热功分解编码成本](../../updates/2026-11-19/#item-47) · 2026-11-19
    - [Context Has a Price：缓存感知上下文成本评测](../../updates/2026-11-18/#context-has-a-price) · 2026-11-18
    - [Thomson问题：智能体搜索与精确认证](../../updates/2026-11-16/#thomson) · 2026-11-16
    - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
14. **证明携带代码**：高风险或昂贵难执行的生成代码，应携带机器可复核的等价性、安全或最优性证书，并明确形式化覆盖；部分验证不可外推整体可信，重大主张还须独立复核。
    - [OpenAI Math：AI批量生成数学证明](../../updates/2026-11-26/#openai-math-ai) · 2026-11-26
    - [量子算法智能体：Lean验证式电路优化](../../updates/2026-11-24/#lean) · 2026-11-24
    - [SailSearch：双智能体辅助算法发现](../../updates/2026-11-21/#sailsearch) · 2026-11-21
    - [Thomson问题：智能体搜索与精确认证](../../updates/2026-11-16/#thomson) · 2026-11-16
    - [Agent-written Heuristics：编码智能体生成调度启发式](../../updates/2026-11-16/#agent-written-heuristics) · 2026-11-16
    - [Claude Code形式化三元哥德巴赫猜想并发现原证明错误](../../updates/2026-11-13/#claude-code) · 2026-11-13
    - [TopoVerus：基于学习反例与课程奖励的形式化证明修复](../../updates/2026-11-12/#topoverus) · 2026-11-12
    - [AI 自动发现形式化验证的量子程序](../../updates/2026-11-12/#item-179) · 2026-11-12
    - [通过完整集合划分精确认证 QPLIB 2096 全局最优性](../../updates/2026-11-06/#qplib-2096) · 2026-11-06
    - [LARK：用 Lean 形式化验证 LLM 生成的 GPU Kernel](../../updates/2026-11-06/#lark-lean-llm-gpu-kernel) · 2026-11-06
15. **义务驱动终止**：补丁满足全部任务义务后应触发独立终止判定；无上限的继续探索会浪费预算，甚至撤销已正确的解。
    - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
    - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
<!-- experience-seen: 2026-11-21/formalfixer-rtl 2026-11-21/sailsearch 2026-11-23/claude 2026-11-23/edagoat-eda-gpu 2026-11-23/grok-bot 2026-11-23/item-10 2026-11-23/splitbench 2026-11-23/zhulong-se 2026-11-24/dive 2026-11-24/hoh 2026-11-24/lean 2026-11-24/shirudo-ebpf 2026-11-25/autoseco 2026-11-25/detection-gap 2026-11-25/fgl 2026-11-25/leannext 2026-11-25/margin 2026-11-25/mosaic 2026-11-25/notary 2026-11-25/online-environment-repair 2026-11-25/pde 2026-11-25/stcg 2026-11-25/swe-gym-verified 2026-11-25/wactorz 2026-11-26/3dcodefactory-3d 2026-11-26/autorlbench-rl 2026-11-26/dots 2026-11-26/fwsp 2026-11-26/openai-math-ai 2026-11-26/pax 2026-11-26/precept 2026-11-26/transharness 2026-11-27/play2evolve 2026-11-27/tabbyml 2026-11-28/dfpo 2026-11-28/gameanything 2026-11-28/kolpona 2026-11-28/ooas -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [FunSearch](https://github.com/google-deepmind/funsearch) — DeepMind 用 LLM 程序搜索取得数学发现
- [AlphaEvolve results](https://github.com/google-deepmind/alphaevolve_results) — AlphaEvolve 发现的算法与数学结果
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) — AlphaEvolve 开源复现
- [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) — 样本高效的开放式程序进化
- [Darwin Gödel Machine (dgm)](https://github.com/jennyzzt/dgm) — 自修改自身代码的编码 Agent
- [Self-Improving Coding Agent (SICA)](https://github.com/MaximeRobeyns/self_improving_coding_agent) — 编码 Agent 编辑自身代码库以提升性能
- [OpenHands](https://github.com/OpenHands/OpenHands) — 开源软件开发 Agent 平台
- [aider](https://github.com/Aider-AI/aider) — 终端 AI 配对编程工具
- [Agentless](https://github.com/OpenAutoCoder/Agentless) — 无 Agent 的定位-修复-验证流程
- [AlphaCodium](https://github.com/Codium-ai/AlphaCodium) — 从提示工程到流程工程的代码生成
- [SWE-smith](https://github.com/SWE-bench/SWE-smith) — 规模化合成软件工程 Agent 训练数据
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) — 训练软件工程 Agent 与验证器的环境
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) — 程序化生成的 SWE 环境与混合验证器
- [SWE-RL](https://github.com/facebookresearch/swe-rl) — 在开源软件演化历史上做 RL

**论文**
- [Evolution through Large Models](https://arxiv.org/abs/2206.08896) — ELM：LLM 作为变异算子的程序进化
- [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) — FunSearch（Nature 2023）
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349)
- [CodeEvolve: an open source evolutionary coding agent for algorithmic discovery and optimization](https://arxiv.org/abs/2510.14150) — 同名开源进化编码 Agent
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954)
- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) — SICA
- [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) — 运行中自进化的 SWE Agent
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128)
- [Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](https://arxiv.org/abs/2401.08500)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449)
- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798)
- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)
- [R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://arxiv.org/abs/2504.07164)
