+++
title = 'NewApply'
proposer = '杜晋华'
since = '2026-10-21'
date = 2026-10-21T00:00:00+08:00
draft = false
toc = true
+++

# NewApply

> 研究方向：**新应用**——模型能力向真实产品与业务流程落地的跟踪，关注"能力如何变成可用的系统"，而非单个模型的技术指标。

## 研究范畴

新应用（new application watch）是本站的横向跟踪方向，与各 `*Evolve` 方向互补：`*Evolve` 关心方法如何自我改进，NewApply 关心这些方法进入真实场景后是否成立。本方向涵盖：智能体开发框架与编排层（多智能体对话、图式工作流、低代码平台）、端到端任务智能体（浏览器操作、桌面操作、软件工程、科研自动化）、本地部署与私有化推理栈、企业流程集成与 RPA 式自动化，以及垂直领域应用（编程、办公、金融、医疗、教育、客服）。社区关注的核心问题包括：demo 与生产的差距（长尾失败、错误累积、成本失控）、在开放环境中的可评测性（真实网站与真实桌面难以稳定复现）、人机责任边界与授权范围、私有化部署下的能力衰减，以及应用层价值究竟来自模型能力还是来自工程编排。

## 研究挑战

- demo 到生产的鸿沟：单步正确率高不代表多步任务可完成，长程错误累积是主要杀手。
- 评测环境不可复现：真实网站改版、桌面状态漂移使基准结果难以追踪与回归。
- 成本与延迟：多轮工具调用 + 长上下文的组合让单任务成本远高于纯对话。
- 安全与授权：浏览器 / 桌面 / 代码执行类智能体天然拥有高权限，提示注入与越权是结构性风险。
- 编排层的价值归因：同一模型在不同框架下表现差异巨大，收益来自模型还是脚手架难以拆分。
- 私有化部署的能力落差：量化、裁剪与本地硬件限制使落地效果弱于云端评测结论。

## 自研项目

- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站自身即是应用层实践：采集 → LLM 判定 → 标注 → 建站部署的完整流水线。
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
1. **生产级运行底座**：智能体落地应以可替换运行底座统一工具、沙箱、持久状态与评测，并支持回滚、分岔和迁移，避免业务逻辑绑定单一模型。
   - [Fin-RSI：统一金融技能与自改进](../../updates/2026-11-25/#fin-rsi) · 2026-11-25
   - [CubeSandbox：状态化微虚拟机沙箱](../../updates/2026-11-18/#cubesandbox) · 2026-11-18
   - [Code Mode：脚本化工具编排](../../updates/2026-11-18/#code-mode) · 2026-11-18
   - [DeepSeek Harness：可演化插件工作台](../../updates/2026-11-15/#deepseek-harness) · 2026-11-15
   - [uni-robot-agent：面向开源机器人智能体的统一 Harness](../../updates/2026-11-04/#uni-robot-agent-harness) · 2026-11-04
   - [Microsoft 通过 Foundry 开放 Copilot Harness，支持多模型智能体开发](../../updates/2026-10-29/#microsoft-foundry-copilot-harness) · 2026-10-29
   - [LangChain 开源设计智能体 Content Studio 的 harness](../../updates/2026-10-29/#langchain-content-studio-harness) · 2026-10-29
2. **分层规划与控制**：需兼顾长程决策与实时动作时，应拆分高层规划器和低延迟控制器，避免大模型直接承担帧级闭环。
   - [Embo-Harness：原生能力优先的机器人策略框架](../../updates/2026-11-25/#embo-harness) · 2026-11-25
   - [3AGameFactory-Motion：参数程序驱动动作生成](../../updates/2026-11-25/#3agamefactory-motion) · 2026-11-25
   - [AutoPILOT：实时游戏控制脚手架](../../updates/2026-11-24/#autopilot) · 2026-11-24
   - [TaskFrame：连接任务级规划与帧级控制的游戏智能体框架](../../updates/2026-10-30/#taskframe) · 2026-10-30
3. **分级模型路由**：高频边界明确任务优先用小型专用模型，并按校准置信度将复杂长尾升级旗舰模型；窄域微调需混入通用语料以防能力坍缩。
   - [WeMM-Ecom：电商多模态混合思考](../../updates/2026-11-25/#wemm-ecom) · 2026-11-25
   - [System 1决策模型：冻结编码器对比答题](../../updates/2026-11-19/#system-1) · 2026-11-19
   - [交通类型化决策模型：结构化低成本决策](../../updates/2026-11-19/#item-54) · 2026-11-19
   - [决策模型：低成本联络中心判别](../../updates/2026-11-19/#item-53) · 2026-11-19
   - [决策模型：带置信度的临床字段抽取](../../updates/2026-11-17/#item-86) · 2026-11-17
   - [小型决策模型在消费级 GPU 上规模化发现内存安全漏洞](../../updates/2026-11-14/#gpu) · 2026-11-14
   - [TrialJev：单次前向传播的开放权重临床试验资格评分器](../../updates/2026-11-12/#trialjev) · 2026-11-12
   - [金融小型决策模型：专业化坍缩与混合语料修复](../../updates/2026-11-06/#item-102) · 2026-11-06
   - [Decision Models：可扩展且保留人类差异的经济代理](../../updates/2026-11-06/#decision-models) · 2026-11-06
   - [开放视觉语言模型在放射学任务中的零样本 System 1 决策评测](../../updates/2026-11-03/#system-1) · 2026-11-03
   - [OpenAI 发布 GPT-6.1 Terra：电脑操作能力比肩 Astra，成本降至十分之一](../../updates/2026-10-29/#openai-gpt-6-1-terra-astra) · 2026-10-29
4. **工具感知调度**：智能体服务不能只按解码负载调度；联合考虑工具就绪、缓存收益和词元占用，才能降低端到端延迟。
   - [TAO：面向 LLM 智能体服务的工具感知联合调度](../../updates/2026-10-30/#tao-llm) · 2026-10-30
5. **持续状态建模**：长期或主动助手需持续维护用户意图、关系与情境状态，并随交互更新；单轮提示难以处理目标演变。
   - [Needwise：免生成需求级决策](../../updates/2026-11-25/#needwise) · 2026-11-25
   - [从自主智能体到认知共生体：迈向 AI 增强人类智能](../../updates/2026-11-06/#item-147) · 2026-11-06
   - [Pandora：模拟心理治疗来访者的个性化表达](../../updates/2026-11-05/#pandora) · 2026-11-05
   - [StreamVibe：面向意图演变的主动式视频智能体](../../updates/2026-10-29/#streamvibe) · 2026-10-29
6. **反馈闭环归因**：反馈进入改进前应先做因果归因、量规化或可执行验证；改进策略还需随剩余错误与回归风险更新，避免反复放大同类偏差。
   - [Fin-RSI：统一金融技能与自改进](../../updates/2026-11-25/#fin-rsi) · 2026-11-25
   - [Semantic PID-RSI：语义PID控制自改进](../../updates/2026-11-24/#semantic-pid-rsi-pid) · 2026-11-24
   - [教育AI提示精炼：情感认知双反馈](../../updates/2026-11-24/#item-47) · 2026-11-24
   - [FinEvo：同模自博弈递归改进](../../updates/2026-11-24/#finevo) · 2026-11-24
   - [MedicalRSI：临床模型与脚手架协同演化](../../updates/2026-11-23/#medicalrsi) · 2026-11-23
   - [PlayCraft：基于游玩经验的游戏迭代](../../updates/2026-11-20/#playcraft) · 2026-11-20
   - [MatOS：证据驱动的科研资产进化](../../updates/2026-11-18/#matos) · 2026-11-18
   - [EmoReward：情感视频生成的自进化奖励校准](../../updates/2026-11-06/#emoreward) · 2026-11-06
   - [LegalEvolver：量规引导自进化的法律判决预测智能体](../../updates/2026-11-05/#legalevolver) · 2026-11-05
   - [NorthCUA：以规模化经验加速计算机操作智能体](../../updates/2026-11-04/#northcua) · 2026-11-04
   - [SPAR：多轮 B2B 销售智能体的经验驱动策略演化](../../updates/2026-11-03/#spar-b2b) · 2026-11-03
   - [百度搜索通过在线反馈闭环实现递归自我进化](../../updates/2026-11-01/#item-1) · 2026-11-01
7. **主动观察**：长视频任务应先规划观察位置并补取关键证据，再生成或行动；均匀处理全部输入常浪费算力并遗漏重点。
   - [Reviso：面向视频字幕生成的优先级引导主动观察](../../updates/2026-11-04/#reviso) · 2026-11-04
8. **可审计任务闭环**：高风险与工程智能体应把确定性计算同语义判断解耦，以可执行约束限定搜索，并内置溯源、动态验证、可证伪实验和权限控制。
   - [lumimax：深度证据链知识网络](../../updates/2026-11-25/#lumimax) · 2026-11-25
   - [GPT-6：通用推理设计蛋白质](../../updates/2026-11-25/#gpt-6) · 2026-11-25
   - [MiniMax密码分析：纸面攻击实战化](../../updates/2026-11-23/#minimax) · 2026-11-23
   - [JevRisk：代码指标驱动的零样本风控](../../updates/2026-11-23/#jevrisk) · 2026-11-23
   - [Grok Bot：约束验证驱动开发](../../updates/2026-11-23/#grok-bot) · 2026-11-23
   - [EDAGoat：EDA约束验证式GPU优化](../../updates/2026-11-23/#edagoat-eda-gpu) · 2026-11-23
   - [芯片PPA优化：模型挖掘成熟设计余量](../../updates/2026-11-19/#ppa) · 2026-11-19
   - [Optics as Code：测量驱动光学训练](../../updates/2026-11-19/#optics-as-code) · 2026-11-19
   - [MLE Agents：自主推荐模型工程](../../updates/2026-11-19/#mle-agents) · 2026-11-19
   - [DiscoveryAgent：科学家主导的可审计研究](../../updates/2026-11-18/#discoveryagent) · 2026-11-18
   - [S1Mal：原子问答与嵌入集成](../../updates/2026-11-17/#s1mal) · 2026-11-17
   - [Agent-written Heuristics：编码智能体生成调度启发式](../../updates/2026-11-16/#agent-written-heuristics) · 2026-11-16
   - [百度智能云伐谋 3.0 将 RSI 自进化闭环带入产业一线](../../updates/2026-11-14/#3-0-rsi) · 2026-11-14
   - [SLIC：强化微调小语言模型实现多轮模拟电路优化](../../updates/2026-11-12/#slic) · 2026-11-12
   - [PCBRouteAgent：多模态智能体自动完成 PCB 布线](../../updates/2026-11-12/#pcbrouteagent-pcb) · 2026-11-12
   - [MRFoundry：知识引导的端到端 MRI 科研智能体循环](../../updates/2026-11-12/#mrfoundry-mri) · 2026-11-12
   - [FinEvolveKG：面向金融知识图谱的可控可归因提示演化](../../updates/2026-11-12/#finevolvekg) · 2026-11-12
   - [PharmAgents2：自主端到端药物发现系统](../../updates/2026-11-08/#pharmagents2) · 2026-11-08
   - [OpenAI 发布 GPT-6 Cyber 网络安全模型](../../updates/2026-11-06/#openai-gpt-6-cyber) · 2026-11-06
   - [El Agente Fármaco：可扩展药物发现科研智能体](../../updates/2026-11-06/#el-agente-f-rmaco) · 2026-11-06
   - [OpenAI 用 Cyber 模型自动挖掘并修补 948 个 Linux 内核提权漏洞](../../updates/2026-11-05/#openai-cyber-948-linux) · 2026-11-05
   - [EpiCoach：面向个体生理建模的智能体贝叶斯实验设计](../../updates/2026-10-30/#epicoach) · 2026-10-30
9. **人机信任校准**：部署不能只看AI使用率或自动化占比；还应评估证据互补、客观认知负荷、信任校准与用户能力保留，并让领域使用者保有设计和接管权。
   - [教师主导的课堂AI定制](../../updates/2026-11-17/#item-67) · 2026-11-17
   - [结果重于学习？学生使用 AI 编程助手编写单元测试的证据](../../updates/2026-11-13/#item-40) · 2026-11-13
   - [AI 辅助代码理解中的认知负荷：感觉更轻松，实际更费力](../../updates/2026-11-12/#item-113) · 2026-11-12
   - [相关性忽视与信任下的 AI 辅助分类](../../updates/2026-11-06/#item-40) · 2026-11-06
   - [Proton 强推 AI 编程引发内部转型冲突](../../updates/2026-10-30/#proton-ai) · 2026-10-30
   - [生成悖论：以 Anti-Prompt 保留人类能力](../../updates/2026-10-30/#anti-prompt) · 2026-10-30
10. **实时防泄漏评测**：开放式动态任务应预先固定成功标准，在决策时点实时核验外部证据，并将证据真实性与交付物可用性分开评分。
    - [EverydayBench：活网交付质量评测](../../updates/2026-11-20/#everydaybench) · 2026-11-20
    - [FINCOSMOS：金融智能体的开放世界评测范式](../../updates/2026-11-08/#fincosmos) · 2026-11-08
    - [EnergyBench：欧洲电力市场日前预测实时评测基准](../../updates/2026-11-08/#energybench) · 2026-11-08
11. **异构角色协作**：角色的工具、知识源或时间尺度不同时，可用专业智能体并行协作，并以共享状态汇合结果。
    - [PharmAgents2：自主端到端药物发现系统](../../updates/2026-11-08/#pharmagents2) · 2026-11-08
    - [StreamDuo：面向未知游戏的实时解说与研究智能体](../../updates/2026-11-06/#streamduo) · 2026-11-06
    - [VibeGame：AI 原生引擎与自进化智能体团队实现提示词生成游戏](../../updates/2026-10-31/#vibegame-ai) · 2026-10-31
12. **多轮保真约束**：多轮编辑和个性化改写要设置内容锚点、保真约束与末端校正，否则身份或意图漂移会逐轮累积。
    - [Coda-DaVinci：任务自适应三维代理导视](../../updates/2026-11-21/#coda-davinci) · 2026-11-21
    - [Code World Model 2.0：渐进强制流式视频](../../updates/2026-11-20/#code-world-model-2-0) · 2026-11-20
    - [TailSteer：抗漂移多轮图像编辑的轨迹尾部引导](../../updates/2026-11-08/#tailsteer) · 2026-11-08
    - [WeFair：基于反馈保真度的短视频个性化查询改写](../../updates/2026-11-03/#wefair) · 2026-11-03
    - [WorldCast：大角度相机控制下的世界一致角色视频生成](../../updates/2026-10-29/#worldcast) · 2026-10-29
13. **仿真到实机闭环**：具身系统应把场景重建、仿真数据、统一评测和实机验证连成闭环，单纯仿真高分不足以证明可部署。
    - [Embo-Harness：原生能力优先的机器人策略框架](../../updates/2026-11-25/#embo-harness) · 2026-11-25
    - [Data to Valves：端侧自学习暖通控制](../../updates/2026-11-19/#data-to-valves) · 2026-11-19
    - [EmbedGym：虚拟硬件闭环调试](../../updates/2026-11-18/#embedgym) · 2026-11-18
    - [uni-robot-agent：面向开源机器人智能体的统一 Harness](../../updates/2026-11-04/#uni-robot-agent-harness) · 2026-11-04
    - [优必选发布Thinker-Sim具身智能仿真平台](../../updates/2026-11-03/#thinker-sim) · 2026-11-03
14. **可信事务托管**：个人智能体需打通私有上下文、跨应用连接与细粒度授权；长程事务宜由定时或变化事件按需唤醒，并以托管完成率、留存和接管率评估。
    - [Grok Bot：定时联网自动找折扣](../../updates/2026-11-24/#grok-bot) · 2026-11-24
    - [Monitor API：变化触发式网页监控](../../updates/2026-11-23/#monitor-api) · 2026-11-23
    - [dots：云电脑后台执行](../../updates/2026-11-20/#dots) · 2026-11-20
    - [Gemini 任务：跨应用任务执行](../../updates/2026-11-18/#gemini) · 2026-11-18
    - [Personal Agent 的北极星指标：从活跃度转向事务托管](../../updates/2026-11-13/#personal-agent) · 2026-11-13
15. **基准产出分离**：高基准分不能替代真实流程产出；上线前还应测试状态、动作与目标变化下的长程完成、可监控性和实际结果。
    - [AgriManager：农业策略模式迁移评测](../../updates/2026-11-24/#agrimanager) · 2026-11-24
    - [Grok Bot：约束验证驱动开发](../../updates/2026-11-23/#grok-bot) · 2026-11-23
    - [编程基准高分不等于实际产出](../../updates/2026-11-19/#item-49) · 2026-11-19
    - [GPT-6.2 Astra：基准满分却实务失灵](../../updates/2026-11-18/#gpt-6-2-astra) · 2026-11-18
<!-- experience-seen: 2026-10-29/deepseek-harness-ai 2026-10-29/jevrec 2026-10-29/langchain-content-studio-harness 2026-10-29/microsoft-foundry-copilot-harness 2026-10-29/openai-gpt-6-1-terra-astra 2026-10-29/streamvibe 2026-10-29/worldcast 2026-10-30/anti-prompt 2026-10-30/epicoach 2026-10-30/proton-ai 2026-10-30/tao-llm 2026-10-30/taskframe 2026-10-31/vibegame-ai 2026-11-01/item-1 2026-11-03/epi2diff-llm 2026-11-03/spar-b2b 2026-11-03/system-1 2026-11-03/thinker-sim 2026-11-03/wefair 2026-11-03/wizard 2026-11-04/item-8 2026-11-04/northcua 2026-11-04/photoguider-360 2026-11-04/reviso 2026-11-04/uni-robot-agent-harness 2026-11-05/legalevolver 2026-11-05/openai-cyber-948-linux 2026-11-05/pandora 2026-11-06/decision-models 2026-11-06/el-agente-f-rmaco 2026-11-06/emoreward 2026-11-06/item-102 2026-11-06/item-147 2026-11-06/item-40 2026-11-06/openai-gpt-6-cyber 2026-11-06/streamduo 2026-11-08/edgar 2026-11-08/energybench 2026-11-08/fincosmos 2026-11-08/pharmagents2 2026-11-08/tailsteer 2026-11-12/finevolvekg 2026-11-12/item-113 2026-11-12/mrfoundry-mri 2026-11-12/pcbrouteagent-pcb 2026-11-12/slic 2026-11-12/trialjev 2026-11-12/video-coder 2026-11-13/google-deepmind-gemini-4-hydrogen 2026-11-13/item-40 2026-11-13/personal-agent 2026-11-14/3-0-rsi 2026-11-14/deepseek-api-chat-demo 2026-11-14/gpu 2026-11-15/deepseek-harness 2026-11-16/agent-written-heuristics 2026-11-17/item-67 2026-11-17/item-86 2026-11-17/s1mal 2026-11-18/allocflow 2026-11-18/claude-mythos-amd 2026-11-18/code-mode 2026-11-18/cubesandbox 2026-11-18/discoveryagent 2026-11-18/embedgym 2026-11-18/gemini 2026-11-18/gpt-6-2-astra 2026-11-18/matos 2026-11-19/data-to-valves 2026-11-19/item-49 2026-11-19/item-53 2026-11-19/item-54 2026-11-19/mle-agents 2026-11-19/optics-as-code 2026-11-19/ppa 2026-11-19/system-1 2026-11-20/code-world-model-2-0 2026-11-20/dots 2026-11-20/everydaybench 2026-11-20/performance-factory-codex 2026-11-20/playcraft 2026-11-20/prola 2026-11-21/coda-davinci 2026-11-23/edagoat-eda-gpu 2026-11-23/grok-bot 2026-11-23/jevrisk 2026-11-23/medicalrsi 2026-11-23/minimax 2026-11-23/monitor-api 2026-11-24/agrimanager 2026-11-24/autopilot 2026-11-24/finevo 2026-11-24/grok-bot 2026-11-24/item-4 2026-11-24/item-47 2026-11-24/semantic-pid-rsi-pid 2026-11-25/3agamefactory-motion 2026-11-25/embo-harness 2026-11-25/fin-rsi 2026-11-25/gpt-6 2026-11-25/lumimax 2026-11-25/needwise 2026-11-25/voyag 2026-11-25/wemm-ecom -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [AutoGen](https://github.com/microsoft/autogen) — 微软多智能体对话编排框架
- [LangGraph](https://github.com/langchain-ai/langgraph) — 以图结构编排有状态智能体工作流
- [CrewAI](https://github.com/crewAIInc/crewAI) — 角色分工式的多智能体协作框架
- [Dify](https://github.com/langgenius/dify) — 低代码 LLM 应用与工作流平台
- [n8n](https://github.com/n8n-io/n8n) — 开源自动化平台，常作为 LLM 接入业务流程的编排层
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — 开源软件工程智能体，含代码执行沙箱与交互界面
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) — 用 SOP 与角色分工编排软件公司式多智能体流程
- [browser-use](https://github.com/browser-use/browser-use) — 让 LLM 直接驱动浏览器的操作层
- [Ollama](https://github.com/ollama/ollama) — 本地模型运行与私有化部署的事实入口
- [Open WebUI](https://github.com/open-webui/open-webui) — 自托管对话前端，私有化部署的常用外壳

**论文**
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — 多智能体可编程对话框架
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — 以真实仓库 issue 定义软件工程智能体任务
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 可复现的真实网站环境与任务集
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 真实操作系统的开放式任务评测
- [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — 面向通用助手的概念简单、执行困难任务集
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) — 端到端自动化科研流程的应用原型
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 技能库沉淀驱动的开放式具身应用
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 长期运行的多智能体社会模拟应用
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) — 早期对通用能力边界的系统性探测
