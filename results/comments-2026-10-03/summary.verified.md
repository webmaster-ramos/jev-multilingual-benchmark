# Run summary: `comments-2026-10-03`

## Per arm

| arm | model | items | errors | unparsed | accuracy | FP | FN | p50 ms | cost | uncertain p (0.3-0.7) | language id |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | google/gemini-2.5-flash-lite | 520 | 0 | 0 | 95% | 18 | 6 | 467 | $0.0280 | - | 99% |
| gemma4 | google/gemma-4-26b-a4b-it | 520 | 0 | 0 | 92% | 9 | 34 | 1200 | $0.0184 | - | 85% |
| gpt5mini | openai/gpt-5-mini | 520 | 0 | 0 | 89% | 57 | 0 | 2180 | $0.2514 | - | 88% |
| jev | jev-1.13.0 | 520 | 0 | 0 | 94% | 22 | 9 | 250 | $0.0245 | 14% | 100% |
| llamaguard | meta-llama/llama-guard-4-12b | 520 | 0 | 0 | 61% | 173 | 32 | 376 | $0.0268 | - | - |
| safeguard | openai/gpt-oss-safeguard-20b | 520 | 0 | 0 | 93% | 19 | 17 | 500 | $0.0713 | - | 99% |

FP = clean item flagged. FN = offensive item passed. Uncertain share applies to the decision arm only (Noul probability in the 0.3-0.7 band).

## Accuracy by language - long

| arm | ar | el | en | id | pt | ro | tr | zh |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | 100% | 92% | 98% | 92% | 88% | 98% | 96% | 98% |
| gemma4 | 100% | 85% | 94% | 95% | 84% | 85% | 97% | 95% |
| gpt5mini | 100% | 89% | 91% | 97% | 74% | 81% | 91% | 89% |
| jev | 97% | 88% | 98% | 95% | 81% | 95% | 99% | 98% |
| llamaguard | 49% | 64% | 71% | 63% | 51% | 63% | 49% | 77% |
| safeguard | 99% | 89% | 95% | 95% | 89% | 86% | 100% | 91% |

## Accuracy by variant

| arm | long flag corpus | long clean corpus |
|---|---:|---:|
| flashlite | 97% | 95% |
| gemma4 | 82% | 97% |
| gpt5mini | 100% | 83% |
| jev | 95% | 93% |
| llamaguard | 83% | 49% |
| safeguard | 91% | 94% |

## Flagged items caught, by language - long corpus

| arm | en | ro | pt | tr | el | ar | id | zh | all |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| flashlite | 12/13 | 41/42 | 23/24 | 13/14 | 41/41 | 22/22 | 15/17 | 11/11 | 178/184 |
| gemma4 | 9/13 | 32/42 | 16/24 | 13/14 | 35/41 | 22/22 | 14/17 | 9/11 | 150/184 |
| gpt5mini | 13/13 | 42/42 | 24/24 | 14/14 | 41/41 | 22/22 | 17/17 | 11/11 | 184/184 |
| jev | 12/13 | 40/42 | 20/24 | 14/14 | 40/41 | 21/22 | 17/17 | 11/11 | 175/184 |
| llamaguard | 3/13 | 42/42 | 11/24 | 14/14 | 34/41 | 22/22 | 16/17 | 10/11 | 152/184 |
| safeguard | 12/13 | 35/42 | 23/24 | 14/14 | 37/41 | 21/22 | 15/17 | 10/11 | 167/184 |

## Decision arm: the 0.3-0.7 band

- answers in the band: 74 of 520
- wrong answers: 31, of which outside the band (confidently wrong): 12
- accuracy on answers outside the band: 97% (434/446)
- routing (Jev outside the band, gpt5mini inside it): 92% (477/520), 14% of items routed

## Misses and failures

| arm | item | lang | label | verdict | p / conf | category | note |
|---|---|---|---|---|---:|---|---|
| flashlite | en-c-f-19 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | ro-c-f-16 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| flashlite | ro-c-c-25 | ro | clean | True | 0.90 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | pt-c-f-41 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-c-03 | pt | clean | True | 0.90 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-13 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-27 | pt | clean | True | 0.95 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-35 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-43 | pt | clean | True | 0.90 | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-f-29 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-c-17 | tr | clean | True | 0.90 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-c-34 | tr | clean | True | 0.90 | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-19 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-29 | el | clean | True | 0.80 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-46 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-47 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-55 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | id-c-f-23 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-41 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-c-19 | id | clean | True | 0.95 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-50 | id | clean | True | 0.80 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-60 | id | clean | True | 0.90 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | zh-c-c-15 | zh | clean | True | 0.85 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| gemma4 | en-c-f-02 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-06 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-39 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| gemma4 | en-c-f-46 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| gemma4 | ro-c-f-02 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-14 | ro | flag | False | 0.85 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| gemma4 | ro-c-f-15 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-16 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-17 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-20 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-43 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-47 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-51 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-57 | ro | flag | False | 0.98 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-c-25 | ro | clean | True | 0.95 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | ro-c-c-28 | ro | clean | True | 0.85 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | pt-c-f-01 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-16 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-20 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-21 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-31 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-41 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-58 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-60 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-c-25 | pt | clean | True | 0.85 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | tr-c-f-29 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-c-10 | tr | clean | True | 0.85 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gemma4 | el-c-f-03 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-17 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-22 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-31 | el | flag | False | 0.80 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-42 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-60 | el | flag | False | 0.85 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-c-46 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-47 | el | clean | True | 0.85 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-55 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-57 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | id-c-f-12 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-23 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-58 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | zh-c-f-06 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-33 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-c-15 | zh | clean | True | 0.92 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | en-c-c-05 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-06 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-07 | en | clean | True | 0.87 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-11 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-48 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-51 | en | clean | True | 0.85 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | ro-c-c-06 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-12 | ro | clean | True | 0.95 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-16 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-18 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-27 | ro | clean | True | 0.92 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-28 | ro | clean | True | 0.90 | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-30 | ro | clean | True | 0.92 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-32 | ro | clean | True | 0.80 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-38 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-41 | ro | clean | True | 0.89 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-44 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-45 | ro | clean | True | 0.82 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-47 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-50 | ro | clean | True | 0.90 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-54 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | pt-c-c-03 | pt | clean | True | 0.95 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-14 | pt | clean | True | 0.86 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-15 | pt | clean | True | 0.85 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-20 | pt | clean | True | 0.95 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-24 | pt | clean | True | 0.92 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-29 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-36 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-39 | pt | clean | True | 0.93 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-41 | pt | clean | True | 0.83 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-43 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-45 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-50 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-51 | pt | clean | True | 0.88 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-54 | pt | clean | True | 0.80 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-09 | tr | clean | True | 0.90 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-10 | tr | clean | True | 0.87 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-20 | tr | clean | True | 0.90 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-33 | tr | clean | True | 0.60 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-34 | tr | clean | True | 0.95 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-36 | tr | clean | True | 0.85 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-18 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-19 | el | clean | True | 0.88 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-29 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-46 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-47 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-55 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-57 | el | clean | True | 0.86 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | id-c-c-47 | id | clean | True | 0.90 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-50 | id | clean | True | 0.90 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | zh-c-c-15 | zh | clean | True | 0.90 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-25 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-27 | zh | clean | True | 0.85 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-41 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-45 | zh | clean | True | 0.90 | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-55 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | en-c-f-39 | en | flag | False | 0.48 | profanity | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| jev | ro-c-f-17 | ro | flag | False | 0.33 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-f-47 | ro | flag | False | 0.16 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-c-25 | ro | clean | True | 0.54 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-52 | ro | clean | True | 0.59 | none | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | pt-c-f-01 | pt | flag | False | 0.49 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-19 | pt | flag | False | 0.47 | profanity | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-31 | pt | flag | False | 0.27 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-41 | pt | flag | False | 0.17 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-c-03 | pt | clean | True | 0.84 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-25 | pt | clean | True | 0.59 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-36 | pt | clean | True | 0.50 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-38 | pt | clean | True | 0.75 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-41 | pt | clean | True | 0.54 | none | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-50 | pt | clean | True | 0.65 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-51 | pt | clean | True | 0.51 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | tr-c-c-34 | tr | clean | True | 0.75 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| jev | el-c-f-33 | el | flag | False | 0.47 | harassment | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| jev | el-c-c-19 | el | clean | True | 0.59 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-20 | el | clean | True | 0.80 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-29 | el | clean | True | 0.74 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-46 | el | clean | True | 0.69 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-47 | el | clean | True | 0.67 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-55 | el | clean | True | 0.87 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-57 | el | clean | True | 0.58 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | ar-c-f-12 | ar | flag | False | 0.29 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-c-18 | ar | clean | True | 0.50 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | id-c-c-09 | id | clean | True | 0.85 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-14 | id | clean | True | 0.70 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-50 | id | clean | True | 0.66 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | zh-c-c-15 | zh | clean | True | 0.93 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | en-c-f-06 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-07 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| llamaguard | en-c-f-18 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.85; mapped to flag/harassment |
| llamaguard | en-c-f-30 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.65; mapped to flag/profanity |
| llamaguard | en-c-f-39 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| llamaguard | en-c-f-43 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.73; mapped to flag/harassment |
| llamaguard | en-c-f-44 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| llamaguard | en-c-f-46 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| llamaguard | en-c-f-55 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.92; mapped to flag/harassment |
| llamaguard | en-c-f-56 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.75; mapped to flag/harassment |
| llamaguard | en-c-c-05 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-06 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-08 | en | clean | True | - | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-11 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-29 | en | clean | True | - | self_harm | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-48 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-49 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-50 | en | clean | True | - | violence | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-60 | en | clean | True | - | self_harm | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | ro-c-c-02 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-03 | ro | clean | True | - | sexual | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-05 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-06 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-09 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-11 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-12 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-16 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-18 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-21 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-23 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-25 | ro | clean | True | - | self_harm | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-26 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-27 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-28 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-30 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-31 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-32 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-33 | ro | clean | True | - | self_harm | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-34 | ro | clean | True | - | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-36 | ro | clean | True | - | sexual | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-38 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-39 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-44 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-45 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-46 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-49 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-54 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-56 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-58 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | pt-c-f-11 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-15 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-16 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-19 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-20 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-31 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-32 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-41 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-53 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-55 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-56 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-57 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-60 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-c-03 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-06 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-13 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-25 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-27 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-29 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-36 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-37 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-41 | pt | clean | True | - | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-43 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-45 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-46 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-54 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-58 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-60 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-01 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-04 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-07 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-09 | tr | clean | True | - | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-10 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-13 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-15 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-16 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-17 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-18 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-19 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-20 | tr | clean | True | - | sexual | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-21 | tr | clean | True | - | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-24 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-25 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-26 | tr | clean | True | - | sexual | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-28 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-30 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-31 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-32 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-33 | tr | clean | True | - | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-34 | tr | clean | True | - | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-35 | tr | clean | True | - | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-36 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-37 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-40 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-46 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-48 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-49 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-51 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-52 | tr | clean | True | - | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-53 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-55 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-56 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-60 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | el-c-f-01 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-07 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-22 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-25 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-33 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-42 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-51 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-c-18 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-19 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-20 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-22 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-24 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-28 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-29 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-33 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-38 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-39 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-40 | el | clean | True | - | sexual | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-44 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-46 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-47 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-49 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-54 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-56 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-01 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-03 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-04 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-07 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-13 | ar | clean | True | - | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-15 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-17 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-18 | ar | clean | True | - | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-19 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-22 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-23 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-24 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-25 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-26 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-27 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-28 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-30 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-31 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-32 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-33 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-35 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-38 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-40 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-41 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-44 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-45 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-46 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-47 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-49 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-50 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-51 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-52 | ar | clean | True | - | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-55 | ar | clean | True | - | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-56 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | id-c-f-11 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| llamaguard | id-c-c-01 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-06 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-07 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-08 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-09 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-14 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-21 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-22 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-26 | id | clean | True | - | self_harm | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-28 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-34 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-35 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-36 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-37 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-42 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-43 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-47 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-49 | id | clean | True | - | self_harm | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-50 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-53 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-60 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | zh-c-f-38 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-c-01 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-04 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-05 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-09 | zh | clean | True | - | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-15 | zh | clean | True | - | illegal | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-17 | zh | clean | True | - | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-22 | zh | clean | True | - | sexual | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-25 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-32 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-41 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-45 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-47 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| safeguard | en-c-f-46 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| safeguard | en-c-c-05 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| safeguard | en-c-c-06 | en | clean | True | 0.80 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| safeguard | ro-c-f-02 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| safeguard | ro-c-f-05 | ro | flag | False | 0.95 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-15 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-16 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-44 | ro | flag | False | 0.95 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-57 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-60 | ro | flag | False | 0.92 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-c-05 | ro | clean | True | 0.95 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-28 | ro | clean | True | 0.92 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-38 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-44 | ro | clean | True | 0.75 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | pt-c-f-53 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-c-03 | pt | clean | True | 0.85 | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-25 | pt | clean | True | 0.80 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-37 | pt | clean | True | 0.85 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-46 | pt | clean | True | 0.80 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | el-c-f-12 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-19 | el | flag | False | 0.99 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-20 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-33 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-c-46 | el | clean | True | 0.99 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-55 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-57 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | ar-c-f-12 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | id-c-f-21 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-57 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-c-07 | id | clean | True | 0.92 | profanity | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | zh-c-f-38 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-c-15 | zh | clean | True | 0.80 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-25 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-29 | zh | clean | True | 0.85 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-55 | zh | clean | True | 0.92 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
