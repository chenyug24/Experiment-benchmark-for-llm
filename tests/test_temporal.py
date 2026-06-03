import unittest
from datetime import date

from temporal_benchmark.schema import Paper, PredictionInstance
from temporal_benchmark.temporal import allowed_prior_papers, cutoff_date, earliest_public_date, leakage_flags


class TemporalTests(unittest.TestCase):
    def test_cutoff_uses_earliest_public_date_minus_buffer(self):
        instance = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Target",
                    "release_dates": {
                        "journal_online": "2024-06-01",
                        "preprint_first_posted": "2024-01-15",
                    },
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

        self.assertEqual(earliest_public_date(instance.target_paper.release_dates), date(2024, 1, 15))
        self.assertEqual(cutoff_date(instance.target_paper.release_dates, 90), date(2023, 10, 17))


    def test_allowed_prior_papers_respects_access_modes(self):
        instance = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Target",
                    "release_dates": {"journal_online": "2024-04-01"},
                    "buffer_days": 90,
                    "reference_ids": ["peer_old"],
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
        corpus = [
            Paper.from_dict(
                {
                    "paper_id": "peer_old",
                    "title": "Peer old",
                    "release_dates": {"journal_online": "2023-01-01"},
                    "paper_type": "peer_reviewed",
                }
            ),
            Paper.from_dict(
                {
                    "paper_id": "preprint_old",
                    "title": "Preprint old",
                    "release_dates": {"preprint_first_posted": "2023-01-02"},
                    "paper_type": "preprint",
                }
            ),
            Paper.from_dict(
                {
                    "paper_id": "peer_late",
                    "title": "Peer late",
                    "release_dates": {"journal_online": "2024-03-01"},
                    "paper_type": "peer_reviewed",
                }
            ),
        ]

        self.assertEqual([paper.paper_id for paper in allowed_prior_papers(instance, corpus, "strict")], ["peer_old"])
        self.assertEqual(
            [paper.paper_id for paper in allowed_prior_papers(instance, corpus, "preprint_aware")],
            ["peer_old", "preprint_old"],
        )
        self.assertEqual(
            [paper.paper_id for paper in allowed_prior_papers(instance, corpus, "reference_only")],
            ["peer_old"],
        )


    def test_leakage_flags_target_and_post_cutoff(self):
        instance = PredictionInstance.from_dict(
            {
                "instance_id": "i1",
                "target_paper": {
                    "paper_id": "target",
                    "title": "Distinct Target Title",
                    "release_dates": {"journal_online": "2024-04-01"},
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
        corpus = [
            Paper.from_dict(
                {
                    "paper_id": "target",
                    "title": "Distinct Target Title",
                    "release_dates": {"journal_online": "2024-04-01"},
                }
            ),
            Paper.from_dict(
                {
                    "paper_id": "late",
                    "title": "Late follow-up",
                    "abstract": "Cites the Distinct Target Title.",
                    "release_dates": {"journal_online": "2024-05-01"},
                    "cited_paper_ids": ["target"],
                }
            ),
        ]

        flags = leakage_flags(instance, corpus)
        self.assertTrue(any("target paper appears" in flag for flag in flags))
        self.assertTrue(any("post-cutoff" in flag for flag in flags))
        self.assertTrue(any("cites target paper" in flag for flag in flags))
        self.assertTrue(any("mentions target paper title" in flag for flag in flags))


if __name__ == "__main__":
    unittest.main()
