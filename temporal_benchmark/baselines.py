from __future__ import annotations

import random
from collections import Counter, defaultdict

from .retrieval import TfidfRetriever, infer_direction_from_paper
from .schema import Direction, Paper, Prediction, PredictionInstance
from .temporal import allowed_prior_papers


def majority_baseline(
    train_instances: list[PredictionInstance],
    eval_instances: list[PredictionInstance],
) -> list[Prediction]:
    counts = Counter(instance.question.gold_direction for instance in train_instances)
    majority = counts.most_common(1)[0][0] if counts else "positive"
    confidence = counts[majority] / sum(counts.values()) if counts else 0.25
    return [
        Prediction(
            question_id=instance.question.question_id,
            predicted_direction=majority,
            predicted_strength="unknown",
            confidence=confidence,
            supporting_paper_ids=(),
            rationale="Majority class from the training split.",
            method="majority",
        )
        for instance in eval_instances
    ]


def random_baseline(
    instances: list[PredictionInstance],
    seed: int = 7,
) -> list[Prediction]:
    rng = random.Random(seed)
    directions: tuple[Direction, ...] = ("positive", "negative", "null", "mixed")
    return [
        Prediction(
            question_id=instance.question.question_id,
            predicted_direction=rng.choice(directions),
            predicted_strength="unknown",
            confidence=0.25,
            supporting_paper_ids=(),
            rationale=f"Uniform random draw with seed {seed}.",
            method="random",
        )
        for instance in instances
    ]


def nearest_prior_paper_baseline(
    instances: list[PredictionInstance],
    corpus: list[Paper],
    access_mode: str = "preprint_aware",
) -> list[Prediction]:
    predictions: list[Prediction] = []
    for instance in instances:
        allowed = allowed_prior_papers(instance, corpus, access_mode=access_mode)
        if not allowed:
            predictions.append(_fallback_prediction(instance, "nearest_prior", "No allowed prior papers."))
            continue
        top = TfidfRetriever(allowed).search(instance.question, k=1)[0]
        direction = infer_direction_from_paper(instance.question, top.paper) or "mixed"
        predictions.append(
            Prediction(
                question_id=instance.question.question_id,
                predicted_direction=direction,
                predicted_strength="unknown",
                confidence=max(0.25, min(0.95, top.score)),
                supporting_paper_ids=(top.paper.paper_id,),
                rationale=f"Copied direction from nearest prior paper {top.paper.paper_id}.",
                method="nearest_prior",
            )
        )
    return predictions


def evidence_voting_baseline(
    instances: list[PredictionInstance],
    corpus: list[Paper],
    access_mode: str = "preprint_aware",
    k: int = 5,
    weighted: bool = False,
) -> list[Prediction]:
    predictions: list[Prediction] = []
    for instance in instances:
        allowed = allowed_prior_papers(instance, corpus, access_mode=access_mode)
        if not allowed:
            method = "weighted_evidence_vote" if weighted else "evidence_vote"
            predictions.append(_fallback_prediction(instance, method, "No allowed prior papers."))
            continue
        results = TfidfRetriever(allowed).search(instance.question, k=k)
        votes: defaultdict[str, float] = defaultdict(float)
        supporting_ids: list[str] = []
        for result in results:
            direction = infer_direction_from_paper(instance.question, result.paper)
            if direction is None:
                continue
            votes[direction] += result.score if weighted else 1.0
            supporting_ids.append(result.paper.paper_id)
        if not votes:
            method = "weighted_evidence_vote" if weighted else "evidence_vote"
            predictions.append(_fallback_prediction(instance, method, "Retrieved papers had no structured findings."))
            continue
        predicted_direction, score = sorted(votes.items(), key=lambda item: (-item[1], item[0]))[0]
        total = sum(votes.values())
        predictions.append(
            Prediction(
                question_id=instance.question.question_id,
                predicted_direction=predicted_direction,
                predicted_strength="unknown",
                confidence=max(0.25, min(0.95, score / total if total else 0.25)),
                supporting_paper_ids=tuple(supporting_ids),
                rationale=f"Direction selected by {'weighted' if weighted else 'unweighted'} vote over retrieved prior evidence.",
                method="weighted_evidence_vote" if weighted else "evidence_vote",
            )
        )
    return predictions


def _fallback_prediction(instance: PredictionInstance, method: str, reason: str) -> Prediction:
    return Prediction(
        question_id=instance.question.question_id,
        predicted_direction="mixed",
        predicted_strength="unknown",
        confidence=0.25,
        supporting_paper_ids=(),
        rationale=reason,
        method=method,
    )
