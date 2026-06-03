from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import TypeVar

from .schema import Paper, Prediction, PredictionInstance

T = TypeVar("T")


def read_jsonl(path: str | Path) -> list[dict]:
    records: list[dict] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                records.append(json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return records


def write_jsonl(path: str | Path, records: Iterable[dict]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def load_records(path: str | Path, parser: Callable[[dict], T]) -> list[T]:
    return [parser(record) for record in read_jsonl(path)]


def load_corpus(path: str | Path) -> list[Paper]:
    return load_records(path, Paper.from_dict)


def load_instances(path: str | Path) -> list[PredictionInstance]:
    return load_records(path, PredictionInstance.from_dict)


def load_predictions(path: str | Path) -> list[Prediction]:
    return load_records(path, Prediction.from_dict)


def write_predictions(path: str | Path, predictions: Iterable[Prediction]) -> None:
    write_jsonl(path, (prediction.to_dict() for prediction in predictions))
