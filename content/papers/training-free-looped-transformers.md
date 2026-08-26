+++
title = '无需训练的循环 Transformer｜Training-Free Looped Transformers'
date = 2026-08-26T00:00:00+08:00
draft = false
toc = true

[extra]
paper = 'https://arxiv.org/abs/2605.23872'
authors = 'Lizhang Chen, Jonathan Li, Chen Liang, Ni Lao, Qiang Liu'
published = '2026-05-22'
+++

# Training-Free Looped Transformers（无需训练的循环 Transformer）

> **一句话速读**：用一个轻量推理时 wrapper，把冻结 checkpoint 中连续的中间层块循环执行——不做任何微调、继续训练或架构改动，即可让现成大模型普遍涨点（Qwen3-4B MMLU-Pro **+2.64 pp**，87% 测试单元格非负）。

## 论文信息

- **arXiv**：[https://arxiv.org/abs/2605.23872](https://arxiv.org/abs/2605.23872)（2026-05-22）
- **作者**：Lizhang Chen, Jonathan Li, Chen Liang, Ni Lao, Qiang Liu
- **方向标签**：免训练 ‧ 循环架构 ‧ 推理时计算 ‧ 深度循环（looping） ‧ ODE 数值视角

## Q1：这篇论文试图解决什么问题？

核心问题：**如何在不进行任何额外训练、微调、持续训练或架构修改的情况下，将循环（recurrence/looping）机制应用于现成的（frozen）预训练 Transformer，以提升推理性能。**具体针对四个挑战：

1. **训练时循环与现成模型的不匹配**。传统循环 Transformer（Universal Transformers、Deep Equilibrium Models 等）需要在训练阶段就把循环结构嵌入架构和权重；而绝大多数公开发布的模型（Qwen3、Llama-3.2、DeepSeek 等）按标准多阶段流水线（持续预训练 → SFT → RLHF/DPO）训练发布，并未考虑循环结构，现成 checkpoint 无法直接套用这些方法。
2. **朴素循环导致性能退化**。直接在推理时对冻结模型块朴素重复应用（naive reapplication）通常显著掉点：预训练模型的后循环层（post-loop layers）被训练为接收特定时间步（t=1）的隐藏状态，朴素循环会把状态推进到 t=K，造成分布偏移。
3. **无需训练的推理时计算扩展**。探索"训练无关"（training-free）的替代方案：通过推理时的轻量 wrapper，对冻结 checkpoint 中连续中间层块多次迭代，在不更新任何参数的情况下暴露潜在的推理时计算能力（latent inference-time computation）。
4. **MoE 模型的特殊挑战**。对 MoE 架构，简单的块级循环（block-mode）会导致专家路由在迭代间剧烈变化（routing thrash）并累积噪声；论文提出层模式（layer-mode）迭代来解决，确保每层的专家选择在整个循环过程中保持一致。

## Q2：与相关工作有何区别？

**CoT 类推理时计算**：本文方法不修改输出序列长度，而是在**单次前向传播内**通过循环中间层增加每 token 的计算量。

**数值分析方法**：

- 残差块作为 ODE 前向欧拉步：将预归一化 Transformer 层视为残差 ODE ẋ = F_g(x) 的离散化，步长 h=1。
- 固定点加速算法：Anderson Acceleration、Heavy-ball、Aitken Δ² 外推；以及高阶 Runge-Kutta 求解器（RK4、Heun、中点法）。
- **关键发现**：这些经典固定点加速方法在循环 Transformer 块上并不稳健，因为该块并非压缩映射（contractive map）；相比之下，简单的阻尼子步或 K 阶段 Runge-Kutta 更有效。

**训练无关的深度操作**（ShortGPT 等层跳过/删除/交换/重复研究显示中间层有冗余和鲁棒性）：本文是**首个**将中间层循环与层模式迭代（针对 MoE 路由稳定性）结合，并在现代多架构 checkpoint（密集、MoE、MLA）上验证的训练无关方法。

## Q3：论文如何解决这个问题？

### 1. 将 Transformer 块重新解释为 ODE 积分步

对循环窗口算子 g = L_b ∘ ⋯ ∘ L_a，定义残差场 F_g(x) := g(x) − x，对应 ODE ẋ = F_g(x)。单次前向传播 g(x) = x + F_g(x) 等价于步长 h=1 的前向欧拉步。

核心问题识别：朴素循环执行 K 次完整步长（h=1）迭代，相当于积分到时间 t=K，但后循环层只在 t=1 附近训练过——这是分布外问题。

**正确视角**：循环不应是推进到 t=K，而是对**同一积分终点 x(t=1)** 的更精确近似——把一个大步拆成 K 个步长 h=1/K 的阻尼子步：

$$
x_{k+1} = \left(1-\tfrac{1}{K}\right)x_k + \tfrac{1}{K}\,g(x_k)
$$

### 2. 迭代模式：块模式 vs 层模式

- **块模式（block-mode）**：整块层循环 K 次后再进入后续层；适合密集模型。
- **层模式（layer-mode）**：逐层迭代，每层的（MoE）路由决策在循环内保持一致；解决路由抖动，在 MoE 模型上显著优于块模式。
- K 阶段 Runge-Kutta（Algorithm 3）通过参数 β 平衡原始输出与细化轨迹。

### 3. 窗口选择：深度分数规则

- 超过 1.7B 参数的模型，最优窗口中心位于层数的 **0.45–0.60 分数深度**（上半部分，0.43–0.71 区间内）。
- 次 1B 模型最优窗口前移（0.25–0.56），避开后期头部特化层。
- 标准配置：**4 层窗口（n=4）**，中间偏后位置（如 Qwen3-4B 的第 [15–18] 层）。

### 4. KV 缓存处理：快照/恢复协议

- 循环体内每次评估不写入 KV 缓存（或用快照长度截断）。
- 循环结束后执行一次存储（stash）阶段，用策略 c ∈ {FIRST, LAST} 写入单一规范的 KV 条目，确保缓存中每层恰好保留一个条目，与原始模型一致。

## Q4：论文做了哪些实验？

在 **45 个（模型，基准）单元格**上系统评估，覆盖 7 个模型家族、多种架构与任务类型。

### 模型与架构覆盖

| 模型家族         | 规模                                | 架构特点          | 类型      |
| ---------------- | ----------------------------------- | ----------------- | --------- |
| Qwen3            | 0.6B / 1.7B / 4B（Base & Instruct） | 标准 MHA          | 密集      |
| Qwen3-MoE        | 30B-A3B-Instruct                    | MoE               | 稀疏      |
| Qwen1.5-MoE      | A2.7B-Chat                          | MoE（24 层）      | 稀疏/蒸馏 |
| Llama-3.2        | 1B / 3B-Instruct                    | 标准 MHA          | 密集/蒸馏 |
| DeepSeek-V2-Lite | 16B / 2.4B 激活                     | MLA + 64 专家 MoE | 稀疏      |
| Moonlight        | 16B-A3B-Instruct                    | MLA + MoE         | 稀疏      |

### 基准测试

以知识密集型多项选择任务为主：MMLU-Pro（5-shot CoT）、GPQA-Main（0-shot）、ARC-Challenge（25-shot）、CommonsenseQA（7-shot）、OpenBookQA（0-shot）、SciQ、MedMCQA、C-Eval 等；另含语言建模困惑度（LAMBADA）与生成任务（GSM8K、MBPP）。

### 主要结果（单一开箱即用配置：中间 4 层、3 阶段 Runge-Kutta、密集用块模式 / MoE 用层模式、无逐单元格调参）

**显著提升（>2 pp）**：

- Qwen3-4B-Instruct：MMLU-Pro **+2.64 pp**，GPQA-Main **+2.01 pp**
- Qwen1.5-MoE-A2.7B：ARC-Challenge **+2.30 pp**

**其他代表性提升**：

- Qwen3-30B-A3B-Instruct：CommonsenseQA +1.14 pp
- Moonlight-16B-A3B：OpenBookQA +1.20 pp
- Llama-3.2-3B-Instruct：GPQA-Main +1.12 pp，MMLU-Pro +0.71 pp

**总体统计**：87% 的测试单元格非负（60% 显著提升、27% 中性、13% 下降）。

### 关键消融

- **窗口大小与位置**：n=4 层最佳；n≥6 性能急剧下降（−0.82 pp）；全网循环灾难性崩溃（−27.73 pp）。最优窗口中心位于 0.45–0.60 分数深度（次 1B 除外）。
- **迭代模式**：MoE 上层模式显著优于块模式（Moonlight ARC-C：+0.51 vs −1.45 pp）。
- **循环策略**：朴素循环（无阻尼）单调下降，K=6 时 −17.71 pp；Uniform Loop 在 K≥6 后失效；本文方法（阻尼欧拉/RK）在 K ∈ {1,…,24} 内保持稳定。
- **高阶数值方法**（Appendix E，40+ 配置）：Midpoint/Heun/RK4、Anderson 加速、Heavy-ball、Aitken Δ² 均未超过简单阻尼欧拉 / K 阶段 RK，证实循环块非压缩映射。
- **缓存策略**（Appendix N）：cache=first 适合长提示 CoT（MMLU-Pro +2.64）；cache=last 适合短结构化生成（MBPP +0.80）；cache=none 灾难性失败（−23.40 pp）。
- **迭代次数 K**：K=2 到 K=24 稳定；朴素循环 K=4 时困惑度从 13 暴涨至 1054。

### 跨架构泛化

- 30B 规模验证（Qwen3-30B-A3B-Instruct，48 层 MoE，固定配置 [22–24] 层、K=2 欧拉）：12 个基准中 11 个非负（CommonsenseQA +1.14、SciQ +0.20、MMLU-flex +0.79）。
- 逐学科分析（Appendix H）：增益集中在 STEM 与定量推理（大学物理 +5.88 pp、高中数学 +5.56 pp）；部分简单人文科目小幅下降。

### 失败案例（Appendix G，论文诚实披露）

- 朴素 K=4 循环：困惑度 13 → 1054。
- 过宽窗口（n=28，全网）：性能崩溃。
- Anderson 加速 K=8：−18.06 pp（证明非压缩性）。
- 次 1B 模型在部分知识 MC 任务上失效（如 Llama-3.2-1B 的 MMLU −0.63 pp）。

### 计算成本（Appendix I）

- Prefill-only 循环（bypass 模式）：无墙钟时间开销（−1.5%，噪声范围内）。
- 完整解码循环：K=3 时约 **+21.6% 延迟**（相当于在 4 层窗口上多跑两次）。

## Q5：有什么可以进一步探索的点？

1. **自适应与动态循环机制**：基于隐藏状态收敛性（‖x_{k+1}−x_k‖ < ε）或置信度阈值的动态停止准则替代固定 K；按输入复杂度自适应调整循环窗口；分层循环策略（不同层不同 K，非均匀时间离散化）。
2. **训练与推理的混合范式**：仅微调循环策略中的少量参数（β 插值权重、步长 α），主体保持冻结；循环感知蒸馏；持续预训练阶段渐进引入循环。
3. **非解码器架构扩展**：编码器-解码器（T5/BART）；状态空间模型（Mamba/RetNet——线性注意力是否支持类似 ODE 解释）；多模态架构（CLIP/LLaVA 的跨模态对齐层循环）。
4. **长上下文与记忆机制**：循环作为上下文压缩（将历史信息压缩进固定大小循环状态）；长度外推；循环迭代替代部分历史 KV 缓存的内存-计算新权衡。
5. **理论分析与可解释性**：刻画 F_g(x) 的李普希茨性质与曲率，解释固定点加速为何失效；用 tuned lens / 因果中介分析追踪循环中信息流动的子空间；探索 K 增大时"精炼 → 幻觉"的相变点。
6. **失败案例的深入理解**：次 1B 模型失效机制（层冗余不足？表示维度限制？）；"循环适用性"的元特征（哪些任务/学科受益）；蒸馏小模型 vs 原生预训练模型的循环敏感性差异。
7. **硬件与系统优化**：speculative execution / 并行化多迭代步降低墙钟时间；轻量循环近似（小网络预测循环终点）；利用迭代确定性模式的 GPU 能效优化。
8. **与其他推理方法协同**：循环作为 CoT 的"内循环"形成层次化推理；循环迭代中集成工具调用；多路径循环 + 自一致性投票。

> 其中**自适应循环机制**与**跨架构扩展**（特别是状态空间模型）可能具有最高的即时研究价值，理论刻画则有助于建立更坚实的数值分析基础。

## Q6：总结

**方法**：Training-Free Looped Transformers 允许直接对冻结的现成预训练模型在推理时引入循环，无需微调、持续训练或架构修改。核心洞察是数值分析视角——预归一化 Transformer 块本质上是残差 ODE ẋ = F_g(x) 的前向欧拉步（h=1），因此循环不应推进到 t=K（朴素循环因此分布外崩溃），而应是对同一终点 x(t=1) 的更精确近似：阻尼子步 + 层模式稳定 MoE 路由 + K 阶段 Runge-Kutta + 深度分数规则选窗 + KV 快照/恢复。

**结果**：7 个模型家族（密集/MoE/MLA，0.6B–30B）、45 个测试单元格，知识密集型多项选择任务提升最显著；87% 单元格非负，且显著优于朴素循环（K=4 时困惑度爆炸至 1054）。

**四大贡献**：

1. **训练无关循环 wrapper**——首个适用于任意现成冻结 checkpoint、无需参数更新的循环方法；
2. **ODE 解释框架**——将 Transformer 循环统一重解释为 ODE 积分细化，涵盖阻尼欧拉、Runge-Kutta 等策略；
3. **MoE 稳定性方案**——层模式迭代解决 MoE 路由不稳定；
4. **跨架构验证**——在密集、稀疏 MoE、MLA 等现代架构上验证通用性。

该方法暴露了大语言模型中潜在的推理时计算能力（latent inference-time computation），为无需训练的测试时扩展（test-time scaling）提供了新途径。

## 启发与局限

- **免训练的深度扩展**：为"推理时增加有效深度/计算"提供零训练成本路径，与 self-consistency、CoT 等序列侧推理时计算互补。
- **ODE 视角可迁移**："大步拆小步 + 阻尼"的思路对其他冻结模型的推理时改造（残差精化、测试时层间插值）有借鉴意义。
- **局限**：收益幅度较小（1～3 pp 量级，集中在知识型 MC 任务）；完整解码循环有约 +21.6% 延迟（K=3）；块选择与阻尼超参仍需按模型调校；次 1B 模型部分失效。

## 关联

- 相关研究主题：[EvolveLRM](/research/evolvelrm/)（推理时计算方向）
- 对比工作：Recirculation（[arXiv 2608.17981](https://arxiv.org/abs/2608.17981)）——同样免训练，但作用于 prefill 阶段的循环与信念状态追踪，二者可对照阅读。
