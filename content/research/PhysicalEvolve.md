+++
title = 'PhysicalEvolve'
proposer = '杜晋华'
since = '2026-11-01'
date = 2026-11-01T00:00:00+08:00
draft = false
toc = true
+++

# PhysicalEvolve

> 研究方向：**物理世界自进化**——让 AI 在与真实物理世界的碰撞中持续改进对物理机制的建模、对物理系统的控制，以及自身的研究与改进方法，由物理环境而非人工标注充当最终裁判。

## 研究范畴

物理世界自进化（physical-world self-evolution）关注 AI 如何"解析"物理世界：不只是在给定方程下调参、在固定基准上刷分，而是从模型预测与实验测量的偏差出发追查机制、修订方程、改写控制程序，并把每一次排查沉淀为可复用的方法，再由真实实验或真机执行验证修订是否有效。本方向把三条此前分散的技术线放在同一个闭环里看待：一是**物理建模自进化**——面向材料、电化学、多物理场耦合等微观物理系统，让 AI Scientist 同时提出参数识别、物理机制、几何、边界条件等多种候选解释并行验证，模型与"研究者"在同一轮试错中共同进化（EvoSim 类）；二是**Physical AI 基础模型的透明进化**——把预训练、checkpoint 序列、真机分布外评测、成本与故障放到同一条公开时间线上，用"持续训练 → 定期保存 → 真机考试 → 失败归因 → 经验筛选 → 再训练"替代经过剪辑的 Demo（Motubrain 2.0 直播类）；三是**具身递归自我改进**——以 Self-Harness 让 System 2（理解与规划）改写 System 1（技能、代码、工具、记忆）及二者协作的工作程序，生成多代候选智能体并由物理环境按任务奖励选出"下一代"（PhysicalRSI 类）。与 [RobotEvolve]({{< relref "/research/RobotEvolve" >}}) 聚焦机器人 VLA 与 sim-to-real 数据飞轮不同，PhysicalEvolve 关心的是更一般的问题：当被改进的对象从数字世界延伸到物理世界，自进化闭环的证据链、选择压力与方法积累应如何组织。社区关注的核心问题包括：模型与实验对不上时如何区分参数不准、求解出错与方程遗漏；通用大模型的语义理解如何转化为精密操作能力；一次失败的分析如何落实为下一代实际运行的代码与配置；以及如何让"能力提升"可追溯到具体版本、交互记录与选择过程。

## 研究挑战

- 多物理场耦合与不可观测内部状态：传输、反应、能量交换相互耦合，关键状态量难以在线实测，单凭外部曲线难以定位错在何处。
- 偏差归因的组合爆炸：参数、机制、几何、边界条件、数值求解都可能是"嫌疑人"，物理 AI 还要再加上通信、接口、本体执行一整套机器人系统。
- 方法而非记录的积累：实验显示"保留完整历史"或"只留摘要"都接近基线，真正拉开差距的是从成败中学会"下一步怎样做"，如何提炼并检验这种方法是开放问题。
- 理解之后的控制鸿沟：通用大模型在 RoboDojo 总分领先但精密操作成功率极低，抓取后的姿态调整、对准插入与多步衔接仍需系统级编排。
- 真机评测的成本与透明度：完整 checkpoint 评测动辄数百次真机执行、数十万美元训练成本，长时间公开会同时暴露模型、硬件、接口与运维边界。
- 自进化中的选择压力与作弊：由任务奖励或成功率定义"适者生存"时，候选 Harness、代码与技能是否会学到基准捷径而非可迁移能力。
- 跨领域可迁移性：从电池析锂、动态电压等可量化起点出发，验证同一套"实验—修订—方法"协同进化能否推广到材料、化工、生物工程等更多有实验数据的系统。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述；物理世界作为自进化闭环的终极验证场。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录物理建模与具身自改进相关工作。

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
1. **偏差驱动模型修订**：面对偏差，应先归因机制、方程、边界、参数、几何或接口，再并行验证，优先修复最早高频断点。机制可编译为带边界与闭合条件的方程部件，以组合失败定位缺失物理项。
   - [RoboAda：计划保持式指令校正](../../updates/2026-11-25/#roboada) · 2026-11-25
   - [物理机制构造：方程原生跨学科编译](../../updates/2026-11-25/#item-151) · 2026-11-25
   - [Mind2Act World：心智动作组合诊断](../../updates/2026-11-21/#mind2act-world) · 2026-11-21
   - [Cyber-Physical RSI：物理反馈闭环自改进](../../updates/2026-11-20/#cyber-physical-rsi) · 2026-11-20
   - [RoboBuilder：实机视频闭环机器人共设计](../../updates/2026-11-19/#robobuilder) · 2026-11-19
   - [Optics as Code：测量驱动光学训练](../../updates/2026-11-19/#optics-as-code) · 2026-11-19
   - [冻结世界模型动作自校正](../../updates/2026-11-19/#item-40) · 2026-11-19
   - [HypoLoop：反馈驱动权重编辑](../../updates/2026-11-19/#hypoloop) · 2026-11-19
   - [PhysLoop：以 LLM 物理认知驱动视频生成模型自我改进](../../updates/2026-11-14/#physloop-llm) · 2026-11-14
   - [梯度感知智能体通过可微 CFD 自主发现湍流模型](../../updates/2026-11-14/#cfd) · 2026-11-14
   - [智能体引导发现并物理验证交换-相关泛函 O159](../../updates/2026-11-12/#o159) · 2026-11-12
   - [智能体机器人自学习中的模型、技能、反馈与课程控制研究](../../updates/2026-11-12/#item-202) · 2026-11-12
   - [DriveFoundry：数据与模型协同演化的自动驾驶闭环框架](../../updates/2026-11-12/#drivefoundry) · 2026-11-12
   - [AI编码、拟合与迭代科学模型](../../updates/2026-11-08/#item-22) · 2026-11-08
   - [LLM 智能体改进地球系统模型参数化](../../updates/2026-11-06/#llm-4) · 2026-11-06
   - [自递归软硬件脚手架驱动自主光学实验](../../updates/2026-11-06/#item-64) · 2026-11-06
   - [EvoSim：自进化多物理场建模系统](../../updates/2026-11-01/#evosim) · 2026-11-01
2. **双层递归改进**：将任务策略与工作流、记忆、验证器等脚手架分层演化；权重更新昂贵时，先改可审计的外部程序也能获得大幅提升。
   - [Self-Upgrading Embodied Agents：经验驱动权重自升级](../../updates/2026-11-25/#self-upgrading-embodied-agents) · 2026-11-25
   - [PhyEvo-Mic-RSI：物理引导显微分析自进化](../../updates/2026-11-25/#phyevo-mic-rsi) · 2026-11-25
   - [Agnes Harness：双系统决策与双层自进化](../../updates/2026-11-20/#agnes-harness) · 2026-11-20
   - [MatOS：证据驱动的科研资产进化](../../updates/2026-11-18/#matos) · 2026-11-18
   - [RSI-PDEbench：偏微分方程求解智能体递归自我改进基准](../../updates/2026-11-13/#rsi-pdebench) · 2026-11-13
   - [SimplEvo：通过文本记忆演化提升具身智能体](../../updates/2026-11-12/#simplevo) · 2026-11-12
   - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
   - [AI 智能体自主优化原子模拟数值算法](../../updates/2026-11-12/#item-94) · 2026-11-12
   - [VISTA：机器人通过自编程实现不动权重的具身自进化](../../updates/2026-11-08/#vista) · 2026-11-08
   - [WeightLoop：基于实验反馈的权重空间编程](../../updates/2026-11-06/#weightloop) · 2026-11-06
   - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
   - [PhysicalRSI 1.0通过具身递归自我改进登顶RoboDojo](../../updates/2026-11-01/#physicalrsi-1-0-robodojo) · 2026-11-01
3. **主动交互辨识**：模型或搜索空间失配时，应主动选择信息量高且近似有效的物理实验，辨识隐藏参数与操作规律，并在连续交互中校准。
   - [Cyber-Physical RSI：物理反馈闭环自改进](../../updates/2026-11-20/#cyber-physical-rsi) · 2026-11-20
   - [Optics as Code：测量驱动光学训练](../../updates/2026-11-19/#optics-as-code) · 2026-11-19
   - [SciResearch-Eval：科学判断力交互评测](../../updates/2026-11-18/#sciresearch-eval) · 2026-11-18
   - [自动显微镜异构多步工作流：奖励设计与知识迁移](../../updates/2026-11-12/#item-226) · 2026-11-12
   - [具身科学智能体：让实验设计具备可学习性](../../updates/2026-11-12/#item-157) · 2026-11-12
   - [自驱动实验室物理测试床：贝叶斯与智能体优化对比](../../updates/2026-11-12/#item-125) · 2026-11-12
   - [CUE：通过自主机器人交互弥合动力学鸿沟](../../updates/2026-11-06/#cue) · 2026-11-06
4. **实验反馈质控**：真实实验须标准化执行、校准漂移并保留可独立复算的原始证据；否则噪声、违规执行或报告偏差会被固化为奖励。
   - [Data to Valves：端侧自学习暖通控制](../../updates/2026-11-19/#data-to-valves) · 2026-11-19
   - [世界即测试套件：具身程序可信验证](../../updates/2026-11-18/#item-39) · 2026-11-18
   - [WindPilot：原始证据绑定式仿真验证](../../updates/2026-11-17/#windpilot) · 2026-11-17
   - [ProTEUS：面向闭环蛋白质进化的突变解析世界模型](../../updates/2026-11-12/#proteus) · 2026-11-12
   - [涌生智能将云端自主实验室打造为AI物理进化训练场](../../updates/2026-11-12/#item-46) · 2026-11-12
   - [自动显微镜异构多步工作流：奖励设计与知识迁移](../../updates/2026-11-12/#item-226) · 2026-11-12
   - [可审计人机团队自主开展同步辐射 X 射线实验](../../updates/2026-11-12/#item-199) · 2026-11-12
   - [DFT-Agent Bench：自主 DFT 的脚手架效应与执行溯源评测](../../updates/2026-11-12/#dft-agent-bench-dft) · 2026-11-12
   - [AISLE：全球首个真实湿实验 AI Scientist 评测基准](../../updates/2026-11-12/#aisle-ai-scientist) · 2026-11-12
   - [具身科学发现：从物理行动到科学证据](../../updates/2026-11-06/#item-150) · 2026-11-06
   - [EnzymeRSI：用于酶设计的双循环递归自我改进系统](../../updates/2026-11-05/#enzymersi) · 2026-11-05
5. **验证器过拟合防控**：自改进时不要暴露可被投机的精确评分规则；验证器须绑定任务契约和后续闭环结果，并用未暴露任务检验迁移。
   - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
   - [EviCraft：证据闭包式具身评测](../../updates/2026-11-25/#evicraft) · 2026-11-25
   - [AeroRSI：续飞验证式递归自改进](../../updates/2026-11-19/#aerorsi) · 2026-11-19
   - [WindPilot：原始证据绑定式仿真验证](../../updates/2026-11-17/#windpilot) · 2026-11-17
   - [Verifiable pXRD：验证器引导的爬山解析](../../updates/2026-11-16/#verifiable-pxrd) · 2026-11-16
   - [AI 智能体自主优化原子模拟数值算法](../../updates/2026-11-12/#item-94) · 2026-11-12
   - [DFT-Agent Bench：自主 DFT 的脚手架效应与执行溯源评测](../../updates/2026-11-12/#dft-agent-bench-dft) · 2026-11-12
   - [学习任务还是学习验证器？具身自我改进中的标准暴露](../../updates/2026-11-08/#item-32) · 2026-11-08
6. **异质真机评测**：真机能力应在多本体、多任务和OOD环境中统一评测，兼看动作—意图偏差、轨迹进展、部署故障与成本；单一终局分数不能证明物理泛化。
   - [WorldLeague：物理能动性统一评测](../../updates/2026-11-25/#worldleague) · 2026-11-25
   - [AgentRoboCritic：意图锚定动作级评测](../../updates/2026-11-24/#agentrobocritic) · 2026-11-24
   - [WorldFoundry：面向世界智能的统一基础设施](../../updates/2026-11-12/#worldfoundry) · 2026-11-12
   - [Embodied First Exam：编码智能体具身控制综合评测](../../updates/2026-11-12/#embodied-first-exam) · 2026-11-12
   - [RoboColosseum：大规模真实场景物理智能评测框架](../../updates/2026-11-05/#robocolosseum) · 2026-11-05
   - [Motubrain 2.0 开启 Physical AI 全流程训练直播](../../updates/2026-10-30/#motubrain-2-0-physical-ai) · 2026-10-30
7. **课程策略域适配**：统一预算下没有课程或域随机化方法跨本体稳定占优；先用简单起点和子任务进度定位首个瓶颈，再按瓶颈加练，避免盲目增难。
   - [ReFocus：进度引导式瓶颈加练](../../updates/2026-11-25/#refocus) · 2026-11-25
   - [LS-MBPO：潜空间子块滚动强化](../../updates/2026-11-23/#ls-mbpo) · 2026-11-23
   - [智能体机器人自学习中的模型、技能、反馈与课程控制研究](../../updates/2026-11-12/#item-202) · 2026-11-12
   - [四足机器人无监督环境设计与课程学习基准](../../updates/2026-10-30/#item-41) · 2026-10-30
8. **风险约束持续学习**：持续学习要同时检查旧技能与OOD能力，按动力学风险限制可塑性；部署时依错误成本和校准置信度选择执行、追问或拒绝，并固化安全边界。
   - [预训练VLA持续学习：分布外遗忘诊断](../../updates/2026-11-25/#vla) · 2026-11-25
   - [nanoAstra：语义动作建模与能力保持微调](../../updates/2026-11-25/#nanoastra) · 2026-11-25
   - [CATWAY：成本敏感三路决策](../../updates/2026-11-25/#catway) · 2026-11-25
   - [NoPeWorld：隐状态穿透防控](../../updates/2026-11-24/#nopeworld) · 2026-11-24
   - [ZeroVLN：语义工具调用免微调导航](../../updates/2026-11-21/#zerovln) · 2026-11-21
   - [Data to Valves：端侧自学习暖通控制](../../updates/2026-11-19/#data-to-valves) · 2026-11-19
   - [MetaAct：可执行动作约束自演化](../../updates/2026-11-17/#metaact) · 2026-11-17
   - [SPIRE：基于情境推断与因果运动基元复用的具身持续学习](../../updates/2026-11-13/#spire) · 2026-11-13
   - [强化学习扩展通用机器人策略的多任务改进能力](../../updates/2026-11-06/#item-25) · 2026-11-06
   - [DRAP：面向物理 AI 持续学习的动力学风险自适应可塑性](../../updates/2026-11-06/#drap-ai) · 2026-11-06
   - [智元发布具身智能模型 GO-3 Preview](../../updates/2026-11-02/#go-3-preview) · 2026-11-02
9. **人机经验联合预训**：用人类视频扩大语义与动作覆盖，再以异构机器人数据持续训练，可提升跨本体迁移，但需学习共享动作或空间表征。
   - [RynnVLA-Latent：几何潜动作预训练](../../updates/2026-11-25/#rynnvla-latent) · 2026-11-25
   - [Native LAM：世界模型提炼潜在动作](../../updates/2026-11-25/#native-lam) · 2026-11-25
   - [TCP4D：统一TCP跟踪与轨迹生成](../../updates/2026-11-19/#tcp4d-tcp) · 2026-11-19
   - [SALA：语义对齐潜在动作双轴扩展](../../updates/2026-11-18/#sala) · 2026-11-18
   - [Ropedia Xperience 2：扩展具身环境与行为数据的黄金标准](../../updates/2026-11-14/#ropedia-xperience-2) · 2026-11-14
   - [SLA：通过持续预训练扩展空间-语言-动作模型](../../updates/2026-11-08/#sla) · 2026-11-08
   - [Open-HumanWAM：扩展人类与机器人经验的开放具身基础模型方案](../../updates/2026-11-08/#open-humanwam) · 2026-11-08
   - [DreamX：视频扩散模型驱动的通用潜在动作学习](../../updates/2026-11-05/#dreamx) · 2026-11-05
   - [智元发布具身智能模型 GO-3 Preview](../../updates/2026-11-02/#go-3-preview) · 2026-11-02
10. **真机锚定仿真数据**：以少量真实标定持续校准仿真，再规模化生成动作标注数据，比完全依赖人工真机采集更易扩展且更可部署。
    - [RoboUniverse-10K：万级可验证具身环境](../../updates/2026-11-25/#robouniverse-10k) · 2026-11-25
    - [RoboBuilder：实机视频闭环机器人共设计](../../updates/2026-11-19/#robobuilder) · 2026-11-19
    - [PyRUA-DataFarm：LLM 远程操作者驱动的真实场景机器人数据采集](../../updates/2026-11-06/#pyrua-datafarm-llm) · 2026-11-06
    - [CUE：通过自主机器人交互弥合动力学鸿沟](../../updates/2026-11-06/#cue) · 2026-11-06
11. **分层异步实时控制**：把慢速语言推理与快速控制解耦，按事件或算力预算启用高层；低层用蒸馏、并行化或决策敏感量化满足时限。
    - [LAQ：潜变量感知四比特量化](../../updates/2026-11-20/#laq) · 2026-11-20
    - [DRIFT：可拆卸语言推理驾驶](../../updates/2026-11-20/#drift) · 2026-11-20
    - [Vanguard：截图感知式草稿判别](../../updates/2026-11-19/#vanguard) · 2026-11-19
    - [ForceHarness：冻结模型力觉闭环](../../updates/2026-11-19/#forceharness) · 2026-11-19
    - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
    - [VFlash：闪光基元解码加速精准视觉规划](../../updates/2026-11-08/#vflash) · 2026-11-08
    - [REA：异步脑-小脑控制的路由式具身智能体运行时](../../updates/2026-11-03/#rea) · 2026-11-03
    - [OSWAM：单步动作生成的世界动作模型](../../updates/2026-11-03/#oswam) · 2026-11-03
12. **经验结构化复用**：把成败轨迹压缩成可检索且经证据审查的记忆、技能或资产；对可能复现的惯例保留原始观测与情境，避免摘要抹去时序证据。
    - [XMind：跨记忆反事实复核](../../updates/2026-11-25/#xmind) · 2026-11-25
    - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
    - [保留观测历史应对惯例复现](../../updates/2026-11-25/#item-117) · 2026-11-25
    - [ReSpaceBench：跨重访空间记忆评测](../../updates/2026-11-24/#respacebench) · 2026-11-24
    - [NavTTT：导航条件式分层参数记忆](../../updates/2026-11-23/#navttt) · 2026-11-23
    - [LoCo-WAM：测试时训练延展长上下文](../../updates/2026-11-23/#loco-wam) · 2026-11-23
    - [F³：形适融经验利用](../../updates/2026-11-20/#item-76) · 2026-11-20
    - [MatOS：证据驱动的科研资产进化](../../updates/2026-11-18/#matos) · 2026-11-18
    - [场景记忆选择性更新](../../updates/2026-11-17/#item-85) · 2026-11-17
    - [MolRSI：跨任务经验驱动策略自改进](../../updates/2026-11-15/#molrsi) · 2026-11-15
    - [SPIRE：基于情境推断与因果运动基元复用的具身持续学习](../../updates/2026-11-13/#spire) · 2026-11-13
    - [WICL：面向智能体机器人操作的世界上下文学习](../../updates/2026-11-12/#wicl) · 2026-11-12
    - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
    - [SimplEvo：通过文本记忆演化提升具身智能体](../../updates/2026-11-12/#simplevo) · 2026-11-12
    - [REINS：面向实时轨迹规划的自进化智能体脚手架](../../updates/2026-11-12/#reins) · 2026-11-12
    - [具身双脑协同：让机器人跨任务复用经验](../../updates/2026-11-08/#item-19) · 2026-11-08
    - [Auto-Robotist：用可复用经验驱动机器人协同设计](../../updates/2026-11-08/#auto-robotist) · 2026-11-08
    - [HTCE：受同胚启发的跨场景导航经验规范化与复用](../../updates/2026-11-06/#htce) · 2026-11-06
13. **世界模型服务决策**：世界模型不必完整生成未来；将隐状态或短程想象对齐动作接口，可用于候选重排、安全约束和训练信号，兼顾预见与低延迟。
    - [ViDecide：决策中心式视频规划](../../updates/2026-11-25/#videcide) · 2026-11-25
    - [NoPeWorld：隐状态穿透防控](../../updates/2026-11-24/#nopeworld) · 2026-11-24
    - [LS-MBPO：潜空间子块滚动强化](../../updates/2026-11-23/#ls-mbpo) · 2026-11-23
    - [冻结世界模型动作自校正](../../updates/2026-11-19/#item-40) · 2026-11-19
    - [BirdDreams：联合透视与 BEV 视频生成的驾驶世界模型](../../updates/2026-11-14/#birddreams-bev) · 2026-11-14
    - [DexForesight：以隐式空间预见增强灵巧操作策略](../../updates/2026-11-12/#dexforesight) · 2026-11-12
    - [Jev-AD：基于语言世界模型的安全自动驾驶](../../updates/2026-11-06/#jev-ad) · 2026-11-06
14. **仿真排序敏感性**：评估仿真器时，应测试误差是否改变候选排序与设计结论，并主动寻找近似仍成立的条件，而非只量绝对输出偏差。
    - [SciResearch-Eval：科学判断力交互评测](../../updates/2026-11-18/#sciresearch-eval) · 2026-11-18
    - [SIRIS：评测 LLM 对仿真误差影响的判断能力](../../updates/2026-11-12/#siris-llm) · 2026-11-12
15. **检索基线先行**：评估VLA学习或自进化前应先做近邻动作复用基线；高分可能来自演示检索，而非形成了可迁移的新策略。
    - [MXI-MemICL：自检索交互记忆](../../updates/2026-11-25/#mxi-memicl) · 2026-11-25
    - [VLA 有多少能力来自 kNN 检索？](../../updates/2026-11-12/#vla-knn) · 2026-11-12
<!-- experience-seen: 2026-10-30/item-41 2026-10-30/motubrain-2-0-physical-ai 2026-11-01/evosim 2026-11-01/physicalrsi-1-0-robodojo 2026-11-02/go-3-preview 2026-11-03/oswam 2026-11-03/rea 2026-11-05/dreamx 2026-11-05/enzymersi 2026-11-05/robocolosseum 2026-11-06/cue 2026-11-06/drap-ai 2026-11-06/htce 2026-11-06/item-150 2026-11-06/item-25 2026-11-06/item-64 2026-11-06/jev-ad 2026-11-06/llm-4 2026-11-06/pyrua-datafarm-llm 2026-11-06/solv3r-transformer 2026-11-06/weightloop 2026-11-08/auto-robotist 2026-11-08/item-19 2026-11-08/item-22 2026-11-08/item-32 2026-11-08/open-humanwam 2026-11-08/sla 2026-11-08/vflash 2026-11-08/vista 2026-11-12/aisle-ai-scientist 2026-11-12/dexforesight 2026-11-12/dft-agent-bench-dft 2026-11-12/drivefoundry 2026-11-12/embodied-first-exam 2026-11-12/gr00t-2 2026-11-12/holidayfactory-1-0 2026-11-12/item-125 2026-11-12/item-157 2026-11-12/item-199 2026-11-12/item-202 2026-11-12/item-226 2026-11-12/item-46 2026-11-12/item-94 2026-11-12/lingbot-touch 2026-11-12/o159 2026-11-12/proteus 2026-11-12/reins 2026-11-12/simplevo 2026-11-12/siris-llm 2026-11-12/splatanything-3dgs 2026-11-12/vla-knn 2026-11-12/wicl 2026-11-12/worldfoundry 2026-11-13/rsi-pdebench 2026-11-13/spire 2026-11-14/birddreams-bev 2026-11-14/cfd 2026-11-14/physloop-llm 2026-11-14/ropedia-xperience-2 2026-11-15/molrsi 2026-11-16/verifiable-pxrd 2026-11-16/vla 2026-11-17/gamer 2026-11-17/item-85 2026-11-17/metaact 2026-11-17/robofinals-rl-envs 2026-11-17/windpilot 2026-11-18/item-39 2026-11-18/matos 2026-11-18/sala 2026-11-18/scalevla-vlm-dit 2026-11-18/sciresearch-eval 2026-11-19/aerorsi 2026-11-19/data-to-valves 2026-11-19/forceharness 2026-11-19/heave-ho 2026-11-19/hypoloop 2026-11-19/item-40 2026-11-19/optics-as-code 2026-11-19/robobuilder 2026-11-19/tcp4d-tcp 2026-11-19/vanguard 2026-11-20/agnes-harness 2026-11-20/coachsi 2026-11-20/cyber-physical-rsi 2026-11-20/drift 2026-11-20/item-76 2026-11-20/laq 2026-11-21/depth-pro-2 2026-11-21/mind2act-world 2026-11-21/turingspace 2026-11-21/voda 2026-11-21/zerovln 2026-11-23/bel 2026-11-23/loco-wam 2026-11-23/ls-mbpo 2026-11-23/navttt 2026-11-24/agentrobocritic 2026-11-24/nopeworld 2026-11-24/respacebench 2026-11-24/scape 2026-11-24/stereovlm 2026-11-25/catway 2026-11-25/embo-harness 2026-11-25/evicraft 2026-11-25/gpt-6 2026-11-25/item-117 2026-11-25/item-151 2026-11-25/mxi-memicl 2026-11-25/nanoastra 2026-11-25/native-lam 2026-11-25/ovogo 2026-11-25/phyevo-mic-rsi 2026-11-25/plan4d-4d 2026-11-25/refocus 2026-11-25/roboada 2026-11-25/robouniverse-10k 2026-11-25/rynnvla-latent 2026-11-25/self-upgrading-embodied-agents 2026-11-25/videcide 2026-11-25/vla 2026-11-25/worldleague 2026-11-25/xmind -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架 / 项目**
- [PhysicalRSI 1.0](https://mmlab.hk/research/PhysicalRSI) — 港大 MMLAB 提出的具身递归自我改进基线：System 1–2 协同自进化 + Embodied Self-Harness，父代依据录像、动作记录与评估反馈生成绑定不同工具、代码、记忆与技能的子代，由物理环境按奖励选择可继承版本
- [Motubrain 2.0 训练直播](https://www.motubrain.com/motubrain2.0-live/) — 生数科技 Motubrain 团队（朱军带队）公开 Physical AI 预训练全流程：训练步数、Loss、成本、checkpoint 部署与四套双臂机器人的真机 OOD 评测实时可见，技术路线为 Agentic WAM + RSI
- [Eureka](https://github.com/eureka-research/Eureka) — LLM 编码自动设计奖励函数，达到人类水平
- [DrEureka](https://github.com/eureka-research/DrEureka) — LLM 引导的 sim-to-real 迁移（奖励 + 域随机化自动设计）
- [RoboGen](https://github.com/Genesis-Embodied-AI/RoboGen) — 生成式仿真自动提出任务、生成场景并采集技能数据
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) — 面向机器人与具身 AI 的生成式物理引擎
- [openpi (π0 / π0.5)](https://github.com/Physical-Intelligence/openpi) — Physical Intelligence 开源通用机器人策略，PhysicalRSI 将其作为可调用的动作工具之一
- [PySR](https://github.com/MilesCranmer/PySR) — 高性能符号回归库，从数据中发现可解释的物理方程

**论文**
- [EvoSim: Learning to Model, Modeling to Learn](https://arxiv.org/abs/2610.11344) — 清华张强团队联合清屿科技、港大、怀柔实验室提出的自进化多物理场建模系统：以实验偏差驱动机制与方程修订，同一轮试错既产生更准的模型也沉淀可复用的建模方法；析锂起点 SOC 平均绝对误差 1.79%，动态电压 RMSE 7.62 mV，均优于人类专家历史模型；方法积累使最佳有效误差比保留完整历史的对照低 75.4%，11 项任务 45 组运行中失败减少 36.4%、累计执行时间减少 42.6%
- [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs](https://arxiv.org/abs/1711.10561) — PINN 奠基工作，把物理方程作为约束嵌入学习
- [Discovering governing equations from data by sparse identification of nonlinear dynamical systems (SINDy)](https://arxiv.org/abs/1509.03580) — 从数据稀疏识别控制方程
- [AI Feynman: a Physics-Inspired Method for Symbolic Regression](https://arxiv.org/abs/1905.11481) — 物理启发的符号回归，自动发现物理公式
- [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) — 奖励函数的进化搜索
- [DrEureka: Language Model Guided Sim-To-Real Transfer](https://arxiv.org/abs/2406.01967)
- [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) — 自提任务 + 生成仿真的数据飞轮
- [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) — 流匹配动作生成的通用机器人策略
- [Mastering Diverse Domains through World Models (DreamerV3)](https://arxiv.org/abs/2301.04104) — 世界模型驱动的通用智能体学习

**综述 / 报道**
- [AI如何解析物理世界？清华联合清屿科技等团队推出自进化多物理场建模系统EvoSim](https://mp.weixin.qq.com/s/28C3URVrOK4V4JSRlWNCgg) — 机器之心报道。EvoSim 让 AI 从"给定方程下调参"走向"从实验偏差中追查机制、修订方程、改进建模方法"：并行提出参数、机制、几何、边界条件等候选解释，每条候选接受物理合理性、数值可靠性、预测贴合度与机制可辨识性四重追问；失败候选的失败条件与步骤也被记录并用于修正建模程序。电池快充析锂（61 个电池、20 组起点条件）与真实驾驶动态电压（8 个温度、16 条轨迹、109,746 个采样点）两个工业级场景验证
- [Physical AI 领域首次训练直播，全流程透明开放！](https://mp.weixin.qq.com/s/G01CUHbhexA5S3EvxKKn8Q) — 具身智能之心报道。Motubrain 2.0-PT 两周公开预训练：每个完整 checkpoint 需在 Clean / Random 两组条件下完成抽屉收纳、擦白板、跨手收纳、挂耳机、插花、叠碗杯盘 6 类任务共 288 次真机执行，Random 组加入干扰物与 0.2 Hz 变化彩色灯光，并设阶段评分记录失败在第几步；约 5 万步时成本约 43.55 万美元（含一次因数据问题重训），Random / Clean 成功率 48.61% / 58.47%、平均分 63.06 / 76.09；团队下一步将推进 Agent 与 RSI 闭环：从失败中区分模型、数据或执行系统问题，筛选有价值经验进入下一轮训练
- [中国团队提出PhysicalRSI 1.0，比GPT-6 Astra节省百倍Tokens，霸榜RoboDojo～](https://mp.weixin.qq.com/s/niXIBI3OIQc2UvuDZ0J8-Q) — 具身智能之心报道。截至 2026-09-28，PhysicalRSI 1.0 在 RoboDojo 42 项任务上取得 36.27 Score / 31.38% SR 位列第一（Simate-beta 33.95 / 27.96%，GPT-6 Astra 28.97 / 22.48%，单独 π0.5 11.44 / 6.93%），全量评测 Token 成本约为 Astra 的百分之一；精密操作上插钥匙 39.33%、插管 66%，而 Astra 对应为 0%。核心是让 System 2 改写 System 1 的动作程序、工具、记忆与技能及二者协作的 Harness，例如把"记录下降路径并沿路径回撤"作为可继承方法，使叠衣服在衣物位置变化后仍能重建状态
