# Group meeting 006: first live integration batch admitted

Date: 2026-08-17

The principal reran the pre-integration staging validator required by Meeting 005 and reported exactly:

```text
Checked 30 entries; 0 failed mechanical validation.
```

The principal also confirmed that immediately before this pass `docs/` and `mkdocs.yml` were byte-identical to `origin/main`. This mechanical result is not treated as source or mathematical verification; the source-audit rulings in Meetings 002--005 remain the admission basis.

`state_narrowed: yes`.

## Live integration ruling

The first eighteen source-audited entries are now admitted to the live wiki. The integration consists of:

- new hub `docs/ergodicity-methods.md`;
- eighteen new `docs/entries/<staged-slug>.md` pages;
- a new top-level `Ergodicity methods` navigation section in `mkdocs.yml`.

Every promoted entry has `status: literature` and `audit: current`. Staging-only front matter was removed from the public pages; the exact source pinpoints remain in the article bodies. The hub is organized by proof interface rather than by claimed strength of conclusion, and the integrated pages contain inline cross-links where neighboring methods need to be distinguished.

The live taxonomy in this first batch is:

1. coupling and local influence: attractiveness, Dobrushin influence contraction, path coupling;
2. spatial mixing and local-to-global transfer: static disagreement percolation, Dobrushin--Shlosman, spectral independence, finite-size strong-mixing bootstrap;
3. functional inequalities, comparison, and multiscale coercivity: Poincare, LSI/mLSI, canonical-path comparison, block bisection, Lu--Yau recursion, entropy factorization, Holley--Stroock perturbation, moving-particle comparison;
4. graphical ancestry and regeneration: finite-dual extinction, information percolation, East distinguished-zero screening.

The twelve entries accepted in Meeting 005 remain staged and are not yet in `docs/`.

## Scope check

A direct repository comparison from the pre-integration branch head `b810fd2` to the integrated head shows exactly twenty public-layer path changes: nineteen additions (`docs/ergodicity-methods.md` plus eighteen method pages) and one modification (`mkdocs.yml`). No pre-existing `docs/` page was modified. Thus the earlier freeze on unrelated legacy/deprecated IPS material remains intact.

## Required post-integration mechanical check

Before another literature wave is dispatched, the principal/orchestrator should check:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Expected staging-validator result remains `Checked 30 entries; 0 failed mechanical validation.` In addition, mechanically confirm:

- all eighteen promoted slugs exist under `docs/entries/`;
- each promoted page contains `status: literature` and `audit: current`;
- `docs/ergodicity-methods.md` is present and the `Ergodicity methods` MkDocs section resolves all nineteen links;
- no pre-existing `docs/` entry changed relative to the pre-integration head `b810fd2`.

The build/link check is the meaningful new mechanical test here. It can detect malformed navigation or broken relative links that `validate_entries.py` does not inspect.

## Current status

- 30 staged entries remain source-audited and accepted;
- first 18 are now also live-wiki admitted;
- 12 remain accepted staging material for a later integration batch;
- Student F idle;
- Student G idle;
- no next assignment is issued until the post-integration mechanical check is reported.
