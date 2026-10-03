"""Assemble per-language source files into runnable datasets.

    uv run python -m bench.build            # data/src/<lang>.jsonl -> data/{short,long}/full.jsonl
    uv run python -m bench.build --clean    # data/src/_partial/*.clean.jsonl -> .../clean.jsonl

`full` needs both halves of every language. `clean` holds only clean items and measures
false positives.
"""

from __future__ import annotations

import sys

from bench.config import DATA_DIR
from bench.data import write_jsonl
from bench.validate import LANG_ORDER, PARTIAL_DIR, SRC_DIR, load, validate_file


def main() -> None:
    clean_only = "--clean" in sys.argv[1:]
    name = "clean" if clean_only else "full"
    short, long_ = [], []
    missing, failed = [], []
    for lang in LANG_ORDER:
        path = PARTIAL_DIR / f"{lang}.clean.jsonl" if clean_only else SRC_DIR / f"{lang}.jsonl"
        if not path.exists():
            missing.append(lang)
            continue
        if validate_file(path, clean_only=clean_only):
            failed.append(lang)
            continue
        items, _ = load(path)
        short += [i for i in items if i["task"] == "short"]
        long_ += [i for i in items if i["task"] == "long"]
    if failed:
        sys.exit(f"validation failed for: {', '.join(failed)} (run bench.validate)")
    write_jsonl(DATA_DIR / "short" / f"{name}.jsonl", short)
    write_jsonl(DATA_DIR / "long" / f"{name}.jsonl", long_)
    langs = len(LANG_ORDER) - len(missing)
    print(f"built {name} dataset: {len(short)} short + {len(long_)} long items, {langs} languages")
    if missing:
        print(f"missing languages: {', '.join(missing)}")


if __name__ == "__main__":
    main()
