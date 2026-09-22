# Writing together

Start with `README.md` for the paper map and build instructions. The repository
root is the inner `synthetic-data-research` directory containing `main.tex`.

## Divide the work

Coordinate proposal (`proposal/`), paper (`chapters/`) and slide (`slides/`)
sections separately. See `research/course_requirements.md` for deadlines and
the rubric. Edit question wording only in `shared/questions.tex`; review it
together because it affects all documents. After shared question, style or
bibliography changes, run `build.bat all` and inspect every PDF. Otherwise build
the relevant document and run `python scripts/check_latex.py main`, `proposal`
or `presentation` as appropriate.

Agree on a lead and reviewer for each file in a GitHub issue before editing.
Suggested split (swap as needed): author A leads RQ1 and RQ3; author B leads
RQ2; each reviews the other's work. Divide source screening between neither:
both record independent screening decisions, then resolve disagreements.
Agree on the methodology together before searching. Write the discussion,
conclusion and abstract after the findings.

Each RQ has a separate file under `chapters/findings/`; the three methodology
parts are under `chapters/methodology/`. Keep `main.tex` and the two section
wrapper files for ordering only. Coordinate edits to shared files, especially
`references.bib`, `glossary.tex` and the style file. Use one paragraph per block
with short source lines to make diffs readable.

## Branch, write, review, merge

Begin from a clean working tree. Commit or deliberately stash current work
before switching branches; never discard a coauthor's changes to fix a conflict.

```powershell
git switch main
git pull --ff-only origin main
git switch -c writing/rq1-requirements
# Edit the section and add its supporting study records.
.\build.bat
python scripts/check_latex.py
git diff --check
git diff
git add chapters/findings/rq1_requirements.tex
# Also stage specific evidence files and bibliography updates you reviewed.
git commit -m "Draft vision data requirements with supporting evidence"
git push -u origin writing/rq1-requirements
```

Use a unique branch name for each contribution. Open a pull request to `main`,
request the other author's review, and wait for the existing **LaTeX build**
check. Resolve comments and merge through GitHub. The README explains how an
administrator can require PRs and passing checks; those rules are not enabled
by this guide. Each author needs GitHub access to push, or can use a fork.

To bring current main into an unfinished writing branch, first commit your
work, then run `git fetch origin` and `git merge origin/main`. For conflicts,
agree on the intended text, remove conflict markers, stage the resolved files,
complete the merge and rebuild. Do not simply choose an entire version of a
bibliography or section. Prefer small PRs covering one coherent contribution.

## Evidence and references

Copy `research/templates/study.md` to `research/studies/<citation-key>.md` for
each source. Each record links claims to source locations and RQ1--RQ3.
Use `research/templates/search.md` for one file per search under
`research/searches/`. Separate files reduce concurrent edits to a shared table.
Keep records for excluded sources too so screening decisions are auditable.
Use `not reported` for missing information; do not infer experimental results.

Import sources through the shared Zotero workflow and preserve citation keys.
Review the exported bibliography diff before staging it. Do not overwrite the
shared bibliography with an incomplete personal library. Discuss overlapping
bibliography changes before exporting. PDFs and generated build files stay
outside Git; source notes should contain links and concise paraphrases.

## Review checklist

- Does the section answer its assigned question and remain focused on vision?
- Can each claim be traced to a source and page/table/figure?
- Are proposals and untested assumptions distinguished from findings?
- Are metric definitions, prerequisites and limitations documented?
- Have task, dataset, model and protocol differences been accounted for?
- Does the complete paper compile with resolved citations and references?
