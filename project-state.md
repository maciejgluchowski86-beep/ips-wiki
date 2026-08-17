# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or closely related relaxation statements in spin systems, IPS, KCSM, Glauber-type and adjacent interacting models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/011-wave-four-live-integration.md`.
- Student F: idle after Assignment 004.
- Student G: idle after Assignment 003.

## Coverage and publication status

There are now **44 source-audited staged entries and 44 live toolbox pages**. The first thirty passed two earlier integration checks. Meeting 010 accepted fourteen further wave-four entries after source/taxonomy corrections, and commit `84feb506` promoted all fourteen atomically.

The public layer consists of:

- `docs/ergodicity-methods.md` as the proof-interface hub;
- forty-four `status: literature`, `audit: current` method pages under `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

Relative to pre-integration audit head `8a167424`, commit `84feb506` adds exactly fourteen method pages and modifies only the hub and MkDocs navigation. No unrelated `docs/` page was changed in that integration commit.

The repository-wide article layout remains deliberate. Toolbox pages stay in `docs/entries/`; reader separation from legacy review debt is supplied by the dedicated hub/navigation and current-audit metadata.

## Wave-four audit notes

- Völlering's weak-Poincare entry had stale theorem numbering despite passing mechanical validation. It was corrected to Theorem 3.2, Corollary 3.3 and Proposition 4.7 at `fa48b2c` before promotion.
- Gobron--Saada refined discrepancy coupling is scoped to invariant-law classification, not bare uniqueness across conserved densities (`44e36ac`).
- Suzuki number-rigidity and potential-theoretic capacity were removed from the generic functional-inequality category (`d7865e0`, `6ce981f`).
- Sturm--Swart parity duality records invariant-law classification plus convergence, not unqualified uniqueness (`1f9f115`).
- The generic common/basic graphical-coupling page remains unwritten because the inspected literature did not expose a proof interface distinct from existing live pages.

`validate_entries.py` remains structural only and must not be described as mathematical or attribution verification.

## Immediate integration check

Before another student wave, run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

Expected structural result:

```text
Checked 44 entries; 0 failed mechanical validation.
```

Also verify all 44 staged slugs are live, hub links resolve and cover exactly the staged set, all 44 live pages have `status: literature` and `audit: current`, no non-toolbox legacy page was modified or deleted, and every MkDocs target resolves. The exact public batch diff is:

```bash
git diff --name-status 8a167424..84feb506 -- docs mkdocs.yml
```

## Remaining coverage

High-value gaps include spectral-profile/evolving-set methods with a genuinely load-bearing interacting-process application; full-Cheeger positive mixing/gap methods for a spin system distinct from canonical paths and large-set conductance; artificial Nummelin splitting in a concrete interacting process; super-Poincare methods distinct from current weak-Poincare/Nash entries; projective/compactness invariant-law arguments; further genuinely infinite-lattice Harris/Lyapunov mechanisms; and additional model-specific coupling, duality, KCSM, regeneration and finite-to-infinite interfaces as the primary literature exposes them.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
