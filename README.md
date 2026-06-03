# Temporal Science Benchmark Starter

This workspace turns the proposal into a small, runnable benchmark scaffold for testing whether an agent can predict empirical scientific findings from temporally valid prior literature.

## What Is Implemented

- JSONL schemas for target papers, prediction questions, prior-corpus papers, findings, and predictions.
- Conservative cutoff logic: `earliest_public_date(target) - buffer_days`.
- Access regimes from the proposal: `strict`, `preprint_aware`, and `reference_only`.
- Leakage warnings for target-paper presence, post-cutoff papers, target citations, and target-title mentions.
- Transparent TF-IDF retrieval with no external services.
- Baselines: majority, random, nearest prior paper, evidence vote, and weighted evidence vote.
- Metrics: direction accuracy, macro F1, relation accuracy, strength accuracy, expected calibration error, and evidence recall.
- Prompt templates for the construction agent and evaluated forecasting agent.

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

## Data Model

Each prediction instance contains a target paper and one structured question. The prediction agent sees the question and allowed prior papers, but not the target paper text.

Each corpus paper has public release metadata and optional structured findings. The starter baselines rely on these findings to infer directions from prior papers. In a full version, those findings can come from human annotation, information extraction, or a construction agent run only on temporally allowed prior papers.

## Next Implementation Step

For a real pilot, create:

- `data/pilot_instances.jsonl` with 50 to 100 target-paper questions.
- `data/pilot_corpus.jsonl` with prior literature and release dates.
- A held-out split so the majority baseline is fit on training labels only.
- Manual leakage audit samples for ambiguous papers, preprints, and online-first publication records.
