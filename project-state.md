# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/006-first-live-integration-batch.md`.
- Student F: idle after Assignment 003.
- Student G: idle after Assignment 002.

## Coverage and publication status

Meetings 002--005 source-audited and accepted **30 staged method entries**. The principal's pre-integration structural check passed all thirty:

```text
Checked 30 entries; 0 failed mechanical validation.
```

The first **18** are now also admitted to the live wiki. `docs/ergodicity-methods.md` is the hub, the eighteen method pages are under `docs/entries/`, and `mkdocs.yml` contains the top-level `Ergodicity methods` navigation section. Every promoted page has `status: literature` and `audit: current`.

The remaining **12** accepted entries are still staged. They cover clan-of-ancestors perfect simulation, censoring, coupling with stationarity, CFTP, voter coalescing-walk duality, dynamical disagreement percolation, discrete Bochner entropy, two-scale conservative LSI, Aldous interchange/exclusion gap reduction, Liggett--Nash relaxation, KCLG renormalized Glauber comparison, and large-set conductance/warm-start mixing.

The voter-duality staging entry was corrected at `1761b47` to remove an overstrong `uniqueness` target; clustering does not remove the two consensus invariant laws.

## Immediate check gate

No new F or G assignment is issued until the first live-integration pass is mechanically checked. Run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Also confirm the eighteen promoted slugs and their live metadata, and that no pre-existing `docs/` entry changed relative to pre-integration branch head `b810fd2`. The Professor's direct repository comparison already shows only nineteen added public pages plus the `mkdocs.yml` navigation change.

## Wiki publication rule

The principal's instruction reopens the live wiki **for this toolbox section**. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited. Staging validation is structural only; source and claim scope are controlled by Professor source audit before promotion.

## Next uncovered families

After the integration check, priority gaps include literal block/maximal coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, Foster--Lyapunov/Harris recurrence, weak/super-Poincare and spectral-profile methods, finite-to-infinite graphical/coercive transfer, further KCSM comparison mechanisms, and model-specific branching/annihilating duals.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
