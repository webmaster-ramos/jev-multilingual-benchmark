"""Comments from published, human-labelled corpora -> data/long/comments.jsonl

    uv run python -m bench.corpora fetch    # pinned files -> data/corpora/_cache (git-ignored)
    uv run python -m bench.corpora build    # -> data/long/comments.jsonl

Nothing here is written by a model. Each language takes both its clean and its flagged
comments from one corpus, so an arm cannot tell the classes apart by source style. Labels are
the corpus authors' human labels mapped to the benchmark policy (see data/corpora/SOURCES.md);
the blind review decides which items are kept.
"""

from __future__ import annotations

import csv
import random
import sys
import urllib.request
from pathlib import Path

from bench.config import DATA_DIR
from bench.data import write_jsonl

CACHE = DATA_DIR / "corpora" / "_cache"
SEED = "jev-multilingual-benchmark/comments/v1"
PER_CLASS = 60
HF = "https://huggingface.co/datasets/{repo}/resolve/{rev}/{path}"

# pinned revisions: refs/convert/parquet commits for parquet, main commit for COLD's csv
SOURCES: dict[str, dict] = {
    "en": {"name": "Civil Comments", "repo": "google/civil_comments", "rev": "29b3493cb776",
           "files": ["default/validation/0000.parquet"], "licence": "CC0-1.0", "script": "Latn",
           "source": "news-site comments, crowd toxicity scores"},
    "ro": {"name": "RO-Offense", "repo": "readerbench/ro-offense", "rev": "f3be6e4497e6",
           "files": ["default/train/0000.parquet", "default/test/0000.parquet"],
           "licence": "Apache-2.0", "script": "Latn",
           "source": "sports-news comments, native annotators"},
    "pt": {"name": "OLID-BR", "repo": "dougtrajano/olid-br", "rev": "77fea0787188",
           "files": ["default/train/0000.parquet", "default/test/0000.parquet"],
           "licence": "CC-BY-4.0", "script": "Latn",
           "source": "YouTube and Twitter comments, qualified annotators"},
    "tr": {"name": "OffensEval 2020 Turkish", "repo": "strombergnlp/offenseval_2020",
           "rev": "fb4638001485",
           "files": ["tr/train/0000.parquet"], "licence": "CC-BY-4.0", "script": "Latn",
           "source": "tweets, native annotators"},
    "el": {"name": "OffensEval 2020 Greek (OGTD)", "repo": "strombergnlp/offenseval_2020",
           "rev": "fb4638001485",
           "files": ["gr/train/0000.parquet"], "licence": "CC-BY-4.0", "script": "Grek",
           "source": "tweets, volunteer annotators"},
    "ar": {"name": "OffensEval 2020 Arabic (OSACT4)", "repo": "strombergnlp/offenseval_2020",
           "rev": "fb4638001485",
           "files": ["ar/train/0000.parquet"], "licence": "CC-BY-4.0", "script": "Arab",
           "source": "tweets, native annotators"},
    "id": {"name": "IndoDiscourse", "repo": "Exqrch/IndoDiscourse", "rev": "4ec83f7c63a6",
           "files": ["main/main/0000.parquet"], "licence": "Apache-2.0", "script": "Latn",
           "source": "social-media posts and news, multiple annotators"},
    "zh": {"name": "COLD", "repo": "thu-coai/COLD",
           "rev": "a31e56eb008ac3c6abe987094fb06a07fc53625f",
           "files": ["train.csv"], "licence": "Apache-2.0", "script": "Hans",
           "source": "Zhihu and Weibo posts, native annotators"},
}
LENGTH = {"zh": (80, 600)}
DEFAULT_LENGTH = (150, 600)

PT_HATE = ("health", "ideology", "lgbtqphobia", "other_lifestyle", "physical_aspects", "racism",
           "religious_intolerance", "sexism", "xenophobia")


def _download(url: str, path: Path) -> None:
    if path.exists() and path.stat().st_size:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as response:  # noqa: S310 - pinned https URLs
        path.write_bytes(response.read())


def fetch() -> None:
    for lang, src in SOURCES.items():
        for file in src["files"]:
            _download(HF.format(repo=src["repo"], rev=src["rev"], path=file),
                      CACHE / lang / file.replace("/", "_"))
    print(f"corpora cached in {CACHE}")


def _rows(lang: str) -> list[dict]:
    src = SOURCES[lang]
    rows: list[dict] = []
    for file in src["files"]:
        path = CACHE / lang / file.replace("/", "_")
        if not path.exists():
            sys.exit(f"{path} is missing: run `python -m bench.corpora fetch` first")
        if path.suffix == ".csv":
            with path.open(encoding="utf-8-sig", newline="") as handle:
                rows += list(csv.DictReader(handle))
        else:
            import pyarrow.parquet as pq
            rows += pq.read_table(path).to_pylist()
    return rows




def classify(lang: str, row: dict) -> tuple[str | None, str | None, str]:
    """Return (label, category, corpus label as text) for one row, label None to skip."""
    if lang == "en":
        tox = row["toxicity"]
        sub = {"profanity": row["obscene"], "violence": row["threat"],
               "harassment": row["insult"], "hate": row["identity_attack"]}
        if tox >= 0.6:
            category = max(sub, key=sub.get) if max(sub.values()) >= 0.3 else "harassment"
            return "flag", category, f"toxicity {tox:.2f}"
        if tox <= 0.05 and max(sub.values()) <= 0.05:
            return "clean", "none", f"toxicity {tox:.2f}"
        return None, None, ""
    if lang == "ro":
        label = row["label"]
        mapping = {"OTHER": ("clean", "none"), "PROFANITY": ("flag", "profanity"),
                   "INSULT": ("flag", "harassment"), "ABUSE": ("flag", "hate")}
        return (*mapping[label], label)
    if lang == "pt":
        if row["is_offensive"] == "NOT":
            return "clean", "none", "NOT"
        if any(row.get(k) for k in PT_HATE):
            category = "hate"
        elif row.get("insult"):
            category = "harassment"
        else:
            category = "profanity"
        return "flag", category, "OFF"
    if lang in ("tr", "el", "ar"):
        off = row["subtask_a"] in (1, "1", "OFF")
        return ("flag", "profanity", "OFF") if off else ("clean", "none", "NOT")
    if lang == "id":
        if str(row.get("is_noise_or_spam_text")) not in ("0", "False", "None", "[]", "['0', '0']"):
            pass
        tox = [str(x) for x in (row["toxicity"] or [])]
        prof = [str(x) for x in (row["profanity_obscenity"] or [])]
        if len(tox) < 2:
            return None, None, ""
        if all(t == "1" for t in tox):
            return "flag", ("profanity" if "1" in prof else "harassment"), "toxicity 1/1"
        if all(t == "0" for t in tox):
            return "clean", "none", "toxicity 0/0"
        return None, None, ""
    if lang == "zh":
        return ("flag", "hate", f"label 1 ({row['topic']})") if row["label"] == "1" \
            else ("clean", "none", f"label 0 ({row['topic']})")
    raise ValueError(lang)


def _text(lang: str, row: dict) -> str:
    key = "TEXT" if lang == "zh" else "text"
    return " ".join(str(row[key]).split())


def build() -> None:
    items: list[dict] = []
    report = []
    for lang, src in SOURCES.items():
        low, high = LENGTH.get(lang, DEFAULT_LENGTH)
        pools: dict[str, list[tuple[str, str, str]]] = {"flag": [], "clean": []}
        seen: set[str] = set()
        for row in _rows(lang):
            text = _text(lang, row)
            if not low <= len(text) <= high or text in seen:
                continue
            label, category, origin = classify(lang, row)
            if label is None:
                continue
            seen.add(text)
            pools[label].append((text, category, origin))
        rng = random.Random(f"{SEED}:{lang}")
        for label in ("flag", "clean"):
            pool = pools[label]
            chosen = rng.sample(pool, min(PER_CLASS, len(pool)))
            for k, (text, category, origin) in enumerate(chosen, 1):
                items.append({
                    "id": f"{lang}-c-{label[0]}-{k:02d}", "task": "long", "lang": lang,
                    "script": src["script"], "label": label, "category": category,
                    "variant": "corpus", "text": text,
                    "note": f"{src['name']}: corpus label {origin}; mapped to {label}/{category}",
                    "source": src["name"],
                })
        report.append(f"{lang}: {src['name']} - eligible flag {len(pools['flag'])}, clean "
                      f"{len(pools['clean'])}; took {min(PER_CLASS, len(pools['flag']))} + "
                      f"{min(PER_CLASS, len(pools['clean']))}")
    write_jsonl(DATA_DIR / "long" / "comments.jsonl", items)
    print("\n".join(report))
    print(f"built comments dataset: {len(items)} items, {len(SOURCES)} languages")


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "fetch":
        fetch()
    elif command == "build":
        build()
    else:
        sys.exit("usage: python -m bench.corpora fetch|build")


if __name__ == "__main__":
    main()
