# Group meeting 007: first integration verified; second live batch opens

Date: 2026-08-17

The principal/orchestrator completed the post-integration checks required by Meeting 006. All eighteen hub links resolve, all eighteen promoted pages carry `status: literature` and `audit: current`, all live slugs match their staged slugs, the `Ergodicity methods` MkDocs navigation resolves, and the public-layer diff against `origin/main` modifies no pre-existing `docs/` page. The earlier concern about broken hub links referred only to the intermediate hub-only commit `c167f72`; the completed integration at `d92e2e3` is clean.

`state_narrowed: yes`.

## 1. Mechanical-validation scope

The thirty-entry staging validator remains a structural test only. Its successful run does not certify mathematical scope or source attribution. The voter-duality overclaim removed at `1761b47` remains the canonical example: a mechanically valid `targets` field can still contain a false conclusion. Professor source audit remains the substantive admission gate.

## 2. Directory-layout ruling

Keep the toolbox pages in the existing article directory `docs/entries/`; do **not** create a separate physical subdirectory such as `docs/ergodicity-methods/`.

This is deliberate for three reasons.

1. The repository's public convention is article-first: ordinary concept pages live in one `docs/entries/` namespace and are organized for readers by hub pages, inline links, and MkDocs navigation.
2. The new toolbox is already clearly separated in the rendered site by its top-level `Ergodicity methods` navigation section, its dedicated hub, and `status: literature` / `audit: current` metadata.
3. Moving only the new pages into a special filesystem namespace would add path churn and a second convention without improving the rendered reading structure. If the repository ever changes its article-directory convention, that should be a global wiki-curation decision rather than a toolbox-specific exception.

The frozen legacy/deprecated IPS material therefore remains untouched. Co-location in `docs/entries/` is not treated as endorsement or audit equivalence.

## 3. Second live integration batch

The remaining twelve entries accepted in Meeting 005 are cleared for live promotion now that the first batch has passed its post-integration check:

### Coupling, graphical ancestry, and exact sampling

- `coupling-with-stationarity-local-uniformity.md`;
- `censoring-monotone-glauber-dynamics.md`;
- `dynamical-disagreement-space-time-percolation.md`;
- `coupling-from-the-past.md`;
- `clan-of-ancestors-perfect-simulation.md`;
- `voter-coalescing-random-walk-duality.md`.

### Functional inequalities, conservative systems, and slow relaxation

- `bochner-bakry-emery-discrete-entropy.md`;
- `two-scale-coarse-graining-conservative-lsi.md`;
- `aldous-interchange-exclusion-gap.md`;
- `liggett-nash-polynomial-relaxation.md`;
- `large-set-conductance-warm-start.md`;
- `kclg-renormalized-glauber-comparison.md`.

The voter page is promoted only in its corrected form, without a uniqueness target. The KCLG page remains a model-specific renormalization/comparison architecture, not a generic nonreversible-sector theorem.

## 4. Publication plan

Promote the twelve pages with `status: literature` and `audit: current`, extend `docs/ergodicity-methods.md`, and expand the existing top-level MkDocs taxonomy. Preserve staged slugs exactly. No unrelated `docs/` page is to be edited.

The hub should preserve proof-interface distinctions rather than merely append a flat list. In particular:

- CFTP, clan-of-ancestors perfect simulation, and information percolation remain separate;
- static and dynamical disagreement percolation remain separate;
- Bochner is a method for proving entropy coercivity, not another name for mLSI;
- Aldous' equality is an exact spectral reduction, not canonical-path comparison;
- large-set conductance is a warm-start polynomial-mixing method, not a positive-Cheeger-constant claim;
- KCLG renormalized comparison is kept visibly model-specific.

## 5. Post-second-batch check

After promotion, rerun the same checks as for the first batch:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

and mechanically confirm:

- all thirty promoted slugs exist under `docs/entries/`;
- every toolbox method page has `status: literature` and `audit: current`;
- every hub and MkDocs target resolves;
- the second-batch diff adds exactly twelve method pages plus the intended hub/navigation edits;
- no pre-existing non-toolbox `docs/` page is modified or deleted.

No new F/G literature assignment is issued until this second integration check is reported. After that checkpoint the next wave should return to uncovered interfaces rather than densifying already well-covered families.
