# Notice: licences and attribution

> **Content warning.** The data in this repository contains profanity, sexual vulgarity,
> insults, threats and hateful statements, in 25 languages, some of it written by real people
> and published in research corpora. It exists to test moderation models. Do not use it to
> train or prompt a model to produce such content.

## Code

Everything under `bench/` and the checker `check_verdicts.py`: MIT, see [LICENSE](LICENSE).

## Data written for this benchmark

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), attribution
"Ruslan Moskalenko (Webmaster Ramos), jev-multilingual-benchmark":

- `data/src/` - the item specification and the written items, which were produced with a
  language model and are not a record of any real person's text
- `data/short/smoke.jsonl`, `data/long/smoke.jsonl`, and the built `full` and `clean` datasets
- the name templates, the transforms and the controls in `data/short/lexicon.jsonl`
- `results/` - model outputs as returned by each provider, and their summaries
- `review/` - the reviewer prompt, the review packages, the verdicts returned by the reviewing
  model (GPT-6.1 Sol), the reports and the per-item status

## Third-party data

Each entry ships only a sample, unchanged except for whitespace collapsing. Full lists and
corpora are not redistributed; `python -m bench.lexicon fetch` and `python -m bench.corpora
fetch` download them from their publishers at pinned revisions. Texts in the corpora belong to
their authors and the platforms they were posted on; the licences below cover the datasets as
published.

### Word lists - terms in `data/short/lexicon.jsonl` (`source` field)

| source | languages | licence | attribution |
|---|---|---|---|
| [LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | ar, cs, de, en, es, fi, fr, hi, hu, it, ja, ko, nl, pl, pt, ru, sv, th, tr, zh | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | List of Dirty, Naughty, Obscene, and Otherwise Bad Words, originally compiled at Shutterstock, maintained by its contributors |
| [vietnamese-offensive-words](https://github.com/blue-eyes-vn/vietnamese-offensive-words) | vi | MIT | Copyright (c) 2023 Blue Eyes - full notice in [LICENSES/MIT-vietnamese-offensive-words.txt](LICENSES/MIT-vietnamese-offensive-words.txt) |

### Corpora - comments in `data/long/comments.jsonl` (`source` field)

| corpus | language | licence | attribution |
|---|---|---|---|
| [Civil Comments](https://huggingface.co/datasets/google/civil_comments) | en | CC0 1.0 | Borkan et al., "Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification", 2019; Jigsaw |
| [RO-Offense](https://huggingface.co/datasets/readerbench/ro-offense) | ro | Apache-2.0, see [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt) | ReaderBench |
| [OLID-BR](https://huggingface.co/datasets/dougtrajano/olid-br) | pt | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Trajano, Bordini and Vieira, "OLID-BR: Offensive Language Identification Dataset for Brazilian Portuguese", 2023 |
| [OffensEval 2020](https://huggingface.co/datasets/strombergnlp/offenseval_2020) | tr, el, ar | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) per the dataset card | Zampieri et al., "SemEval-2020 Task 12: Multilingual Offensive Language Identification in Social Media", 2020; Turkish: Çöltekin 2020; Greek: Pitenis, Zampieri and Ranasinghe 2020; Arabic: Mubarak et al. 2020 |
| [IndoDiscourse](https://huggingface.co/datasets/Exqrch/IndoDiscourse) | id | Apache-2.0, see [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt) | Susanto et al., IndoToxic2024 / IndoDiscourse |
| [COLD](https://huggingface.co/datasets/thu-coai/COLD) | zh | Apache-2.0, see [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt) | Deng et al., "COLD: A Benchmark for Chinese Offensive Language Detection", 2022 |

Pinned revisions, selection rules and the label mapping: [data/lexicons/SOURCES.md](data/lexicons/SOURCES.md)
and [data/corpora/SOURCES.md](data/corpora/SOURCES.md).

