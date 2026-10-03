"""Blind review of the dataset by a second agent.

    uv run python -m bench.review export                    # names round -> review/package/
    uv run python -m bench.review compare                   # -> review/report.md + status.jsonl
    uv run python -m bench.review export --round=comments   # -> review/package-comments/
    uv run python -m bench.review compare --round=comments  # -> report-comments.md + status

Export takes every item of the `full`, `clean` and `lexicon` datasets, each once. The package
folder is what the reviewer gets. The key stays outside it.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

from bench.config import ROOT
from bench.data import load_items, write_jsonl
from bench.score import LANG_NAMES

REVIEW_DIR = ROOT / "review"
SALT = "jev-multilingual-benchmark/review/v1"

# A round is one package handed to the reviewer. Each has its own items, key and status.
ROUNDS: dict[str, dict] = {
    "names": {"datasets": ("full", "clean", "lexicon"), "package": "package",
              "key": "key.jsonl", "status": "status.jsonl", "report": "report.md"},
    "comments": {"datasets": ("comments",), "package": "package-comments",
                 "key": "key-comments.jsonl", "status": "status-comments.jsonl",
                 "report": "report-comments.md"},
}
ROUND = ROUNDS["names"]
PACKAGE_DIR = REVIEW_DIR / ROUND["package"]
KEY_PATH = REVIEW_DIR / ROUND["key"]
STATUS_PATH = REVIEW_DIR / ROUND["status"]


def set_round(name: str) -> None:
    global ROUND, PACKAGE_DIR, KEY_PATH, STATUS_PATH  # noqa: PLW0603 - module-level paths
    ROUND = ROUNDS[name]
    PACKAGE_DIR = REVIEW_DIR / ROUND["package"]
    KEY_PATH = REVIEW_DIR / ROUND["key"]
    STATUS_PATH = REVIEW_DIR / ROUND["status"]


def rid_for(item_id: str) -> str:
    return "r-" + hashlib.sha1(f"{SALT}:{item_id}".encode()).hexdigest()[:10]


def all_items() -> list[dict]:
    """Every built item of the round once."""
    seen: dict[str, dict] = {}
    for dataset in ROUND["datasets"]:
        for task in ("short", "long"):
            for item in load_items(dataset, task):
                seen.setdefault(item["id"], item)
    return list(seen.values())


def export() -> None:
    items = all_items()
    if not items:
        sys.exit("no built dataset; run bench.build (and bench.build --clean) first")
    by_lang: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        by_lang[item["lang"]].append(item)
    key_rows, all_rows = [], []
    items_dir = PACKAGE_DIR / "items"
    for lang, lang_items in by_lang.items():
        shuffled = list(lang_items)
        random.Random(f"{SALT}:{lang}").shuffle(shuffled)
        rows = []
        for item in shuffled:
            rid = rid_for(item["id"])
            rows.append({"rid": rid, "lang": lang, "language": LANG_NAMES[lang],
                         "task": item["task"], "text": item["text"]})
            key_rows.append({"rid": rid, "id": item["id"]})
        write_jsonl(items_dir / f"{lang}.jsonl", rows)
        all_rows += rows
    write_jsonl(PACKAGE_DIR / "items-all.jsonl", all_rows)
    write_jsonl(KEY_PATH, key_rows)
    (PACKAGE_DIR / "verdicts").mkdir(parents=True, exist_ok=True)
    base = REVIEW_DIR / "package"
    if base != PACKAGE_DIR:
        for name in ("PROMPT.md", "check_verdicts.py"):
            (PACKAGE_DIR / name).write_text((base / name).read_text(encoding="utf-8"),
                                            encoding="utf-8")
    print(f"exported {len(all_rows)} items in {len(by_lang)} languages -> {items_dir}")


def _read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                rows.append({"_broken": line[:80]})
    return rows


def _load_checker():
    """The package's own checker, so compare and the reviewer apply the same rules."""
    path = PACKAGE_DIR / "check_verdicts.py"
    if not path.exists():  # every round ships the same prompt and checker
        path = REVIEW_DIR / "package" / "check_verdicts.py"
    spec = importlib.util.spec_from_file_location("check_verdicts", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Every reason that keeps an item from being verified, in the order it decides the status.
BLOCKERS = ("missing", "invalid", "abstained", "disputed", "wrong_language", "language_unknown",
            "policy_ambiguous", "label_unsure", "reading_low", "garbled")


def assess(item: dict, verdict: dict | None, checker) -> tuple[list[str], list[str]]:
    """Return (blockers, notes) for one item. No blockers means the item is verified."""
    if verdict is None:
        return ["missing"], []
    row_problems = checker.check_row(verdict)
    if row_problems:
        return ["invalid"], [f"verdict row is malformed: {'; '.join(row_problems)}"]
    if verdict["label"] is None:
        return ["abstained"], []
    blockers, notes = [], []
    if verdict["label"] != item["label"]:
        blockers.append("disputed")
        notes.append(f"label: intended {item['label']}, reviewer {verdict['label']}")
    if verdict["language_ok"] is False:
        blockers.append("wrong_language")
        notes.append("reviewer says this is not the stated language")
    elif verdict["language_ok"] is not True:
        blockers.append("language_unknown")
        notes.append("reviewer could not tell whether this is the stated language")
    if verdict["policy_ambiguous"] is True:
        blockers.append("policy_ambiguous")
        notes.append("reviewer says the policy does not settle this item")
    if verdict["label_confidence"] == "low":
        blockers.append("label_unsure")
        notes.append("reviewer is unsure of the label under the policy")
    if verdict["reading_confidence"] == "low":
        blockers.append("reading_low")
        notes.append("reviewer reads this item poorly")
    if verdict["natural"] == 1:
        blockers.append("garbled")
        notes.append("naturalness 1/3")
    elif verdict["natural"] == 2:
        notes.append("naturalness 2/3")
    if verdict["issue"]:
        notes.append(f"issue: {verdict['issue']}")
    return blockers, notes


def compare() -> None:
    checker = _load_checker()
    items = {i["id"]: i for i in all_items()}
    key = {row["rid"]: row["id"] for row in _read_jsonl(KEY_PATH)}
    verdicts: dict[str, dict] = {}
    stray = 0
    for path in sorted((PACKAGE_DIR / "verdicts").glob("*.jsonl")):
        for row in _read_jsonl(path):
            rid = row.get("rid")
            if "_broken" in row or not isinstance(rid, str) or rid not in key:
                stray += 1
                continue
            verdicts[key[rid]] = row

    per_lang: dict[str, dict] = defaultdict(lambda: defaultdict(int))
    status_rows, listed = [], []
    for item_id, item in items.items():
        verdict = verdicts.get(item_id)
        blockers, notes = assess(item, verdict, checker)
        status = blockers[0] if blockers else "verified"
        stats = per_lang[item["lang"]]
        stats["items"] += 1
        stats[status] += 1
        if verdict and not blockers:
            categories = [verdict["category"], *verdict["other_categories"]]
            if item["label"] == "flag" and item["category"] not in categories:
                stats["category_differs"] += 1
            if verdict["reading_confidence"] == "medium":
                stats["reading_medium"] += 1
        status_rows.append({"id": item_id, "status": status, "blockers": blockers})
        if notes:
            listed.append((item_id, item, verdict, status, notes))

    columns = ["verified", *BLOCKERS]
    totals = {c: sum(stats[c] for stats in per_lang.values()) for c in columns}
    lines = ["# Blind review report", "",
             f"{len(items)} items, {len(verdicts)} verdict rows matched, {stray} stray rows.", "",
             "An item is **verified** only if it was judged (not abstained), the label agrees, the",
             "reviewer confirms the stated language, reads it with high or medium",
             "confidence, is not unsure of the label, does not find the policy ambiguous on it,",
             "and does not find it garbled. Everything else carries the first reason that",
             "applies, in the column order below. Only verified items enter the analysis.", "",
             f"**Verified: {totals['verified']} of {len(items)}.**", "",
             "## Per language", "",
             "| lang | items | " + " | ".join(columns) + " | category differs | reading medium |",
             "|---|---:|" + "---:|" * (len(columns) + 2)]
    for lang, stats in per_lang.items():
        lines.append(f"| {lang} | {stats['items']} | " + " | ".join(str(stats[c]) for c in columns)
                     + f" | {stats['category_differs']} | {stats['reading_medium']} |")
    total_cells = " | ".join(str(totals[c]) for c in columns)
    lines.append(f"| all | {len(items)} | {total_cells} | | |")
    lines += ["", "`category differs` and `reading medium` are counted among verified items and do "
              "not block verification.", "", "## Items to look at", ""]
    for item_id, item, verdict, status, notes in listed:
        lines += [f"### {item_id} - {status} ({item['label']} / {item['category']} / "
                  f"{item['variant']})", "",
                  f"- text: `{item['text']}`",
                  f"- intended: {item['note']}"]
        if status != "invalid":
            lines += [f"- reviewer gloss: {verdict['gloss_en']}",
                      f"- reviewer: label {verdict['label']}, category {verdict['category']}, "
                      f"decoded {verdict['decoded']}, reading {verdict['reading_confidence']}, "
                      f"label confidence {verdict['label_confidence']}"]
        lines += [f"- {note}" for note in notes] + [""]
    report = REVIEW_DIR / ROUND["report"]
    report.write_text("\n".join(lines), encoding="utf-8")
    write_jsonl(STATUS_PATH, status_rows)
    print(f"verified {totals['verified']} of {len(items)}; {len(listed)} items to look at "
          f"-> {report}, {STATUS_PATH}")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--round")]
    for a in sys.argv[1:]:
        if a.startswith("--round="):
            set_round(a.split("=", 1)[1])
    command = args[0] if args else ""
    if command == "export":
        export()
    elif command == "compare":
        compare()
    else:
        sys.exit("usage: python -m bench.review export|compare")


if __name__ == "__main__":
    main()
