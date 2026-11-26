+++
title = 'Awesome-RSI'
proposer = '杜晋华'
since = '2026-06-12'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# Awesome-RSI

> 研究方向：**递归自我改进（Recursive Self-Improvement, RSI）**方向的精选资源与论文清单。

## 研究范畴

递归自我改进（RSI）指一个系统能够持续改进自身，且其"改进机制"本身也被纳入改进对象，从而形成自指式的提升闭环。本方向涵盖：自我改进 Agent、自我重写 / 自我修复、LLM-as-a-Judge 自迭代、开放式 RSI 任务，以及面向 RSI 的治理与安全框架。社区关注的核心问题包括：自我改进能否持续近似单调地提升、是否存在上限或退化、自我奖励 / 自评判信号是否存在系统性偏差、如何度量"改进"本身以避免被优化目标作弊，以及 RSI 与对齐、可控性的协同。

## 研究挑战

- 奖励作弊（reward hacking）与退化解、捷径行为。
- 长期迭代的稳定性与灾难性遗忘。
- 评测有效性：如何在快速自进化的系统中持续评估真实能力。
- 安全治理：失控风险、红队、披露与审计。
- 计算与数据成本随迭代轮次快速膨胀。

## 自研项目

- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 面向 RSI 的持续研究项目：维护综述、整理论文与资源、沉淀自动化采集/归并工具，先跑通"采集 → 去重归并论文库 → AI/人工笔记 → 综述引用位置"的最小可检查闭环。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI / 走向真正的 ASI》承载仓库，含开题材料与综述《大语言模型复杂推理的自我进化机制》。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — LLM 论文/工具/资讯每日自动聚合系统（爬取→翻译→摘要），Hugo+FixIt 网站 + topic/research 双聚合 + Flask/LLM 抽取后端。
- [LLMDailyDigestWeb](https://github.com/dujh22/LLMDailyDigestWeb) — LLM-DailyDigest 的线上静态站点（GitHub Pages 构建产物）。
- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》（唐杰、杜晋华，清华）配套仓库，Word+LaTeX，覆盖深度学习/Transformer/预训练/SFT/RLHF/评测对齐/Agent/安全/多模态/生成模型等章节。

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
1. **可验证闭环优先**：优先选择能自动生成且独立验证反馈的任务；缺少可证伪信号时，递归迭代容易把评测误差当作能力提升。
   - [Fin-RSI：统一金融技能与自改进](../../updates/2026-11-25/#fin-rsi) · 2026-11-25
   - [FinEvo：同模自博弈递归改进](../../updates/2026-11-24/#finevo) · 2026-11-24
   - [EVA-RSI：代理考试驱动视频评估自改进](../../updates/2026-11-19/#eva-rsi) · 2026-11-19
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [百度披露 ERNIE Evolve 递归自我改进进展，已用于文心 5.5 Flash 研发](../../updates/2026-11-12/#ernie-evolve-5-5-flash) · 2026-11-12
   - [RecRSI：机制引导的推荐算法自动发现框架](../../updates/2026-11-06/#recrsi) · 2026-11-06
   - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [递归自我改进（RSI）：2026 年论文趋势盘点](../../updates/2026-11-01/#rsi-2026) · 2026-11-01
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [RSI-Master：受控实验驱动的自主模型改进](../../updates/2026-10-30/#rsi-master) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
2. **评判器必须隔离**：凡评估结果参与选模或训练，评判器都应按干预接受隔离审计；加入独立执行、人评、语义等价变换及证据匹配对照，排查迎合、方向偏差和定向误导。
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [DoppelVet：对照式更新安全验证](../../updates/2026-11-25/#doppelvet) · 2026-11-25
   - [量表反转探针：审计评判方向偏差](../../updates/2026-11-21/#item-21) · 2026-11-21
   - [CRITFAULT：评论器安全审计](../../updates/2026-11-17/#critfault) · 2026-11-17
   - [RSI Arena：人类反馈校准递归改进](../../updates/2026-11-16/#rsi-arena) · 2026-11-16
   - [临床AI评估即干预](../../updates/2026-11-16/#item-18) · 2026-11-16
   - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
   - [更换评判模型会改变系统排名：跨提供商预注册复现研究](../../updates/2026-11-06/#item-74) · 2026-11-06
   - [Agent-as-a-Judge 中的确认偏差：证据落地仍难免疫](../../updates/2026-11-06/#agent-as-a-judge) · 2026-11-06
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [RSI 系统优化 Agent 的 Reward Hacking 与验证边界](../../updates/2026-11-04/#rsi-agent-reward-hacking) · 2026-11-04
   - [不可能代码，评分几乎不变：代码评判模型复现实验](../../updates/2026-11-03/#item-39) · 2026-11-03
   - [RSI Arena：基于人类反馈的递归自我改进实验](../../updates/2026-10-30/#rsi-arena) · 2026-10-30
3. **验证随搜索扩容**：迭代次数和候选规模增大时，应同步提高验证覆盖、强度与独立性，否则选择压力会持续放大奖励作弊。
   - [TRUST：具备统计保证的可信递归自我改进](../../updates/2026-11-12/#trust) · 2026-11-12
   - [AI适应过程：达尔文式、拉马克式与智能体定向演化](../../updates/2026-11-06/#item-23) · 2026-11-06
   - [RSI 系统优化 Agent 的 Reward Hacking 与验证边界](../../updates/2026-11-04/#rsi-agent-reward-hacking) · 2026-11-04
4. **脚手架协同演化**：协同演化提示、工具、记忆、控制流和评判准则，比只改模型输出更易持久提升；目标规划与奖励合成应职责解耦，并以未见任务检验迁移。
   - [Habitats：开放式智能体目标演化](../../updates/2026-11-25/#habitats) · 2026-11-25
   - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
   - [JevRSI：递归改进决策脚手架](../../updates/2026-11-18/#jevrsi) · 2026-11-18
   - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
   - [腾讯混元发布终端智能体递归自我改进框架 Terminal-RSI](../../updates/2026-11-12/#terminal-rsi) · 2026-11-12
   - [GEAR：Scikit-learn 式模块化 RSI 框架推动 Agent 持续进化](../../updates/2026-11-12/#gear-scikit-learn-rsi-agent) · 2026-11-12
   - [BOXBOX：面向长程性能优化的递归脚手架自我改进](../../updates/2026-11-12/#boxbox) · 2026-11-12
   - [长程角色扮演对话的递归自我改进](../../updates/2026-11-08/#item-53) · 2026-11-08
   - [Strategist：用智能体演化推理策略](../../updates/2026-11-06/#strategist) · 2026-11-06
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
   - [Harness 自进化研究进展与趋势盘点](../../updates/2026-10-30/#harness) · 2026-10-30
   - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
   - [RuHarness：评判准则与智能体脚手架协同演化](../../updates/2026-10-29/#ruharness) · 2026-10-29
5. **状态驱动任务刷新**：按能力与知识状态同步刷新题池和可用证据，并依据正确率与有效优势信号选择干预，比固定课程更省预算，也能避免把证据缺失误判为能力错误。
   - [Search-RSI：能力前沿驱动搜索扩展](../../updates/2026-11-23/#search-rsi) · 2026-11-23
   - [AutoRL：多智能体闭环强化学习](../../updates/2026-11-16/#autorl) · 2026-11-16
   - [R²Orch：通过技能内化与自博弈实现智能体编排的递归自我改进](../../updates/2026-11-03/#r-orch) · 2026-11-03
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [RKI：状态感知的递归知识改进框架](../../updates/2026-10-29/#rki) · 2026-10-29
6. **失败经验资产化**：保留失败现场、修改理由、效果、评测环境与适用边界，可将失败转成跨轮次、跨任务复用的搜索资产。
   - [PhyEvo-Mic-RSI：物理引导显微分析自进化](../../updates/2026-11-25/#phyevo-mic-rsi) · 2026-11-25
   - [AeroRSI：续飞验证式递归自改进](../../updates/2026-11-19/#aerorsi) · 2026-11-19
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [ACE-RL：基于经验交接强化学习的递归自我改进](../../updates/2026-11-14/#ace-rl) · 2026-11-14
   - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
   - [SwarmRSI：共享失败经验驱动科研智能体群递归自我改进](../../updates/2026-11-05/#swarmrsi) · 2026-11-05
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
   - [ReTerm：让Code Agent从失败恢复中递归自我改进](../../updates/2026-11-04/#reterm-code-agent) · 2026-11-04
   - [读完 DGM：对 RSI 自我进化的几点判断](../../updates/2026-11-04/#dgm-rsi) · 2026-11-04
7. **抑制自训练坍缩**：无监督自训练需监控当前策略分布上的自评保真度、跨任务参数耦合与策略多样性；采用投影解耦、稳定化隔离或动态教师，避免阈值性坍缩。
   - [SRO：保真度诊断与投影解耦](../../updates/2026-11-24/#sro) · 2026-11-24
   - [DiVE：小模型多样性递归改进](../../updates/2026-11-24/#dive) · 2026-11-24
   - [递归自我改进（RSI）：2026 年论文趋势盘点](../../updates/2026-11-01/#rsi-2026) · 2026-11-01
   - [RISE：交错 RLVR 与在策略蒸馏实现递归自我改进](../../updates/2026-10-31/#rise-rlvr) · 2026-10-31
   - [跨任务耦合驱动无监督 RLVR 策略坍缩](../../updates/2026-10-29/#rlvr) · 2026-10-29
8. **多维轨迹评估**：即时分数或偏好上升不等于持续进步；应沿版本轨迹报告未见任务、安全、故障发现率、局部退化、历史峰值、更新保持度及端到端成本。
   - [RecurSciBench：科学RSI迁移评测](../../updates/2026-11-25/#recurscibench-rsi) · 2026-11-25
   - [Detection Gap：自改进智能体失效盲区](../../updates/2026-11-25/#detection-gap) · 2026-11-25
   - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
   - [OpenAI RSI：智能体驱动研发闭环](../../updates/2026-11-20/#openai-rsi) · 2026-11-20
   - [RSIBench-Infra：生产级基础设施优化评测](../../updates/2026-11-19/#rsibench-infra) · 2026-11-19
   - [研究加速报告：量化智能体研发效能](../../updates/2026-11-19/#item-15) · 2026-11-19
   - [RSI Arena：人类反馈校准递归改进](../../updates/2026-11-16/#rsi-arena) · 2026-11-16
   - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
   - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
   - [RSI-PDEbench：偏微分方程求解智能体递归自我改进基准](../../updates/2026-11-13/#rsi-pdebench) · 2026-11-13
   - [Third Eye：递归自我改进的长期效用评估](../../updates/2026-11-12/#third-eye) · 2026-11-12
   - [RSI Tax：递归自我改进何时得不偿失](../../updates/2026-11-12/#rsi-tax) · 2026-11-12
   - [Flex-RSI：前沿智能体递归自我改进评测基准](../../updates/2026-11-12/#flex-rsi) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [SelfImprove-Bench：自改进智能体泛化能力评测](../../updates/2026-11-06/#selfimprove-bench) · 2026-11-06
   - [RSI Arena：基于人类反馈的递归自我改进实验](../../updates/2026-10-30/#rsi-arena) · 2026-10-30
9. **受控实验基础设施**：将训练、推理、评测和预算服务化并记录研究DAG，配合单组件干预或匹配预算，提高可复现性、因果归因与作弊排查能力。
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [RSIBench-Infra：生产级基础设施优化评测](../../updates/2026-11-19/#rsibench-infra) · 2026-11-19
   - [TrainExplorer：规划解耦式后训练探索](../../updates/2026-11-17/#trainexplorer) · 2026-11-17
   - [Terminal-RSI：递归改写与策略精炼](../../updates/2026-11-17/#terminal-rsi) · 2026-11-17
   - [AI4AI：三决策研究控制框架](../../updates/2026-11-15/#ai4ai) · 2026-11-15
   - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [CompressionBench：编码智能体自主压缩 LLM 评测](../../updates/2026-11-06/#compressionbench-llm) · 2026-11-06
   - [RSIGym：面向递归自我改进的真实训练环境](../../updates/2026-11-05/#rsigym) · 2026-11-05
   - [RSI-Master：受控实验驱动的自主模型改进](../../updates/2026-10-30/#rsi-master) · 2026-10-30
10. **真实反馈闭环**：具身与科学任务应接入质量受控的真实执行或实验反馈；仅靠模拟自评难以发现动作、测量和候选选择误差。
    - [PhyEvo-Mic-RSI：物理引导显微分析自进化](../../updates/2026-11-25/#phyevo-mic-rsi) · 2026-11-25
    - [Fin-RSI：统一金融技能与自改进](../../updates/2026-11-25/#fin-rsi) · 2026-11-25
    - [FinEvo：同模自博弈递归改进](../../updates/2026-11-24/#finevo) · 2026-11-24
    - [Cyber-Physical RSI：物理反馈闭环自改进](../../updates/2026-11-20/#cyber-physical-rsi) · 2026-11-20
    - [AeroRSI：续飞验证式递归自改进](../../updates/2026-11-19/#aerorsi) · 2026-11-19
    - [书生·S2.1 Flash：统一表征与递归进化](../../updates/2026-11-17/#s2-1-flash) · 2026-11-17
    - [MolRSI：跨任务经验驱动策略自改进](../../updates/2026-11-15/#molrsi) · 2026-11-15
    - [WeightLoop：基于实验反馈的权重空间编程](../../updates/2026-11-06/#weightloop) · 2026-11-06
    - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
    - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
    - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
    - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
    - [MoLRSI：面向分子发现的递归自我改进智能体](../../updates/2026-10-30/#molrsi) · 2026-10-30
    - [智元 Genie Master 在便利店跑通具身递归自我改进](../../updates/2026-10-29/#genie-master) · 2026-10-29
11. **多层联合优化**：复杂任务中应把改进策略本身纳入反馈回路，并联合优化工作流、模型、记忆和脚手架；固定改进器会随剩余错误分布变化而封顶。
    - [TT-RSI：测试时递归自我改进](../../updates/2026-11-25/#tt-rsi) · 2026-11-25
    - [RSI：改进器自演化推导](../../updates/2026-11-24/#rsi) · 2026-11-24
    - [MetaRSI/RSI²：双轴元递归自改进](../../updates/2026-11-24/#metarsi-rsi) · 2026-11-24
    - [MedicalRSI：临床模型与脚手架协同演化](../../updates/2026-11-23/#medicalrsi) · 2026-11-23
    - [Piccolo：模型数据协同自进化](../../updates/2026-11-20/#piccolo) · 2026-11-20
    - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
    - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
    - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
    - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
    - [JoMoHa：强化学习驱动的模型—脚手架联合优化](../../updates/2026-11-12/#jomoha) · 2026-11-12
    - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
    - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
    - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
    - [MoLRSI：面向分子发现的递归自我改进智能体](../../updates/2026-10-30/#molrsi) · 2026-10-30
12. **共享记忆降本**：跨任务共享记忆可减少重复搜索，但须记录修改理由、效果、评测环境、来源与适用边界，避免把局部经验误当通则。
    - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
    - [JevRSI：递归改进决策脚手架](../../updates/2026-11-18/#jevrsi) · 2026-11-18
    - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
    - [MolRSI：跨任务经验驱动策略自改进](../../updates/2026-11-15/#molrsi) · 2026-11-15
    - [ACE-RL：基于经验交接强化学习的递归自我改进](../../updates/2026-11-14/#ace-rl) · 2026-11-14
    - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
    - [openJiuwen发布TTSE双轨经验学习框架](../../updates/2026-11-12/#openjiuwen-ttse) · 2026-11-12
    - [GEAR：Scikit-learn 式模块化 RSI 框架推动 Agent 持续进化](../../updates/2026-11-12/#gear-scikit-learn-rsi-agent) · 2026-11-12
    - [Recursa：递归自我改进的基础模型系统](../../updates/2026-11-06/#recursa) · 2026-11-06
    - [SwarmRSI：共享失败经验驱动科研智能体群递归自我改进](../../updates/2026-11-05/#swarmrsi) · 2026-11-05
    - [801-30B：将 RSI 引入前沿预训练](../../updates/2026-11-05/#801-30b-rsi) · 2026-11-05
13. **权重空间更新**：权重编辑或门控增量模块适合低成本局部修复，且可隔离部分副作用；效果仍可能依赖规模或数值痕迹，须做舍入对照、跨任务测试、安全审计和回退。
    - [SELFWRITE：无梯度自写权重编辑](../../updates/2026-11-25/#selfwrite) · 2026-11-25
    - [Self-Upgrading Embodied Agents：经验驱动权重自升级](../../updates/2026-11-25/#self-upgrading-embodied-agents) · 2026-11-25
    - [Self-WSP：权重空间自我编程](../../updates/2026-11-24/#self-wsp) · 2026-11-24
    - [Don't Train It, Write It：智能体直写模型能力](../../updates/2026-11-24/#don-t-train-it-write-it) · 2026-11-24
    - [Keel：智能体改权消除视觉循环](../../updates/2026-11-20/#keel) · 2026-11-20
    - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
    - [Weight Space Programming：低位痕迹引导权重修复](../../updates/2026-11-19/#weight-space-programming) · 2026-11-19
    - [Self-Rewriting：无梯度自改权重](../../updates/2026-11-18/#self-rewriting) · 2026-11-18
    - [权重空间编程：无梯度后门注入](../../updates/2026-11-16/#item-36) · 2026-11-16
    - [Tree-Ising：基于位级 Ising 编辑的语言模型修复](../../updates/2026-11-12/#tree-ising-ising) · 2026-11-12
    - [NCP：验证器引导的权重空间控制策略优化](../../updates/2026-11-12/#ncp) · 2026-11-12
    - [LLM 通过权重编辑调试机器人策略](../../updates/2026-11-12/#llm-8) · 2026-11-12
    - [权重空间编程的能力、泛化与局限](../../updates/2026-11-12/#item-192) · 2026-11-12
    - [WeightLoop：基于实验反馈的权重空间编程](../../updates/2026-11-06/#weightloop) · 2026-11-06
    - [Astra 直接编程神经网络权重，显著提升 Qwen 数学能力](../../updates/2026-11-03/#astra-qwen) · 2026-11-03
14. **持久更新治理**：持久更新应经独立审计、安全回归与非劣效检验，默认拒绝失败版本并保留回退；自生成内容、权重编辑及种群跨代变化均按不可信输入处理。
    - [Self-Upgrading Embodied Agents：经验驱动权重自升级](../../updates/2026-11-25/#self-upgrading-embodied-agents) · 2026-11-25
    - [Evolutionary AI Control：演化种群安全证明](../../updates/2026-11-25/#evolutionary-ai-control) · 2026-11-25
    - [DoppelVet：对照式更新安全验证](../../updates/2026-11-25/#doppelvet) · 2026-11-25
    - [Semantic PID-RSI：语义PID控制自改进](../../updates/2026-11-24/#semantic-pid-rsi-pid) · 2026-11-24
    - [Safe Personal RSI：回滚修复式安全更新](../../updates/2026-11-19/#safe-personal-rsi) · 2026-11-19
    - [GUARD：后悔引导脚手架演化](../../updates/2026-11-19/#guard) · 2026-11-19
    - [权重空间编程：无梯度后门注入](../../updates/2026-11-16/#item-36) · 2026-11-16
    - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
    - [自主智能体自生成更新的证据治理采纳框架 EGE](../../updates/2026-11-14/#ege) · 2026-11-14
    - [EvoTrias：智能体程序进化的权力分立架构](../../updates/2026-11-13/#evotrias) · 2026-11-13
    - [快慢双环：长程智能体部署的控制论监督框架](../../updates/2026-11-12/#item-210) · 2026-11-12
    - [BadEvolve：通过失败感知任务优化投毒自进化智能体](../../updates/2026-11-12/#badevolve) · 2026-11-12
15. **评测分辨率优先**：候选扩容前先确认评测能稳定区分小幅真实改进；用方差分解、可控扰动、等价规则不变性及策略—裁判暴露度校验信号，否则收益无法跨代累积。
    - [暴露度预判奖励作弊](../../updates/2026-11-25/#item-123) · 2026-11-25
    - [SRO：保真度诊断与投影解耦](../../updates/2026-11-24/#sro) · 2026-11-24
    - [量表反转探针：审计评判方向偏差](../../updates/2026-11-21/#item-21) · 2026-11-21
    - [Sage-Evolve-Preview：自适应观测驱动持续改进](../../updates/2026-11-20/#sage-evolve-preview) · 2026-11-20
    - [Resolution Hypothesis：评测分辨率瓶颈](../../updates/2026-11-19/#resolution-hypothesis) · 2026-11-19
    - [EVA-RSI：代理考试驱动视频评估自改进](../../updates/2026-11-19/#eva-rsi) · 2026-11-19
<!-- experience-seen: 2026-11-18/elite 2026-11-18/jevrsi 2026-11-18/self-rewriting 2026-11-19/aerorsi 2026-11-19/eva-rsi 2026-11-19/guard 2026-11-19/item-15 2026-11-19/item-48 2026-11-19/resolution-hypothesis 2026-11-19/rsi-prime 2026-11-19/rsibench-infra 2026-11-19/safe-personal-rsi 2026-11-19/weight-space-programming 2026-11-20/agnes-harness 2026-11-20/basersi 2026-11-20/cyber-physical-rsi 2026-11-20/keel 2026-11-20/openai-rsi 2026-11-20/piccolo 2026-11-20/sage-evolve-preview 2026-11-20/self-replicating-language-models 2026-11-20/system-one-rsi 2026-11-21/agi-asi 2026-11-21/item-21 2026-11-23/alps-lab 2026-11-23/coevobench 2026-11-23/embodied-harness 2026-11-23/medicalrsi 2026-11-23/openai-ai 2026-11-23/search-rsi 2026-11-24/2026-ai-rsi 2026-11-24/dive 2026-11-24/don-t-train-it-write-it 2026-11-24/finevo 2026-11-24/metarsi-rsi 2026-11-24/rsi 2026-11-24/self-wsp 2026-11-24/semantic-pid-rsi-pid 2026-11-24/sro 2026-11-24/superintelligence-is-arriving-ai 2026-11-25/detection-gap 2026-11-25/doppelvet 2026-11-25/evolutionary-ai-control 2026-11-25/fin-rsi 2026-11-25/glm-5-5-rsi 2026-11-25/habitats 2026-11-25/item-123 2026-11-25/phyevo-mic-rsi 2026-11-25/recurscibench-rsi 2026-11-25/self-upgrading-embodied-agents 2026-11-25/selfwrite 2026-11-25/tt-rsi -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [awesome_Recursive_Self-Improving_LLM](https://github.com/robert-lee2016/awesome_Recursive_Self-Improving_LLM) — RSI 精选清单（同名方向）
- [letta](https://github.com/letta-ai/letta) — 有状态、可自进化的智能体平台
- [ai-redteam-recursive-self-improvement](https://github.com/lihouwenbin/ai-redteam-recursive-self-improvement) — RSI 治理红队框架
- [recursive-improve (kayba-ai)](https://github.com/kayba-ai/recursive-improve) — 捕获 LLM 调用 trace，递归修复自身
- [recursive-self-improvement-suite (keskival)](https://github.com/keskival/recursive-self-improvement-suite) — 面向 LLM 的开放式 RSI 任务集
- [self-improvement-llm (Zesearch)](https://github.com/Zesearch/self-improvement-llm) — LLM 自我改进技术综述仓库
- [Awesome-Self-Improving-Agents (selfimproving-agent)](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) — 自我改进 Agent 系统合集
- [Awesome-Self-Improving-Agents (FrontisAI)](https://github.com/FrontisAI/Awesome-Self-Improving-Agents) — RL、skill library 等方向的另一合集
- [Awesome-Self-Evolving-Agents (XMUDeepLIT)](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 厦大自进化 Agent 综述
- [awesome-agent-harness (RUCAIBox)](https://github.com/RUCAIBox/awesome-agent-harness) — Agent harness 与自我改进

**论文**
- [Foundations of GenIR](https://arxiv.org/abs/2501.02842)
- [Adaptive Data Flywheel: MAPE Control Loops for AI Agent Improvement](https://arxiv.org/abs/2510.27051)
- [Gödel Agent: A Self-Referential Framework for Agents](https://arxiv.org/abs/2410.04444) — Gödel Machine 启发的递归自改写 Agent（被引 19+）
- [LADDER: Self-Improving LLMs Through Recursive Problem Decomposition](https://arxiv.org/abs/2503.00735) — 递归问题分解自主提升（被引 24）
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM-as-a-Judge 自我改进（被引 996）
- [Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) — Meta-Rewarding（被引 223）
- [ReST meets ReAct (ICLR 2024)](https://arxiv.org/abs/2312.10003) — 强化学习+自蒸馏多步推理改进（被引 96）
- [Noise-to-Meaning Recursive Self-Improvement](https://arxiv.org/abs/2505.02888) — RSI 系统性框架
- [On the Limits of Self-Improving in Large Language Models](https://arxiv.org/abs/2601.05280) — 自我改进理论极限
- [Recursive Self-Improvement in AI (Survey)](https://arxiv.org/abs/2607.07663) — 综述 1250 篇论文
- [How to Realize Recursively Self-Improving Agents](https://arxiv.org/abs/2607.12254) — 治理式多 Agent RSI 架构
- [Self Rewarding Self Improving](https://arxiv.org/abs/2505.08827) — 无参考答案的自评判自我改进
- [RISE (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf) — 多轮交互自我提升推理（被引 214）
- [SPC: Evolving Self-Play Critic (NeurIPS 2025)](https://neurips.cc/virtual/2025/poster/118706) — 对抗自博弈 Critic 进化

**研讨会 / 课程 / 报告**
- [ICLR 2026 Workshop on Recursive Self-Improvement](https://recursive-workshop.github.io/) — RSI 专题研讨会
- [Stanford CS329A: Self-Improving AI Agents](https://cs329a.stanford.edu/) — 斯坦福自我改进 Agent 课程
- [CSA: RSI Security Implications](https://labs.cloudsecurityalliance.org/research/ai-recursive-self-improvement-security-implications-v1-0-csa) — 云安全联盟 RSI 安全报告
