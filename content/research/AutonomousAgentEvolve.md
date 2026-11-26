+++
title = 'AutonomousAgentEvolve'
proposer = '杜晋华'
since = '2026-11-17'
date = 2026-11-17T00:00:00+08:00
draft = false
toc = true
+++

# AutonomousAgentEvolve

> 研究方向：**自主 Agent 自进化**——让 Agent 从"用户发一句、它答一句"的被动会话，走向跨会话持续运行、自主决定何时醒来与何时汇报的常驻（always-on）形态，并在无人监督的长程运行中依靠持久记忆、自设定时器与权限边界持续积累经验、自我改进。

## 研究范畴

自主 Agent 自进化（autonomous / always-on agent self-evolution）关注的不是单次任务里的推理链，而是 Agent 在"睡眠—唤醒—工作—沉淀"的无限循环中如何保持连续性并越跑越好。Anthropic 在《Building always-on agents》中给出了一个可工程化的参照框架：所谓"常驻"只是用户体验，Agent 实际上大部分时间在休眠，每次被事件唤醒执行一段 **run**，run 运行在承载消息与工具调用记录的 **session** 中；包裹核心 Agent 循环的外部架构由五个原语组成——**事件收件箱**（webhook、定时任务、后台作业统一写入持久事件表，单 worker 消费、去重、批处理，防止并发 run 与事件丢失）、**定时器**（Agent 给自己设的 follow-up 与周期性 schedule，由调度器轮询后投递回收件箱）、**记忆**（用户指令、用户画像、已发消息、任务进度分文件持久存储，只加载索引，并可通过 "dreaming" 回顾历史会话整理记忆）、**权限**（凭据代理注入、auto mode 分类器拦截高风险动作、deferred tool call 挂起等待用户批准）与**发件箱**（分离的出站消息表与 dispatcher，控制汇报节奏，"先安静、再逐步赢得用户注意力"）。本方向把这一架构视为自进化的载体：记忆与 dreaming 构成跨 run 的经验积累通道，定时器让 Agent 自主规划后续行动，权限与发件箱则是自主性的安全与人机交互边界。与 [AgentEvolve]({{< relref "/research/AgentEvolve" >}}) 关注单个 Agent 的推理时反思与技能积累、[HarnessEvolve]({{< relref "/research/HarnessEvolve" >}}) 关注脚手架本身的演化、[MemoryEvolve]({{< relref "/research/MemoryEvolve" >}}) 关注记忆机制不同，AutonomousAgentEvolve 关心的是"长期无人值守运行"这一系统形态下的整体闭环：事件驱动的唤醒、跨 session 的状态延续、主动性与打扰之间的平衡，以及以"每个已解决任务的成本"而非单 token 价格衡量的长程经济性——Anthropic 的成本文档显示，在 SWE-bench Pro 子集上从 Opus 5 升级到 Opus 5.5，解题率基本持平（91.9% → 92.8%），每个已解决任务的成本下降 78%（按 Opus 5 价格折算约 69%），而典型负载下的降幅为 40%，长程任务正是模型进步最受益的场景。

## 研究挑战

- 跨 run 连续性：会话被压缩或重开都会丢失细节，哪些信息必须写入记忆、哪些只存指针（"只记无法再查到的东西"）仍缺乏系统性方法。
- 记忆的整理与进化：dreaming 式离线回顾如何识别过时条目、提炼只在多次运行中才显现的模式，又不把错误经验固化。
- 主动性与打扰的平衡：发多了是噪声、发少了漏掉关键信息，需要专门 eval 来校准汇报频率与时机。
- 无人值守下的权限与安全：run 持有用户访问权限且默认无人监督，凭据隔离、高风险动作分类拦截、何时必须挂起等待人类批准都是开放问题；事件内容中的提示注入需在 run 内深度校验。
- 并发与可靠性：多事件同时到达、worker 中途崩溃、run 中途插入新事件（推迟 / 合并 / 中断重启）等分布式系统问题与 Agent 语义交织。
- 长程经济性评测：上下文开销在每个 run 中重复支付，需要以每个已完成任务的成本、尾部最难任务的成本来评估，而非每 token 价格。
- 自主改进的可追溯性：Agent 自设定时器、自写记忆、自调整行为，如何让每一次能力或行为变化可审计、可回滚。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，长期自主运行是自进化机制落地的关键形态。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录自主 Agent 与长程自改进相关工作。

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
1. **闭环而非驻留**：常驻能力应由感知、记忆与行动的跨请求闭环定义，并用用户边界约束其持续演化，而非让模型进程始终在线。
   - [持续在线个人智能：三模块持续闭环](../../updates/2026-11-17/#item-1) · 2026-11-17
2. **事件驱动休眠**：长程 Agent 应默认休眠，由定时器或外部变化按需唤醒；持久状态与可靠事件处理比持续推理更省成本。
   - [Grok Bot：定时联网自动找折扣](../../updates/2026-11-24/#grok-bot) · 2026-11-24
   - [Monitor API：变化触发式网页监控](../../updates/2026-11-23/#monitor-api) · 2026-11-23
   - [Always-on Agent：事件驱动休眠架构](../../updates/2026-11-17/#always-on-agent) · 2026-11-17
3. **关系层可迁移**：长期个性与用户关系应独立于具体模型，沉淀为用户掌控、可审计和可迁移的状态，避免换模型即失忆。
   - [认知共生体：关系可迁移的终身增强](../../updates/2026-11-19/#item-1) · 2026-11-19
4. **沙箱内自建学习环**：强 Agent 可从宽泛目标、基础工具和经验记录中自建学习循环；迁移到现实任务前应在有边界环境验证与回滚。
   - [自主自学习：智能体自建改进算法](../../updates/2026-11-19/#item-48) · 2026-11-19
5. **执行环境与授权分离**：异步跨应用任务需要持续可用的独立执行环境，并将连接、数据和操作权限细分授权，避免后台能力等同全权访问。
   - [dots：云电脑后台执行](../../updates/2026-11-20/#dots) · 2026-11-20
6. **上下文资源化**：并发常驻任务应隔离、调度并验证合并上下文，而非依赖追加路由层；这能减少任务串扰与排队阻塞。
   - [ClonAct：无路由上下文虚拟化](../../updates/2026-11-20/#clonact) · 2026-11-20
7. **副作用状态化约束**：安全策略应观测实际系统副作用并跨动作保留状态，而非只检查表面命令，才能约束多步信息传播与攻击。
   - [Tether：可验证有状态策略执行](../../updates/2026-11-21/#tether) · 2026-11-21
8. **证据链贯通记忆**：工具动作、事后叙述和长期记忆应绑定同一可验证收据；未获证据的信息不得作为已执行事实写入记忆。
   - [Epistemic Guard：收据绑定运行时验证](../../updates/2026-11-23/#epistemic-guard) · 2026-11-23
9. **持久化可执行状态**：长程运行应保存结构化任务状态与环境事实，而非持续追加完整对话；决策进度和代码事实宜分通道维护。
   - [SKILL.state：结构化状态转移](../../updates/2026-11-24/#skill-state) · 2026-11-24
   - [HoH：双状态长程编码代理](../../updates/2026-11-24/#hoh) · 2026-11-24
10. **演员级故障隔离**：边缘常驻 Agent 应将状态与执行单元解耦，通过演员级重启、迁移和修复延续任务，避免整套系统重启。
    - [Wactorz：自编写边缘智能体运行时](../../updates/2026-11-25/#wactorz) · 2026-11-25
11. **任务状态即协作接口**：后台 Agent 应提供可快速恢复的任务表征，让用户间歇检查、调整和接管，而非要求持续监督执行过程。
    - [Calm Agent：间歇注意式交互](../../updates/2026-11-25/#calm-agent) · 2026-11-25
<!-- experience-seen: 2026-11-19/item-1 2026-11-19/item-48 2026-11-20/clonact 2026-11-20/dots 2026-11-21/tether 2026-11-23/epistemic-guard 2026-11-23/monitor-api 2026-11-24/grok-bot 2026-11-24/hoh 2026-11-24/skill-state 2026-11-25/calm-agent 2026-11-25/wactorz -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架 / 文档**
- [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents) — Anthropic Claude Platform 指南（William Hu，2026-11-13）：常驻 Agent 的五原语架构——事件收件箱、定时器、记忆、权限、发件箱，以及 run / session 循环
- [Optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence) — Anthropic 成本优化文档：按"每个已解决任务成本"比较模型；SWE-bench Pro 子集上 Opus 5.5 默认 effort 解题率 92.8%、每个已解决任务 0.22 美元，较 Opus 5 降 78%
- [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — Messages API 记忆工具，以文件目录形式实现跨会话记忆
- [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) — 长会话上下文压缩
- [Claude Code hooks: defer a tool call](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later) — 挂起工具调用等待用户输入，常驻 Agent 审批流的基础模式
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) — 基于 Claude Code 内核构建自主 Agent 的 SDK
- [Letta (MemGPT)](https://github.com/letta-ai/letta) — 有状态 Agent 框架，分层记忆管理
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — 开源自主软件工程 Agent 平台
- [Temporal](https://github.com/temporalio/temporal) — 持久化执行引擎，可作为常驻 Agent 的调度器与可靠执行底座

**论文**
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 借鉴操作系统虚拟内存的分层记忆，支撑跨会话长期运行
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 记忆流 + 反思 + 规划的长期自主 Agent 架构
- [Sleep-time Compute: Beyond Inference Scaling at Test-time](https://arxiv.org/abs/2504.13171) — 在空闲时间离线预处理上下文，与 dreaming 式记忆整理思路相近
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 把失败反思写回记忆，跨尝试自我改进
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 自动课程 + 技能库的终身学习 Agent
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) — Agent 改写自身代码的开放式自进化
- [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) — METR 以任务时长度量 Agent 自主能力的增长趋势

**综述 / 报道**
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic 关于 Agent 核心循环与工作流模式的经典文章，常驻 Agent 在其之上叠加外部架构
- [刚刚，Anthropic公开Opus 5.5同款自主Agent架构：算力成本狂降78%](https://mp.weixin.qq.com/s/X0-a-e99nb8NM1tRoN9TaQ) — 对《Building always-on agents》的中文解读。需注意标题中的"78%"源自 Anthropic 成本文档，指 SWE-bench Pro 子集上 Opus 5 → Opus 5.5 每个已解决任务的成本降幅（解题率 91.9% → 92.8%，按 Opus 5 价格折算约 69%），并非算力成本；典型负载降幅为 40%。所谓"架构"是面向开发者的常驻 Agent 系统设计指南，而非模型内部架构
