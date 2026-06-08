# Temporal Science Benchmark Starter

This workspace turns the proposal into a small, runnable benchmark scaffold for testing whether an agent can predict empirical scientific findings from temporally valid prior literature.

## What Is Implemented

- JSONL schemas for target papers, prediction questions, prior-corpus papers, findings, and predictions.
- Logical-query fields for \(X\), \(Y\), context \(Z\), relation \(r\), and question type.
- Negative-control questions: `null_control`, `decoy_relation`, and `context_shift`.
- An `unsupported` answer label matching the proposal's \(\bot\) relation label.
- Conservative cutoff logic: `earliest_public_date(target) - buffer_days`.
- Access regimes from the proposal: `strict`, `preprint_aware`, and `reference_only`.
- Leakage warnings for target-paper presence, post-cutoff papers, target citations, and target-title mentions.
- Search-agent gating: an evaluated agent may find its own candidate papers, but every candidate must pass temporal and leakage filters before it becomes usable prior literature.
- Transparent TF-IDF retrieval with no external services.
- Baselines: majority, random, nearest prior paper, evidence vote, and weighted evidence vote.
- Metrics: direction accuracy, macro F1, relation accuracy, strength accuracy, expected calibration error, evidence recall, and negative-control false positive rate.
- Prompt templates for the construction agent and evaluated forecasting agent.
- Optional quantitative prediction fields for correlations and effect sizes: `numeric_metric`, `gold_numeric_value`, `numeric_tolerance`, `numeric_unit`, and `predicted_numeric_value`.

## Run It

```bash
python -m unittest discover -s tests -v
```

```bash
python -m temporal_benchmark.cli validate \
  --instances data/example_instances.jsonl \
  --corpus data/example_corpus.jsonl \
  --access-mode preprint_aware
```

```bash
python -m temporal_benchmark.cli run-baseline \
  --instances data/example_instances.jsonl \
  --corpus data/example_corpus.jsonl \
  --baseline weighted_vote \
  --access-mode preprint_aware \
  --out outputs/weighted_vote_predictions.jsonl
```

```bash
python -m temporal_benchmark.cli evaluate \
  --instances data/example_instances.jsonl \
  --predictions outputs/weighted_vote_predictions.jsonl
```

## Search-Agent Setting

This is the setting where the agent can search for papers itself. The benchmark still controls leakage by treating search results as candidate papers, then passing them through a temporal gate.

```bash
python -m temporal_benchmark.cli gate-search \
  --instances biology_pilot/biology_pilot_instances.jsonl \
  --candidate-corpus biology_pilot/search_candidates_example.jsonl \
  --access-mode preprint_aware \
  --out outputs/biology_gated_prior_corpus.jsonl \
  --audit-out outputs/biology_search_gate_audit.jsonl
```

The output corpus contains candidate papers allowed for at least one target instance. The audit file records every allow/reject decision with reasons such as `post_cutoff`, `is_target_paper`, `cites_target_paper`, `mentions_target_title`, or `not_peer_reviewed`.

For a real experiment, replace `biology_pilot/search_candidates_example.jsonl` with papers found by your search agent or an API. The JSONL format is the same as the corpus format used by the baselines.

## Data Model

Each prediction instance contains a target paper and one structured question. The prediction agent sees the question and allowed prior papers, but not the target paper text.

Questions include a `question_type` field. Ordinary and null-control questions usually have `relation_exists: true`; decoy-relation and some context-shift questions can use `relation_exists: false` with `gold_direction: "unsupported"`.

Quantitative questions can add `numeric_metric`, `gold_numeric_value`, `numeric_tolerance`, and `numeric_unit`. For example, a correlation question might use `numeric_metric: "correlation_r"`, `gold_numeric_value: 0.42`, `numeric_tolerance: 0.10`, and `numeric_unit: "r"`. Predictions can include `predicted_numeric_value`, and evaluation reports numeric MAE, numeric coverage, and within-tolerance accuracy.

Each corpus paper has public release metadata and optional structured findings. The starter baselines rely on these findings to infer directions from prior papers. In a full version, those findings can come from human annotation, information extraction, or a construction agent run only on temporally allowed prior papers.

## Biology Pilot

The recommended biology pilot file is `biology_pilot/biology_pilot_instances_v2.jsonl`. It contains 60 questions from 10 target papers, richer experimental context for each question, no `unsupported` answers, and a more balanced directional label distribution: `negative`, `positive`, `null`, and `mixed`.

The readable guide is `biology_pilot/questions_and_answers_v2_zh.md`.

## Next Implementation Step

For a real pilot, create:

- `data/pilot_instances.jsonl` with 50 to 100 target-paper questions.
- `data/pilot_corpus.jsonl` or a gated search-agent corpus with prior literature and release dates.
- A held-out split so the majority baseline is fit on training labels only.
- Manual leakage audit samples for ambiguous papers, preprints, and online-first publication records.

## Paper Drafts

- `paper_draft.md`: first manuscript-style draft of the benchmark paper.
- `reading_guide_zh.md`: Chinese guide explaining how to read the paper and how to continue the project.
