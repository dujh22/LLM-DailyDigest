+++
title = 'Groom'
proposer = '杜晋华'
since = '2026-05-28'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# Groom

> 研究方向：**数据 / 模型的培养与精炼（grooming）**——围绕训练数据的清洗、筛选、配比与 token 级质量、安全分析，系统化地"养好"模型。

## 研究范畴

"grooming"关注在数据进入训练前后的精炼与治理：从大规模、噪声高的原始语料中，筛选、配比、清洗出对目标能力最有价值的子集，并对 token 级别的质量与安全效应进行度量。本方向涵盖：数据精炼与配比（data curation / mixing）、token 级质量分析、安全 / 毒性 token 审计，以及面向精炼过程的评测基准。社区关注的核心问题包括：如何量化数据 / token 的"质量"及其对模型行为的边际影响、token 级特定模式（安全、毒性、越狱触发等）如何影响模型、精炼与配比策略如何与下游能力（推理、对齐、安全）关联，以及如何自动化、可审计地完成大规模数据治理。

## 研究挑战

- 大规模数据的自动化清洗与去重成本。
- token 级效应的因果归因困难、易受混杂。
- 安全与能力、隐私与效用之间的权衡。
- 精炼过程本身的可复现性与评测有效性。

## 自研项目

- [Groom](https://github.com/dujh22/Groom)
- [H-TokenBench](https://github.com/dujh22/H-TokenBench)

## 相关工作

> 公开检索（GitHub / arXiv，多组关键词：data/model/agent grooming、code/repository grooming、fine-tuning grooming 等）暂未找到以 "Groom" 为名的明确公开项目或论文。相关公开工作可参考 [[DataEvolve]]（数据自进化）与 [[EvalEvolve]]（进化式评测）方向下的资源。
