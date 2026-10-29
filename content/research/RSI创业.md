+++
title = 'RSI创业'
proposer = '杜晋华'
since = '2026-10-29'
date = 2026-10-29T00:00:00+08:00
draft = false
toc = true
+++

# RSI创业

> 研究方向：**RSI 创业与产业化**——跟踪以递归自我改进（Recursive Self-Improvement, RSI）为核心叙事的初创公司、融资事件、商业化路径与产业生态位，回答"RSI 作为一门生意，能否成立、在哪一层先成立"。

## 研究范畴

RSI 创业（RSI entrepreneurship）是本站的产业侧横向跟踪方向，与 [[Awesome-RSI]] 的分工是：Awesome-RSI 关心 RSI 的方法与论文，本方向关心 RSI 如何变成公司、产品与资本叙事。本方向涵盖：以 RSI 为主线融资的基模公司与初创团队（如智谱的"完全自训练"体系与 GLM-5.3 Infra Agent、Richard Socher 的 Recursive、超衍智能、Novix、Evolvent AI、芯生代、通衍灵智、域变换、Mind Lab 等）；RSI 产业图谱中的各个生态位——数据自产、环境自造、Verifier 与评测、Harness 与脚手架、后训练平台、推理基础设施自优化、具身部署时自进化、个人 / 企业专属模型；"AI 研究 AI"（AI4AI）与科研自动化作为创业切入点；企业 Agent 等被认为最可能率先闭环的落地场景；资本市场对 RSI 叙事的定价与估值逻辑；以及中美在 RSI 路径上的差异（自下而上的商业驱动 vs 国家主导）。社区关注的核心问题包括：RSI 在哪一层最先产生可验证的商业回报、"自我改进"能否形成持续的护城河而非一次性优化、创业公司如何在基模厂商的 RSI 投入面前找到位置、以及 RSI 叙事与安全治理（减速呼吁、智能爆炸风险）之间的张力如何影响融资与监管环境。

## 研究挑战

- 验证与叙事的落差：多数公司以"RSI"为融资叙事，但可公开核验的闭环案例（如基础设施吞吐提升）仍是少数，难以区分真实自改进与一次性工程优化。
- 护城河来源不清：改进来自模型、数据、Harness 还是基础设施反馈，决定了创业公司与基模厂商之间的竞争边界。
- 反馈信号稀缺：只有具备诚实、稠密、可归因反馈的场景（推理引擎、企业 Agent、科研实验）才可能先闭环，多数业务场景不满足此条件。
- 算力与资本门槛：基模层 RSI 需要数十亿美元级投入，初创公司只能选择垂直层或工具层切入，生态位易被挤压。
- 安全与监管不确定性：头部实验室的减速呼吁与学界对智能爆炸的警告，可能转化为对 RSI 类公司的披露与部署约束。
- 评价缺位：没有统一的"RSI 自主性等级"或商业成熟度标尺，投资判断缺少可比基线。
- 人才稀缺：同时懂后训练、Agentic RL、评测体系与基础设施的复合型人才极少，招募本身成为竞争焦点。

## 自研项目

- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 面向 RSI 的持续研究项目，本方向的产业条目是其论文 / 方法清单的产业侧补充。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，RSI 创业跟踪为其"从研究到产业"的观察窗口。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 持续采集 RSI 相关融资、公司动态与产业分析的信息流水线，本页「相关工作」由其日报条目自动聚合。

## 相关工作

**代码 / 框架**
- [autoresearch (karpathy)](https://github.com/karpathy/autoresearch) — 自动闭合"提出想法—实现—实验—验证"研究循环的开源原型，是 Recursive 等"AI 研究 AI"公司的公共参照
- [novix-science](https://github.com/novix-science) — Novix 的开源组织，围绕 RSI、AI4AI 与 Agentic RL 的科研合作入口
- [Recursia](https://github.com/cocacola-lab/Recursia) — 北京灵行智能科技等机构发布的具身递归自我改进框架，校企合作走向产品化的样本

**论文**
- [Recursive Self-Improvement in AI (Survey)](https://arxiv.org/abs/2607.07663) — 覆盖 1250 篇论文的 RSI 综述，产业跟踪的概念基线
- [How to Realize Recursively Self-Improving Agents](https://arxiv.org/abs/2607.12254) — 治理式多 Agent RSI 架构，对应"Harness + Verifier"类创业路线
- [RSI 正在重走深度学习的老路](https://arxiv.org/abs/2610.14625) — 将 RSI 与优化、元学习、蒸馏、持续学习等成熟机制逐一对应，解释为何工程化路径正在收敛
- [Anthropic 联创将 RSI 预期提前至 2027 年（关联论文）](https://arxiv.org/abs/2610.06824) — Jack Clark 等基于数学推理、科研品味与自动编程进展给出的时间判断，直接影响资本预期

**公司 / 融资**
- [智谱融资 335 亿元，60% 投向 GLM 与 RSI 研发](https://mp.weixin.qq.com/s/k0jnzEhPF-xg2HdDZX8fPw) — 约 50 亿美元融资中约六成投入下一代 GLM、"完全自训练"体系（数据自产、环境自造、基础设施自我优化）与算力，是基模层 RSI 投入的标杆案例
- [智谱 GLM-5.3 Infra Agent 展现 RSI 早期形态](https://www.qbitai.com/2026/09/491357.html) — 在超 10 万张国产加速卡集群上，由 GLM-5.3 驱动的 Infra Agent 两周内把生产推理服务的端到端吞吐提升到基线约 3 倍，是目前最可核验的"模型优化系统、系统服务模型"闭环
- [Recursive 获 6.5 亿美元押注"AI 研究 AI"](https://mp.weixin.qq.com/s/eEAAXyl8OiMWHFlABdu_MQ) — Richard Socher 创办，以自动化研究循环为起点迈向递归超级智能
- [超衍智能融资近 4 亿元，押注基模层递归自我改进](https://mp.weixin.qq.com/s/D0bLvGvZfPlPT1Fph5NaDg) — 清华陈勇超创立，以科研轨迹驱动基模与 Harness 的递归改进
- [Novix 跑通协同进化式 RSI 规模化闭环](https://mp.weixin.qq.com/s/iLtJ8g3xwawKfnoShFBIFg) — AI 自主探索 + 专家持续反馈 + 系统能力回流，应用于后训练与科学工程任务；另见其[研究人才招募](https://mp.weixin.qq.com/s/gjk73y5IrBu52msSN6XTog?scene=1)
- [专访胡梦康：Agent 之后，下一站是 AI 自我进化](https://mp.weixin.qq.com/s/ZcCsfjXF1J4QYAQl8KYEHw) — Evolvent AI 创始人提出以 Data、Environment、Verifier、Harness、Experience 构建 Evolution OS
- [芯生代融资数千万元，打造 Agent 自进化推理引擎](https://mp.weixin.qq.com/s/X0Ty_Ke_mtiACMcnSmDbpQ) — 上海交大团队种子轮，Agent 针对"模型 × 芯片 × 场景"组合生成并迭代定制推理引擎；文中亦提及前英伟达工程师创办的 INT21，详见 [[InfraEvolve]]
- [通衍灵智推出可持续进化 Personal AI](https://aiera.com.cn/asi-preview/asi-item.html?id=tgb48e88) — 北京通用人工智能研究院孵化，以 Personal LoRA + 评估闭环 + 训推基础设施做个人 / 企业专属模型的 RSI
- [域变换提出具身自进化部署范式](https://mp.weixin.qq.com/s/u1RQ8g6YQ9kt8n6KIszhGQ) — 清华 AIR 曹婷团队与域变换的 Zeva / Zetta ζ / Z-Infra，机器人部署后从真实交互中持续提升
- [Mind Lab 推出自迭代后训练平台 Mint Recursive](https://mp.weixin.qq.com/s/dLrLWtAMhQBRQlNSUCgSQg) — 评测、数据、后训练、部署、生产反馈闭环，面向企业的低成本专用模型持续迭代
- [30B 模型端侧运行，Ember 推理引擎探索自进化](http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247936009&idx=1&sn=e6fb685ed336535de3f97dbdda25b34a&chksm=e94720a9900acc6c4661a7e8b4983071434e1057d3837319a0ff5f591ecba90f30cdafe8531d&scene=0&xtrack=1#rd) — 无量火科技在端侧推理层探索可积累优化经验的自进化系统
- [Mirendil 与 Recursive 发布 RSI 自动化研究成果](https://aiera.com.cn/asi-preview/asi-item.html?id=tg5a4a84) — 智能体主导的基座模型训练与自动研究闭环，同时强调人类判断与实验审计

**产业分析 / 报道**
- [RSI 产业图谱：围绕智能进化速度的新竞赛](https://mp.weixin.qq.com/s/heLOhdyxEqK7RGt2Jaf9Nw) — Z Research 将 RSI 拆解为数据、模型、Harness、改进方法与评价标准五个生态位
- [RSI 递归自我改进：定义、评估验证与创业机会](https://mp.weixin.qq.com/s/VIPVAk0cxj5e9L36uIO-HQ) — 甲子光年组织清华、上交与创业界研究者讨论 RSI 的阶段定义、验证难点与产业生态位
- [RSI 早期产业形态或率先落地企业 Agent](https://mp.weixin.qq.com/s/YGVvrn846F2ZsoYj5q3rCw) — 认为企业 Agent 凭借明确任务、可验证结果与持续反馈轨迹最可能先形成产业化闭环
- [中国特色的 RSI：中美递归式自我改进路径差异](https://mp.weixin.qq.com/s/_sFhKJ-vPMJxd1mPZEva2A?scene=1) — 中国的 RSI 主要由企业融资、研发自动化与算力约束自下而上驱动
- [79 页综述提出 RSI 五级自主性分层架构](https://mp.weixin.qq.com/s/Ttmci98QZIL5dAcWOX3-Pg?scene=1) — 上交联合清华、字节跳动以改进环路为单位提出 B0–L5 分层，可作为评估公司 RSI 成熟度的参照标尺
- [《State of AI Report 2026》：RSI 走向台前](https://mp.weixin.qq.com/s/R0kCieHTz1D6yv9YTmy4CQ) — Air Street Capital 年度报告将 RSI 与 AI 参与 AI 研发列为核心趋势
- [持续学习赛道升温：Karpathy 称仍需十年](https://mp.weixin.qq.com/s/36ckT5YKJbVuq8754RC1BA) — 技术成熟度判断与创业热度之间的落差
- [Hinton 等 22 人警告 RSI 或触发智能爆炸](https://mp.weixin.qq.com/s/FBLlIVgdEdEgY_hxOM5hYg) — 治理侧对 RSI 商业化的约束来源之一
- [Dario 呼吁 AI 减速，OpenAI 因安全风险暂缓 IPO](https://www.qbitai.com/2026/09/488380.html) — 头部实验室的减速叙事直接作用于资本市场
