# Group meeting 008: second live integration batch admitted

Date: 2026-08-17

Meeting 007 recorded the clean post-integration check for the first eighteen pages and opened the second live batch. The remaining twelve source-audited entries from Meeting 005 have now been promoted.

`state_narrowed: yes`.

## Live status

All **30** source-audited toolbox entries are now represented in the live wiki. The second batch adds exactly twelve new method pages and modifies only the toolbox hub and `mkdocs.yml` navigation relative to the pre-batch head `3e99b211`.

The direct repository comparison shows:

- 12 added files under `docs/entries/`;
- `docs/ergodicity-methods.md` modified to integrate the new methods by proof interface;
- `mkdocs.yml` modified to expose the new pages in the existing top-level `Ergodicity methods` section;
- no other `docs/` path changed.

Every new page has `status: literature` and `audit: current`. Staged slugs were preserved exactly.

## Taxonomy additions

### Coupling and local influence

Added coupling with stationarity/local uniformity, censoring inequalities, and dynamical disagreement domination by space-time percolation.

### Functional inequalities and coercivity

Added discrete Bochner--Bakry--Emery entropy coercivity, two-scale conservative coarse graining, Aldous interchange/exclusion spectral-gap reduction, Liggett--Nash polynomial relaxation, large-set conductance/warm-start mixing, and the model-specific Kob--Andersen renormalized Glauber comparison.

### Graphical ancestry, duality, and exact sampling

Added voter coalescing-walk duality, coupling from the past, and clan-of-ancestors perfect simulation. The hub keeps these distinct from information percolation and finite-dual extinction.

## Directory ruling retained

All toolbox concept pages remain in the repository-wide `docs/entries/` namespace. Separation from legacy material is rendered through the dedicated hub, top-level navigation, and current-audit metadata rather than a toolbox-specific filesystem convention. No legacy/deprecated page was touched.

## Required post-second-batch check

Before another literature wave is dispatched, run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

and mechanically confirm:

1. all thirty staged slugs have corresponding live pages;
2. every toolbox method page has `status: literature` and `audit: current`;
3. all links from `docs/ergodicity-methods.md` and all targets in the `Ergodicity methods` MkDocs section resolve;
4. `git diff --name-status 3e99b211..HEAD -- docs mkdocs.yml` shows exactly twelve added method pages plus modifications to the hub and `mkdocs.yml`;
5. no pre-existing non-toolbox `docs/` page was modified or deleted.

This remains structural publication checking, not mathematical or source verification.

## Current worker status

- Student F idle.
- Student G idle.
- No new assignment issued until the second integration check is reported.

After that checkpoint, the next wave should target uncovered proof interfaces rather than add variants of already dense coupling/LSI material.
