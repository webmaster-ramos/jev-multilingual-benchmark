# Lexicon sources

The `lexicon` dataset takes its flagged terms from published word lists, not from a language
model. Ten terms per language are sampled with a fixed seed; `bench/lexicon.py` wraps each in a
name template and produces a disguised copy by code. The lists themselves are not vendored:
`python -m bench.lexicon fetch` downloads the pinned versions into `data/lexicons/_cache/`
(git-ignored). Only the sampled terms ship, inside `data/short/lexicon.jsonl`.

| languages | list | pinned at | licence |
|---|---|---|---|
| ar, cs, de, en, es, fi, fr, hi, hu, it, ja, ko, nl, pl, pt, ru, sv, th, tr, zh | [LDNOOBW - List of Dirty, Naughty, Obscene, and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | commit `5faf2ba` | CC BY 4.0 |
| vi | [blue-eyes-vn/vietnamese-offensive-words](https://github.com/blue-eyes-vn/vietnamese-offensive-words) | commit `684b568` | MIT |
| ro, el, id | none found with a clear licence | | |
| uk | removed on 2026-10-03 - see below | | |

Terms are used under those licences with attribution to the list authors. The LDNOOBW lists
were originally compiled at Shutterstock and are maintained by contributors.

**Ukrainian removed (2026-10-03).** The only Ukrainian list found, the `uk` split of
`textdetox/multilingual_toxic_lexicon`, is published under OpenRAIL++ while its upstream,
`saganoren/obscene-ukr`, states no licence. Its 20 items were removed from the dataset, the
results and the review rather than shipped on unclear terms. Ukrainian keeps its clean names
and controls.

## What a list term is and is not

- **Flagged by list membership.** Nobody in this project judged the terms. A list can contain a
  mild or ambiguous word; `lexicon_plain` recall therefore mixes "the model does not know the
  word" with "the word is not that bad". The paired design does not depend on it: for every
  term a model catches in plain form, the disguised copy is the same word.
- **Selection rules** (in `eligible_terms`): one token (two for Vietnamese), letters of the
  language's script only, 4-9 characters for alphabetic scripts (4-7 for Cyrillic, to prefer
  base forms in a list full of inflections), 3-9 for Arabic and Thai, 2-6 for Japanese, Korean
  and Chinese. For Latin-script languages other than English, terms that also sit in the
  English list are dropped, so each language is tested on its own words.
- **Hindi is romanised.** The LDNOOBW Hindi list is written in Latin letters, the way Hindi
  profanity is commonly typed, so Hindi terms are Latin-script and get the Latin transforms.
- **Chinese** terms are taken as listed, without separating Simplified from Traditional.
- **A machine-translated list was rejected.** `washyourmouthoutwithsoap` covers 23 of the 25
  languages, but its non-English lists are Google Translate output of an English list.

## Transforms

| technique | what the code does | scripts |
|---|---|---|
| `leet` | digits for letters (`a`→4, `e`→3, `i`→1, `o`→0, `s`→5; Cyrillic and Greek equivalents) | Latin, Cyrillic, Greek |
| `homoglyph` | look-alike letters from another alphabet (Latin↔Cyrillic, Greek→Latin) | Latin, Cyrillic, Greek |
| `spaced` | a dot between characters | all |
| `stretched` | one character tripled - the first vowel where the script has vowels | all |
| `masked` | one character replaced by `*` | all |

Alphabetic scripts rotate through all five; Arabic, Thai, Japanese, Korean and Chinese through
the last three. If a technique changes nothing in a term (no mappable letter), the next one in
the rotation is used and recorded.

The same rotation is applied to one word of five clean names per language
(`control_obfuscated`). A flag on those is a false positive caused by how the text looks.
