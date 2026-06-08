# Example Benchmark Run

This page shows what the benchmark looks like when it is run on the recommended biology pilot v2 dataset.

The biology v2 dataset contains 60 structured prediction questions from 10 target papers. It uses directional labels only:

- `positive`: the intervention or variable increases the outcome, improves it, or has a positive association.
- `negative`: the intervention or variable decreases the outcome, suppresses it, or has a negative association.
- `null`: the target paper reports no clear change in this context.
- `mixed`: different readouts move in different directions.

The v2 dataset has no `unsupported` answers.

## 1. Validate The Dataset

Command:

```bash
python -m temporal_benchmark.cli validate \
  --instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --corpus data/example_corpus.jsonl \
  --access-mode preprint_aware
```

Example output excerpt:

```text
bio_001_v2_q01: cutoff=2025-10-02 allowed_prior_papers=4
bio_001_v2_q02: cutoff=2025-10-02 allowed_prior_papers=4
...
bio_010_v2_q06: cutoff=2024-11-04 allowed_prior_papers=4

Validated 60 instances against 4 corpus papers.
Mean allowed prior papers: 4.00
```

This command checks that the benchmark instances are readable and that the cutoff logic runs for every target paper. The `data/example_corpus.jsonl` file is only a toy corpus, so this is a structural check rather than a real biology evaluation.

## 2. Gate Agent Search Results

In the search-agent setting, the agent can search for papers, but every candidate paper must pass the temporal leakage gate before it becomes usable prior literature.

Command:

```bash
python -m temporal_benchmark.cli gate-search \
  --instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --candidate-corpus biology_pilot/search_candidates_example.jsonl \
  --access-mode preprint_aware \
  --out outputs/biology_v2_gated_prior_corpus.jsonl \
  --audit-out outputs/biology_v2_search_gate_audit.jsonl
```

Example output:

```json
{
  "access_mode": "preprint_aware",
  "allowed_instance_candidate_pairs": 12,
  "audit_out": "outputs/biology_v2_search_gate_audit.jsonl",
  "candidate_papers": 4,
  "deduped_allowed_corpus_papers": 2,
  "instances": 60,
  "out": "outputs/biology_v2_gated_prior_corpus.jsonl",
  "rejected_instance_candidate_pairs": 12
}
```

The audit file explains why each candidate paper was accepted or rejected. Rejection reasons include `post_cutoff`, `is_target_paper`, `cites_target_paper`, `mentions_target_title`, and `not_peer_reviewed`.

## 3. Run A Baseline

The following command runs a random baseline. This is useful for checking the output format, not for scientific conclusions.

Command:

```bash
python -m temporal_benchmark.cli run-baseline \
  --instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --corpus data/example_corpus.jsonl \
  --baseline random \
  --access-mode preprint_aware \
  --seed 7 \
  --out outputs/biology_v2_random_predictions.jsonl
```

Example metric report:

```json
{
  "direction_accuracy": 0.23333333333333334,
  "evidence_recall": 0.0,
  "expected_calibration_error": 0.016666666666666663,
  "label_distribution": {
    "mixed": 4,
    "negative": 27,
    "null": 5,
    "positive": 24
  },
  "macro_f1": 0.19866092778574845,
  "n": 60,
  "negative_control_false_positive_rate": 0.0,
  "numeric_coverage": 0.0,
  "numeric_mae": 0.0,
  "numeric_question_count": 0,
  "numeric_within_tolerance_accuracy": 0.0,
  "question_type_distribution": {
    "context_shift": 4,
    "null_control": 3,
    "ordinary": 53
  },
  "relation_accuracy": 1.0,
  "strength_accuracy": 0.0
}
```

The prediction file is JSONL. Each line is one prediction:

```json
{"confidence": 0.25, "method": "random", "predicted_direction": "null", "predicted_numeric_value": null, "predicted_strength": "unknown", "question_id": "bio_001_v2_q01", "rationale": "Uniform random draw from this question's answer choices with seed 7.", "relation_exists": true, "supporting_paper_ids": []}
```

## 4. Majority Baseline Example

Command:

```bash
python -m temporal_benchmark.cli run-baseline \
  --instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --train-instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --corpus data/example_corpus.jsonl \
  --baseline majority \
  --access-mode preprint_aware \
  --out outputs/biology_v2_majority_predictions.jsonl
```

Example metric report:

```json
{
  "direction_accuracy": 0.45,
  "evidence_recall": 0.0,
  "expected_calibration_error": 0.0,
  "label_distribution": {
    "mixed": 4,
    "negative": 27,
    "null": 5,
    "positive": 24
  },
  "macro_f1": 0.15517241379310345,
  "n": 60,
  "negative_control_false_positive_rate": 0.0,
  "numeric_coverage": 0.0,
  "numeric_mae": 0.0,
  "numeric_question_count": 0,
  "numeric_within_tolerance_accuracy": 0.0,
  "question_type_distribution": {
    "context_shift": 4,
    "null_control": 3,
    "ordinary": 53
  },
  "relation_accuracy": 1.0,
  "strength_accuracy": 0.0
}
```

Because `negative` is the most common v2 label, the majority baseline predicts `negative` for every question. A useful forecasting agent should beat this baseline while also providing calibrated confidence and high-quality supporting evidence.

## 5. What A Real Agent Output Should Look Like

A real forecasting agent should produce one JSON object per question:

```json
{
  "question_id": "bio_002_v2_q01",
  "predicted_direction": "negative",
  "predicted_strength": "moderate",
  "predicted_numeric_value": null,
  "relation_exists": true,
  "confidence": 0.74,
  "supporting_paper_ids": ["prior_asthma_001", "prior_btla_002"],
  "rationale": "Prior Th17-driven asthma studies suggest that activating inhibitory checkpoint signaling should reduce airway hyperreactivity and lung inflammation."
}
```

For quantitative questions, `predicted_numeric_value` can be used for an estimated correlation coefficient, effect size, odds ratio, tumor-volume ratio, or percentage change.
