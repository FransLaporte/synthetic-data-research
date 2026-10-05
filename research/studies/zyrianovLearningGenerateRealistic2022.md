# Study: zyrianovLearningGenerateRealistic2022

- Title: Learning to Generate Realistic LiDAR Point Clouds
- Source: [paper record](https://arxiv.org/abs/2209.03954)
- Version: Author manuscript identifying ECCV 2022; Zotero currently exports it as prepublished.
- Role: Primary score-based generation example bridging RQ1 to RQ2.
- Search record: [RQ1 source checks](../searches/2026-10-01-rq1-source-checks.md).
- Extraction: AI-assisted targeted reading, 2026-10-01.
- Author A/B screening, agreed inclusion and author verification: pending.
- This is a targeted claim record for the draft, not a completed full-study appraisal.

## Claims used in RQ1

| Claim | Source location | Scope and qualification |
| --- | --- | --- |
| Range/intensity representation and multi-noise-level score training. | Section 4.1; PDF pp. 7-8. | Representation-specific method. Avoid transferring physical-feasibility claims to arbitrary sensors. |
| Sampling uses repeated annealed Langevin updates. | Section 4.1; PDF pp. 8-9. | The cost implication is our interpretation; no latency comparison extracted. |
| Point insertion and other manipulations reuse real scan data. | Section 2.3; PDF pp. 4-5. | Supports augmentation boundary discussion, not a blanket claim that insertion is physically invalid. |

## Extraction limits

### Follow-up for RQ2/RQ3, 5 October 2026

AI-assisted targeted full-text check; author verification remains pending.
See [completion checks](../searches/2026-10-05-review-completion.md).

- Section 5.1: MMD uses 50 x 50 BEV histograms; JSD uses 100 x 100 BEV
  histograms. Fréchet range distance uses pretrained RangeNet++ activations.
- Table 1: ProjectedGAN MMD 3.47e-4 versus LiDARGen 3.87e-4 (lower better);
  LiDARGen has lower range-feature distance and JSD. The review follows the
  table, not the inconsistent numerical wording in Section 5.2.
- Section 5.3 and supplement: nuScenes generation concentrates points nearer
  the viewpoint, with worse BEV MMD despite favourable visual comparisons.
- Section 5.4: RangeNet++ applied to densified 16-beam inputs **without
  fine-tuning**. Reported IoU 0.394 for nearest-neighbour and 0.449 for LiDARGen;
  these are not training-on-generated-data gains or a full benchmark mIoU claim.
- Sections 4 and 5 distinguish unconditional sampling and conditional
  densification. Generated range/intensity does not itself provide semantic
  training labels.

The earlier extraction limits below apply to the original RQ1 notes; the
specific numerical extraction above extends them for this revision.

No numerical effect sizes, compute benchmarks or uncertainty estimates are extracted
for RQ1. Dataset sizes, full split details, seeds and model settings are not fully
extracted here and must be checked before using this study for an empirical RQ3
comparison. PDF page indices are one-based in the local copy, not necessarily
publisher page numbers. No human screening or checking is implied by this record.
