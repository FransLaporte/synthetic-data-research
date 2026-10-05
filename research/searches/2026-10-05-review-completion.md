# Review completion and source verification, 5 October 2026

This is a targeted verification log, not a systematic database search.
AI-assisted extraction; independent author screening and checking are pending.
The revised paper reports that limitation explicitly. No search-result totals,
screening counts, study-selection agreement or new experiments are claimed.

## Web queries actually issued

```text
site.openaccess.thecvf.com LiDARsim Realistic LiDAR Simulation 2020
site.arxiv.org LiDARGen 2209.03954
site.arxiv.org SynLiDAR Transfer Learning Synthetic Real LiDAR Point Cloud semantic segmentation
site.openaccess.thecvf.com Towards Zero Domain Gap 2023 LiDAR
```

Primary records consulted:

- [LiDARsim, CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Manivasagam_LiDARsim_Realistic_LiDAR_Simulation_by_Leveraging_the_Real_World_CVPR_2020_paper.html).
- [LiDARGen author manuscript](https://arxiv.org/abs/2209.03954), identifying ECCV 2022.
- [SynLiDAR author manuscript](https://arxiv.org/abs/2107.05399) and
  [authors' repository](https://github.com/xiaoaoran/SynLiDAR).
- [Paired-scenario ICCV 2023 paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Manivasagam_Towards_Zero_Domain_Gap_A_Comprehensive_Study_of_Realistic_LiDAR_ICCV_2023_paper.pdf).
  The HTML landing-page follow-up returned 403; the local Zotero full text was used.

## Full texts checked

The existing Zotero PDFs for LiDARsim, LiDARGen, SynLiDAR and Towards Zero
Domain Gap were extracted locally. Method and experiment passages, table
values and qualifications were checked against those texts. Extracted copies
and rendered review pages live in the ignored build directory, not in Git.
Earlier RQ1 source records remain the basis of the compressed general overview.

## Editorial decisions

- The inherited `rq2_metrics.tex` primarily answered evaluation/RQ3. Its supported
  arguments and SynLiDAR numerical results were condensed into RQ3; RQ2 now
  discusses generation and sensor requirements. Canonical questions are unchanged.
- LiDARsim's KITTI result is **BEV vehicle detection**, not a demonstrated full
  3D-detection result. Its SemanticKITTI comparison is vehicle/background
  segmentation, not the complete multiclass benchmark. Both use real validation
  splits. KITTI labels are used to construct the dynamic object bank.
- LiDARGen's completion experiment uses an existing segmenter without fine-tuning;
  it does not demonstrate gains from training on unconditional generated scans.
- SynLiDAR gains are reported in percentage points with baseline scores, model
  and validation sequences; PCT's intervention is separated from adding raw data.
- The paired-scenario study concerns evaluation of a trained autonomy system,
  not training gains. The proposed metric-to-utility study is a research direction,
  not an established novel gap.
- The original bibliography had uncommitted changes when work began. It was left
  byte-for-byte unchanged (SHA256:
  `1E945901BD69C72A4891ABBDB51204BE882A65A1D089B83F9077D0C20124A0DD`).

## Length and validation

The user confirmed 10 pages from introduction through conclusion. The revised
XeLaTeX/Biber build uses 8 pages for that span, with references starting on
Arabic page 9. The full PDF has 14 pages (three front-matter pages, eight body
pages, one reference page and two glossary pages). Font size, margins and body
line spacing are unchanged. Citations and cross-references pass the repository
checker; final pages were rendered for layout inspection.
