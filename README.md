# jev-multilingual-benchmark

> **Content warning.** The data contains profanity, sexual vulgarity, insults, threats and
> hateful statements in 25 languages, some of it written by real people and published in
> research corpora. It is here to test moderation models; do not use it to train or prompt a
> model to produce such content. Licences and attribution: [NOTICE.md](NOTICE.md).

A reproducible benchmark of **typed decision models vs chat and guard models** on one job a
multilingual storefront actually has: moderating short user-generated text (a display name, a
personalisation field) and long user-generated text (a comment, a review) across the
**30 store views / 25 languages** of a real storefront.

The question: TypeSafe's Jev documents English as its primary training language and says other
languages "are handled but not equally well; test on your own content". This repo is that test,
run against the alternatives a store can reach through one OpenRouter key.

## Findings in brief

Measured 2-3 October 2026, scored only on items a blind reviewer confirmed:

- **Clean text is safe with the decision model in every language tested.** One false
  positive across 360 clean texts in 25 languages.
- **On real comments it holds outside English.** 94.0% on 520 verified comments in eight
  languages (English 98.5%, the other seven 93.4%), second to Gemini Flash-Lite. Paired with
  Flash-Lite for its uncertain band it reaches 95.4% at its own price.
- **On a short name field it does not.** A bare native swear word is caught about three times
  in four in English, Spanish, Russian, Japanese and Chinese, and about one time in five in
  the other sixteen languages tested; and its probability rises for anything that
  looks disguised, clean or not.
- **The most expensive chat model is too strict for a storefront policy.** gpt-5-mini catches
  every abusive comment and flags one acceptable comment in six.

The boundary is the kind of text, not the language. Details and caveats below.

## Status (2026-10-03)

- **Four datasets are built and run** on six arms (see [Data](#data)): `full` for 5 languages,
  `clean` for the other 20, `lexicon` - names built from published profanity lists - for 21,
  and `comments` - 960 human-labelled comments from published corpora - for 8.
- **Reviewed.** A second agent (GPT-6.1 Sol) judged every item blind ([`review/`](review/README.md)).
  Of the 980 in the first round, 772 are verified: every written item, and 107 of 210 list
  terms with 105 of their disguised copies. Report: [`review/report.md`](review/report.md); status per item:
  [`review/status.jsonl`](review/status.jsonl).
- **The numbers below are on verified items only** (`summary.verified.md` in each run). The
  `comments` set was reviewed in a second round: 520 of 960 verified.
- No item has been read by a native speaker.
- **Smoke** (40 items, 8 languages): a first look with seven arms, kept at the end.

## Arms

| key | model | kind | why it is here |
|---|---|---|---|
| `jev` | `jev-1.13.0` (TypeSafe, direct API) | typed decision model | the subject of the test; pinned version |
| `gpt5mini` | `openai/gpt-5-mini` via OpenRouter | chat + strict JSON schema | the model class most stores run this job on today |
| `flashlite` | `google/gemini-2.5-flash-lite` | chat + strict JSON schema | cheapest Google route with structured output |
| `gemma4` | `google/gemma-4-26b-a4b-it` | chat + strict JSON schema | open-weight Google model |
| `llamaguard` | `meta-llama/llama-guard-4-12b` | fixed-taxonomy guard | what a "safety classifier" answers; profanity is not a hazard in its taxonomy |
| `safeguard` | `openai/gpt-oss-safeguard-20b` | policy-conditioned guard | takes our policy text as the policy |

**Tested and dropped: `nemotron`** (`nvidia/nemotron-3.5-content-safety`, a 4B guard with the
Aegis taxonomy, which includes Profanity). It answers safe or unsafe with no probability, so
nothing can be routed on it; on the written items it was the weakest arm after Llama Guard
(130 of 150, 11 of 25 obfuscated names) and the slowest but one (p50 1.6 s); and its free route
is capped per day, which stopped a run. It stays in the smoke results and can still be run
with `--arms nemotron`.

There is no typed-decision model from Google or from OpenRouter itself. OpenRouter lists
`typesafe/jev-router`, a model router built on Jev, with no endpoints and hidden pricing; it is
not the decision API. Jev is reached directly.

## Tasks

- **short** - a display name or personalisation field, up to 100 characters. One Noul
  (`flag`), one Choice (`category`), one Choice (`language`).
- **long** - a comment or review, 150-600 characters. The same three plus a Score (`severity`).

Every chat arm gets the same policy text and the same JSON schema; the guard arms get the raw text
(or the policy, for the policy-conditioned one) and their output is mapped to `flag`. The policy
in [`bench/prompts.py`](bench/prompts.py) was written for this benchmark and is not a production
prompt.

## Data

No data comes from any store or customer. The written items (`smoke`, `full`, `clean`) were
produced with a language model for this benchmark; the `lexicon` names are terms from
published word lists inside templates; the `comments` are real posts and comments from
published research corpora, as their authors released them (tweets keep the corpora's own
`@USER` and `URL` placeholders). Labels are by construction for the written and list items
and by the corpus annotators for the comments; in every case the blind review decides what
is scored.

| dataset | built from | what it holds | what it measures |
|---|---|---|---|
| `smoke` | `data/{short,long}/smoke.jsonl` | 40 hand-picked items, 8 languages | the pipeline; a first look |
| `full` | `data/src/<lang>.jsonl` | the complete written item matrix, both halves: 30 items per language | accuracy, false positives and false negatives on written items |
| `clean` | `data/src/_partial/<lang>.clean.jsonl` | only the clean half of a language: plain names and comments, trap items, one heated but civil complaint | false positives |
| `lexicon` | published word lists + code | per language: 10 terms from a profanity list as plain names, the same 10 disguised by code, 5 clean names and the same 5 disguised | whether a model knows the language's own profanity, what a disguise costs on the same word, and whether a disguise alone triggers a flag |
| `comments` | published human-labelled corpora | 60 flagged and 60 clean comments per language from one corpus per language, 150-600 characters (Chinese 80-600) | the long task on organic text in 8 languages: en, ro, pt, tr, el, ar, id, zh |

The written item matrix, its trap and obfuscation variants and the field definitions are in
[`data/src/SPEC.md`](data/src/SPEC.md); `bench.validate` enforces them. The lexicon sources,
licences, selection rules and transforms are in
[`data/lexicons/SOURCES.md`](data/lexicons/SOURCES.md). The corpora, their licences, the
pinned revisions and the label mapping are in [`data/corpora/SOURCES.md`](data/corpora/SOURCES.md).

| languages | written items | lexicon items |
|---|---|---|
| en, de, fr, es, it | `full`: 30 each, both halves | 10 terms each |
| pt, nl, pl, cs, hu, sv, fi, tr, ru, ar, hi, th | `clean`: 15 each, with trap items | 10 terms each |
| uk | `clean`: 15, with trap items | none - the only list found was removed, see SOURCES |
| vi, ja, ko, zh | `clean`: 12 each, no trap items | 10 terms each |
| ro, el | `clean`: 15 each | none - no list with a clear licence |
| id | `clean`: 12 | none |

Why two kinds of flagged data: the offensive half of the written matrix could be produced by
a language model for five languages only, and that was not forced. For the rest, flagged terms
come from published lists and every disguise is a deterministic transform, so no flagged text
in the `lexicon` dataset is model-written. The cost: a list term is flagged by membership, not
by a moderator's judgment, and a list gives words, not comments - the long task has flagged
items in five languages only.

```json
{"id": "de-s-fp-03", "task": "short", "lang": "de", "script": "Latn", "label": "flag",
 "category": "sexual", "variant": "plain", "text": "...", "note": "English gloss"}
```

## Run

```bash
uv sync
cp .env.example .env   # TYPESAFE_API_KEY, OPENROUTER_API_KEY

uv run python -m bench.validate && uv run python -m bench.build            # -> full
uv run python -m bench.validate --clean && uv run python -m bench.build --clean   # -> clean

uv run --with pyarrow python -m bench.lexicon fetch                         # pinned word lists
uv run python -m bench.lexicon build                                       # -> lexicon
uv run python -m bench.corpora fetch && uv run python -m bench.corpora build   # -> comments

uv run python -m bench.runner --dataset lexicon --run lexicon-2026-10-02
uv run python -m bench.score --run results/lexicon-2026-10-02
```

Each arm writes `results/<run>/<arm>.jsonl` with the verdict, latency (client-side, from one
machine in Europe), token usage and cost as the provider reported it. `score` writes
`summary.md` next to them.

`--resume` keeps the parsed rows already in `results/<run>/<arm>.jsonl` and reruns only errors
and unparseable answers, which is how a rate-limited arm gets finished:

```bash
uv run python -m bench.runner --dataset smoke --arms safeguard --run smoke-2026-10-02 --workers 1 --resume
```

## Metrics

- accuracy, false positives (clean flagged) and false negatives (offensive passed), per arm,
  per language and per variant
- paired obfuscation: of the list terms an arm catches in plain form, the share it still
  catches in disguise, per technique; and the same disguises on clean names as a control
- for the decision arm: the Noul probability itself, the share of answers in the 0.3-0.7
  band - the "uncertain" region TypeSafe's docs tell you to route on - how many wrong answers
  fall outside it, and what routing the band to a chat model yields
- language identification accuracy (does the model know what it is reading)
- latency p50 and cost per item as reported

## Results on verified items (2026-10-02 and 10-03)

Full tables: [`full`](results/full-2026-10-02/summary.verified.md),
[`clean`](results/clean-2026-10-02/summary.verified.md),
[`lexicon`](results/lexicon-2026-10-02/summary.verified.md). The same runs on all items,
before the review, are in `summary.md` next to them.

| | jev | gpt5mini | flashlite | gemma4 | safeguard | llamaguard |
|---|---:|---:|---:|---:|---:|---:|
| all 772 verified items of the first round - correct | 79.1% | 91.6% | 89.5% | 85.9% | 82.1% | 64.1% |
| written items, 5 languages - correct of 150 | 136 | 149 | 147 | 142 | 144 | 99 |
| written clean items, 20 languages - false positives of 285 | 1 | 0 | 2 | 2 | 4 | 24 |
| written obfuscated names caught, of 25 | 13 | 25 | 22 | 17 | 19 | 2 |
| verified list terms flagged plain, of 107 (21 languages) | 36 | 78 | 76 | 71 | 53 | 7 |
| kept after disguise, of the terms caught plain | 56% | 86% | 70% | 59% | 51% | 57% |
| disguised clean names flagged, of 125 | 7 | 0 | 7 | 7 | 0 | 4 |
| p50 latency, ms | 258 | 2,611 | 458 | 1,222 | 414 | 340 |
| cost per 1,000 verdicts | $0.04 | $0.39 | $0.05 | $0.03 | $0.11 | $0.04 |

- **Clean text is safe with the decision model in every language tested**: one false positive
  in 360 written clean items across 25 languages; none when 125 of those names were run again
  in the list set.
- **Abuse written out is caught**: 28 of 30 plain flagged names and 20 of 20 flagged comments
  (five languages).
- **A bare native swear word as a name is the gap, and it splits by language, not script.**
  Jev flags 21 of 27 verified terms in English, Spanish, Russian, Japanese and Chinese, and
  15 of 80 in the other sixteen languages; gpt-5-mini 25 and 53. With 2-10
  verified terms per language, only group totals carry weight.
- **Disguise raises the decision model's probability whatever the word is**: disguising a clean
  name lifts it by 0.16 on average, so lowering the threshold to recover misses also flags
  text that merely looks obfuscated (55 of 125 disguised clean names at 0.2). gpt-5-mini
  flags none.
- **Half of the list terms did not survive the review**: 66 of 210 were judged clean as a bare
  public name and 30 were cases the policy does not settle. A published profanity list is not
  a set of unacceptable names.
- Changing one noun in the task prompt flipped 4 of 435 verdicts for Jev and 5 for Gemma.

### Comments from corpora, verified (520 of 960, 8 languages)

| | jev | gpt5mini | flashlite | gemma4 | safeguard | llamaguard |
|---|---:|---:|---:|---:|---:|---:|
| accuracy | 94.0% | 89.0% | 95.4% | 91.7% | 93.1% | 60.6% |
| flagged caught, of 184 | 175 | 184 | 178 | 150 | 167 | 152 |
| clean flagged, of 336 | 22 | 57 | 18 | 9 | 19 | 173 |
| flags on the 186 policy-ambiguous comments | 65% | 89% | 51% | 29% | 52% | 74% |

- On organic comments the decision model holds across eight languages (English 98.5%, the
  other seven 93.4%) and ranks second, behind Flash-Lite.
- gpt-5-mini catches everything and flags 17% of acceptable comments; as a fallback behind
  Jev it lowers accuracy. Flash-Lite behind Jev's 0.3-0.7 band gives 95.4% with 14% routed.
- 39% of the comments the reviewer found the policy does not settle fall in Jev's 0.3-0.7
  band, against 14% of the verified ones.

## Smoke results (2026-10-02, 40 items, 8 languages, 5 scripts)

| arm | accuracy | FP | FN | p50 ms | cost | language id |
|---|---:|---:|---:|---:|---:|---:|
| gpt5mini | 40/40 | 0 | 0 | 2,658 | $0.0140 | 98% |
| safeguard | 40/40 | 0 | 0 | 379 | $0.0033 | 95% |
| jev | 39/40 | 0 | 1 | 265 | $0.0016 | 90% |
| flashlite | 39/40 | 0 | 1 | 596 | $0.0019 | 95% |
| gemma4 | 39/40 | 0 | 1 | 1,273 | $0.0016 | 90% |
| nemotron | 38/40 | 0 | 2 | 1,931 | $0 | - |
| llamaguard | 21/40 | 2 | 17 | 360 | $0.0016 | - |

Jev's one miss (Ukrainian profanity, p = 0.39) and one near-miss (leetspeak Spanish, p = 0.51)
are its only two answers in the 0.3-0.7 band; the same leetspeak name is passed by Gemini and
Gemma with self-reported confidence 0.90-1.00. Jev identified three of four Ukrainian names as
Russian. Llama Guard passes every profane short name by taxonomy design and flags two clean
comments as "specialized advice". Forty items is a look, not a result.

## Caveats

- No native speaker has read the items. The written items were produced with a language model,
  the names come from word lists, and everything was reviewed blind by a second model
  (GPT-6.1 Sol). Two models agreeing is a weaker check than a native speaker: shared blind
  spots in low-resource languages survive it, and for eleven languages the reviewer reported
  only medium confidence in its own reading.
- Flagged evidence differs by language. Written flagged items: en, de, fr, es, it.
  List-derived flagged names: 21 languages (not ro, el, id, uk). Flagged comments: en, ro, pt,
  tr, el, ar, id, zh. Cyrillic, Japanese, Korean, Hindi, Thai and Vietnamese comments are not
  in the comment set: no corpus with a usable licence was found.
- A list term is flagged by membership in a published list; the review kept 107 of 210. Plain-
  form recall mixes "the model does not know the word" with "the word is mild"; the paired
  comparison does not.
- Verified comments are those on which the reviewer and the corpus annotators agree - the
  clearer half of real text. 11-42 verified flagged comments per language.
- The reviewer is an OpenAI model, as are gpt-5-mini and gpt-oss-safeguard. gpt-5-mini still
  scores lowest of the chat arms on verified comments, so the review did not reward its own
  family's strictness, but the overlap is there.
- Guard models answer a different question (hazard taxonomies) than a storefront policy. Their
  misses on plain profanity are expected and reported, not hidden.
- Thresholds and routing bands were fitted on the items they are scored on.
- A snapshot: all runs on 2-3 October 2026, with `jev-1.13.0` pinned; the OpenRouter arms are
  called by name and not pinned. Changing one noun in the task prompt flipped 4 of 435 Jev
  verdicts. Latency is wall-clock from one client in Europe; it compares arms, not regions.

## Licence

Code: MIT ([LICENSE](LICENSE)). Data written for this benchmark: CC BY 4.0. Word-list terms
and corpus comments: their publishers' licences, with attribution, in [NOTICE.md](NOTICE.md).
