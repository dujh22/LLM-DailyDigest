+++
title = 'EvolveLRM'
proposer = '杜晋华'
since = '2026-01-09'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# EvolveLRM

> 研究方向：**大推理模型（LRM）的自我进化**——通过 RL / 自我博弈等让推理模型持续提升。

## 研究范畴

大推理模型（Large Reasoning Model, LRM）的自我进化，聚焦于通过强化学习 / 自我博弈 / 过程奖励 / 树搜索等范式，让"System 2"式长链推理模型在推理质量上持续提升。本方向涵盖：RL 后训练、自我博弈、过程 / 结果奖励、搜索增强训练、长思维链与推理时计算。社区关注的核心问题包括：RL 训练带来的能力提升能否泛化到分布外任务、奖励稀疏 / 奖励作弊与"伪推理"如何识别与缓解、探索—利用的平衡与思维链忠实度（faithfulness），以及训练效率与推理时算力的权衡。

## 研究挑战

- 训练稳定性、奖励设计与奖励黑客。
- 高昂的算力与数据成本。
- 评测上限（benchmark saturation）与防污染。
- 推理安全（越狱、长链中的错误累积）。

## 自研项目

- [EvolveLRM](https://github.com/dujh22/EvolveLRM) — 面向逻辑推理的自我进化闭环框架，自动跑通"评测 → 数据选择 → 训练 → 再评测"；含 Evaluator / DataMaker / Trainer 三模块与 Planner / Adapter / Logger，支持 SFT 与 RL（PPO/GRPO/LoRA）及底层训练框架热插拔。

## 自研洞察

<!-- human-only:start 自研洞察｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

*（待人工补充）*

<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

1. 直接基于 Pi 或者 Claude 或者 OpenAI 的 Agent SDK 封装，甚至把一个已经跑的还不错的 Agent 拷贝下来去魔改，都不是困难的事情。
2. 在Qwen3系列的四个参数规模（1.7B、4B、8B、14B），泛化并非SFT目标的固定属性，而是优化充分度、数据质量与结构、以及基模型能力共同作用的产物。
3. 记忆是用 Markdown 存的；检索用的是 SQLite；结构通过 AX Tree 暴露出来；你可以读、可以改、可以迁移；LangGraph将状态建模为流经图节点的类型字典，用reducer合并更新。

<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->

1. **稀疏奖励先破零**：困难题若整组采样全错，标准RLVR没有有效信号；先用相关易题、策略兼容引导或局部纠正制造足量成功事件，再逐步撤除辅助。
   - [DART：不确定性引导轨迹改写](../../updates/2026-11-26/#dart) · 2026-11-26
   - [成功组数预测强化学习起飞](../../updates/2026-11-20/#item-44) · 2026-11-20
   - [ASH：激活引导消除提示错配](../../updates/2026-11-19/#ash) · 2026-11-19
   - [STONE：踏脚石式无标签自蒸馏](../../updates/2026-11-17/#stone) · 2026-11-17
   - [RuACT：将失活评分准则转化为自适应批评者与教师](../../updates/2026-11-12/#ruact) · 2026-11-12
   - [实时捕获并纠正 LLM 推理错误](../../updates/2026-11-12/#llm-2) · 2026-11-12
   - [AutoScaffold：AI 自动生成自适应训练脚手架](../../updates/2026-11-12/#autoscaffold-ai) · 2026-11-12
   - [RLVR 困难提示的零到一跃迁诊断与引导](../../updates/2026-11-06/#rlvr-3) · 2026-11-06
   - [PIVOT：基于在线教师纠正的渐进式干预](../../updates/2026-10-30/#pivot) · 2026-10-30
   - [H²R：基于分层提示奖励的数学推理强化学习](../../updates/2026-10-30/#h-r) · 2026-10-30
   - [PICO：全失败采样下的策略兼容联合解码](../../updates/2026-10-29/#pico) · 2026-10-29
   - [Guided-RLVR：以引导式探索提升可验证奖励强化学习](../../updates/2026-10-29/#guided-rlvr) · 2026-10-29
2. **抑制策略过锐化**：只追求pass@1会压低覆盖并反转大预算pass@k；监控成功与失败轨迹的有效熵，用参考策略重置或有效多样性正则保留可解路径。
   - [THRIFTY：预算约束推理数据合成](../../updates/2026-11-24/#thrifty) · 2026-11-24
   - [ROAM-GRPO：离模策略挖掘](../../updates/2026-11-20/#roam-grpo) · 2026-11-20
   - [有效熵对齐 LLM 探索，破解多样性幻觉](../../updates/2026-11-13/#llm) · 2026-11-13
   - [RCEA：RLVR 中的奖励条件熵分配诊断](../../updates/2026-11-12/#rcea-rlvr) · 2026-11-12
   - [后训练策略优化理论：覆盖坍缩与参考策略重置](../../updates/2026-11-12/#item-64) · 2026-11-12
   - [KAPPO：控制 LLM 后训练中的策略锐化](../../updates/2026-11-06/#kappo-llm) · 2026-11-06
   - [奖励预算缓解 LLM 推理强化学习的过早收敛](../../updates/2026-11-05/#llm-4) · 2026-11-05
   - [RLVR 无免费午餐：pass@1 提升必付出 pass@k 代价](../../updates/2026-10-30/#rlvr-pass-1-pass-k) · 2026-10-30
   - [PSN-RLVR：参数空间噪声恢复强化学习模型探索能力](../../updates/2026-10-30/#psn-rlvr) · 2026-10-30
3. **能力难度分离调度**：混合训练会优先强化已会题；结合完整解支持、原子技能覆盖、成功率与更新后风险，把rollout预算投向可学边界。
   - [BRIAR：分岔引导的信念平滑](../../updates/2026-11-26/#briar) · 2026-11-26
   - [THRIFTY：预算约束推理数据合成](../../updates/2026-11-24/#thrifty) · 2026-11-24
   - [基础能力状态如何预测强化学习后训练效果](../../updates/2026-11-12/#item-140) · 2026-11-12
   - [GRPO 中稠密奖励值得其 Token 成本吗？](../../updates/2026-11-12/#grpo-token) · 2026-11-12
   - [ICRPM以前瞻风险预测优化Rollout任务采样](../../updates/2026-11-08/#icrpm-rollout) · 2026-11-08
   - [RLVR 训练中的首因偏差](../../updates/2026-11-06/#rlvr) · 2026-11-06
   - [ReSI-Math：探索可恢复能力边界以高效提升数学推理](../../updates/2026-11-06/#resi-math) · 2026-11-06
   - [FADE：面向在线 RLVR 的能力—难度分解调度](../../updates/2026-11-06/#fade-rlvr) · 2026-11-06
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
4. **多信号优化先校准**：多任务或多验证器信号不应未经校准硬压成单分数；保留帕累托不可比关系，并约束冲突更新方向，可减少尺度偏差与参数耦合导致的坍缩。
   - [PMOPD：子空间保护式多教师蒸馏](../../updates/2026-11-25/#pmopd) · 2026-11-25
   - [Structure Over Scale：结构化适配防秩坍缩](../../updates/2026-11-23/#structure-over-scale) · 2026-11-23
   - [RLCDR：校准式决策奖励](../../updates/2026-11-20/#rlcdr) · 2026-11-20
   - [POLPO：多验证器帕累托策略优化](../../updates/2026-11-17/#polpo) · 2026-11-17
   - [TACE：多模态 RLVR 的分布式奖励校准与预算中性信用分配](../../updates/2026-10-30/#tace-rlvr) · 2026-10-30
   - [跨任务耦合驱动无监督 RLVR 策略坍缩](../../updates/2026-10-29/#rlvr) · 2026-10-29
5. **验证奖励防投机**：验证器缺口的方向与暴露度比平均误差更关键；重点修复会高估错误且策略常触达的漏洞，并持续校准裁判置信度与类别偏差。
   - [暴露度预判奖励作弊](../../updates/2026-11-25/#item-123) · 2026-11-25
   - [RLCDR：校准式决策奖励](../../updates/2026-11-20/#rlcdr) · 2026-11-20
   - [盲点迁移：评判偏见类别泛化](../../updates/2026-11-20/#item-65) · 2026-11-20
   - [Optimistic Verifiers：精确过程预言机审计](../../updates/2026-11-18/#optimistic-verifiers) · 2026-11-18
   - [诚实是一场竞赛：可验证奖励强化学习何时诱导模型虚张声势](../../updates/2026-11-14/#item-44) · 2026-11-14
   - [跨提示共享如何抑制或放大奖励作弊](../../updates/2026-11-12/#item-92) · 2026-11-12
   - [基于监控器的强化学习奖励作弊干预设计](../../updates/2026-11-12/#item-177) · 2026-11-12
   - [RcRL：利用生成—验证鸿沟改进开放域强化学习](../../updates/2026-11-05/#rcrl) · 2026-11-05
   - [FORK：精确率目标缓解评分标准强化学习中的奖励投机](../../updates/2026-10-29/#fork) · 2026-10-29
6. **正确不等于忠实**：结果正确或可读CoT不等于内部推理忠实；用反事实依赖测试与内部激活监测，独立评估RL、蒸馏和架构对可监控性的影响。
   - [CLR：无痕隐藏目标推理](../../updates/2026-11-25/#clr) · 2026-11-25
   - [任务方向引导式隐状态旋转](../../updates/2026-11-20/#item-80) · 2026-11-20
   - [OpenAI：模型生命周期因素如何影响 CoT 可监控性](../../updates/2026-11-12/#openai-cot) · 2026-11-12
   - [后训练如何影响语言模型的显式算法推理](../../updates/2026-11-12/#item-80) · 2026-11-12
   - [Chain of Faith：策略内部奖励增强推理依赖](../../updates/2026-11-06/#chain-of-faith) · 2026-11-06
   - [视频 RLVR 中的捷径放大与感知不确定性坍缩](../../updates/2026-10-29/#rlvr-2) · 2026-10-29
7. **泛化须测策略变化**：RLVR常只重排已有解法概率，评分提升不证明新能力；须与受控SFT比较，并用难度外推、结构变换、互补任务和独立安全评测检验。
   - [强化学习解耦推理形式与功能](../../updates/2026-11-23/#item-53) · 2026-11-23
   - [科学论证迁移：显式脚手架训练](../../updates/2026-11-23/#item-25) · 2026-11-23
   - [RSI Arena：人类反馈校准递归改进](../../updates/2026-11-16/#rsi-arena) · 2026-11-16
   - [验证器强化学习相对 SFT 的边际价值评估](../../updates/2026-11-08/#sft) · 2026-11-08
   - [RLVR只优化解题路径选择，未提升内在推理能力](../../updates/2026-11-06/#rlvr-4) · 2026-11-06
   - [RLVR 推理策略并非都能泛化：可控方程求解案例](../../updates/2026-11-06/#rlvr-2) · 2026-11-06
8. **后训练防能力漂移**：RL与递归蒸馏可能损伤奖励外能力，也会固化已撤回的中间错误；用答案或自生成简报做巩固，并配基础能力回放与独立OOD评测。
   - [自幻觉记忆：后训练固化错误事实](../../updates/2026-11-23/#item-49) · 2026-11-23
   - [B-OPSD：自生成简报蒸馏](../../updates/2026-11-17/#b-opsd) · 2026-11-17
   - [RL训练：大模型能力漂移](../../updates/2026-11-15/#item-1) · 2026-11-15
   - [奖励范围之外：多语言后训练中的能力漂移](../../updates/2026-11-14/#item-46) · 2026-11-14
   - [强化学习后印度语言任务的增益与退化](../../updates/2026-11-14/#item-35) · 2026-11-14
   - [TOPSD：从可教前缀进行多语言推理蒸馏](../../updates/2026-11-08/#topsd) · 2026-11-08
   - [Shuffled OPSD：语义一致性何时损害在策略自蒸馏](../../updates/2026-11-06/#shuffled-opsd) · 2026-11-06
   - [在策略蒸馏用于强化学习后能力巩固的泛化局限](../../updates/2026-11-06/#item-14) · 2026-11-06
   - [RISE：交错 RLVR 与在策略蒸馏实现递归自我改进](../../updates/2026-10-31/#rise-rlvr) · 2026-10-31
9. **自生成任务要可验**：零外部数据自进化依赖可独立验证的任务与监督；除成功率和优势外，可用隐藏态群体结构筛除低支持轨迹，避免自证循环。
   - [STONE：踏脚石式无标签自蒸馏](../../updates/2026-11-17/#stone) · 2026-11-17
   - [SpeCal：隐藏态谱双层校准](../../updates/2026-11-17/#specal) · 2026-11-17
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [LongZero：零外部数据增强长上下文推理](../../updates/2026-10-30/#longzero) · 2026-10-30
10. **测试时扩展保多样**：测试时扩展应按语义策略而非文本分支计数，保留跨深度候选并继承前次有效推理；选择端用双向或逐项验证，避免投票固化错误。
    - [TT-RSI：测试时递归自我改进](../../updates/2026-11-25/#tt-rsi) · 2026-11-25
    - [LPC-MCTS：表征共享式探索计数](../../updates/2026-11-18/#lpc-mcts) · 2026-11-18
    - [AGPV：智能体引导过程验证](../../updates/2026-11-17/#agpv) · 2026-11-17
    - [PreG：短前缀置信度引导的并行测试时采样](../../updates/2026-11-13/#preg) · 2026-11-13
    - [深度候选源：循环测试时扩展的组合分配](../../updates/2026-11-12/#item-222) · 2026-11-12
    - [多数投票伪标签在测试时强化学习中的可靠性](../../updates/2026-11-12/#item-176) · 2026-11-12
    - [BiVerify：双向验证闭环驱动数学自我纠错](../../updates/2026-11-12/#biverify) · 2026-11-12
    - [TTT-Consolidate：以测试时训练整合多智能体推理](../../updates/2026-11-06/#ttt-consolidate) · 2026-11-06
    - [Test-Time Self-Play：无需验证器的测试时扩展](../../updates/2026-11-06/#test-time-self-play) · 2026-11-06
    - [验证器引导的自一致性：不完美生成器与验证器下的测试时推理](../../updates/2026-11-06/#item-32) · 2026-11-06
11. **推理预算动态停止**：固定长度删失会把成本约束内化为能力边界；应学习“思考价值”动态停止，并先分解未结束样本构成，再判断预算增加是否导致过度思考。
    - [推理强度训练：密集目标分离强度层级](../../updates/2026-11-25/#item-56) · 2026-11-25
    - [Budget Internalization：固定预算内化约束](../../updates/2026-11-20/#budget-internalization) · 2026-11-20
    - [Conserved Verdicts：承诺-裁决差识别过度思考](../../updates/2026-11-18/#conserved-verdicts) · 2026-11-18
    - [思考的价值：混合决策模型学习何时推理](../../updates/2026-11-14/#item-22) · 2026-11-14
    - [bf16 循环状态舍入导致混合推理模型过度思考](../../updates/2026-11-12/#bf16) · 2026-11-12
    - [代码生成中的推理轨迹溢出：显式推理模型实证研究](../../updates/2026-11-08/#item-48) · 2026-11-08
    - [Concise-9B：去除推理轨迹中的冗余思考](../../updates/2026-11-06/#concise-9b) · 2026-11-06
    - [LoCo：基于本地偏好学习的推理压缩](../../updates/2026-11-05/#loco) · 2026-11-05
12. **潜在推理留控制口**：连续潜变量可承载推理并支持测试时优化，但工具调用与过程控制仍需显式Token或推理锚点作为接口。
    - [任务方向引导式隐状态旋转](../../updates/2026-11-20/#item-80) · 2026-11-20
    - [RELOAD：通过层循环扩展类型化决策模型推理](../../updates/2026-11-08/#reload) · 2026-11-08
    - [TAC-CoT：交错显式 Token 增强工具化隐式思维链](../../updates/2026-11-06/#tac-cot-token) · 2026-11-06
    - [LARC：统一多模态模型的连续空间潜在推理](../../updates/2026-11-03/#larc) · 2026-11-03
    - [LatentWeave：面向多模态推理的测试时潜变量优化](../../updates/2026-10-30/#latentweave) · 2026-10-30
13. **信用分配分层细化**：长链信用应与语义段、决策分叉、输出组件和责任模块对齐；用决策器或证据增益低成本稠密化，并让过程奖励随策略分布校准。
    - [BRIAR：分岔引导的信念平滑](../../updates/2026-11-26/#briar) · 2026-11-26
    - [VOPD：验证器引导的稠密蒸馏](../../updates/2026-11-25/#vopd) · 2026-11-25
    - [MSPO：模块特定信用分配](../../updates/2026-11-25/#mspo) · 2026-11-25
    - [ELGO：循环外推自教师强化学习](../../updates/2026-11-25/#elgo) · 2026-11-25
    - [APRM：内部注意力过程奖励](../../updates/2026-11-25/#aprm) · 2026-11-25
    - [AnchorCredit：输出锚定式信用分配](../../updates/2026-11-25/#anchorcredit) · 2026-11-25
    - [SH-PRM：语义分段短程监督](../../updates/2026-11-23/#sh-prm) · 2026-11-23
    - [DM-PRM：决策模型零样本过程奖励](../../updates/2026-11-23/#dm-prm) · 2026-11-23
    - [CreditFilter：熵秩校准的词元信用分配](../../updates/2026-11-23/#creditfilter) · 2026-11-23
    - [PAIR-MED：策略奖励交替优化](../../updates/2026-11-21/#pair-med) · 2026-11-21
    - [ECA：证据增益式信用分配](../../updates/2026-11-19/#eca) · 2026-11-19
    - [AGPV：智能体引导过程验证](../../updates/2026-11-17/#agpv) · 2026-11-17
    - [MCPO：基于边际犹豫度的 Token 信用分配](../../updates/2026-11-12/#mcpo-token) · 2026-11-12
    - [实时捕获并纠正 LLM 推理错误](../../updates/2026-11-12/#llm-2) · 2026-11-12
    - [即插即用验证器解耦过程奖励，稳定长程智能体推理](../../updates/2026-11-12/#item-167) · 2026-11-12
    - [GRPO 中稠密奖励值得其 Token 成本吗？](../../updates/2026-11-12/#grpo-token) · 2026-11-12
    - [TACE：多模态 RLVR 的分布式奖励校准与预算中性信用分配](../../updates/2026-10-30/#tace-rlvr) · 2026-10-30
    - [SCARL：序列置信度对齐强化学习](../../updates/2026-10-30/#scarl) · 2026-10-30
    - [H²R：基于分层提示奖励的数学推理强化学习](../../updates/2026-10-30/#h-r) · 2026-10-30
14. **信息增益训练求知**：检索或实验设计中，奖励信息增益而非只奖最终答案，可把昂贵搜索摊销为可泛化的行动选择策略。
    - [ECA：证据增益式信用分配](../../updates/2026-11-19/#eca) · 2026-11-19
    - [推理 LLM 中序贯实验设计的摊销学习](../../updates/2026-10-30/#llm) · 2026-10-30
    - [强化学习激励大语言模型自主学习长篇教材](../../updates/2026-10-30/#item-61) · 2026-10-30
15. **群体估计控偏稳方差**：奖励依赖同组答案时，GRPO基线会扭曲协作目标；应采用无偏组目标，并按悲观方差估计自适应调整组规模。
    - [U-Statistics-Powered LLM Reasoning：悲观估计自适应组规模](../../updates/2026-11-26/#u-statistics-powered-llm-reasoning) · 2026-11-26
    - [群体依赖奖励下，GRPO会演变为零和锦标赛](../../updates/2026-11-06/#grpo) · 2026-11-06

<!-- experience-seen: 2026-11-19/ash 2026-11-19/eca 2026-11-19/option-grpo 2026-11-20/budget-internalization 2026-11-20/item-44 2026-11-20/item-65 2026-11-20/item-80 2026-11-20/multiagentbench 2026-11-20/openai-rsi 2026-11-20/rlcdr 2026-11-20/roam-grpo 2026-11-21/pair-med 2026-11-23/creditfilter 2026-11-23/ctrl-gpu 2026-11-23/dm-prm 2026-11-23/item-25 2026-11-23/item-49 2026-11-23/item-53 2026-11-23/sh-prm 2026-11-23/structure-over-scale 2026-11-24/pbpt 2026-11-24/thrifty 2026-11-25/anchorcredit 2026-11-25/aprm 2026-11-25/clr 2026-11-25/elgo 2026-11-25/epro 2026-11-25/item-123 2026-11-25/item-56 2026-11-25/mspo 2026-11-25/pmopd 2026-11-25/tt-rsi 2026-11-25/vopd 2026-11-26/briar 2026-11-26/dart 2026-11-26/u-statistics-powered-llm-reasoning -->

<!-- research-experience:end -->

## 相关工作

**代码 / 框架**

- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 从零数据自进化的推理 LLM（ICLR 2026）
- [SE-Agent](https://github.com/JARVIS-Xs/SE-Agent) — 智能体自进化框架
- [DeepScaleR](https://github.com/agentica-project/deepscaler) — 小模型大推理 RL 训练框架，1.5B 模型在 AIME 超越 o1
- [Reasoning-Self-Evolution-Survey](https://github.com/cs-holder/Reasoning-Self-Evolution-Survey) — 配套复杂推理自进化综述的资源仓库
- [Awesome-Agentic-Reasoning](https://github.com/weitianxin/Awesome-Agentic-Reasoning) — Agent 推理论文分类整理（含自我进化专题）
- [self-improvement-llm](https://github.com/Zesearch/self-improvement-llm) — 系统级自我改进语言模型技术整理

**论文**

- [LLM Reasoning Abilities Under Non-Ideal Conditions After RL-Fine-Tuning](https://arxiv.org/abs/2508.04848)
- [The Impact of Quantization on Large Reasoning Model RL](https://arxiv.org/abs/2511.15694)
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化方法综述
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM 作为自身裁判生成偏好数据自我改进（被引 996+）
- [STaR: Bootstrapping Reasoning With Self-Taught Reasoning](https://arxiv.org/abs/2203.14465) — 经典自我推理引导方法（被引 1959+）
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) — 零数据自进化推理（被引 157）
- [Debate, Train, Evolve (DTE)](https://arxiv.org/abs/2505.15734) — 多 Agent 辩论轨迹训练实现推理自进化（EMNLP 2025）
- [ALIVE: Awakening LLM Reasoning via Adversarial Self-Evolution](https://arxiv.org/abs/2602.05472) — 对抗性自我进化激活推理能力
- [A Survey of Reasoning Large Language Models](https://arxiv.org/abs/2502.17419) — System 1 到 System 2 视角的推理 LLM 综述（被引 415）
- [Towards Large Reasoning Models: A Survey of Reinforced Self-Training](https://arxiv.org/abs/2501.09686) — 强化自我训练方法综述
- [On the Limits of Self-Improving in Large Language Models](https://arxiv.org/abs/2601.05280) — 自我改进理论极限分析
