# Study: manivasagamLiDARsimRealisticLiDAR2020

- Title: LiDARsim: Realistic LiDAR Simulation by Leveraging the Real World
- Source: [paper record](https://openaccess.thecvf.com/content_CVPR_2020/html/Manivasagam_LiDARsim_Realistic_LiDAR_Simulation_by_Leveraging_the_Real_World_CVPR_2020_paper.html)
- Version: CVPR 2020 primary study; Zotero CVF PDF.
- Role: Concrete hybrid example bridging RQ1 to RQ2.
- Search record: [RQ1 source checks](../searches/2026-10-01-rq1-source-checks.md).
- Extraction: AI-assisted targeted reading, 2026-10-01.
- Author A/B screening, agreed inclusion and author verification: pending.
- This is a targeted claim record for the draft, not a completed full-study appraisal.

## Claims used in RQ1

| Claim | Source location | Scope and qualification |
| --- | --- | --- |
| Scene assets are reconstructed from real recordings. | Sections 3.1-3.2; PDF pp. 3-4. | Uses repeated scene scans and object annotations; do not call it independent of real data. |
| Ray casting is combined with learned ray-drop modelling. | Sections 4.1-4.2; PDF pp. 4-5. | Hybrid example; ray drop is not rain-drop simulation. |
| Simplified materials and sensor modelling can create a domain gap. | Related work; PDF p. 3. | Authors' motivation. The RQ1 draft does not claim all simulators share identical limitations. |

## Figures used in the review

- `Images/IndividualLidarSweep to surfelmeshing.png`: user-supplied image
  matching Figure 4, PDF page 4. Four panels show an individual sweep,
  accumulated observations, symmetry completion and the refined surfel asset.
  The original caption groups outlier removal and surfel meshing in its last stage.
- `Images/RaycastvsLiDARsimvsRealLiDAR.png`: user-supplied image matching
  Figure 7, PDF page 6. Qualitative comparison of ray-cast LiDAR, LiDARsim
  and real LiDAR; discussed with the learned ray-drop method in Section 4.2.
- Both figures are attributed in the review using the existing Zotero key.
  Captions are paraphrased; no new bibliography entry or image alteration is used.

## Extraction limits

### Follow-up for RQ2/RQ3, 5 October 2026

AI-assisted targeted full-text check; author verification remains pending.
See [completion checks](../searches/2026-10-05-review-completion.md).

- Section 5.2 and Table 1: **vehicle/background** segmentation on SemanticKITTI
  validation, trained with 5,000 examples per source. Not full multiclass mIoU.
- Section 5.2 and Table 2: **BEV vehicle detection** on KITTI hard validation.
  At IoU 0.7: modified CARLA 42.2, LiDARsim 73.7, real KITTI 80.0.
  The table calls the score mAP; it is not evidence for full 3D detection.
- Section 5.2: sensor height and azimuth resolution adapted to KITTI, and KITTI
  labelled data used to build the dynamic object bank. Synthetic-only perception
  training therefore does not mean no real data or annotations in the pipeline.
- Sections 3.1--3.2: real asset reconstruction and vehicle symmetry; authors
  distinguish rigid vehicles from future support for deformable participants.
- Section 5.3: learned ray drop compared against no/random/ground-truth ray drop.

The earlier extraction limits below apply to the original RQ1 notes; the
specific numerical extraction above extends them for this revision.

No numerical effect sizes, compute benchmarks or uncertainty estimates are extracted
for RQ1. Dataset sizes, full split details, seeds and model settings are not fully
extracted here and must be checked before using this study for an empirical RQ3
comparison. PDF page indices are one-based in the local copy, not necessarily
publisher page numbers. No human screening or checking is implied by this record.
