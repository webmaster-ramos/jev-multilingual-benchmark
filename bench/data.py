"""Datasets: JSONL items plus the locale table."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from bench.config import DATA_DIR


def load_items(dataset: str, task: str) -> list[dict]:
    path = DATA_DIR / task / f"{dataset}.jsonl"
    if not path.exists():
        return []
    items = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line and not line.startswith("#"):
                items.append(json.loads(line))
    return items


def load_languages() -> dict:
    with (DATA_DIR / "languages.yml").open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
