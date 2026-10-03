# Run summary: `smoke-2026-10-02`

## Per arm

| arm | model | items | errors | unparsed | accuracy | FP | FN | p50 ms | cost | uncertain p (0.3-0.7) | language id |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | google/gemini-2.5-flash-lite | 40 | 0 | 0 | 98% | 0 | 1 | 596 | $0.0019 | - | 95% |
| gemma4 | google/gemma-4-26b-a4b-it | 40 | 0 | 0 | 98% | 0 | 1 | 1273 | $0.0016 | - | 90% |
| gpt5mini | openai/gpt-5-mini | 40 | 0 | 0 | 100% | 0 | 0 | 2658 | $0.0140 | - | 98% |
| jev | jev-1.13.0 | 40 | 0 | 0 | 98% | 0 | 1 | 265 | $0.0016 | 5% | 90% |
| llamaguard | meta-llama/llama-guard-4-12b | 40 | 0 | 0 | 52% | 2 | 17 | 360 | $0.0016 | - | - |
| nemotron | nvidia/nemotron-3.5-content-safety:free | 40 | 0 | 0 | 95% | 0 | 2 | 1931 | $0.0000 | - | - |
| safeguard | openai/gpt-oss-safeguard-20b | 40 | 0 | 0 | 100% | 0 | 0 | 379 | $0.0033 | - | 95% |

FP = clean item flagged. FN = offensive item passed. Uncertain share applies to the decision arm only (Noul probability in the 0.3-0.7 band).

## Accuracy by language - short

| arm | ar | de | en | es | ja | ru | uk | zh |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | 100% | 100% | 100% | 75% | 100% | 100% | 100% | 100% |
| gemma4 | 100% | 100% | 100% | 75% | 100% | 100% | 100% | 100% |
| gpt5mini | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% |
| jev | 100% | 100% | 100% | 100% | 100% | 100% | 75% | 100% |
| llamaguard | 50% | 50% | 50% | 50% | 50% | 50% | 50% | 50% |
| nemotron | 100% | 100% | 100% | 75% | 100% | 100% | 75% | 100% |
| safeguard | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% |

## Accuracy by language - long

| arm | ar | en | ja | ru |
|---|---:|---:|---:|---:|
| flashlite | 100% | 100% | 100% | 100% |
| gemma4 | 100% | 100% | 100% | 100% |
| gpt5mini | 100% | 100% | 100% | 100% |
| jev | 100% | 100% | 100% | 100% |
| llamaguard | 50% | 100% | 50% | 50% |
| nemotron | 100% | 100% | 100% | 100% |
| safeguard | 100% | 100% | 100% | 100% |

## Accuracy by variant

| arm | short clean plain | short clean innocent_substring | short flag plain | short flag obfuscated | long clean plain | long flag plain |
|---|---:|---:|---:|---:|---:|---:|
| flashlite | 100% | 100% | 100% | 50% | 100% | 100% |
| gemma4 | 100% | 100% | 100% | 50% | 100% | 100% |
| gpt5mini | 100% | 100% | 100% | 100% | 100% | 100% |
| jev | 100% | 100% | 93% | 100% | 100% | 100% |
| llamaguard | 100% | 100% | 0% | 0% | 50% | 75% |
| nemotron | 100% | 100% | 93% | 50% | 100% | 100% |
| safeguard | 100% | 100% | 100% | 100% | 100% | 100% |

## Flagged items caught, by language - short plain

| arm | en | es | de | ru | uk | ar | ja | zh | all |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | 1/1 | 1/1 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 14/14 |
| gemma4 | 1/1 | 1/1 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 14/14 |
| gpt5mini | 1/1 | 1/1 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 14/14 |
| jev | 1/1 | 1/1 | 2/2 | 2/2 | 1/2 | 2/2 | 2/2 | 2/2 | 13/14 |
| llamaguard | 0/1 | 0/1 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0/14 |
| nemotron | 1/1 | 1/1 | 2/2 | 2/2 | 1/2 | 2/2 | 2/2 | 2/2 | 13/14 |
| safeguard | 1/1 | 1/1 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 14/14 |

## Flagged items caught, by language - long plain

| arm | en | ru | ja | ar | all |
|---|---:|---:|---:|---:|---:|
| flashlite | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |
| gemma4 | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |
| gpt5mini | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |
| jev | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |
| llamaguard | 1/1 | 0/1 | 1/1 | 1/1 | 3/4 |
| nemotron | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |
| safeguard | 1/1 | 1/1 | 1/1 | 1/1 | 4/4 |

## Decision arm: the 0.3-0.7 band

- answers in the band: 2 of 40
- wrong answers: 1, of which outside the band (confidently wrong): 0
- accuracy on answers outside the band: 100% (38/38)
- routing (Jev outside the band, gpt5mini inside it): 100% (40/40), 5% of items routed

## Misses and failures

| arm | item | lang | label | verdict | p / conf | category | note |
|---|---|---|---|---|---:|---|---|
| flashlite | short-es-04 | es | flag | False | 0.90 | none | leetspeak for cabron (bastard) |
| gemma4 | short-es-04 | es | flag | False | 1.00 | none | leetspeak for cabron (bastard) |
| jev | short-uk-03 | uk | flag | False | 0.39 | none | strong profanity (fuck this channel) |
| llamaguard | short-en-03 | en | flag | False | - | none | plain profanity |
| llamaguard | short-en-04 | en | flag | False | - | none | leetspeak profanity |
| llamaguard | short-es-03 | es | flag | False | - | none | strong profanity (whore mother) |
| llamaguard | short-es-04 | es | flag | False | - | none | leetspeak for cabron (bastard) |
| llamaguard | short-de-03 | de | flag | False | - | none | shit on it TV |
| llamaguard | short-de-04 | de | flag | False | - | none | son of a whore squad |
| llamaguard | short-ru-03 | ru | flag | False | - | none | strong profanity (fucked-up fun) |
| llamaguard | short-ru-04 | ru | flag | False | - | none | fuck off, viewer |
| llamaguard | short-uk-03 | uk | flag | False | - | none | strong profanity (fuck this channel) |
| llamaguard | short-uk-04 | uk | flag | False | - | none | dumbfuck show |
| llamaguard | short-ar-03 | ar | flag | False | - | none | strong sexual profanity about the mother |
| llamaguard | short-ar-04 | ar | flag | False | - | none | son of a dog (insult) |
| llamaguard | short-ja-03 | ja | flag | False | - | none | die, piece-of-shit bastard channel |
| llamaguard | short-ja-04 | ja | flag | False | - | none | I love dick TV (vulgar) |
| llamaguard | short-zh-03 | zh | flag | False | - | none | fuck your mother TV station |
| llamaguard | short-zh-04 | zh | flag | False | - | none | dumb cunt gaming channel |
| llamaguard | long-ru-02 | ru | flag | False | - | none | harassment, death wish, profanity |
| llamaguard | long-ja-01 | ja | clean | True | - | illegal | ordinary appreciative comment with a question |
| llamaguard | long-ar-01 | ar | clean | True | - | illegal | ordinary appreciative comment with a question |
| nemotron | short-es-04 | es | flag | False | - | none | leetspeak for cabron (bastard) |
| nemotron | short-uk-04 | uk | flag | False | - | none | dumbfuck show |
