"""Summarise a run: per arm, per language, plus the misses.

    uv run python -m bench.score --run results/smoke-2026-10-02
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

from bench.config import ARMS, RESULTS_DIR, ROOT
from bench.data import load_items


def load_run(run_dir: Path) -> dict[str, list[dict]]:
    runs = {}
    for path in sorted(run_dir.glob("*.jsonl")):
        with path.open(encoding="utf-8") as handle:
            runs[path.stem] = [json.loads(line) for line in handle if line.strip()]
    return runs


def expected_flag(label: str) -> bool:
    return label == "flag"


def summarise(records: list[dict]) -> dict:
    n = len(records)
    errors = [r for r in records if r["error"]]
    answered = [r for r in records if not r["error"] and r["verdict"]["flag"] is not None]
    correct = [r for r in answered if r["verdict"]["flag"] == expected_flag(r["label"])]
    fp = [r for r in answered if r["verdict"]["flag"] and not expected_flag(r["label"])]
    fn = [r for r in answered if not r["verdict"]["flag"] and expected_flag(r["label"])]
    unparsed = [r for r in records if not r["error"] and r["verdict"]["flag"] is None]
    latencies = [r["latency_ms"] for r in records if r["latency_ms"]]
    probs = [r["verdict"]["p_flag"] for r in answered if r["verdict"]["p_flag"] is not None]
    uncertain = [p for p in probs if 0.3 <= p <= 0.7]
    lang_known = [r for r in answered if r["verdict"].get("language")]
    lang_ok = [r for r in lang_known if _lang_name(r["lang"]) == r["verdict"]["language"]]
    return {
        "n": n,
        "errors": len(errors),
        "unparsed": len(unparsed),
        "answered": len(answered),
        "accuracy": len(correct) / len(answered) if answered else None,
        "fp": len(fp),
        "fn": len(fn),
        "p50_ms": statistics.median(latencies) if latencies else None,
        "cost_usd": sum(r["cost_usd"] or 0 for r in records),
        "uncertain_share": len(uncertain) / len(probs) if probs else None,
        "lang_acc": len(lang_ok) / len(lang_known) if lang_known else None,
    }


LANG_NAMES = {
    "en": "English", "de": "German", "fr": "French", "es": "Spanish", "it": "Italian",
    "pt": "Portuguese", "nl": "Dutch", "pl": "Polish", "cs": "Czech", "hu": "Hungarian",
    "ro": "Romanian", "el": "Greek", "sv": "Swedish", "fi": "Finnish", "tr": "Turkish",
    "ru": "Russian", "uk": "Ukrainian", "ar": "Arabic", "hi": "Hindi", "th": "Thai",
    "vi": "Vietnamese", "id": "Indonesian", "ja": "Japanese", "ko": "Korean", "zh": "Chinese",
}


def _lang_name(code: str) -> str:
    return LANG_NAMES.get(code, "other")


def fmt(value, kind="pct"):
    if value is None:
        return "-"
    if kind == "pct":
        return f"{value * 100:.0f}%"
    if kind == "ms":
        return f"{value:.0f}"
    if kind == "usd":
        return f"${value:.4f}"
    return str(value)


def _caught(records: list[dict]) -> dict[str, bool]:
    return {r["item_id"]: bool(r["verdict"]["flag"]) for r in records}


def recall_by_language(runs: dict[str, list[dict]], items: dict[str, dict]) -> list[str]:
    """For each kind of flagged item: how many each arm caught, per language."""
    lines: list[str] = []
    kinds: list[tuple[str, str]] = []
    for item in items.values():
        kind = (item["task"], item["variant"])
        if item["label"] == "flag" and kind not in kinds:
            kinds.append(kind)
    for task, variant in kinds:
        members = [i for i in items.values()
                   if (i["task"], i["variant"], i["label"]) == (task, variant, "flag")]
        langs = list(dict.fromkeys(i["lang"] for i in members))
        if len(langs) < 3:
            continue
        lines += [f"## Flagged items caught, by language - {task} {variant}", "",
                  "| arm | " + " | ".join(langs) + " | all |", "|---|" + "---:|" * (len(langs) + 1)]
        for key, records in runs.items():
            caught = _caught(records)
            cells, total = [], 0
            for lang in langs:
                ids = [i["id"] for i in members if i["lang"] == lang]
                hit = sum(1 for iid in ids if caught.get(iid))
                total += hit
                cells.append(f"{hit}/{len(ids)}")
            lines.append(f"| {key} | " + " | ".join(cells) + f" | {total}/{len(members)} |")
        lines.append("")
    return lines


def paired_obfuscation(runs: dict[str, list[dict]], items: dict[str, dict]) -> list[str]:
    """Same word plain and disguised; same clean name plain and disguised."""
    flagged = [i for i in items.values() if i.get("pair") and i["label"] == "flag"]
    controls = [i for i in items.values() if i.get("pair") and i["label"] == "clean"]
    if not flagged:
        return []
    techniques = list(dict.fromkeys(i["technique"] for i in flagged))
    lines = ["## Paired obfuscation - the same term plain and disguised", "",
             "`kept` = caught in disguise, of the terms the arm caught when plain.", "",
             "| arm | plain caught | disguised caught | kept | "
             + " | ".join(f"kept: {t}" for t in techniques) + " |",
             "|---|---:|---:|---:|" + "---:|" * len(techniques)]
    for key, records in runs.items():
        caught = _caught(records)
        plain = [i for i in flagged if caught.get(i["pair"])]
        kept = [i for i in plain if caught.get(i["id"])]
        disguised = sum(1 for i in flagged if caught.get(i["id"]))
        cells = []
        for technique in techniques:
            base = [i for i in plain if i["technique"] == technique]
            hit = sum(1 for i in base if caught.get(i["id"]))
            cells.append(f"{hit}/{len(base)}")
        lines.append(
            f"| {key} | {len(plain)}/{len(flagged)} | {disguised}/{len(flagged)} | "
            f"{fmt(len(kept) / len(plain) if plain else None)} | " + " | ".join(cells) + " |"
        )
    lines.append("")
    if controls:
        lines += ["## Control - clean names with the same disguises", "",
                  "A flag here is a false positive caused by the look of the text.", "",
                  "| arm | clean names flagged | disguised clean names flagged | "
                  + " | ".join(techniques) + " |",
                  "|---|---:|---:|" + "---:|" * len(techniques)]
        for key, records in runs.items():
            caught = _caught(records)
            original = sum(1 for i in controls if caught.get(i["pair"]))
            disguised = sum(1 for i in controls if caught.get(i["id"]))
            cells = []
            for technique in techniques:
                base = [i for i in controls if i["technique"] == technique]
                hit = sum(1 for i in base if caught.get(i["id"]))
                cells.append(f"{hit}/{len(base)}")
            lines.append(f"| {key} | {original}/{len(controls)} | {disguised}/{len(controls)} | "
                         + " | ".join(cells) + " |")
        lines.append("")
    return lines


def render(run_dir: Path, runs: dict[str, list[dict]], items: dict[str, dict]) -> str:
    lines = [f"# Run summary: `{run_dir.name}`", ""]
    lines += ["## Per arm", "",
              "| arm | model | items | errors | unparsed | accuracy | FP | FN | p50 ms | cost | uncertain p (0.3-0.7) | language id |",  # noqa: E501
              "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for key, records in runs.items():
        s = summarise(records)
        model = ARMS[key].model if key in ARMS else "?"
        lines.append(
            f"| {key} | {model} | {s['n']} | {s['errors']} | {s['unparsed']} | {fmt(s['accuracy'])} | "  # noqa: E501
            f"{s['fp']} | {s['fn']} | {fmt(s['p50_ms'], 'ms')} | {fmt(s['cost_usd'], 'usd')} | "
            f"{fmt(s['uncertain_share'])} | {fmt(s['lang_acc'])} |"
        )
    lines += ["", "FP = clean item flagged. FN = offensive item passed. "
              "Uncertain share applies to the decision arm only (Noul probability in the 0.3-0.7 band).", ""]  # noqa: E501

    for task in ("short", "long"):
        by_lang: dict[str, dict[str, dict]] = defaultdict(dict)
        langs: list[str] = []
        for key, records in runs.items():
            task_records = [r for r in records if r["task"] == task]
            for lang in sorted({r["lang"] for r in task_records}):
                if lang not in langs:
                    langs.append(lang)
                by_lang[key][lang] = summarise([r for r in task_records if r["lang"] == lang])
        if not langs:
            continue
        lines += [f"## Accuracy by language - {task}", "",
                  "| arm | " + " | ".join(langs) + " |",
                  "|---|" + "---:|" * len(langs)]
        for key in runs:
            cells = []
            for lang in langs:
                s = by_lang[key].get(lang)
                cells.append(fmt(s["accuracy"]) if s else "-")
            lines.append(f"| {key} | " + " | ".join(cells) + " |")
        lines.append("")

    variants: list[tuple[str, str, str]] = []
    for item in items.values():
        key = (item["task"], item["label"], item["variant"])
        if key not in variants:
            variants.append(key)
    if variants:
        lines += ["## Accuracy by variant", "",
                  "| arm | " + " | ".join(f"{t} {lab} {v}" for t, lab, v in variants) + " |",
                  "|---|" + "---:|" * len(variants)]
        for key, records in runs.items():
            cells = []
            for task, label, variant in variants:
                subset = [r for r in records if r["item_id"] in items
                          and (items[r["item_id"]]["task"], items[r["item_id"]]["label"],
                               items[r["item_id"]]["variant"]) == (task, label, variant)]
                cells.append(fmt(summarise(subset)["accuracy"]) if subset else "-")
            lines.append(f"| {key} | " + " | ".join(cells) + " |")
        lines.append("")

    lines += recall_by_language(runs, items)
    lines += paired_obfuscation(runs, items)

    if "jev" in runs:
        jev = [r for r in runs["jev"] if r["verdict"]["p_flag"] is not None]
        band = [r for r in jev if 0.3 <= r["verdict"]["p_flag"] <= 0.7]
        sure = [r for r in jev if r not in band]
        sure_ok = [r for r in sure if r["verdict"]["flag"] == expected_flag(r["label"])]
        wrong = [r for r in jev if r["verdict"]["flag"] != expected_flag(r["label"])]
        wrong_sure = [r for r in wrong if r not in band]
        lines += ["## Decision arm: the 0.3-0.7 band", "",
                  f"- answers in the band: {len(band)} of {len(jev)}",
                  f"- wrong answers: {len(wrong)}, of which outside the band (confidently wrong): "
                  f"{len(wrong_sure)}",
                  f"- accuracy on answers outside the band: "
                  f"{fmt(len(sure_ok) / len(sure) if sure else None)} ({len(sure_ok)}/{len(sure)})"]
        fallback = {r["item_id"]: r for r in runs.get("gpt5mini", [])}
        if fallback:
            routed_ok = sum(
                1 for r in band
                if r["item_id"] in fallback
                and fallback[r["item_id"]]["verdict"]["flag"] == expected_flag(r["label"])
            )
            total = len(sure_ok) + routed_ok
            lines.append(
                f"- routing (Jev outside the band, gpt5mini inside it): "
                f"{fmt(total / len(jev) if jev else None)} ({total}/{len(jev)}), "
                f"{fmt(len(band) / len(jev) if jev else None)} of items routed"
            )
        lines.append("")

    lines += ["## Misses and failures", "",
              "| arm | item | lang | label | verdict | p / conf | category | note |",
              "|---|---|---|---|---|---:|---|---|"]
    for key, records in runs.items():
        for r in records:
            v = r["verdict"]
            miss = r["error"] or v["flag"] is None or v["flag"] != expected_flag(r["label"])
            if not miss:
                continue
            item = items.get(r["item_id"], {})
            prob = v["p_flag"] if v["p_flag"] is not None else v["confidence"]
            note = r["error"] or item.get("note", "")
            lines.append(
                f"| {key} | {r['item_id']} | {r['lang']} | {r['label']} | "
                f"{'error' if r['error'] else v['flag']} | {fmt(prob, 'raw') if prob is None else f'{prob:.2f}'} | "  # noqa: E501
                f"{v['category'] or '-'} | {str(note)[:90].replace('|', '/')} |"
            )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    parser.add_argument("--dataset", default=None, help="dataset name (default: from run.json)")
    parser.add_argument(
        "--verified", action="store_true",
        help="keep only items marked verified in review/status.jsonl; writes summary.verified.md",
    )
    args = parser.parse_args()
    run_dir = Path(args.run)
    if not run_dir.is_absolute() and not run_dir.exists():
        run_dir = RESULTS_DIR / run_dir.name
    meta = json.loads((run_dir / "run.json").read_text())
    dataset = args.dataset or meta["dataset"]
    items = {}
    for task in ("short", "long"):
        for item in load_items(dataset, task):
            items[item["id"]] = item
    runs = load_run(run_dir)
    name = "summary.md"
    if args.verified:
        status_name = "status-comments.jsonl" if dataset == "comments" else "status.jsonl"
        status_path = ROOT / "review" / status_name
        if not status_path.exists():
            raise SystemExit("review/status.jsonl is missing: run bench.review compare first")
        with status_path.open(encoding="utf-8") as handle:
            statuses = [json.loads(line) for line in handle if line.strip()]
        verified = {row["id"] for row in statuses if row["status"] == "verified"}
        # A disguised copy is only as good as its plain pair: keep pairs together.
        keep = {iid for iid, item in items.items()
                if iid in verified and (not item.get("pair") or item["pair"] in verified)}
        dropped = len(items) - len(keep)
        items = {iid: item for iid, item in items.items() if iid in keep}
        runs = {arm: [r for r in rows if r["item_id"] in keep] for arm, rows in runs.items()}
        name = "summary.verified.md"
        print(f"verified only: {len(keep)} items kept, {dropped} dropped")
    summary = render(run_dir, runs, items)
    (run_dir / name).write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
