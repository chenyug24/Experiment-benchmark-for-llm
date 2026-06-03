import unittest

from temporal_benchmark.baselines import evidence_voting_baseline, majority_baseline, nearest_prior_paper_baseline
from temporal_benchmark.metrics import direction_accuracy, evidence_recall, macro_f1
from temporal_benchmark.schema import Paper, PredictionInstance


def _instance(gold_direction="positive"):
    return PredictionInstance.from_dict(
        {
            "instance_id": "i1",
            "target_paper": {
                "paper_id": "target",
                "title": "Target paper",
                "release_dates": {"journal_online": "2024-01-01"},
                "buffer_days": 90,
                "reference_ids": ["p1"],
            },
            "question": {
                "question_id": "q1",
                "target_paper_id": "target",
                "entity_1": "treatment X",
                "relation": "improves",
                "entity_2": "outcome Y",
                "context": "adult trial",
                "gold_direction": gold_direction,
                "gold_strength": "moderate",
                "gold_evidence_paper_ids": ["p1"],
            },
        }
    )


def _corpus():
    return [
        Paper.from_dict(
            {
                "paper_id": "p1",
                "title": "Treatment X improves outcome Y",
                "abstract": "Prior adult trial evidence suggested treatment X improved outcome Y.",
                "release_dates": {"journal_online": "2020-01-01"},
                "paper_type": "peer_reviewed",
                "findings": [
                    {
                        "entity_1": "treatment X",
                        "relation": "improves",
                        "entity_2": "outcome Y",
                        "context": "adult trial",
                        "direction": "positive",
                        "strength": "moderate",
                    }
                ],
            }
        )
    ]


class BaselineMetricTests(unittest.TestCase):
    def test_majority_baseline_predicts_training_majority(self):
        train = [_instance("negative"), _instance("negative"), _instance("positive")]
        eval_instances = [_instance("negative")]

        predictions = majority_baseline(train, eval_instances)

        self.assertEqual(predictions[0].predicted_direction, "negative")
        self.assertEqual(direction_accuracy(eval_instances, predictions), 1.0)


    def test_nearest_prior_baseline_copies_nearest_finding(self):
        instances = [_instance("positive")]

        predictions = nearest_prior_paper_baseline(instances, _corpus())

        self.assertEqual(predictions[0].predicted_direction, "positive")
        self.assertEqual(predictions[0].supporting_paper_ids, ("p1",))
        self.assertEqual(direction_accuracy(instances, predictions), 1.0)
        self.assertEqual(evidence_recall(instances, predictions), 1.0)


    def test_voting_baseline_and_macro_f1(self):
        instances = [_instance("positive")]

        predictions = evidence_voting_baseline(instances, _corpus(), k=1)

        self.assertEqual(predictions[0].predicted_direction, "positive")
        self.assertEqual(macro_f1(instances, predictions), 0.25)


if __name__ == "__main__":
    unittest.main()
