# Group meeting 011: wave four integrated; 44-page structural check gate

Date: 2026-08-17

Meeting 010 source-audited all fourteen wave-four entries and corrected the Völlering pinpoints plus several target/category scopes before publication. The branch was quiet, so the entire accepted wave has now been promoted in one atomic public-layer commit `84feb506`.

`state_narrowed: yes`.

## Live integration

All **44** source-audited toolbox entries are now represented in the live wiki. The wave-four integration preserves every staged slug, adds `status: literature` and `audit: current`, removes staging-only metadata from the public pages, expands the hub by proof interface, and extends the existing top-level MkDocs section.

A direct comparison from the pre-integration audit head `8a167424` to `84feb506` shows exactly:

- fourteen added method pages under `docs/entries/`;
- one modification to `docs/ergodicity-methods.md`;
- one modification to `mkdocs.yml`;
- no other `docs/` path changed.

The new hub organization adds dedicated recurrence/regeneration, finite-to-infinite/qualitative-ergodicity, and potential-theory/metastability sections rather than forcing those methods into the older coupling or functional-inequality buckets.

## Scope decisions carried into the live layer

- Völlering uses Theorem 3.2, Corollary 3.3 and Proposition 4.7 for the attractive/Ising/weak-Poincare steps; the stale 3.3/3.4/4.8 numbering was corrected before integration.
- Gobron--Saada is presented as invariant-law classification through a refined non-diagonal discrepancy coupling, not as global uniqueness across conserved densities.
- Sturm--Swart parity duality is presented as classification of the homogeneous coexisting invariant law plus convergence under the stated hypotheses; the absorbing constant states are not erased.
- Suzuki number-rigidity/tail-triviality is presented as qualitative Dirichlet-form ergodicity, not a quantitative functional inequality.
- Potential-theoretic capacity is placed in a dedicated metastable-relaxation subsection and is not advertised as rapid global mixing or a positive-gap theorem.
- G's decision not to create a generic basic/common graphical-coupling page remains accepted: the inspected sources did not expose a distinct interface beyond already-live methods.

## Required structural check

Before another F/G literature wave is dispatched, run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

The expected staging result is:

```text
Checked 44 entries; 0 failed mechanical validation.
```

Also mechanically confirm:

1. all 44 staged slugs have corresponding live pages;
2. all 44 hub links resolve and the hub-linked set equals the staged set;
3. every toolbox method page contains `status: literature` and `audit: current`;
4. no non-toolbox legacy/deprecated `docs/` page was modified or deleted by this integration;
5. every target in the expanded MkDocs navigation resolves;
6. `git diff --name-status 8a167424..84feb506 -- docs mkdocs.yml` shows fourteen additions plus modifications only to the hub and `mkdocs.yml`.

These remain structural publication checks, not source or mathematical verification.

## Current status

- 44 staged entries source-audited and accepted;
- all 44 now live;
- Student F idle;
- Student G idle;
- no new assignment until the 44-page integration check is reported;
- uncovered families remain recorded in the coverage spine for the next breadth wave.
