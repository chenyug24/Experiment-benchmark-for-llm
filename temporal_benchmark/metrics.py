from __future__ import annotations

from collections import Counter

from .schema import Prediction, PredictionInstance


def align_predictions(
    instances: list[PredictionInstance],
    predictions: list[Prediction],
) -> list[tuple[PredictionInstance, Prediction]]:
    by_question_id = {prediction.question_id: prediction for prediction in predictions}
    aligned: list[tuple[PredictionInstance, Prediction]] = []
    missing: list[str] = []
    for instance in instances:
        prediction = by_question_id.get(instance.question.question_id)
        if prediction is None:
            missing.append(instance.question.question_id)
        else:
            aligned.append((instance, prediction))
    if missing:
        raise ValueError(f"Missing predictions for question ids: {', '.join(missing)}")
    return aligned


def direction_accuracy(instances: list[PredictionInstance], predictions: list[Prediction]) -> float:
    aligned = align_predictions(instances, predictions)
    if not aligned:
        return 0.0
    correct = sum(
        instance.question.gold_direction == prediction.predicted_direction
        for instance, prediction in aligned
    )
    return correct / len(aligned)


def relation_accuracy(instances: list[PredictionInstance], predictions: list[Prediction]) -> float:
    aligned = align_predictions(instances, predictions)
    if not aligned:
        return 0.0
    correct = sum(
        instance.question.relation_exists == prediction.relation_exists
        for instance, prediction in aligned
    )
    return correct / len(aligned)


def strength_accuracy(instances: list[PredictionInstance], predictions: list[Prediction]) -> float:
    aligned = [
        pair
        for pair in align_predictions(instances, predictions)
        if pair[0].question.gold_strength != "unknown"
    ]
    if not aligned:
        return 0.0
    correct = sum(
        instance.question.gold_strength == prediction.predicted_strength
        for instance, prediction in aligned
    )
    return correct / len(aligned)


def macro_f1(instances: list[PredictionInstance], predictions: list[Prediction]) -> float:
    aligned = align_predictions(instances, predictions)
    labels = ("positive", "negative", "null", "mixed")
    f1_scores: list[float] = []
    for label in labels:
        tp = sum(
            instance.question.gold_direction == label and prediction.predicted_direction == label
            for instance, prediction in aligned
        )
        fp = sum(
            instance.question.gold_direction != label and prediction.predicted_direction == label
            for instance, prediction in aligned
        )
        fn = sum(
            instance.question.gold_direction == label and prediction.predicted_direction != label
            for instance, prediction in aligned
        )
        if tp == 0 and fp == 0 and fn == 0:
            f1_scores.append(0.0)
            continue
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1_scores.append(2 * precision * recall / (precision + recall) if precision + recall else 0.0)
    return sum(f1_scores) / len(f1_scores)


def expected_calibration_error(
    instances: list[PredictionInstance],
    predictions: list[Prediction],
    bins: int = 10,
) -> float:
    aligned = align_predictions(instances, predictions)
    if not aligned:
        return 0.0
    buckets: list[list[float]] = [[] for _ in range(bins)]
    accuracies: list[list[float]] = [[] for _ in range(bins)]
    for instance, prediction in aligned:
        confidence = min(1.0, max(0.0, prediction.confidence))
        bucket_index = min(bins - 1, int(confidence * bins))
        buckets[bucket_index].append(confidence)
        accuracies[bucket_index].append(
            1.0 if instance.question.gold_direction == prediction.predicted_direction else 0.0
        )
    total = len(aligned)
    ece = 0.0
    for bucket_confidences, bucket_accuracies in zip(buckets, accuracies):
        if not bucket_confidences:
            continue
        avg_confidence = sum(bucket_confidences) / len(bucket_confidences)
        avg_accuracy = sum(bucket_accuracies) / len(bucket_accuracies)
        ece += (len(bucket_confidences) / total) * abs(avg_accuracy - avg_confidence)
    return ece


def evidence_recall(instances: list[PredictionInstance], predictions: list[Prediction]) -> float:
    aligned = [
        pair
        for pair in align_predictions(instances, predictions)
        if pair[0].question.gold_evidence_paper_ids
    ]
    if not aligned:
        return 0.0
    recalls: list[float] = []
    for instance, prediction in aligned:
        gold = set(instance.question.gold_evidence_paper_ids)
        predicted = set(prediction.supporting_paper_ids)
        recalls.append(len(gold & predicted) / len(gold))
    return sum(recalls) / len(recalls)


def label_distribution(instances: list[PredictionInstance]) -> dict[str, int]:
    return dict(Counter(instance.question.gold_direction for instance in instances))


def metric_report(instances: list[PredictionInstance], predictions: list[Prediction]) -> dict[str, float | dict[str, int]]:
    return {
        "n": len(instances),
        "label_distribution": label_distribution(instances),
        "direction_accuracy": direction_accuracy(instances, predictions),
        "macro_f1": macro_f1(instances, predictions),
        "relation_accuracy": relation_accuracy(instances, predictions),
        "strength_accuracy": strength_accuracy(instances, predictions),
        "expected_calibration_error": expected_calibration_error(instances, predictions),
        "evidence_recall": evidence_recall(instances, predictions),
    }
