# Group meeting 012: wave-four integration verified; breadth wave five opened

Date: 2026-08-17

The principal/orchestrator reports that the 44-page live integration from Meeting 011 passes every required structural publication check:

- `validate_entries.py`: `Checked 44 entries; 0 failed mechanical validation.`
- `mkdocs build --strict`: clean exit; the only non-INFO output is the upstream Material-for-MkDocs advisory banner.
- all 44 staged slugs have live counterparts;
- the hub links exactly those 44 pages and every link resolves;
- every toolbox page has `status: literature` and `audit: current`;
- relative to `origin/main`, the toolbox contribution under `docs/` is additions-only, with no legacy/deprecated page modified or deleted;
- every MkDocs navigation target resolves.

The two pre-existing INFO conditions reported by the build are unchanged legacy conditions and are not attributed to this programme.

`state_narrowed: yes`.

## Directory ruling

The directory question is closed. Toolbox concept pages remain in the repository-wide article namespace `docs/entries/`.

This is deliberate rather than provisional. `README.md` defines an article-first wiki in which ordinary concept pages live under `docs/entries/`. The toolbox is separated for readers by its dedicated hub, top-level navigation, cross-links, and `audit: current` metadata. Creating a toolbox-only subtree would introduce a second article namespace and path churn while leaving the legacy-review problem itself unsolved. If the repository later adopts a new filesystem taxonomy, that should be a wiki-wide migration applied consistently rather than a toolbox exception.

## Publication status

All 44 source-audited methods are live and mechanically verified. No additional publication gate remains open for waves one through four.

The structural validator remains structural only. The source/claim corrections recorded in Meetings 002--010 remain the substantive admission record.

## Wave-five direction

The next wave remains breadth-first but should now spend effort on proof interfaces not yet represented rather than variants of the dense basic-coupling/Poincare/LSI territory. Two complementary lanes are opened.

### Student F: analytic, KCM, recurrence, and limiting interfaces

Assignment 005 targets:

1. bootstrap-percolation closure/legal-path criteria that transfer deterministic emptying to KCM ergodicity or exponential relaxation;
2. long-range constrained Poincare/good-path inequalities used as a genuine relaxation engine;
3. Matryoshka-doll or comparable nested multiscale renormalisation where the nested event construction itself is the proof interface;
4. CBSEP/generalised-CBSEP auxiliary-process comparison for constrained dynamics, if the auxiliary branching/coalescing process is load-bearing rather than just a model definition;
5. artificial Nummelin splitting/manufactured-atom regeneration in a concrete interacting-process application, only if a clean primary source exists;
6. projective/compactness invariant-law arguments in an interacting system, with the compactness/consistency passage itself load-bearing;
7. super-Poincare relaxation with a distinct interacting-process application; if this again has no clean source, substitute a genuinely infinite-lattice Harris/Lyapunov mechanism or another uncovered analytic interface.

The first four KCM targets are deliberately method-specific. They should not be merged merely because they coexist in the same model literature; the checked primary proofs must decide whether each deserves a separate page.

### Student G: coupling, interfaces, duals, and graphical limits

Assignment 004 targets:

1. successful coupling of finite dual particle systems used to classify invariant measures or prove convergence;
2. second-class-particle or shock coupling as a long-time/invariant-law interface for conservative IPS;
3. literal maximal local coupling for a nonmonotone spin system, distinct from block resampling and path coupling;
4. regeneration of a disagreement or competition interface, distinct from the already-live physical reactive-front renewal page;
5. contact/multitype/block-construction complete convergence or restart arguments whose proof interface is distinct from Sturm--Swart parity duality;
6. boundary-uniform projective graphical transfer from finite-volume coupling estimates to infinite-volume uniqueness/convergence;
7. a nonmonotone Wasserstein/reflection/jump coupling for an infinite interacting system, distinct from the existing weighted synchronous-contraction page.

## Anti-padding rule

The negative taxonomy findings from prior waves remain binding. A target name is not evidence that a distinct method exists. If the inspected primary literature collapses a target into an existing live interface, or only supplies generic Markov-chain theory without a concrete interacting-process application, the student records the negative result and substitutes another uncovered source-supported method.

The generic basic/common graphical-coupling page remains unwarranted unless new primary evidence materially changes the previous ruling. Likewise, F should not repeat the generic nonreversible sector/hypocoercive search merely to fill a slot.

## Durability and admission

Each finished entry is committed immediately as its own substantive commit. Both students stage under `research/active/ergodicity-methods-toolbox/entries/`, do not edit `docs/` or `mkdocs.yml`, and finish with durable handoff files. The Professor source-audits each handoff before any further assignment or live promotion.
