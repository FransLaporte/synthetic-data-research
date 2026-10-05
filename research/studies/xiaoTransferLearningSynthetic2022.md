# Study: xiaoTransferLearningSynthetic2022

- Source: [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/20183).
- Version: AAAI 2022, local Zotero PDF; peer-reviewed conference article.
- Extraction: AI-assisted targeted reading, 5 October 2026; author verification pending.
- Search record: [completion checks](../searches/2026-10-05-review-completion.md).

| Claim | Location | Scope |
| --- | --- | --- |
| Virtual environments provide over 19 billion points and 32 semantic classes. | Abstract; SynLiDAR dataset section | Dataset scale does not itself prove deployment coverage. |
| Intensity model uses SemanticKITTI coordinates/labels and real intensity targets. | Dataset section, Rendering | Qualifies claims that synthesis requires no real data. |
| PCT separates appearance and sparsity translation. | Point Cloud Translation section | Translation is an additional learned intervention. |
| Real-only 60.3, +SynLiDAR 62.5, +PCT 64.7 mIoU on SemanticKITTI. | Table 2 | Differences: +2.2 and +4.4 percentage points from real-only. |
| Real-only 50.6, +SynLiDAR 53.2, +PCT 55.8 mIoU on SemanticPOSS. | Table 3 | Differences: +2.6 and +5.2 percentage points from real-only. |
| MinkowskiNet, SemanticKITTI validation sequence 08; SemanticPOSS validation sequence 03. | Experiments, Datasets and Implementation Details | These are real validation results, not an untouched final benchmark test claim. |
| Extra source classes mapped to unlabeled; voxel size 0.05; coordinates and intensity as features. | Same implementation section | Label mapping and preprocessing matter to comparison. |

No repeated-seed confidence intervals or complete compute/label-cost comparison
are extracted. The review does not infer statistical significance or general
deployment benefits from these point estimates.
