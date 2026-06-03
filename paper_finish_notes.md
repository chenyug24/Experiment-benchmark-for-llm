# Proposal Finishing Notes

The current proposal has a strong core. To make it paper-ready, I would add or sharpen the following pieces.

## Add A Third Contribution

Section 9 says there are three contributions but lists only two. A natural third contribution is:

Third, it introduces a reproducible leakage-control protocol and baseline suite for separating prospective scientific forecasting from retrospective retrieval, citation leakage, and memorization.

## Add A Formal Dataset Schema

The methods section should define the fields implemented in the starter code:

- Target paper metadata: title, domain, earliest public release dates, references, buffer size.
- Prediction question: entity 1, relation, entity 2, context, answer choices, gold direction, gold strength, relation-existence label.
- Prior corpus paper: title, abstract/full text, public release dates, paper type, citations, structured findings.
- Prediction output: direction, strength, confidence, supporting evidence, rationale.

## Add Leakage Audit Protocol

The proposal should explicitly say that each benchmark instance gets an automated and manual leakage audit:

- Exclude the target paper itself.
- Exclude any paper or artifact after the cutoff.
- Exclude papers that cite the target.
- Flag target-title mentions in prior-corpus text.
- Manually audit a stratified sample of preprints, online-first records, and highly similar papers.

## Add Experimental Design

A clean pilot experiment can compare:

- Majority baseline.
- Random baseline.
- Nearest prior paper baseline.
- Evidence-voting baseline.
- Weighted evidence-voting baseline.
- Single-agent RAG baseline.
- Structured retrieval + synthesis + forecast agent.

Evaluate each under `strict`, `preprint_aware`, and `reference_only` access settings. The reference-only setting should be framed as a diagnostic ablation because it may leak information through citation selection.

## Add Reporting Table

The paper should report:

- Direction accuracy.
- Macro F1.
- Strength accuracy when available.
- Relation-existence accuracy.
- Expected calibration error.
- Evidence recall or evidence support quality.
- Performance by domain and access regime.

## Add A Pilot Completion Checklist

- Select 50 to 100 target empirical papers.
- Record earliest public release dates and 90-day buffered cutoffs.
- Generate 1 to 5 structured prediction questions per target paper.
- Build a prior-literature corpus for each target using only records available before cutoff.
- Run automated leakage checks.
- Manually audit at least 10 percent of instances.
- Run all baselines and the structured agent system.
- Analyze which domains, relations, and access regimes are most predictable.
