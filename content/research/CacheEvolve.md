+++
title = 'CacheEvolve'
proposer = '杜晋华'
since = '2026-10-21'
date = 2026-10-21T00:00:00+08:00
draft = false
toc = true
+++

# CacheEvolve

> 研究方向：**缓存自进化**——让推理记忆从"随长度线性膨胀"转向"固定预算下自适应取舍"，并自动学习记住什么、压缩什么、丢弃什么。

## 研究范畴

缓存自进化（cache self-evolution）把推理过程中的缓存看作可被模型自己学习管理的记忆资源。传统 KV Cache 每生成一个 token 就多存一份，上下文从 4K 涨到 256K，显存跟着翻几十倍，直接决定单卡能跑多少并发、单位 token 的算力成本，以及端侧与 Agent 场景是否可用。本方向涵盖三条技术线的融合：一是给单个 token 瘦身（MLA 类潜在注意力、KIVI 类低比特量化、TurboQuant 类随机旋转量化），二是改变注意力结构本身（Mamba / RWKV / Gated DeltaNet 等循环状态模型、滑动窗口注意力、混合层架构），三是把「记住什么」变成可学习的决策（缓存淘汰策略、可学习锚点库、按重要性打分的写入与合并机制）。社区关注的核心问题包括：固定内存下如何保住远处细节、淘汰策略如何从人工启发式升级为可学习策略、缓存预算如何与推理框架的调度 / 前缀复用协同、长上下文与长程 Agent 任务上如何评测真实收益而非只看困惑度，以及缓存管理与外部记忆、参数化记忆之间的分工边界。

## 研究挑战

- 容量与保真度的根本权衡：有界状态模型内存恒定但远距离回忆坍缩，全注意力保真但成本随长度线性增长，如何在中间地带稳定取到关键细节。
- 淘汰策略的自动化：H2O / SnapKV / 滑动窗口这类静态规则难以适配多样化负载，需要把"留下哪条记录"交给可学习的评分与写入机制。
- 关键信息识别本身是困难的：分不清哪些细节后续会被用到，压缩就会变成信息删除，且错误不可逆。
- 评测失真：needle-in-a-haystack 通过率高不代表多跳、状态更新、跨文档组合与变量绑定场景可用，需要更贴近真实任务的长上下文基准。
- 与推理基础设施的耦合：分页注意力、前缀缓存、连续批处理都以"缓存随长度增长"为前提设计，固定内存状态需要新的调度与容量规划模型。
- 确定性收益的兑现：内存预算可提前算清是工程价值核心，但需要模型、runtime 与硬件协同才能落地。
- 与 Agent 记忆系统的分工：哪些信息该留在缓存里、哪些该写入外部记忆、哪些该固化进参数，缺少统一框架。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [vLLM](https://github.com/vllm-project/vllm) — PagedAttention 与分页 KV Cache，现代推理服务缓存管理的事实标准
- [LMCache](https://github.com/LMCache/LMCache) — 面向 LLM 服务的 KV Cache 跨请求复用与分层存储层
- [EdgeRock](https://github.com/rockmatrix-ai/EdgeRock) — 岩芯矩阵联合港科大、CMU 开源的固定内存架构，以记忆岩锚（RMA）替代增长的 KV Cache

**论文**
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — 用操作系统分页思想管理 KV Cache，消除碎片并支持共享
- [Efficient Streaming Language Models with Attention Sinks](https://arxiv.org/abs/2309.17453) — 滑动窗口 + 注意力汇聚点，固定缓存实现无限流式输入
- [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://arxiv.org/abs/2306.14048) — 依据累积注意力分数动态淘汰 KV
- [SnapKV: LLM Knows What You are Looking for Before Generation](https://arxiv.org/abs/2404.14469) — 利用提示词注意力分布做查询感知的缓存压缩
- [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://arxiv.org/abs/2406.02069) — 按层分配缓存预算，浅层多留深层少留
- [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://arxiv.org/abs/2402.02750) — 键值分通道量化，把单 token 成本压到 2bit
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — 恒定内存的线性时间状态空间模型
- [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464) — 门控 delta 规则，混合架构中承担循环记忆层
- [Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time](https://arxiv.org/abs/2305.17118) — 基于重要性持久性假设的固定预算缓存淘汰
- [Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference](https://arxiv.org/abs/2407.11550) — 按注意力头自适应分配淘汰预算
- [EdgeRock: Strong Reasoning at Constant Memory](https://arxiv.org/abs/2610.10118) — EdgeRock-4B 技术报告，含记忆岩锚（RMA）架构、由 Qwen3.5-4B 分阶段转换的训练流程与完整评测

**综述 / 报道**
- [KV Cache砍掉99%，单卡吞吐飙6倍：港科大、CMU与岩芯矩阵开源 EdgeRock-4B](https://mp.weixin.qq.com/s/XlGTNPhtP88uAL5srNtoxQ) — 量子位报道。256K 上下文下 KV Cache 恒定为 72MiB，单卡 512 路并发、吞吐 6.42 倍；核心是记忆岩锚（RMA）：循环状态抓大意、1024 token 局部窗口管眼前、1024 条锚点库记关键，每 256 条候选与存量一起打分只留高分者；关掉 RMA 后长上下文准确率从 94.1% 跌到 0.4%，证明收益确由锚点读取远处细节而来。
- [EdgeRock 技术报告（中文版）](https://rockmatrix.ai/documents/edgerock-report-zh.pdf) — 上述报告的官方中文全文
