# Study: manivasagamZeroDomainGap2023

- Source: [ICCV 2023 paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Manivasagam_Towards_Zero_Domain_Gap_A_Comprehensive_Study_of_Realistic_LiDAR_ICCV_2023_paper.pdf).
- Version: published ICCV paper, local Zotero IEEE PDF.
- Extraction: AI-assisted targeted reading, 5 October 2026; author verification pending.
- Search record: [completion checks](../searches/2026-10-05-review-completion.md).

| Claim | Location | Scope |
| --- | --- | --- |
| Reconstructed digital twins enable paired comparison of real and simulated scenarios. | Section 4 | Requires matched recordings and reconstruction. |
| Oracle modifications investigate missing returns, multiple echoes, noise and scanning effects. | Sections 3.2 and 5; Tables 1 onward | Diagnostic study, not a reference-free deployable generator. |
| Motion blur, material response and traffic-participant geometry contribute to discrepancies. | Introduction and experimental analysis | Effects depend on the sensor and system under study. |
| Standard aggregate perception precision/recall need not track planning domain gap. | Introduction; Section 4 metric definitions; experimental analysis | Distinguish detection agreement and planning-output differences. |
| Autonomy system is already trained. | Section 4, text following scenario/domain-gap definitions | Does not show gains from retraining on generated data. |

No numerical planning effects are reproduced; no cross-system universality or
synthetic-training improvement is claimed. Novelty of the review's proposed
diagnostic-to-training-utility extension still requires broader searching.
