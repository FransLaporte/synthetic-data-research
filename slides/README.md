# Beamer template

Compile `presentation.tex` from the repository root with `build.bat presentation`.
The output is `presentation.pdf` (16:9). Use XeLaTeX and Biber, also on Overleaf.
The starter deck presents the proposed study; it contains no invented results.

- Edit one topic per file in this folder; include new files in `presentation.tex`.
- Copy a frame from `method.tex` for a list/block layout, `motivation.tex` for
  columns, or `assessment.tex` for a table.
- Change deck title, authors and date in `presentation.tex`.
- Edit the cover's proposal label in `beamerthemeTwenteResearch.sty` when adapting
  the deck for the final paper presentation.
- Edit question wording only in `shared/questions.tex`.
- Add citations using the shared `references.bib` and Zotero workflow.
- Keep frames short; split a crowded frame instead of shrinking its text.
- The theme is independent and UT-inspired, not an official university template.
- `twente-visual.sty` shares fonts and colours with the paper and proposal;
  Beamer has its own layout and does not load the article-only paper style.
