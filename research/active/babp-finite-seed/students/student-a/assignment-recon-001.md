# Graduate Student A reconnaissance 001: opportunity-cost scan from recent open-problem literature

Work on branch `research/babp-finite-seed`.

This is a bounded target-selection task for the Professor, not a reopening of FA-1f and not a second active programme.

The current working target is all-parameter finite-seed convergence for one-dimensional BABP. Graduate Student B is auditing that problem's historical threshold and the 2025 DFP inputs. Your job is to determine whether there is a materially better problem we should be working on before we invest deeply in BABP.

The principal has supplied two pieces of scientific guidance which matter here:

1. extensive prior ChatGPT work on one-dimensional FA-1f off-equilibrium convergence did not yield results, so neighboring KCM convergence problems carry a real tractability prior against them unless there is a new concrete handle;
2. cancellation/duality is not a required mechanism. Search problem-first. Recent serious survey/progress papers that state open problems are especially useful starting points.

Read the current:

- `project-state.md`;
- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/fa1f-finite-seed/meetings/002-unnormalized-patch-review.md` for the latest closure logic and negative lessons.

Use the canonical patch paper only where it is actually relevant. Do not force patches, centered moments, or duality onto candidates.

## Source pool

Begin with recent high-quality sources that genuinely summarize current progress or state explicit open problems. At minimum inspect:

- Martinelli--Shapira--Toninelli (2025), *Long time behaviour of one facilitated kinetically constrained models: results and open problems*;
- Hartarsky--Toninelli (2025), *Kinetically Constrained Models*, especially explicit conjectures/open problems;
- Capannoli--den Hollander (2024), *Interacting Particle Systems on Random Graphs*, looking for explicit unresolved problems rather than generic exposition;
- Ngoc--Schuetz (2025), *Open interacting particle systems and Ising measures*, for open-boundary IPS problems if they are mathematically precise and serious;
- other 2024--2026 survey/progress papers in probability, IPS, stochastic processes, KCM, branching/coalescing systems, or adjacent areas that you judge stronger than these.

You may use broad open-problem compilations such as Randomstrasse only as discovery tools. A candidate should ultimately be grounded in serious field literature and checked against successors.

## What to return

Return at most **five** candidate problems. Fewer is preferable if the others are weak.

For each candidate give:

1. a precise mathematical target, not a topic;
2. the exact source location where it is stated open, or a reasoned novelty case if no explicit open statement is available;
3. a successor-literature check through August 2026, including alternate terminology where relevant;
4. the current best result and the concrete obstruction separating it from the target;
5. one plausible first calculation or lemma that could falsify tractability cheaply;
6. why this group has or lacks a comparative advantage, including possible use of the principal's prior work but without forcing it;
7. a candid expected-value assessment relative to the current BABP finite-seed problem.

Do not nominate any closed programme or route from `project-state.md`. The broader problem behind a closed route may appear only if you can articulate a genuinely different obstruction-level mechanism; otherwise exclude it.

Treat 1D FA-1f off-equilibrium convergence as having a substantial negative tractability prior from prior project effort plus the just-closed programme. Do not recommend it unless you find a qualitatively new theorem interface that was not part of those efforts.

## Ranking criterion

Rank candidates primarily by the product of:

- mathematical significance;
- confidence the problem is actually unresolved;
- tractability for a small persistent LLM research group over sustained work;
- sharpness/localization of the present obstruction;
- availability of a cheap first falsification test;
- genuine leverage from the group's background or the principal's prior mathematics.

Do **not** rank by superficial resemblance to cancellation, patches, duality, or the existing papers.

For the current BABP target, include it in the comparison even if it is not one of your external candidates. State explicitly whether, after the scan, you would keep BABP as the next serious investment or replace it, and why.

## Durable output

Commit the reconnaissance to

`research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`.

Keep literature claims source-specific and distinguish explicit open statements from your inference. End with a short Professor handoff naming the top one or two targets and the single cheapest calculation that would discriminate between them.
