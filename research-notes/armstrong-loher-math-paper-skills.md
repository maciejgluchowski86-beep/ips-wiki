# Armstrong–Loher mathematical-paper writing workflow

Recorded: 2026-10-20  
Status: **Reference for future evaluation; not installed or adopted.**

## Sources

- **Paper-writing skills:** https://github.com/amelieloher/math-paper-skills
  - Public release dated 2026-10-06. Developed from a private collection by Scott Armstrong and Amélie Loher; hosted in Loher's GitHub account.
  - Licensed CC BY 4.0 (consult upstream for attribution and updates).
- **Armstrong's Lean formalization skills:** https://github.com/scottnarmstrong/LeanAutoformalizationSkills
- **Armstrong's explanation of the Lean architecture:** https://www.scottnarmstrong.com/2026/10/autoformalization-is-now-very-easy/
- **Loher's skills listing:** https://amelieloher.github.io/skills.html

## What is available

The paper-writing repository is a collection of agent instructions, not a new model or a turnkey research engine. It works with Codex and Claude Code and includes:

| Skill | Intended use |
| --- | --- |
| `latex-math-writing` | Mathematical prose, notation, statements, proofs, introductions, typesetting, and rendered-PDF review. |
| `math-paper-campaign` | Build a paper from notes or systematically polish an existing checked manuscript. |
| `math-figures` | Figures and animations that convey a mathematical idea. |
| `visual-paper` | Audited companion website with proof dependencies, quotations from the paper, and explanatory material. |

For an existing manuscript, `math-paper-campaign` organizes revision into successive phases: reduction, citations, linearization of exposition, rewriting, introduction, and final audit. Its described controls include work packets, a ledger of changes and status, independent reviewers, and checks against mathematical drift.

The main principles are: mathematical fidelity over stylistic polish; explain the idea before technical details; do not silently alter hypotheses, conclusions, constants, or quantifiers; inspect the *rendered PDF*; and independently check edited content.

The separate Lean repository organizes formalization around dependency graphs, author-approved frozen statements, bounded proof-writing tasks, independent audits, and verification of the exact formal statements. It is a much larger investment and serves a different function.

## Assessment for our IPS research loop

**Promising for exposition; unvalidated as a quantitative improvement.**

The reported remark that this produces a “90% finished paper” was not independently verified. No controlled before/after measurement was located in the upstream material as of this note. Treat it as an informal characterization, not a performance guarantee.

The immediate use case is editorial work after substantive mathematical claims and proofs have been checked. In particular, the methods address recurring problems encountered while drafting the patch-positivity paper:

- awkward or unfamiliar mathematical language;
- premature definitions and unexplained hypotheses;
- redundant exposition and inefficient ordering of statements;
- loss of a reader's perspective after repeated revisions;
- accidental mathematical changes during prose editing.

## Suggested pilot (not yet performed)

1. Select one substantial, mathematically checked section of the patch-positivity paper. Freeze its source version and establish a list of statements, assumptions, and citations that must remain intact.
2. Produce a separate revision with `latex-math-writing` and the relevant parts of `math-paper-campaign`. Do not overwrite the source manuscript.
3. Independently audit the diff for changes to assumptions, conclusions, quantifiers, constants, definitions, citations, and proof logic.
4. Have a fresh reader evaluate the original and revised sections for natural mathematical language, clarity, orientation, and redundancy without relying on the revision history.
5. Compile both versions and inspect the rendered pages. Compare correction workload, length, and actual readability with Georg before deciding whether to adopt the process.

Potential later integration: add scoped writing/auditing instructions to the research workflow while keeping proof discovery, proof verification, and final manuscript editing as separate stages.

**Next decision:** Test on one section before installing the full collection or changing the project's standing instructions.

No upstream skill files were vendored in this note; use and attribute the linked canonical sources if adopting them.
