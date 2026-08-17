# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction. Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/004-f-wave-two-source-audit-and-analytic-wave-three.md`.

## Publication target and wiki status

The live wiki is reopened for this toolbox section only. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Research entries are staged under this workspace. Source-audited entries are later promoted as ordinary `status: literature`, `audit: current` pages under a new top-level MkDocs section `Ergodicity methods`:

- `docs/ergodicity-methods.md` hub;
- `docs/entries/<method-slug>.md` concept pages;
- `mkdocs.yml` top-level navigation.

The principal reports that `docs/` and `mkdocs.yml` remain byte-identical to `origin/main` after F Assignment 002. No live promotion has yet occurred.

## Workers and current assignments

- Student F: active on `students/student-f/assignment-003.md`, analytic breadth wave three.
- Student G: active on `students/student-g/assignment-002.md`, coupling/graphical breadth wave two. Do not interrupt or retask before handoff.

Every finished method entry is committed immediately as its own artifact. A rendering/session failure should cost at most the current unfinished entry.

## Inclusion and source standard

Include a method when it has a rigorous theorem/criterion/reusable proof architecture, a spin-system/IPS/KCSM/Glauber application or formulation, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete IPS/spin application. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Only `source_status: primary-checked` entries accepted in a Professor source-audit meeting are eligible for live promotion.

`validate_entries.py` checks metadata, headings, source-pinpoint/URL presence, and length only; it does not certify attribution or mathematical correctness.

## Accepted staged entries

Meetings 002--004 source-audited and accepted **eighteen** staged entries.

### Coupling and local influence

- `attractive-monotone-coupling-extremal-laws.md`;
- `dobrushin-influence-contraction.md`;
- `path-coupling-glauber-dynamics.md`.

### Spatial mixing and local-to-global influence

- `disagreement-percolation-gibbs-uniqueness.md`;
- `dobrushin-shlosman-spatial-to-dynamical.md`;
- `spectral-independence-local-to-global.md`;
- `finite-size-strong-mixing-criterion.md`.

### Functional inequalities, comparison, and multiscale coercivity

- `poincare-spectral-gap.md`;
- `log-sobolev-modified-log-sobolev.md`;
- `dirichlet-form-canonical-path-comparison.md`;
- `block-dynamics-bisection-variance.md`;
- `lu-yau-martingale-conditional-variance.md`;
- `block-factorization-entropy.md`;
- `holley-stroock-bounded-perturbation.md`;
- `moving-particle-long-jump-exclusion.md`.

### Graphical ancestry, duality, and regeneration

- `duality-extinction-finite-ancestor-process.md`;
- `information-percolation-backward-histories.md`;
- `east-distinguished-zero-screening.md`.

All eighteen are source-audited staged material. The first twelve remain the first live-integration batch. The six F-wave-two entries are queued behind them.

## Current work

F Assignment 003 targets Bakry--Emery/Bochner Gamma methods, two-scale coarse-graining, the Aldous/interchange spectral-gap reduction, Nash/spectral-profile smoothing with an IPS application, nonreversible coercivity with an IPS application, and conductance/Cheeger methods for spin chains; source-supported substitutions are allowed for the last three if necessary.

G Assignment 002 continues unchanged: dynamical disagreement domination, CFTP, clan-of-ancestors/perfect simulation, censoring, block/local/maximal coupling, and coalescing-walk voter duality.

Live integration is deferred until no student is actively committing a staging batch.
