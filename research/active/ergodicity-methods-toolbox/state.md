# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction. Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/005-g-wave-two-f-wave-three-source-audit-and-integration-gate.md`.

## Publication target and wiki status

The live wiki is reopened for this toolbox section only. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Research entries are staged under this workspace. Source-audited entries are promoted as ordinary `status: literature`, `audit: current` pages under a new top-level MkDocs section `Ergodicity methods`:

- `docs/ergodicity-methods.md` hub;
- `docs/entries/<method-slug>.md` concept pages;
- `mkdocs.yml` top-level navigation.

No live promotion has yet occurred. The next Professor action is a bounded integration pass for the first 18 accepted entries before another student wave is dispatched.

## Workers

- Student F: idle after Assignment 003 and handoff `students/student-f/003-handoff.md` (`9c214623`).
- Student G: idle after Assignment 002 and handoff `students/student-g/handoff-002.md` (`7d5e739`).
- No new assignment is issued until the first live integration pass is complete and mechanically checked.

Every finished method entry is committed immediately as its own artifact. A rendering/session failure should cost at most the current unfinished entry.

## Inclusion and source standard

Include a method when it has a rigorous theorem/criterion/reusable proof architecture, a spin-system/IPS/KCSM/Glauber application or formulation, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete IPS/spin application. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Only `source_status: primary-checked` entries accepted in a Professor source-audit meeting are eligible for live promotion.

`validate_entries.py` checks metadata, headings, source-pinpoint/URL presence, and length only; it does not certify attribution or mathematical correctness.

## Accepted inventory

Meetings 002--005 have source-audited and accepted **30 staged entries**.

The first 18 are the already-taxonomized live-integration batch. The twelve accepted in Meeting 005 are:

### Coupling, graphical ancestry, and model-specific duality

- `clan-of-ancestors-perfect-simulation.md`;
- `censoring-monotone-glauber-dynamics.md`;
- `coupling-with-stationarity-local-uniformity.md`;
- `coupling-from-the-past.md`;
- `voter-coalescing-random-walk-duality.md`;
- `dynamical-disagreement-space-time-percolation.md`.

The voter entry was corrected at `1761b47` to remove `targets: uniqueness`; its checked conclusions are clustering/convergence and coupling agreement, while the consensus states remain distinct invariant laws.

### Analytic, conservative, and slow-relaxation methods

- `bochner-bakry-emery-discrete-entropy.md`;
- `two-scale-coarse-graining-conservative-lsi.md`;
- `aldous-interchange-exclusion-gap.md`;
- `liggett-nash-polynomial-relaxation.md`;
- `kclg-renormalized-glauber-comparison.md`;
- `large-set-conductance-warm-start.md`.

The KCLG entry is the authorized substitution for the attempted nonreversible sector/hypocoercive slot; no clean primary IPS source was located in which that latter machinery itself proves the desired relaxation statement.

## Mechanical status

The principal's last validator run covered 28 entries and passed all 28. Two further F entries were already committed before Meeting 005 was composed. Rerun

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
```

on the current branch; the expected count is 30.

## Next coverage after integration

High-priority uncovered families include literal block/maximal local coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, graphical finite-to-infinite transfer, Foster--Lyapunov/Harris recurrence, weak/super-Poincare and spectral-profile methods, dedicated finite-to-infinite coercivity transfer, additional KCSM comparison mechanisms, and model-specific branching/annihilating duals.
