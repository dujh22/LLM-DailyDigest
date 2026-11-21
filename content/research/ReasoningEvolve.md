+++
title = 'ReasoningEvolve'
proposer = '杜晋华'
since = '2026-11-21'
date = 2026-11-21T00:00:00+08:00
draft = false
toc = true
+++

# ReasoningEvolve

> 研究方向：**推理时自进化**——让 LLM 在推理服务（inference serving）过程中，利用真实用户交互产生的前向计算本身完成任务自适应，在不做反向传播、不引入额外训练开销的前提下"边推理、边进化"。

## 研究范畴

推理时自进化（inference-time self-evolution）关注的是把"推理"从单纯消耗算力的服务环节，变成模型持续适配下游任务的进化环节。随着 LLM 大规模部署，推理服务已成为 AI 能耗增长的主要来源，而服务过程中由真实用户交互产生的海量前向计算几乎全部被"用完即弃"。主流的自适应手段分两类：一是调优技术（SFT、LoRA / Adapter 等 PEFT、提示调优、前缀调优、测试时训练），依赖反向传播，相比推理本身有显著额外的显存与算力开销；二是知识增强技术（ICL、RAG、提示工程、激活引导、工具调用），只改输入或注入信息，不触碰模型内部权重。本方向关注第三条路线——**仅前向（forward-only）学习**：只依赖前向传播完成权重层面的自适应，使自适应可以直接嵌入推理服务链路。代表工作是 NeurIPS 2026 论文 *Efficient LLM Adaptation with Forward-Only Passes*（隆德大学 & Google DeepMind）：它对选定权重矩阵做 SVD 分解，各 SVD 分量引起的激活之和恢复标准前向传播；再用各分量激活相对隐藏状态的**角度集中度**衡量其贡献是"分散"还是"集中"，据此只靠前向传播找出离散度最高、最值得降秩的权重矩阵，裁掉高阶分量、保留低阶分量。与基于梯度的 LASER-Grad 相比峰值显存更低、加速比更高；与穷举搜索的 LASER 相比加速比更高、精度相当，并在高达 57B 参数的 LLaMA2、DeepSeek V1、Mistral、Qwen2 及其 MoE 版本和多模态模型上验证了泛化性。社区关注的核心问题包括：仅前向信号（激活几何、零阶估计、局部损失、进化策略）能否替代梯度给出可靠的更新方向；如何利用用户偏好或自标注验证数据在服务期间在线、低成本地持续适配；以及"推理即训练"如何与推理基础设施、安全与稳定性约束协同。与 [EvolveLRM]({{< relref "/research/EvolveLRM" >}}) 关注推理模型的能力进化、[LogicEvolve]({{< relref "/research/LogicEvolve" >}}) 关注逻辑推理能力、[CacheEvolve]({{< relref "/research/CacheEvolve" >}}) 关注推理时缓存记忆的自适应管理、[InfraEvolve]({{< relref "/research/InfraEvolve" >}}) 关注基础设施演化不同，ReasoningEvolve 关心的是：**推理服务的前向计算本身能否成为模型进化的燃料**。

## 研究挑战

- 无梯度的更新信号：仅前向方法（前向梯度、零阶优化、进化策略）在深层、大规模模型上的可扩展性仍是难题——方差大、需要多次扰动或多轮前向，如何像角度集中度这样找到"一次前向就够用"的结构性信号。
- 从"一次性适配"到"持续进化"：现有代表工作本质上是一次性搜索出待降秩的权重矩阵，离"服务期间在线实时适应"还有距离；如何在连续流量下增量更新、避免灾难性遗忘与漂移。
- 监督信号来源：服务过程中缺少标注，需依赖用户偏好、隐式反馈或自标注验证数据，噪声与偏差会直接写进权重。
- 与推理基础设施的耦合：前缀缓存、连续批处理、多租户共享同一权重的前提，与"按任务 / 用户群体改权重"天然冲突，需要新的权重版本管理与调度设计。
- 压缩与适配的边界：选择性去除 SVD 高阶分量既是压缩也能提升下游精度（LASER 现象），其机理、适用任务与失效条件尚不清楚。
- 评测与安全：如何证明在线自适应带来的是真实任务收益而非对局部分布的过拟合；用户交互驱动的权重修改如何防止投毒、偏见放大与对齐退化。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录推理时 / 测试时自适应相关工作。

## 相关工作

**代码 / 框架**
- [LASER](https://github.com/pratyushasharma/laser) — 层选择性降秩：去除权重 SVD 高阶分量可提升推理精度，本方向代表工作的对比基线
- [MeZO](https://github.com/princeton-nlp/MeZO) — 仅用前向传播的零阶优化微调 LLM
- [Transformer²（self-adaptive-llms）](https://github.com/SakanaAI/self-adaptive-llms) — Sakana AI：推理时调整权重奇异值实现自适应

**论文**
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

**综述 / 报道**
- [NeurIPS 2026 | 如何让LLM在推理中不断进化](https://mp.weixin.qq.com/s/WgJNWHiUImUiQmKu-mYevQ) — 机器之心对 *Efficient LLM Adaptation with Forward-Only Passes* 的中文解读。需注意：标题中的"推理"指推理服务（inference），而非逻辑 / 数学推理（reasoning）；论文方法是一次性的仅前向搜索与降秩，"服务期间在线实时适应、持续进化"是文末对未来应用的展望，而非论文已验证的结果
