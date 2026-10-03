#!/usr/bin/env python3
"""Check reviewer output against the input files. Standard library only.

    python3 check_verdicts.py            # run from the package folder
    python3 check_verdicts.py <folder>   # or point it at the folder

Exit code 0 and `OK` when every verdict file is complete and well-formed. Types are checked
exactly: JSON `true` is not `1`, `3` is not `3.0`.
"""

import json
import sys
from pathlib import Path

FLAG_CATEGORIES = ("profanity", "sexual", "hate", "harassment", "violence", "self_harm", "illegal")
FIELDS = ["rid", "reading_confidence", "language_ok", "natural", "gloss_en", "label", "category",
          "other_categories", "decoded", "label_confidence", "policy_ambiguous", "issue"]
READING = ("high", "medium", "low", "none")
CONFIDENCE = ("high", "medium", "low")


def is_str(value):
    return type(value) is str


def one_of(value, allowed):
    """True only for a string that is in `allowed` - never raises on lists, dicts or numbers."""
    return is_str(value) and value in allowed


def bool_or_none(value):
    return value is None or type(value) is bool


def read_lines(path):
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            rows.append((number, line))
    return rows


def check_row(row):
    problems = []
    missing = [f for f in FIELDS if f not in row]
    if missing:
        return [f"missing fields {missing}"]
    unknown = sorted(k for k in row if k not in FIELDS)
    if unknown:
        problems.append(f"unknown fields {unknown}")

    reading, label, category = row["reading_confidence"], row["label"], row["category"]
    others, confidence, ambiguous = (row["other_categories"], row["label_confidence"],
                                     row["policy_ambiguous"])
    natural = row["natural"]

    if not one_of(reading, READING):
        problems.append(f"reading_confidence must be one of {list(READING)}, got {reading!r}")
    if not bool_or_none(row["language_ok"]):
        problems.append(f"language_ok must be true, false or null, got {row['language_ok']!r}")
    if not (natural is None or (type(natural) is int and natural in (1, 2, 3))):
        problems.append(f"natural must be the integer 1, 2 or 3, or null, got {natural!r}")
    if type(others) is not list or not all(one_of(c, FLAG_CATEGORIES) for c in others):
        problems.append(f"other_categories must be a list of flag categories, got {others!r}")
        others = []
    elif len(set(others)) != len(others):
        problems.append("other_categories has duplicates")
    if not bool_or_none(ambiguous):
        problems.append(f"policy_ambiguous must be true, false or null, got {ambiguous!r}")
    for name in ("gloss_en", "decoded", "issue"):
        if not (row[name] is None or is_str(row[name])):
            problems.append(f"{name} must be a string or null")
    has_issue = is_str(row["issue"]) and bool(row["issue"].strip())

    abstained = reading == "none" or label is None
    if abstained:
        if not (reading == "none" and label is None and category is None
                and confidence is None and ambiguous is None):
            problems.append("abstention must be all-or-nothing: reading_confidence none with "
                            "label, category, label_confidence and policy_ambiguous null")
        if others:
            problems.append("abstention with other_categories")
        if not has_issue:
            problems.append("abstention needs a reason in issue")
        return problems

    if not one_of(label, ("clean", "flag")):
        problems.append(f"label must be clean, flag or null, got {label!r}")
    if not one_of(confidence, CONFIDENCE):
        problems.append(f"label_confidence must be one of {list(CONFIDENCE)}, got {confidence!r}")
    if type(ambiguous) is not bool:
        problems.append("policy_ambiguous must be true or false on a judged item")
    if label == "clean" and (category != "none" or others):
        problems.append("clean needs category none and empty other_categories")
    if label == "flag":
        if not one_of(category, FLAG_CATEGORIES):
            problems.append(f"flag needs a category from the list, got {category!r}")
        elif category in others:
            problems.append("primary category repeated in other_categories")
    if not (is_str(row["gloss_en"]) and row["gloss_en"].strip()):
        problems.append("gloss_en is empty")
    if (reading == "low" or confidence == "low" or ambiguous is True) and not has_issue:
        problems.append("low confidence or policy_ambiguous needs a note in issue")
    return problems


def check_folder(root):
    """Return (problem count, verdicts seen, abstentions), printing problems per file."""
    item_files = sorted((root / "items").glob("*.jsonl"))
    if not item_files:
        sys.exit(f"no input files in {root / 'items'}")
    total_problems = reviewed = abstained = 0
    for item_file in item_files:
        expected = [json.loads(line)["rid"] for _, line in read_lines(item_file)]
        verdict_file = root / "verdicts" / item_file.name
        problems = []
        if not verdict_file.exists():
            problems.append("verdict file is missing")
        else:
            seen = set()
            for number, line in read_lines(verdict_file):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    problems.append(f"line {number}: invalid JSON ({exc.msg})")
                    continue
                if type(row) is not dict:
                    problems.append(f"line {number}: not a JSON object")
                    continue
                rid = row.get("rid")
                if not is_str(rid):
                    problems.append(f"line {number}: rid must be a string, got {rid!r}")
                    continue
                if rid in seen:
                    problems.append(f"line {number}: rid {rid} appears twice")
                    continue
                seen.add(rid)
                if rid not in expected:
                    problems.append(f"line {number}: rid {rid} is not in {item_file.name}")
                    continue
                for problem in check_row(row):
                    problems.append(f"line {number} ({rid}): {problem}")
                reviewed += 1
                abstained += row.get("label") is None
            for rid in expected:
                if rid not in seen:
                    problems.append(f"rid {rid} has no verdict")
        if problems:
            total_problems += len(problems)
            print(f"FAIL {item_file.name}: {len(problems)} problem(s)")
            for problem in problems[:40]:
                print(f"  - {problem}")
            if len(problems) > 40:
                print(f"  ... and {len(problems) - 40} more")
    known = {f.name for f in item_files}
    verdict_dir = root / "verdicts"
    extra = sorted(p.name for p in verdict_dir.glob("*.jsonl") if p.name not in known) \
        if verdict_dir.exists() else []
    if extra:
        total_problems += len(extra)
        print(f"FAIL unexpected verdict files: {extra}")
    return total_problems, reviewed, abstained, len(item_files)


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    problems, reviewed, abstained, files = check_folder(root)
    if problems:
        sys.exit(1)
    print(f"OK: {reviewed} verdicts in {files} files, {abstained} abstentions")


if __name__ == "__main__":
    main()
