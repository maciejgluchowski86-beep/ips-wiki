# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction. Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/006-first-live-integration-batch.md`.

## Publication target and wiki status

The live wiki is reopened for this toolbox section only. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

The first bounded live integration is complete:

- `docs/ergodicity-methods.md` is the hub;
- eighteen source-audited method pages are live under `docs/entries/`;
- `mkdocs.yml` has a top-level `Ergodicity methods` section grouped by proof interface.

All eighteen promoted pages carry `status: literature` and `audit: current`. Direct comparison with the pre-integration head `b810fd2` shows no pre-existing `docs/` page was modified: the public-layer change consists only of nineteen added pages and the navigation update.

## Workers

- Student F: idle after Assignment 003 and handoff `students/student-f/003-handoff.md` (`9c214623`).
- Student G: idle after Assignment 002 and handoff `students/student-g/handoff-002.md` (`7d5e739`).
- No new assignment is issued until the post-integration mechanical check is reported.

Every finished method entry is committed immediately as its own artifact. A rendering/session failure should cost at most the current unfinished entry.

## Inclusion and source standard

Include a method when it has a rigorous theorem/criterion/reusable proof architecture, a spin-system/IPS/KCSM/Glauber application or formulation, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete IPS/spin application. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Only `source_status: primary-checked` entries accepted in a Professor source-audit meeting are eligible for live promotion.

`validate_entries.py` checks metadata, headings, source-pinpoint/URL presence, and length only; it does not certify attribution or mathematical correctness. The voter-duality overclaim corrected at `1761b47` is the explicit reminder that validator success is structural only.

## Accepted inventory

Meetings 002--005 source-audited and accepted **30 staged entries**. The first 18 are now also live-wiki admitted. The twelve accepted in Meeting 005 remain staged:

### Coupling, graphical ancestry, and model-specific duality

- `clan-of-ancestors-perfect-simulation.md`;
- `censoring-monotone-glauber-dynamics.md`;
- `coupling-with-stationarity-local-uniformity.md`;
- `coupling-from-the-past.md`;
- `voter-coalescing-random-walk-duality.md`;
- `dynamical-disagreement-space-time-percolation.md`.

### Analytic, conservative, and slow-relaxation methods

- `bochner-bakry-emery-discrete-entropy.md`;
- `two-scale-coarse-graining-conservative-lsi.md`;
- `aldous-interchange-exclusion-gap.md`;
- `liggett-nash-polynomial-relaxation.md`;
- `kclg-renormalized-glauber-comparison.md`;
- `large-set-conductance-warm-start.md`.

The voter entry has no `uniqueness` target. The KCLG entry is the authorized substitution for the attempted nonreversible sector/hypocoercive slot.

## Mechanical status

The principal reran the pre-integration staging validator and reported:

```text
Checked 30 entries; 0 failed mechanical validation.
```

The required post-integration check is now:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Also mechanically confirm the eighteen promoted slugs, their `status: literature` / `audit: current` metadata, and that no pre-existing `docs/` entry changed relative to `b810fd2`.

## Next coverage after the integration check

High-priority uncovered families include literal block/maximal local coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, graphical finite-to-infinite transfer, Foster--Lyapunov/Harris recurrence, weak/super-Poincare and spectral-profile methods, dedicated finite-to-infinite coercivity transfer, additional KCSM comparison mechanisms, and model-specific branching/annihilating duals.
