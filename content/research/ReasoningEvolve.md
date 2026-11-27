+++
title = 'ReasoningEvolve'
proposer = '杜晋华'
since = '2026-11-21'
date = 2026-11-21T00:00:00+08:00
draft = false
toc = true
+++

# ReasoningEvolve

> 研究方向：**推理中的自进化**——"推理"取双重含义：既指推理服务（inference）过程，让模型利用服务中的前向计算与真实交互持续自适应；也指思维推理（reasoning）过程，让模型在思考、求解、反思中不断改进自己的推理能力与推理策略。两者共同指向"边推理、边进化"。

## 研究范畴

ReasoningEvolve 把"推理"从一次性消耗算力的环节，变成模型持续进化的环节，涵盖两条相互交织的主线。

**一、推理服务中的自进化（inference-time adaptation）。** 随着 LLM 大规模部署，推理服务已成为 AI 能耗增长的主要来源，而服务过程中由真实用户交互产生的海量前向计算几乎全部被"用完即弃"。主流自适应手段要么是依赖反向传播的调优技术（SFT、LoRA / Adapter 等 PEFT、提示调优、测试时训练），相比推理本身有显著额外开销；要么是只改输入、不触碰权重的知识增强技术（ICL、RAG、提示工程、激活引导）。本方向关注第三条路线——**仅前向（forward-only）学习**：只依赖前向传播完成权重层面的自适应，使其可以直接嵌入推理服务链路。代表工作是 NeurIPS 2026 论文 *Efficient LLM Adaptation with Forward-Only Passes*（隆德大学 & Google DeepMind）：对选定权重矩阵做 SVD 分解，用各分量激活相对隐藏状态的**角度集中度**衡量其贡献是"分散"还是"集中"，只靠前向传播找出离散度最高、最值得降秩的权重矩阵，裁掉高阶分量、保留低阶分量；与基于梯度的 LASER-Grad 相比峰值显存更低、加速比更高，与穷举搜索的 LASER 相比加速比更高、精度相当，并在高达 57B 参数的多种稠密、MoE 与多模态模型上验证了泛化性。

**二、思维推理中的自进化（reasoning self-evolution）。** 模型在推理过程中产生的思维链、尝试、失败与验证结果，本身就是进化的素材：STaR 类方法用自己生成的正确推理自举训练；测试时扩展（test-time scaling）通过搜索、多数投票、自我验证与反思让单次推理变强；TTRL、无外部奖励 RL、Absolute Zero 等工作在没有标注的情况下，用自一致性、自信度或自我出题在测试时 / 零数据条件下强化推理；Buffer of Thoughts、Dynamic Cheatsheet、ReasoningBank 等把推理经验沉淀为可复用的"思维模板 / 推理记忆"，让模型越用越会想。

两条主线的交汇点是：**推理时产生的计算与经验，能否以低成本、可持续、安全的方式回写到模型（权重、记忆或策略）中**。社区关注的核心问题包括：仅前向信号（激活几何、零阶估计、进化策略）与无监督推理信号（自一致性、自信度、可验证奖励）能否替代梯度与人工标注给出可靠的更新方向；服务期间如何利用用户偏好或自标注数据在线持续适配；推理时算力与训练时算力如何权衡；以及"推理即训练"如何与推理基础设施、安全与稳定性约束协同。与 [EvolveLRM]({{< relref "/research/EvolveLRM" >}}) 聚焦大推理模型的 RL 后训练、[LogicEvolve]({{< relref "/research/LogicEvolve" >}}) 聚焦逻辑推理能力、[CacheEvolve]({{< relref "/research/CacheEvolve" >}}) 聚焦推理时缓存记忆、[MemoryEvolve]({{< relref "/research/MemoryEvolve" >}}) 聚焦外部记忆系统、[InfraEvolve]({{< relref "/research/InfraEvolve" >}}) 聚焦基础设施演化不同，ReasoningEvolve 关心的是：**推理过程本身——无论是服务中的前向计算还是思考中的推理轨迹——能否成为模型进化的燃料**。

## 研究挑战

**推理服务侧**
- 无梯度的更新信号：前向梯度、零阶优化、进化策略在深层大模型上方差大、需多次扰动或多轮前向；如何像角度集中度这样找到"一次前向就够用"的结构性信号。
- 从"一次性适配"到"持续进化"：现有代表工作本质上是一次性搜索与降秩，离服务期间在线实时适应还有距离；如何在连续流量下增量更新、避免灾难性遗忘与漂移。
- 与推理基础设施的耦合：前缀缓存、连续批处理、多租户共享同一权重的前提，与"按任务 / 用户群体改权重"天然冲突，需要新的权重版本管理与调度设计。
- 压缩与适配的边界：选择性去除 SVD 高阶分量既是压缩也能提升下游精度（LASER 现象），其机理、适用任务与失效条件尚不清楚。

**思维推理侧**
- 无监督信号的可靠性：自一致性、自信度、熵等内在信号可能强化"自信的错误"，导致多数投票塌缩与熵坍缩，推理多样性下降。
- 推理经验的抽象与迁移：哪些推理轨迹值得沉淀、如何从具体解法提炼可泛化的策略，避免记忆污染与过拟合。
- 推理效率：测试时扩展带来过度思考（overthinking）与成本膨胀，需要按难度自适应分配思考预算。
- 忠实度与可验证性：思维链未必反映真实计算过程，自我验证本身也可能出错，自进化可能放大推理链上的错误传播。

**共性**
- 监督信号来源：服务过程缺少标注，依赖用户偏好、隐式反馈或自标注验证数据，噪声与偏差会直接写进权重或记忆。
- 评测与安全：如何证明推理中的进化带来的是真实任务收益而非局部分布过拟合；交互驱动的自修改如何防止投毒、偏见放大与对齐退化。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理评测与自进化平台，可用于检验推理自进化的真实收益。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录推理时 / 测试时自适应与推理自进化相关工作。

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
1. **无梯度能力写入**：前向激活与可解析表示代数可直接驱动局部、门控的低秩改写；其上限取决于目标子空间可分性及冻结表征覆盖度。
   - [vSFT：语言监督式测试时调优](../../updates/2026-11-26/#vsft) · 2026-11-26
   - [FWSP：确定性前向权重编辑](../../updates/2026-11-26/#fwsp) · 2026-11-26
   - [Don't Train It, Write It：智能体直写模型能力](../../updates/2026-11-24/#don-t-train-it-write-it) · 2026-11-24
   - [Weight-Space Programming：无梯度写入ICL](../../updates/2026-11-23/#weight-space-programming-icl) · 2026-11-23
   - [Forward-Only Passes：角度集中度引导降秩](../../updates/2026-11-21/#forward-only-passes) · 2026-11-21
2. **测试时更新安全**：测试时参数可作为离窗记忆，但监督宜来自可控变换等确定标签；用户交互驱动更新时，必须隔离并审计更新通道。
   - [P-TAP：会话适配器渐进投毒](../../updates/2026-11-25/#p-tap) · 2026-11-25
   - [RoTTT：旋转监督式测试时训练](../../updates/2026-11-24/#rottt) · 2026-11-24
   - [LoCo-WAM：测试时训练延展长上下文](../../updates/2026-11-23/#loco-wam) · 2026-11-23
3. **累积式自改进**：独立重采样不会形成自进化；应以不确定性定位失败分叉，保留局部正确步骤，并将异质失败抽象为可迁移经验或写回权重。
   - [DART：不确定性引导轨迹改写](../../updates/2026-11-26/#dart) · 2026-11-26
   - [TT-RSI：测试时递归自我改进](../../updates/2026-11-25/#tt-rsi) · 2026-11-25
   - [LCE：失败模式多样性诊断](../../updates/2026-11-25/#lce) · 2026-11-25
4. **推理资源动态分配**：缓存、注意力和推理深度不宜静态配置；用不确定性、冗余度与中间状态按层按样本分配计算，更易兼顾精度和延迟。
   - [DFly2：共享目标稀疏性的推测解码](../../updates/2026-11-26/#dfly2) · 2026-11-26
   - [层级执行控制：中间状态驱动计算分配](../../updates/2026-11-25/#item-128) · 2026-11-25
   - [Turnout：自适应注意力切换](../../updates/2026-11-23/#turnout) · 2026-11-23
   - [RoCoKV：置信冗余感知缓存压缩](../../updates/2026-11-20/#rocokv) · 2026-11-20
5. **最小充分推理状态**：长链应压缩为对后续转移充分的紧凑状态；训练时以局部续写分布一致性检验充分性，并用精确执行语义抑制深度漂移。
   - [TruSuCo：局部续写驱动的状态压缩](../../updates/2026-11-25/#trusuco) · 2026-11-25
   - [Markovian Reasoning LLM：结构化状态缓存压缩](../../updates/2026-11-24/#markovian-reasoning-llm) · 2026-11-24
   - [ORION：精确规范状态监督](../../updates/2026-11-23/#orion) · 2026-11-23
6. **预算塑造停止策略**：固定长度上限会被内化为停止策略并限制测试时扩展；稳定控制多个推理档位需状态级、档位专属监督。
   - [推理强度训练：密集目标分离强度层级](../../updates/2026-11-25/#item-56) · 2026-11-25
   - [Budget Internalization：固定预算内化约束](../../updates/2026-11-20/#budget-internalization) · 2026-11-20
7. **强化学习起飞条件**：SFT可只建立输出结构，再由强化学习发现推理功能；采样须有足够成功事件以推翻预训练先验，组规模宜按梯度估计不确定性调节。
   - [U-Statistics-Powered LLM Reasoning：悲观估计自适应组规模](../../updates/2026-11-26/#u-statistics-powered-llm-reasoning) · 2026-11-26
   - [强化学习解耦推理形式与功能](../../updates/2026-11-23/#item-53) · 2026-11-23
   - [成功组数预测强化学习起飞](../../updates/2026-11-20/#item-44) · 2026-11-20
8. **策略多样性维护**：对已会题目继续做离模探索并自蒸馏不同正确解，可将冗余正确奖励转成策略多样性，避免坍缩到单一路径。
   - [ROAM-GRPO：离模策略挖掘](../../updates/2026-11-20/#roam-grpo) · 2026-11-20
9. **局部信用分配**：奖励应归因到造成结果的决策分叉、输出片段或模型模块，而非整段响应平均传播；熵排名和输出锚点可低成本定位。
   - [BRIAR：分岔引导的信念平滑](../../updates/2026-11-26/#briar) · 2026-11-26
   - [MSPO：模块特定信用分配](../../updates/2026-11-25/#mspo) · 2026-11-25
   - [AnchorCredit：输出锚定式信用分配](../../updates/2026-11-25/#anchorcredit) · 2026-11-25
   - [CreditFilter：熵秩校准的词元信用分配](../../updates/2026-11-23/#creditfilter) · 2026-11-23
10. **优化信号共适应**：固定奖励或训练策略代理会随实际轨迹失准；应交替校准奖励与策略，按执行风险收缩更新，并将结果信号蒸馏为词元级监督。
    - [VOPD：验证器引导的稠密蒸馏](../../updates/2026-11-25/#vopd) · 2026-11-25
    - [EPRO：不完美预测下的鲁棒策略优化](../../updates/2026-11-25/#epro) · 2026-11-25
    - [ELGO：循环外推自教师强化学习](../../updates/2026-11-25/#elgo) · 2026-11-25
    - [PAIR-MED：策略奖励交替优化](../../updates/2026-11-21/#pair-med) · 2026-11-21
11. **推理过程忠实性**：答案正确或思维链可读都不能证明过程忠实；评测应结合预测依赖、内部表征，并对可形式化结果使用独立语义解析与可弃权确定性检查。
    - [FOL-Proof：确定性语义验证](../../updates/2026-11-26/#fol-proof) · 2026-11-26
    - [CLR：无痕隐藏目标推理](../../updates/2026-11-25/#clr) · 2026-11-25
    - [APRM：内部注意力过程奖励](../../updates/2026-11-25/#aprm) · 2026-11-25
    - [二维推理：语义图量化推理忠实与效率](../../updates/2026-11-24/#item-67) · 2026-11-24
12. **外部能力内化**：教师分布、工具观察和专用中间令牌可作为可撤除脚手架，经蒸馏或表示监督内化为单遍决策、无工具感知或骨干能力。
    - [S-Mind：空间令牌内化多视图几何](../../updates/2026-11-26/#s-mind) · 2026-11-26
    - [Tool-to-Self：视觉工具能力内化](../../updates/2026-11-24/#tool-to-self) · 2026-11-24
    - [GLiDE：推理蒸馏单遍决策](../../updates/2026-11-20/#glide) · 2026-11-20
13. **领域推理脚手架**：领域推理不会仅靠规模自动迁移；可先用自动生成的前置任务培养通用变换能力，再以显式分解、证据需求或工具反馈维持跨步语义。
    - [ThinkMorph-SSL：前置任务扩展交错推理](../../updates/2026-11-26/#thinkmorph-ssl) · 2026-11-26
    - [科学论证迁移：显式脚手架训练](../../updates/2026-11-23/#item-25) · 2026-11-23
    - [Space-X：证据链驱动空间自进化](../../updates/2026-11-21/#space-x) · 2026-11-21
14. **参数适配几何**：参数高效适配应优先设计可达更新流形并匹配预训练结构；持续合并知识时，宜在跨样本对齐的生成潜空间组合，而非直接叠加最终参数。
    - [Latent Merger：潜空间LoRA合并](../../updates/2026-11-26/#latent-merger-lora) · 2026-11-26
    - [Structure Over Scale：结构化适配防秩坍缩](../../updates/2026-11-23/#structure-over-scale) · 2026-11-23
15. **成本敏感评测**：高难推理基准接近饱和后，应同时报告准确率、推理Token和单位任务成本；等精度下的计算压缩更能区分系统价值。
    - [Gemini 4 Neon：低成本高分推理](../../updates/2026-11-25/#gemini-4-neon) · 2026-11-25
    - [Gemini 4 Hydrogen：半量Token高分推理](../../updates/2026-11-21/#gemini-4-hydrogen-token) · 2026-11-21
<!-- experience-seen: 2026-11-20/budget-internalization 2026-11-20/glide 2026-11-20/item-44 2026-11-20/roam-grpo 2026-11-20/rocokv 2026-11-21/claude-lean 2026-11-21/forward-only-passes 2026-11-21/gemini-4-hydrogen-token 2026-11-21/pair-med 2026-11-21/space-x 2026-11-23/alps-lab 2026-11-23/bel 2026-11-23/creditfilter 2026-11-23/item-25 2026-11-23/item-53 2026-11-23/loco-wam 2026-11-23/orion 2026-11-23/structure-over-scale 2026-11-23/turnout 2026-11-23/weight-space-programming-icl 2026-11-24/don-t-train-it-write-it 2026-11-24/future-opsd 2026-11-24/item-67 2026-11-24/markovian-reasoning-llm 2026-11-24/rottt 2026-11-24/rtc 2026-11-24/tool-to-self 2026-11-25/9-4 2026-11-25/anchorcredit 2026-11-25/aprm 2026-11-25/clr 2026-11-25/elgo 2026-11-25/epro 2026-11-25/gemini-4-neon 2026-11-25/item-128 2026-11-25/item-56 2026-11-25/lce 2026-11-25/mspo 2026-11-25/p-tap 2026-11-25/trusuco 2026-11-25/tt-rsi 2026-11-25/videcide 2026-11-25/vopd 2026-11-26/briar 2026-11-26/cogentic 2026-11-26/dart 2026-11-26/dfly2 2026-11-26/fol-proof 2026-11-26/fwsp 2026-11-26/latent-merger-lora 2026-11-26/openai-math-ai 2026-11-26/s-mind 2026-11-26/thinkmorph-ssl 2026-11-26/u-statistics-powered-llm-reasoning 2026-11-26/vsft 2026-11-27/docseam -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [LASER](https://github.com/pratyushasharma/laser) — 层选择性降秩：去除权重 SVD 高阶分量可提升推理精度，仅前向自适应代表工作的对比基线
- [MeZO](https://github.com/princeton-nlp/MeZO) — 仅用前向传播的零阶优化微调 LLM
- [Transformer²（self-adaptive-llms）](https://github.com/SakanaAI/self-adaptive-llms) — Sakana AI：推理时调整权重奇异值实现自适应

**论文：推理服务中的自适应**
- [Efficient LLM Adaptation with Forward-Only Passes (NeurIPS 2026)](https://arxiv.org/abs/2611.10610) — 利用 SVD 分量激活的角度集中度做仅前向搜索，定位并降秩权重矩阵；[NeurIPS 页面](https://neurips.cc/virtual/2026/loc/atlanta/poster/148809)
- [Backpropagation-Free Learning: On the Emergence of Forward-Only Algorithms](https://doi.org/10.36227/techrxiv.176739859.93468234/v1) — 同一团队的仅前向学习综述（TechRxiv 2026）
- [The Truth is in There: Layer-Selective Rank Reduction (LASER)](https://arxiv.org/abs/2312.13558) — 选择性降秩提升 LLM 推理能力
- [Fine-Tuning Language Models with Just Forward Passes (MeZO)](https://arxiv.org/abs/2305.17333) — 零阶优化，显存与推理相当
- [Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark](https://arxiv.org/abs/2402.11592) — 零阶优化微调 LLM 的系统基准
- [Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning](https://arxiv.org/abs/2509.24372) — 进化策略在十亿级参数上直接微调 LLM
- [The Forward-Forward Algorithm](https://arxiv.org/abs/2212.13345) — Hinton 提出的以两次前向替代反向传播的学习算法
- [Transformer-Squared: Self-adaptive LLMs](https://arxiv.org/abs/2501.06252) — 推理时按任务调节奇异值的自适应 LLM
- [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943) — 模型自生成微调数据与更新指令实现自适应
- [Test-Time Training on Nearest Neighbors for LLMs](https://arxiv.org/abs/2305.18466) — 测试时检索近邻并微调的 TTT 方法
- [Tent: Fully Test-time Adaptation by Entropy Minimization](https://arxiv.org/abs/2006.10726) — 经典测试时自适应
- [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620) — 把测试时训练内化为序列层
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663) — 测试时学习记忆的神经记忆模块
- [ASVD: Activation-aware SVD for Compressing LLMs](https://arxiv.org/abs/2312.05821) — 激活感知的 SVD 压缩
- [SVD-LLM: Truncation-aware SVD for LLM Compression](https://arxiv.org/abs/2403.07378) — 截断感知的 SVD 压缩
- [PiSSA: Principal Singular Values and Singular Vectors Adaptation](https://arxiv.org/abs/2404.02948) — 基于主奇异分量的 PEFT
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — 依赖反向传播的低秩适配基线

**论文：思维推理中的自进化**
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) — 用自己生成的正确推理自举训练，推理自进化的经典起点
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL](https://arxiv.org/abs/2501.12948) — 纯 RL 激发长链推理与自我反思
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) — 在无标注测试数据上以多数投票为奖励进行 RL
- [Learning to Reason without External Rewards](https://arxiv.org/abs/2505.19590) — 以模型自信度为内在奖励强化推理
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) — 自我出题、自我求解的零数据推理自进化
- [The Entropy Mechanism of RL for Reasoning Language Models](https://arxiv.org/abs/2505.22617) — 推理 RL 中的熵坍缩与探索机制
- [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) — 推理时算力的最优扩展可胜过扩大参数
- [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703) — 计算最优的测试时扩展策略
- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) — 预算强制（budget forcing）控制思考长度
- [Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs](https://arxiv.org/abs/2412.21187) — 推理模型的过度思考问题
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — 推理时自我反馈迭代改进
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 以语言反思形式积累经验
- [Buffer of Thoughts: Thought-Augmented Reasoning with LLMs](https://arxiv.org/abs/2406.04271) — 沉淀并复用高层思维模板
- [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952) — 推理时持续积累可复用解题策略
- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) — 从成功与失败中提炼推理记忆，实现测试时自进化

**综述 / 报道**
- [NeurIPS 2026 | 如何让LLM在推理中不断进化](https://mp.weixin.qq.com/s/WgJNWHiUImUiQmKu-mYevQ) — 机器之心对 *Efficient LLM Adaptation with Forward-Only Passes* 的中文解读，属于本方向"推理服务"一侧。需注意：论文方法是一次性的仅前向搜索与降秩，"服务期间在线实时适应、持续进化"是文末对未来应用的展望，而非论文已验证的结果
