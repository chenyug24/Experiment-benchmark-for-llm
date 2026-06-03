# 中文阅读指南：这篇论文怎么看、怎么继续写

## 一句话版

这篇论文想做一个新的 benchmark：让 AI agent 只看“目标论文发表之前已经存在的文献”，去预测目标论文最后会得到什么 empirical finding。重点不是让模型复述论文，而是测试它有没有真正的“前瞻性科学推理”能力。

## 核心问题

你要抓住一个主问题：

AI agent 能不能在不看目标论文、也不看目标论文之后的信息的情况下，根据之前的文献预测目标论文的发现方向？

比如：

- 某个药物会不会提高某个生物指标？
- 某个政策会不会改善经济结果？
- 某种心理治疗会不会改善行为表现？
- 某个机器学习方法会不会提高准确率？

答案不是开放作文，而是结构化预测：

- positive
- negative
- null
- mixed

还可以加 strength、confidence、supporting evidence、rationale。

## 为什么这个题重要

普通的科学问答 benchmark 很容易泄漏答案。模型可能已经见过目标论文，或者能搜到后来的论文、新闻、preprint 更新、引用目标论文的文章。这样它答对不一定是推理强，而可能只是找到了答案。

所以这篇论文最大的贡献是 temporal control，也就是按时间切断信息：

目标论文 cutoff date = 目标论文最早公开日期 - buffer

proposal 里建议 buffer 用 90 天。这样可以减少 accepted manuscript、conference preview、metadata 更新等造成的提前泄漏。

## 每一节怎么读

### 1. Introduction

看这节时只问：作者为什么要做这个 benchmark？

答案是：现在 AI 能读文献，但我们不知道它能不能在时间上“站在过去”预测未来研究结果。

### 2. Task Definition

这一节是整篇论文的骨架。

每个 target paper 会变成一个或多个 prediction question。预测 agent 不能看 target paper，只能看 cutoff 之前的 prior literature。

你要特别注意几个字段：

- X: entity or variable 1
- relation: improves / increases / decreases / affects 等
- Y: outcome
- context: population / dataset / method / measurement
- gold direction: target paper 的真实结果

### 3. Temporal Filtering

这是最关键的方法部分。

看这一节时要问：什么资料可以给 agent 看，什么不可以？

三种 access setting：

- strict：只看 cutoff 前 peer-reviewed paper
- preprint-aware：也可以看 cutoff 前 preprint
- reference-only：只看 target paper 参考文献里、且 cutoff 前的文献

注意：reference-only 不是主实验，而是 ablation。因为 target paper 的 reference list 本身可能暗含答案。

### 4. Dataset Construction

这一节回答：benchmark 数据怎么造？

实际流程是：

1. 选 50 到 100 篇 empirical target papers。
2. 对每篇 target paper 找最早公开日期。
3. 从 target paper 的 results / figures / tables / discussion 提取 finding。
4. 把 finding 变成结构化问题。
5. 建 prior-literature corpus。
6. 做 leakage audit。

这里以后最费时间的是选论文和查日期。

### 5. Agent Framework

这里区分两种 agent：

construction agent：可以看 target paper，用来造题和 gold labels。

evaluation agent：被测试的 agent，绝对不能看 target paper。

被测试系统可以分成三步：

1. retrieval
2. evidence synthesis
3. forecasting

### 6. Baselines

这节是实验比较对象。

你至少需要这些 baseline：

- majority baseline
- random baseline
- nearest prior paper
- evidence voting
- weighted evidence voting
- single-agent RAG

如果你的 multi-agent method 打不过这些 baseline，论文就比较危险；如果打过了，就有结果可以讲。

### 7. Metrics

主要指标：

- direction accuracy：方向预测准不准
- macro F1：类别不平衡时更公平
- relation accuracy：有没有关系判断准不准
- strength accuracy：强弱预测准不准
- expected calibration error：confidence 是否校准
- evidence recall / evidence quality：引用的 prior evidence 是否真的支持预测

### 8. Starter Implementation

这一节对应 GitHub 代码。

现在代码已经实现：

- JSONL schema
- cutoff date 计算
- leakage warnings
- 三种 access regime
- TF-IDF retrieval
- deterministic baselines
- evaluation metrics
- CLI commands
- unit tests

这部分可以证明项目不是只有想法，已经有一个可运行的 prototype。

### 9. Pilot Study Plan

这节是下一步工作清单。

真正能投稿之前，需要补：

- 50 到 100 篇 target papers
- real prior-literature corpus
- 所有 baseline 的结果
- RAG baseline
- structured multi-agent result
- error analysis
- leakage audit table

## 你现在应该怎么推进

最推荐的顺序：

1. 先把 `paper_draft.md` 当作论文主稿。
2. 把 proposal 里的内容慢慢合并到 draft 中。
3. 选一个领域先做 pilot，比如 psychology 或 machine learning。
4. 先做 10 篇 target papers 的 mini pilot，不要一开始就做 100 篇。
5. 每篇 target paper 只做 1 到 3 个 high-confidence questions。
6. 跑 baseline。
7. 看结果有没有 signal。
8. 再决定扩展到 50 到 100 篇。

## 和老师/合作者怎么解释

你可以这样讲：

“这个项目不是普通的 LLM scientific QA。我们把每篇论文当成一个 forecasting task，并严格限制模型只能使用目标论文发表前的信息。这样可以测试模型是否真的能从 prior literature 预测 future empirical findings，而不是靠检索或记忆已经发表的答案。”

## 最容易被问到的问题

### Q1: 模型是不是可能训练时已经看过目标论文？

是的，这是风险。解决办法包括：

- 用很新的论文
- 用低引用论文
- 用 private held-out test set
- 做 no-retrieval baseline
- 在 limitation 里承认 pretraining memorization 无法完全消除

### Q2: gold label 会不会太主观？

会，所以需要人类检查。可以先让 construction agent 提取，再人工审核。

### Q3: reference-only setting 为什么可能有问题？

因为 target paper 引用了哪些文献，本身可能透露作者的研究脉络和结果方向。它适合做 ablation，不适合作为主设置。

### Q4: 没有 prior literature 的新发现怎么办？

这种情况本来就难预测。可以把它作为 difficulty 分析：有 prior evidence 的问题和 truly novel 的问题分开报告。

## 最短阅读路线

如果你时间很少，只看这几部分：

1. Abstract
2. Introduction 最后一段贡献
3. Task Definition
4. Temporal Filtering
5. Baselines
6. Pilot Study Plan

这六块看懂，就基本懂整篇论文了。
