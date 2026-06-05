from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

from .schema import AccessMode, Paper, PredictionInstance, ReleaseDates, VALID_ACCESS_MODES
from .temporal import cutoff_date, earliest_public_date, parse_date


@dataclass(frozen=True)
class SearchGateAuditRecord:
    instance_id: str
    question_id: str
    target_paper_id: str
    candidate_paper_id: str
    candidate_title: str
    cutoff: str
    candidate_public_date: str | None
    access_mode: AccessMode
    decision: str
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "instance_id": self.instance_id,
            "question_id": self.question_id,
            "target_paper_id": self.target_paper_id,
            "candidate_paper_id": self.candidate_paper_id,
            "candidate_title": self.candidate_title,
            "cutoff": self.cutoff,
            "candidate_public_date": self.candidate_public_date,
            "access_mode": self.access_mode,
            "decision": self.decision,
            "reasons": list(self.reasons),
        }


def gate_search_results(
    instances: list[PredictionInstance],
    candidates: list[Paper],
    access_mode: AccessMode = "preprint_aware",
) -> tuple[list[Paper], list[SearchGateAuditRecord]]:
    """Filter agent-found candidate papers through temporal and leakage checks.

    The returned corpus is deduplicated and contains any paper that is allowed for
    at least one target instance. The audit records preserve the per-instance
    allow/reject decision so experiments remain inspectable.
    """

    if access_mode not in VALID_ACCESS_MODES:
        raise ValueError(f"Unknown access mode: {access_mode}")

    allowed_by_id: dict[str, Paper] = {}
    audit_records: list[SearchGateAuditRecord] = []
    for instance in instances:
        for candidate in candidates:
            if not _candidate_applies_to_instance(candidate, instance):
                continue
            decision, reasons, public_date = evaluate_search_candidate(instance, candidate, access_mode)
            audit_records.append(
                SearchGateAuditRecord(
                    instance_id=instance.instance_id,
                    question_id=instance.question.question_id,
                    target_paper_id=instance.target_paper.paper_id,
                    candidate_paper_id=candidate.paper_id,
                    candidate_title=candidate.title,
                    cutoff=cutoff_date(
                        instance.target_paper.release_dates,
                        instance.target_paper.buffer_days,
                    ).isoformat(),
                    candidate_public_date=_date_to_string(public_date),
                    access_mode=access_mode,
                    decision=decision,
                    reasons=tuple(reasons),
                )
            )
            if decision == "allowed":
                allowed_by_id[candidate.paper_id] = candidate
    return list(allowed_by_id.values()), audit_records


def evaluate_search_candidate(
    instance: PredictionInstance,
    candidate: Paper,
    access_mode: AccessMode = "preprint_aware",
) -> tuple[str, list[str], date | None]:
    """Return allow/reject decision, reasons, and the relevant public date."""

    if access_mode not in VALID_ACCESS_MODES:
        raise ValueError(f"Unknown access mode: {access_mode}")

    reasons: list[str] = []
    target = instance.target_paper
    cutoff = cutoff_date(target.release_dates, target.buffer_days)
    public_date = _public_date_for_access_mode(candidate, access_mode, reasons)

    if candidate.paper_id == target.paper_id:
        reasons.append("is_target_paper")
    if public_date is not None and public_date > cutoff:
        reasons.append(f"post_cutoff:{public_date.isoformat()}")
    if access_mode == "strict" and candidate.paper_type != "peer_reviewed":
        reasons.append(f"not_peer_reviewed:{candidate.paper_type}")
    if access_mode == "reference_only" and candidate.paper_id not in set(target.reference_ids):
        reasons.append("not_in_target_references")
    if target.paper_id in candidate.cited_paper_ids:
        reasons.append("cites_target_paper")

    searchable_text = f"{candidate.title}\n{candidate.abstract}".lower()
    target_title = target.title.strip().lower()
    if target_title and target_title in searchable_text:
        reasons.append("mentions_target_title")

    decision = "rejected" if reasons else "allowed"
    return decision, reasons, public_date


def _public_date_for_access_mode(
    paper: Paper,
    access_mode: AccessMode,
    reasons: list[str],
) -> date | None:
    if access_mode == "strict":
        public_date = _earliest_non_preprint_date(paper.release_dates)
        if public_date is None:
            reasons.append("missing_peer_reviewed_public_date")
        return public_date

    try:
        return earliest_public_date(paper.release_dates)
    except ValueError:
        reasons.append("missing_public_date")
        return None


def _earliest_non_preprint_date(release_dates: ReleaseDates) -> date | None:
    candidates = [
        parse_date(release_dates.journal_online),
        parse_date(release_dates.doi_registered),
        parse_date(release_dates.indexed),
        parse_date(release_dates.conference_release),
    ]
    valid = [candidate for candidate in candidates if candidate is not None]
    return min(valid) if valid else None


def _candidate_applies_to_instance(candidate: Paper, instance: PredictionInstance) -> bool:
    """Let search-result files optionally scope candidates to targets/questions."""

    metadata = candidate.metadata or {}
    if not _metadata_contains(metadata, "target_paper_ids", instance.target_paper.paper_id):
        return False
    if not _metadata_contains(metadata, "instance_ids", instance.instance_id):
        return False
    if not _metadata_contains(metadata, "question_ids", instance.question.question_id):
        return False
    return True


def _metadata_contains(metadata: dict[str, Any], key: str, value: str) -> bool:
    values = metadata.get(key)
    if values is None:
        return True
    if isinstance(values, str):
        return values == value
    return value in set(values)


def _date_to_string(value: date | None) -> str | None:
    return value.isoformat() if value is not None else None
