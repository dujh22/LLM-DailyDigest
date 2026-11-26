+++
title = 'CacheEvolve'
proposer = '杜晋华'
since = '2026-10-21'
date = 2026-10-21T00:00:00+08:00
draft = false
toc = true
+++

# CacheEvolve

> 研究方向：**缓存自进化**——让推理记忆从"随长度线性膨胀"转向"固定预算下自适应取舍"，并自动学习记住什么、压缩什么、丢弃什么。

## 研究范畴

缓存自进化（cache self-evolution）把推理过程中的缓存看作可被模型自己学习管理的记忆资源。传统 KV Cache 每生成一个 token 就多存一份，上下文从 4K 涨到 256K，显存跟着翻几十倍，直接决定单卡能跑多少并发、单位 token 的算力成本，以及端侧与 Agent 场景是否可用。本方向涵盖三条技术线的融合：一是给单个 token 瘦身（MLA 类潜在注意力、KIVI 类低比特量化、TurboQuant 类随机旋转量化），二是改变注意力结构本身（Mamba / RWKV / Gated DeltaNet 等循环状态模型、滑动窗口注意力、混合层架构），三是把「记住什么」变成可学习的决策（缓存淘汰策略、可学习锚点库、按重要性打分的写入与合并机制）。社区关注的核心问题包括：固定内存下如何保住远处细节、淘汰策略如何从人工启发式升级为可学习策略、缓存预算如何与推理框架的调度 / 前缀复用协同、长上下文与长程 Agent 任务上如何评测真实收益而非只看困惑度，以及缓存管理与外部记忆、参数化记忆之间的分工边界。

## 研究挑战

- 容量与保真度的根本权衡：有界状态模型内存恒定但远距离回忆坍缩，全注意力保真但成本随长度线性增长，如何在中间地带稳定取到关键细节。
- 淘汰策略的自动化：H2O / SnapKV / 滑动窗口这类静态规则难以适配多样化负载，需要把"留下哪条记录"交给可学习的评分与写入机制。
- 关键信息识别本身是困难的：分不清哪些细节后续会被用到，压缩就会变成信息删除，且错误不可逆。
- 评测失真：needle-in-a-haystack 通过率高不代表多跳、状态更新、跨文档组合与变量绑定场景可用，需要更贴近真实任务的长上下文基准。
- 与推理基础设施的耦合：分页注意力、前缀缓存、连续批处理都以"缓存随长度增长"为前提设计，固定内存状态需要新的调度与容量规划模型。
- 确定性收益的兑现：内存预算可提前算清是工程价值核心，但需要模型、runtime 与硬件协同才能落地。
- 与 Agent 记忆系统的分工：哪些信息该留在缓存里、哪些该写入外部记忆、哪些该固化进参数，缺少统一框架。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

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
1. **混合记忆分工**：长上下文中，用滑窗或块内注意保留局部细节，以快慢循环状态承载全局，再用锚点或内容记忆补检索，更能兼顾恒定内存与精度。
   - [Motion Mamba 2.0：持久记忆式长时控制](../../updates/2026-11-25/#motion-mamba-2-0) · 2026-11-25
   - [Integral DeltaNet：双状态自适应记忆](../../updates/2026-11-25/#integral-deltanet) · 2026-11-25
   - [Clover：循环记忆增强块扩散](../../updates/2026-11-20/#clover) · 2026-11-20
   - [Bilateral Log-Linear Attention：双锚点层级注意力](../../updates/2026-11-17/#bilateral-log-linear-attention) · 2026-11-17
   - [UniSpark：面向多模态理解与生成的混合注意力模型](../../updates/2026-11-14/#unispark) · 2026-11-14
   - [Muir：敏感度分配门控与匹配滤波读出的线性注意力](../../updates/2026-11-08/#muir) · 2026-11-08
   - [E-Gaborformer：结合 Gabor 卷积与 Delta 记忆的严格因果语音识别器](../../updates/2026-11-08/#e-gaborformer-gabor-delta) · 2026-11-08
   - [Anchor：跨层循环状态增强长上下文检索](../../updates/2026-11-06/#anchor) · 2026-11-06
   - [长上下文混合架构：线性注意力与滑窗注意力的协同机制](../../updates/2026-11-01/#item-11) · 2026-11-01
   - [文心 Unlimited OCR 2 开源：KV 缓存降低 96%](../../updates/2026-10-29/#unlimited-ocr-2-kv-96) · 2026-10-29
2. **极限压缩学习编码**：追求数十倍压缩时，优先端到端学习缓存编解码器并纳入任务损失；按查询重建时，潜态仍应保留RoPE作用，避免重放历史。
   - [MemOnce：稀疏解码式可扩展记忆](../../updates/2026-11-23/#memonce) · 2026-11-23
   - [GaugeRoPE：RoPE兼容潜态执行](../../updates/2026-11-17/#gaugerope-rope) · 2026-11-17
   - [Transformer-FSQ：离散潜变量实现极限 KV-Cache 压缩](../../updates/2026-11-12/#transformer-fsq-kv-cache) · 2026-11-12
   - [DCKV：混合语言模型提示词 KV Cache 的学习式变换编码](../../updates/2026-10-29/#dckv-kv-cache) · 2026-10-29
3. **冗余表示与重建**：免改基础权重时，优先利用跨层、低秩、K/V代数或数值编码冗余做重建或无损压缩；部署需核算带宽、通信、编解码与内核开销。
   - [LoomKV：无损KV缓存分层压缩](../../updates/2026-11-25/#loomkv-kv) · 2026-11-25
   - [Gemma 4 K=V Cache：重叠视图单份缓存](../../updates/2026-11-19/#gemma-4-k-v-cache) · 2026-11-19
   - [KVPath：跨 Transformer 层连接键值表示](../../updates/2026-11-14/#kvpath-transformer) · 2026-11-14
   - [TraceKV：面向推理视觉语言模型的策略保持低秩 KV 缓存压缩](../../updates/2026-11-13/#tracekv-kv) · 2026-11-13
   - [SinkState：在线 SVD 压缩循环状态，加速混合 LLM 推理服务](../../updates/2026-11-12/#sinkstate-svd-llm) · 2026-11-12
   - [RidgeFill：免训练后层缓存填充加速 Prefill](../../updates/2026-11-12/#ridgefill-prefill) · 2026-11-12
   - [LowRAM：可组合的测试时 KV Cache 压缩](../../updates/2026-11-06/#lowram-kv-cache) · 2026-11-06
   - [BasisKV：面向通信优化与键路由的 Value 潜表示](../../updates/2026-11-06/#basiskv-value) · 2026-11-06
   - [SEED：浅层编码生成深层记忆](../../updates/2026-11-05/#seed) · 2026-11-05
4. **状态演化感知量化**：缓存量化应沿状态演化轴校准，并按层、状态敏感度、未来影响与复用次数混精；循环状态仍需随机舍入。表示需直配内核，并用布局及完整历史恢复测试正确性。
   - [量化KV缓存维护：布局漂移与历史恢复](../../updates/2026-11-25/#item-93) · 2026-11-25
   - [Hopper 4-bit KV解码：访存计算重叠](../../updates/2026-11-25/#hopper-4-bit-kv) · 2026-11-25
   - [LAQ：潜变量感知四比特量化](../../updates/2026-11-20/#laq) · 2026-11-20
   - [MiSTiQ：微缩放格码缓存量化](../../updates/2026-11-18/#mistiq) · 2026-11-18
   - [量化草稿缓存：低内存投机解码](../../updates/2026-11-17/#item-40) · 2026-11-17
   - [FOSCAR：通过仿射折叠加速 2/4-bit KV Cache 解码注意力](../../updates/2026-11-12/#foscar-2-4-bit-kv-cache) · 2026-11-12
   - [CoMixKV：面向多智能体系统的协同混合精度 KV 缓存量化](../../updates/2026-11-12/#comixkv-kv) · 2026-11-12
   - [CALFA-KV：联合校准与 Fisher 引导锚点的 1-bit KV 缓存压缩](../../updates/2026-11-12/#calfa-kv-fisher-1-bit-kv) · 2026-11-12
   - [BitDecoding-FP4：原生 FP4 KV 缓存解码](../../updates/2026-11-12/#bitdecoding-fp4-fp4-kv) · 2026-11-12
   - [bf16 循环状态舍入导致混合推理模型过度思考](../../updates/2026-11-12/#bf16) · 2026-11-12
   - [LoopVQ：循环 Transformer 的亚 1 比特 KV Cache 量化](../../updates/2026-11-06/#loopvq-transformer-1-kv-cache) · 2026-11-06
   - [LoopKV：循环 Transformer 的循环感知 KV 缓存压缩](../../updates/2026-11-06/#loopkv-transformer-kv) · 2026-11-06
   - [FlagRot：面向低比特 KV Cache 的选择性旋转](../../updates/2026-11-06/#flagrot-kv-cache) · 2026-11-06
   - [循环语言模型量化比想象中更容易：LoReS 状态量化](../../updates/2026-11-03/#lores) · 2026-11-03
   - [扩散语言模型的 KV Cache 量化](../../updates/2026-10-30/#kv-cache) · 2026-10-30
   - [低比特 GDN 循环状态量化：全局梯度感知分配与纯写滑动窗口](../../updates/2026-10-30/#gdn) · 2026-10-30
5. **分层检索验证**：百万级上下文先以语义块、树或分页索引筛选，再按查询误差界验证并补漏；预算应按质量自适应，且审计子集交互而非只排单词元。
   - [SwapCert：稀疏注意力联合支持审计](../../updates/2026-11-25/#swapcert) · 2026-11-25
   - [NFA：近远分区稀疏检索](../../updates/2026-11-25/#nfa) · 2026-11-25
   - [RefineKV：误差界驱动的KV缓存压缩](../../updates/2026-11-24/#refinekv-kv) · 2026-11-24
   - [DisSparse：流水化Top-p稀疏注意力](../../updates/2026-11-24/#dissparse-top-p) · 2026-11-24
   - [LRSA：分页索引式稀疏注意力](../../updates/2026-11-23/#lrsa) · 2026-11-23
   - [VerKV：先验证后取回的可靠 KV Cache 压缩](../../updates/2026-11-12/#verkv-kv-cache) · 2026-11-12
   - [粗粒度语义块实现免训练稀疏注意力加速](../../updates/2026-11-06/#item-69) · 2026-11-06
   - [递归稀疏注意力：以对数成本外推至百万词元](../../updates/2026-11-06/#item-22) · 2026-11-06
   - [CISA：用分块索引稀疏注意力改造稠密注意力模型](../../updates/2026-11-06/#cisa) · 2026-11-06
6. **自适应淘汰评分**：用早期代理查询预选、以中层统一评分，再以查询反馈纠错；评分还应结合置信度、内容新颖性与模型级时间衰减。
   - [NoHairCache：单次校准幂律淘汰](../../updates/2026-11-24/#nohaircache) · 2026-11-24
   - [RoCoKV：置信冗余感知缓存压缩](../../updates/2026-11-20/#rocokv) · 2026-11-20
   - [中层网络最适合评判 KV Cache 淘汰](../../updates/2026-11-06/#kv-cache-2) · 2026-11-06
   - [EchoKV：基于迭代查询反馈的自纠错 KV Cache 淘汰](../../updates/2026-11-06/#echokv-kv-cache) · 2026-11-06
   - [EarlySelectKV：跨层查询代理实现前瞻式 KV 选择](../../updates/2026-11-03/#earlyselectkv-kv) · 2026-11-03
7. **淘汰门控防退化**：可学习淘汰或摘要若只接冻结模型的延迟任务损失，易出现门控抵消或信用稀疏；应加稠密教师、归一化补偿、信息增量或局部续写一致性奖励。
   - [TruSuCo：局部续写驱动的状态压缩](../../updates/2026-11-25/#trusuco) · 2026-11-25
   - [MaxIM：基于强化学习的最大信息增量摘要](../../updates/2026-11-12/#maxim) · 2026-11-12
   - [KV Cache 淘汰的门控机制](../../updates/2026-11-08/#kv-cache) · 2026-11-08
8. **层头稀疏配置**：稀疏模式与检索偏差随层、头和生成阶段变化；应逐层动态配置，用覆盖率修复失效头，并复用相邻层候选隐藏索引开销。索引器训练需覆盖部署位置跨度。
   - [位置跳跃蒸馏：短训长服稀疏索引](../../updates/2026-11-25/#item-150) · 2026-11-25
   - [Turnout：自适应注意力切换](../../updates/2026-11-23/#turnout) · 2026-11-23
   - [Lost in a Few Heads：盲头定点修复稀疏注意力](../../updates/2026-11-18/#lost-in-a-few-heads) · 2026-11-18
   - [CVSA：长上下文稀疏注意力的覆盖率闭环验证](../../updates/2026-11-12/#cvsa) · 2026-11-12
   - [多层索引器：重叠执行 DeepSeek 稀疏注意力的选择与计算](../../updates/2026-11-06/#deepseek) · 2026-11-06
   - [无需重训练的大规模混合 LLM 长上下文解码加速](../../updates/2026-11-05/#llm) · 2026-11-05
9. **可恢复智能体检查点**：长程智能体应分离紧凑可执行状态与可寻址原始证据，按查询、计划或工具依赖读取并保留溯源；评测任务续行与行为成本，而非摘要相似度。
   - [DMC-5：双模型缓存感知压缩](../../updates/2026-11-25/#dmc-5) · 2026-11-25
   - [Markovian Reasoning LLM：结构化状态缓存压缩](../../updates/2026-11-24/#markovian-reasoning-llm) · 2026-11-24
   - [Contexture：工具感知式上下文驱逐](../../updates/2026-11-23/#contexture) · 2026-11-23
   - [RAA：分辨率式记忆注意](../../updates/2026-11-20/#raa) · 2026-11-20
   - [GrepMem：无损免索引长期记忆](../../updates/2026-11-20/#grepmem) · 2026-11-20
   - [CompAct-Bench：工作上下文压缩评测](../../updates/2026-11-20/#compact-bench) · 2026-11-20
   - [VideoNexus：独立感知的证据压缩](../../updates/2026-11-19/#videonexus) · 2026-11-19
   - [SCH：状态证据分离式上下文交接](../../updates/2026-11-19/#sch) · 2026-11-19
   - [MoE-Context：按需分块上下文掩码](../../updates/2026-11-19/#moe-context) · 2026-11-19
   - [Context Has a Price：缓存感知上下文成本评测](../../updates/2026-11-18/#context-has-a-price) · 2026-11-18
   - [CarryOn：源链接证据自适应保留](../../updates/2026-11-16/#carryon) · 2026-11-16
   - [Folio：面向长程智能体的可恢复多分辨率上下文折叠](../../updates/2026-11-14/#folio) · 2026-11-14
   - [WAAC：面向工作流的智能体轨迹压缩](../../updates/2026-11-12/#waac) · 2026-11-12
   - [Think or Remember：智能体推理中的思考与记忆成本交换率](../../updates/2026-11-12/#think-or-remember) · 2026-11-12
   - [SemanticKV：面向智能体自回归视频生成的语义对齐 KV 缓存压缩](../../updates/2026-11-12/#semantickv-kv) · 2026-11-12
   - [PACE：长程智能体的规划感知 KV 缓存与位置重编号](../../updates/2026-11-12/#pace-kv) · 2026-11-12
   - [QRAE：面向深度搜索智能体的查询相关注意力熵上下文压缩](../../updates/2026-11-08/#qrae) · 2026-11-08
   - [增强压缩式 AI 智能体记忆的局部与全局结构](../../updates/2026-11-08/#item-31) · 2026-11-08
   - [推理历史压缩对后续生成与智能体成本的因果影响](../../updates/2026-11-06/#item-82) · 2026-11-06
   - [无需长上下文：频繁压缩与语义状态空间模型](../../updates/2026-11-06/#item-50) · 2026-11-06
   - [CORAL：面向长程智能体的认知资源自分配](../../updates/2026-10-30/#coral) · 2026-10-30
10. **规则记忆隔离**：摘要保留规则文本不等于保留授权边界；压缩时应将规则与权限设为不可淘汰区，并在真实工具调用链评测违规率。
    - [ARCBench：智能体上下文压缩后的规则遵循评测](../../updates/2026-11-06/#arcbench) · 2026-11-06
11. **非前缀复用修复**：非前缀或失效KV存在位置和上下文不兼容；先做位置适配，或仅用于投机并精确验证，把重计算优先给答案承载块。
    - [Callo：失效KV投机解码](../../updates/2026-11-16/#callo-kv) · 2026-11-16
    - [非前缀 KV-Cache 复用中的修复预算分配](../../updates/2026-11-06/#kv-cache) · 2026-11-06
    - [CacheWeave：学习重计算的高效位置无关 KV 缓存](../../updates/2026-11-03/#cacheweave-kv) · 2026-11-03
12. **分支状态复用**：共享前缀、多问题或树状探索应把缓存组织成可分叉DAG并精确零拷贝复用；共享骨干后只重算分支读出。
    - [MBT：并行分支与共享缓存](../../updates/2026-11-19/#mbt) · 2026-11-19
    - [Flide：以精确状态分叉加速决策推理](../../updates/2026-11-12/#flide) · 2026-11-12
    - [Q64：共享上下文候选评分与联合适配读出网络](../../updates/2026-11-06/#q64) · 2026-11-06
    - [Octopus：基于潜在 KV 分支的单模型多智能体强化学习框架](../../updates/2026-11-06/#octopus-kv) · 2026-11-06
13. **混合状态移交**：混合架构的前缀复用或跨模型移交需联合处理全注意力KV、循环状态和卷积历史；在可预测交互边界生成检查点，可避免提示重放与预填充切分。
    - [FrontierReplay：无切分精确前缀缓存](../../updates/2026-11-20/#frontierreplay) · 2026-11-20
    - [HST：混合线性注意力 LLM 的跨模型状态移交](../../updates/2026-11-08/#hst-llm) · 2026-11-08
14. **快速权重在线学习**：将循环快速权重视为在线学习器时，更新规则需做前缀对齐、归一化与选择性遗忘；分层线性写入可兼顾非线性表达和高效分块训练。
    - [Toaster：目标传播式非线性记忆](../../updates/2026-11-19/#toaster) · 2026-11-19
    - [KRA：协方差引导选择性遗忘](../../updates/2026-11-19/#kra) · 2026-11-19
    - [Falcon快速权重注意力实现持续学习](../../updates/2026-11-02/#falcon) · 2026-11-02
15. **递归深度共享缓存**：增加测试时计算深度时，可跨层、跨轮共享同组KV；训练应匹配共享拓扑并随机深度。推测解码的验证调度还应贴合缓存轮转，避免跨循环搬运。
    - [LoopCache：置信更新与循环KV缓存](../../updates/2026-11-19/#loopcache-kv) · 2026-11-19
    - [KV Replay：跨迭代缓存复用](../../updates/2026-11-17/#kv-replay) · 2026-11-17
    - [Looped CED：零轮次 KV 增长的递归深度架构](../../updates/2026-11-12/#looped-ced-kv) · 2026-11-12
<!-- experience-seen: 2026-11-18/context-has-a-price 2026-11-18/kv-ltm-kv 2026-11-18/lost-in-a-few-heads 2026-11-18/mistiq 2026-11-18/movieroll 2026-11-19/gemma-4-k-v-cache 2026-11-19/kra 2026-11-19/loopcache-kv 2026-11-19/mbt 2026-11-19/moe-context 2026-11-19/sch 2026-11-19/toaster 2026-11-19/videonexus 2026-11-20/clover 2026-11-20/compact-bench 2026-11-20/frontierreplay 2026-11-20/grepmem 2026-11-20/laq 2026-11-20/raa 2026-11-20/rocokv 2026-11-23/contexture 2026-11-23/lrsa 2026-11-23/memonce 2026-11-23/turnout 2026-11-24/declarative-attention 2026-11-24/dissparse-top-p 2026-11-24/markovian-reasoning-llm 2026-11-24/nohaircache 2026-11-24/refinekv-kv 2026-11-24/vaw 2026-11-25/dmc-5 2026-11-25/hopper-4-bit-kv 2026-11-25/integral-deltanet 2026-11-25/item-150 2026-11-25/item-93 2026-11-25/loomkv-kv 2026-11-25/motion-mamba-2-0 2026-11-25/nfa 2026-11-25/swapcert 2026-11-25/trusuco -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [vLLM](https://github.com/vllm-project/vllm) — PagedAttention 与分页 KV Cache，现代推理服务缓存管理的事实标准
- [LMCache](https://github.com/LMCache/LMCache) — 面向 LLM 服务的 KV Cache 跨请求复用与分层存储层
- [EdgeRock](https://github.com/rockmatrix-ai/EdgeRock) — 岩芯矩阵联合港科大、CMU 开源的固定内存架构，以记忆岩锚（RMA）替代增长的 KV Cache

**论文**
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — 用操作系统分页思想管理 KV Cache，消除碎片并支持共享
- [Efficient Streaming Language Models with Attention Sinks](https://arxiv.org/abs/2309.17453) — 滑动窗口 + 注意力汇聚点，固定缓存实现无限流式输入
- [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://arxiv.org/abs/2306.14048) — 依据累积注意力分数动态淘汰 KV
- [SnapKV: LLM Knows What You are Looking for Before Generation](https://arxiv.org/abs/2404.14469) — 利用提示词注意力分布做查询感知的缓存压缩
- [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://arxiv.org/abs/2406.02069) — 按层分配缓存预算，浅层多留深层少留
- [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://arxiv.org/abs/2402.02750) — 键值分通道量化，把单 token 成本压到 2bit
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — 恒定内存的线性时间状态空间模型
- [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464) — 门控 delta 规则，混合架构中承担循环记忆层
- [Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time](https://arxiv.org/abs/2305.17118) — 基于重要性持久性假设的固定预算缓存淘汰
- [Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference](https://arxiv.org/abs/2407.11550) — 按注意力头自适应分配淘汰预算
- [EdgeRock: Strong Reasoning at Constant Memory](https://arxiv.org/abs/2610.10118) — EdgeRock-4B 技术报告，含记忆岩锚（RMA）架构、由 Qwen3.5-4B 分阶段转换的训练流程与完整评测

**综述 / 报道**
- [KV Cache砍掉99%，单卡吞吐飙6倍：港科大、CMU与岩芯矩阵开源 EdgeRock-4B](https://mp.weixin.qq.com/s/XlGTNPhtP88uAL5srNtoxQ) — 量子位报道。256K 上下文下 KV Cache 恒定为 72MiB，单卡 512 路并发、吞吐 6.42 倍；核心是记忆岩锚（RMA）：循环状态抓大意、1024 token 局部窗口管眼前、1024 条锚点库记关键，每 256 条候选与存量一起打分只留高分者；关掉 RMA 后长上下文准确率从 94.1% 跌到 0.4%，证明收益确由锚点读取远处细节而来。
- [EdgeRock 技术报告（中文版）](https://rockmatrix.ai/documents/edgerock-report-zh.pdf) — 上述报告的官方中文全文
