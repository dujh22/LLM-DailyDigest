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
*（暂无，随日报自动积累）*
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
