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
