# Student G Assignment 006: source-led one-dimensional, contour, and graphical breadth

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 015, `entry-template.md`, your `005-handoff.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Wave seven is deliberately source-led. Do not spend another block on generic coupling labels that have already failed the concrete-application gate. Inspect the named primary source families below and isolate only proof interfaces that remain genuinely distinct from the 67 live pages.

Do **not** force four entries.

## Targets

1. **Gray's positive-rates theorem for one-dimensional attractive/repulsive nearest-neighbour spin systems.** Inspect Lawrence F. Gray, *The positive rates problem for attractive nearest neighbor spin systems on Z*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 61 (1982), 389--404, DOI `10.1007/BF00539839`, together with the companion Gray--Griffeath stability paper only if the proof requires it. The theorem itself is central but a page belongs only if you can state the actual load-bearing proof object beyond generic attractiveness/extremal-law reduction. Do not create a page that merely says “attractiveness + positive rates implies uniqueness.”

2. **Gray's duality for general attractive spin systems and edge relaxation.** Inspect Lawrence Gray, *Duality for General Attractive Spin Systems with Applications in One Dimension*, Ann. Probab. 14 (1986), 371--396. The source develops a monotonicity-based dual for nonadditive attractive spin systems and uses it for one-dimensional convergence/edge results. Determine whether this duality and its edge-process application form a distinct page from the live finite-dual extinction, voter-coalescence, parity-duality, and successful-fixed-size-dual pages. Merge with target 1 only if primary inspection shows that they are not separable interfaces.

3. **Toom graphs/contours for low-noise probabilistic cellular automata.** Start with de Maere d'Aertrycke--Ponselet, *Exponential Decay of Correlations for Strongly Coupled Toom Probabilistic Cellular Automata*, J. Stat. Phys. 147 (2012), 634--652, DOI `10.1007/s10955-012-0487-9`, arXiv `1110.1540`. The possible page should isolate the graphical error/Toom-contour expansion that turns erosion plus low noise into exponential convergence and space-time correlation decay. Keep it distinct from disagreement percolation and ordinary Peierls/Gibbs uniqueness if the source supports that distinction.

4. **Essential hitting times as survival-conditioned subadditive regeneration.** Start with Garet--Marchand, *Asymptotic shape for the contact process in random environment*, Ann. Appl. Probab. 22 (2012), 1362--1410, DOI `10.1214/11-AAP796`, arXiv `0910.1230`. The candidate interface is the essential hitting time: replace ordinary hitting times, which lose stationarity/subadditivity after survival conditioning, by a regeneration time that supports an almost-subadditive ergodic theorem. This is an adjacent long-time-growth method, not automatically an ergodicity page; include it only if the renewal/subadditive architecture is sufficiently reusable and clearly distinct from the live survival-conditioned complete-convergence renewal page.

## Closed searches

Do not reopen the generic disagreement-front regeneration search or the generic quasi-successful-coupling search. Your previous wave found no concrete interacting-process theorem satisfying the gate. Generic boundary-uniform projective coupling and generic common/basic graphical coupling remain closed as well.

## Entry standard

For each surviving source family, create one staged page using the current template. Check exact theorem/proposition/section pinpoints in the primary source. Preserve source scope: phase-specific convergence, edge laws, growth/shape, and global ergodicity are different conclusions.

The Gray targets are especially important taxonomically: the live attractiveness page records attractiveness as a reduction, not Gray's one-dimensional positive-rates proof. A Gray page must explain what extra mechanism actually closes the theorem.

## Durability

Commit each finished entry immediately as its own substantive commit. Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-g/006-handoff.md` listing entry commits, exact source pinpoints, merge/rejection decisions, and any new source-led gaps. Mechanical validation remains structural only.
