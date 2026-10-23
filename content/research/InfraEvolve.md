+++
title = 'InfraEvolve'
proposer = '杜晋华'
since = '2026-10-23'
date = 2026-10-23T00:00:00+08:00
draft = false
toc = true
+++

# InfraEvolve

> 研究方向：**基础设施自进化**——让 Agent 自己写出、验证并迭代推理引擎，把"某个模型在某块卡上怎么跑最快"从人工调优变成可自动搜索、可沉淀复用的进化闭环。

## 研究范畴

基础设施自进化（AI-for-AI infrastructure self-evolution）研究 Agent 能否在编译器、算子、推理引擎与服务调度这一层自主改进软件。与模型侧自进化不同，这里的进化对象是"跑模型的那套东西"：算子实现、图编译、Kernel 融合、并行切分、批处理策略、KV Cache 调度与算子-服务层的联合调优。它的可行性来自一个关键性质——这一层的反馈信号是诚实且可机器判定的：吞吐（Token/秒）、时延、显存占用、算子正确性都能在真实硬件上直接测量，Agent 可以自己提出改法、自己跑、自己判断是否保留，人类只需提前配置好环境。本方向涵盖：Agent 生成 / 优化算子与 Triton / CUDA 内核、推理引擎的自动化改造、基于记忆 + 强化学习的经验积累（把成功与失败的调优轨迹沉淀成可检索记忆）、面向国产芯片的跨平台适配与经验迁移、以及"通用引擎与专用管线"之间的定制化权衡。社区关注的核心问题包括：非 CUDA 平台语料稀缺时 Agent 从何处学习、如何保证生成的内核既正确又更快、探索成本与收敛速度、跨芯片经验能否复用、以及自动改写基础设施的安全性边界。

## 研究挑战

- 语料稀缺：国产卡的算子库、图编译器、推理框架各不相同，公开可学的数据远少于 CUDA 生态，Agent 几乎"没东西可学"。
- 正确性与性能的双重验证：内核要被编译器接受、数值要对齐、还要真的更快，三者缺一即无效，且失败模式难以归因。
- 探索成本：在真实硬件上试错的时延与算力开销高，需要记忆复用与搜索剪枝来控制。
- 跨平台迁移：为一种"模型 × 芯片 × 场景"组合调出的管线，换一个组合往往失效，经验能否结构化复用是核心变量。
- 定制即性能 vs 供应链成本：最优管线依组合而变，但为每个组合单独维护不现实，需要自动生成的专用化。
- 评测缺位：缺少统一的"引擎优化"基准，不同工作难以在同一条件下比较收益。
- 安全边界：允许 Agent 修改运行时代码，需要隔离、回滚与可审计的变更记录。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，基础设施自进化是"自进化"从模型 / Agent 层下沉到系统层的研究分支。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 持续跟踪自进化推理引擎、算子生成与国产芯片适配工作的信息流水线。

## 相关工作

**代码 / 框架**
- [vLLM](https://github.com/vllm-project/vllm) — 主流开源推理引擎，PagedAttention 与连续批处理的事实标准，也是自动化改造的主要对象
- [SGLang](https://github.com/sgl-project/sglang) — 结构化生成与 RadixAttention，推理调度层的另一参考实现
- [Triton](https://github.com/triton-lang/triton) — 面向 GPU 的高层内核语言，是 LLM 生成算子最常见的落地目标
- [TVM](https://github.com/apache/tvm) — 深度学习编译器栈，Ansor 的自动张量程序搜索是该方向的经典前身
- [KernelBench](https://github.com/ScalingIntelligence/KernelBench) — 用 LLM 生成并评测 GPU 内核的基准

**论文**
- [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://arxiv.org/abs/2501.16466) — 系统评测 LLM 写高效内核的能力，是该方向的基准起点
- [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://arxiv.org/abs/2006.06762) — 基于搜索的自动张量程序生成，自动调优的思想源头
- [Learning to Optimize Tensor Programs](https://arxiv.org/abs/1805.08166) — 学习驱动的成本模型与调度搜索
- [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) — 进化式编码 Agent 改进算法与内核的公开范例
- [EvoKernel](https://mp.weixin.qq.com/s/X0Ty_Ke_mtiACMcnSmDbpQ) — ICML 2026，面向昇腾算子生成的价值驱动记忆（Value-Driven Memory）框架；论文链接见报道，未取得独立 arXiv 条目

**综述 / 报道**
- [上海交大00后团队融资数千万，让Agent做定制的自进化推理引擎｜智能涌现首发](https://mp.weixin.qq.com/s/X0Ty_Ke_mtiACMcnSmDbpQ) — 芯生代（上海交大人工智能学院李卓、郑雨杰，导师温颖、温睦宁）完成数千万元种子轮，投资方为启高资本、交大菡源母基金、元生创投。核心思路：给定"模型 × 芯片 × 场景"的具体组合，由 Agent 生成专用推理管线并在真实硬件上验证正确性与速度；EvoKernel 通过把试错经验沉淀为记忆，让 Ascend 上的算子生成正确率从 4% 提升到 83%，且无需重训或新标注。文中对标的智谱 RSI 工程化结果（GLM-5.3 驱动的 Infra Agent 在 10 万+ 国产加速卡集群上把端到端吞吐提升到基线约 3 倍）与前英伟达工程师创办的 INT21（用 Agent 群生成整套推理引擎）构成该方向的两条产业参照。
