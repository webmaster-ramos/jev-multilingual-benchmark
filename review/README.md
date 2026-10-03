# Blind review

No native speakers check this dataset. A second agent does, blind to the intended labels.

**Run on 2026-10-02 by GPT-6.1 Sol** (a different model family from the items' author):
1,000 verdicts, 13 abstentions. The 20 Ukrainian list items were later removed with their list
(see `data/lexicons/SOURCES.md`), leaving 980 items, 9 abstentions and 772 verified. The verdicts are in
`package/verdicts/`, the outcome in [`report.md`](report.md) and `status.jsonl`.

`review/package/` holds 980 items in 25 languages: the written sets (complete for
en, de, fr, es, it; clean halves for the other 20) and the names built from published word
lists. The reviewer is not told which is which, nor which languages have only clean items.
The reviewer's label on a list-derived name is the only judgment anyone makes about that
term, so those verdicts decide which terms stay in the analysis.

1. `uv run python -m bench.review export` writes `review/package/items/<lang>.jsonl`,
   `review/package/items-all.jsonl` and the answer key `review/key.jsonl` (git-ignored).
2. Give the reviewer **only the `review/package/` folder** - copy it out of the repository, so
   `data/` and the key are out of reach - and [`package/PROMPT.md`](package/PROMPT.md) as the
   task. The items were written by Claude; use a reviewer from another model family.
3. The reviewer runs `python3 check_verdicts.py` inside the package before finishing: every
   `rid` exactly once, valid JSON, values from the schema, consistent abstentions. Put the
   `verdicts/<lang>.jsonl` files back into `review/package/verdicts/` and run it once more.
4. `uv run python -m bench.review compare` writes `review/report.md` and
   `review/status.jsonl`. It validates every verdict row with the package's own checker and
   gives each item one status.
5. `uv run python -m bench.score --run results/<run> --verified` rescores a run on verified
   items only (`summary.verified.md`). A disguised item is kept only if its plain pair is
   verified too.

An item is **verified** only if all of this holds: it was judged, not abstained; the
reviewer's label equals the intended one; the reviewer confirms the stated language
(`language_ok` is true, not null); reading
confidence is high or medium; label confidence is high or medium; `policy_ambiguous` is
false; naturalness is not 1. Otherwise it carries the first status that applies: `missing`,
`invalid` (malformed row), `abstained`, `disputed`, `wrong_language`, `language_unknown`,
`policy_ambiguous`,
`label_unsure`, `reading_low`, `garbled`. Only verified items enter the analysis the article
quotes. A category that differs, a medium reading confidence and naturalness 2 are reported
and do not block verification.

The reviewer reports two confidences separately: how well it reads the item
(`reading_confidence`) and how sure it is of the label under the policy (`label_confidence`).
The first says whether a translation check is needed, the second whether the item or the
policy is ambiguous. The policy text in the prompt is exactly what the tested models receive;
it is not extended with boundary rules for the reviewer, so an item the policy does not settle
is marked `policy_ambiguous` by the reviewer and removed.

Disagreements are resolved by a person reading the report, not automatically: fix or replace the
item in `data/src/`, rebuild, re-export, rerun the changed items.

## Round 2: comments

`review/package-comments/` holds the 960 corpus comments (8 languages, 120 each), with the same
`PROMPT.md` and `check_verdicts.py`. The reviewer is not told that these come from corpora or
that each language is half and half. Export, compare and verified-only scoring take
`--round=comments`:

```bash
uv run python -m bench.review export --round=comments
uv run python -m bench.review compare --round=comments      # -> report-comments.md, status-comments.jsonl
uv run python -m bench.score --run results/comments-2026-10-03 --verified
```

## Answer keys

`key.jsonl` (round 1) and `key-comments.jsonl` (round 2) map each package `rid` to the item
`id`. They were kept out of the package and out of git while the review ran, so the reviewer
could not see the intended labels. Both rounds are finished, and the keys are published so that
anyone can rerun `bench.review compare` on the committed verdicts.
