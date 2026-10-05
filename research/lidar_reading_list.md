# Reading path: synthetic data generation to automotive LiDAR

Prepared 1 October 2026. These are ten candidate readings, not ten included
studies or a completed systematic review. Metadata and relevance were checked
against publisher/proceedings records and author abstracts. Full-text extraction,
experimental comparisons and two-author screening remain to be done.
For the subsequent RQ1 source checks, see
[reading provenance](searches/2026-10-01-rq1-source-checks.md).

## Scope and reading order

Start with a short general taxonomy, then concentrate on scene-level automotive
LiDAR for detection and semantic segmentation. Compare statistical/procedural
methods, physics-based simulation, learned generation and hybrids. Separate
new scenes, new views of reconstructed scenes, and completion of existing scans.
This distinction is our proposed review structure, not a finding of the search.

Read Nikolenko selectively, then LiDARsim, LiDARGen, R2DM and SynLiDAR first.
Use LiDAR4D and SG-LDM to extend the comparison to dynamic reconstruction and
semantic control. Jordon and Alaa supply general concepts; CARLA supplies
simulation context. This list is representative, not a claim to cover the latest
or all relevant work through October 2026.

## General foundations

1. **Jordon et al. (2022), Synthetic Data -- what, why and how?**
   [Author report/preprint](https://arxiv.org/abs/2205.03257).
   An accessible introduction to definitions, uses and caveats, with a privacy
   emphasis. Useful for RQ1 terminology, but not direct evidence for LiDAR utility.

2. **Nikolenko (2019), Synthetic Data for Deep Learning.**
   [Survey preprint, version consulted](https://arxiv.org/abs/1909.11512).
   Maps simulation, synthetic datasets and synthetic-to-real adaptation across
   applications. Read the urban-scene and adaptation sections selectively.
   Useful for RQ1 and backward citation tracing; it predates recent diffusion work.

3. **Alaa et al. (ICML 2022), How Faithful is your Synthetic Data?
   Sample-level Metrics for Evaluating and Auditing Generative Models.**
   [Proceedings](https://proceedings.mlr.press/v162/alaa22a.html).
   General fidelity, diversity and generalization concepts for RQ3.
   Already in the bibliography as `alaaHowFaithfulYour2022`.
   Examine whether its representations and assumptions are appropriate for LiDAR;
   do not treat a domain-general framework as demonstrated LiDAR effectiveness.

## Simulation and the bridge to driving

4. **Dosovitskiy et al. (CoRL 2017), CARLA: An Open Urban Driving Simulator.**
   [Proceedings](https://proceedings.mlr.press/v78/dosovitskiy17a.html).
   Establishes an open driving simulator with configurable environments and
   sensor suites. Useful background for controllable virtual worlds (RQ1/RQ2).
   The original paper is not evidence about every feature of current CARLA or
   about the fidelity of modern LiDAR simulation; inspect version-specific work.

5. **Manivasagam et al. (CVPR 2020), LiDARsim: Realistic LiDAR Simulation
   by Leveraging the Real World.**
   [Proceedings and paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Manivasagam_LiDARsim_Realistic_LiDAR_Simulation_by_Leveraging_the_Real_World_CVPR_2020_paper.html).
   Combines reconstructed real-world assets, ray casting and learned corrections.
   A key hybrid-method example for RQ2. Extract its real-data requirements, scenario
   controls and perception-testing evidence. Keep testing/closed-loop evidence
   distinct from evidence for training-data augmentation.

## Learned generation and reconstruction

6. **Zyrianov, Zhu and Wang (ECCV 2022), Learning to Generate Realistic
   LiDAR Point Clouds (LiDARGen).**
   [Author manuscript](https://arxiv.org/abs/2209.03954).
   Uses score-based stochastic denoising in an equirectangular representation;
   also demonstrates conditioning and densification. A starting point for learned
   scan generation (RQ2). Inspect how realism is measured and what is actually
   demonstrated about downstream utility (RQ3).

7. **Nakashima and Kurazume (ICRA 2024), LiDAR Data Synthesis with Denoising
   Diffusion Probabilistic Models (R2DM).**
   [Author manuscript](https://arxiv.org/abs/2309.09256),
   [published DOI](https://doi.org/10.1109/ICRA57147.2024.10611480).
   Generates range and reflectance with diffusion and also supports completion.
   Useful for analysing representation and spatial assumptions (RQ2).
   Compare generation and completion evaluations separately; neither alone
   establishes better detection or segmentation after synthetic-data training.

8. **Zheng et al. (CVPR 2024), LiDAR4D: Dynamic Neural Fields for Novel
   Space-time View LiDAR Synthesis.**
   [Author manuscript](https://arxiv.org/abs/2404.02742).
   Studies dynamic scene reconstruction, temporal consistency and ray-drop
   modelling. Useful for RQ2's reconstruction branch. New views and times of
   recorded scenes must be distinguished from independent new-scene sampling.
   Examine split construction and whether unseen scenes are evaluated.

## Transfer and training usefulness

9. **Xiao et al. (AAAI 2022), Transfer Learning from Synthetic to Real
   LiDAR Point Cloud for Semantic Segmentation (SynLiDAR).**
   [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/20183),
   DOI: `10.1609/aaai.v36i3.20183`.
   Introduces synthetic annotated scans and point-cloud translation addressing
   appearance and sparsity differences. Covers augmentation and domain-adaptation
   setups. Central to RQ3: separate the contribution of synthetic data from that
   of the adaptation method and check real-test protocols.

10. **Xiang et al. (ICCV 2025), SG-LDM: Semantic-Guided LiDAR Generation
    via Latent-Aligned Diffusion.**
    [Proceedings PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Xiang_SG-LDM_Semantic-Guided_LiDAR_Generation_via_Latent-Aligned_Diffusion_ICCV_2025_paper.pdf),
    [author manuscript](https://arxiv.org/abs/2506.23606).
    Connects semantic conditioning, diffusion generation and cross-domain
    translation with segmentation augmentation. Relevant to RQ2 and RQ3.
    Extract label requirements, the source of semantic layouts, and controlled
    ablations separating synthesis from translation.

## What to record for each focused paper

| Dimension | Extraction question |
| --- | --- |
| Generation task | New scene, new view/time, translation, completion or augmentation? |
| Inputs and control | Real scans, images, assets, labels, layouts, trajectories or text? |
| Representation | Points, voxels, range images or an implicit scene representation? |
| Sensor properties | Beam pattern, range, intensity, occlusion, dropouts and motion? |
| Annotation | Are labels available, generated consistently and useful for the task? |
| Coverage | Which classes, environments, sensors and rare conditions are tested? |
| Quality evaluation | Paired geometry or unpaired distributions; which features and settings? |
| Training utility | Real-only, synthetic-only and mixed baselines on independent real tests? |
| Resources | Real-data dependence, assets, training/sampling cost, code and checkpoints? |
| Validity | Scene leakage, mismatched budgets, adaptation confounds and uncertainty? |

An interesting candidate synthesis question is whether stronger scan-quality
scores accompany stronger real-test perception results, and under which sensor
and training conditions. Establish whether sufficient comparable evidence exists
before claiming this is an open research gap.

Nikolenko, LiDARsim and LiDARGen are now present in the shared Zotero export;
use its existing citation keys. Import the remaining selected records, resolve duplicate
preprint/published versions and export the agreed citation keys before adding
new citations to the review. Additional foundational method papers are listed in the RQ1 source-check
notes for possible Zotero import; no manual bibliography entries are supplied.
