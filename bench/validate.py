"""Validate per-language source files against data/src/SPEC.md.

    uv run python -m bench.validate data/src/de.jsonl [more files]
    uv run python -m bench.validate            # every file in data/src
    uv run python -m bench.validate --clean    # clean halves in data/src/_partial
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from bench.config import DATA_DIR
from bench.prompts import CATEGORIES

SRC_DIR = DATA_DIR / "src"
PARTIAL_DIR = SRC_DIR / "_partial"

LANG_SCRIPT = {
    "en": "Latn", "de": "Latn", "fr": "Latn", "es": "Latn", "it": "Latn", "pt": "Latn",
    "nl": "Latn", "pl": "Latn", "cs": "Latn", "hu": "Latn", "ro": "Latn", "sv": "Latn",
    "fi": "Latn", "tr": "Latn", "vi": "Latn", "id": "Latn", "el": "Grek", "ru": "Cyrl",
    "uk": "Cyrl", "ar": "Arab", "hi": "Deva", "th": "Thai", "ja": "Jpan", "ko": "Kore",
    "zh": "Hans",
}
LANG_ORDER = list(LANG_SCRIPT)
DENSE = {"ja", "zh", "ko", "th"}

SCRIPT_RANGES = {
    "Latn": r"A-Za-zÀ-ɏḀ-ỿ",
    "Grek": r"Ͱ-Ͽἀ-῿",
    "Cyrl": r"Ѐ-ԯ",
    "Arab": r"؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿",
    "Deva": r"ऀ-ॿ",
    "Thai": r"฀-๿",
    "Jpan": r"぀-ヿ一-鿿ｦ-ﾟ",
    "Kore": r"가-힯ᄀ-ᇿ㄰-㆏",
    "Hans": r"一-鿿㐀-䶿",
    "Hant": r"一-鿿㐀-䶿",
}

# (task, label, variant) -> (id code, count)
MATRIX = {
    ("short", "clean", "plain"): ("s-cp", 8),
    ("short", "clean", "tricky"): ("s-ct", 3),
    ("short", "flag", "plain"): ("s-fp", 6),
    ("short", "flag", "obfuscated"): ("s-fo", 5),
    ("short", "flag", "transliterated"): ("s-ft", 2),
    ("long", "clean", "plain"): ("l-cp", 3),
    ("long", "clean", "civil_heated"): ("l-ch", 1),
    ("long", "flag", "plain"): ("l-fp", 3),
    ("long", "flag", "embedded"): ("l-fe", 1),
}
FIELDS = ("id", "task", "lang", "script", "label", "category", "variant", "text", "note")


def script_share(text: str, script: str) -> float:
    letters = [ch for ch in text if ch.isalpha()]
    if not letters:
        return 0.0
    pattern = re.compile(f"[{SCRIPT_RANGES[script]}]")
    return sum(1 for ch in letters if pattern.match(ch)) / len(letters)


def load(path: Path) -> tuple[list[dict], list[str]]:
    items, problems = [], []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError as exc:
            problems.append(f"line {number}: invalid JSON ({exc.msg})")
    return items, problems


def validate_file(path: Path, clean_only: bool = False) -> list[str]:
    """Check one language file. `clean_only` accepts a file holding just the clean half."""
    lang = path.name.split(".")[0]
    items, problems = load(path)
    if lang not in LANG_SCRIPT:
        return [f"unknown language file name: {path.name}"]
    native = LANG_SCRIPT[lang]
    non_latin = native != "Latn"
    seen_ids: set[str] = set()
    seen_texts: set[str] = set()
    counts: Counter = Counter()

    for item in items:
        iid = item.get("id", "?")
        missing = [f for f in FIELDS if not isinstance(item.get(f), str) or not item[f].strip()]
        if missing:
            problems.append(f"{iid}: missing or empty fields {missing}")
            continue
        key = (item["task"], item["label"], item["variant"])
        if key not in MATRIX:
            problems.append(f"{iid}: task/label/variant {key} is not in the matrix")
            continue
        code = MATRIX[key][0]
        counts[key] += 1
        if not re.fullmatch(rf"{lang}-{code}-\d\d", iid):
            problems.append(f"{iid}: id should match {lang}-{code}-NN")
        if iid in seen_ids:
            problems.append(f"{iid}: duplicate id")
        seen_ids.add(iid)
        if item["text"] in seen_texts:
            problems.append(f"{iid}: duplicate text")
        seen_texts.add(item["text"])
        if item["lang"] != lang:
            problems.append(f"{iid}: lang {item['lang']} in file {path.name}")
        if item["label"] == "clean" and item["category"] != "none":
            problems.append(f"{iid}: clean item must have category none")
        if item["label"] == "flag" and (
            item["category"] == "none" or item["category"] not in CATEGORIES
        ):
            problems.append(f"{iid}: flag item needs a category from the list")
        if len(item["note"].strip()) < 10:
            problems.append(f"{iid}: note too short")

        length = len(item["text"])
        if item["task"] == "short" and not 3 <= length <= 100:
            problems.append(f"{iid}: short text length {length} outside 3-100")
        if item["task"] == "long":
            minimum = 80 if lang in DENSE else 150
            if not minimum <= length <= 600:
                problems.append(f"{iid}: long text length {length} outside {minimum}-600")

        script = item["script"]
        if script not in SCRIPT_RANGES:
            problems.append(f"{iid}: unknown script {script}")
            continue
        if item["variant"] == "transliterated":
            if script != "Latn" or script_share(item["text"], "Latn") < 0.7:
                problems.append(f"{iid}: transliterated item must be mostly Latin, script Latn")
        elif item["variant"] != "obfuscated":
            allowed = {"Hans", "Hant"} if lang == "zh" else {native}
            if script not in allowed:
                problems.append(f"{iid}: script {script}, expected one of {sorted(allowed)}")
            elif script_share(item["text"], script) < 0.5:
                problems.append(f"{iid}: less than half of the letters are {script}")

    for key, (code, count) in MATRIX.items():
        expected = count
        if key[2] == "transliterated" and not non_latin:
            expected = 0
        if clean_only:
            if key[1] == "flag":
                expected = 0
            elif key[2] == "tricky" and counts[key] == 0:
                continue  # the trap items are optional in a clean-only file
        if counts[key] != expected:
            problems.append(f"{lang}: {code} has {counts[key]} items, expected {expected}")
    if clean_only:
        return problems

    plain_flags = [i for i in items if (i.get("task"), i.get("label"), i.get("variant")) ==
                   ("short", "flag", "plain")]
    cats = Counter(i.get("category") for i in plain_flags)
    for needed in ("profanity", "sexual", "harassment", "hate"):
        if cats[needed] < 1:
            problems.append(f"{lang}: s-fp needs at least one {needed} item")
    long_flags = {i.get("category") for i in items if (i.get("task"), i.get("label"),
                  i.get("variant")) == ("long", "flag", "plain")}
    for needed in ("harassment", "hate", "sexual"):
        if needed not in long_flags:
            problems.append(f"{lang}: l-fp needs one {needed} item")
    if lang == "zh":
        scripts = Counter(i.get("script") for i in items if i.get("variant") != "transliterated")
        if scripts["Hans"] < 8 or scripts["Hant"] < 8:
            problems.append("zh: needs both Hans and Hant items (at least 8 each)")
    return problems


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--clean"]
    clean_only = "--clean" in sys.argv[1:]
    default = sorted(PARTIAL_DIR.glob("*.clean.jsonl")) if clean_only else sorted(
        SRC_DIR.glob("*.jsonl"))
    paths = [Path(p) for p in args] or default
    if not paths:
        sys.exit("no files to validate")
    failed = False
    for path in paths:
        problems = validate_file(path, clean_only=clean_only)
        items, _ = load(path)
        if problems:
            failed = True
            print(f"FAIL {path.name}: {len(problems)} problem(s), {len(items)} items")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"OK   {path.name}: {len(items)} items")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
