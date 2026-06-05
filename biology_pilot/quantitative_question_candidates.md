# Quantitative Question Candidates

These are candidate quantitative questions for the biology pilot. They are not final gold labels yet. Fill `gold_numeric_value` only after checking the target paper full text, figures, tables, statistical annotations, and supplementary files.

Use these fields in `biology_pilot_instances.jsonl` after verification:

```json
{
  "numeric_metric": "correlation_r",
  "gold_numeric_value": 0.42,
  "numeric_tolerance": 0.10,
  "numeric_unit": "r"
}
```

For correlations, use `numeric_metric: "correlation_r"` and set `numeric_tolerance` to something like `0.05` or `0.10` depending on how precise the paper reports the value. For non-correlation quantitative findings, use metrics such as `mean_difference`, `percent_change`, `fold_change`, `hazard_ratio`, `odds_ratio`, `tumor_volume_ratio`, or `survival_days`.

## Candidate Questions

1. `bio_003_intestinimonas_metabolic`
   - Candidate: correlation between Intestinimonas abundance and metabolic-health markers in the human cohort.
   - Metric: `correlation_r`
   - Needs source: cohort correlation figure, table, or supplement.

2. `bio_003_intestinimonas_metabolic`
   - Candidate: quantitative change in adipose inflammation after Intestinimonas administration in diet-induced obese mice.
   - Metric: `percent_change` or `mean_difference`
   - Needs source: mouse intervention figure values.

3. `bio_007_fh15_colitis`
   - Candidate: effect size for Fh15 treatment on disease activity index in DSS-induced colitis.
   - Metric: `mean_difference` or `percent_change`
   - Needs source: DAI plot or table.

4. `bio_007_fh15_colitis`
   - Candidate: effect size for Fh15 treatment on colon length.
   - Metric: `mean_difference`
   - Needs source: colon-length figure.

5. `bio_010_if_colitis`
   - Candidate: quantitative reduction in colonic histological score after intermittent fasting.
   - Metric: `mean_difference` or `percent_change`
   - Needs source: histology score figure.

6. `bio_010_if_colitis`
   - Candidate: quantitative reduction in CD4-positive T-cell proportion after intermittent fasting.
   - Metric: `percentage_point_change`
   - Needs source: flow-cytometry figure or supplement.

7. `bio_008_cryo_pd1_cervical`
   - Candidate: quantitative change in distant tumor volume for cryoablation plus anti-PD-1 versus control.
   - Metric: `tumor_volume_ratio` or `percent_change`
   - Needs source: distant-tumor growth curve.

8. `bio_008_cryo_pd1_cervical`
   - Candidate: quantitative survival benefit from cryoablation plus anti-PD-1.
   - Metric: `survival_days`, `hazard_ratio`, or `median_survival_ratio`
   - Needs source: Kaplan-Meier plot or survival table.

9. `bio_009_gastric_crispr`
   - Candidate: quantitative increase in tumor size after Pten inactivation.
   - Metric: `fold_change`, `mean_difference`, or `tumor_volume_ratio`
   - Needs source: gastric tumor-size figure.

10. `bio_006_uchl5_hnscc`
    - Candidate: quantitative anti-PD-1 response improvement after Uchl5 deficiency.
    - Metric: `tumor_volume_ratio`, `percent_change`, or `response_rate_difference`
    - Needs source: anti-PD-1 treatment-response figure.

## Recommended Answer Format

For an evaluated agent, ask for both direction and number:

```json
{
  "predicted_direction": "positive",
  "predicted_strength": "moderate",
  "predicted_numeric_value": 0.35,
  "confidence": 0.72,
  "supporting_paper_ids": ["prior_001", "prior_002"],
  "rationale": "Prior cohort studies show a positive but moderate association."
}
```

This lets the benchmark evaluate whether the agent got the direction right and whether its numeric estimate was close.
