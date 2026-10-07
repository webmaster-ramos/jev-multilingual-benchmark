"""Run one or more arms over a dataset and write one JSONL per arm.

    uv run python -m bench.runner --dataset smoke --tasks short,long --arms gpt5mini,flashlite
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from pathlib import Path

from bench import prompts, verdicts
from bench.config import ARMS, DEFAULT_ARMS, RESULTS_DIR, Arm
from bench.data import load_items
from bench.providers import jev, openai_decisions, openrouter


def run_item(arm: Arm, item: dict) -> dict:
    task, text = item["task"], item["text"]
    record = {
        "item_id": item["id"],
        "task": task,
        "lang": item["lang"],
        "label": item["label"],
        "arm": arm.key,
        "model_requested": arm.model,
        "verdict": dict(verdicts.EMPTY),
        "latency_ms": None,
        "usage": None,
        "cost_usd": None,
        "model": None,
        "provider": None,
        "finish_reason": None,
        "raw": None,
        "error": None,
    }
    try:
        if arm.kind == "decision":
            result = jev.evaluate(
                prompts.jev_state(task, text), prompts.jev_questions(task), model=arm.model
            )
            record["raw"] = result["answers"]
            record["verdict"] = verdicts.from_jev(result["answers"])
        elif arm.kind == "decision_openai":
            result = openai_decisions.evaluate(
                text, prompts.decision_questions(task), model=arm.model
            )
            record["raw"] = result["answers"]
            record["verdict"] = verdicts.from_openai_decisions(result["answers"])
        else:
            if arm.kind == "chat_json" or arm.kind == "guard_policy":
                messages, schema = prompts.chat_messages(task, text), prompts.CHAT_SCHEMA
            else:
                messages, schema = prompts.guard_messages(text), None
            result = openrouter.chat(
                arm.model,
                messages,
                schema=schema,
                temperature=arm.temperature,
                max_tokens=arm.max_tokens,
                reasoning_effort=arm.reasoning_effort,
            )
            record["raw"] = result["text"]
            if arm.kind in ("chat_json", "guard_policy"):
                record["verdict"] = verdicts.from_chat_json(result["text"])
            elif arm.kind == "guard_llama":
                record["verdict"] = verdicts.from_llama_guard(result["text"])
            elif arm.kind == "guard_nemotron":
                record["verdict"] = verdicts.from_nemotron(result["text"])
        for key in ("latency_ms", "usage", "cost_usd", "model", "provider", "finish_reason"):
            record[key] = result.get(key)
    except Exception as exc:  # noqa: BLE001 - every failure is a data point here
        record["error"] = f"{type(exc).__name__}: {exc}"[:500]
    return record


def run_arm(
    arm: Arm, items: list[dict], out_dir: Path, workers: int, resume: bool
) -> list[dict]:
    out_path = out_dir / f"{arm.key}.jsonl"
    kept: dict[str, dict] = {}
    if resume and out_path.exists():
        with out_path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    record = json.loads(line)
                    if not record["error"] and record["verdict"]["flag"] is not None:
                        kept[record["item_id"]] = record
    todo = [item for item in items if item["id"] not in kept]
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        fresh = list(pool.map(lambda item: run_item(arm, item), todo))
    by_id = {**kept, **{record["item_id"]: record for record in fresh}}
    records = [by_id[item["id"]] for item in items if item["id"] in by_id]
    with out_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    errors = sum(1 for r in records if r["error"])
    unparsed = sum(1 for r in records if not r["error"] and r["verdict"]["flag"] is None)
    cost = sum(r["cost_usd"] or 0 for r in fresh)
    print(
        f"[{arm.key}] {len(records)} items ({len(fresh)} run, {len(kept)} kept), "
        f"{errors} errors, {unparsed} unparsed, ${cost:.4f} this pass, "
        f"{time.perf_counter() - started:.0f}s -> {out_path}",
        file=sys.stderr,
    )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="smoke")
    parser.add_argument("--tasks", default="short,long")
    parser.add_argument("--arms", default=",".join(DEFAULT_ARMS))
    parser.add_argument(
        "--run", default=None, help="results sub-directory (default: <dataset>-<utc date>)"
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=0, help="first N items per task (0 = all)")
    parser.add_argument(
        "--resume", action="store_true",
        help="keep parsed records already in results/<run>/<arm>.jsonl; rerun errors and unparsed",
    )
    args = parser.parse_args()

    items: list[dict] = []
    for task in args.tasks.split(","):
        task_items = load_items(args.dataset, task.strip())
        items.extend(task_items[: args.limit] if args.limit else task_items)
    if not items:
        sys.exit("no items loaded")

    run_name = args.run or f"{args.dataset}-{datetime.now(UTC):%Y-%m-%d}"
    out_dir = RESULTS_DIR / run_name
    out_dir.mkdir(parents=True, exist_ok=True)
    # One runner per arm group may share a run directory: record the arms on disk afterwards.
    if not (args.resume and (out_dir / "run.json").exists()):
        (out_dir / "run.json").write_text(
            json.dumps(
                {
                    "dataset": args.dataset,
                    "tasks": args.tasks,
                    "arms": args.arms,
                    "items": len(items),
                    "started_utc": datetime.now(UTC).isoformat(timespec="seconds"),
                },
                indent=2,
            )
        )
    for key in args.arms.split(","):
        arm = ARMS[key.strip()]
        run_arm(arm, items, out_dir, args.workers, args.resume)
    meta = json.loads((out_dir / "run.json").read_text())
    meta["arms"] = ",".join(sorted(p.stem for p in out_dir.glob("*.jsonl")))
    (out_dir / "run.json").write_text(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
