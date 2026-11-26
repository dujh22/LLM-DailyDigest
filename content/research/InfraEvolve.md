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
1. **实机闭环搜索**：算子和引擎优化应以真实硬件上的正确性、吞吐与时延作保留门槛；自动迭代已能稳定超过人工精调。
   - [EvolonAI：机器反馈驱动算力自进化](../../updates/2026-11-26/#evolonai) · 2026-11-26
   - [Performance Factory：Codex自动修复性能回归](../../updates/2026-11-20/#performance-factory-codex) · 2026-11-20
   - [Claude Mythos：三天自动适配AMD内核](../../updates/2026-11-18/#claude-mythos-amd) · 2026-11-18
   - [Mobile AI Factory：手机感知式模型定制](../../updates/2026-11-17/#mobile-ai-factory) · 2026-11-17
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [百度披露 ERNIE Evolve 递归自我改进进展，已用于文心 5.5 Flash 研发](../../updates/2026-11-12/#ernie-evolve-5-5-flash) · 2026-11-12
   - [IQuestRT 推理提速近 3 倍，Agent 两周反超人工精调](../../updates/2026-11-06/#iquestrt-3-agent) · 2026-11-06
   - [ForgeKernel零样本自进化生成算子，性能超越DeepSeek FlashMLA 9.8%](../../updates/2026-10-31/#forgekernel-deepseek-flashmla-9-8) · 2026-10-31
   - [ForgeKernel 登顶华为与英伟达算子评测榜](../../updates/2026-10-29/#forgekernel) · 2026-10-29
   - [无问芯穹算子优化Agent斩获SOL-ExecBench 88项第一](../../updates/2026-10-29/#agent-sol-execbench-88) · 2026-10-29
2. **独立验证门控**：候选须经独立执行、数值及领域约束测试，评判器不得受修改者控制；高风险内核还需验证功能与内存行为等价。
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [EDAGoat：EDA约束验证式GPU优化](../../updates/2026-11-23/#edagoat-eda-gpu) · 2026-11-23
   - [芯片PPA优化：模型挖掘成熟设计余量](../../updates/2026-11-19/#ppa) · 2026-11-19
   - [Callo：失效KV投机解码](../../updates/2026-11-16/#callo-kv) · 2026-11-16
   - [AutoAssumption：搜索算法假设以发现 ML 系统新算法](../../updates/2026-11-13/#autoassumption-ml) · 2026-11-13
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [LARK：用 Lean 形式化验证 LLM 生成的 GPU Kernel](../../updates/2026-11-06/#lark-lean-llm-gpu-kernel) · 2026-11-06
   - [CompressionBench：编码智能体自主压缩 LLM 评测](../../updates/2026-11-06/#compressionbench-llm) · 2026-11-06
3. **跨栈联合优化**：先建模引擎层级依赖和硬件能力，再联动算法、内核、通信与调度；单层最优常非端到端最优。
   - [Uni3Sim：统一系统级推理仿真](../../updates/2026-11-24/#uni3sim) · 2026-11-24
   - [RSIBench-Infra：生产级基础设施优化评测](../../updates/2026-11-19/#rsibench-infra) · 2026-11-19
   - [Xing 4：昇腾原生训推协同](../../updates/2026-11-18/#xing-4) · 2026-11-18
   - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [EngineAgent：感知推理栈层级与硬件能力的端侧推理引擎智能体](../../updates/2026-11-12/#engineagent) · 2026-11-12
   - [IQuestRT 推理提速近 3 倍，Agent 两周反超人工精调](../../updates/2026-11-06/#iquestrt-3-agent) · 2026-11-06
   - [Formulaic：智能体驱动的 AI 基础设施软硬件协同设计](../../updates/2026-10-30/#formulaic-ai) · 2026-10-30
4. **模型先验加实测**：用成本模型或低成本代理缩小搜索域，再以周期性或在线实测纠偏，比纯穷举或纯模型决策更省预算。
   - [Uni3Sim：统一系统级推理仿真](../../updates/2026-11-24/#uni3sim) · 2026-11-24
   - [QDA：智能体闭环量化设计](../../updates/2026-11-19/#qda) · 2026-11-19
   - [NCCL-BOT：用在线多臂老虎机闭环优化 NCCL 成本决策](../../updates/2026-11-12/#nccl-bot-nccl) · 2026-11-12
   - [AutoQS：大语言模型自动设计量化策略](../../updates/2026-11-12/#autoqs) · 2026-11-12
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [Formulaic：智能体驱动的 AI 基础设施软硬件协同设计](../../updates/2026-10-30/#formulaic-ai) · 2026-10-30
5. **经验持久化**：把成功改写、失败轨迹及其来源和适用边界结构化沉淀；跨模型与后端检索并交叉不同机制，可减少从零试错和经验误用。
   - [NoeVera：证据演化式配置搜索](../../updates/2026-11-25/#noevera) · 2026-11-25
   - [MOSAIC：记忆组织式反模仿搜索](../../updates/2026-11-25/#mosaic) · 2026-11-25
   - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
   - [KernelMosaic：CUDA Kernel 生成数据集与智能体框架](../../updates/2026-11-13/#kernelmosaic-cuda-kernel) · 2026-11-13
   - [面向自主 RTL 与综合优化的基准和自改进智能体](../../updates/2026-11-12/#rtl) · 2026-11-12
   - [InfraRSI：递归自我改进驱动训练基础设施优化](../../updates/2026-11-12/#infrarsi) · 2026-11-12
   - [EngineAgent：感知推理栈层级与硬件能力的端侧推理引擎智能体](../../updates/2026-11-12/#engineagent) · 2026-11-12
   - [ModelBlaster：跨模型、内核与硬件后端的学习增强优化智能体](../../updates/2026-11-06/#modelblaster) · 2026-11-06
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
6. **团队动态重组**：固定多智能体分工易陷局部最优；由监督者诊断停滞、重组角色并保留独立验证更稳。
   - [百度披露 ERNIE Evolve 递归自我改进进展，已用于文心 5.5 Flash 研发](../../updates/2026-11-12/#ernie-evolve-5-5-flash) · 2026-11-12
   - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
7. **长程预算评测**：固定时间、算力和成本，在条件匹配的真实负载上回放；受限任务单点超越不能外推为持续自改进，短测也会漏算搜索开销。
   - [Singularity-Bench：AI研发设施自主构建](../../updates/2026-11-20/#singularity-bench-ai) · 2026-11-20
   - [RSIBench-Infra：生产级基础设施优化评测](../../updates/2026-11-19/#rsibench-infra) · 2026-11-19
   - [Re-Reading Is Not Free：缓存感知能耗估算](../../updates/2026-11-18/#re-reading-is-not-free) · 2026-11-18
   - [LLMs for AI Infrastructure：基础设施全生命周期综述](../../updates/2026-11-17/#llms-for-ai-infrastructure) · 2026-11-17
   - [Singularity-Bench：AI基建自主构建评测](../../updates/2026-11-16/#singularity-bench-ai) · 2026-11-16
   - [AscendGYM：成本感知算子优化评测](../../updates/2026-11-16/#ascendgym) · 2026-11-16
   - [Singularity-Bench：智能体能否自主构建智能体？](../../updates/2026-11-14/#singularity-bench) · 2026-11-14
   - [面向低成本智能体脚手架的系统优化](../../updates/2026-11-12/#item-108) · 2026-11-12
   - [Infrathon：真实世界长程 AI 基础设施优化智能体基准](../../updates/2026-11-12/#infrathon-ai) · 2026-11-12
   - [ServerBench：编码智能体设计专用 LLM 服务系统的评测基准](../../updates/2026-11-06/#serverbench-llm) · 2026-11-06
   - [RSIGym：面向递归自我改进的真实训练环境](../../updates/2026-11-05/#rsigym) · 2026-11-05
8. **端到端SLO调度**：智能体服务应联合决定准入、放置、预填充路由和缓存去留；按端到端SLO优化比逐组件提利用率更可靠。
   - [Contexture：工具感知式上下文驱逐](../../updates/2026-11-23/#contexture) · 2026-11-23
   - [静态图 NPU 多模型智能体工作流中的 KV 缓存恢复与重计算](../../updates/2026-11-13/#npu-kv) · 2026-11-13
   - [Evolving Infra：面向智能体负载的自适应 LLM 服务](../../updates/2026-11-13/#evolving-infra-llm) · 2026-11-13
   - [TAO：面向 LLM 智能体服务的工具感知联合调度](../../updates/2026-10-30/#tao-llm) · 2026-10-30
   - [DolphinRouting：面向PD解耦推理服务的集群级二元路由](../../updates/2026-10-30/#dolphinrouting-pd) · 2026-10-30
9. **状态分叉复用**：树状决策和并行 rollout 应精确分叉执行状态并共享公共前缀，避免复制工作区与重复预填充。
   - [Flide：以精确状态分叉加速决策推理](../../updates/2026-11-12/#flide) · 2026-11-12
   - [BunshinRL：面向智能体强化学习的低内存工作空间分叉系统](../../updates/2026-11-12/#bunshinrl) · 2026-11-12
10. **免训练配置搜索**：先搜索逐层稀疏、量化与缓存近似并设置精度门控；冻结权重常能换取显著推理收益。
    - [QDA：智能体闭环量化设计](../../updates/2026-11-19/#qda) · 2026-11-19
    - [RidgeFill：免训练后层缓存填充加速 Prefill](../../updates/2026-11-12/#ridgefill-prefill) · 2026-11-12
    - [AutoQS：大语言模型自动设计量化策略](../../updates/2026-11-12/#autoqs) · 2026-11-12
    - [SEED：浅层编码生成深层记忆](../../updates/2026-11-05/#seed) · 2026-11-05
    - [无需重训练的大规模混合 LLM 长上下文解码加速](../../updates/2026-11-05/#llm) · 2026-11-05
11. **低比特软硬协同**：低比特KV缓存需联合设计量化误差、位操作和GPU流水线，单改数值格式难转化为端到端吞吐。
    - [Hopper 4-bit KV解码：访存计算重叠](../../updates/2026-11-25/#hopper-4-bit-kv) · 2026-11-25
    - [FOSCAR：通过仿射折叠加速 2/4-bit KV Cache 解码注意力](../../updates/2026-11-12/#foscar-2-4-bit-kv-cache) · 2026-11-12
    - [BitDecoding-FP4：原生 FP4 KV 缓存解码](../../updates/2026-11-12/#bitdecoding-fp4-fp4-kv) · 2026-11-12
12. **算法系统共搜索**：对投机解码等部署敏感技术，应联合搜索算法参数、验证粒度与批处理策略，而非只调单个内核。
    - [DisSparse：流水化Top-p稀疏注意力](../../updates/2026-11-24/#dissparse-top-p) · 2026-11-24
    - [LoopCache：置信更新与循环KV缓存](../../updates/2026-11-19/#loopcache-kv) · 2026-11-19
    - [Callo：失效KV投机解码](../../updates/2026-11-16/#callo-kv) · 2026-11-16
    - [SpecPilot：面向投机解码的自主算法发现与系统优化](../../updates/2026-11-06/#specpilot) · 2026-11-06
    - [IQuestRT 推理提速近 3 倍，Agent 两周反超人工精调](../../updates/2026-11-06/#iquestrt-3-agent) · 2026-11-06
13. **假设与问题引导**：在关键节点先提出方向问题或待放宽假设，并用形式证明约束重推导，比直接反复改代码更省试错。
    - [AutoAssumption：搜索算法假设以发现 ML 系统新算法](../../updates/2026-11-13/#autoassumption-ml) · 2026-11-13
    - [KernelSeek：问题驱动的 GPU 内核优化智能体](../../updates/2026-11-06/#kernelseek-gpu) · 2026-11-06
14. **反馈吞吐扩展**：大规模并行搜索扩容前先提升正确性验证与稳定测速吞吐；候选生成快于反馈时，增加智能体只会堆积待测实验。
    - [CompoundingKernel：谱系归档式内核进化](../../updates/2026-11-17/#compoundingkernel) · 2026-11-17
15. **安全有状态沙箱**：生产级编程智能体应以最小权限隔离不可信操作，并原生支持状态持久化、回滚、分岔和迁移；无状态执行不足以承载长程任务。
    - [Codex 沙箱：跨平台权限隔离](../../updates/2026-11-19/#codex) · 2026-11-19
    - [CubeSandbox：状态化微虚拟机沙箱](../../updates/2026-11-18/#cubesandbox) · 2026-11-18
<!-- experience-seen: 2026-11-19/codex 2026-11-19/gemma-4-k-v-cache 2026-11-19/loopcache-kv 2026-11-19/ppa 2026-11-19/qda 2026-11-19/rsibench-infra 2026-11-20/performance-factory-codex 2026-11-20/singularity-bench-ai 2026-11-23/contexture 2026-11-23/ctrl-gpu 2026-11-23/edagoat-eda-gpu 2026-11-24/dissparse-top-p 2026-11-24/shirudo-ebpf 2026-11-24/uni3sim 2026-11-25/glm-5-5-rsi 2026-11-25/hopper-4-bit-kv 2026-11-25/loomkv-kv 2026-11-25/mosaic 2026-11-25/noevera 2026-11-26/evolonai -->
<!-- research-experience:end -->

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
