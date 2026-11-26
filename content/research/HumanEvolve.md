+++
title = 'HumanEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# HumanEvolve

> 研究方向：**AI 辅助的人类进化**——AI 作为协作者、导师与认知放大器，如何改变人的学习、技能、判断与创造方式，以及去技能化与认知负债等反向效应。

## 研究范畴

AI 辅助的人类进化（AI-augmented human evolution）关注"人这一侧"如何因 AI 而改变：AI 承担检索、写作、编码与决策支持后，人类的时间分配、技能结构与认知习惯发生怎样的迁移；哪些设计让人变强（upskilling、认知参与度提升），哪些让人变弱（deskilling、认知债务、判断外包）。本方向涵盖：AI 辅助学习与教育、AI 协作对劳动生产率与技能结构的实证影响、人机联合决策的互补性与增益条件、认知负荷与批判性思维的长期变化、AI 辅助科研与知识工作、面向"增强人"的交互界面设计，以及职业通道与人才培养体系的结构性变化。与 [[PersonalEvolve]] 的分工：PersonalEvolve 研究"AI 自己怎么变强"，本方向研究"人借助 AI 怎么变强或变弱"。

## 研究挑战

- 长期效应难以度量：短期效率提升与长期能力退化往往方向相反。
- 增益条件不明：何种任务分工、解释方式与信任校准才能产生人机互补而非依赖。
- 认知负债与去技能化：隐性知识与练习机会被 AI 挤占后的补偿机制。
- 职业通道断裂：初级岗位减少对人才培养的影响需长期追踪。
- 公平与可及性：增强效应是否只惠及已具备较高能力的人群。

## 自研项目

- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》配套仓库，本身即 AI 辅助知识传递的教学实践。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，"模型自进化 → 人机共同进化"是其中的研究延伸。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 以 AI 过滤信息、由人反馈标注的日常科研信息流，是"AI 增强研究者认知带宽"的实践样本。

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
1. **隐性建议效应**：AI建议可显著改变专家判断，而用户常低估这种影响；高风险协作应记录建议暴露，并用真实结果校准信任。
   - [Anthropic实验：AI建议显著影响专家决策与自我归因](../../updates/2026-10-29/#anthropic-ai) · 2026-10-29
2. **证据重叠约束**：选择AI决策支持不能只看单体准确率；人机依据高度重叠时互补增益有限，应按情境测量证据相关性与适当性。
   - [无真实标签条件下的人机互补性评估](../../updates/2026-11-12/#item-147) · 2026-11-12
   - [相关性忽视与信任下的 AI 辅助分类](../../updates/2026-11-06/#item-40) · 2026-11-06
3. **结果门控介入**：人类介入应按预期下游收益和跨任务校准能力分配，不能用资历、活跃度或单次自信替代。
   - [Knowing What You Know：结果门控的审查者校准](../../updates/2026-11-20/#knowing-what-you-know) · 2026-11-20
   - [CVD：面向 LLM 智能体的人类咨询价值学习](../../updates/2026-11-06/#cvd-llm) · 2026-11-06
4. **协作多维评估**：评估人机协作不能只看准确率或完成率，还应测可操控性、信任校准、安全边界、情境适当性与工作体验。
   - [人机任务分配：绩效与体验协同权衡](../../updates/2026-11-25/#item-83) · 2026-11-25
   - [RealCLI：统一评估 CLI 智能体的人机协作](../../updates/2026-10-30/#realcli-cli) · 2026-10-30
5. **主动生成脚手架**：学习和初级工作中应先让人提出假设、草案与验收标准，再由AI补充；阶段奖励和协商权可减少一次性代答造成的技能流失。
   - [ChatWise：学习者能动性协商](../../updates/2026-11-25/#chatwise) · 2026-11-25
   - [结果重于学习？学生使用 AI 编程助手编写单元测试的证据](../../updates/2026-11-13/#item-40) · 2026-11-13
   - [AI 辅助工作中的技能学习激励与人力发展](../../updates/2026-11-05/#item-37) · 2026-11-05
   - [Addy Osmani：Agent 时代如何保持批判性思维](../../updates/2026-11-04/#addy-osmani-agent) · 2026-11-04
   - [生成悖论：以 Anti-Prompt 保留人类能力](../../updates/2026-10-30/#anti-prompt) · 2026-10-30
6. **主观轻松偏差**：不能以自报轻松推断认知增益；AI可能不改善理解成绩却增加客观负荷，评估须同时测绩效、过程与负荷。
   - [AI 辅助代码理解中的认知负荷：感觉更轻松，实际更费力](../../updates/2026-11-12/#item-113) · 2026-11-12
7. **教师侧设计权**：教学AI应把任务、反馈和使用边界的配置权交给一线教师；贴近班级情境的定制比中心化通用部署更稳。
   - [教师主导的课堂AI定制](../../updates/2026-11-17/#item-67) · 2026-11-17
8. **多轮审议核查**：事实核查场景可让多个智能体展示分歧并支持多轮追问；对抗角色和强制参与则需单独权衡准确率与体验。
   - [多智能体审议对人机协同决策的影响](../../updates/2026-11-13/#item-35) · 2026-11-13
9. **纵向目标对齐**：短期满意度或偏好提升不代表能力、安全与长期福祉同步改善；持续协作系统应加入技能保持、依赖和安全的纵向指标。
   - [生成式 AI 的对齐短视问题](../../updates/2026-11-06/#item-28) · 2026-11-06
   - [RSI Arena：基于人类反馈的递归自我改进实验](../../updates/2026-10-30/#rsi-arena) · 2026-10-30
10. **实践驱动共演**：专业AI应允许用户依据真实故障持续修改工具与流程；纵向共演比一次性部署更能吸收隐性情境知识。
    - [实践生长型 AI 工具：用户与软件协同演化范式](../../updates/2026-11-08/#item-47) · 2026-11-08
11. **间歇监督接口**：后台智能体应保存可快速恢复的任务状态、决策轨迹和边界，让人按检查点介入，而非被迫持续盯守。
    - [Calm Agent：间歇注意式交互](../../updates/2026-11-25/#calm-agent) · 2026-11-25
12. **初级通道空心化**：AI编程的近期劳动冲击更可能是减少初级招聘而非立即裁员；人才体系应保留入门实践，并转向设计、验证和整合能力。
    - [AI-Assisted Programming：编程助手重塑技术招聘](../../updates/2026-11-25/#ai-assisted-programming) · 2026-11-25
    - [模型一代：AI重塑大学秩序](../../updates/2026-11-20/#item-5) · 2026-11-20
13. **科研闭环瓶颈**：评估AI科研加速不能用平均成功率外推；最弱任务环节、实验闭环、研究品味与监督决定端到端收益。
    - [研究加速报告：量化智能体研发效能](../../updates/2026-11-19/#item-15) · 2026-11-19
14. **机器证明分层验真**：超长AI证明应先审计命题语义与关键证书，再用独立内核交叉复现；形式正确不能替代编码和可解释性审查。
    - [Navier–Stokes爆破证明：Claude协作与Lean核验](../../updates/2026-11-23/#navier-stokes-claude-lean) · 2026-11-23
    - [黎曼猜想形式化证明：多内核交叉验真](../../updates/2026-11-23/#item-7) · 2026-11-23
15. **双目标任务分配**：人机分工要同时优化任务绩效与人的工作体验，显式建模对厌恶任务的规避，并随风险和决策主体调整权重。
    - [人机任务分配：绩效与体验协同权衡](../../updates/2026-11-25/#item-83) · 2026-11-25
<!-- experience-seen: 2026-10-29/anthropic-ai 2026-10-30/anti-prompt 2026-10-30/proton-ai 2026-10-30/realcli-cli 2026-10-30/rsi-arena 2026-10-31/deepmind-ai 2026-11-04/addy-osmani-agent 2026-11-05/item-37 2026-11-06/cvd-llm 2026-11-06/item-147 2026-11-06/item-28 2026-11-06/item-40 2026-11-08/item-47 2026-11-12/item-113 2026-11-12/item-147 2026-11-13/item-35 2026-11-13/item-40 2026-11-17/item-67 2026-11-19/item-15 2026-11-20/item-5 2026-11-20/knowing-what-you-know 2026-11-23/item-7 2026-11-23/navier-stokes-claude-lean 2026-11-24/superintelligence-is-arriving-ai 2026-11-25/ai-assisted-programming 2026-11-25/calm-agent 2026-11-25/chatwise 2026-11-25/item-83 -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [hh-rlhf](https://github.com/anthropics/hh-rlhf) — Anthropic 有益无害人类偏好数据集，人类判断作为训练信号的基准资源
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 人类监督失效后如何继续引导强模型的实验代码

**论文**
- [Human-AI Coevolution](https://arxiv.org/abs/2306.13723) — 人机共演化作为独立研究领域
- [Position: Towards Bidirectional Human-AI Alignment](https://arxiv.org/abs/2406.09264) — "双向对齐"：AI 对齐人类价值，同时人类认知被 AI 塑造
- [Generative AI at Work](https://arxiv.org/abs/2304.11771) — 生成式 AI 对一线工作者生产率与技能的实证研究
- [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872) — AI 辅助写作对认知参与度与脑活动的影响
- [Experimental evidence on the productivity effects of generative artificial intelligence](https://arxiv.org/abs/2302.06590) — 客服场景的随机对照实验
- [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) — 人类能力上限之外的监督问题
