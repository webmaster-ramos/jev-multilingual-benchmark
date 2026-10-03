# Corpus sources for the `comments` dataset

The `comments` dataset holds 960 comments in 8 languages, 60 flagged and 60 clean per language,
all from published corpora labelled by people. Nothing in it is written by a model. For each
language both classes come from the same corpus, so an arm cannot tell them apart by style.
`python -m bench.corpora fetch` downloads the pinned files into `data/corpora/_cache/`
(git-ignored); only the sampled rows ship, in `data/long/comments.jsonl`, with the corpus name
and the original label in every row's `note`.

| lang | corpus | text source | annotation | pinned revision | licence |
|---|---|---|---|---|---|
| en | Civil Comments (Jigsaw, 2019), HF `google/civil_comments`, validation split | news-site comments | crowd toxicity scores (fraction of raters) | `29b3493cb776` (parquet) | CC0-1.0 |
| ro | RO-Offense (2023), HF `readerbench/ro-offense` | gsp.ro sports-news comments | native annotators, four classes | `f3be6e4497e6` (parquet) | Apache-2.0 |
| pt | OLID-BR (2022), HF `dougtrajano/olid-br` | YouTube and Twitter comments | qualified annotators, offensive flag plus categories | `77fea0787188` (parquet) | CC-BY-4.0 |
| tr | OffensEval 2020 Turkish (Çöltekin), HF `strombergnlp/offenseval_2020` `tr` | tweets | native annotators, OFF / NOT | `fb4638001485` (parquet) | CC-BY-4.0 per the card |
| el | OffensEval 2020 Greek, OGTD (Pitenis et al.), same repo, `gr` | tweets | volunteer annotators, OFF / NOT | same | CC-BY-4.0 per the card |
| ar | OffensEval 2020 Arabic, OSACT4 (Mubarak et al.), same repo, `ar` | tweets | native annotators, OFF / NOT | same | CC-BY-4.0 per the card |
| id | IndoDiscourse (2025), HF `Exqrch/IndoDiscourse` | X, Facebook, Instagram, news | multiple annotators, toxicity per annotator | `4ec83f7c63a6` (parquet) | Apache-2.0 |
| zh | COLD (2022, Tsinghua), HF `thu-coai/COLD`, `train.csv` | Zhihu and Weibo | native annotators, offensive / safe, topics race, region, gender | `a31e56eb008a` | Apache-2.0 |

Texts belong to their authors and platforms; the licences above cover the datasets as
published, not platform terms. Tweets carry the corpora's own `@USER` and `URL` placeholders.

## Selection and label mapping

- Length 150-600 characters (Chinese 80-600), whitespace collapsed, duplicates dropped, 60 per
  class sampled with a fixed seed.
- **en:** toxicity at least 0.6 is `flag`; at most 0.05 with every subtype at most 0.05 is
  `clean`; the rest is skipped. Category: the strongest subtype at 0.3 or more (obscene ->
  profanity, threat -> violence, insult -> harassment, identity_attack -> hate), else
  harassment.
- **ro:** OTHER -> clean; PROFANITY -> profanity; INSULT -> harassment; ABUSE -> hate.
- **pt:** NOT -> clean; OFF -> flag, hate if any identity flag is set, harassment if `insult`,
  else profanity.
- **tr, el, ar:** OFF -> flag (category profanity: the OffensEval label covers profanity and
  targeted offence alike), NOT -> clean.
- **id:** both annotators toxic -> flag (profanity if either marks profanity, else harassment);
  both non-toxic -> clean; split votes skipped.
- **zh:** label 1 -> flag (category hate: the corpus is built around race, region and gender),
  label 0 -> clean.

Corpus labels follow each corpus's own guidelines, not this benchmark's policy. The mapping
above is a choice; the blind review (`review/package-comments/`) judges every comment under
the benchmark policy, and only items where the two agree are scored.

## Considered and not used

- **BAN-PL** (Polish, CC-BY-4.0): the authors password-protect the archive to prevent
  automated use. Republishing sampled rows in an open benchmark would go against that intent.
- **Toxic Russian Comments** (ok.ru, CC-BY-NC-SA) and **Thai Toxicity Tweet Corpus**
  (CC-BY-NC): non-commercial licences; this repository belongs to a commercial brand.
- **K-MHaS** (Korean) and **ukr-toxicity-dataset** (Ukrainian): too short for the comment task
  (medians 26 and 55 characters).
- **Jigsaw Multilingual** (CC0): no mirror with text and labels found outside Kaggle.
- **DALC** (Dutch), **MACD** (Hindi), **ViHSD** (Vietnamese): gated or without a stated licence.
