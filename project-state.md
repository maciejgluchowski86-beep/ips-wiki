# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/004-f-wave-two-source-audit-and-analytic-wave-three.md`.
- Student F: active on analytic breadth Assignment 003.
- Student G: active on coupling/graphical Assignment 002.

## Accepted staged coverage

Meetings 002--004 have source-audited and accepted **18** method entries. The principal reports all eighteen pass `validate_entries.py`.

Accepted coverage now includes:

- coupling/local influence: attractiveness, Dobrushin contraction, path coupling;
- spatial/local-to-global methods: disagreement percolation, Dobrushin--Shlosman, spectral independence, finite-size strong-mixing bootstrap;
- functional/comparison methods: Poincare, LSI/mLSI, Dirichlet/canonical paths, block bisection, Lu--Yau martingale recursion, entropy block factorization, Holley--Stroock perturbation, moving-particle/effective-resistance comparison;
- graphical ancestry/regeneration: finite-dual extinction, information percolation, East distinguished-zero screening.

The first twelve remain the first live-integration batch; F's six wave-two entries are queued behind them. Shared primary sources do not imply duplicate methods when the proof interfaces differ.

## Current assignments

F Assignment 003 targets Bakry--Emery/Bochner Gamma methods, two-scale/coarse-graining coercivity, Aldous/interchange spectral-gap reduction, Nash/spectral-profile smoothing with an IPS application, nonreversible coercivity with an IPS application, and conductance/Cheeger methods for spin chains, with source-supported substitutions allowed for weak targets.

G Assignment 002 continues on dynamical disagreement domination, CFTP, clan-of-ancestors perfect simulation, censoring, block/local/maximal coupling, and coalescing-random-walk voter duality.

The durability rule remains mandatory: every finished method entry is committed immediately as its own artifact.

## Wiki publication rule

The principal's instruction reopens the live wiki **for this toolbox section**. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Accepted material will be promoted to:

- `docs/ergodicity-methods.md` hub;
- one `status: literature`, `audit: current` method page under `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

`docs/` and `mkdocs.yml` are still untouched by the toolbox branch. Live integration is deferred until no student is actively committing a staging batch.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
