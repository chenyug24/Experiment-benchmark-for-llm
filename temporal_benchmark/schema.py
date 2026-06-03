from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Direction = Literal["positive", "negative", "null", "mixed"]
Strength = Literal["weak", "moderate", "strong", "unknown"]
AccessMode = Literal["strict", "preprint_aware", "reference_only"]
PaperType = Literal["peer_reviewed", "preprint", "conference", "other"]

VALID_DIRECTIONS = {"positive", "negative", "null", "mixed"}
VALID_STRENGTHS = {"weak", "moderate", "strong", "unknown"}
VALID_ACCESS_MODES = {"strict", "preprint_aware", "reference_only"}


@dataclass(frozen=True)
class ReleaseDates:
    """Public timestamps used to compute a conservative cutoff date."""

    journal_online: str | None = None
    doi_registered: str | None = None
    indexed: str | None = None
    preprint_first_posted: str | None = None
    conference_release: str | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any] | None) -> "ReleaseDates":
        value = value or {}
        return cls(
            journal_online=value.get("journal_online"),
            doi_registered=value.get("doi_registered"),
            indexed=value.get("indexed"),
            preprint_first_posted=value.get("preprint_first_posted"),
            conference_release=value.get("conference_release"),
        )

    def to_dict(self) -> dict[str, str | None]:
        return {
            "journal_online": self.journal_online,
            "doi_registered": self.doi_registered,
            "indexed": self.indexed,
            "preprint_first_posted": self.preprint_first_posted,
            "conference_release": self.conference_release,
        }


@dataclass(frozen=True)
class Finding:
    entity_1: str
    relation: str
    entity_2: str
    context: str
    direction: Direction
    strength: Strength = "unknown"

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Finding":
        direction = value["direction"]
        strength = value.get("strength", "unknown")
        if direction not in VALID_DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")
        if strength not in VALID_STRENGTHS:
            raise ValueError(f"Invalid strength: {strength}")
        return cls(
            entity_1=value["entity_1"],
            relation=value["relation"],
            entity_2=value["entity_2"],
            context=value.get("context", ""),
            direction=direction,
            strength=strength,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "entity_1": self.entity_1,
            "relation": self.relation,
            "entity_2": self.entity_2,
            "context": self.context,
            "direction": self.direction,
            "strength": self.strength,
        }


@dataclass(frozen=True)
class Paper:
    paper_id: str
    title: str
    abstract: str
    release_dates: ReleaseDates
    paper_type: PaperType = "peer_reviewed"
    cited_paper_ids: tuple[str, ...] = ()
    findings: tuple[Finding, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Paper":
        return cls(
            paper_id=value["paper_id"],
            title=value["title"],
            abstract=value.get("abstract", ""),
            release_dates=ReleaseDates.from_dict(value.get("release_dates")),
            paper_type=value.get("paper_type", "peer_reviewed"),
            cited_paper_ids=tuple(value.get("cited_paper_ids", [])),
            findings=tuple(Finding.from_dict(item) for item in value.get("findings", [])),
            metadata=value.get("metadata", {}),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "paper_id": self.paper_id,
            "title": self.title,
            "abstract": self.abstract,
            "release_dates": self.release_dates.to_dict(),
            "paper_type": self.paper_type,
            "cited_paper_ids": list(self.cited_paper_ids),
            "findings": [finding.to_dict() for finding in self.findings],
            "metadata": self.metadata,
        }

    @property
    def text_for_retrieval(self) -> str:
        finding_text = " ".join(
            f"{finding.entity_1} {finding.relation} {finding.entity_2} "
            f"{finding.context} {finding.direction} {finding.strength}"
            for finding in self.findings
        )
        return f"{self.title}\n{self.abstract}\n{finding_text}".strip()


@dataclass(frozen=True)
class PredictionQuestion:
    question_id: str
    target_paper_id: str
    entity_1: str
    relation: str
    entity_2: str
    context: str
    answer_choices: tuple[Direction, ...] = ("positive", "negative", "null", "mixed")
    gold_direction: Direction = "mixed"
    gold_strength: Strength = "unknown"
    relation_exists: bool = True
    gold_evidence_paper_ids: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "PredictionQuestion":
        gold_direction = value["gold_direction"]
        gold_strength = value.get("gold_strength", "unknown")
        if gold_direction not in VALID_DIRECTIONS:
            raise ValueError(f"Invalid gold direction: {gold_direction}")
        if gold_strength not in VALID_STRENGTHS:
            raise ValueError(f"Invalid gold strength: {gold_strength}")
        return cls(
            question_id=value["question_id"],
            target_paper_id=value["target_paper_id"],
            entity_1=value["entity_1"],
            relation=value["relation"],
            entity_2=value["entity_2"],
            context=value.get("context", ""),
            answer_choices=tuple(value.get("answer_choices", ["positive", "negative", "null", "mixed"])),
            gold_direction=gold_direction,
            gold_strength=gold_strength,
            relation_exists=value.get("relation_exists", True),
            gold_evidence_paper_ids=tuple(value.get("gold_evidence_paper_ids", [])),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "target_paper_id": self.target_paper_id,
            "entity_1": self.entity_1,
            "relation": self.relation,
            "entity_2": self.entity_2,
            "context": self.context,
            "answer_choices": list(self.answer_choices),
            "gold_direction": self.gold_direction,
            "gold_strength": self.gold_strength,
            "relation_exists": self.relation_exists,
            "gold_evidence_paper_ids": list(self.gold_evidence_paper_ids),
        }

    @property
    def text_for_retrieval(self) -> str:
        return f"{self.entity_1} {self.relation} {self.entity_2} {self.context}".strip()

    @property
    def natural_language(self) -> str:
        return (
            f"Does {self.entity_1} {self.relation} {self.entity_2} "
            f"in the following context: {self.context}?"
        )


@dataclass(frozen=True)
class TargetPaper:
    paper_id: str
    title: str
    release_dates: ReleaseDates
    reference_ids: tuple[str, ...] = ()
    buffer_days: int = 90
    domain: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "TargetPaper":
        return cls(
            paper_id=value["paper_id"],
            title=value["title"],
            release_dates=ReleaseDates.from_dict(value.get("release_dates")),
            reference_ids=tuple(value.get("reference_ids", [])),
            buffer_days=int(value.get("buffer_days", 90)),
            domain=value.get("domain", "unknown"),
            metadata=value.get("metadata", {}),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "paper_id": self.paper_id,
            "title": self.title,
            "release_dates": self.release_dates.to_dict(),
            "reference_ids": list(self.reference_ids),
            "buffer_days": self.buffer_days,
            "domain": self.domain,
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class PredictionInstance:
    instance_id: str
    target_paper: TargetPaper
    question: PredictionQuestion

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "PredictionInstance":
        return cls(
            instance_id=value["instance_id"],
            target_paper=TargetPaper.from_dict(value["target_paper"]),
            question=PredictionQuestion.from_dict(value["question"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "instance_id": self.instance_id,
            "target_paper": self.target_paper.to_dict(),
            "question": self.question.to_dict(),
        }


@dataclass(frozen=True)
class Prediction:
    question_id: str
    predicted_direction: Direction
    predicted_strength: Strength = "unknown"
    relation_exists: bool = True
    confidence: float = 0.5
    supporting_paper_ids: tuple[str, ...] = ()
    rationale: str = ""
    method: str = "unknown"

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Prediction":
        predicted_direction = value["predicted_direction"]
        predicted_strength = value.get("predicted_strength", "unknown")
        if predicted_direction not in VALID_DIRECTIONS:
            raise ValueError(f"Invalid predicted direction: {predicted_direction}")
        if predicted_strength not in VALID_STRENGTHS:
            raise ValueError(f"Invalid predicted strength: {predicted_strength}")
        confidence = float(value.get("confidence", 0.5))
        if confidence < 0 or confidence > 1:
            raise ValueError(f"Confidence must be in [0, 1]: {confidence}")
        return cls(
            question_id=value["question_id"],
            predicted_direction=predicted_direction,
            predicted_strength=predicted_strength,
            relation_exists=value.get("relation_exists", True),
            confidence=confidence,
            supporting_paper_ids=tuple(value.get("supporting_paper_ids", [])),
            rationale=value.get("rationale", ""),
            method=value.get("method", "unknown"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "predicted_direction": self.predicted_direction,
            "predicted_strength": self.predicted_strength,
            "relation_exists": self.relation_exists,
            "confidence": self.confidence,
            "supporting_paper_ids": list(self.supporting_paper_ids),
            "rationale": self.rationale,
            "method": self.method,
        }
