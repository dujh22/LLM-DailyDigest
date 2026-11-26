+++
title = 'NewModel'
proposer = '杜晋华'
since = '2026-10-21'
date = 2026-10-21T00:00:00+08:00
draft = false
toc = true
+++

# NewModel

> 研究方向：**新模型**——基础模型新版本、新架构与新训练范式的跟踪与剖析，关注"模型本身变了什么"，而非某个自进化机制。

## 研究范畴

新模型（new model watch）是本站的横向跟踪方向，与各 `*Evolve` 方向互补：`*Evolve` 关心"如何让模型自己变强"的方法论，NewModel 关心"新发布的模型在架构、数据、训练配方与能力边界上到底改了什么"。本方向涵盖：开源与闭源基础模型的新版本（通用 / 推理 / 多模态 / 小尺寸端侧）、注意力与序列建模架构创新（线性注意力、稀疏注意力、混合 Mamba-Transformer、循环记忆层）、MoE 稀疏化与专家路由设计、训练配方与优化器（数据配比、课程、Muon 类二阶优化、长上下文训练）、推理模型的后训练范式（RLVR、可验证奖励、测试时扩展），以及扩散语言模型等非自回归路线的进展。社区关注的核心问题包括：新架构的收益能否在同等算力下复现、benchmark 分数与真实能力之间的落差、开源权重与训练细节披露的不对称、模型谱系与蒸馏关系难以追溯，以及新模型发布节奏下如何做有效的横向对比而非简单刷榜。

## 研究挑战

- 可比性缺失：不同模型的评测口径、提示模板、思维链预算与工具权限差异极大，分数不可直接横比。
- 复现成本高：新架构的收益往往依赖未披露的训练数据与算力规模，小规模复现结论常与论文不一致。
- 能力归因困难：架构改动、数据配比与后训练策略同时变化，难以判断收益来自哪一项。
- 过拟合榜单：benchmark 污染与针对性优化使新模型的真实增量被高估。
- 披露不对称：闭源模型只给分数不给细节，开源模型常缺训练配方，横向分析只能停在表面。
- 长上下文与新架构的工程落地：稀疏 / 线性注意力在训练侧可行，但推理框架支持与吞吐收益未必同步。

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
1. **混合长上下文架构**：长上下文不宜押注单一注意力；线性、递归或循环状态管全局，局部或稀疏注意力保精度，并用多时间尺度状态、分页索引或按需重建KV控成本。
   - [SWGDN：滑窗增强键值更新](../../updates/2026-11-26/#swgdn) · 2026-11-26
   - [SSA：上下文依赖记忆保留](../../updates/2026-11-26/#ssa) · 2026-11-26
   - [Integral DeltaNet：双状态自适应记忆](../../updates/2026-11-25/#integral-deltanet) · 2026-11-25
   - [MemT-1.0-Pro：记忆原生模型](../../updates/2026-11-24/#memt-1-0-pro) · 2026-11-24
   - [MemOnce：稀疏解码式可扩展记忆](../../updates/2026-11-23/#memonce) · 2026-11-23
   - [LRSA：分页索引式稀疏注意力](../../updates/2026-11-23/#lrsa) · 2026-11-23
   - [Clover：循环记忆增强块扩散](../../updates/2026-11-20/#clover) · 2026-11-20
   - [Toaster：目标传播式非线性记忆](../../updates/2026-11-19/#toaster) · 2026-11-19
   - [KRA：协方差引导选择性遗忘](../../updates/2026-11-19/#kra) · 2026-11-19
   - [MovieRoll：长视频滚动生成框架](../../updates/2026-11-18/#movieroll) · 2026-11-18
   - [Bilateral Log-Linear Attention：双锚点层级注意力](../../updates/2026-11-17/#bilateral-log-linear-attention) · 2026-11-17
   - [UniSpark：面向多模态理解与生成的混合注意力模型](../../updates/2026-11-14/#unispark) · 2026-11-14
   - [文心 5.5 Flash Preview 发布：升级游戏开发与 3D 建模能力](../../updates/2026-11-13/#5-5-flash-preview-3d) · 2026-11-13
   - [Looped CED：零轮次 KV 增长的递归深度架构](../../updates/2026-11-12/#looped-ced-kv) · 2026-11-12
   - [Muir：敏感度分配门控与匹配滤波读出的线性注意力](../../updates/2026-11-08/#muir) · 2026-11-08
   - [百度开源稀疏 MoE 基座模型 ERNIE-5.5-Flash-Base](../../updates/2026-11-08/#moe-ernie-5-5-flash-base) · 2026-11-08
   - [E-Gaborformer：结合 Gabor 卷积与 Delta 记忆的严格因果语音识别器](../../updates/2026-11-08/#e-gaborformer-gabor-delta) · 2026-11-08
   - [递归稀疏注意力：以对数成本外推至百万词元](../../updates/2026-11-06/#item-22) · 2026-11-06
   - [Anchor：跨层循环状态增强长上下文检索](../../updates/2026-11-06/#anchor) · 2026-11-06
   - [SEED：浅层编码生成深层记忆](../../updates/2026-11-05/#seed) · 2026-11-05
   - [Mistral Large 4 开放权重并发布技术报告](../../updates/2026-11-04/#mistral-large-4) · 2026-11-04
   - [循环语言模型量化比想象中更容易：LoReS 状态量化](../../updates/2026-11-03/#lores) · 2026-11-03
   - [Falcon快速权重注意力实现持续学习](../../updates/2026-11-02/#falcon) · 2026-11-02
   - [长上下文混合架构：线性注意力与滑窗注意力的协同机制](../../updates/2026-11-01/#item-11) · 2026-11-01
   - [文心 Unlimited OCR 2 开源：KV 缓存降低 96%](../../updates/2026-10-29/#unlimited-ocr-2-kv-96) · 2026-10-29
2. **稀疏模型看有效算力**：评估MoE应看激活参数、每Token计算、缓存与全任务Token成本，而非总参数；稀疏路由只有转化为稳定吞吐和交付成本才有价值。
   - [AliceAI-Foundation：混合注意力稀疏基座](../../updates/2026-11-26/#aliceai-foundation) · 2026-11-26
   - [Beam：稀疏MoE高效推理](../../updates/2026-11-20/#beam-moe) · 2026-11-20
   - [K2-Horizon：全流程开放模型舰队](../../updates/2026-11-18/#k2-horizon) · 2026-11-18
   - [Qwen4-Max：稀疏长上下文高效推理](../../updates/2026-11-17/#qwen4-max) · 2026-11-17
   - [混元4 Flash：稀疏激活降本提速](../../updates/2026-11-17/#4-flash) · 2026-11-17
   - [Qwen4 Max：性能成本双优化](../../updates/2026-11-16/#qwen4-max) · 2026-11-16
   - [Hy4 flash：百万上下文低价推理](../../updates/2026-11-16/#hy4-flash) · 2026-11-16
   - [文心 5.5 Flash Preview 发布：升级游戏开发与 3D 建模能力](../../updates/2026-11-13/#5-5-flash-preview-3d) · 2026-11-13
   - [美团开源万亿参数长程智能体模型 LongCat-2.5](../../updates/2026-11-12/#longcat-2-5) · 2026-11-12
   - [百度开源稀疏 MoE 基座模型 ERNIE-5.5-Flash-Base](../../updates/2026-11-08/#moe-ernie-5-5-flash-base) · 2026-11-08
   - [蚂蚁百灵发布原生多模态模型 Ling-3.2-flash](../../updates/2026-11-08/#ling-3-2-flash) · 2026-11-08
   - [Thinking Machines Lab 发布 Inkling 2 Small，计划开放 Apache 2.0 权重](../../updates/2026-11-06/#thinking-machines-lab-inkling-2-small-ap) · 2026-11-06
   - [百度开源文心5.5 Flash Base，同尺寸多基准达 SOTA](../../updates/2026-11-06/#5-5-flash-base-sota) · 2026-11-06
   - [腾讯发布混元Hy4：原生视觉与长程Agent能力升级](../../updates/2026-11-05/#hy4-agent) · 2026-11-05
   - [Mistral Large 4 开放权重并发布技术报告](../../updates/2026-11-04/#mistral-large-4) · 2026-11-04
   - [美团发布原生多模态模型 LongCat-2.5](../../updates/2026-11-04/#longcat-2-5) · 2026-11-04
   - [Mistral发布万亿参数开放权重模型Large 4](../../updates/2026-10-31/#mistral-large-4) · 2026-10-31
   - [Mistral 开放 1T 参数旗舰模型 Large 4 权重](../../updates/2026-10-30/#mistral-1t-large-4) · 2026-10-30
   - [扩散智能发布350亿参数Agent模型Clover-35B-A3B](../../updates/2026-10-30/#350-agent-clover-35b-a3b) · 2026-10-30
   - [蚂蚁百灵开源面向 Personal Agent 的 Ling-3.1-flash-1019](../../updates/2026-10-29/#personal-agent-ling-3-1-flash-1019) · 2026-10-29
3. **动态分配推理计算**：低延迟模型应按输入、词元、步骤或任务阶段分配计算；潜变量评分、动态电路、模型路由、块并行和少步蒸馏均优于全程等量计算。
   - [LoomFormer：逐词元动态重连电路](../../updates/2026-11-26/#loomformer) · 2026-11-26
   - [GLiDE：推理蒸馏单遍决策](../../updates/2026-11-20/#glide) · 2026-11-20
   - [StepRefine：步数感知潜变量精炼](../../updates/2026-11-17/#steprefine) · 2026-11-17
   - [Karpo Decision：单次前向并行决策](../../updates/2026-11-17/#karpo-decision) · 2026-11-17
   - [LuthorSQL：单遍置信路由](../../updates/2026-11-16/#luthorsql) · 2026-11-16
   - [Gemini 4 Hydrogen：高效模型与动态路由](../../updates/2026-11-15/#gemini-4-hydrogen) · 2026-11-15
   - [Google 发布多模态决策模型 Gemini Decision 1](../../updates/2026-11-13/#google-gemini-decision-1) · 2026-11-13
   - [Google 发布 Gemini Decisions API：单次前向批量判断千题](../../updates/2026-11-12/#google-gemini-decisions-api) · 2026-11-12
   - [DriveFoundry：数据与模型协同演化的自动驾驶闭环框架](../../updates/2026-11-12/#drivefoundry) · 2026-11-12
   - [APEX：通过条件迁移实现少步流式视频生成](../../updates/2026-11-12/#apex) · 2026-11-12
   - [WeLM-Image：面向视觉智能的统一图像生成模型](../../updates/2026-11-08/#welm-image) · 2026-11-08
   - [Wave Forcing：光速级流式视频生成](../../updates/2026-11-04/#wave-forcing) · 2026-11-04
   - [OSWAM：单步动作生成的世界动作模型](../../updates/2026-11-03/#oswam) · 2026-11-03
   - [LOWN：证书引导视觉路由加速扩散视觉语言模型](../../updates/2026-10-31/#lown) · 2026-10-31
   - [扩散智能发布350亿参数Agent模型Clover-35B-A3B](../../updates/2026-10-30/#350-agent-clover-35b-a3b) · 2026-10-30
   - [GUI-JEPA：基于候选条件潜变量的移动端 GUI 智能体快速动作策略](../../updates/2026-10-29/#gui-jepa-gui) · 2026-10-29
4. **中期训练重在调分布**：扩长上下文或迁移领域时，应同步调整数据分布与学习率；即使目标统一，也要控制静态与在线数据配比。
   - [WeMM-Ecom：电商多模态混合思考](../../updates/2026-11-25/#wemm-ecom) · 2026-11-25
   - [金融小型决策模型：专业化坍缩与混合语料修复](../../updates/2026-11-06/#item-102) · 2026-11-06
   - [单一算法统一训练基础模型](../../updates/2026-11-01/#item-13) · 2026-11-01
   - [Mid-Training 综述：大模型中期训练的统一框架](../../updates/2026-10-30/#mid-training) · 2026-10-30
5. **显式状态维持世界**：长程交互世界需持久化历史、空间及视野外状态；显式场景、三维或语义记忆比仅依赖视频骨干更易保持动作后果一致。
   - [π⁴：几何条件化运动建模](../../updates/2026-11-19/#item-10) · 2026-11-19
   - [Looki 发布第一视角多模态模型系列 Loom](../../updates/2026-11-14/#looki-loom) · 2026-11-14
   - [BirdDreams：联合透视与 BEV 视频生成的驾驶世界模型](../../updates/2026-11-14/#birddreams-bev) · 2026-11-14
   - [EvoWorld：生成式视频中的视野外世界演化](../../updates/2026-11-12/#evoworld) · 2026-11-12
   - [Wizard：智能体式实时操控任意游戏世界](../../updates/2026-11-03/#wizard) · 2026-11-03
   - [L3G-World：潜在3D高斯记忆驱动的实时无限世界生成](../../updates/2026-10-31/#l3g-world-3d) · 2026-10-31
   - [Hy-Nomas：自由形式交互式世界生成](../../updates/2026-10-29/#hy-nomas) · 2026-10-29
   - [Google DeepMind发布实时交互世界模型Genie 4](../../updates/2026-10-29/#google-deepmind-genie-4) · 2026-10-29
6. **先预测未来再决策**：具身控制中，先预测任务相关的未来特征或分层状态，再生成动作，比在线生成完整视频更适合实时部署。
   - [BirdDreams：联合透视与 BEV 视频生成的驾驶世界模型](../../updates/2026-11-14/#birddreams-bev) · 2026-11-14
   - [OSWAM：单步动作生成的世界动作模型](../../updates/2026-11-03/#oswam) · 2026-11-03
   - [HiFOR：动作引导世界锚定与分层前瞻的视觉-语言-动作模型](../../updates/2026-11-03/#hifor) · 2026-11-03
   - [PDRVLA：融合物理动力学表征的视觉-语言-动作模型](../../updates/2026-10-29/#pdrvla) · 2026-10-29
7. **具身训练需要闭环**：具身泛化应串联人类视频预训练、跨具身或虚实后训练、真机评测与部署反馈，单一机器人数据难覆盖长尾。
   - [英伟达开源 GR00T 2 机器人模型、硬件与十万小时数据](../../updates/2026-11-12/#gr00t-2) · 2026-11-12
   - [DriveFoundry：数据与模型协同演化的自动驾驶闭环框架](../../updates/2026-11-12/#drivefoundry) · 2026-11-12
   - [Open-HumanWAM：扩展人类与机器人经验的开放具身基础模型方案](../../updates/2026-11-08/#open-humanwam) · 2026-11-08
   - [智元发布具身智能模型 GO-3 Preview](../../updates/2026-11-02/#go-3-preview) · 2026-11-02
   - [Motubrain 2.0 开启 Physical AI 全流程训练直播](../../updates/2026-10-30/#motubrain-2-0-physical-ai) · 2026-10-30
   - [HuGe：基于自我中心经验的类人通用视觉-语言-动作模型](../../updates/2026-10-30/#huge) · 2026-10-30
8. **视觉词元重在预算**：离散视觉表示的瓶颈不是离散化本身，而是有效比特与路由方式；因子化编码并解耦局部细节可逼近连续表示。
   - [Qwen-Image-HD：分块自回归高清生成](../../updates/2026-11-26/#qwen-image-hd) · 2026-11-26
   - [G-STAR：组缩放 Token 容量实现深度压缩自回归图像生成](../../updates/2026-11-14/#g-star-token) · 2026-11-14
   - [dNaViT：离散编码作为通用视觉表征](../../updates/2026-11-12/#dnavit) · 2026-11-12
   - [SpecSlot：像素空间生成式 Transformer 的角色耦合分词](../../updates/2026-10-31/#specslot-transformer) · 2026-10-31
   - [离散视觉词元可实现语义无损的视觉表示](../../updates/2026-10-29/#item-28) · 2026-10-29
9. **JEPA用于低延迟决策**：JEPA潜空间可用于低延迟评分，但表征中存在动态信息不等于下游会读取；需用答案均衡的反事实监督激活动态能力。
   - [V-JEPA-LM：反事实监督读取视频动态](../../updates/2026-11-17/#v-jepa-lm) · 2026-11-17
   - [JEPA 证明并改进柏拉图式表征假说](../../updates/2026-10-31/#jepa) · 2026-10-31
   - [GUI-JEPA：基于候选条件潜变量的移动端 GUI 智能体快速动作策略](../../updates/2026-10-29/#gui-jepa-gui) · 2026-10-29
10. **多模态统一共享接口**：统一多模态模型应共享骨干、潜空间或输出模式，并保留模态专用接口；仅把独立模块拼接难形成跨任务协同。
    - [S-Mind：空间令牌内化多视图几何](../../updates/2026-11-26/#s-mind) · 2026-11-26
    - [WeMM-Video：全模态音视频联合推理](../../updates/2026-11-21/#wemm-video) · 2026-11-21
    - [HiUni：共享骨干统一视觉能力](../../updates/2026-11-21/#hiuni) · 2026-11-21
    - [Sage S2.1 Flash：科学感知与可验证执行](../../updates/2026-11-18/#sage-s2-1-flash) · 2026-11-18
    - [书生·S2.1 Flash：统一表征与递归进化](../../updates/2026-11-17/#s2-1-flash) · 2026-11-17
    - [UniSpark：面向多模态理解与生成的混合注意力模型](../../updates/2026-11-14/#unispark) · 2026-11-14
    - [Duo v1：面向全双工交互的互惠世界模型](../../updates/2026-11-14/#duo-v1) · 2026-11-14
    - [WaveGen：基于内部频谱轨迹学习的端到端波形生成](../../updates/2026-11-12/#wavegen) · 2026-11-12
    - [LingBot-Touch：面向通用灵巧操作的异构触觉表征学习](../../updates/2026-11-12/#lingbot-touch) · 2026-11-12
    - [WeLM-Image：面向视觉智能的统一图像生成模型](../../updates/2026-11-08/#welm-image) · 2026-11-08
    - [Prism：统一多模态模型的双向自教学](../../updates/2026-11-06/#prism) · 2026-11-06
    - [NEO-VLA：从像素到动作的原生视觉-语言-动作策略](../../updates/2026-11-06/#neo-vla) · 2026-11-06
    - [Multimodal Flow：全连续统一语言与视觉建模](../../updates/2026-11-06/#multimodal-flow) · 2026-11-06
    - [美团发布原生多模态模型 LongCat-2.5](../../updates/2026-11-03/#longcat-2-5) · 2026-11-03
    - [Apriel Voice 27B Preview：统一语音推理与工具调用的开放模型](../../updates/2026-11-03/#apriel-voice-27b-preview) · 2026-11-03
    - [Youtu-Parsing-Omni：统一编码器与模式的全模态解析器](../../updates/2026-10-31/#youtu-parsing-omni) · 2026-10-31
    - [AMBIT：基于可执行计划与自蒸馏 Transfusion 的空间音频生成编辑](../../updates/2026-10-29/#ambit-transfusion) · 2026-10-29
11. **文档解析分层优化**：超长文档先用稀疏注意力和分块解码控内存，再优化少量检索头定位证据，并以判别器筛除不可信结果。
    - [MLLM 检索头的跨模态机制与优化](../../updates/2026-10-31/#mllm) · 2026-10-31
    - [面壁智能开源 MiniCPM-OCR 高效可信文档解析模型](../../updates/2026-10-30/#minicpm-ocr) · 2026-10-30
    - [文心 Unlimited OCR 2 开源：KV 缓存降低 96%](../../updates/2026-10-29/#unlimited-ocr-2-kv-96) · 2026-10-29
12. **小模型靠任务化补偿**：在端侧、文档、GUI和高频决策等边界明确任务上，专用数据、非生成式评分、置信校准与主动弃权可让小模型接近大模型并显著降本。
    - [GLiDE：推理蒸馏单遍决策](../../updates/2026-11-20/#glide) · 2026-11-20
    - [Microsoft-Decision-1.1：校准置信度与弃权](../../updates/2026-11-18/#microsoft-decision-1-1) · 2026-11-18
    - [Karpo Decision：单次前向并行决策](../../updates/2026-11-17/#karpo-decision) · 2026-11-17
    - [LuthorSQL：单遍置信路由](../../updates/2026-11-16/#luthorsql) · 2026-11-16
    - [SteerDistill：闭环教师引导的 LLM 智能体量化](../../updates/2026-11-13/#steerdistill-llm) · 2026-11-13
    - [Meta 发布轻量级智能体模型 Muse Ember](../../updates/2026-11-12/#meta-muse-ember) · 2026-11-12
    - [Jais 3：面向阿拉伯语的开放智能体模型系列](../../updates/2026-11-12/#jais-3) · 2026-11-12
    - [Drex：迈向基础决策模型](../../updates/2026-11-08/#drex) · 2026-11-08
    - [Decision Models：可扩展且保留人类差异的经济代理](../../updates/2026-11-06/#decision-models) · 2026-11-06
    - [Zuse：面向欧洲语言的决策模型](../../updates/2026-11-05/#zuse) · 2026-11-05
    - [面壁智能开源 MiniCPM-OCR 高效可信文档解析模型](../../updates/2026-10-30/#minicpm-ocr) · 2026-10-30
    - [OXR 1.3B 开源：文档解析三榜第一并引入 RSI 训练](../../updates/2026-10-29/#oxr-1-3b-rsi) · 2026-10-29
    - [OpenAI 发布 GPT-6.1 Terra：电脑操作能力比肩 Astra，成本降至十分之一](../../updates/2026-10-29/#openai-gpt-6-1-terra-astra) · 2026-10-29
    - [Liquid AI 发布 6 款 LFM3 端侧模型，2B 视觉模型追平 12B](../../updates/2026-10-29/#liquid-ai-6-lfm3-2b-12b) · 2026-10-29
    - [GUI-JEPA：基于候选条件潜变量的移动端 GUI 智能体快速动作策略](../../updates/2026-10-29/#gui-jepa-gui) · 2026-10-29
13. **发布结论分级采信**：仅有厂商基准、限量开放或爆料时，不应据此判定能力边界；需等待可复现实测，并按任务类型、成功任务成本与访问条件比较。
    - [Gemini 4 Neon：长流程智能体优化](../../updates/2026-11-26/#gemini-4-neon) · 2026-11-26
    - [前沿模型安全失控引发停发讨论](../../updates/2026-11-25/#item-29) · 2026-11-25
    - [Gemini 4 Neon：低成本高分推理](../../updates/2026-11-25/#gemini-4-neon) · 2026-11-25
    - [Hy4：百万上下文开放权重](../../updates/2026-11-21/#hy4) · 2026-11-21
    - [Gemini 4 Hydrogen：半量Token高分推理](../../updates/2026-11-21/#gemini-4-hydrogen-token) · 2026-11-21
    - [Hy4：原生多模态旗舰MoE](../../updates/2026-11-20/#hy4-moe) · 2026-11-20
    - [Xing 4：昇腾原生训推协同](../../updates/2026-11-18/#xing-4) · 2026-11-18
    - [微软 MAI 系列：高性价比专用模型矩阵](../../updates/2026-11-18/#mai) · 2026-11-18
    - [GPT-6.2 Astra：基准满分却实务失灵](../../updates/2026-11-18/#gpt-6-2-astra) · 2026-11-18
    - [Google DeepMind 发布 Gemini 4 Hydrogen](../../updates/2026-11-13/#google-deepmind-gemini-4-hydrogen) · 2026-11-13
    - [文心 5.5 Flash Preview 发布：升级游戏开发与 3D 建模能力](../../updates/2026-11-13/#5-5-flash-preview-3d) · 2026-11-13
    - [阿里发布Qwen4-Max预览版，升级编程与Agentic能力](../../updates/2026-11-12/#qwen4-max-agentic) · 2026-11-12
    - [Meta 发布轻量级智能体模型 Muse Ember](../../updates/2026-11-12/#meta-muse-ember) · 2026-11-12
    - [Claude Fable 5.2与Mythos 5.2发布：千智能体形式化费马大定理](../../updates/2026-11-12/#claude-fable-5-2-mythos-5-2) · 2026-11-12
    - [Thinking Machines Lab 发布 Inkling 2 Small，计划开放 Apache 2.0 权重](../../updates/2026-11-06/#thinking-machines-lab-inkling-2-small-ap) · 2026-11-06
    - [OpenAI 发布 GPT-6 Cyber 网络安全模型](../../updates/2026-11-06/#openai-gpt-6-cyber) · 2026-11-06
    - [Axion 1.0：简化训练的开放智能体基础模型](../../updates/2026-11-05/#axion-1-0) · 2026-11-05
    - [OpenAI GPT-6.2 Astra与Claude 5.5旗舰模型曝光](../../updates/2026-11-03/#openai-gpt-6-2-astra-claude-5-5) · 2026-11-03
    - [Google DeepMind 发布旗舰模型 Gemini 4 Carbon](../../updates/2026-10-30/#google-deepmind-gemini-4-carbon) · 2026-10-30
    - [Gemini 4 Carbon发布：强化长程编程、安全防御与成本效率](../../updates/2026-10-29/#gemini-4-carbon) · 2026-10-29
14. **结构化复用模型先验**：新任务应优先复用成熟基座；轻量适配需按结构差异设计更新子空间或可门控模块，避免只加秩或混合损失导致能力冲突。
    - [PMOPD：子空间保护式多教师蒸馏](../../updates/2026-11-25/#pmopd) · 2026-11-25
    - [Native LAM：世界模型提炼潜在动作](../../updates/2026-11-25/#native-lam) · 2026-11-25
    - [nanoAstra：语义动作建模与能力保持微调](../../updates/2026-11-25/#nanoastra) · 2026-11-25
    - [Don't Train It, Write It：智能体直写模型能力](../../updates/2026-11-24/#don-t-train-it-write-it) · 2026-11-24
    - [Structure Over Scale：结构化适配防秩坍缩](../../updates/2026-11-23/#structure-over-scale) · 2026-11-23
    - [DRIFT：可拆卸语言推理驾驶](../../updates/2026-11-20/#drift) · 2026-11-20
    - [ScaleVLA：前沿VLM驱动动作DiT](../../updates/2026-11-18/#scalevla-vlm-dit) · 2026-11-18
    - [Marimba：冻结ASR特征的语音决策](../../updates/2026-11-16/#marimba-asr) · 2026-11-16
    - [Open Vision Banana：全开放生成式视觉感知方案](../../updates/2026-11-14/#open-vision-banana) · 2026-11-14
    - [PACT：预填充到自回归的跨模型迁移](../../updates/2026-11-08/#pact) · 2026-11-08
    - [Zuse：面向欧洲语言的决策模型](../../updates/2026-11-05/#zuse) · 2026-11-05
    - [ReLift：将稠密三维跟踪转化为轨迹修复](../../updates/2026-11-03/#relift) · 2026-11-03
    - [FrameForge：借助视频基础模型先验统一图像生成](../../updates/2026-11-03/#frameforge) · 2026-11-03
15. **推理预算应可调**：推理计算应与输出长度解耦并按输入调节循环深度；循环时只保留未来充分状态、复用跨轮缓存，并在训练中对齐共享KV拓扑。
    - [Sleep：循环前向提升上下文适应](../../updates/2026-11-25/#sleep) · 2026-11-25
    - [Markovian Reasoning LLM：结构化状态缓存压缩](../../updates/2026-11-24/#markovian-reasoning-llm) · 2026-11-24
    - [Inkling2Mini：循环计算延长隐式推理](../../updates/2026-11-24/#inkling2mini) · 2026-11-24
    - [GLM-5.4：循环层扩展计算深度](../../updates/2026-11-24/#glm-5-4) · 2026-11-24
    - [WeMM-Video：全模态音视频联合推理](../../updates/2026-11-21/#wemm-video) · 2026-11-21
    - [DRIFT：可拆卸语言推理驾驶](../../updates/2026-11-20/#drift) · 2026-11-20
    - [MBT：并行分支与共享缓存](../../updates/2026-11-19/#mbt) · 2026-11-19
    - [Loopback Transformer：更新分流式残差循环](../../updates/2026-11-17/#loopback-transformer) · 2026-11-17
    - [KV Replay：跨迭代缓存复用](../../updates/2026-11-17/#kv-replay) · 2026-11-17
    - [Google DeepMind 发布 Gemini 4 Hydrogen](../../updates/2026-11-13/#google-deepmind-gemini-4-hydrogen) · 2026-11-13
    - [Looped CED：零轮次 KV 增长的递归深度架构](../../updates/2026-11-12/#looped-ced-kv) · 2026-11-12
    - [RELOAD：通过层循环扩展类型化决策模型推理](../../updates/2026-11-08/#reload) · 2026-11-08
    - [Dory1.0-4B：可循环的归一化 GPT](../../updates/2026-11-06/#dory1-0-4b-gpt) · 2026-11-06
    - [Concise-9B：去除推理轨迹中的冗余思考](../../updates/2026-11-06/#concise-9b) · 2026-11-06
    - [商汤开源循环架构模型 SenseNova Loop-9B-Preview](../../updates/2026-11-03/#sensenova-loop-9b-preview) · 2026-11-03
    - [LARC：统一多模态模型的连续空间潜在推理](../../updates/2026-11-03/#larc) · 2026-11-03
    - [Mistral发布万亿参数开放权重模型Large 4](../../updates/2026-10-31/#mistral-large-4) · 2026-10-31
<!-- experience-seen: 2026-11-19/fastframes 2026-11-19/gemini-4-neon 2026-11-19/item-10 2026-11-19/kra 2026-11-19/mbt 2026-11-19/toaster 2026-11-19/transformer 2026-11-19/weight-space-programming 2026-11-20/alive 2026-11-20/beam-moe 2026-11-20/clover 2026-11-20/drift 2026-11-20/gemini-4-neon-genie-4 2026-11-20/glide 2026-11-20/hy4-moe 2026-11-20/jeveration 2026-11-21/depth-pro-2 2026-11-21/egocaptioner 2026-11-21/gemini-4-hydrogen-token 2026-11-21/hiuni 2026-11-21/hy4 2026-11-21/wemm-video 2026-11-23/lrsa 2026-11-23/memonce 2026-11-23/structure-over-scale 2026-11-24/cmhc 2026-11-24/don-t-train-it-write-it 2026-11-24/duopra 2026-11-24/glm-5-4 2026-11-24/gpt-6-2-sol 2026-11-24/hy-mt3 2026-11-24/inkling2mini 2026-11-24/markovian-reasoning-llm 2026-11-24/memt-1-0-pro 2026-11-25/deciform 2026-11-25/eeg-jev 2026-11-25/gemini-4-neon 2026-11-25/integral-deltanet 2026-11-25/item-152 2026-11-25/item-29 2026-11-25/leannext 2026-11-25/nanoastra 2026-11-25/native-lam 2026-11-25/pmopd 2026-11-25/sleep 2026-11-25/wemm-ecom 2026-11-26/aliceai-foundation 2026-11-26/antom 2026-11-26/gemini-4-neon 2026-11-26/gpt-6-2-sol 2026-11-26/lingsante-medguard 2026-11-26/loomformer 2026-11-26/qwen-image-hd 2026-11-26/s-mind 2026-11-26/ssa 2026-11-26/swgdn -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架 / 模型权重**
- [Qwen3](https://github.com/QwenLM/Qwen3) — 阿里通义千问开源系列，含稠密与 MoE 双路线及混合思考模式
- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) — DeepSeek 开源 MoE 基础模型，MLA + 无辅助损失负载均衡
- [GLM-4](https://github.com/THUDM/GLM-4) — 智谱 GLM 系列开源权重与推理代码
- [vLLM](https://github.com/vllm-project/vllm) — 新模型落地推理的主流服务框架，新架构支持速度是事实上的可用性门槛
- [SGLang](https://github.com/sgl-project/sglang) — 高性能推理框架，常作为新模型论文的对拍基线

**论文**
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — 开源模型少见的完整训练配方披露：数据、缩放律、后训练与长上下文分阶段策略
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — MoE 架构 + MLA + FP8 训练，671B 总参数下激活参数控制
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066) — 细粒度专家切分与共享专家隔离
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — 纯 RL 激发推理能力，并蒸馏回小模型
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) — 稠密 / MoE 统一系列与思考—非思考模式融合
- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) — 早期融合的混合模态 token 化架构
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — Transformer 与 Mamba 层交错，兼顾长上下文效率与质量
- [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635) — 门控线性注意力的硬件友好并行训练算法
- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://arxiv.org/abs/2502.11089) — 可原生训练、硬件对齐的稀疏注意力
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663) — 测试时可学习的长期记忆模块，与注意力互补
- [Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982) — 二阶优化器在大规模预训练上的可扩展性验证
- [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) — 扩散式语言模型在规模化下的可行性
- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) — 用 1000 条样本 + 预算强制实现测试时扩展

**综述 / 报道**
- [arXiv cs.CL / cs.LG 新提交](https://arxiv.org/list/cs.CL/recent) — 新模型类工作的高频来源，本站推荐系统的默认抓取源之一
