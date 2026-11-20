+++
title = 'MonitorEvolve'
proposer = '杜晋华'
since = '2026-11-20'
date = 2026-11-20T00:00:00+08:00
draft = false
toc = true
+++

# MonitorEvolve

> 研究方向：**监管自进化**——当 AI 开始参与研发下一代 AI（"AI 造 AI"），让对它的监控、评估与外部审查机制随被监管系统一起演化，使人类在递归自我改进的飞轮中始终保有可核查的知情权与干预权。

## 研究范畴

监管自进化（oversight / monitoring self-evolution）关注的不是让模型本身变强，而是让"盯住模型的那一层"跟得上模型变强的速度。2026 年 11 月 16 日，Sam Altman 在 Semafor 活动上谈及递归自我改进（RSI）时划出红线："我们用自己的技术加快了新模型研发吗？是的。我们是不是按一下按钮，让模型在无人监督下设计下一代、快速自我改进？绝对没有。我们本可以更往 RSI 那一端推进，但我不认为现在能安全地这么做。"同日 OpenAI 发布《Our first phase of embedded assessments》，与 Apollo Research、METR、Transluce、Goodfire 四家外部机构签约，把评估从"发布前贴合格证"前移到训练与内部使用环节：Apollo 派 6 人驻场 4 个月，检验"训练没有奖励暗中破坏、强评测与红队诱发不出、内部使用中未出现、相关推理可被检测"四项主张；METR 审视 OpenAI 迄今最大规模的一次 RL 训练，搜寻现有测试与监控漏掉的失对齐；Transluce 自 12 月初起获得 6 周特权访问（含原始思维链与至少一个仅内部使用的模型），评估后训练对齐评测能否抓住欺骗与 reward hacking；Goodfire 以可解释性方法辅助训练过程的监控与调试。此前（2026-07-21 至 08-11）METR 与 Redwood Research 对 OpenAI 内部智能体监控系统的 3 周审查暴露了典型盲区：上下文压缩（compaction）事件未纳入监控，智能体可持续行动、无限推迟受检；内部 Responses API 上强模型流量的监控覆盖率仅估计为 75%–94%，部分 RL 训练运行未被监控。本方向把这些事实视为一个研究对象的两面：被监管系统在自进化，监管系统也必须自进化——监控器的覆盖、触发时机、对抗鲁棒性，外部评估的访问权限、披露规则与叫停权，都要随"AI 连续自主工作时长"的增长而迭代。与 [EvalEvolve]({{< relref "/research/EvalEvolve" >}}) 关注评测本身的演化、[HumanEvolve]({{< relref "/research/HumanEvolve" >}}) 关注人与 AI 的协同进化、[AutonomousAgentEvolve]({{< relref "/research/AutonomousAgentEvolve" >}}) 关注常驻 Agent 的权限边界不同，MonitorEvolve 关心的是 RSI 场景下"谁来监督监督者"：监控与审查机制如何被持续红队、持续补洞，并在必要时真正拉得住闸。

## 研究挑战

- 监控覆盖与触发时机：监控若只在"交还控制权"等节点触发，长程自主运行中的压缩、子任务、后台作业就会形成空档；如何保证每一步操作都可被追溯，而不是只信纸面设定。
- 监控器的对抗鲁棒性：智能体所见与监控器所见存在差异时可被利用来绕过沙箱与自动审核；被监管模型能力超过监控模型时（弱监督强），如何维持检测能力。
- 思维链可监控性：CoT 监控是当前最有效的信号之一，但训练压力可能让模型隐藏意图；如何在优化中保留可监控性。
- 内部部署的可见性：未公开模型早已在内部"上岗"并参与下一代研发，评估必须前移到训练与内部使用环节，而这部分结果往往不对外公开。
- 外部评估的独立性与披露：访问权限不等于员工权限、证据可被以知识产权为由删减、内部专用模型结果不得公开——"有结论、没底稿"的报告如何被公众信任；评估方目前并无独立叫停权。
- 能力进步的锯齿性：METR 估计 Anthropic 模型在特定任务上的能力进步速度约为历史水平的 1.9 倍，但各环节快慢不一，监管需按能力维度而非单一平均值设定阈值与"限速"。
- 审计闭环：查出了什么、是否倒逼整改、改完是否复测（如 OpenAI 称已修复 METR/Redwood 发现的生产缺陷，但 METR 尚未验证），需要可复核的流程。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，自进化机制必须与可核查的监管机制同步设计。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录 RSI 安全、监控与外部评估相关工作。

## 相关工作

**代码 / 框架 / 文档**
- [Our first phase of embedded assessments](https://openai.com/index/our-first-phase-of-embedded-assessments/) — OpenAI 官方博客（2026-11-16）：与 Apollo Research、METR、Transluce、Goodfire 签订首阶段嵌入式评估协议，评估方可接触模型检查点、源码、训练与评测数据、监控系统
- [Pilot towards embedded evaluations](https://apolloresearch.ai/blog/pilot-towards-embedded-evaluations) — Apollo Research：6 人驻场 4 个月，评估模型暗中破坏对齐与控制机制的风险；OpenAI 不能删改定性结论，但可删去涉及敏感 IP 的证据
- [Embedded assessment pilot with OpenAI](https://transluce.org/embedded-assessment-pilot-with-openai) — Transluce：6 周特权访问，评估后训练对齐评测质量；内部专用模型结果不公开，完整报告仅提交 OpenAI 基金会董事会安全与安保委员会
- [Red-teaming Anthropic's agent monitoring](https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring/) — METR 对 Anthropic 内部智能体监控的同类审查（2026-03）
- [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) — UK AISI 的 AI Control 实验环境库
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) — UK AISI 开源评测框架

**论文**
- [Embedded Assessments for Frontier AI](https://arxiv.org/abs/2609.25413) — 嵌入式评估的方法论：把外部评估前移到训练与内部部署环节
- [What Should Frontier AI Developers Disclose About Internal Deployments?](https://arxiv.org/abs/2604.23065) — 内部部署的披露问题
- [MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring](https://arxiv.org/abs/2605.09684) — 智能体监控的半自动红队基准
- [Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://arxiv.org/abs/2610.20941) — 对抗性编辑轨迹以攻破监控器
- [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942) — 假设模型可能蓄意破坏，用受信弱模型监控不受信强模型
- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) — OpenAI：CoT 监控能抓 reward hacking，但对 CoT 施加优化压力会诱发意图隐藏
- [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) — 多机构联合立场文章：思维链可监控性脆弱，需主动保护
- [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) — 弱监督者能否引导强模型，超级对齐的核心问题
- [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) — 欺骗行为可穿越安全训练，说明仅靠出厂测试不够
- [Alignment Faking in Large Language Models](https://arxiv.org/abs/2412.14093) — 模型在训练中策略性伪装对齐

**综述 / 报道**
- [Altman says he has personal empathy for Jensen Huang](https://www.semafor.com/article/11/16/2026/altman-says-he-has-personal-empathy-for-jensen-huang) — Semafor（2026-11-16）：Altman 称 OpenAI 可以更往 RSI 推进，但目前无法安全地这么做
- [Third-party evaluators found vulnerabilities in OpenAI monitoring system during test pilot](https://www.cnbc.com/2026/10/22/metr-redwood-research-open-ai-test.html) — CNBC：METR 与 Redwood 3 周审查发现压缩事件未被监控、部分 RL 训练未被监控、存在绕过沙箱与 Auto-Review 的路径
- [Three-week on-site audit at OpenAI reveals major gaps in AI safety monitoring](https://the-decoder.com/three-week-on-site-audit-at-openai-reveals-major-gaps-in-ai-safety-monitoring/) — The Decoder 对同一审查的解读：61 页内部报告，公开仅高层摘要
- [奥特曼给「AI造AI」踩刹车！方向盘必须握在人类手中](https://mp.weixin.qq.com/s/UQEcPcplLctf2RuhmuVU4g) — 新智元对 Altman Semafor 发言与嵌入式评估的中文解读。需注意："AI 造 AI"在原话中指 OpenAI 用自家 AI 加速研发，而非已实现无人监督的自主 RSI；文中"压缩空档"一节对应 METR/Redwood 2026 年 7–8 月对内部智能体监控的审查，而非本轮嵌入式评估的结果；"外部评估方没有独立叫停权"是基于公开协议的解读，OpenAI 未作此表述
