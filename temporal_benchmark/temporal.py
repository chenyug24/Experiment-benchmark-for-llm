from __future__ import annotations

from datetime import date, datetime, timedelta

from .schema import AccessMode, Paper, PredictionInstance, ReleaseDates, VALID_ACCESS_MODES


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError(f"Dates must use YYYY-MM-DD format: {value}") from exc


def earliest_public_date(release_dates: ReleaseDates) -> date:
    candidates = [
        parse_date(release_dates.journal_online),
        parse_date(release_dates.doi_registered),
        parse_date(release_dates.indexed),
        parse_date(release_dates.preprint_first_posted),
        parse_date(release_dates.conference_release),
    ]
    valid = [candidate for candidate in candidates if candidate is not None]
    if not valid:
        raise ValueError("At least one public release date is required.")
    return min(valid)


def cutoff_date(release_dates: ReleaseDates, buffer_days: int = 90) -> date:
    return earliest_public_date(release_dates) - timedelta(days=buffer_days)


def is_available_before(paper: Paper, cutoff: date) -> bool:
    return earliest_public_date(paper.release_dates) <= cutoff


def allowed_prior_papers(
    instance: PredictionInstance,
    corpus: list[Paper],
    access_mode: AccessMode = "preprint_aware",
) -> list[Paper]:
    if access_mode not in VALID_ACCESS_MODES:
        raise ValueError(f"Unknown access mode: {access_mode}")

    cutoff = cutoff_date(instance.target_paper.release_dates, instance.target_paper.buffer_days)
    reference_ids = set(instance.target_paper.reference_ids)
    allowed: list[Paper] = []
    for paper in corpus:
        if paper.paper_id == instance.target_paper.paper_id:
            continue
        if not is_available_before(paper, cutoff):
            continue
        if access_mode == "strict" and paper.paper_type != "peer_reviewed":
            continue
        if access_mode == "reference_only" and paper.paper_id not in reference_ids:
            continue
        allowed.append(paper)
    return allowed


def leakage_flags(instance: PredictionInstance, corpus: list[Paper]) -> list[str]:
    """Return human-readable leakage warnings for one benchmark instance."""

    flags: list[str] = []
    cutoff = cutoff_date(instance.target_paper.release_dates, instance.target_paper.buffer_days)
    target_id = instance.target_paper.paper_id
    target_title = instance.target_paper.title.lower()
    for paper in corpus:
        try:
            public_date = earliest_public_date(paper.release_dates)
        except ValueError:
            flags.append(f"{paper.paper_id}: missing public date")
            continue
        if paper.paper_id == target_id:
            flags.append(f"{paper.paper_id}: target paper appears in prior corpus")
        if public_date > cutoff:
            flags.append(f"{paper.paper_id}: post-cutoff paper in candidate corpus ({public_date})")
        if target_id in paper.cited_paper_ids:
            flags.append(f"{paper.paper_id}: cites target paper")
        searchable_text = f"{paper.title}\n{paper.abstract}".lower()
        if target_title and target_title in searchable_text:
            flags.append(f"{paper.paper_id}: mentions target paper title")
    return flags
