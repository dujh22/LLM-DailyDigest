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
