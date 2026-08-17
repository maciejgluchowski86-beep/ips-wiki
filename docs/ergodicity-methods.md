---
title: Ergodicity methods
status: literature
audit: current
tags:
  - ergodicity
  - mixing
  - spectral gap
---

# Ergodicity methods

This section is a toolbox of proof mechanisms used for spin systems, interacting particle systems, kinetically constrained models, and Glauber-type dynamics. It is organized by **proof interface**, not by a hierarchy of strength. The conclusions are not interchangeable: uniqueness of an invariant law, convergence from specified initial states, coupling agreement, a positive spectral gap, logarithmic Sobolev inequalities, and finite-volume total-variation mixing each require their own hypotheses.

The useful question for each page is: *what object must be controlled to make the argument go through?* Some methods are deliberately model-specific.

## Coupling and local influence

[Attractive monotone coupling](entries/attractive-monotone-coupling-extremal-laws.md) preserves the partial order and reduces uniqueness to equality of upper and lower invariant laws. [Dobrushin influence contraction](entries/dobrushin-influence-contraction.md) instead propagates a matrix of one-site conditional sensitivities, while [path coupling](entries/path-coupling-glauber-dynamics.md) asks only for contraction on neighboring configurations in a path metric.

These methods are closest when a single disagreement has a simple local evolution, but their inputs differ: stochastic order, influence matrices, and contractive local couplings are distinct structures.

## Spatial mixing and local-to-global transfer

[Disagreement percolation](entries/disagreement-percolation-gibbs-uniqueness.md) turns static boundary disagreements into a geometric percolation problem and yields Gibbs uniqueness when long disagreement paths die out. [Dobrushin--Shlosman spatial mixing](entries/dobrushin-shlosman-spatial-to-dynamical.md) uses strong uniform boundary screening to obtain volume-uniform functional inequalities and Glauber relaxation.

[Spectral independence](entries/spectral-independence-local-to-global.md) replaces worst-case influence sums by spectral control of conditional influence matrices and transfers linkwise expansion to the global Glauber chain. A different finite-to-large-scale route is the [finite-size strong-mixing criterion](entries/finite-size-strong-mixing-criterion.md): prove a sufficiently strong boundary-mixing estimate on one mesoscopic reference cube and bootstrap it by block decimation.

## Functional inequalities, comparison, and multiscale coercivity

The [Poincare/spectral-gap method](entries/poincare-spectral-gap.md) converts a static variance inequality into exponential \(L^2\) relaxation. [Logarithmic Sobolev and modified logarithmic Sobolev inequalities](entries/log-sobolev-modified-log-sobolev.md) strengthen this to hypercontractivity or entropy decay.

Several pages concern ways to *prove* those inequalities. [Canonical-path and Dirichlet-form comparison](entries/dirichlet-form-canonical-path-comparison.md) routes moves of a tractable reference chain through legal moves of the target chain. [Block dynamics and bisection](entries/block-dynamics-bisection-variance.md) recursively decomposes variance across overlapping regions. The [Lu--Yau martingale method](entries/lu-yau-martingale-conditional-variance.md) instead follows a filtration and controls conditional expectations under a conservation law. [Block factorization of entropy](entries/block-factorization-entropy.md) first proves entropy contraction for large updates and then reduces it to single-site factorization.

[Holley--Stroock bounded-perturbation transfer](entries/holley-stroock-bounded-perturbation.md) transports an existing Poincare or log-Sobolev inequality across a uniformly bounded change of density. For symmetric exclusion, the [moving-particle lemma](entries/moving-particle-long-jump-exclusion.md) replaces an illegal long exchange by the full local exclusion energy at an effective-resistance cost.

## Graphical ancestry and regeneration

[Finite-ancestor duality plus extinction](entries/duality-extinction-finite-ancestor-process.md) rewrites local memory as survival of a finite graphical dual. [Information percolation](entries/information-percolation-backward-histories.md) is more permissive: backward histories may survive, provided the clusters still carrying initial information are sparse enough to be hidden by equilibrium noise.

The [distinguished-zero method for the East model](entries/east-distinguished-zero-screening.md) is a model-specific regeneration mechanism. A moving vacancy creates an exact conditional-equilibrium region behind it, allowing equilibrium spectral information to be used in a nonequilibrium convergence proof.

## How to use the section

For a new model, first identify the natural object that carries memory: an ordered disagreement, an influence matrix, a boundary perturbation, a Dirichlet form, a finite ancestor set, or a regeneration interface. Then consult the corresponding page for the exact criterion, the mechanism that turns that criterion into relaxation, a representative IPS application, and the main failure modes. Failure of one criterion is generally failure of that method, not evidence of nonergodicity.
