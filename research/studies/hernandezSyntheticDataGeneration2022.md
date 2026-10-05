# Study: hernandezSyntheticDataGeneration2022

- Title: Synthetic data generation for tabular health records: A systematic review
- Source: [paper record](https://doi.org/10.1016/j.neucom.2022.04.053)
- Version: Journal review (2022); accepted manuscript with repository cover sheet.
- Role: General tabular-method background; not automotive utility evidence.
- Search record: [RQ1 source checks](../searches/2026-10-01-rq1-source-checks.md).
- Extraction: AI-assisted targeted reading, 2026-10-01.
- Author A/B screening, agreed inclusion and author verification: pending.
- This is a targeted claim record for the draft, not a completed full-study appraisal.

## Claims used in RQ1

| Claim | Source location | Scope and qualification |
| --- | --- | --- |
| Statistical models sample fitted attribute relationships. | Section 5.1.2; PDF p. 14, manuscript p. 13. | Tabular numerical/categorical data. Adequacy of omitted dependencies is our interpretation. |
| Autoencoders use encoded representations and reconstruction; GANs use generator/discriminator training. | Sections 5.2.1-5.2.2; PDF p. 14. | The AE description alone is not evidence that every AE is a generative VAE; TVAE is sourced to Hansen. |
| Classical and neural methods can be organised separately. | Section 5; PDF pp. 13-14. | The paper's taxonomy is specific to tabular health records. Our broader categories also include simulation. |

## Extraction limits

No numerical effect sizes, compute benchmarks or uncertainty estimates are extracted
for RQ1. Dataset sizes, full split details, seeds and model settings are not fully
extracted here and must be checked before using this study for an empirical RQ3
comparison. PDF page indices are one-based in the local copy, not necessarily
publisher page numbers. No human screening or checking is implied by this record.
