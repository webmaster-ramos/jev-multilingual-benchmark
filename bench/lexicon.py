"""Lexicon-derived names: published profanity lists -> template names -> obfuscation by code.

    uv run python -m bench.lexicon fetch                  # pinned lists -> data/lexicons/_cache
    uv run python -m bench.lexicon build                  # -> data/short/lexicon.jsonl

No item text here is written by a language model. Flagged terms are sampled, with a fixed seed,
from published word lists (see data/lexicons/SOURCES.md); the name around a term is a template;
every disguise is a deterministic transform. Each term appears twice - plain and obfuscated -
so the effect of the disguise is measured on the same word. The same transforms are applied to
clean names as a control: a model that flags those is reacting to the look, not the meaning.
"""

from __future__ import annotations

import json
import random
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

from bench.config import DATA_DIR
from bench.data import write_jsonl
from bench.validate import LANG_ORDER, LANG_SCRIPT, PARTIAL_DIR, SCRIPT_RANGES, SRC_DIR

LEX_DIR = DATA_DIR / "lexicons"
CACHE = LEX_DIR / "_cache"
SEED = "jev-multilingual-benchmark/lexicon/v1"
TERMS_PER_LANG = 10
CONTROLS_PER_LANG = 5
SUFFIXES = ["TV", "HD", "24", "FM", "7"]

LDNOOBW_SHA = "5faf2ba42d7b1c0977169ec3611df25a3c08eb13"
LDNOOBW_RAW = (
    "https://raw.githubusercontent.com/LDNOOBW/"
    f"List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/{LDNOOBW_SHA}/{{lang}}"
)
LDNOOBW_LANGS = ["ar", "cs", "de", "en", "es", "fi", "fr", "hi", "hu", "it", "ja", "ko", "nl",
                 "pl", "pt", "ru", "sv", "th", "tr", "zh"]
VI_URL = (
    "https://raw.githubusercontent.com/blue-eyes-vn/vietnamese-offensive-words/"
    "684b568e4d54ce47b743d7c564447e29a02cc260/vn_offensive_words.txt"
)
SOURCE_NAME = {"ldnoobw": "LDNOOBW", "vi": "vietnamese-offensive-words"}

# The LDNOOBW Hindi list is romanised, so Hindi terms are Latin-script (Hinglish).
TERM_SCRIPT = {**LANG_SCRIPT, "hi": "Latn"}
ALPHABETIC = {"Latn", "Cyrl", "Grek"}
LENGTH = {"Latn": (4, 9), "Cyrl": (4, 7), "Grek": (4, 9), "Arab": (3, 9), "Thai": (3, 9),
          "Jpan": (2, 6), "Kore": (2, 6), "Hans": (2, 6)}
TECHNIQUES = {True: ["leet", "spaced", "homoglyph", "stretched", "masked"],
              False: ["spaced", "masked", "stretched"]}

LEET = {
    "Latn": {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"},
    "Cyrl": {"о": "0", "з": "3", "ч": "4", "б": "6", "і": "1"},
    "Grek": {"ο": "0", "ε": "3", "ι": "1", "α": "4"},
}
HOMOGLYPH = {
    "Latn": {"a": "а", "e": "е", "o": "о", "c": "с", "p": "р", "x": "х", "y": "у", "i": "і"},
    "Cyrl": {"а": "a", "е": "e", "о": "o", "с": "c", "р": "p", "х": "x", "у": "y", "і": "i"},
    "Grek": {"α": "a", "ο": "o", "ε": "e", "ρ": "p", "τ": "t", "ι": "i", "κ": "k", "ν": "v"},
}
VOWELS = {"Latn": "aeiouy", "Cyrl": "аеёиоуыэюяіїє", "Grek": "αεηιουω"}


# --- fetch ---------------------------------------------------------------------------------

def _download(url: str, path: Path) -> None:
    if path.exists() and path.stat().st_size:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=60) as response:  # noqa: S310 - pinned https URLs
        path.write_bytes(response.read())


def fetch() -> None:
    for lang in LDNOOBW_LANGS:
        _download(LDNOOBW_RAW.format(lang=lang), CACHE / "ldnoobw" / lang)
    _download(VI_URL, CACHE / "vi" / "vn_offensive_words.txt")
    print(f"lexicons cached in {CACHE}")


# --- terms ---------------------------------------------------------------------------------

def clusters(text: str) -> list[str]:
    """Split into user-perceived characters: a base plus its combining marks."""
    out: list[str] = []
    for ch in text:
        if out and (unicodedata.category(ch).startswith("M") or ch in "‌‍"):
            out[-1] += ch
        else:
            out.append(ch)
    return out


def _read_list(lang: str) -> tuple[str, list[str]]:
    if lang == "vi":
        path, source = CACHE / "vi" / "vn_offensive_words.txt", "vi"
    elif lang in LDNOOBW_LANGS:
        path, source = CACHE / "ldnoobw" / lang, "ldnoobw"
    else:
        return "", []
    if not path.exists():
        sys.exit(f"{path} is missing: run `python -m bench.lexicon fetch` first")
    lines = path.read_text(encoding="utf-8").splitlines()
    terms = [unicodedata.normalize("NFC", line.strip()) for line in lines]
    return source, [t for t in terms if t and not t.startswith("#")]


def eligible_terms(lang: str) -> tuple[str, list[str]]:
    source, terms = _read_list(lang)
    if not terms:
        return source, []
    script = TERM_SCRIPT[lang]
    low, high = LENGTH[script]
    letter = re.compile(f"[{SCRIPT_RANGES[script]}̀-ͯ]")
    english = set()
    if script == "Latn" and lang != "en":
        english = {t.casefold() for t in _read_list("en")[1]}
    max_tokens = 2 if lang == "vi" else 1
    seen: set[str] = set()
    out = []
    for term in terms:
        tokens = term.split(" ")
        body = term.replace(" ", "")
        if len(tokens) > max_tokens or not body:
            continue
        if not all(letter.fullmatch(ch) for ch in body):
            continue
        if not low <= len(clusters(body)) <= high:
            continue
        key = term.casefold()
        if key in seen or key in english:
            continue
        seen.add(key)
        out.append(key if script in ALPHABETIC else term)
    return source, sorted(out)


# --- transforms ----------------------------------------------------------------------------

def _base(ch: str) -> str:
    return unicodedata.normalize("NFD", ch)[0].lower()


def _pivot(cl: list[str], script: str) -> int:
    """The cluster a person would stretch or mask: the first vowel, else the second cluster."""
    vowels = VOWELS.get(script, "")
    for index, cluster in enumerate(cl):
        if index and _base(cluster) in vowels:
            return index
    return 1 if len(cl) > 1 else 0


def _per_token(term: str, fn) -> str:
    return " ".join(fn(token) for token in term.split(" "))


def _map_chars(term: str, table: dict[str, str]) -> str:
    out = []
    for ch in term:
        low = ch.lower()
        if low in table:
            swapped = table[low]
            out.append(swapped.upper() if ch != low and swapped.isalpha() else swapped)
        else:
            out.append(ch)
    return "".join(out)


def transform(technique: str, term: str, script: str) -> str | None:
    if technique == "spaced":
        result = _per_token(term, lambda tok: ".".join(clusters(tok)))
    elif technique in ("masked", "stretched"):
        tokens = term.split(" ")
        cl = clusters(tokens[0])
        index = _pivot(cl, script) if technique == "stretched" or script in VOWELS else len(cl) - 1
        cl[index] = "*" if technique == "masked" else cl[index] * 3
        tokens[0] = "".join(cl)
        result = " ".join(tokens)
    elif technique == "leet":
        result = _map_chars(term, LEET.get(script, {}))
    elif technique == "homoglyph":
        result = _map_chars(term, HOMOGLYPH.get(script, {}))
    else:
        raise ValueError(technique)
    return result if result != term else None


def disguise(term: str, script: str, k: int) -> tuple[str, str]:
    techniques = TECHNIQUES[script in ALPHABETIC]
    for step in range(len(techniques)):
        technique = techniques[(k + step) % len(techniques)]
        result = transform(technique, term, script)
        if result:
            return technique, result
    raise ValueError(f"no technique applies to a {script} term of {len(term)} characters")


def _title(term: str) -> str:
    return term[:1].upper() + term[1:]


# --- build ---------------------------------------------------------------------------------

def _clean_names(lang: str) -> list[dict]:
    for path in (SRC_DIR / f"{lang}.jsonl", PARTIAL_DIR / f"{lang}.clean.jsonl"):
        if path.exists():
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
                    if line.strip()]
            names = [r for r in rows if r["id"].startswith(f"{lang}-s-cp-")]
            return sorted(names, key=lambda r: r["id"])[:CONTROLS_PER_LANG]
    return []


def _control(item: dict, k: int) -> dict:
    script = item["script"] if item["script"] not in ("Hant",) else "Hans"
    letter = re.compile(f"[{SCRIPT_RANGES[script]}̀-ͯ]")
    tokens = item["text"].split(" ")
    candidates = [t for t in tokens if t and all(letter.fullmatch(ch) for ch in t)]
    target = max(candidates or tokens, key=lambda t: len(clusters(t)))
    technique, disguised = disguise(target, script, k)
    text = " ".join(disguised if t == target else t for t in tokens)
    lang = item["lang"]
    return {
        "id": f"{lang}-x-co-{k + 1:02d}", "task": "short", "lang": lang, "script": item["script"],
        "label": "clean", "category": "none", "variant": "control_obfuscated", "text": text,
        "note": f"clean name {item['id']} with one word disguised by code; technique: {technique}",
        "technique": technique, "pair": item["id"],
    }


def build() -> None:
    items: list[dict] = []
    report = []
    for lang in LANG_ORDER:
        names = _clean_names(lang)
        items += names
        items += [_control(name, k) for k, name in enumerate(names)]

        source, pool = eligible_terms(lang)
        if not pool:
            report.append(f"{lang}: no lexicon source - controls only")
            continue
        script = TERM_SCRIPT[lang]
        terms = random.Random(f"{SEED}:{lang}").sample(pool, min(TERMS_PER_LANG, len(pool)))
        used = []
        for k, term in enumerate(terms):
            suffix = SUFFIXES[k % len(SUFFIXES)]
            technique, disguised = disguise(term, script, k)
            used.append(technique)
            base = {"task": "short", "lang": lang, "script": script, "label": "flag",
                    "category": "profanity", "source": source}
            plain_id = f"{lang}-x-fp-{k + 1:02d}"
            items.append({
                "id": plain_id, **base, "variant": "lexicon_plain",
                "text": f"{_title(term)} {suffix}",
                "note": f"term sampled from {SOURCE_NAME[source]}; flagged by list membership, "
                        "no gloss",
            })
            items.append({
                "id": f"{lang}-x-fo-{k + 1:02d}", **base, "variant": "lexicon_obfuscated",
                "text": f"{_title(disguised)} {suffix}",
                "note": f"same term as {plain_id}, disguised by code; technique: {technique}",
                "technique": technique, "pair": plain_id,
            })
        counts = {t: used.count(t) for t in dict.fromkeys(used)}
        report.append(f"{lang}: {SOURCE_NAME[source]}, {len(pool)} eligible, {len(terms)} terms, "
                      f"{counts}")

    ids = [item["id"] for item in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    assert all(3 <= len(item["text"]) <= 100 for item in items), "text length out of range"
    write_jsonl(DATA_DIR / "short" / "lexicon.jsonl", items)
    print("\n".join(report))
    by_variant: dict[str, int] = {}
    for item in items:
        by_variant[item["variant"]] = by_variant.get(item["variant"], 0) + 1
    print(f"built lexicon dataset: {len(items)} items {by_variant}")


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "fetch":
        fetch()
    elif command == "build":
        build()
    else:
        sys.exit("usage: python -m bench.lexicon fetch|build")


if __name__ == "__main__":
    main()
