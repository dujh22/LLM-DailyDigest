+++
title = 'GeneralizeEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# GeneralizeEvolve

> 研究方向：**自进化中的泛化**——自进化带来的提升能否跨任务、跨分布迁移而非基准过拟合，以及测试时学习与持续学习如何不遗忘。

## 研究范畴

自进化中的泛化（generalization in self-evolution）追问一个核心问题：模型 / Agent 通过自迭代获得的能力，究竟是真实的能力扩展，还是对训练分布与评测基准的记忆与过拟合。本方向涵盖：SFT 与 RL 后训练的泛化差异（"SFT 记忆、RL 泛化"）、RLVR 是否扩展了基座模型的推理边界、在线 RL 为何遗忘更少、无外部奖励的自信号学习（Intuitor 类）、测试时训练与自适应（TTT、SEAL 自生成微调数据）、测试时记忆与长上下文架构（Titans）、持续学习与灾难性遗忘、弱到强泛化，以及 ARC-AGI 类强调流体智能而非知识回忆的评测。社区关注的核心问题包括：如何在自进化闭环中设计分布外（OOD）与组合泛化的检验、如何区分"学到的算法"与"记住的模式"（grokking 现象）、持续自进化下能力增益与遗忘的权衡，以及测试时计算与测试时学习在多大程度上能替代参数规模。

## 研究挑战

- 基准过拟合与数据污染：自迭代容易把评测集"学进去"。
- 持续自进化下的灾难性遗忘与能力退化。
- 自生成信号（自信度、自评）可能强化已有偏差而非扩展边界。
- OOD / 组合泛化缺乏公认且不易被攻陷的度量。
- 测试时学习的算力成本与稳定性。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，自进化的泛化边界是综述《大语言模型复杂推理的自我进化机制》讨论的核心科学问题。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 元数据驱动的可控逻辑推理任务生成，可按难度 / 规模 / 规则维度构造 OOD 测试，检验自进化带来的泛化。

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
1. **持续学习四维评测**：持续学习不能只看末轮均值；应沿适应过程测可塑性、旧任务保持、跨任务干扰和迁移，并用域外任务及不同读出接口区分真遗忘与暂时错配。
   - [预训练VLA持续学习：分布外遗忘诊断](../../updates/2026-11-25/#vla) · 2026-11-25
   - [三接口持续学习诊断](../../updates/2026-11-25/#item-109) · 2026-11-25
   - [Stability Gap：持续强化学习稳定性缺口](../../updates/2026-11-20/#stability-gap) · 2026-11-20
   - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
   - [Continual-ARC：衡量智能体终身技能习得](../../updates/2026-11-12/#continual-arc) · 2026-11-12
   - [DeepMind：自演化智能体能否持续学习？](../../updates/2026-10-29/#deepmind) · 2026-10-29
   - [CLE：LLM 智能体长时程持续学习与经验学习基准](../../updates/2026-10-29/#cle-llm) · 2026-10-29
2. **经验保留不等于迁移**：经验能解题不等于可迁移或适合训练；应以重置、未见任务及对当前优化的边际贡献筛选，并回测旧任务终局质量。
   - [STUN-Bench：真未见工具路由评测](../../updates/2026-11-25/#stun-bench) · 2026-11-25
   - [E2L：梯度对齐经验演化](../../updates/2026-11-25/#e2l) · 2026-11-25
   - [AutoSECO：可迁移求解技能演化](../../updates/2026-11-25/#autoseco) · 2026-11-25
   - [From Acting to Learning：优化器感知梯度选样](../../updates/2026-11-23/#from-acting-to-learning) · 2026-11-23
   - [SIM：自改进记忆支持持续递归优化](../../updates/2026-11-17/#sim) · 2026-11-17
   - [上下文与权重协同适应](../../updates/2026-11-17/#item-54) · 2026-11-17
   - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
   - [编程智能体能否在持续演化中避免遗忘？](../../updates/2026-11-06/#item-94) · 2026-11-06
   - [Continual AutoResearch：智能体能否跨任务持续学习](../../updates/2026-11-06/#continual-autoresearch) · 2026-11-06
3. **路由隔离任务干扰**：任务规模扩大时，按原型或任务簇路由隔离的适配器、提示与记忆，比共享参数连续更新更稳；模块独立训练后还须验证接口兼容性。
   - [独立蒸馏记忆检索策略](../../updates/2026-11-25/#item-105) · 2026-11-25
   - [CSPD：可组合软提示蒸馏](../../updates/2026-11-25/#cspd) · 2026-11-25
   - [BiSpace：双空间解耦知识编辑](../../updates/2026-11-20/#bispace) · 2026-11-20
   - [ENA：物理索引式专家记忆](../../updates/2026-11-18/#ena) · 2026-11-18
   - [Microfitting：文档隔离式缓存适配](../../updates/2026-11-17/#microfitting) · 2026-11-17
   - [Meta提出路由式持续学习架构Routed CL](../../updates/2026-11-03/#meta-routed-cl) · 2026-11-03
   - [CaRE：扩展至300+任务的持续学习架构](../../updates/2026-11-03/#care-300) · 2026-11-03
   - [CaLLM：基于非参数适配器路由的持续适应](../../updates/2026-10-29/#callm) · 2026-10-29
4. **更新前控险后巩固**：持续更新前先界定行为变化及覆盖风险，更新中以增益—保留联合选参并约束参数几何，更新后用教师或回放巩固；晋升须验收域外累积能力。
   - [增益保留联合调参](../../updates/2026-11-26/#item-34) · 2026-11-26
   - [InstructReplay：自答回放保留通用能力](../../updates/2026-11-25/#instructreplay) · 2026-11-25
   - [CurvDelta：低曲率约束式学习遗忘](../../updates/2026-11-20/#curvdelta) · 2026-11-20
   - [Safe AD：动态预算蒸馏与成本重加权](../../updates/2026-11-18/#safe-ad) · 2026-11-18
   - [G-CAST：治理式持续自训练](../../updates/2026-11-16/#g-cast) · 2026-11-16
   - [FireGate：持续强化学习微调前的行为变化界定](../../updates/2026-11-12/#firegate) · 2026-11-12
   - [Agentic-OPD：通过在策略蒸馏恢复智能体遗忘能力](../../updates/2026-11-12/#agentic-opd) · 2026-11-12
   - [在策略蒸馏用于强化学习后能力巩固的泛化局限](../../updates/2026-11-06/#item-14) · 2026-11-06
   - [DRAP：面向物理 AI 持续学习的动力学风险自适应可塑性](../../updates/2026-11-06/#drap-ai) · 2026-11-06
   - [Google「睡眠框架」缓解大模型灾难性遗忘](../../updates/2026-10-31/#google) · 2026-10-31
   - [Google 为大模型引入「睡眠」机制，缓解灾难性遗忘](../../updates/2026-10-30/#google) · 2026-10-30
5. **选择性测试时适应**：测试时更新须筛查样本、伪标签及会话历史的可靠性与恶意操纵，并核验代理目标对齐最终指标；优先用可控监督，在收益或安全性转负前停止。
   - [P-TAP：会话适配器渐进投毒](../../updates/2026-11-25/#p-tap) · 2026-11-25
   - [RoTTT：旋转监督式测试时训练](../../updates/2026-11-24/#rottt) · 2026-11-24
   - [Normal-Only TTA：正常更新不保证检测增益](../../updates/2026-11-19/#normal-only-tta) · 2026-11-19
   - [SpeCal：隐藏态谱双层校准](../../updates/2026-11-17/#specal) · 2026-11-17
   - [TRUER：面向测试时强化学习的错误感知奖励校正](../../updates/2026-11-12/#truer) · 2026-11-12
   - [SCALAR：控制时序伪标签边际以稳定在线测试时适应](../../updates/2026-11-12/#scalar) · 2026-11-12
   - [无需训练的视觉语言模型主动测试时适应](../../updates/2026-11-12/#item-201) · 2026-11-12
   - [多数投票伪标签在测试时强化学习中的可靠性](../../updates/2026-11-12/#item-176) · 2026-11-12
   - [核定律预测多数投票测试时强化学习的答案锁定](../../updates/2026-11-12/#item-143) · 2026-11-12
   - [MIRA：互信息引导的可靠测试时适应校准](../../updates/2026-11-03/#mira) · 2026-11-03
   - [Timbre：面向无标签多模态测试时强化学习的可靠性感知调和共识](../../updates/2026-10-30/#timbre) · 2026-10-30
   - [PORTAL：何时应在测试时干预？](../../updates/2026-10-29/#portal) · 2026-10-29
6. **相关记忆选择修订**：在线记忆应按任务状态与效用选择写入层级、强度和位置，并用结果或反事实修订；显式管理版本、期限、衰减与拒答，避免旧经验污染。
   - [XMind：跨记忆反事实复核](../../updates/2026-11-25/#xmind) · 2026-11-25
   - [WASP：流式权重个性化](../../updates/2026-11-25/#wasp) · 2026-11-25
   - [NavTTT：导航条件式分层参数记忆](../../updates/2026-11-23/#navttt) · 2026-11-23
   - [LoCo-WAM：测试时训练延展长上下文](../../updates/2026-11-23/#loco-wam) · 2026-11-23
   - [F³：形适融经验利用](../../updates/2026-11-20/#item-76) · 2026-11-20
   - [参数记忆：可控持久与衰减](../../updates/2026-11-20/#item-63) · 2026-11-20
   - [Experience Rot：静默变更引发经验腐化](../../updates/2026-11-18/#experience-rot) · 2026-11-18
   - [ReHarness：反向修订式持续学习](../../updates/2026-11-17/#reharness) · 2026-11-17
   - [Anchor：跨层循环状态增强长上下文检索](../../updates/2026-11-06/#anchor) · 2026-11-06
   - [Falcon快速权重注意力实现持续学习](../../updates/2026-11-02/#falcon) · 2026-11-02
   - [Select-TTT：查询条件化的选择性快速权重更新](../../updates/2026-10-29/#select-ttt) · 2026-10-29
7. **先测可恢复能力边界**：RLVR常提高已有路径采样率；训练前应以完整解支持度和原子技能覆盖定位边界，并估算能否采到足量成功事件，单测困难样本。
   - [Shift Adapter：逐层恒定偏移适配](../../updates/2026-11-26/#shift-adapter) · 2026-11-26
   - [成功组数预测强化学习起飞](../../updates/2026-11-20/#item-44) · 2026-11-20
   - [基础能力状态如何预测强化学习后训练效果](../../updates/2026-11-12/#item-140) · 2026-11-12
   - [TOPSD：从可教前缀进行多语言推理蒸馏](../../updates/2026-11-08/#topsd) · 2026-11-08
   - [验证器强化学习相对 SFT 的边际价值评估](../../updates/2026-11-08/#sft) · 2026-11-08
   - [RLVR只优化解题路径选择，未提升内在推理能力](../../updates/2026-11-06/#rlvr-4) · 2026-11-06
   - [RLVR 训练中的首因偏差](../../updates/2026-11-06/#rlvr) · 2026-11-06
   - [ReSI-Math：探索可恢复能力边界以高效提升数学推理](../../updates/2026-11-06/#resi-math) · 2026-11-06
8. **同时报告采样曲线**：RLVR提升pass@1可能伴随覆盖坍缩和pass@k反转；应报告完整采样曲线，并用难度自适应正则或周期重置KL参考策略保持覆盖。
   - [后训练策略优化理论：覆盖坍缩与参考策略重置](../../updates/2026-11-12/#item-64) · 2026-11-12
   - [KAPPO：控制 LLM 后训练中的策略锐化](../../updates/2026-11-06/#kappo-llm) · 2026-11-06
   - [RLVR 无免费午餐：pass@1 提升必付出 pass@k 代价](../../updates/2026-10-30/#rlvr-pass-1-pass-k) · 2026-10-30
9. **核验推理机制泛化**：高分可能来自数据污染、验证器暴露、文本捷径或检索复用；应用污染校正、标准盲化、过程证据核验、模态消融和难度外推确认迁移机制。
   - [VFR：验证式失败驱动修复](../../updates/2026-11-26/#vfr) · 2026-11-26
   - [多玩家社交游戏：可验证社会智能训练](../../updates/2026-11-25/#item-63) · 2026-11-25
   - [RDQA：原始证据轨迹核验](../../updates/2026-11-24/#rdqa) · 2026-11-24
   - [Benchleaking：基准污染校正评测](../../updates/2026-11-18/#benchleaking) · 2026-11-18
   - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
   - [示例解答会掩盖自生成训练数据中的规则组合能力成本](../../updates/2026-11-12/#item-106) · 2026-11-12
   - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
   - [RLVR 推理策略并非都能泛化：可控方程求解案例](../../updates/2026-11-06/#rlvr-2) · 2026-11-06
   - [视频 RLVR 中的捷径放大与感知不确定性坍缩](../../updates/2026-10-29/#rlvr-2) · 2026-10-29
10. **后训练泛化看数据**：“SFT记忆、RL泛化”并非定律；对齐预算后，数据来源、规模、解法与输出结构及评判器类别偏差更关键，窄域优化还须回放未奖励能力。
    - [PRIOR：调用前推理保留工具能力](../../updates/2026-11-26/#prior) · 2026-11-26
    - [IRTIQA：自进化跨语言迁移评测](../../updates/2026-11-26/#irtiqa) · 2026-11-26
    - [强化学习解耦推理形式与功能](../../updates/2026-11-23/#item-53) · 2026-11-23
    - [科学论证迁移：显式脚手架训练](../../updates/2026-11-23/#item-25) · 2026-11-23
    - [盲点迁移：评判偏见类别泛化](../../updates/2026-11-20/#item-65) · 2026-11-20
    - [奖励范围之外：多语言后训练中的能力漂移](../../updates/2026-11-14/#item-46) · 2026-11-14
    - [强化学习后印度语言任务的增益与退化](../../updates/2026-11-14/#item-35) · 2026-11-14
    - [重新审视“RL 泛化、SFT 记忆”：SFT 数据的关键作用](../../updates/2026-11-13/#rl-sft-sft) · 2026-11-13
    - [验证器强化学习相对 SFT 的边际价值评估](../../updates/2026-11-08/#sft) · 2026-11-08
    - [特征干扰视角下的 SFT 普遍能力退化理论与 AEGIS 损失](../../updates/2026-11-06/#sft-aegis) · 2026-11-06
    - [金融小型决策模型：专业化坍缩与混合语料修复](../../updates/2026-11-06/#item-102) · 2026-11-06
11. **合成循环需外源刷新**：递归使用模型生成数据会侵蚀稀有知识并传递隐性偏好；须持续注入独立核验信息，并以稀有知识和分布形态等多指标监测。
    - [视觉语言模型中的潜意识学习与隐性偏好迁移](../../updates/2026-11-13/#item-14) · 2026-11-13
    - [自训练中的有序 Rényi 熵交叉：丰富度不等于均匀度](../../updates/2026-11-12/#r-nyi) · 2026-11-12
    - [批量生成具有意外副作用的训练数据](../../updates/2026-11-08/#item-46) · 2026-11-08
    - [谁为模型复制的知识买单？Rogers 悖论下的模型坍缩](../../updates/2026-11-05/#rogers) · 2026-11-05
12. **按交互预算训练**：多轮RL主要增强错误恢复和长程韧性，且收益依赖交互预算；训练时混合预算，并按预算分层报告表现。
    - [多轮强化学习究竟提升了 LLM 智能体的什么能力？](../../updates/2026-11-05/#llm-3) · 2026-11-05
13. **脚手架能力回迁**：脚手架演化应对比成功与失败轨迹，使干预锚定当前执行证据；部署前还须将其诱发的能力回迁到无辅助策略。
    - [TransHarness：可迁移脚手架演化](../../updates/2026-11-26/#transharness) · 2026-11-26
    - [RLM-27B：脚手架组合泛化](../../updates/2026-11-24/#rlm-27b) · 2026-11-24
    - [自进化多模态智能体的跨场景综述与迁移分析](../../updates/2026-11-12/#item-68) · 2026-11-12
    - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
    - [Harness-S：从同源脚手架学习实现可泛化智能体训练](../../updates/2026-11-06/#harness-s) · 2026-11-06
    - [The Trinity：能力驱动的多模态智能体递归自我改进](../../updates/2026-10-29/#the-trinity) · 2026-10-29
14. **增益归因控制成本**：开发集增益应扣除选择噪声及额外交互、词元、时延与能耗，并区分加速收敛和提高上限；高分近饱和时优先比较单位任务成本。
    - [Sleep：循环前向提升上下文适应](../../updates/2026-11-25/#sleep) · 2026-11-25
    - [Gemini 4 Neon：低成本高分推理](../../updates/2026-11-25/#gemini-4-neon) · 2026-11-25
    - [Gemini 4 Hydrogen：半量Token高分推理](../../updates/2026-11-21/#gemini-4-hydrogen-token) · 2026-11-21
    - [Grokking：顿悟不改训练能效走势](../../updates/2026-11-16/#grokking) · 2026-11-16
    - [RSI 持续进步评测：从 RSIBench-Data 到 S³Gym](../../updates/2026-11-13/#rsi-rsibench-data-s-gym) · 2026-11-13
    - [示例解答会掩盖自生成训练数据中的规则组合能力成本](../../updates/2026-11-12/#item-106) · 2026-11-12
    - [数据策展究竟提升上限还是加速训练？](../../updates/2026-10-29/#item-73) · 2026-10-29
    - [BiPA：用二部归因重新评估智能体技能优化](../../updates/2026-10-29/#bipa) · 2026-10-29
15. **抽象评测拆解瓶颈**：流体智能评测应按未见规则、任务模式及长度与深度外推分级，并拆分感知、规划、记忆和表征瓶颈；总分提升不足以证明抽象迁移。
    - [Grokking：训练前定位泛化子空间](../../updates/2026-11-25/#grokking) · 2026-11-25
    - [AgriManager：农业策略模式迁移评测](../../updates/2026-11-24/#agrimanager) · 2026-11-24
    - [ORION：精确规范状态监督](../../updates/2026-11-23/#orion) · 2026-11-23
    - [Rigel-Ladon：选项数准确率定律](../../updates/2026-11-20/#rigel-ladon) · 2026-11-20
    - [SelfImprove-Bench：自改进智能体泛化能力评测](../../updates/2026-11-06/#selfimprove-bench) · 2026-11-06
    - [SARBLOH：空间感知主导 ARC-AGI-3 交互推理](../../updates/2026-11-06/#sarbloh-arc-agi-3) · 2026-11-06
    - [规模化 ConceptARC：评估推理模型的概念理解](../../updates/2026-11-06/#conceptarc) · 2026-11-06
<!-- experience-seen: 2026-11-20/agnes-harness 2026-11-20/bispace 2026-11-20/curvdelta 2026-11-20/item-44 2026-11-20/item-63 2026-11-20/item-65 2026-11-20/item-76 2026-11-20/rigel-ladon 2026-11-20/stability-gap 2026-11-21/gemini-4-hydrogen-token 2026-11-23/from-acting-to-learning 2026-11-23/item-25 2026-11-23/item-53 2026-11-23/loco-wam 2026-11-23/navttt 2026-11-23/orion 2026-11-23/structure-over-scale 2026-11-24/agrimanager 2026-11-24/rdqa 2026-11-24/rlm-27b 2026-11-24/rottt 2026-11-25/autoseco 2026-11-25/cspd 2026-11-25/e2l 2026-11-25/gemini-4-neon 2026-11-25/grokking 2026-11-25/instructreplay 2026-11-25/item-105 2026-11-25/item-109 2026-11-25/item-63 2026-11-25/p-tap 2026-11-25/sleep 2026-11-25/stun-bench 2026-11-25/vla 2026-11-25/wasp 2026-11-25/xmind 2026-11-26/grokking 2026-11-26/irtiqa 2026-11-26/item-34 2026-11-26/omniact 2026-11-26/prior 2026-11-26/shift-adapter 2026-11-26/transharness 2026-11-26/vfr 2026-11-27/i2vt -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [SEAL](https://github.com/Continual-Intelligence/SEAL) — Self-Adapting Language Models：模型自生成微调数据与更新指令
- [marc](https://github.com/ekinakyurek/marc) — ARC 上测试时训练（TTT）的参考实现
- [ttt-lm-pytorch](https://github.com/test-time-training/ttt-lm-pytorch) — 测试时训练层（Learning to Learn at Test Time）
- [ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) — 强调流体智能的抽象推理基准
- [limit-of-RLVR](https://github.com/LeapLabTHU/limit-of-RLVR) — "RL 是否真正扩展推理边界"的实验代码
- [Intuitor](https://github.com/sunblaze-ucb/Intuitor) — 以自信度为内在奖励、无外部奖励的 RL
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 弱到强泛化实验代码
- [Avalanche](https://github.com/ContinualAI/avalanche) — 持续学习端到端库

**论文**
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](https://arxiv.org/abs/2501.17161)
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837) — RLVR 的能力边界
- [RL's Razor: Why Online Reinforcement Learning Forgets Less](https://arxiv.org/abs/2509.04259) — 在线 RL 偏向 KL 最小解因而遗忘更少
- [Learning to Reason without External Rewards](https://arxiv.org/abs/2505.19590) — Intuitor，自信度驱动的泛化
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) — SEAL
- [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://arxiv.org/abs/2411.07279) — ARC 上 TTT 大幅提升
- [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620)
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390)
- [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) — 记忆到泛化的相变
- [Continual Learning of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2404.16789)
