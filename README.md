# Synthetic data literature review

A University of Twente-inspired academic manuscript scaffold with an original vector cover, a review framework table and a workflow figure. Draft prompts are explicitly marked; no findings or references have been invented.

## Build

Run from this directory using MiKTeX or TeX Live:

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Use **XeLaTeX** on Overleaf too. Arial is used when installed; otherwise the template uses TeX Gyre Heros. Two passes resolve contents and cross-references. Once actual citations are added, enable the bibliography lines in main.tex and run XeLaTeX, BibTeX, XeLaTeX, XeLaTeX.

## Edit

- main.tex: overview, chapter order, PDF metadata and bibliography switch.
- cover.tex: visible title, authors, date and editable TikZ artwork.
- twente-paper.sty: margins, fonts, palette, headings, headers/footers, captions and reusable researchbox / draftnote commands.
- chapters/: research content; replace grey italic drafting prompts as writing progresses.
- references.bib: verified bibliography entries.

The body flows naturally as it grows; only the overview and the current methodology spread start on new pages. Remove the latter clearpage in main.tex if continuous flow is preferred.

## Design sources

The black-and-white palette and sans-serif typography take their cues from UT's public visual identity. Arial is an explicitly listed alternative to licensed Linotype Univers:

- [UT colours](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/colours)
- [UT fonts](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/font)
- [UT elements](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/elements)

This is an independent student-paper design, not an official UT template. The cover graphic is original TikZ artwork, not UT's corporate graphic elements. The institutional name is plain text, not an official logo.

