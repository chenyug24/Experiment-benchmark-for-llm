import unittest

from temporal_benchmark.schema import Paper, PredictionInstance
from temporal_benchmark.search_gate import evaluate_search_candidate, gate_search_results


class SearchGateTests(unittest.TestCase):
    def test_gate_rejects_leaky_candidates_and_keeps_valid_prior(self):
        instance = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Distinct Target Title",
                    "release_dates": {"journal_online": "2024-06-01"},
                    "buffer_days": 90,
                    "reference_ids": ["valid"],
                },
                "question": {
                    "question_id": "q1",
                    "target_paper_id": "target",
                    "entity_1": "X",
                    "relation": "affects",
                    "entity_2": "Y",
                    "gold_direction": "positive",
                },
            }
        )
        candidates = [
            Paper.from_dict(
                {
                    "paper_id": "valid",
                    "title": "Earlier relevant paper",
                    "release_dates": {"journal_online": "2023-01-01"},
                    "paper_type": "peer_reviewed",
                }
            ),
            Paper.from_dict(
                {
                    "paper_id": "target",
                    "title": "Distinct Target Title",
                    "release_dates": {"journal_online": "2024-06-01"},
                    "paper_type": "peer_reviewed",
                }
            ),
            Paper.from_dict(
                {
                    "paper_id": "late",
                    "title": "Late follow-up",
                    "abstract": "This paper discusses Distinct Target Title.",
                    "release_dates": {"journal_online": "2024-05-01"},
                    "cited_paper_ids": ["target"],
                    "paper_type": "peer_reviewed",
                }
            ),
        ]

        allowed, audit = gate_search_results([instance], candidates)

        self.assertEqual([paper.paper_id for paper in allowed], ["valid"])
        self.assertEqual(len(audit), 3)
        rejected_reasons = {
            record.candidate_paper_id: set(record.reasons)
            for record in audit
            if record.decision == "rejected"
        }
        self.assertIn("is_target_paper", rejected_reasons["target"])
        self.assertIn("post_cutoff:2024-05-01", rejected_reasons["late"])
        self.assertIn("cites_target_paper", rejected_reasons["late"])
        self.assertIn("mentions_target_title", rejected_reasons["late"])

    def test_strict_mode_uses_peer_reviewed_public_date_not_preprint_date(self):
        instance = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Target",
                    "release_dates": {"journal_online": "2024-06-01"},
                    "buffer_days": 90,
                },
                "question": {
                    "question_id": "q1",
                    "target_paper_id": "target",
                    "entity_1": "X",
                    "relation": "affects",
                    "entity_2": "Y",
                    "gold_direction": "positive",
                },
            }
        )
        candidate = Paper.from_dict(
            {
                "paper_id": "candidate",
                "title": "Candidate",
                "release_dates": {
                    "preprint_first_posted": "2023-01-01",
                    "journal_online": "2024-05-01",
                },
                "paper_type": "peer_reviewed",
            }
        )

        decision, reasons, public_date = evaluate_search_candidate(instance, candidate, "strict")

        self.assertEqual(decision, "rejected")
        self.assertEqual(public_date.isoformat(), "2024-05-01")
        self.assertIn("post_cutoff:2024-05-01", reasons)

    def test_candidate_metadata_can_scope_search_results_to_one_question(self):
        instance_a = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Target",
                    "release_dates": {"journal_online": "2024-06-01"},
                    "buffer_days": 90,
                },
                "question": {
                    "question_id": "q1",
                    "target_paper_id": "target",
                    "entity_1": "X",
                    "relation": "affects",
                    "entity_2": "Y",
                    "gold_direction": "positive",
                },
            }
        )
        instance_b = PredictionInstance.from_dict(
            {
                "instance_id": "i2",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Target",
                    "release_dates": {"journal_online": "2024-06-01"},
                    "buffer_days": 90,
                },
                "question": {
                    "question_id": "q2",
                    "target_paper_id": "target",
                    "entity_1": "A",
                    "relation": "affects",
                    "entity_2": "B",
                    "gold_direction": "null",
                },
            }
        )
        candidate = Paper.from_dict(
            {
                "paper_id": "candidate",
                "title": "Candidate",
                "release_dates": {"journal_online": "2023-01-01"},
                "metadata": {"question_ids": ["q2"]},
            }
        )

        allowed, audit = gate_search_results([instance_a, instance_b], [candidate])

        self.assertEqual([paper.paper_id for paper in allowed], ["candidate"])
        self.assertEqual([record.question_id for record in audit], ["q2"])


if __name__ == "__main__":
    unittest.main()
