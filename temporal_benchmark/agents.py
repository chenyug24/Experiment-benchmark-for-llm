from __future__ import annotations

from dataclasses import dataclass

from .retrieval import TfidfRetriever
from .schema import Paper, PredictionQuestion


CONSTRUCTION_PROMPT = """\
You are constructing a temporally controlled scientific forecasting benchmark.
Read the target paper results, figures, tables, discussion, and conclusion.
Extract relationship-level findings that can become prediction questions.

Return JSON with:
- entity_1
- relation
- entity_2
- context
- question_type: "ordinary", "null_control", "decoy_relation", or "context_shift"
- answer_choices: ["positive", "negative", "null", "mixed"] plus "unsupported" for unsupported controls
- relation_exists
- gold_direction
- gold_strength: "weak", "moderate", "strong", or "unknown"
- numeric_metric: optional, for quantitative questions such as "correlation_r", "coefficient_beta", "odds_ratio", "mean_difference", or "percent_change"
- gold_numeric_value: optional number extracted from the target paper
- numeric_tolerance: optional acceptable absolute error for numeric evaluation
- numeric_unit: optional unit, such as "r", "beta", "OR", "%", "mm", or "tumor_volume_mm3"
- short_gold_rationale

Do not include information that the evaluated prediction agent should see.
"""


FORECASTING_PROMPT = """\
You are an evaluated forecasting agent. You must not use the target paper or
post-cutoff information. Predict the likely result of the target paper from
the temporally valid prior literature only.

Return JSON with:
- predicted_direction: "positive", "negative", "null", "mixed", or "unsupported"
- predicted_strength: "weak", "moderate", "strong", or "unknown"
- relation_exists: false when the query is unsupported or cannot be inferred
- predicted_numeric_value: number or null when the question asks for a quantitative value
- confidence: number from 0 to 1
- supporting_paper_ids
- rationale
"""


@dataclass(frozen=True)
class ForecastingPacket:
    question: str
    instructions: str
    evidence: list[dict[str, str | float]]


def build_forecasting_packet(
    question: PredictionQuestion,
    prior_papers: list[Paper],
    k: int = 8,
) -> ForecastingPacket:
    results = TfidfRetriever(prior_papers).search(question, k=k) if prior_papers else []
    evidence = [
        {
            "paper_id": result.paper.paper_id,
            "title": result.paper.title,
            "abstract": result.paper.abstract,
            "retrieval_score": round(result.score, 4),
        }
        for result in results
    ]
    return ForecastingPacket(
        question=question.natural_language,
        instructions=FORECASTING_PROMPT,
        evidence=evidence,
    )
