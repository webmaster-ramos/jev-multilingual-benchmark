# Run summary: `comments-2026-10-07`

## Per arm

| arm | model | items | errors | unparsed | accuracy | FP | FN | p50 ms | cost | uncertain p (0.3-0.7) | language id |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| decisions | gpt-6-luna | 960 | 0 | 0 | 76% | 64 | 162 | 242 | $0.0971 | 8% | 100% |
| flashlite | google/gemini-2.5-flash-lite | 960 | 0 | 0 | 75% | 71 | 170 | 466 | $0.0516 | - | 99% |
| gemma4 | google/gemma-4-26b-a4b-it | 960 | 0 | 0 | 68% | 47 | 259 | 1155 | $0.0340 | - | 87% |
| gpt5mini | openai/gpt-5-mini | 960 | 0 | 0 | 78% | 163 | 52 | 2272 | $0.4954 | - | 90% |
| jev | jev-1.13.0 | 960 | 0 | 0 | 76% | 97 | 132 | 250 | $0.0452 | 27% | 100% |
| llamaguard | meta-llama/llama-guard-4-12b | 960 | 0 | 0 | 59% | 271 | 124 | 380 | $0.0493 | - | - |
| luna | openai/gpt-6-luna | 960 | 0 | 0 | 77% | 96 | 126 | 2488 | $0.1081 | - | 99% |
| safeguard | openai/gpt-oss-safeguard-20b | 960 | 0 | 0 | 74% | 71 | 177 | 558 | $0.1481 | - | 98% |

FP = clean item flagged. FN = offensive item passed. Uncertain share applies to the decision arm only (Noul probability in the 0.3-0.7 band).

## Accuracy by language - long

| arm | ar | el | en | id | pt | ro | tr | zh |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| decisions | 92% | 76% | 74% | 75% | 72% | 90% | 74% | 59% |
| flashlite | 89% | 76% | 73% | 74% | 69% | 91% | 65% | 62% |
| gemma4 | 87% | 72% | 61% | 61% | 63% | 80% | 62% | 59% |
| gpt5mini | 92% | 68% | 88% | 85% | 68% | 73% | 80% | 68% |
| jev | 86% | 73% | 72% | 80% | 66% | 88% | 74% | 70% |
| llamaguard | 59% | 57% | 54% | 68% | 49% | 59% | 62% | 63% |
| luna | 92% | 72% | 79% | 73% | 77% | 86% | 73% | 62% |
| safeguard | 89% | 74% | 71% | 76% | 70% | 83% | 69% | 61% |

## Accuracy by variant

| arm | long flag corpus | long clean corpus |
|---|---:|---:|
| decisions | 66% | 87% |
| flashlite | 65% | 85% |
| gemma4 | 46% | 90% |
| gpt5mini | 89% | 66% |
| jev | 72% | 80% |
| llamaguard | 74% | 44% |
| luna | 74% | 80% |
| safeguard | 63% | 85% |

## Flagged items caught, by language - long corpus

| arm | en | ro | pt | tr | el | ar | id | zh | all |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| decisions | 30/60 | 57/60 | 34/60 | 30/60 | 56/60 | 56/60 | 36/60 | 19/60 | 318/480 |
| flashlite | 31/60 | 56/60 | 40/60 | 22/60 | 54/60 | 49/60 | 36/60 | 22/60 | 310/480 |
| gemma4 | 14/60 | 41/60 | 21/60 | 18/60 | 43/60 | 44/60 | 23/60 | 17/60 | 221/480 |
| gpt5mini | 56/60 | 60/60 | 55/60 | 45/60 | 59/60 | 57/60 | 54/60 | 42/60 | 428/480 |
| jev | 30/60 | 54/60 | 42/60 | 33/60 | 57/60 | 50/60 | 49/60 | 33/60 | 348/480 |
| llamaguard | 16/60 | 59/60 | 26/60 | 52/60 | 51/60 | 59/60 | 54/60 | 39/60 | 356/480 |
| luna | 35/60 | 60/60 | 45/60 | 31/60 | 55/60 | 58/60 | 40/60 | 30/60 | 354/480 |
| safeguard | 28/60 | 48/60 | 38/60 | 25/60 | 49/60 | 50/60 | 36/60 | 29/60 | 303/480 |

## Decision arm: the 0.3-0.7 band

- answers in the band: 260 of 960
- wrong answers: 229, of which outside the band (confidently wrong): 118
- accuracy on answers outside the band: 83% (582/700)
- routing (Jev outside the band, gpt5mini inside it): 78% (744/960), 27% of items routed

## Misses and failures

| arm | item | lang | label | verdict | p / conf | category | note |
|---|---|---|---|---|---:|---|---|
| decisions | en-c-f-04 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-05 | en | flag | False | 0.03 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| decisions | en-c-f-08 | en | flag | False | 0.09 | harassment | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| decisions | en-c-f-09 | en | flag | False | 0.13 | harassment | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-10 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| decisions | en-c-f-12 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-13 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-14 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| decisions | en-c-f-15 | en | flag | False | 0.03 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-17 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| decisions | en-c-f-20 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| decisions | en-c-f-21 | en | flag | False | 0.04 | hate | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| decisions | en-c-f-22 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| decisions | en-c-f-23 | en | flag | False | 0.04 | harassment | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| decisions | en-c-f-27 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| decisions | en-c-f-28 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-29 | en | flag | False | 0.21 | harassment | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| decisions | en-c-f-30 | en | flag | False | 0.46 | sexual | Civil Comments: corpus label toxicity 0.65; mapped to flag/profanity |
| decisions | en-c-f-31 | en | flag | False | 0.03 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| decisions | en-c-f-32 | en | flag | False | 0.22 | hate | Civil Comments: corpus label toxicity 0.70; mapped to flag/hate |
| decisions | en-c-f-33 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| decisions | en-c-f-34 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-35 | en | flag | False | 0.41 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-37 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-38 | en | flag | False | 0.02 | harassment | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| decisions | en-c-f-40 | en | flag | False | 0.00 | harassment | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| decisions | en-c-f-47 | en | flag | False | 0.02 | harassment | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-48 | en | flag | False | 0.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| decisions | en-c-f-51 | en | flag | False | 0.02 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| decisions | en-c-f-59 | en | flag | False | 0.01 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| decisions | en-c-c-16 | en | clean | True | 0.83 | profanity | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| decisions | ro-c-f-12 | ro | flag | False | 0.06 | harassment | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| decisions | ro-c-f-18 | ro | flag | False | 0.24 | profanity | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| decisions | ro-c-f-47 | ro | flag | False | 0.18 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| decisions | ro-c-c-04 | ro | clean | True | 0.73 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-13 | ro | clean | True | 0.62 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-17 | ro | clean | True | 0.55 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-19 | ro | clean | True | 0.85 | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-24 | ro | clean | True | 0.88 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-35 | ro | clean | True | 0.63 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-48 | ro | clean | True | 0.82 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-57 | ro | clean | True | 0.66 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | ro-c-c-60 | ro | clean | True | 0.87 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| decisions | pt-c-f-02 | pt | flag | False | 0.00 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-12 | pt | flag | False | 0.12 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-17 | pt | flag | False | 0.01 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-20 | pt | flag | False | 0.20 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-22 | pt | flag | False | 0.03 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-24 | pt | flag | False | 0.00 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-25 | pt | flag | False | 0.05 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-26 | pt | flag | False | 0.14 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-27 | pt | flag | False | 0.02 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-28 | pt | flag | False | 0.14 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-29 | pt | flag | False | 0.23 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-32 | pt | flag | False | 0.41 | hate | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-33 | pt | flag | False | 0.10 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-34 | pt | flag | False | 0.00 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-35 | pt | flag | False | 0.23 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-36 | pt | flag | False | 0.19 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-37 | pt | flag | False | 0.10 | hate | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-40 | pt | flag | False | 0.02 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-41 | pt | flag | False | 0.01 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-42 | pt | flag | False | 0.00 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-47 | pt | flag | False | 0.15 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-48 | pt | flag | False | 0.00 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-49 | pt | flag | False | 0.00 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-f-51 | pt | flag | False | 0.30 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-53 | pt | flag | False | 0.26 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| decisions | pt-c-f-54 | pt | flag | False | 0.01 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| decisions | pt-c-c-07 | pt | clean | True | 0.96 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-11 | pt | clean | True | 0.88 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-18 | pt | clean | True | 0.92 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-23 | pt | clean | True | 0.88 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-28 | pt | clean | True | 0.80 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-33 | pt | clean | True | 0.56 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-43 | pt | clean | True | 0.57 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | pt-c-c-47 | pt | clean | True | 0.84 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| decisions | tr-c-f-02 | tr | flag | False | 0.17 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-03 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-06 | tr | flag | False | 0.22 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-08 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-09 | tr | flag | False | 0.04 | hate | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-11 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-13 | tr | flag | False | 0.24 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-14 | tr | flag | False | 0.00 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-15 | tr | flag | False | 0.04 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-18 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-19 | tr | flag | False | 0.05 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-20 | tr | flag | False | 0.02 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-21 | tr | flag | False | 0.29 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-23 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-26 | tr | flag | False | 0.07 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-28 | tr | flag | False | 0.39 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-30 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-34 | tr | flag | False | 0.25 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-36 | tr | flag | False | 0.18 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-37 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-40 | tr | flag | False | 0.17 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-43 | tr | flag | False | 0.02 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-44 | tr | flag | False | 0.02 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-45 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-49 | tr | flag | False | 0.01 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-50 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-51 | tr | flag | False | 0.10 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-53 | tr | flag | False | 0.01 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-55 | tr | flag | False | 0.01 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-f-59 | tr | flag | False | 0.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| decisions | tr-c-c-59 | tr | clean | True | 0.79 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| decisions | el-c-f-36 | el | flag | False | 0.05 | hate | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| decisions | el-c-f-40 | el | flag | False | 0.03 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| decisions | el-c-f-52 | el | flag | False | 0.13 | harassment | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| decisions | el-c-f-56 | el | flag | False | 0.12 | hate | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| decisions | el-c-c-01 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-02 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-04 | el | clean | True | 0.56 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-07 | el | clean | True | 0.99 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-09 | el | clean | True | 0.89 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-10 | el | clean | True | 0.74 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-11 | el | clean | True | 0.96 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-13 | el | clean | True | 0.79 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-14 | el | clean | True | 0.99 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-16 | el | clean | True | 0.93 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-17 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-20 | el | clean | True | 0.52 | none | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-21 | el | clean | True | 0.71 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-23 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-25 | el | clean | True | 0.93 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-27 | el | clean | True | 0.81 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-34 | el | clean | True | 0.89 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-35 | el | clean | True | 0.81 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-42 | el | clean | True | 1.00 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-43 | el | clean | True | 0.97 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-45 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-47 | el | clean | True | 0.60 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-53 | el | clean | True | 0.78 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-55 | el | clean | True | 0.61 | none | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | el-c-c-58 | el | clean | True | 0.74 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| decisions | ar-c-f-25 | ar | flag | False | 0.23 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| decisions | ar-c-f-39 | ar | flag | False | 0.35 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| decisions | ar-c-f-48 | ar | flag | False | 0.09 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| decisions | ar-c-f-59 | ar | flag | False | 0.00 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| decisions | ar-c-c-08 | ar | clean | True | 0.56 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | ar-c-c-09 | ar | clean | True | 0.81 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | ar-c-c-10 | ar | clean | True | 0.61 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | ar-c-c-37 | ar | clean | True | 0.61 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | ar-c-c-39 | ar | clean | True | 0.64 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | ar-c-c-59 | ar | clean | True | 0.53 | none | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| decisions | id-c-f-01 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-04 | id | flag | False | 0.06 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-07 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-08 | id | flag | False | 0.26 | harassment | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-09 | id | flag | False | 0.13 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-10 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-12 | id | flag | False | 0.45 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-14 | id | flag | False | 0.02 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-17 | id | flag | False | 0.04 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-20 | id | flag | False | 0.37 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-31 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-33 | id | flag | False | 0.27 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-37 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-43 | id | flag | False | 0.02 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-46 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-49 | id | flag | False | 0.39 | hate | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| decisions | id-c-f-50 | id | flag | False | 0.08 | hate | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-51 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-52 | id | flag | False | 0.02 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-53 | id | flag | False | 0.25 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-55 | id | flag | False | 0.02 | hate | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-56 | id | flag | False | 0.14 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-58 | id | flag | False | 0.04 | hate | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-f-60 | id | flag | False | 0.00 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| decisions | id-c-c-11 | id | clean | True | 0.82 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | id-c-c-14 | id | clean | True | 0.53 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | id-c-c-20 | id | clean | True | 0.50 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | id-c-c-24 | id | clean | True | 0.81 | none | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | id-c-c-48 | id | clean | True | 0.97 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | id-c-c-52 | id | clean | True | 0.62 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| decisions | zh-c-f-01 | zh | flag | False | 0.28 | harassment | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-02 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-03 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-04 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-08 | zh | flag | False | 0.27 | harassment | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-10 | zh | flag | False | 0.08 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-11 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-12 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-14 | zh | flag | False | 0.38 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-15 | zh | flag | False | 0.07 | hate | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-16 | zh | flag | False | 0.25 | hate | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-18 | zh | flag | False | 0.20 | hate | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-19 | zh | flag | False | 0.02 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-21 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-22 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-23 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-24 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-29 | zh | flag | False | 0.15 | hate | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-30 | zh | flag | False | 0.10 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-31 | zh | flag | False | 0.02 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-32 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-35 | zh | flag | False | 0.02 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-37 | zh | flag | False | 0.09 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-39 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-40 | zh | flag | False | 0.03 | hate | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-42 | zh | flag | False | 0.05 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-43 | zh | flag | False | 0.11 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-44 | zh | flag | False | 0.02 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-45 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-46 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-47 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-48 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-49 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-50 | zh | flag | False | 0.01 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-51 | zh | flag | False | 0.06 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-53 | zh | flag | False | 0.11 | harassment | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-55 | zh | flag | False | 0.32 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-f-56 | zh | flag | False | 0.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-57 | zh | flag | False | 0.37 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-59 | zh | flag | False | 0.02 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| decisions | zh-c-f-60 | zh | flag | False | 0.04 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| decisions | zh-c-c-02 | zh | clean | True | 0.97 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| decisions | zh-c-c-03 | zh | clean | True | 1.00 | sexual | COLD: corpus label label 0 (race); mapped to clean/none |
| decisions | zh-c-c-08 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| decisions | zh-c-c-15 | zh | clean | True | 0.94 | none | COLD: corpus label label 0 (race); mapped to clean/none |
| decisions | zh-c-c-21 | zh | clean | True | 1.00 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| decisions | zh-c-c-28 | zh | clean | True | 0.91 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| decisions | zh-c-c-44 | zh | clean | True | 0.75 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| decisions | zh-c-c-55 | zh | clean | True | 0.75 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | en-c-f-04 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-05 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| flashlite | en-c-f-08 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| flashlite | en-c-f-09 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-10 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| flashlite | en-c-f-12 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-14 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| flashlite | en-c-f-15 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-17 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | en-c-f-19 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | en-c-f-20 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| flashlite | en-c-f-21 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| flashlite | en-c-f-22 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| flashlite | en-c-f-23 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| flashlite | en-c-f-24 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| flashlite | en-c-f-27 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | en-c-f-28 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-29 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | en-c-f-33 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| flashlite | en-c-f-35 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-36 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| flashlite | en-c-f-37 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-38 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| flashlite | en-c-f-40 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| flashlite | en-c-f-47 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-48 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| flashlite | en-c-f-51 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| flashlite | en-c-f-58 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.61; mapped to flag/harassment |
| flashlite | en-c-f-60 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.72; mapped to flag/harassment |
| flashlite | en-c-c-16 | en | clean | True | 0.80 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| flashlite | en-c-c-21 | en | clean | True | 0.80 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| flashlite | en-c-c-45 | en | clean | True | 0.90 | violence | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| flashlite | ro-c-f-16 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| flashlite | ro-c-f-26 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| flashlite | ro-c-f-41 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| flashlite | ro-c-f-58 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| flashlite | ro-c-c-01 | ro | clean | True | 0.80 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-04 | ro | clean | True | 0.80 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-17 | ro | clean | True | 0.85 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-24 | ro | clean | True | 0.80 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-25 | ro | clean | True | 0.90 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-48 | ro | clean | True | 0.80 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | ro-c-c-60 | ro | clean | True | 0.90 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| flashlite | pt-c-f-02 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-10 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-12 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-17 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-22 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-24 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-26 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-28 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-33 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-34 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-35 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-37 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-39 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-40 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-41 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-42 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-48 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| flashlite | pt-c-f-49 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-52 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-f-54 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| flashlite | pt-c-c-03 | pt | clean | True | 0.90 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-04 | pt | clean | True | 0.90 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-07 | pt | clean | True | 0.90 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-11 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-13 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-18 | pt | clean | True | 0.90 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-22 | pt | clean | True | 0.90 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-23 | pt | clean | True | 0.80 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-27 | pt | clean | True | 0.95 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-28 | pt | clean | True | 0.80 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-32 | pt | clean | True | 0.95 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-34 | pt | clean | True | 0.90 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-35 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-43 | pt | clean | True | 0.90 | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-47 | pt | clean | True | 0.90 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | pt-c-c-48 | pt | clean | True | 0.85 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-f-01 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-02 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-03 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-04 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-05 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-06 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-08 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-09 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-11 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-13 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-14 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-15 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-16 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-17 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-18 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-20 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-21 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-23 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-24 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-25 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-26 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-28 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-29 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-30 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-34 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-37 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-40 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-42 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-43 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-44 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-45 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-50 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-51 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-53 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-55 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-56 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-58 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-f-59 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| flashlite | tr-c-c-17 | tr | clean | True | 0.90 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-c-34 | tr | clean | True | 0.90 | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-c-41 | tr | clean | True | 0.90 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | tr-c-c-59 | tr | clean | True | 0.80 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| flashlite | el-c-f-21 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-f-36 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-f-39 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-f-40 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-f-52 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-f-56 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| flashlite | el-c-c-02 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-07 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-11 | el | clean | True | 0.80 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-13 | el | clean | True | 0.80 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-14 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-17 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-19 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-21 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-23 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-25 | el | clean | True | 0.80 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-27 | el | clean | True | 0.80 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-29 | el | clean | True | 0.80 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-32 | el | clean | True | 0.80 | violence | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-34 | el | clean | True | 0.80 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-42 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-43 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-45 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-46 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-47 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-50 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-52 | el | clean | True | 0.80 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-55 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | el-c-c-58 | el | clean | True | 0.80 | sexual | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| flashlite | ar-c-f-01 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-04 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-07 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-10 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-25 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-26 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-39 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-45 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-48 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-50 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-f-59 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| flashlite | ar-c-c-09 | ar | clean | True | 0.80 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| flashlite | ar-c-c-10 | ar | clean | True | 0.80 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| flashlite | id-c-f-01 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-02 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| flashlite | id-c-f-04 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-05 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-06 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-07 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-08 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-10 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-16 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| flashlite | id-c-f-17 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-23 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-31 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-35 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-37 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-40 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-41 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-42 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-43 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-46 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-49 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| flashlite | id-c-f-51 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-53 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-55 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-f-56 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| flashlite | id-c-c-19 | id | clean | True | 0.95 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-24 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-30 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-32 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-48 | id | clean | True | 0.90 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-50 | id | clean | True | 0.80 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | id-c-c-60 | id | clean | True | 0.90 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| flashlite | zh-c-f-02 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-03 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-04 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-05 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-07 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-11 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-12 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-13 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-14 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-15 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-16 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-18 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-19 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-21 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-22 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-24 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-29 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-30 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-31 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-32 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-35 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-37 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-39 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-40 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-42 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-44 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-45 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-46 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-47 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-48 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-49 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-50 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-51 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-53 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-55 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-f-56 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-59 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| flashlite | zh-c-f-60 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| flashlite | zh-c-c-02 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| flashlite | zh-c-c-03 | zh | clean | True | 0.90 | sexual | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | zh-c-c-08 | zh | clean | True | 0.85 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | zh-c-c-15 | zh | clean | True | 0.85 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | zh-c-c-21 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | zh-c-c-28 | zh | clean | True | 0.90 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| flashlite | zh-c-c-43 | zh | clean | True | 0.80 | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| flashlite | zh-c-c-44 | zh | clean | True | 0.80 | self_harm | COLD: corpus label label 0 (region); mapped to clean/none |
| gemma4 | en-c-f-02 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-04 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-05 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| gemma4 | en-c-f-06 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-08 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| gemma4 | en-c-f-09 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-10 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| gemma4 | en-c-f-12 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-13 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-14 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| gemma4 | en-c-f-15 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-16 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-17 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-20 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| gemma4 | en-c-f-21 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| gemma4 | en-c-f-22 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| gemma4 | en-c-f-23 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| gemma4 | en-c-f-24 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| gemma4 | en-c-f-26 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/hate |
| gemma4 | en-c-f-27 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-28 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-29 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-31 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| gemma4 | en-c-f-33 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-34 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-35 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-36 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| gemma4 | en-c-f-37 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-38 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| gemma4 | en-c-f-39 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| gemma4 | en-c-f-40 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| gemma4 | en-c-f-41 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.76; mapped to flag/harassment |
| gemma4 | en-c-f-42 | en | flag | False | 0.92 | none | Civil Comments: corpus label toxicity 0.65; mapped to flag/harassment |
| gemma4 | en-c-f-45 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| gemma4 | en-c-f-46 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| gemma4 | en-c-f-47 | en | flag | False | 1.00 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-48 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-49 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| gemma4 | en-c-f-51 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| gemma4 | en-c-f-52 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gemma4 | en-c-f-53 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/hate |
| gemma4 | en-c-f-54 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gemma4 | en-c-f-57 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| gemma4 | en-c-f-58 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.61; mapped to flag/harassment |
| gemma4 | en-c-f-59 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| gemma4 | en-c-f-60 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.72; mapped to flag/harassment |
| gemma4 | en-c-c-21 | en | clean | True | 0.70 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gemma4 | ro-c-f-02 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-12 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-14 | ro | flag | False | 0.85 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| gemma4 | ro-c-f-15 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-16 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-17 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-18 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-20 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-25 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-26 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-28 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-33 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-41 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-43 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-47 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| gemma4 | ro-c-f-51 | ro | flag | False | 0.85 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-57 | ro | flag | False | 0.98 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-58 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| gemma4 | ro-c-f-59 | ro | flag | False | 0.95 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| gemma4 | ro-c-c-04 | ro | clean | True | 0.85 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | ro-c-c-13 | ro | clean | True | 0.85 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | ro-c-c-17 | ro | clean | True | 0.70 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | ro-c-c-25 | ro | clean | True | 0.95 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | ro-c-c-28 | ro | clean | True | 0.85 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gemma4 | pt-c-f-01 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-02 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-03 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-04 | pt | flag | False | 0.85 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-06 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-08 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-09 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-10 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-12 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-16 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-17 | pt | flag | False | 1.00 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-18 | pt | flag | False | 0.85 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-20 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-21 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-22 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-24 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-25 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-26 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-27 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-28 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-29 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-31 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-33 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-34 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-37 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-38 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-39 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-40 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-41 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-42 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-47 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-48 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-49 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-50 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-51 | pt | flag | False | 0.85 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-52 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-54 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gemma4 | pt-c-f-58 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-f-60 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gemma4 | pt-c-c-04 | pt | clean | True | 0.85 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | pt-c-c-11 | pt | clean | True | 0.98 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | pt-c-c-18 | pt | clean | True | 0.95 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | pt-c-c-25 | pt | clean | True | 0.85 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | pt-c-c-47 | pt | clean | True | 0.85 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gemma4 | tr-c-f-01 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-02 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-03 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-05 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-06 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-08 | tr | flag | False | 1.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-09 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-11 | tr | flag | False | 1.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-13 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-14 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-15 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-16 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-18 | tr | flag | False | 1.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-20 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-21 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-23 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-25 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-26 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-28 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-29 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-30 | tr | flag | False | 1.00 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-31 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-34 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-35 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-36 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-37 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-40 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-41 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-42 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-43 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-44 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-45 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-49 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-50 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-51 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-53 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-54 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-55 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-57 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-58 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-59 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-f-60 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gemma4 | tr-c-c-10 | tr | clean | True | 0.85 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gemma4 | tr-c-c-41 | tr | clean | True | 0.92 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gemma4 | tr-c-c-59 | tr | clean | True | 0.85 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gemma4 | el-c-f-02 | el | flag | False | 0.85 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-03 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-10 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-14 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-15 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-17 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-21 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-22 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-29 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-31 | el | flag | False | 0.80 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-36 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-39 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-42 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-43 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-52 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-56 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-f-60 | el | flag | False | 0.85 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gemma4 | el-c-c-01 | el | clean | True | 0.85 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-02 | el | clean | True | 0.92 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-10 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-11 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-13 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-17 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-25 | el | clean | True | 0.95 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-26 | el | clean | True | 0.95 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-35 | el | clean | True | 0.85 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-42 | el | clean | True | 0.85 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-43 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-45 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-46 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-47 | el | clean | True | 0.85 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-52 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-55 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | el-c-c-57 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gemma4 | ar-c-f-04 | ar | flag | False | 0.85 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-07 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-09 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-10 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-19 | ar | flag | False | 0.85 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-23 | ar | flag | False | 0.85 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-25 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-26 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-30 | ar | flag | False | 0.98 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-39 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-41 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-45 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-47 | ar | flag | False | 0.85 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-48 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-50 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | ar-c-f-59 | ar | flag | False | 1.00 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gemma4 | id-c-f-01 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-02 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| gemma4 | id-c-f-04 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-05 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-07 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-08 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-09 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-10 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-12 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-14 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-16 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| gemma4 | id-c-f-17 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-20 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-23 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-24 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| gemma4 | id-c-f-28 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-30 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-31 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-32 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-33 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-35 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-36 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-37 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-43 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-45 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-46 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-47 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-48 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-49 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| gemma4 | id-c-f-51 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-52 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-53 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-55 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-56 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-58 | id | flag | False | 0.85 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-59 | id | flag | False | 0.80 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-f-60 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gemma4 | id-c-c-02 | id | clean | True | 0.85 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-11 | id | clean | True | 0.95 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-17 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-20 | id | clean | True | 0.92 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-24 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-30 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-32 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-33 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-52 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | id-c-c-58 | id | clean | True | 0.95 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gemma4 | zh-c-f-02 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-03 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-04 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-05 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-06 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-10 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-11 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-12 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-13 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-14 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-15 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-16 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-18 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-19 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-21 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-22 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-23 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-24 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-27 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-29 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-30 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-31 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-32 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-33 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-35 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-37 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-39 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-40 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-43 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-44 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-45 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-46 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-47 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-48 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-49 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-50 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-51 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-53 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-55 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-f-56 | zh | flag | False | 1.00 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-57 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-59 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gemma4 | zh-c-f-60 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gemma4 | zh-c-c-02 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| gemma4 | zh-c-c-03 | zh | clean | True | 0.95 | sexual | COLD: corpus label label 0 (race); mapped to clean/none |
| gemma4 | zh-c-c-08 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gemma4 | zh-c-c-15 | zh | clean | True | 0.92 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| gemma4 | zh-c-c-21 | zh | clean | True | 0.98 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gemma4 | zh-c-c-28 | zh | clean | True | 0.95 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | en-c-f-12 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gpt5mini | en-c-f-14 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| gpt5mini | en-c-f-17 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| gpt5mini | en-c-f-48 | en | flag | False | 0.90 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| gpt5mini | en-c-c-05 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-06 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-07 | en | clean | True | 0.87 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-11 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-16 | en | clean | True | 0.88 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-21 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-33 | en | clean | True | 0.85 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-36 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-45 | en | clean | True | 0.90 | violence | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-48 | en | clean | True | 0.90 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | en-c-c-51 | en | clean | True | 0.85 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| gpt5mini | ro-c-c-04 | ro | clean | True | 0.95 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-06 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-10 | ro | clean | True | 0.60 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-12 | ro | clean | True | 0.95 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-13 | ro | clean | True | 0.98 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-16 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-17 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-18 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-19 | ro | clean | True | 0.90 | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-22 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-24 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-27 | ro | clean | True | 0.92 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-28 | ro | clean | True | 0.90 | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-29 | ro | clean | True | 0.95 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-30 | ro | clean | True | 0.92 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-32 | ro | clean | True | 0.80 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-35 | ro | clean | True | 0.92 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-38 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-40 | ro | clean | True | 0.88 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-41 | ro | clean | True | 0.89 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-44 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-45 | ro | clean | True | 0.82 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-47 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-48 | ro | clean | True | 0.87 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-50 | ro | clean | True | 0.90 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-51 | ro | clean | True | 0.92 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-53 | ro | clean | True | 0.88 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-54 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-55 | ro | clean | True | 0.88 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-57 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-59 | ro | clean | True | 0.85 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | ro-c-c-60 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| gpt5mini | pt-c-f-27 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gpt5mini | pt-c-f-37 | pt | flag | False | 0.70 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| gpt5mini | pt-c-f-38 | pt | flag | False | 0.85 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gpt5mini | pt-c-f-42 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gpt5mini | pt-c-f-49 | pt | flag | False | 0.91 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| gpt5mini | pt-c-c-03 | pt | clean | True | 0.95 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-04 | pt | clean | True | 0.90 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-07 | pt | clean | True | 0.93 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-10 | pt | clean | True | 0.86 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-11 | pt | clean | True | 0.95 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-14 | pt | clean | True | 0.86 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-15 | pt | clean | True | 0.85 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-18 | pt | clean | True | 0.95 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-19 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-20 | pt | clean | True | 0.95 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-23 | pt | clean | True | 0.90 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-24 | pt | clean | True | 0.92 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-26 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-28 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-29 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-30 | pt | clean | True | 0.80 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-32 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-33 | pt | clean | True | 0.92 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-34 | pt | clean | True | 0.89 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-36 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-39 | pt | clean | True | 0.93 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-40 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-41 | pt | clean | True | 0.83 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-43 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-45 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-47 | pt | clean | True | 0.92 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-50 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-51 | pt | clean | True | 0.88 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-53 | pt | clean | True | 0.90 | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-54 | pt | clean | True | 0.80 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-55 | pt | clean | True | 0.95 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-57 | pt | clean | True | 0.85 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | pt-c-c-59 | pt | clean | True | 0.93 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-f-08 | tr | flag | False | 0.96 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-11 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-15 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-18 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-19 | tr | flag | False | 0.83 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-21 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-23 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-30 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-36 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-45 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-49 | tr | flag | False | 0.92 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-50 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-51 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-53 | tr | flag | False | 0.86 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-f-55 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| gpt5mini | tr-c-c-09 | tr | clean | True | 0.90 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-10 | tr | clean | True | 0.87 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-12 | tr | clean | True | 0.90 | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-20 | tr | clean | True | 0.90 | profanity | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-33 | tr | clean | True | 0.60 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-34 | tr | clean | True | 0.95 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-36 | tr | clean | True | 0.85 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-41 | tr | clean | True | 0.93 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | tr-c-c-59 | tr | clean | True | 0.90 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-f-40 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| gpt5mini | el-c-c-01 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-02 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-03 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-04 | el | clean | True | 0.88 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-05 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-06 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-07 | el | clean | True | 0.95 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-09 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-10 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-11 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-13 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-14 | el | clean | True | 0.96 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-15 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-16 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-17 | el | clean | True | 0.95 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-18 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-19 | el | clean | True | 0.88 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-21 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-23 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-25 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-27 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-29 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-34 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-35 | el | clean | True | 0.92 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-36 | el | clean | True | 0.88 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-42 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-43 | el | clean | True | 0.92 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-45 | el | clean | True | 0.95 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-46 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-47 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-48 | el | clean | True | 0.92 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-50 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-52 | el | clean | True | 0.86 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-53 | el | clean | True | 0.87 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-55 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-57 | el | clean | True | 0.86 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-58 | el | clean | True | 0.90 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | el-c-c-60 | el | clean | True | 0.86 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-f-25 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gpt5mini | ar-c-f-30 | ar | flag | False | 0.92 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gpt5mini | ar-c-f-59 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| gpt5mini | ar-c-c-02 | ar | clean | True | 0.90 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-08 | ar | clean | True | 0.90 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-09 | ar | clean | True | 0.90 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-10 | ar | clean | True | 0.90 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-37 | ar | clean | True | 0.93 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-39 | ar | clean | True | 0.85 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | ar-c-c-59 | ar | clean | True | 0.86 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| gpt5mini | id-c-f-07 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-f-31 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-f-46 | id | flag | False | 0.87 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-f-55 | id | flag | False | 0.80 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-f-56 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-f-60 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| gpt5mini | id-c-c-02 | id | clean | True | 0.90 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-05 | id | clean | True | 0.90 | profanity | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-10 | id | clean | True | 0.85 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-11 | id | clean | True | 0.90 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-12 | id | clean | True | 0.90 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-20 | id | clean | True | 0.90 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-24 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-30 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-47 | id | clean | True | 0.90 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-48 | id | clean | True | 0.92 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-50 | id | clean | True | 0.90 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | id-c-c-56 | id | clean | True | 0.82 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| gpt5mini | zh-c-f-03 | zh | flag | False | 0.85 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-12 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-22 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-23 | zh | flag | False | 0.80 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-24 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-32 | zh | flag | False | 0.86 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-37 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-39 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-42 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-44 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-46 | zh | flag | False | 0.93 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-47 | zh | flag | False | 0.93 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-f-48 | zh | flag | False | 0.92 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-49 | zh | flag | False | 0.80 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-50 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-56 | zh | flag | False | 0.94 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-57 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| gpt5mini | zh-c-f-60 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| gpt5mini | zh-c-c-02 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-03 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-08 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-12 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-14 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-15 | zh | clean | True | 0.90 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-21 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-25 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-27 | zh | clean | True | 0.85 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-28 | zh | clean | True | 0.92 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-33 | zh | clean | True | 0.92 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-41 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-43 | zh | clean | True | 0.90 | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-44 | zh | clean | True | 0.83 | self_harm | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-45 | zh | clean | True | 0.90 | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| gpt5mini | zh-c-c-48 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-53 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-55 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-57 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| gpt5mini | zh-c-c-60 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| jev | en-c-f-04 | en | flag | False | 0.09 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-05 | en | flag | False | 0.14 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| jev | en-c-f-08 | en | flag | False | 0.48 | harassment | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| jev | en-c-f-09 | en | flag | False | 0.36 | harassment | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-10 | en | flag | False | 0.11 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| jev | en-c-f-12 | en | flag | False | 0.17 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-13 | en | flag | False | 0.11 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-14 | en | flag | False | 0.46 | hate | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| jev | en-c-f-15 | en | flag | False | 0.17 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-17 | en | flag | False | 0.22 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| jev | en-c-f-20 | en | flag | False | 0.44 | harassment | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| jev | en-c-f-22 | en | flag | False | 0.10 | harassment | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| jev | en-c-f-23 | en | flag | False | 0.28 | harassment | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| jev | en-c-f-27 | en | flag | False | 0.05 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| jev | en-c-f-28 | en | flag | False | 0.20 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-29 | en | flag | False | 0.32 | harassment | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| jev | en-c-f-31 | en | flag | False | 0.22 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| jev | en-c-f-33 | en | flag | False | 0.40 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| jev | en-c-f-34 | en | flag | False | 0.19 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-35 | en | flag | False | 0.29 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-37 | en | flag | False | 0.15 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-38 | en | flag | False | 0.11 | harassment | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| jev | en-c-f-39 | en | flag | False | 0.48 | profanity | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| jev | en-c-f-40 | en | flag | False | 0.32 | harassment | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| jev | en-c-f-45 | en | flag | False | 0.34 | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| jev | en-c-f-47 | en | flag | False | 0.25 | harassment | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-48 | en | flag | False | 0.22 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| jev | en-c-f-49 | en | flag | False | 0.46 | harassment | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| jev | en-c-f-51 | en | flag | False | 0.34 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| jev | en-c-f-59 | en | flag | False | 0.26 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| jev | en-c-c-21 | en | clean | True | 0.60 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| jev | en-c-c-33 | en | clean | True | 0.50 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| jev | en-c-c-36 | en | clean | True | 0.54 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| jev | ro-c-f-17 | ro | flag | False | 0.33 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-f-18 | ro | flag | False | 0.36 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-f-28 | ro | flag | False | 0.40 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-f-41 | ro | flag | False | 0.30 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| jev | ro-c-f-47 | ro | flag | False | 0.16 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| jev | ro-c-f-58 | ro | flag | False | 0.48 | harassment | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| jev | ro-c-c-04 | ro | clean | True | 0.60 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-13 | ro | clean | True | 0.53 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-24 | ro | clean | True | 0.89 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-25 | ro | clean | True | 0.54 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-35 | ro | clean | True | 0.91 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-52 | ro | clean | True | 0.59 | none | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-55 | ro | clean | True | 0.53 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-57 | ro | clean | True | 0.55 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | ro-c-c-60 | ro | clean | True | 0.79 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| jev | pt-c-f-01 | pt | flag | False | 0.49 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-17 | pt | flag | False | 0.21 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-19 | pt | flag | False | 0.47 | profanity | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-22 | pt | flag | False | 0.22 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-24 | pt | flag | False | 0.19 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-26 | pt | flag | False | 0.42 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-27 | pt | flag | False | 0.36 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-29 | pt | flag | False | 0.38 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-31 | pt | flag | False | 0.27 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-33 | pt | flag | False | 0.49 | harassment | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-34 | pt | flag | False | 0.13 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-39 | pt | flag | False | 0.38 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-40 | pt | flag | False | 0.33 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-41 | pt | flag | False | 0.17 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-42 | pt | flag | False | 0.26 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-48 | pt | flag | False | 0.21 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| jev | pt-c-f-49 | pt | flag | False | 0.28 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-f-54 | pt | flag | False | 0.32 | harassment | OLID-BR: corpus label OFF; mapped to flag/harassment |
| jev | pt-c-c-03 | pt | clean | True | 0.84 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-04 | pt | clean | True | 0.90 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-07 | pt | clean | True | 0.88 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-10 | pt | clean | True | 0.57 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-11 | pt | clean | True | 0.97 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-18 | pt | clean | True | 0.76 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-19 | pt | clean | True | 0.70 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-23 | pt | clean | True | 0.86 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-25 | pt | clean | True | 0.59 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-26 | pt | clean | True | 0.80 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-28 | pt | clean | True | 0.90 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-32 | pt | clean | True | 0.60 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-34 | pt | clean | True | 0.70 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-36 | pt | clean | True | 0.50 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-38 | pt | clean | True | 0.75 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-41 | pt | clean | True | 0.54 | none | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-47 | pt | clean | True | 0.53 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-48 | pt | clean | True | 0.81 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-50 | pt | clean | True | 0.65 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-51 | pt | clean | True | 0.51 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-53 | pt | clean | True | 0.58 | none | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-55 | pt | clean | True | 0.61 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | pt-c-c-57 | pt | clean | True | 0.67 | none | OLID-BR: corpus label NOT; mapped to clean/none |
| jev | tr-c-f-01 | tr | flag | False | 0.31 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-03 | tr | flag | False | 0.33 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-05 | tr | flag | False | 0.37 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-08 | tr | flag | False | 0.13 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-09 | tr | flag | False | 0.32 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-11 | tr | flag | False | 0.08 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-14 | tr | flag | False | 0.10 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-15 | tr | flag | False | 0.42 | violence | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-18 | tr | flag | False | 0.11 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-20 | tr | flag | False | 0.21 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-23 | tr | flag | False | 0.43 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-24 | tr | flag | False | 0.47 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-25 | tr | flag | False | 0.22 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-26 | tr | flag | False | 0.35 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-30 | tr | flag | False | 0.12 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-35 | tr | flag | False | 0.38 | harassment | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-36 | tr | flag | False | 0.37 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-37 | tr | flag | False | 0.17 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-40 | tr | flag | False | 0.45 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-44 | tr | flag | False | 0.45 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-45 | tr | flag | False | 0.16 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-50 | tr | flag | False | 0.25 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-51 | tr | flag | False | 0.42 | violence | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-53 | tr | flag | False | 0.25 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-55 | tr | flag | False | 0.40 | hate | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-57 | tr | flag | False | 0.28 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-f-59 | tr | flag | False | 0.38 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| jev | tr-c-c-12 | tr | clean | True | 0.85 | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| jev | tr-c-c-34 | tr | clean | True | 0.75 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| jev | tr-c-c-41 | tr | clean | True | 0.70 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| jev | tr-c-c-59 | tr | clean | True | 0.82 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| jev | el-c-f-33 | el | flag | False | 0.47 | harassment | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| jev | el-c-f-39 | el | flag | False | 0.34 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| jev | el-c-f-52 | el | flag | False | 0.46 | harassment | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| jev | el-c-c-01 | el | clean | True | 0.92 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-02 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-04 | el | clean | True | 0.64 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-06 | el | clean | True | 0.59 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-07 | el | clean | True | 0.64 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-09 | el | clean | True | 0.51 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-10 | el | clean | True | 0.78 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-11 | el | clean | True | 0.94 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-13 | el | clean | True | 0.88 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-16 | el | clean | True | 0.66 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-17 | el | clean | True | 0.74 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-19 | el | clean | True | 0.59 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-20 | el | clean | True | 0.80 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-21 | el | clean | True | 0.73 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-25 | el | clean | True | 0.93 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-27 | el | clean | True | 0.74 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-29 | el | clean | True | 0.74 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-34 | el | clean | True | 0.85 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-35 | el | clean | True | 0.76 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-36 | el | clean | True | 0.64 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-42 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-43 | el | clean | True | 0.97 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-45 | el | clean | True | 0.82 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-46 | el | clean | True | 0.69 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-47 | el | clean | True | 0.67 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-50 | el | clean | True | 0.50 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-55 | el | clean | True | 0.87 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-57 | el | clean | True | 0.58 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | el-c-c-58 | el | clean | True | 0.50 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| jev | ar-c-f-09 | ar | flag | False | 0.39 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-10 | ar | flag | False | 0.30 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-12 | ar | flag | False | 0.29 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-25 | ar | flag | False | 0.29 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-30 | ar | flag | False | 0.15 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-39 | ar | flag | False | 0.28 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-45 | ar | flag | False | 0.29 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-48 | ar | flag | False | 0.42 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-50 | ar | flag | False | 0.41 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-f-59 | ar | flag | False | 0.04 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| jev | ar-c-c-08 | ar | clean | True | 0.52 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-09 | ar | clean | True | 0.88 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-10 | ar | clean | True | 0.88 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-18 | ar | clean | True | 0.50 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-37 | ar | clean | True | 0.58 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-39 | ar | clean | True | 0.72 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | ar-c-c-48 | ar | clean | True | 0.51 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| jev | id-c-f-01 | id | flag | False | 0.20 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-08 | id | flag | False | 0.47 | harassment | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-10 | id | flag | False | 0.17 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-14 | id | flag | False | 0.34 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-31 | id | flag | False | 0.10 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-37 | id | flag | False | 0.48 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-43 | id | flag | False | 0.33 | harassment | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-45 | id | flag | False | 0.41 | harassment | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-46 | id | flag | False | 0.13 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-51 | id | flag | False | 0.30 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-f-60 | id | flag | False | 0.22 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| jev | id-c-c-02 | id | clean | True | 0.67 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-09 | id | clean | True | 0.85 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-11 | id | clean | True | 0.93 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-14 | id | clean | True | 0.70 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-17 | id | clean | True | 0.77 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-24 | id | clean | True | 0.89 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-30 | id | clean | True | 0.75 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-32 | id | clean | True | 0.84 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-33 | id | clean | True | 0.72 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-48 | id | clean | True | 0.89 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-50 | id | clean | True | 0.66 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-52 | id | clean | True | 0.85 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | id-c-c-58 | id | clean | True | 0.69 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| jev | zh-c-f-02 | zh | flag | False | 0.21 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-03 | zh | flag | False | 0.17 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-10 | zh | flag | False | 0.31 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-11 | zh | flag | False | 0.37 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-12 | zh | flag | False | 0.06 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-14 | zh | flag | False | 0.37 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-16 | zh | flag | False | 0.48 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-19 | zh | flag | False | 0.42 | hate | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-21 | zh | flag | False | 0.23 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-22 | zh | flag | False | 0.20 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-23 | zh | flag | False | 0.25 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-24 | zh | flag | False | 0.16 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-30 | zh | flag | False | 0.48 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-32 | zh | flag | False | 0.08 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-37 | zh | flag | False | 0.30 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-39 | zh | flag | False | 0.09 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-44 | zh | flag | False | 0.04 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-46 | zh | flag | False | 0.09 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-47 | zh | flag | False | 0.03 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-48 | zh | flag | False | 0.07 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-49 | zh | flag | False | 0.05 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-50 | zh | flag | False | 0.14 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-53 | zh | flag | False | 0.35 | harassment | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-55 | zh | flag | False | 0.34 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-f-56 | zh | flag | False | 0.03 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-57 | zh | flag | False | 0.36 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| jev | zh-c-f-60 | zh | flag | False | 0.46 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| jev | zh-c-c-02 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| jev | zh-c-c-03 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | zh-c-c-08 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | zh-c-c-15 | zh | clean | True | 0.93 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | zh-c-c-21 | zh | clean | True | 0.98 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | zh-c-c-28 | zh | clean | True | 0.70 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| jev | zh-c-c-44 | zh | clean | True | 0.55 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| jev | zh-c-c-57 | zh | clean | True | 0.52 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| jev | zh-c-c-60 | zh | clean | True | 0.70 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | en-c-f-01 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| llamaguard | en-c-f-04 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-05 | en | flag | False | - | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| llamaguard | en-c-f-06 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-07 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| llamaguard | en-c-f-08 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| llamaguard | en-c-f-09 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-10 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| llamaguard | en-c-f-12 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-13 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-14 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| llamaguard | en-c-f-16 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-17 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-18 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.85; mapped to flag/harassment |
| llamaguard | en-c-f-20 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| llamaguard | en-c-f-22 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| llamaguard | en-c-f-23 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| llamaguard | en-c-f-24 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| llamaguard | en-c-f-27 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-28 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-29 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-30 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.65; mapped to flag/profanity |
| llamaguard | en-c-f-31 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| llamaguard | en-c-f-33 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-35 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-37 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-39 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/profanity |
| llamaguard | en-c-f-40 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| llamaguard | en-c-f-42 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.65; mapped to flag/harassment |
| llamaguard | en-c-f-43 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.73; mapped to flag/harassment |
| llamaguard | en-c-f-44 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| llamaguard | en-c-f-45 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| llamaguard | en-c-f-46 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| llamaguard | en-c-f-47 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| llamaguard | en-c-f-49 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| llamaguard | en-c-f-50 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.84; mapped to flag/harassment |
| llamaguard | en-c-f-51 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| llamaguard | en-c-f-52 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| llamaguard | en-c-f-53 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/hate |
| llamaguard | en-c-f-55 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.92; mapped to flag/harassment |
| llamaguard | en-c-f-56 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.75; mapped to flag/harassment |
| llamaguard | en-c-f-57 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| llamaguard | en-c-f-59 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| llamaguard | en-c-f-60 | en | flag | False | - | none | Civil Comments: corpus label toxicity 0.72; mapped to flag/harassment |
| llamaguard | en-c-c-05 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-06 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-08 | en | clean | True | - | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-11 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-14 | en | clean | True | - | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-16 | en | clean | True | - | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-29 | en | clean | True | - | self_harm | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-48 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-49 | en | clean | True | - | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-50 | en | clean | True | - | violence | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | en-c-c-60 | en | clean | True | - | self_harm | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| llamaguard | ro-c-f-31 | ro | flag | False | - | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| llamaguard | ro-c-c-01 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-02 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-03 | ro | clean | True | - | sexual | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-04 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-05 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-06 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-09 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-10 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-11 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-12 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-13 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-16 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-17 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-18 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-19 | ro | clean | True | - | sexual | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-20 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-21 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-22 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-23 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-24 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-25 | ro | clean | True | - | self_harm | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-26 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-27 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-28 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-29 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-30 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-31 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-32 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-33 | ro | clean | True | - | self_harm | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-34 | ro | clean | True | - | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-35 | ro | clean | True | - | self_harm | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-36 | ro | clean | True | - | sexual | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-37 | ro | clean | True | - | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-38 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-39 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-40 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-43 | ro | clean | True | - | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-44 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-45 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-46 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-49 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-53 | ro | clean | True | - | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-54 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-55 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-56 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-57 | ro | clean | True | - | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-58 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | ro-c-c-59 | ro | clean | True | - | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| llamaguard | pt-c-f-02 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-03 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-06 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-08 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-09 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-11 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-12 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-15 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-16 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-17 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-19 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-20 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-22 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-24 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-25 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-26 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-28 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-31 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-32 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-34 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-38 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-39 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-40 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-41 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-42 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-44 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-47 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-49 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-53 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-54 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-55 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-56 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-f-57 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| llamaguard | pt-c-f-60 | pt | flag | False | - | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| llamaguard | pt-c-c-01 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-02 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-03 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-06 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-10 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-11 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-13 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-25 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-26 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-27 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-28 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-29 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-32 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-34 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-36 | pt | clean | True | - | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-37 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-41 | pt | clean | True | - | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-43 | pt | clean | True | - | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-44 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-45 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-46 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-53 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-54 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-55 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-57 | pt | clean | True | - | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-58 | pt | clean | True | - | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | pt-c-c-60 | pt | clean | True | - | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-f-01 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-03 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-05 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-37 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-45 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-50 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-57 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-f-59 | tr | flag | False | - | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| llamaguard | tr-c-c-01 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-04 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-07 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-09 | tr | clean | True | - | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-10 | tr | clean | True | - | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-12 | tr | clean | True | - | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-13 | tr | clean | True | - | illegal | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-14 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
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
| llamaguard | tr-c-c-59 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | tr-c-c-60 | tr | clean | True | - | self_harm | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| llamaguard | el-c-f-01 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-07 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-22 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-25 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-33 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-36 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-39 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-42 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-f-51 | el | flag | False | - | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| llamaguard | el-c-c-01 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-02 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-03 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-05 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-07 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-08 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-09 | el | clean | True | - | self_harm | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-11 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-13 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-14 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-16 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-18 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-19 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-20 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-22 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-24 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-25 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-26 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-27 | el | clean | True | - | sexual | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-28 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-29 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-33 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-34 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-35 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-36 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-38 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-39 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-40 | el | clean | True | - | sexual | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-42 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-43 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-44 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-45 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-46 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-47 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-48 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-49 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-50 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-51 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-52 | el | clean | True | - | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-54 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-56 | el | clean | True | - | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-58 | el | clean | True | - | illegal | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | el-c-c-60 | el | clean | True | - | self_harm | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-f-20 | ar | flag | False | - | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| llamaguard | ar-c-c-01 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-02 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-03 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-04 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-06 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-07 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-08 | ar | clean | True | - | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-09 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-10 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-11 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
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
| llamaguard | ar-c-c-37 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-38 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-39 | ar | clean | True | - | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-40 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-41 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-42 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-44 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-45 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-46 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-47 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-48 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-49 | ar | clean | True | - | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-50 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-51 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-52 | ar | clean | True | - | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-53 | ar | clean | True | - | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-55 | ar | clean | True | - | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-56 | ar | clean | True | - | illegal | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-58 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-59 | ar | clean | True | - | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | ar-c-c-60 | ar | clean | True | - | sexual | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| llamaguard | id-c-f-01 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| llamaguard | id-c-f-11 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| llamaguard | id-c-f-45 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| llamaguard | id-c-f-46 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| llamaguard | id-c-f-47 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| llamaguard | id-c-f-48 | id | flag | False | - | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| llamaguard | id-c-c-01 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-02 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-06 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-07 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-08 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-09 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-10 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-12 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-14 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-17 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-20 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-21 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-22 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-24 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-26 | id | clean | True | - | self_harm | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-27 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-28 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-30 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-33 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-34 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-35 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-36 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-37 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-39 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-42 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-43 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-47 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-49 | id | clean | True | - | self_harm | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-50 | id | clean | True | - | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-53 | id | clean | True | - | sexual | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-56 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-58 | id | clean | True | - | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | id-c-c-60 | id | clean | True | - | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| llamaguard | zh-c-f-05 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-12 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-13 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-14 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-19 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-22 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-24 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-32 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-35 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-37 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-38 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-39 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-40 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-42 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-44 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-46 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-47 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-48 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-50 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-f-53 | zh | flag | False | - | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| llamaguard | zh-c-f-56 | zh | flag | False | - | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| llamaguard | zh-c-c-01 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-02 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-04 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-05 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-08 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-09 | zh | clean | True | - | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-12 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-14 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-15 | zh | clean | True | - | illegal | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-17 | zh | clean | True | - | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-21 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-22 | zh | clean | True | - | sexual | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-25 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-32 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-41 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-43 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-44 | zh | clean | True | - | self_harm | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-45 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-47 | zh | clean | True | - | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| llamaguard | zh-c-c-48 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-53 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-57 | zh | clean | True | - | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| llamaguard | zh-c-c-60 | zh | clean | True | - | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | en-c-f-04 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-05 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| luna | en-c-f-09 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-10 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| luna | en-c-f-12 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-14 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| luna | en-c-f-15 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-17 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| luna | en-c-f-22 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| luna | en-c-f-23 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| luna | en-c-f-27 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| luna | en-c-f-28 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-29 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| luna | en-c-f-32 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/hate |
| luna | en-c-f-33 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| luna | en-c-f-34 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-37 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-38 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| luna | en-c-f-40 | en | flag | False | 0.97 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| luna | en-c-f-47 | en | flag | False | 0.91 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-48 | en | flag | False | 0.97 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| luna | en-c-f-51 | en | flag | False | 0.97 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| luna | en-c-f-53 | en | flag | False | 0.97 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/hate |
| luna | en-c-f-58 | en | flag | False | 0.96 | none | Civil Comments: corpus label toxicity 0.61; mapped to flag/harassment |
| luna | en-c-f-59 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| luna | ro-c-c-01 | ro | clean | True | 0.84 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-04 | ro | clean | True | 0.86 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-13 | ro | clean | True | 0.83 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-17 | ro | clean | True | 0.96 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-19 | ro | clean | True | 0.92 | violence | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-24 | ro | clean | True | 0.91 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-29 | ro | clean | True | 0.86 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-35 | ro | clean | True | 0.91 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-40 | ro | clean | True | 0.84 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-48 | ro | clean | True | 0.98 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-51 | ro | clean | True | 0.76 | hate | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-52 | ro | clean | True | 0.85 | illegal | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-53 | ro | clean | True | 0.94 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-55 | ro | clean | True | 0.91 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-57 | ro | clean | True | 0.77 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-59 | ro | clean | True | 0.72 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | ro-c-c-60 | ro | clean | True | 0.96 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| luna | pt-c-f-09 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-24 | pt | flag | False | 0.96 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-26 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-27 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-34 | pt | flag | False | 0.99 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-37 | pt | flag | False | 0.88 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-38 | pt | flag | False | 0.96 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-39 | pt | flag | False | 0.96 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-40 | pt | flag | False | 0.90 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| luna | pt-c-f-41 | pt | flag | False | 0.91 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-42 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-47 | pt | flag | False | 0.97 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-49 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-52 | pt | flag | False | 0.94 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-f-54 | pt | flag | False | 0.99 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| luna | pt-c-c-04 | pt | clean | True | 0.84 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-11 | pt | clean | True | 0.99 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-18 | pt | clean | True | 0.99 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-22 | pt | clean | True | 0.82 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-23 | pt | clean | True | 0.98 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-25 | pt | clean | True | 0.91 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-26 | pt | clean | True | 0.82 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-28 | pt | clean | True | 0.88 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-34 | pt | clean | True | 0.84 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-47 | pt | clean | True | 0.91 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-49 | pt | clean | True | 0.82 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-51 | pt | clean | True | 0.84 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | pt-c-c-55 | pt | clean | True | 0.87 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| luna | tr-c-f-01 | tr | flag | False | 0.94 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-02 | tr | flag | False | 0.97 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-03 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-08 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-09 | tr | flag | False | 0.96 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-11 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-14 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-18 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-19 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-20 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-21 | tr | flag | False | 0.97 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-23 | tr | flag | False | 0.96 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-24 | tr | flag | False | 0.93 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-28 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-30 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-31 | tr | flag | False | 0.94 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-36 | tr | flag | False | 0.93 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-37 | tr | flag | False | 0.96 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-40 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-42 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-43 | tr | flag | False | 0.91 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-44 | tr | flag | False | 0.93 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-45 | tr | flag | False | 0.97 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-49 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-50 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-51 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-53 | tr | flag | False | 0.96 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-55 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-f-59 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| luna | tr-c-c-08 | tr | clean | True | 0.84 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| luna | tr-c-c-12 | tr | clean | True | 0.96 | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| luna | tr-c-c-43 | tr | clean | True | 0.78 | harassment | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| luna | el-c-f-27 | el | flag | False | 0.87 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| luna | el-c-f-36 | el | flag | False | 0.87 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| luna | el-c-f-39 | el | flag | False | 0.89 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| luna | el-c-f-40 | el | flag | False | 0.87 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| luna | el-c-f-56 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| luna | el-c-c-01 | el | clean | True | 0.92 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-02 | el | clean | True | 0.99 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-03 | el | clean | True | 0.68 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-04 | el | clean | True | 0.79 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-05 | el | clean | True | 0.91 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-07 | el | clean | True | 0.98 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-09 | el | clean | True | 0.88 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-10 | el | clean | True | 0.87 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-11 | el | clean | True | 0.86 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-13 | el | clean | True | 0.91 | violence | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-14 | el | clean | True | 0.99 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-16 | el | clean | True | 0.91 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-17 | el | clean | True | 0.99 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-20 | el | clean | True | 0.78 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-21 | el | clean | True | 0.98 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-23 | el | clean | True | 0.97 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-25 | el | clean | True | 0.98 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-27 | el | clean | True | 0.91 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-34 | el | clean | True | 0.91 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-35 | el | clean | True | 0.89 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-42 | el | clean | True | 0.99 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-43 | el | clean | True | 0.99 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-45 | el | clean | True | 0.96 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-46 | el | clean | True | 0.82 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-47 | el | clean | True | 0.86 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-48 | el | clean | True | 0.79 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-51 | el | clean | True | 0.82 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-53 | el | clean | True | 0.91 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | el-c-c-60 | el | clean | True | 0.86 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| luna | ar-c-f-26 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| luna | ar-c-f-59 | ar | flag | False | 0.99 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| luna | ar-c-c-08 | ar | clean | True | 0.79 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-09 | ar | clean | True | 0.87 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-10 | ar | clean | True | 0.88 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-37 | ar | clean | True | 0.78 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-39 | ar | clean | True | 0.72 | self_harm | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-42 | ar | clean | True | 0.78 | violence | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | ar-c-c-53 | ar | clean | True | 0.73 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| luna | id-c-f-02 | id | flag | False | 0.97 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| luna | id-c-f-04 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-07 | id | flag | False | 0.99 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-09 | id | flag | False | 0.96 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-10 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-14 | id | flag | False | 0.97 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-17 | id | flag | False | 0.96 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-20 | id | flag | False | 0.94 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-31 | id | flag | False | 0.99 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-32 | id | flag | False | 0.88 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-33 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-35 | id | flag | False | 0.91 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-37 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-43 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-47 | id | flag | False | 0.94 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-51 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-52 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-55 | id | flag | False | 0.94 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-59 | id | flag | False | 0.94 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-f-60 | id | flag | False | 0.98 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| luna | id-c-c-02 | id | clean | True | 0.78 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-05 | id | clean | True | 0.96 | profanity | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-10 | id | clean | True | 0.76 | harassment | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-17 | id | clean | True | 0.99 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-20 | id | clean | True | 0.88 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-24 | id | clean | True | 0.98 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-30 | id | clean | True | 0.96 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-32 | id | clean | True | 0.97 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-33 | id | clean | True | 0.92 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-52 | id | clean | True | 0.98 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-56 | id | clean | True | 0.73 | violence | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | id-c-c-58 | id | clean | True | 0.83 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| luna | zh-c-f-02 | zh | flag | False | 0.94 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-03 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-04 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-08 | zh | flag | False | 0.97 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-10 | zh | flag | False | 0.88 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-11 | zh | flag | False | 0.91 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-12 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-21 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-22 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-23 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-24 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-28 | zh | flag | False | 0.97 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-31 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-32 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-37 | zh | flag | False | 0.94 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-39 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-42 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-43 | zh | flag | False | 0.96 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-44 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-45 | zh | flag | False | 0.96 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-46 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-47 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-f-48 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-49 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-50 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-51 | zh | flag | False | 0.91 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-56 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-57 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-58 | zh | flag | False | 0.91 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| luna | zh-c-f-60 | zh | flag | False | 0.96 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| luna | zh-c-c-02 | zh | clean | True | 0.98 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | zh-c-c-03 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-08 | zh | clean | True | 0.99 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-12 | zh | clean | True | 0.78 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-14 | zh | clean | True | 0.86 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-15 | zh | clean | True | 0.82 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-21 | zh | clean | True | 0.99 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-28 | zh | clean | True | 0.98 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | zh-c-c-32 | zh | clean | True | 0.79 | harassment | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-33 | zh | clean | True | 0.93 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | zh-c-c-44 | zh | clean | True | 0.91 | self_harm | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | zh-c-c-45 | zh | clean | True | 0.87 | harassment | COLD: corpus label label 0 (region); mapped to clean/none |
| luna | zh-c-c-48 | zh | clean | True | 0.76 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-53 | zh | clean | True | 0.91 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| luna | zh-c-c-57 | zh | clean | True | 0.78 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | en-c-f-04 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-05 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 1.00; mapped to flag/harassment |
| safeguard | en-c-f-09 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-10 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| safeguard | en-c-f-12 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-13 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-14 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/hate |
| safeguard | en-c-f-15 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-17 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| safeguard | en-c-f-20 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.82; mapped to flag/harassment |
| safeguard | en-c-f-22 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| safeguard | en-c-f-23 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/harassment |
| safeguard | en-c-f-24 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| safeguard | en-c-f-27 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| safeguard | en-c-f-28 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-29 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| safeguard | en-c-f-31 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| safeguard | en-c-f-33 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.70; mapped to flag/harassment |
| safeguard | en-c-f-34 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-36 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| safeguard | en-c-f-37 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-38 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.83; mapped to flag/harassment |
| safeguard | en-c-f-40 | en | flag | False | 0.99 | none | Civil Comments: corpus label toxicity 0.71; mapped to flag/harassment |
| safeguard | en-c-f-41 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.76; mapped to flag/harassment |
| safeguard | en-c-f-45 | en | flag | False | 0.98 | none | Civil Comments: corpus label toxicity 0.81; mapped to flag/harassment |
| safeguard | en-c-f-46 | en | flag | False | 0.85 | none | Civil Comments: corpus label toxicity 0.79; mapped to flag/harassment |
| safeguard | en-c-f-47 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-48 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.60; mapped to flag/harassment |
| safeguard | en-c-f-51 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.67; mapped to flag/harassment |
| safeguard | en-c-f-53 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.80; mapped to flag/hate |
| safeguard | en-c-f-58 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.61; mapped to flag/harassment |
| safeguard | en-c-f-59 | en | flag | False | 0.95 | none | Civil Comments: corpus label toxicity 0.68; mapped to flag/harassment |
| safeguard | en-c-c-05 | en | clean | True | 0.90 | hate | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| safeguard | en-c-c-06 | en | clean | True | 0.80 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| safeguard | en-c-c-21 | en | clean | True | 0.80 | harassment | Civil Comments: corpus label toxicity 0.00; mapped to clean/none |
| safeguard | ro-c-f-02 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| safeguard | ro-c-f-05 | ro | flag | False | 0.95 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-11 | ro | flag | False | 0.90 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-15 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-16 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-28 | ro | flag | False | 0.95 | none | RO-Offense: corpus label PROFANITY; mapped to flag/profanity |
| safeguard | ro-c-f-41 | ro | flag | False | 0.90 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-44 | ro | flag | False | 0.95 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-57 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-58 | ro | flag | False | 0.95 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-f-59 | ro | flag | False | 0.90 | none | RO-Offense: corpus label ABUSE; mapped to flag/hate |
| safeguard | ro-c-f-60 | ro | flag | False | 0.92 | none | RO-Offense: corpus label INSULT; mapped to flag/harassment |
| safeguard | ro-c-c-05 | ro | clean | True | 0.95 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-13 | ro | clean | True | 0.80 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-28 | ro | clean | True | 0.92 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-35 | ro | clean | True | 0.95 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-38 | ro | clean | True | 0.90 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-44 | ro | clean | True | 0.75 | harassment | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-48 | ro | clean | True | 0.85 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | ro-c-c-53 | ro | clean | True | 0.80 | profanity | RO-Offense: corpus label OTHER; mapped to clean/none |
| safeguard | pt-c-f-02 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-04 | pt | flag | False | 0.85 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-08 | pt | flag | False | 0.98 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-09 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-10 | pt | flag | False | 0.92 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-12 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-17 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-24 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-25 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-26 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-27 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-29 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-34 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-35 | pt | flag | False | 0.99 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-37 | pt | flag | False | 0.99 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-38 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-39 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-40 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-47 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-48 | pt | flag | False | 0.99 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-f-49 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/harassment |
| safeguard | pt-c-f-53 | pt | flag | False | 0.95 | none | OLID-BR: corpus label OFF; mapped to flag/hate |
| safeguard | pt-c-c-03 | pt | clean | True | 0.85 | illegal | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-07 | pt | clean | True | 0.92 | violence | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-11 | pt | clean | True | 0.99 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-18 | pt | clean | True | 0.95 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-23 | pt | clean | True | 0.92 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-25 | pt | clean | True | 0.80 | sexual | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-26 | pt | clean | True | 0.85 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-28 | pt | clean | True | 0.70 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-37 | pt | clean | True | 0.85 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-38 | pt | clean | True | 0.90 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-46 | pt | clean | True | 0.80 | hate | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-53 | pt | clean | True | 0.85 | self_harm | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-55 | pt | clean | True | 0.80 | harassment | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | pt-c-c-59 | pt | clean | True | 0.80 | profanity | OLID-BR: corpus label NOT; mapped to clean/none |
| safeguard | tr-c-f-01 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-03 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-05 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-06 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-08 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-09 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-11 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-13 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-14 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-15 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-16 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-17 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-18 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-19 | tr | flag | False | 0.92 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-20 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-23 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-24 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-25 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-26 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-28 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-30 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-34 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-35 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-36 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-37 | tr | flag | False | 0.97 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-40 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-44 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-45 | tr | flag | False | 0.98 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-49 | tr | flag | False | 0.90 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-50 | tr | flag | False | 0.99 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-51 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-53 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-54 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-57 | tr | flag | False | 0.95 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-f-59 | tr | flag | False | 0.85 | none | OffensEval 2020 Turkish: corpus label OFF; mapped to flag/profanity |
| safeguard | tr-c-c-12 | tr | clean | True | 0.95 | violence | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| safeguard | tr-c-c-41 | tr | clean | True | 0.95 | hate | OffensEval 2020 Turkish: corpus label NOT; mapped to clean/none |
| safeguard | el-c-f-02 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-06 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-12 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-19 | el | flag | False | 0.99 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-20 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-21 | el | flag | False | 0.90 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-33 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-36 | el | flag | False | 0.98 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-39 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-40 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-f-52 | el | flag | False | 0.95 | none | OffensEval 2020 Greek (OGTD): corpus label OFF; mapped to flag/profanity |
| safeguard | el-c-c-01 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-03 | el | clean | True | 0.80 | violence | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-05 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-07 | el | clean | True | 0.95 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-10 | el | clean | True | 0.75 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-14 | el | clean | True | 0.95 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-17 | el | clean | True | 0.92 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-21 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-25 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-34 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-35 | el | clean | True | 0.90 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-42 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-43 | el | clean | True | 0.95 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-45 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-46 | el | clean | True | 0.99 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-48 | el | clean | True | 0.95 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-50 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-55 | el | clean | True | 0.95 | hate | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-57 | el | clean | True | 0.90 | profanity | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | el-c-c-58 | el | clean | True | 0.85 | harassment | OffensEval 2020 Greek (OGTD): corpus label NOT; mapped to clean/none |
| safeguard | ar-c-f-07 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-12 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-15 | ar | flag | False | 0.99 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-25 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-30 | ar | flag | False | 0.99 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-37 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-39 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-45 | ar | flag | False | 0.90 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-48 | ar | flag | False | 0.95 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-f-59 | ar | flag | False | 0.99 | none | OffensEval 2020 Arabic (OSACT4): corpus label OFF; mapped to flag/profanity |
| safeguard | ar-c-c-06 | ar | clean | True | 0.85 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| safeguard | ar-c-c-09 | ar | clean | True | 0.95 | harassment | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| safeguard | ar-c-c-37 | ar | clean | True | 0.90 | hate | OffensEval 2020 Arabic (OSACT4): corpus label NOT; mapped to clean/none |
| safeguard | id-c-f-01 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-02 | id | flag | False | 0.92 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| safeguard | id-c-f-04 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-07 | id | flag | False | 0.80 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-08 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-10 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-14 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-21 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-24 | id | flag | False | 0.99 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| safeguard | id-c-f-28 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-31 | id | flag | False | 0.99 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-35 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-40 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-42 | id | flag | False | 0.92 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-43 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-44 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/profanity |
| safeguard | id-c-f-45 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-46 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-47 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-51 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-52 | id | flag | False | 0.90 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-57 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-59 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-f-60 | id | flag | False | 0.95 | none | IndoDiscourse: corpus label toxicity 1/1; mapped to flag/harassment |
| safeguard | id-c-c-05 | id | clean | True | 0.92 | profanity | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | id-c-c-07 | id | clean | True | 0.92 | profanity | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | id-c-c-24 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | id-c-c-32 | id | clean | True | 0.90 | illegal | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | id-c-c-48 | id | clean | True | 0.95 | hate | IndoDiscourse: corpus label toxicity 0/0; mapped to clean/none |
| safeguard | zh-c-f-02 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-03 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-04 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-05 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-07 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-08 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-12 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-14 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-16 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-19 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-21 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-22 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-23 | zh | flag | False | 0.92 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-29 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-32 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-37 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-38 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-39 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-40 | zh | flag | False | 0.92 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-43 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-45 | zh | flag | False | 0.92 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-46 | zh | flag | False | 0.98 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-47 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-48 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-49 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-50 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-53 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-f-56 | zh | flag | False | 0.99 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-57 | zh | flag | False | 0.90 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-59 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (race); mapped to flag/hate |
| safeguard | zh-c-f-60 | zh | flag | False | 0.95 | none | COLD: corpus label label 1 (region); mapped to flag/hate |
| safeguard | zh-c-c-02 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| safeguard | zh-c-c-03 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-08 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-14 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-15 | zh | clean | True | 0.80 | violence | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-21 | zh | clean | True | 0.99 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-25 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-28 | zh | clean | True | 0.95 | profanity | COLD: corpus label label 0 (region); mapped to clean/none |
| safeguard | zh-c-c-29 | zh | clean | True | 0.85 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-33 | zh | clean | True | 0.95 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
| safeguard | zh-c-c-43 | zh | clean | True | 0.92 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-44 | zh | clean | True | 0.92 | self_harm | COLD: corpus label label 0 (region); mapped to clean/none |
| safeguard | zh-c-c-48 | zh | clean | True | 0.90 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-55 | zh | clean | True | 0.92 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-57 | zh | clean | True | 0.70 | hate | COLD: corpus label label 0 (race); mapped to clean/none |
| safeguard | zh-c-c-60 | zh | clean | True | 0.75 | hate | COLD: corpus label label 0 (region); mapped to clean/none |
