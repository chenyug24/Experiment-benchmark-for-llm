# Biology Mini Pilot Question Bank

This folder is a separate biology-focused pilot draft for the temporal scientific forecasting benchmark.

It contains:

- `target_papers.md`: 10 candidate biology / biomedical target papers.
- `biology_pilot_instances.jsonl`: 60 draft prediction instances, about 6 questions per target paper.
- `questions_and_answers_zh.md`: Chinese readable version of the 60 questions and answers.
- `biology_pilot_instances_v2.jsonl`: recommended v2 version with richer context, no `unsupported` labels, and balanced positive / negative / null / mixed labels.
- `questions_and_answers_v2_zh.md`: readable v2 question-answer guide with the expanded context for each question.
- `search_candidates_example.jsonl`: a tiny example of agent-found candidate papers before temporal gating.
- `quantitative_question_candidates.md`: candidate correlation / effect-size questions that need full-text numeric extraction.

The goal is to test the updated benchmark design:

- ordinary relationship prediction
- biomarker / mechanism prediction
- null-control questions
- decoy-relation questions
- context-shift questions
- `unsupported` labels corresponding to the proposal's \(\bot\)
- optional quantitative targets, such as correlation coefficients or effect sizes

Important: this is a question-bank draft. Before using it as real benchmark data, verify every gold label against the target paper full text and verify the earliest public availability date using PubMed, Crossref, publisher pages, preprint records, and DOI metadata.

Prefer the v2 files for new experiments. The original `biology_pilot_instances.jsonl` is kept as an earlier draft, but it uses `unsupported` controls and a support-based meaning of `positive`. The v2 file instead uses directional labels: `positive` means increase / improvement / positive association, while `negative` means decrease / suppression / negative association.

## How To Inspect It

From the repo root:

```bash
python -m temporal_benchmark.cli validate \
  --instances biology_pilot/biology_pilot_instances_v2.jsonl \
  --corpus data/example_corpus.jsonl \
  --access-mode preprint_aware
```

This will only test that the instance file is structurally readable and that cutoff logic can run. It is not a real biology evaluation yet because `data/example_corpus.jsonl` is only toy prior literature.

## Search-Agent Workflow

Use this when you want the agent to find papers itself. The agent or search API writes candidate papers to JSONL first. Then the benchmark filters them:

```bash
python -m temporal_benchmark.cli gate-search \
  --instances biology_pilot/biology_pilot_instances.jsonl \
  --candidate-corpus biology_pilot/search_candidates_example.jsonl \
  --access-mode preprint_aware \
  --out outputs/biology_gated_prior_corpus.jsonl \
  --audit-out outputs/biology_search_gate_audit.jsonl
```

The agent is allowed to search, but it is not allowed to directly use every search result. It can only use papers that appear in the gated output corpus. Check the audit file to see why each candidate paper was accepted or rejected.

Candidate papers may optionally include metadata fields such as:

```json
{"target_paper_ids": ["bio_001_inulin_colitis"], "question_ids": ["bio_001_q01"]}
```

These fields let you record which target/question the search agent found the paper for.

## Next Step

Create a real candidate search-result file:

```text
biology_pilot/biology_search_candidates.jsonl
```

For each target paper, let the agent collect 10-30 candidate papers. Each candidate paper should include release dates, abstract, paper type, and structured findings when possible. Then run `gate-search` to produce the usable prior corpus.

For quantitative questions, first use `quantitative_question_candidates.md` as a checklist. Do not fill `gold_numeric_value` until the exact number has been verified from the target paper full text or supplement.
