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

## 相关工作

> 公开检索（GitHub / arXiv）暂未找到以 "Groom" 为名的同类公开项目或论文。相关公开工作可参考 [[HarnessEvolve]]（评测 harness 演进）与 [[EvalEvolve]]（进化式评测）方向下的资源。
