# IPS Wiki

This is a public-facing mathematical wiki for interacting particle systems, spin systems, ergodicity, duality, branching representations for nonlinear PDEs, and related research.

Each article is a separate page with rendered TeX math and ordinary links to neighboring entries. The source files are Markdown under `docs/`.

For the patch theory, the canonical source is the repository manuscript *Patch representations and convergence for facilitated spin systems*. The wiki pages below present that paper's current definitions and proved results; older development-stage conditional warnings have been removed.

## Core entries

A minimal dependency order is:

1. [Lattice and graph](entries/lattice-and-graph.md)
2. [Polynomial-growth lattice](entries/polynomial-growth-lattice.md)
3. [Local functions](entries/local-functions.md)
4. [Monomials](entries/monomials.md)
5. [Bernoulli product measure](entries/bernoulli-product-measure.md)
6. [Interacting particle system](entries/interacting-particle-system.md)
7. [Spin system](entries/spin-system.md)
8. [Pure noise spin system](entries/pure-noise-spin-system.md)
9. [Oriented spin system](entries/oriented-spin-system.md)
10. [Invariant measure](entries/invariant-measure.md)
11. [Ergodicity](entries/ergodicity.md)

## Duality entries

1. [Duality](entries/duality.md)
2. [Monomial Feynman-Kac duality for spin systems](entries/monomial-duality-for-spin-systems.md)
3. [Duality noise lemma](entries/duality-noise-lemma.md)

## Signed additive set processes

1. [Signed additive set process](entries/signed-additive-set-process.md)
2. [Graphical construction of signed additive set process](entries/graphical-construction-of-signed-additive-set-process.md)
3. [Successful interaction](entries/successful-interaction.md)

## Patches

1. [Patch](entries/patch.md)
2. [Interaction cone](entries/interaction-cone.md)
3. [Consistent patch law](entries/patch-consistency-event.md)
4. [Patch factorization](entries/patch-factorization.md)
5. [Patch contribution](entries/patch-contribution.md)
6. [Patch positivity property](entries/patch-positivity-property.md)
7. [Patch threshold profile](entries/patch-critical-density.md)
8. [Centered-moment order and cones](entries/high-density-measure.md)
9. [Patch representation of spin systems](entries/patch-representation-of-spin-systems.md)
10. [Centered-moment order preservation](entries/monomial-monotonicity-for-high-density-measures.md)
11. [Pure-death comparison under patch positivity](entries/pure-death-comparison-under-patch-positivity.md)
12. [Spatial confinement of patch weights](entries/undoing-duality-under-confined-interactions.md)
13. [Finite propagation for zero-boundary restrictions](entries/finite-propagation-for-zero-boundary-restrictions.md)
14. [Late interactions and no-late relaxation](entries/exponential-relaxation-under-confined-late-interactions.md)
15. [Common invariant limit under uniform pure deaths](entries/common-invariant-limit-under-uniform-pure-deaths.md)

## KCSM entries

The KCSM block uses the standard convention that `0` is the facilitating state. The vacancy density is $q$, and $p=1-q$ is the density of occupied sites.

1. [Bernoulli refresh operator](entries/bernoulli-refresh-operator.md)
2. [Update family](entries/update-family.md)
3. [Kinetically constrained spin model](entries/kinetically-constrained-spin-model.md)
4. [Soft KCSM](entries/soft-kcsm.md)
5. [Legal update](entries/legal-update.md)
6. [FA-1f model](entries/fa-1f-model.md)
7. [East model](entries/east-model.md)
8. [Biased annihilating branching process](entries/babp-model.md)
9. [KCSM relaxation and mixing](entries/kcsm-relaxation-and-mixing.md)
10. [KCSM out of equilibrium](entries/kcsm-out-of-equilibrium.md)
11. [FA-1f out of equilibrium](entries/fa-1f-out-of-equilibrium.md)
12. [East out of equilibrium](entries/east-out-of-equilibrium.md)
13. [BABP out of equilibrium](entries/babp-out-of-equilibrium.md)

## PDE and branching representations

Start with [Probabilistic representations for nonlinear PDEs](pde-branching-representations.md), then follow the [PDE reading path](pde-reading-path.md). The terminated quadratic-Hessian theorem chain is not part of the live research path. The surviving material is limited to audited reusable finite or analytic mechanisms and observations; it does not supply an active quadratic-Hessian representation theorem.

## Meta pages

- [Notation](meta/notation.md)
- [Style decisions](meta/style-decisions.md)
- [Wiki quality and pruning](meta/wiki-quality-and-pruning.md)
- [Entry template](meta/entry-template.md)
- [References](meta/references.md)

## Public-content rule

This repository is intended to be safe for public viewing. Entries should contain definitions, standard facts, cited literature summaries, and carefully labeled project-level concepts. Private research strategy, raw scratch work, credentials, personal information, and unpublished claims stated without proof status do not belong here.
