# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction, not a continuation of the positive-rates proof loop. Breadth is intentional: model-specific methods are in scope.

Latest meeting: `meetings/003-g-wave-one-source-audit-and-joint-taxonomy.md`.

## Publication target and wiki status

The principal's new instruction explicitly reopens the live wiki **for this toolbox section only**. The previous freeze remains in force for unrelated legacy/deprecated IPS pages unless a separate current audit is requested.

Research drafts are staged under this workspace. Entries accepted by Professor source audit are later promoted to ordinary audited literature entries under a new top-level MkDocs section `Ergodicity methods`:

- `docs/ergodicity-methods.md` — compact toolbox map;
- `docs/entries/<method-slug>.md` — one concept page per method;
- `mkdocs.yml` — top-level `Ergodicity methods` navigation.

All twelve first-wave entries are now mathematically and taxonomically cleared for promotion. Promotion is deferred only to the next quiet integration window while both students are actively committing wave-two staging files.

## Workers and current assignments

Student F and Student G are reused. Repository/project claims are not literature authority; every entry must be grounded in actual external sources.

- Student F: active on `students/student-f/assignment-002.md` — Lu--Yau/martingale recursion, spectral independence, block/approximate entropy factorization, bounded perturbation, moving-particle comparison, finite-size relaxation criteria.
- Student G: active on `students/student-g/assignment-002.md` — dynamical disagreement domination, coupling from the past, clan-of-ancestors perfect simulation, censoring, block/local/maximal coupling, coalescing-walk voter duality.

At most two sessions remain in flight.

## Durability rule

Every finished method entry is committed immediately as its own durable artifact. Do not batch a survey into one final response. A session freeze should cost at most the current unfinished entry.

## Inclusion and source standard

Include a method when:

1. there is a rigorous theorem, criterion, or reusable proof architecture in the literature;
2. it proves or is explicitly used to prove ergodicity/uniqueness, convergence, coupling agreement/coalescence, spectral gap/Poincare, LSI/mLSI, quantitative mixing, or equivalent forgetting/extinction;
3. it has a spin-system/IPS/KCSM/Glauber-type application or is formulated for such models;
4. hypotheses, mechanism, conclusion, and limitations can be stated self-containedly;
5. at least one primary source has been inspected and pinpointed.

General Markov-chain methods require a concrete IPS/spin application. Model-specific techniques are explicitly welcome. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one inspected primary source with exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Only entries marked `source_status: primary-checked` and accepted in a Professor source-audit meeting are eligible for live promotion.

## Entry size and mechanical checking

Staged entries use `entry-template.md`. Target length is 400–900 words; hard ceiling 1200 words excluding front matter and references. Each entry contains a mathematical criterion/theorem-level statement.

`validate_entries.py` checks required metadata, headings, source pinpoints/URLs, and length. Passing it certifies structure only, not mathematical correctness or attribution.

## Accepted first-wave entries

Meetings 002--003 source-audited and accepted twelve staged entries. The joint taxonomy is by load-bearing proof interface.

### A. Coupling and local influence

- `attractive-monotone-coupling-extremal-laws.md`;
- `dobrushin-influence-contraction.md`;
- `path-coupling-glauber-dynamics.md`.

### B. Spatial mixing and boundary influence

- `disagreement-percolation-gibbs-uniqueness.md`;
- `dobrushin-shlosman-spatial-to-dynamical.md`.

### C. Functional inequalities and comparison

- `poincare-spectral-gap.md`;
- `log-sobolev-modified-log-sobolev.md`;
- `dirichlet-form-canonical-path-comparison.md`;
- `block-dynamics-bisection-variance.md`.

### D. Graphical ancestry, duality, and regeneration

- `duality-extinction-finite-ancestor-process.md`;
- `information-percolation-backward-histories.md`;
- `east-distinguished-zero-screening.md`.

Shared primary sources do not imply duplicate entries when the proof interfaces differ. Meeting 003 records the required cross-links and deduplication rules for promotion.

## Current work

- F Assignment 002 active.
- G Assignment 002 active.
- Twelve first-wave entries accepted and queued for the next quiet live-wiki integration window.
