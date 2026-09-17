# Synthetic data literature review

A University of Twente-inspired academic manuscript scaffold with a dedicated title page, the supplied UT logo, a review framework table, a workflow figure, a linked glossary and mathematical examples. Draft prompts are explicitly marked. The literature review cites the Zotero-exported Alaa et al. paper as a starting point for evaluating synthetic data quality.

## Build

PDFs and `.bib` exports are local files excluded from Git. After cloning, configure Zotero's Better BibLaTeX export to write `references.bib` into this directory before building. Each collaborator needs the cited sources and matching citation keys in their export.

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

## Edit

- main.tex: overview, chapter order, PDF metadata, bibliography, glossary and appendix.
- cover.tex: visible title, authors, date and editable TikZ artwork.
- twente-paper.sty: margins, fonts, palette, headings, headers/footers, captions and reusable researchbox / draftnote commands.
- chapters/: research content; replace grey italic drafting prompts as writing progresses.
- references.bib: managed by Zotero through Better BibLaTeX automatic export. Update metadata in Zotero, because the next export overwrites manual edits.
- glossary.tex: term definitions; use `\gls{synthetic-data}`, `\Gls{synthetic-data}` or `\glspl{gan}` to create linked terms. Only used entries appear, alphabetically.
- Abbreviations: use `\gls{gan}` for **GAN**, `\glspl{gan}` for **GANs**, `\gls{machine-learning}` for **ML** and `\gls{ctgan}` for **CTGAN**. These blue labels jump directly to their full definitions in the glossary. Typing plain `GAN` does not create a hyperlink. Add another abbreviation with `\newglossaryentry{key}{name={ABC},description={Full name: definition}}` in glossary.tex, then use `\gls{key}` in the text.
- chapters/mathematical_examples.tex: removable example appendix with inline math, numbered equations, aligned expressions, matrices and cases. Use `\label{eq:name}` and `\eqref{eq:name}` for linked equation references.
- build.bat: runs XeLaTeX, Biber, XeLaTeX, XeLaTeX and produces main.pdf.

Use `\textcite{alaaHowFaithfulYour2022}` for an author-led citation or `\parencite{alaaHowFaithfulYour2022}` for a bracketed numeric citation. Import sources into Zotero and use their exported citation keys in the text. Only cited entries appear in the reference list; uncited library items remain in the export. After changing Zotero entries, let the automatic export finish, then run build.bat.

The body flows naturally as it grows. The overview, references, glossary and mathematical appendix start on separate pages.

## Design sources

The black-and-white palette and sans-serif typography take their cues from UT's public visual identity. Arial is an explicitly listed alternative to licensed Linotype Univers:

- [UT colours](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/colours)
- [UT fonts](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/font)
- [UT elements](https://www.utwente.nl/en/service-portal/communication/visual-identity/visual-identity-components/elements)

This is an independent student-paper design, not an official UT template. The cover graphic is original TikZ artwork, not UT's corporate graphic elements. The title page uses the supplied `Images/UTLogo.png` with its aspect ratio preserved.
