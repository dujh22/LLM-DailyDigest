+++
title = 'Groom'
proposer = '杜晋华'
since = '2026-05-28'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# Groom

> 研究方向：**面向 Agent Harness 的过程级 token 利用评测**——把自主智能体的评测从"做对没 / 花了多少"重述为"token 是否被有效利用"，以证据驱动的方式对异构 Agent / Harness 做过程级 token 归因与横向比较。

## 研究范畴

随着大模型驱动的自主智能体从单轮问答走向长程任务执行，其表现由多轮规划、工具调用、环境反馈、错误恢复与最终交付共同决定。但现有评测仍主要看**最终是否做对**，存在两个盲区：**过程不可观测**（无法判断成功来自可靠推理还是偶然试错 / 冗余搜索）与**成本不可归因**（即便完成也难定位 token 究竟消耗在规划、检索、工具反馈、错误恢复还是重复确认）。本方向以证据驱动（不信自我声明、要求执行轨迹中的可审计证据）对异构 Agent / Harness（如 Claude Code / Codex / OpenClaw）做过程级 token 利用归因与比较。社区关注的核心问题包括：成功是否来自可靠推理、token 成本在多阶段中的占比、以及 harness 选择如何系统性影响 token 成本结构。

## 研究挑战

- 异构系统的过程观测统一（原生日志不足时需旁路补齐）。
- token 成本多阶段分解的可靠性与跨系统一致性。
- "是否真正支撑决策"的可验证判据（区分注入 / 读取 / 有效）。
- 抗自我声明、可复现、跨系统可比的评测协议设计。

## 自研项目

- [Groom](https://github.com/dujh22/Groom) — 面向 Agent Harness 的过程级 token 利用评测框架：`native + sidecar` 统一过程观测、token 8 阶段成本分解、`Injected / Referenced / Effective` 三态证据判据；V0 工具链仅用标准库、已跑通 golden trace 闭环。
- [H-TokenBench](https://github.com/dujh22/H-TokenBench) — "Benchmarking How LLMs Harness Tokens for Reasoning"，评测 LLM 在推理中如何利用 token 的基准。

## 自研洞察

<!-- human-only:start 自研洞察｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

1. 脚手架在建筑完工后会被拆除。随着模型改进，Harness的复杂性应该降低。Manus在六个月内重写了五次，每次重写都在去除复杂性。复杂的工具定义变成了通用的shell执行，「管理agent」变成了简单的结构化移交
2. TerminalBench的证据很清楚：只改变Harness，就能让agent的排名移动20个以上的位次。

<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->

1. Deepseek Harness 的 Trajectory 分析页面
2. 为了能与真实世界的反馈对齐，采用与 Terminal-Bench 同源的 Harbor 容器化隔离架构，将 Agent 代码沙箱与仿真/验证后端彻底隔开
3. 在 LLM API 调用层插入代理网关，在 token 级别捕获完整的执行轨迹
4. 理想的harness是完全不需要人工介入的

<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->

1. **终局成功不等于有效**：成功率会掩盖中间失效、冗余动作和偶然恢复；应联合评估终态、步骤合法性与轨迹质量，并检验过程分数相对结果、成本和行为统计的增量信息。
   - [端点条件化过程增益评估](../../updates/2026-11-25/#item-133) · 2026-11-25
   - [二维推理：语义图量化推理忠实与效率](../../updates/2026-11-24/#item-67) · 2026-11-24
   - [RagHarnessDebugger：Jev引导的修复审计](../../updates/2026-11-19/#ragharnessdebugger-jev) · 2026-11-19
   - [DetourBench：精确最短动作轨迹评测](../../updates/2026-11-18/#detourbench) · 2026-11-18
   - [Agent Trajectories：轨迹证据化质量审查](../../updates/2026-11-18/#agent-trajectories) · 2026-11-18
   - [Instrumenting Failure：逐决策节点评测](../../updates/2026-11-17/#instrumenting-failure) · 2026-11-17
   - [编码智能体行为轨迹画像](../../updates/2026-11-16/#item-35) · 2026-11-16
   - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
   - [长程 LLM 智能体的轨迹中心故障审计](../../updates/2026-11-12/#llm) · 2026-11-12
   - [CAREFUL-Bench：面向调用效果的多轮函数调用无评判器评测](../../updates/2026-11-06/#careful-bench) · 2026-11-06
   - [MemUse：在使用点评估智能体记忆](../../updates/2026-11-03/#memuse) · 2026-11-03
   - [TauIndianBankBench：银行工具智能体的流程感知评测](../../updates/2026-10-30/#tauindianbankbench) · 2026-10-30
   - [前缀可执行性：超越最终成功的工具智能体评估](../../updates/2026-10-30/#item-38) · 2026-10-30
2. **组合体是验证单元**：同一模型会因提示、工具、记忆和审查流程而改变合规、成本乃至排名；横评应锁定模型—Harness组合。
   - [SkillBuffBench：多因素技能贡献评测](../../updates/2026-11-18/#skillbuffbench) · 2026-11-18
   - [VIALS-AA评测：Claude以高频工具调用领先科研图表视觉推理](../../updates/2026-11-12/#vials-aa-claude) · 2026-11-12
   - [企业级 SOP 中智能体架构的成本—成功率权衡评测](../../updates/2026-11-12/#sop) · 2026-11-12
   - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
   - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
   - [智能体脚手架显著影响固定 LLM 的银行合规表现](../../updates/2026-11-05/#llm-2) · 2026-11-05
   - [TraceTrial-Bench：智能体运行框架可靠性与故障归因基准](../../updates/2026-10-29/#tracetrial-bench) · 2026-10-29
3. **全链路证据留痕**：过程归因应记录会话、决策、工具调用、状态与产物的可验证关联，并声明证据的资源、生命周期与授权边界；自述或单项检查不足以证明完成。
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [受治理实验全程审计](../../updates/2026-11-19/#item-36) · 2026-11-19
   - [Evidence Interpretation：检查证据边界判定](../../updates/2026-11-19/#evidence-interpretation) · 2026-11-19
   - [Agent Trajectories：轨迹证据化质量审查](../../updates/2026-11-18/#agent-trajectories) · 2026-11-18
   - [用评估侧部分可观测博弈缓解智能体欺骗](../../updates/2026-11-12/#item-221) · 2026-11-12
   - [Soei：面向多智能体软件工程的证据与意图结构化可观测性](../../updates/2026-10-30/#soei) · 2026-10-30
   - [APE：面向软件开发智能体的过程证据](../../updates/2026-10-30/#ape) · 2026-10-30
   - [TraceTrial-Bench：智能体运行框架可靠性与故障归因基准](../../updates/2026-10-29/#tracetrial-bench) · 2026-10-29
4. **归因需要反事实**：失败原因不能由事后轨迹直接判定；应在可恢复状态上干预、回放，并用环境终态与中性对照验证。
   - [预算配对反事实审计](../../updates/2026-11-21/#item-24) · 2026-11-21
   - [AgentFaultBench：状态验证式故障恢复评测](../../updates/2026-11-17/#agentfaultbench) · 2026-11-17
   - [长程智能体失败归因需执行反事实：迈向报告标准](../../updates/2026-11-06/#item-46) · 2026-11-06
   - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30
5. **前缀定位故障传播**：逐前缀定位最早关键错误，再用其局部证据诊断传播、反证忽略与恢复，比整段轨迹审读更准确且少受无关信息干扰。
   - [RecordRoute：定位引导的故障诊断](../../updates/2026-11-26/#recordroute) · 2026-11-26
   - [Instrumenting Failure：逐决策节点评测](../../updates/2026-11-17/#instrumenting-failure) · 2026-11-17
   - [长程 LLM 智能体的轨迹中心故障审计](../../updates/2026-11-12/#llm) · 2026-11-12
   - [基于闭合序列模式挖掘的网页导航智能体可解释早停](../../updates/2026-11-06/#item-153) · 2026-11-06
   - [GraphRail：搜索智能体的图结构步骤级验证](../../updates/2026-11-06/#graphrail) · 2026-11-06
   - [前缀可执行性：超越最终成功的工具智能体评估](../../updates/2026-10-30/#item-38) · 2026-10-30
6. **Token按作用计量**：总Token或调用次数不能代表利用率；应把消耗关联到改变状态、提供证据或推动下一有效动作的贡献。
   - [软件热力学：热功分解编码成本](../../updates/2026-11-19/#item-47) · 2026-11-19
   - [编码智能体行为轨迹画像](../../updates/2026-11-16/#item-35) · 2026-11-16
   - [VIALS-AA评测：Claude以高频工具调用领先科研图表视觉推理](../../updates/2026-11-12/#vials-aa-claude) · 2026-11-12
   - [AI 智能体如何浪费 Token 成本？](../../updates/2026-11-06/#ai-token) · 2026-11-06
   - [MemUse：在使用点评估智能体记忆](../../updates/2026-11-03/#memuse) · 2026-11-03
7. **反事实删减测冗余**：以剪枝或压缩后任务质量是否保持来判定Token冗余，比按文本长度或推理自述分类更可靠。
   - [CoACT：面向 Coding Agent 的动作保持式上下文压缩](../../updates/2026-11-14/#coact-coding-agent) · 2026-11-14
   - [推理历史压缩对后续生成与智能体成本的因果影响](../../updates/2026-11-06/#item-82) · 2026-11-06
   - [AI 智能体如何浪费 Token 成本？](../../updates/2026-11-06/#ai-token) · 2026-11-06
8. **历史压缩因模而异**：推理历史的保留价值依赖模型与任务；压缩应以状态、下一动作与端到端质量保持为准，并按缓存价格、重读和诱发行为核算工作流成本。
   - [Re-Reading Is Not Free：缓存感知能耗估算](../../updates/2026-11-18/#re-reading-is-not-free) · 2026-11-18
   - [Context Has a Price：缓存感知上下文成本评测](../../updates/2026-11-18/#context-has-a-price) · 2026-11-18
   - [CoACT：面向 Coding Agent 的动作保持式上下文压缩](../../updates/2026-11-14/#coact-coding-agent) · 2026-11-14
   - [Think or Remember：智能体推理中的思考与记忆成本交换率](../../updates/2026-11-12/#think-or-remember) · 2026-11-12
   - [推理历史删除敏感性是模型级属性](../../updates/2026-11-12/#item-220) · 2026-11-12
   - [推理历史压缩对后续生成与智能体成本的因果影响](../../updates/2026-11-06/#item-82) · 2026-11-06
9. **工具上下文主导成本**：大工具集与长返回可使输入成本暴涨；优先收窄工具、稀疏读取、截断结果并用代码封装调用。
   - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
   - [SparseRead：面向 AI 智能体的高效稀疏读取层](../../updates/2026-11-13/#sparseread-ai) · 2026-11-13
   - [OpenRouter 实测 MCP、CLI 与 Skills 的上下文 Token 成本](../../updates/2026-11-12/#openrouter-mcp-cli-skills-token) · 2026-11-12
10. **返回协议决定可靠性**：工具接口须显式声明交互与返回语义，否则假成功、超时和无效Token会被误算为推理失败。
    - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
    - [RECEIPT：测量并修复智能体工具调用的返回假设](../../updates/2026-11-03/#receipt) · 2026-11-03
11. **首次解题到终止**：应回放定位首次满足任务状态与实际停止；早停和续跑都须验证，因停止可能是上下文诱发的假边界，续跑也可能破坏结果。
    - [SCoRe：停机突发式上下文压缩](../../updates/2026-11-19/#score) · 2026-11-19
    - [Done, But Still Working：编程智能体早停评测](../../updates/2026-11-19/#done-but-still-working) · 2026-11-19
    - [终止滞后：编程智能体早已解题却迟迟不停](../../updates/2026-11-13/#item-32) · 2026-11-13
    - [代码生成中的推理轨迹溢出：显式推理模型实证研究](../../updates/2026-11-08/#item-48) · 2026-11-08
    - [基于闭合序列模式挖掘的网页导航智能体可解释早停](../../updates/2026-11-06/#item-153) · 2026-11-06
12. **状态回放免评判器**：可执行任务优先用轨迹回放和状态差分检测重复、破坏性或无效动作，减少生成式评判器偏差。
    - [AgentFaultBench：状态验证式故障恢复评测](../../updates/2026-11-17/#agentfaultbench) · 2026-11-17
    - [CAREFUL-Bench：面向调用效果的多轮函数调用无评判器评测](../../updates/2026-11-06/#careful-bench) · 2026-11-06
    - [TauIndianBankBench：银行工具智能体的流程感知评测](../../updates/2026-10-30/#tauindianbankbench) · 2026-10-30
13. **质量成本联合优化**：脚手架选择应比较质量—成本帕累托面及统计支持度；单一分数提升可能牺牲可靠性、迁移性或预算。
    - [JevAgentHarness：Jev嵌入式快速决策](../../updates/2026-11-25/#jevagentharness-jev) · 2026-11-25
    - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
    - [企业级 SOP 中智能体架构的成本—成功率权衡评测](../../updates/2026-11-12/#sop) · 2026-11-12
    - [面向低成本智能体脚手架的系统优化](../../updates/2026-11-12/#item-108) · 2026-11-12
    - [表面之下：智能体演化中被忽视的可靠性、成本与迁移问题](../../updates/2026-11-08/#item-41) · 2026-11-08
    - [ParetoSaddler：面向质量与成本的智能体脚手架帕累托优化](../../updates/2026-11-06/#paretosaddler) · 2026-11-06
14. **难度因素分离控制**：横评应控制依赖深度、候选规模、活跃状态与接口条件，并直接估计成对差值；单体分数准确不保证排名差距准确。
    - [网页智能体评测：证据约束式差距估计](../../updates/2026-11-25/#item-108) · 2026-11-25
    - [编码智能体行为轨迹画像](../../updates/2026-11-16/#item-35) · 2026-11-16
    - [Pdb 还是 Bash：用 Pass_X@k 比较智能体调试接口](../../updates/2026-11-12/#pdb-bash-pass-x-k) · 2026-11-12
    - [有状态工具工作流中的智能体难度审计](../../updates/2026-11-06/#item-92) · 2026-11-06
15. **验证器分布校验**：验证器可靠性随轨迹分布与证据视图变化；应报告跨视图一致性，并用覆盖目标分布的校准集估计偏差、弃答与不确定界。
    - [Transport-Safe Evaluation：轨迹感知的随时有效审计](../../updates/2026-11-25/#transport-safe-evaluation) · 2026-11-25
    - [Verification Transport：抽象边界验证迁移](../../updates/2026-11-16/#verification-transport) · 2026-11-16
    - [EnvOS：动态环境下计算机使用智能体的审计与证据评估](../../updates/2026-10-30/#envos) · 2026-10-30

<!-- experience-seen: 2026-11-19/done-but-still-working 2026-11-19/evidence-interpretation 2026-11-19/item-36 2026-11-19/item-47 2026-11-19/l2c 2026-11-19/ragharnessdebugger-jev 2026-11-19/score 2026-11-21/item-24 2026-11-24/item-67 2026-11-25/item-108 2026-11-25/item-133 2026-11-25/jevagentharness-jev 2026-11-25/transport-safe-evaluation 2026-11-26/recordroute -->

<!-- research-experience:end -->

## 相关工作

> 公开检索（GitHub / arXiv）暂未找到以 "Groom" 为名的同类公开项目或论文。相关公开工作可参考 [[HarnessEvolve]]（评测 harness 演进）与 [[EvalEvolve]]（进化式评测）方向下的资源。
