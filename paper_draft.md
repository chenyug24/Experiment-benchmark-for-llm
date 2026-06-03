# A Temporally Controlled Benchmark for AI Agents Predicting Scientific Findings from Prior Literature

## Abstract

Large language model agents are increasingly used to retrieve, synthesize, and reason over scientific literature. However, many evaluations of scientific reasoning are vulnerable to retrospective information leakage: an agent may answer correctly because it has access to the target paper, later papers that cite it, post-publication commentary, or memorized training data. This paper proposes a temporally controlled benchmark for evaluating whether AI agents can predict empirical scientific findings using only information that was publicly available before the target paper appeared. Each benchmark instance treats a target paper as a forecasting problem. A construction agent, used only during dataset creation, reads the target paper and extracts structured relationship-level findings. The evaluated prediction agent never sees the target paper; it receives only a prediction question and temporally valid prior literature. We define conservative cutoff rules based on the earliest public availability date of the target paper minus a leakage buffer, formalize multiple access regimes, and provide deterministic baselines including majority prediction, random prediction, nearest-prior-paper retrieval, evidence voting, and weighted evidence voting. The benchmark evaluates direction accuracy, relation-existence accuracy, strength accuracy, confidence calibration, and evidence quality. By separating benchmark construction from benchmark evaluation and enforcing strict temporal access constraints, this benchmark aims to distinguish genuine prospective scientific reasoning from retrieval, citation leakage, and memorization.

## 1. Introduction

Scientific discovery is inherently prospective. Researchers form hypotheses, interpret prior evidence, design experiments, and make judgments about what new studies are likely to find. Modern AI agents can already search large literatures, summarize findings, and produce plausible explanations. A harder question is whether such systems can use prior literature to forecast the results of future empirical studies.

This question is difficult to evaluate because scientific text is embedded in time. Once a target paper has been published, many forms of information may leak the answer: the target paper itself, later papers that cite it, updated preprints, conference talks, press releases, lab webpages, replication studies, social media discussions, or model pretraining data. If an agent can access these sources, then high performance may reflect retrospective retrieval rather than prospective reasoning.

We propose a temporally controlled benchmark for evaluating AI agents on scientific finding prediction. For each target paper, the benchmark constructs one or more structured prediction questions from the paper's actual findings. The evaluated agent must predict the direction and strength of the finding using only literature available before a conservative cutoff date. The cutoff is defined as the earliest public availability date of the target paper minus a fixed buffer, such as 90 days.

The benchmark focuses on relationship-level prediction rather than free-form paper generation. Instead of asking an agent to predict an entire results section, we ask whether a relationship holds in a specific context: for example, whether an intervention improves an outcome, whether a biological factor increases a marker, whether a policy changes an economic measure, or whether a machine learning method improves performance. This design makes the task measurable while still requiring nontrivial synthesis of prior evidence.

The paper makes three contributions:

1. It proposes a temporally controlled benchmark for evaluating whether AI agents can predict empirical scientific findings from prior literature.
2. It formulates scientific forecasting as structured relationship-level prediction over entities, relations, outcomes, contexts, directions, strengths, and confidence scores.
3. It introduces a reproducible leakage-control protocol and baseline suite for distinguishing prospective scientific forecasting from retrospective retrieval, citation leakage, and memorization.

## 2. Task Definition

Let \(P^\*\) denote a target empirical paper. During benchmark construction, a construction agent or human annotator reads \(P^\*\) and extracts one or more findings. Each finding becomes a prediction question \(q_i\). The evaluated prediction agent never sees \(P^\*\). It sees only \(q_i\) and a set of temporally valid prior papers.

Each prediction question contains:

- entity or variable 1, \(X\)
- relation \(r\), such as affects, increases, decreases, inhibits, improves, reduces, or is associated with
- entity or outcome 2, \(Y\)
- context \(c\), such as population, dataset, experimental system, policy setting, disease, method, or measurement
- answer choices: positive, negative, null, or mixed
- gold direction from the target paper
- optional gold strength: weak, moderate, strong, or unknown
- relation-existence label

The evaluated agent outputs:

- predicted direction: positive, negative, null, or mixed
- predicted strength: weak, moderate, strong, or unknown
- confidence score in \([0,1]\)
- supporting prior papers
- short rationale

A natural-language version of the task is: given prior literature available before the target paper, does \(X\) increase, decrease, have no effect on, or have mixed effects on \(Y\) in context \(c\)?

## 3. Temporal Filtering and Leakage Control

Temporal filtering is the central methodological constraint. For each target paper \(P^\*\), we define:

\[
\text{cutoff}(P^\*) = \text{earliest_public_date}(P^\*) - \Delta
\]

where \(\Delta\) is a leakage buffer, set to 90 days in the initial protocol. The earliest public date is the first available timestamp among:

- journal online publication date
- DOI registration or online-first date
- indexing date, such as PubMed or a comparable database
- preprint first-posted date
- conference paper release date

The buffer reduces the risk that accepted manuscripts, conference previews, metadata updates, or informal discussion leak information before the formal publication date.

The benchmark defines three access regimes:

1. **Strict**: only peer-reviewed papers available before the cutoff date are allowed.
2. **Preprint-aware**: peer-reviewed papers and preprints are allowed, but only versions posted before the cutoff date.
3. **Reference-only**: the agent can use only papers cited by the target paper that were published before the cutoff.

The reference-only regime is useful as a diagnostic ablation, but it should not be treated as the main evaluation setting because a target paper's reference list may encode hidden information about its eventual result. The main setting is the time-indexed prior-literature corpus, where the agent retrieves from all available pre-cutoff literature.

For each instance, the benchmark should run automated leakage checks:

- exclude the target paper itself from the prior corpus
- exclude post-cutoff papers and artifacts
- flag papers that cite the target paper
- flag target-title mentions in prior-corpus text
- manually audit a subset of ambiguous preprints, online-first records, and highly similar papers

## 4. Dataset Construction

The pilot dataset should contain approximately 50 to 100 empirical target papers across multiple domains, such as psychology, economics, political science, education, biomedical science, materials science, climate science, and machine learning. The common requirement is that each target paper reports clear empirical findings about relationships between variables, methods, interventions, or outcomes.

Dataset construction has four stages.

First, target papers are selected. Each target must have enough metadata to determine a conservative earliest public availability date. Recent and lower-citation papers are preferred when possible because they reduce the risk of model memorization.

Second, findings are extracted from the target paper. A construction agent, with optional human review, reads the results, figures, tables, discussion, and conclusion. It extracts relationship-level findings and converts them into structured prediction questions. This construction stage can see the target paper because it is part of benchmark creation, not benchmark evaluation.

Third, a temporally valid prior-literature corpus is built for each target paper. Candidate prior papers are filtered by cutoff date and access regime. The corpus records paper metadata, release dates, paper type, citations, abstracts or full text, and optional structured findings.

Fourth, leakage audits are performed. Automated checks identify obvious violations, and manual review verifies a subset of cases where metadata or textual similarity may be ambiguous.

## 5. Agent Framework

The benchmark distinguishes construction agents from evaluation agents.

The construction agent is used offline to create the benchmark. It sees the target paper and produces structured questions and gold labels.

The evaluation agent is the system being tested. It must not see the target paper or post-cutoff information. A structured evaluation agent may contain three components:

1. A retrieval agent that searches temporally valid prior literature.
2. An evidence-synthesis agent that summarizes prior evidence relevant to the relationship.
3. A forecasting agent that predicts the target finding and provides confidence, support, and rationale.

The forecasting agent should not simply count prior papers. It should consider contextual similarity: population, dataset, experimental design, method, measurement, domain, and whether prior evidence transfers to the target setting.

## 6. Baselines

Baselines provide lower and middle bounds for agent performance.

The **majority baseline** predicts the most common direction in the training set:

\[
\hat{y}^{maj}_i = \arg\max_{y \in \mathcal{Y}} \sum_{j=1}^{n_{train}} \mathbf{1}(y_j = y)
\]

The **random baseline** samples uniformly from the answer choices:

\[
\hat{y}^{rand}_i \sim \text{Uniform}(\mathcal{Y})
\]

The **nearest-prior-paper baseline** retrieves the most similar prior paper before the cutoff and copies the direction of its most relevant structured finding:

\[
p_i^\* = \arg\max_{p \in C_i} \text{sim}(q_i, p)
\]

The **evidence-voting baseline** retrieves the top \(K\) prior papers and predicts the most common direction among their aligned findings:

\[
\hat{y}^{vote}_i = \arg\max_{y \in \mathcal{Y}} \sum_{p \in R_i^K} \mathbf{1}(d(p, q_i) = y)
\]

The **weighted evidence-voting baseline** weights each vote by retrieval similarity:

\[
\hat{y}^{weighted}_i = \arg\max_{y \in \mathcal{Y}} \sum_{p \in R_i^K} \text{sim}(q_i,p) \cdot \mathbf{1}(d(p,q_i)=y)
\]

The **single-agent RAG baseline** gives one language model the question and retrieved prior papers, then asks it to produce a structured prediction. The proposed multi-agent system separates retrieval, evidence synthesis, and forecasting to test whether modular reasoning improves performance.

## 7. Evaluation Metrics

The primary metric is direction accuracy:

\[
\text{Accuracy} = \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}(\hat{y}_i = y_i)
\]

Because label distributions may be imbalanced, macro F1 should also be reported. Relation-existence accuracy measures whether the system correctly predicts whether a relationship exists. Strength accuracy measures weak, moderate, or strong effect predictions when those labels are available.

Calibration is measured using expected calibration error. Predictions are binned by confidence, and the difference between average confidence and empirical accuracy is computed within each bin.

Evidence quality can be measured through evidence recall when gold supporting papers are known, and through human or model-assisted review when evidence support is qualitative. A strong prediction should not only match the gold direction but also cite temporally valid prior evidence that genuinely supports the rationale.

Results should be reported by access regime, domain, relation type, and question difficulty. A large performance gap between reference-only and time-indexed retrieval may indicate citation-selection leakage.

## 8. Starter Implementation

The accompanying starter implementation operationalizes the benchmark as a lightweight Python package. It defines JSONL schemas for target papers, prediction questions, prior-corpus papers, structured findings, and predictions. It implements conservative cutoff computation, strict/preprint-aware/reference-only filtering, leakage warnings, deterministic TF-IDF retrieval, baseline methods, and evaluation metrics.

The implementation is intentionally dependency-light. This makes the benchmark auditable before adding external scholarly search APIs, embedding models, vector databases, or LLM providers.

The current example data are toy records used only to verify that the benchmark pipeline runs end to end. They should not be reported as scientific results. A real pilot requires a curated dataset of 50 to 100 target papers, a larger pre-cutoff prior-literature corpus, and manual leakage audits.

## 9. Pilot Study Plan

The pilot study should answer four questions:

1. Can any evaluated agent outperform majority, random, nearest-paper, and evidence-voting baselines?
2. Does a structured retrieval-synthesis-forecasting agent outperform a single-agent RAG baseline?
3. How sensitive is performance to the access regime?
4. Which domains and relation types are most predictable from prior literature?

The pilot should use a held-out evaluation split. Majority and learned baselines should be fit only on training labels. Each target paper should have one to five prediction questions, depending on the clarity and number of major empirical findings. The final report should include aggregate metrics, per-domain metrics, leakage audit statistics, qualitative error analysis, and examples of successful and failed forecasts.

## 10. Limitations

The benchmark has several limitations.

First, gold-label extraction is difficult. Scientific findings are often conditional, statistical, or nuanced. Human review may be necessary to ensure that structured labels do not oversimplify the target paper.

Second, some findings are genuinely novel. In these cases, poor prediction may reflect the absence of prior evidence rather than weak reasoning.

Third, language models may have memorized target papers during pretraining. Temporal filtering controls retrieval access, but it cannot fully remove memorization. Recent papers, low-citation papers, private held-out sets, and no-retrieval controls can reduce this risk.

Fourth, publication metadata can be noisy. Preprint versions, online-first publication, DOI registration, and indexing dates may disagree. The benchmark therefore uses conservative cutoffs and manual audits.

Fifth, evidence quality is not fully captured by accuracy. An agent may predict the right direction for the wrong reason, or cite evidence that is temporally valid but contextually weak. Evidence review should therefore accompany quantitative metrics.

## 11. Conclusion

This paper proposes a temporally controlled benchmark for evaluating whether AI agents can predict empirical scientific findings from prior literature. By treating each target paper as a forecasting problem, generating structured relationship-level questions, and enforcing strict cutoff-based access rules, the benchmark aims to separate prospective scientific reasoning from retrospective retrieval and memorization.

The benchmark is designed to be practical: it includes explicit data schemas, leakage checks, access regimes, baselines, and evaluation metrics. The next step is to build a 50 to 100 paper pilot dataset and evaluate structured agent systems against deterministic and RAG baselines. If successful, the benchmark can help measure whether AI systems are not only capable of reading science, but also capable of reasoning prospectively about what future studies are likely to find.

## Appendix A. Current Repository Commands

Run tests:

```bash
python -m unittest discover -s tests -v
```

Validate temporal filtering and leakage warnings:

```bash
python -m temporal_benchmark.cli validate \
  --instances data/example_instances.jsonl \
  --corpus data/example_corpus.jsonl \
  --access-mode preprint_aware
```

Run a baseline:

```bash
python -m temporal_benchmark.cli run-baseline \
  --instances data/example_instances.jsonl \
  --corpus data/example_corpus.jsonl \
  --baseline weighted_vote \
  --access-mode preprint_aware \
  --out outputs/weighted_vote_predictions.jsonl
```

Evaluate predictions:

```bash
python -m temporal_benchmark.cli evaluate \
  --instances data/example_instances.jsonl \
  --predictions outputs/weighted_vote_predictions.jsonl
```

## Appendix B. Items To Complete Before Submission

- Add real related-work citations.
- Build the 50 to 100 paper pilot dataset.
- Run all baselines under all access regimes.
- Add single-agent RAG and structured multi-agent results.
- Add tables for aggregate metrics, domain metrics, calibration, and leakage audit outcomes.
- Add qualitative examples of correct forecasts, incorrect forecasts, and leakage-sensitive cases.
- Decide whether the submission should be framed as a benchmark paper, methods paper, or short workshop paper.
