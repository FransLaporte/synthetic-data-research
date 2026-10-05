# Study: breugelSyntheticDataReal2023

- Title: Synthetic Data, Real Errors: How (Not) to Publish and Use Synthetic Data
- Source: [paper record](https://proceedings.mlr.press/v202/van-breugel23a.html)
- Version: ICML 2023 primary study; Zotero PDF.
- Role: General limitation and uncertainty evidence; not LiDAR performance evidence.
- Search record: [RQ1 source checks](../searches/2026-10-01-rq1-source-checks.md).
- Extraction: AI-assisted targeted reading, 2026-10-01.
- Author A/B screening, agreed inclusion and author verification: pending.
- This is a targeted claim record for the draft, not a completed full-study appraisal.

## Claims used in RQ1

| Claim | Source location | Scope and qualification |
| --- | --- | --- |
| Learned generation can suffer mode collapse, poor coverage and other errors. | Introduction and related work; PDF p. 2. | Motivates separating sample plausibility and diversity; does not establish all models fail. |
| Synthetic-test results can misrepresent real-test performance. | Figure 2 and accompanying SEER/CTGAN example; PDF p. 2. | Specific tabular experiment, not a universal quantitative claim. |
| More generated observations do not automatically resolve uncertainty in the fitted generator. | Introduction, contributions and Section 3 context; PDF pp. 1-3. | RQ1's sample-count/information distinction is our interpretation of this issue. No new uncertainty estimates are claimed. |

## Extraction limits

No numerical effect sizes, compute benchmarks or uncertainty estimates are extracted
for RQ1. Dataset sizes, full split details, seeds and model settings are not fully
extracted here and must be checked before using this study for an empirical RQ3
comparison. PDF page indices are one-based in the local copy, not necessarily
publisher page numbers. No human screening or checking is implied by this record.
