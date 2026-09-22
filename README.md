# Synthetic data literature review

## Three documents, one research project

| Document | Root file | Content files | Windows build |
| --- | --- | --- | --- |
| Literature review | `main.tex` | `chapters/` | `build.bat main` |
| Research proposal | `proposal.tex` | `proposal/` | `build.bat proposal` |
| Beamer presentation (16:9) | `presentation.tex` | `slides/` | `build.bat presentation` |

Run `build.bat all` to build all three. No argument still builds the paper.
Use these root files on Overleaf too; all use XeLaTeX and Biber.
Outputs are `main.pdf`, `proposal.pdf` and `presentation.pdf`, excluded from Git.
For manual builds, replace `main` in the commands below with the desired root.
Validate with `python scripts/check_latex.py proposal` (or `main`/`presentation`).

The **main research question** is: How can the suitability of synthetic datasets
for training computer vision models be assessed in terms of data requirements,
quality metrics and assessment resources?

RQ1--RQ3 are its subquestions. Edit their canonical wording only in
`shared/questions.tex`; all three documents load it. Article question layout
is in `shared/question-block.tex`. Shared fonts and colours live in
`twente-visual.sty`; slide layouts live in `beamerthemeTwenteResearch.sty`.

See [proposal notes](proposal/README.md), [Beamer notes](slides/README.md) and
the [deadlines and rubric checklist](research/course_requirements.md).
Draft review: **5 October 2026**; proposal: **9 October, 17:00**; peer review:
**12 October**; supervisor feedback: **19 October**; both final documents:
**6 November, 17:00** (Europe/Amsterdam). The proposal is a draft for coauthor
review; its candidate gap must still be substantiated by the literature review.

## Paper structure and shared writing

The paper focuses on synthetic data for **computer vision**. It is a working
review scaffold: candidate metrics and drafting prompts are not final findings.
Read [CONTRIBUTING.md](CONTRIBUTING.md) for the two-author Git workflow and
[research/README.md](research/README.md) for shared evidence records.

| Reading order | File | Purpose |
| --- | --- | --- |
| Abstract | `chapters/abstract.tex` | Write last, once the answers are known. |
| 1. Introduction | `chapters/introduction.tex` | Vision scope and three research questions. |
| 2. Background | `chapters/background.tex` | Concepts and working definitions. |
| 3. Methodology | `chapters/methodology/*.tex` | Search, selection, extraction and synthesis. |
| 4. Findings: RQ1 | `chapters/findings/rq1_requirements.tex` | Requirements on synthetic vision data. |
| 4. Findings: RQ2 | `chapters/findings/rq2_metrics.tex` | Metrics, validity and limitations. |
| 4. Findings: RQ3 | `chapters/findings/rq3_assessment_resources.tex` | Real data, priors, networks and other inputs. |
| 5. Discussion | `chapters/discussion.tex` | Integrate answers, trade-offs and limitations. |
| 6. Conclusion | `chapters/conclusion.tex` | Concise answers to all three questions. |

`main.tex` assembles the paper; `chapters/methodology.tex` and
`chapters/literature_review.tex` assemble their respective subsections.
Compile **main.tex**, not individual section files. The mathematical example
appendix is retained as a writing aid but excluded from the paper by default.

A University of Twente-inspired manuscript scaffold with a dedicated title page,
the supplied UT logo, a candidate assessment table and a linked glossary.
Draft prompts are explicitly marked. The background cites the Zotero-exported
Alaa et al. paper as a starting point for evaluating synthetic data quality.

## Build

PDFs are excluded from Git; `references.bib` is versioned so local and GitHub builds use the same sources and citation keys. After cloning, the committed bibliography is ready to build. When updating sources, configure Zotero's Better BibLaTeX export to write `references.bib` into this directory and commit the updated export with the text that cites it.

On Windows, run `build.bat` using MiKTeX or TeX Live (with XeLaTeX and Biber on PATH). The script works from any working directory and stops on errors. In PowerShell:

```powershell
.\build.bat
```

Equivalent manual build:

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Use **XeLaTeX** on Overleaf too. Arial is used when installed; otherwise the template uses TeX Gyre Heros. The build resolves contents, citations, equations and glossary links. The glossary uses `glossaries` in no-index mode, so neither Perl nor `makeglossaries` is needed. Install missing LaTeX packages through your distribution; additions include `biblatex`, `glossaries`, `amsmath`, `amssymb` and `bm`.

## GitHub Actions: PDF downloads and merge checks

`.github/workflows/latex.yml` builds pull requests targeting `main`, every push
to `main`, merge-queue groups, and manual runs. All three documents are built
and included in the downloadable artifact. The rolling release still publishes
the literature review only. XeLaTeX and Biber run through
latexmk. The `LaTeX build` check fails on compilation errors, missing bibliography
entries and unresolved references. Linux uses the template's TeX Gyre Heros font
fallback when Arial is unavailable, so line breaks can differ from Windows.

### Bibliography collaboration

CI reads the committed `references.bib`; no shared URL or secret is needed.
Keep citation keys stable and use the same Better BibLaTeX export settings.
Prefer a shared Zotero collection/library or one person managing the export:
exporting an incomplete personal library over this file can remove a coauthor's
references. Review the bibliography diff before committing. If Git reports a
conflict, preserve the required entries or regenerate from the complete shared
collection, then rebuild. Avoid changing metadata for the same entries in parallel.

### Download the PDF

- [Latest successful main PDF](https://github.com/FransLaporte/synthetic-data-research/releases/download/latest-pdf/main.pdf)
  is updated after successful `main` builds. It is stored as a release asset,
  outside Git, without the Actions artifact expiry. The rolling prerelease notes
  identify the source commit and workflow run; its tag marks initial creation.
- For a particular PR or commit, open **Actions > LaTeX PDF > run > Artifacts**
  and download `paper-<commit SHA>`. These artifacts are retained for 90 days
  (subject to repository policy). Failed runs upload diagnostic logs.
- The latest link becomes available after the first successful `main` publication.
  If a build fails, the link continues to serve the previous successful build.

### Require compilation before merging

After the workflow has run once, a repository administrator should configure a
branch protection rule/ruleset for `main` in **Settings > Branches / Rules**:

1. Require pull requests before merging.
2. Require status checks to pass: select **LaTeX build** (GitHub Actions).
3. Require the branch to be up to date before merging.
4. Apply the rule to administrators too if everyone must obey it.

The YAML creates the check; it cannot itself enable GitHub branch protection.
Do not require the publication job, which runs only on `main`. The workflow needs
Actions enabled and permission for its publication job to write release assets.

## Editing the document

- main.tex: chapter order, PDF metadata, bibliography and glossary; abstract text is in chapters/abstract.tex.
- cover.tex: visible title, authors, date and editable TikZ artwork.
- twente-paper.sty: margins, fonts, palette, headings, headers/footers, captions and reusable researchbox / draftnote commands.
- chapters/: research content; replace grey italic drafting prompts as writing progresses.
- references.bib: managed by Zotero through Better BibLaTeX automatic export. Update metadata in Zotero, because the next export overwrites manual edits.
- glossary.tex: term definitions; use `\gls{synthetic-data}`, `\Gls{synthetic-data}` or `\glspl{gan}` to create linked terms. Only used entries appear, alphabetically.
- Abbreviations: use `\gls{gan}` for **GAN**, `\glspl{gan}` for **GANs**, `\gls{machine-learning}` for **ML** and `\gls{ctgan}` for **CTGAN**. These blue labels jump directly to their full definitions in the glossary. Typing plain `GAN` does not create a hyperlink. Add another abbreviation with `\newglossaryentry{key}{name={ABC},description={Full name: definition}}` in glossary.tex, then use `\gls{key}` in the text.
- chapters/mathematical_examples.tex: removable example appendix with inline math, numbered equations, aligned expressions, matrices and cases. Use `\label{eq:name}` and `\eqref{eq:name}` for linked equation references.
- build.bat: runs XeLaTeX, Biber, XeLaTeX, XeLaTeX and produces main.pdf.

Use `\textcite{alaaHowFaithfulYour2022}` for an author-led citation or `\parencite{alaaHowFaithfulYour2022}` for a bracketed numeric citation. Import sources into Zotero and use their exported citation keys in the text. Only cited entries appear in the reference list; uncited library items remain in the export. After changing Zotero entries, let the automatic export finish, then run build.bat.

The body flows naturally as it grows. The overview, references and glossary start on separate pages.

## Design sources

The black-and-white palette and sans-serif typography take their cues from UT's public visual identity. Arial is an explicitly listed alternative to licensed Linotype Univers:

- [UT colours](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/colours)
- [UT fonts](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/font)
- [UT elements](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/elements)

This is an independent student-paper design, not an official UT template. The cover graphic is original TikZ artwork, not UT's corporate graphic elements. The title page uses the supplied `Images/UTLogo.png` with its aspect ratio preserved.
