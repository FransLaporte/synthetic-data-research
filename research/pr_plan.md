# Branches and PR plan

Prepared 1 October 2026. These are four local, committed branches forming a
stack. Each row adds only its own work on top of the previous row. The original
branch and `main` remain at the original base, `cc57915`.

| Order | Head branch | PR base branch | Focus |
| --- | --- | --- | --- |
| 1 | `research/01-lidar-scope` | `main` | Revised questions, broad-to-LiDAR scope, method and aligned paper/proposal/slides |
| 2 | `research/02-ai-acknowledgement` | `research/01-lidar-scope` | AI disclosure and title-page spacing |
| 3 | `research/03-sources-and-reading-notes` | `research/02-ai-acknowledgement` | User's Zotero export, annotated reading list, source-check notes and Zotero-only rule |
| 4 | `writing/04-rq1-generation-methods` | `research/03-sources-and-reading-notes` | RQ1 synthesis, comparison table, six evidence records and drafting disclosure |

RQ1 belongs to the requesting author; the coauthor's source verification remains
pending. No human screening decisions, approval or assignment of RQ2/RQ3 is
claimed. Their sections remain prompts.

## Publish the branches when ready

No PRs have been created and these branches have not been pushed by this work.
From the repository root, publish each branch without force:

```powershell
git push -u origin research/01-lidar-scope
git push -u origin research/02-ai-acknowledgement
git push -u origin research/03-sources-and-reading-notes
git push -u origin writing/04-rq1-generation-methods
```

Create each PR with the head/base pair above. Opening all four against `main`
immediately would show earlier changes repeatedly. Review and merge in order.
After the parent merges, check and retarget the next PR to `main`. If using
squash merges, the remaining branches may need rebasing onto the new parent
commit to remove already-merged changes from the diff; do not blindly force-push.

## Suggested PR titles and descriptions

### 1. Refocus the review on synthetic generation and automotive LiDAR

The review previously focused on assessing synthetic images. Revise the shared
questions and scope to start with general generation methods, then examine
LiDAR generation and real-test perception evidence. Align the paper, proposal,
slides, section prompts and extraction template. Validation: all three LaTeX
documents built, with resolved citations and cross-references.

### 2. Acknowledge AI assistance on the title page

Add the author's AI acknowledgement and adjust spacing so the disclosure,
contact details and institutional footer fit on the formal title page.
Validation: the review built with resolved references. The final combined
title-page layout was also inspected visually.

### 3. Add Zotero sources and a focused reading path

Commit the author's Zotero export, retain existing citation keys, and add an
annotated candidate reading list and source-check notes. Record that all
bibliography entries must come from Zotero. No manually authored bibliography
entries or supplementary `.bib` files are included. Metadata corrections and
possible foundational-paper imports are listed for the author in the notes.

Validation: the final stack builds using only `references.bib`; its Git blob
matches the pre-split recovery snapshot exactly.

### 4. Draft RQ1: synthetic data generation methods and trade-offs

Replace RQ1 prompts with a cited synthesis of statistical generation,
procedural/physical simulation, neural generators and hybrid approaches.
Add a comparison table, an explicit answer and a bridge to the LiDAR questions.
Six source records link claims to PDF sections and qualify their scope.
Update the AI disclosure to include drafting assistance. Author screening and
verification remain pending; RQ2 and RQ3 are not presented as completed findings.

Validation: all three documents built with resolved citations/references;
the RQ1 pages and title-page layout were inspected. No training experiment
or comprehensive literature search is claimed.

## Recovery and bibliography

The stash labelled `Recovery snapshot before splitting scope, AI disclosure,
sources and RQ1 work` preserves the original staged/unstaged tracked changes
and untracked reading list. A second stash preserves an intermediate RQ1 draft.
Keep the original recovery stash until satisfied with the split; applying it
over the completed branches is unnecessary and may create conflicts.

Only files relevant to this repository were reorganised. Zotero's database and
PDF attachments were read but not modified. Import any additional source into
Zotero and export it before citing its key in LaTeX.
