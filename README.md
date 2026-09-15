# Synthetic data literature review

A University of Twente-inspired academic manuscript scaffold with a dedicated title page, the supplied UT logo, a review framework table, a workflow figure, a linked glossary and mathematical examples. Draft prompts are explicitly marked. Two real papers are included as example references, not a completed literature synthesis.

## Build

On Windows, run `build.bat` using MiKTeX or TeX Live (with XeLaTeX and BibTeX on PATH). The script works from any working directory and stops on errors. In PowerShell:

```powershell
.\build.bat
```

Equivalent manual build:

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Use **XeLaTeX** on Overleaf too. Arial is used when installed; otherwise the template uses TeX Gyre Heros. The build resolves contents, citations, equations and glossary links. The glossary uses `glossaries` in no-index mode, so neither Perl nor `makeglossaries` is needed. Install missing LaTeX packages through your distribution; additions include `natbib`, `glossaries`, `amsmath`, `amssymb` and `bm`.

## Edit

- main.tex: overview, chapter order, PDF metadata, bibliography, glossary and appendix.
- cover.tex: visible title, authors, date and editable TikZ artwork.
- twente-paper.sty: margins, fonts, palette, headings, headers/footers, captions and reusable researchbox / draftnote commands.
- chapters/: research content; replace grey italic drafting prompts as writing progresses.
- references.bib: verified bibliography entries.
- glossary.tex: term definitions; use `\gls{synthetic-data}`, `\Gls{synthetic-data}` or `\glspl{gan}` to create linked terms. Only used entries appear, alphabetically.
- Abbreviations: use `\gls{gan}` for **GAN**, `\glspl{gan}` for **GANs**, `\gls{machine-learning}` for **ML** and `\gls{ctgan}` for **CTGAN**. These blue labels jump directly to their full definitions in the glossary. Typing plain `GAN` does not create a hyperlink. Add another abbreviation with `\newglossaryentry{key}{name={ABC},description={Full name: definition}}` in glossary.tex, then use `\gls{key}` in the text.
- chapters/mathematical_examples.tex: removable example appendix with inline math, numbered equations, aligned expressions, matrices and cases. Use `\label{eq:name}` and `\eqref{eq:name}` for linked equation references.
- build.bat: runs XeLaTeX, BibTeX, XeLaTeX, XeLaTeX and produces main.pdf.

Use `\citet{goodfellow2014generative}` for an author-led citation or `\citep{xu2019modeling}` for a bracketed numeric citation. Add entries to references.bib and cite their keys in the text; the reference list is generated automatically with linked source URLs. Replace or remove the example-citation subsection as the review develops.

The body flows naturally as it grows. The overview, references, glossary and mathematical appendix start on separate pages.

## Design sources

The black-and-white palette and sans-serif typography take their cues from UT's public visual identity. Arial is an explicitly listed alternative to licensed Linotype Univers:

- [UT colours](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/colours)
- [UT fonts](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/font)
- [UT elements](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/elements)

This is an independent student-paper design, not an official UT template. The cover graphic is original TikZ artwork, not UT's corporate graphic elements. The title page uses the supplied `Images/UTLogo.png` with its aspect ratio preserved.

