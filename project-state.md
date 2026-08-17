# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/005-g-wave-two-f-wave-three-source-audit-and-integration-gate.md`.
- Student F: idle after Assignment 003.
- Student G: idle after Assignment 002.

## Accepted staged coverage

Meetings 002--005 have source-audited and accepted **30 staged method entries**. The branch advanced beyond the principal's 28-entry validator snapshot: F completed Assignment 003 with two additional entries and a handoff before Meeting 005 was composed.

The newest accepted coverage includes:

- graphical/coupling: clan-of-ancestors perfect simulation, censoring, coupling with stationarity/local uniformity, CFTP, voter coalescing-walk duality, dynamical space-time disagreement percolation;
- analytic/conservative: discrete Bochner entropy, two-scale conservative LSI, Aldous interchange/exclusion gap reduction, Liggett--Nash polynomial relaxation, KCLG renormalized long-range Glauber comparison, and large-set conductance/warm-start mixing.

The voter-duality entry was corrected at `1761b47` to remove an overstrong `uniqueness` target; the recurrent voter model clusters but retains the two consensus invariant states.

The first 18 accepted entries are next in the bounded live-integration queue. The 12 accepted in Meeting 005 remain staged behind them.

## Immediate integration gate

No new F or G assignment is issued until the first live-wiki integration pass is completed and mechanically checked. This is a curation checkpoint, not a stop of the literature programme.

Before integration rerun:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
```

The expected current count is 30. Mechanical validation checks structure only; Professor source audit is separate.

## Wiki publication rule

The principal's instruction reopens the live wiki **for this toolbox section**. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Accepted material will be promoted to:

- `docs/ergodicity-methods.md` hub;
- one `status: literature`, `audit: current` method page under `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

No toolbox page has yet been promoted to `docs/`; the first 18-entry integration is the next Professor maintenance action.

## Next uncovered families

After integration, priority gaps include literal block/maximal coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, Foster--Lyapunov/Harris recurrence, weak/super-Poincare and spectral-profile methods, finite-to-infinite graphical/coercive transfer, further KCSM comparison mechanisms, and model-specific branching/annihilating duals.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
