# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent interacting Markov models.

Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/011-wave-four-live-integration.md`.

## Publication status

All **44** source-audited method entries are now represented in the live wiki:

- `docs/ergodicity-methods.md` is the proof-interface hub;
- all forty-four method pages are ordinary articles under `docs/entries/`;
- `mkdocs.yml` contains the dedicated top-level `Ergodicity methods` section;
- every toolbox method page carries `status: literature` and `audit: current` by construction.

The newest fourteen were promoted atomically at `84feb506`. Relative to pre-integration audit head `8a167424`, that commit adds exactly fourteen method pages and modifies only the toolbox hub and `mkdocs.yml`; no unrelated `docs/` page changed in the integration commit.

The repository-wide article layout is retained. Toolbox pages remain in `docs/entries/`; reader separation from legacy review debt is supplied by the dedicated hub/navigation and audit metadata.

## Wave-four audit corrections

Meeting 010 accepted all fourteen wave-four entries after source/taxonomy corrections:

- Völlering's weak-Poincare entry uses Theorem 3.2, Corollary 3.3 and Proposition 4.7, corrected at `fa48b2c`;
- Gobron--Saada now targets invariant-law classification rather than bare uniqueness, `44e36ac`;
- Suzuki number-rigidity and potential-theoretic capacity were moved out of the generic functional-inequality category, `d7865e0` and `6ce981f`;
- Sturm--Swart parity duality now records invariant-law classification plus convergence rather than unqualified uniqueness, `1f9f115`.

`validate_entries.py` checks structure only; these corrections again show why source/claim audit is separate.

## Workers

- Student F: idle after Assignment 004 and handoff `students/student-f/004-handoff.md` (`55d5e44`).
- Student G: idle after Assignment 003 and handoff `students/student-g/handoff-003.md` (`753f4eb`).
- No new assignment is issued until the wave-four live integration passes its structural check.

Every finished method entry in future waves must still be committed immediately as its own artifact. Students stage outside `docs/` and do not edit the live wiki directly.

## Current live coverage added in wave four

### Coupling, graphical, and duality

Block coupling by joint resampling; weighted Wasserstein contraction; refined non-diagonal discrepancy coupling; supercritical block construction; parity branching-annihilating duality.

### Recurrence and regeneration

Foster--Lyapunov plus Harris recurrence; literal particle-collapse regeneration; moving-front renewal/regeneration.

### Analytic and finite-to-infinite

Weak Poincare relaxation; finite-volume coercivity plus exhaustion; graphical finite-speed transfer; number-rigidity/tail-triviality Dirichlet ergodicity; KCSM constraint domination by a slower reference process.

### Adjacent relaxation

Potential-theoretic capacity for metastable Glauber crossover. This is explicitly not presented as a global mixing or positive-gap result.

## Required structural check

Run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Expected staging-validator result:

```text
Checked 44 entries; 0 failed mechanical validation.
```

Also check staged-versus-promoted completeness, hub link resolution and coverage, `status: literature` / `audit: current`, legacy safety, and every MkDocs target. Compare the integration itself with:

```bash
git diff --name-status 8a167424..84feb506 -- docs mkdocs.yml
```

## Remaining coverage

High-value gaps include a genuine spectral-profile/evolving-set interacting-process application; a full-Cheeger positive-gap/rapid-mixing spin application distinct from canonical paths and large-set conductance; artificial Nummelin splitting in a concrete interacting process; super-Poincare methods distinct from weak-Poincare/Nash; projective/compactness invariant-law arguments; further infinite-lattice Harris/Lyapunov mechanisms; and additional model-specific coupling, duality, KCSM, front, and finite-to-infinite interfaces when primary sources expose genuinely new proof mechanisms.
