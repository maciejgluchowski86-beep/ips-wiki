# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/003-g-wave-one-source-audit-and-joint-taxonomy.md`.
- Student F: active on analytic/functional Assignment 002.
- Student G: active on coupling/graphical Assignment 002.

## Accepted staged coverage

Meetings 002--003 have source-audited and accepted twelve first-wave method entries. The live-wiki taxonomy is by load-bearing proof interface:

1. **Coupling and local influence:** attractive monotone coupling; Dobrushin influence contraction; path coupling.
2. **Spatial mixing and boundary influence:** disagreement percolation for Gibbs uniqueness; Dobrushin--Shlosman spatial-to-dynamical relaxation.
3. **Functional inequalities and comparison:** Poincare/spectral gap; LSI/mLSI; Dirichlet-form/canonical-path comparison; block-dynamics/bisection variance.
4. **Graphical ancestry, duality, and regeneration:** finite-ancestor duality/extinction; information percolation; East distinguished-zero screening.

All twelve are mathematically and taxonomically cleared for live-wiki promotion. Shared primary sources are not duplicate-entry evidence when the proof interfaces differ. Meeting 003 fixes the cross-linking rules.

Promotion is deferred only to the next quiet integration window while both students commit wave-two staging files.

## Current second wave

F Assignment 002 targets Lu--Yau/martingale recursion, spectral independence, block/approximate entropy factorization, bounded-perturbation transfer, moving-particle comparison, and finite-size relaxation criteria.

G Assignment 002 targets dynamical disagreement domination, coupling from the past, clan-of-ancestors perfect simulation, censoring inequalities, block/local/maximal coupling, and coalescing-random-walk voter duality.

The durability rule remains mandatory: every finished method entry is committed immediately as its own artifact.

## Wiki publication rule

The principal's instruction reopens the live wiki **for this toolbox section**. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Accepted material will be promoted to:

- `docs/ergodicity-methods.md` hub;
- one `status: literature`, `audit: current` method page under `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

The current live-wiki admission gate remains in force. Every staged entry needs an inspected primary source with an exact pinpoint; `validate_entries.py` checks structure only, while Professor review decides mathematical/source acceptance.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
