from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from .schema import Paper, PredictionQuestion

TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_+-]{1,}")


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_RE.finditer(text)]


@dataclass(frozen=True)
class RetrievalResult:
    paper: Paper
    score: float


class TfidfRetriever:
    """Small transparent TF-IDF retriever for reproducible baselines."""

    def __init__(self, papers: list[Paper]):
        self.papers = papers
        self._term_counts = [Counter(tokenize(paper.text_for_retrieval)) for paper in papers]
        document_frequency: Counter[str] = Counter()
        for counts in self._term_counts:
            document_frequency.update(counts.keys())
        n_docs = max(len(papers), 1)
        self._idf = {
            term: math.log((1 + n_docs) / (1 + df)) + 1.0
            for term, df in document_frequency.items()
        }
        self._vectors = [self._vectorize_counts(counts) for counts in self._term_counts]

    def _vectorize_counts(self, counts: Counter[str]) -> dict[str, float]:
        if not counts:
            return {}
        max_count = max(counts.values())
        return {
            term: (0.5 + 0.5 * count / max_count) * self._idf.get(term, 1.0)
            for term, count in counts.items()
        }

    def vectorize_query(self, text: str) -> dict[str, float]:
        return self._vectorize_counts(Counter(tokenize(text)))

    @staticmethod
    def cosine(left: dict[str, float], right: dict[str, float]) -> float:
        if not left or not right:
            return 0.0
        overlap = set(left) & set(right)
        numerator = sum(left[term] * right[term] for term in overlap)
        left_norm = math.sqrt(sum(value * value for value in left.values()))
        right_norm = math.sqrt(sum(value * value for value in right.values()))
        if left_norm == 0 or right_norm == 0:
            return 0.0
        return numerator / (left_norm * right_norm)

    def search(self, query: str | PredictionQuestion, k: int = 5) -> list[RetrievalResult]:
        query_text = query.text_for_retrieval if isinstance(query, PredictionQuestion) else query
        query_vector = self.vectorize_query(query_text)
        scored = [
            RetrievalResult(paper=paper, score=self.cosine(query_vector, vector))
            for paper, vector in zip(self.papers, self._vectors)
        ]
        scored.sort(key=lambda result: (-result.score, result.paper.paper_id))
        return scored[:k]


def finding_overlap_score(question: PredictionQuestion, finding_text: str) -> int:
    question_terms = set(tokenize(question.text_for_retrieval))
    finding_terms = set(tokenize(finding_text))
    return len(question_terms & finding_terms)


def infer_direction_from_paper(question: PredictionQuestion, paper: Paper) -> str | None:
    """Pick the most lexically aligned finding direction from a prior paper."""

    best_direction: str | None = None
    best_score = -1
    for finding in paper.findings:
        text = f"{finding.entity_1} {finding.relation} {finding.entity_2} {finding.context}"
        score = finding_overlap_score(question, text)
        if score > best_score:
            best_direction = finding.direction
            best_score = score
    if best_score <= 0:
        return None
    return best_direction
