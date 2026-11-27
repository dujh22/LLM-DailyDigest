+++
title = 'RobotEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# RobotEvolve

> 研究方向：**具身智能自进化**——机器人 / 具身 Agent 在仿真与真实环境中通过自主数据采集、自动奖励设计与 sim-to-real 迭代持续提升。

## 研究范畴

具身智能自进化（embodied self-evolution）关注机器人与具身 Agent 如何在与物理（或高保真仿真）世界的交互中自主改进：由模型自己提出任务、生成场景与资产、设计奖励函数、采集与筛选轨迹，再回灌到视觉-语言-动作（VLA）基础模型的训练中，形成"任务生成 → 仿真执行 → 数据回灌 → 模型更新 → sim-to-real 验证"的闭环。本方向涵盖：VLA / 通用机器人基础模型、跨本体（cross-embodiment）数据与迁移、LLM 驱动的奖励与课程自动设计（Eureka 类）、生成式仿真与自动场景合成（RoboGen 类）、世界模型驱动的想象训练，以及具身 Agent 的技能库积累与长程规划。社区关注的核心问题包括：真实交互数据昂贵且不可无限扩展时如何让自进化闭环"跑得起"、仿真进化出的能力能否稳定迁移到真实机器人、自动奖励与自评是否会被策略作弊，以及如何度量具身能力的真实泛化而非在固定基准上过拟合。

## 研究挑战

- 真实世界数据采集成本高、不可逆风险大，自进化闭环难以高频迭代。
- sim-to-real 差距：仿真中进化出的策略在真实环境中退化。
- 自动奖励设计与自评信号的作弊与误导（reward hacking）。
- 跨本体、跨任务的泛化度量缺乏统一标准，易在基准上过拟合。
- 安全约束下的探索：具身系统的失败可能造成物理损害。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述；具身方向作为自进化闭环从数字世界延伸到物理世界的验证场。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录具身 / 机器人自改进相关工作。

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
1. **双路径自进化**：部署后先用记忆、Harness与接口适配快速纠错，缺失能力再更新策略；脚手架验证的成功经验可蒸馏回权重，但须评测分布外能力保持。
   - [RoboEvo²：脚手架策略协同进化](../../updates/2026-11-26/#roboevo) · 2026-11-26
   - [预训练VLA持续学习：分布外遗忘诊断](../../updates/2026-11-25/#vla) · 2026-11-25
   - [Self-Upgrading Embodied Agents：经验驱动权重自升级](../../updates/2026-11-25/#self-upgrading-embodied-agents) · 2026-11-25
   - [RoboAda：计划保持式指令校正](../../updates/2026-11-25/#roboada) · 2026-11-25
   - [Embo-Harness：原生能力优先的机器人策略框架](../../updates/2026-11-25/#embo-harness) · 2026-11-25
   - [LoCo-WAM：测试时训练延展长上下文](../../updates/2026-11-23/#loco-wam) · 2026-11-23
   - [Embodied-Harness：经验驱动脚手架自改进](../../updates/2026-11-23/#embodied-harness) · 2026-11-23
   - [CoachSI：语言教练驱动策略自改进](../../updates/2026-11-20/#coachsi) · 2026-11-20
   - [WICL：面向智能体机器人操作的世界上下文学习](../../updates/2026-11-12/#wicl) · 2026-11-12
   - [SimplEvo：通过文本记忆演化提升具身智能体](../../updates/2026-11-12/#simplevo) · 2026-11-12
   - [LLM 通过权重编辑调试机器人策略](../../updates/2026-11-12/#llm-8) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [具身双脑协同：让机器人跨任务复用经验](../../updates/2026-11-08/#item-19) · 2026-11-08
   - [uni-robot-agent：面向开源机器人智能体的统一 Harness](../../updates/2026-11-04/#uni-robot-agent-harness) · 2026-11-04
   - [智元发布具身智能模型 GO-3 Preview](../../updates/2026-11-02/#go-3-preview) · 2026-11-02
   - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
   - [智元 Genie Master 在便利店跑通具身递归自我改进](../../updates/2026-10-29/#genie-master) · 2026-10-29
2. **潜在未来建模**：未来建模应按用途选形态：显式规划联合生成视觉与稠密4D几何；部署控制将潜在未来对齐动作分块；仅需视觉鲁棒性时用训练期未来结构作辅助目标。
   - [HOG-WAM：未来梯度监督增强视觉鲁棒性](../../updates/2026-11-27/#hog-wam) · 2026-11-27
   - [Plan4D：生成式可规划4D世界](../../updates/2026-11-25/#plan4d-4d) · 2026-11-25
   - [LS-MBPO：潜空间子块滚动强化](../../updates/2026-11-23/#ls-mbpo) · 2026-11-23
   - [HINT-WAM：事后信息在策略自蒸馏](../../updates/2026-11-20/#hint-wam) · 2026-11-20
   - [DexForesight：以隐式空间预见增强灵巧操作策略](../../updates/2026-11-12/#dexforesight) · 2026-11-12
   - [HiFOR：动作引导世界锚定与分层前瞻的视觉-语言-动作模型](../../updates/2026-11-03/#hifor) · 2026-11-03
   - [PDRVLA：融合物理动力学表征的视觉-语言-动作模型](../../updates/2026-10-29/#pdrvla) · 2026-10-29
   - [视觉语言智能体在自身潜在世界中学习：Dwell框架](../../updates/2026-10-29/#dwell) · 2026-10-29
3. **反事实经验回溯**：处理失败应先归因最早的关键决策点，比较替代动作，并以策略自身分布上的续跑结果验证，才能把稀疏成败信号转成动作级监督。
   - [Mind2Act World：心智动作组合诊断](../../updates/2026-11-21/#mind2act-world) · 2026-11-21
   - [AeroRSI：续飞验证式递归自改进](../../updates/2026-11-19/#aerorsi) · 2026-11-19
   - [智能体机器人自学习中的模型、技能、反馈与课程控制研究](../../updates/2026-11-12/#item-202) · 2026-11-12
   - [Rollback：世界模型中的经验回溯与策略改进](../../updates/2026-10-29/#rollback) · 2026-10-29
4. **自动仿真审计**：自动生成环境与轨迹不能只扩规模；须审计去重、物理可执行性及跨模态接触时序，保持长程状态连续，并以真实重建校准、隔离评分逻辑。
   - [VeriTouch：验证式视触觉轨迹合成](../../updates/2026-11-25/#veritouch) · 2026-11-25
   - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
   - [γ-Scape：智能体中心具身世界](../../updates/2026-11-24/#scape) · 2026-11-24
   - [RoboFinals RL Envs：物理可信长程仿真](../../updates/2026-11-17/#robofinals-rl-envs) · 2026-11-17
   - [HolidayFactory 1.0：工业机器人任务仿真、生成与评测框架](../../updates/2026-11-12/#holidayfactory-1-0) · 2026-11-12
   - [PyRUA-DataFarm：LLM 远程操作者驱动的真实场景机器人数据采集](../../updates/2026-11-06/#pyrua-datafarm-llm) · 2026-11-06
   - [优必选发布Thinker-Sim具身智能仿真平台](../../updates/2026-11-03/#thinker-sim) · 2026-11-03
   - [Gym-Anything：用编程智能体规模化构建机器人仿真](../../updates/2026-10-30/#gym-anything) · 2026-10-30
5. **主动孪生校准**：sim-to-real应以高信息量、无重置交互和实机失败证据持续反校孪生及设计，优于固定随机化或单向仿真搜索。
   - [RoboBuilder：实机视频闭环机器人共设计](../../updates/2026-11-19/#robobuilder) · 2026-11-19
   - [CUE：通过自主机器人交互弥合动力学鸿沟](../../updates/2026-11-06/#cue) · 2026-11-06
6. **课程基线优先**：固定训练预算下应先跑简单环境和低难度课程基线；复杂课程没有跨机器人与地形的稳定优势，须逐本体验证。
   - [四足机器人无监督环境设计与课程学习基准](../../updates/2026-10-30/#item-41) · 2026-10-30
7. **人机数据分阶段**：先用人类第一视角数据学习语义与空间先验，再以机器人数据分阶段对齐动作，比直接混合更利于可执行迁移。
   - [SLA：通过持续预训练扩展空间-语言-动作模型](../../updates/2026-11-08/#sla) · 2026-11-08
   - [Open-HumanWAM：扩展人类与机器人经验的开放具身基础模型方案](../../updates/2026-11-08/#open-humanwam) · 2026-11-08
   - [HuGe：基于自我中心经验的类人通用视觉-语言-动作模型](../../updates/2026-10-30/#huge) · 2026-10-30
8. **跨本体潜在空间**：跨本体迁移应统一语义对齐的潜在动作或工具中心空间，并以场景条件运动学结构显式处理形态、参数化和控制频率差异。
   - [OmniAct：运动学图驱动跨具身控制](../../updates/2026-11-26/#omniact) · 2026-11-26
   - [RynnVLA-Latent：几何潜动作预训练](../../updates/2026-11-25/#rynnvla-latent) · 2026-11-25
   - [Native LAM：世界模型提炼潜在动作](../../updates/2026-11-25/#native-lam) · 2026-11-25
   - [TCP4D：统一TCP跟踪与轨迹生成](../../updates/2026-11-19/#tcp4d-tcp) · 2026-11-19
   - [SALA：语义对齐潜在动作双轴扩展](../../updates/2026-11-18/#sala) · 2026-11-18
   - [EgoX：基于具身梦境的第一视角跨具身操控](../../updates/2026-11-14/#egox) · 2026-11-14
   - [DreamX：视频扩散模型驱动的通用潜在动作学习](../../updates/2026-11-05/#dreamx) · 2026-11-05
   - [连续动作世界模型：跨具身时空动力学先验学习](../../updates/2026-11-01/#item-15) · 2026-11-01
9. **群体经验共享**：多机器人持续学习应异步汇聚同伴经验，并用失败条件引导检索与微调；容错训练是规模化真机学习的前提。
   - [清华联合无问芯穹、智元提出机器人群体经验学习范式 CEL](../../updates/2026-10-30/#cel) · 2026-10-30
10. **结构化经验复用**：经验应按用途结构化：控制历史压缩为可寻址状态，技能存为可组合、可调试的程序或语义动作块；易变惯例保留原始观测，避免摘要丢失情境。
    - [PyRUA-Dex：编程智能体生成双手策略](../../updates/2026-11-27/#pyrua-dex) · 2026-11-27
    - [nanoAstra：语义动作建模与能力保持微调](../../updates/2026-11-25/#nanoastra) · 2026-11-25
    - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
    - [Motion Mamba 2.0：持久记忆式长时控制](../../updates/2026-11-25/#motion-mamba-2-0) · 2026-11-25
    - [保留观测历史应对惯例复现](../../updates/2026-11-25/#item-117) · 2026-11-25
    - [NavTTT：导航条件式分层参数记忆](../../updates/2026-11-23/#navttt) · 2026-11-23
    - [R2A：成败记忆驱动在线适应](../../updates/2026-11-17/#r2a) · 2026-11-17
    - [MetaAct：可执行动作约束自演化](../../updates/2026-11-17/#metaact) · 2026-11-17
    - [SPIRE：基于情境推断与因果运动基元复用的具身持续学习](../../updates/2026-11-13/#spire) · 2026-11-13
    - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
    - [HiMEM：面向3D场景VLA模型的仿海马记忆管理](../../updates/2026-11-12/#himem-3d-vla) · 2026-11-12
    - [Auto-Robotist：用可复用经验驱动机器人协同设计](../../updates/2026-11-08/#auto-robotist) · 2026-11-08
    - [HTCE：受同胚启发的跨场景导航经验规范化与复用](../../updates/2026-11-06/#htce) · 2026-11-06
    - [CausGround：基于因果交互定位的自适应具身规划](../../updates/2026-10-30/#causground) · 2026-10-30
11. **多维真实评测**：评测应覆盖目标进展、完成裕度、实时动态、跨本体、真机OOD、工程故障与镜像反事实，并逐动作归因首错；二元成功率会掩盖部署缺口。
    - [RoboDojo-Mirror：镜像反射鲁棒性评测](../../updates/2026-11-26/#robodojo-mirror) · 2026-11-26
    - [WorldLeague：物理能动性统一评测](../../updates/2026-11-25/#worldleague) · 2026-11-25
    - [RoboLiveMem：动静态配对记忆评测](../../updates/2026-11-25/#robolivemem) · 2026-11-25
    - [MARGIN：近失裕度驱动程序修复](../../updates/2026-11-25/#margin) · 2026-11-25
    - [AgentRoboCritic：意图锚定动作级评测](../../updates/2026-11-24/#agentrobocritic) · 2026-11-24
    - [Mind2Act World：心智动作组合诊断](../../updates/2026-11-21/#mind2act-world) · 2026-11-21
    - [Embodied First Exam：编码智能体具身控制综合评测](../../updates/2026-11-12/#embodied-first-exam) · 2026-11-12
    - [RoboColosseum：大规模真实场景物理智能评测框架](../../updates/2026-11-05/#robocolosseum) · 2026-11-05
    - [Motubrain 2.0 开启 Physical AI 全流程训练直播](../../updates/2026-10-30/#motubrain-2-0-physical-ai) · 2026-10-30
    - [Gym-Anything-RT：视觉语言智能体实时交互评测基准](../../updates/2026-10-29/#gym-anything-rt) · 2026-10-29
12. **信息边界闭合**：评测、工具与训练轨迹都须只使用部署时可见信息，并隔离评分逻辑；偏好奖励强搜索需配独立标准与校准正则，防止泄漏和优化验证器。
    - [SealedLoop：环外密封评判](../../updates/2026-11-26/#sealedloop) · 2026-11-26
    - [Best-of-N Steering：验证误差放大奖励作弊](../../updates/2026-11-26/#best-of-n-steering) · 2026-11-26
    - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
    - [EviCraft：证据闭包式具身评测](../../updates/2026-11-25/#evicraft) · 2026-11-25
    - [CGSI：上下文对齐技能内化](../../updates/2026-11-25/#cgsi) · 2026-11-25
    - [规划器中的 Goodhart：采样控制如何利用人类偏好奖励](../../updates/2026-11-12/#goodhart) · 2026-11-12
    - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
13. **离线代理筛选**：可用感觉—运动几何一致性或局部动作一致性预筛表征与检索器，降低训练成本，但仍须用真实成功率校准。
    - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
    - [感觉运动对齐：具身策略成功的低成本代理指标](../../updates/2026-10-30/#item-18) · 2026-10-30
14. **异步实时控制**：高层推理、低层控制及可并行部件应异步且可拆卸，仅在物理依赖或技能边界处协调，并用提前停止和单步生成控制时延。
    - [ACAP：异步多智能体机器人控制](../../updates/2026-11-26/#acap) · 2026-11-26
    - [RoboHarness-Zero：规划控制解耦脚手架](../../updates/2026-11-25/#roboharness-zero) · 2026-11-25
    - [ZeroVLN：语义工具调用免微调导航](../../updates/2026-11-21/#zerovln) · 2026-11-21
    - [DRIFT：可拆卸语言推理驾驶](../../updates/2026-11-20/#drift) · 2026-11-20
    - [JustRUA：GPT-6 机器人操作智能体的受控研究](../../updates/2026-11-14/#justrua-gpt-6) · 2026-11-14
    - [REA：异步脑-小脑控制的路由式具身智能体运行时](../../updates/2026-11-03/#rea) · 2026-11-03
    - [OSWAM：单步动作生成的世界动作模型](../../updates/2026-11-03/#oswam) · 2026-11-03
15. **策略强化协同**：后训练不应均匀扩数据；应按失败条件与任务进度定位瓶颈，优先合成稀缺场景及连接困难状态到进展路径的可恢复行为，再以价值与动作约束稳健更新。
    - [失败驱动数据飞轮：失败图引导数据合成](../../updates/2026-11-26/#item-83) · 2026-11-26
    - [Exploratory Midtraining：连接式行为覆盖](../../updates/2026-11-26/#exploratory-midtraining) · 2026-11-26
    - [ReFocus：进度引导式瓶颈加练](../../updates/2026-11-25/#refocus) · 2026-11-25
    - [OVOGO：离线价值引导生成优化](../../updates/2026-11-25/#ovogo) · 2026-11-25
    - [JKO-GRPO：Wasserstein近端更新](../../updates/2026-11-25/#jko-grpo-wasserstein) · 2026-11-25
    - [强化学习扩展通用机器人策略的多任务改进能力](../../updates/2026-11-06/#item-25) · 2026-11-06
<!-- experience-seen: 2026-11-20/coachsi 2026-11-20/drift 2026-11-20/hint-wam 2026-11-20/item-73 2026-11-20/laq 2026-11-21/mind2act-world 2026-11-21/zerovln 2026-11-23/embodied-harness 2026-11-23/loco-wam 2026-11-23/ls-mbpo 2026-11-23/navttt 2026-11-24/agentrobocritic 2026-11-24/nopeworld 2026-11-24/scape 2026-11-25/catway 2026-11-25/cgsi 2026-11-25/embo-harness 2026-11-25/evicraft 2026-11-25/item-117 2026-11-25/jko-grpo-wasserstein 2026-11-25/margin 2026-11-25/motion-mamba-2-0 2026-11-25/mxi-memicl 2026-11-25/nanoastra 2026-11-25/native-lam 2026-11-25/ovogo 2026-11-25/plan4d-4d 2026-11-25/refocus 2026-11-25/roboada 2026-11-25/roboharness-zero 2026-11-25/robolivemem 2026-11-25/robouniverse-10k 2026-11-25/rynnvla-latent 2026-11-25/self-upgrading-embodied-agents 2026-11-25/veritouch 2026-11-25/vla 2026-11-25/worldleague 2026-11-26/acap 2026-11-26/best-of-n-steering 2026-11-26/exploratory-midtraining 2026-11-26/item-83 2026-11-26/omniact 2026-11-26/robodojo-mirror 2026-11-26/roboevo 2026-11-26/sealedloop 2026-11-27/hog-wam 2026-11-27/pyrua-dex -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [OpenVLA](https://github.com/openvla/openvla) — 开源 7B 视觉-语言-动作模型，基于 Open X-Embodiment 数据训练
- [Octo](https://github.com/octo-models/octo) — 开源通用机器人策略，支持跨本体微调
- [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) — 跨机构、跨本体机器人学习数据集与 RT-X 模型
- [openpi (π0)](https://github.com/Physical-Intelligence/openpi) — Physical Intelligence 开源的 π0 / π0-FAST 通用机器人策略
- [LeRobot](https://github.com/huggingface/lerobot) — Hugging Face 真实机器人学习全流程库（数据、训练、部署）
- [Eureka](https://github.com/eureka-research/Eureka) — LLM 编码自动设计奖励函数，达到人类水平
- [DrEureka](https://github.com/eureka-research/DrEureka) — LLM 引导的 sim-to-real 迁移（奖励 + 域随机化自动设计）
- [RoboGen](https://github.com/Genesis-Embodied-AI/RoboGen) — 生成式仿真自动提出任务、生成场景并采集技能数据
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) — 面向机器人与具身 AI 的生成式物理引擎
- [ManiSkill](https://github.com/mani-skill/ManiSkill) — GPU 并行的通用操作技能仿真基准
- [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T) — NVIDIA 人形机器人通用基础模型 GR00T N1 开源实现
- [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) — 具身智能入门与资源指南

**论文**
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) — VLA 范式奠基
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) — 跨本体数据规模化带来正迁移
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)
- [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) — 流匹配动作生成的通用机器人策略
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)
- [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) — 奖励函数的进化搜索
- [DrEureka: Language Model Guided Sim-To-Real Transfer](https://arxiv.org/abs/2406.01967)
- [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) — 自提任务 + 生成仿真的数据飞轮
- [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) — VLA 综述
