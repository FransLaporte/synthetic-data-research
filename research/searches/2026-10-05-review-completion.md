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

## Follow-up: glossary and overview figure

At the user's request, added an original editable TikZ diagram connecting
scene construction, LiDAR generation, labelled training data, perception
training and real-data evaluation. It distinguishes possible real development
inputs from held-out evaluation data and qualifies the scene and label stages
for learned generators. The existing LiDARsim illustrations remain.

Expanded and linked the glossary for MMD, JSD, FRD, BEV, IoU, voxels,
score matching, densification, fine-tuning and domain adaptation; linked
existing surfel, diffusion and mode-collapse entries. Kept brief explanations
where needed to follow the argument. The diagram is a conceptual synthesis,
not a new empirical result.

The updated build has **9 body pages**, with references on Arabic page 10:
15 PDF pages total (three front-matter, nine body, one references and two
glossary). The paper, proposal and slides all passed the citation/reference
checker after the shared glossary edit. Final diagram and glossary layouts
were rendered and inspected; no overfull boxes or unresolved references remain.

## Corrected requirement: 4--6 pages and approximately 15 references

The user subsequently corrected the requirement to 4--6 pages and approximately
15 used references, retaining the introduction-through-conclusion counting span.
This supersedes the earlier limits recorded above.

The final shortened revision contains **5 body pages and 15 distinct cited
references**. The complete PDF is 12 pages: three front-matter pages, five body
pages, two reference pages and two glossary pages. It retains the original
overview diagram and combined LiDARsim illustration. The font, margins and
body line spacing are unchanged. Repetitive explanations and overlapping
comparison tables were removed; the SynLiDAR results table remains.

Five additional existing bibliography entries were checked against their
local Zotero full texts: PreSIL, KITTI (2012), Shumailov et al. (2024),
Westphal and Brannath (2019), and Achterberg et al. (2026). Each now has a
separate study record. These references have specific roles: generation and
transfer, real benchmark context, recursive-training coverage risk,
selection-induced optimism, and task-aware metric selection respectively.
The latter is identified as a tabular preprint; recursive-training findings
are not extrapolated into a claim of collapse from one-pass LiDAR augmentation.

Direct web record checks were made at arXiv 1905.00160, the PMLR Westphal
landing page, the Nature Shumailov landing page and the EngrXiv Achterberg
record. The latter two could not be retrieved by the web tool, so locally
available full texts supplied the evidence. No new database search or
screening counts are claimed.

PreSIL Section IV.B revealed selection of the best checkpoint on its real
evaluation split. The manuscript explicitly records this limitation instead
of presenting its gain as an untouched-test result. All 15 keys exist in
the already-committed bibliography; the user's local bibliography edits remain
byte-for-byte unchanged and are not needed to resolve these citations.

Validation: full XeLaTeX/Biber build; repository citation/reference checker;
15 unique bibliography entries; introduction on Arabic page 1 and conclusion
on page 5; references beginning on page 6; rendered-page inspection;
no unresolved references or overfull boxes.
