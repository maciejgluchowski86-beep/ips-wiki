# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/008-second-live-integration-batch.md`.
- Student F: idle after Assignment 003.
- Student G: idle after Assignment 002.

## Coverage and publication status

Meetings 002--005 source-audited and accepted **30 method entries**. All thirty are now live under the dedicated `Ergodicity methods` wiki section.

The public layer consists of:

- `docs/ergodicity-methods.md` as the proof-interface hub;
- thirty `status: literature`, `audit: current` method pages under `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

The first eighteen pages passed their post-integration checks. The second batch added the remaining twelve pages and modified only the toolbox hub and navigation relative to pre-batch head `3e99b211`; no unrelated `docs/` page was changed in that integration.

The voter-duality page was corrected before promotion to remove an overstrong uniqueness target: clustering leaves the two consensus invariant laws distinct.

The repository-wide article layout is retained. Toolbox pages remain in `docs/entries/`; rendered separation from legacy review debt is supplied by the dedicated hub/navigation and `audit: current` metadata. No toolbox-specific filesystem reorganization is planned.

## Immediate check gate

Before another F/G literature wave is dispatched, run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Also confirm all thirty live slugs and current-audit metadata, all hub and MkDocs targets, the exact second-batch diff against `3e99b211`, and absence of modifications/deletions to non-toolbox `docs/` pages. This is structural publication checking only; source acceptance remains the Professor audit recorded in Meetings 002--005.

## Next uncovered families

After the check, priority gaps include literal block/maximal coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, Foster--Lyapunov/Harris recurrence, small-set/Nummelin regeneration, weak/super-Poincare and spectral-profile methods, finite-to-infinite graphical/coercive transfer, further KCSM comparison mechanisms, a dedicated full-Cheeger gap route with a spin application, and model-specific branching/annihilating duals.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
