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

This section is a toolbox of proof mechanisms used for spin systems, interacting particle systems, kinetically constrained models, and Glauber-type dynamics. It is organized by **proof interface**, not by a hierarchy of strength. The conclusions are not interchangeable: uniqueness of an invariant law, convergence from specified initial states, coupling agreement, a positive spectral gap, logarithmic Sobolev inequalities, exact sampling, and finite-volume total-variation mixing each require their own hypotheses.

The useful question for each page is: *what object must be controlled to make the argument go through?* Some methods are deliberately model-specific.

## Coupling and local influence

[Attractive monotone coupling](entries/attractive-monotone-coupling-extremal-laws.md) preserves the partial order and reduces uniqueness to equality of upper and lower invariant laws. [Dobrushin influence contraction](entries/dobrushin-influence-contraction.md) propagates a matrix of one-site conditional sensitivities, while [path coupling](entries/path-coupling-glauber-dynamics.md) asks only for contraction on neighboring configurations in a path metric.

[Coupling with stationarity](entries/coupling-with-stationarity-local-uniformity.md) relaxes worst-case contraction by requiring it only when one copy lies in a high-probability equilibrium set. [Censoring inequalities](entries/censoring-monotone-glauber-dynamics.md) do something different again: for ordered starts in a monotone system, deleting updates can only delay mixing, so a structured update schedule may be analyzed and transferred back to the real chain.

[Dynamical disagreement percolation](entries/dynamical-disagreement-space-time-percolation.md) encodes the actual spread of coupled discrepancies by oriented space-time connectivity. This is a dynamical coupling method and should not be confused with the static Gibbs uniqueness method below.

## Spatial mixing and local-to-global transfer

[Disagreement percolation](entries/disagreement-percolation-gibbs-uniqueness.md) turns static boundary disagreements into a geometric percolation problem and yields Gibbs uniqueness when long disagreement paths die out. [Dobrushin--Shlosman spatial mixing](entries/dobrushin-shlosman-spatial-to-dynamical.md) uses strong uniform boundary screening to obtain volume-uniform functional inequalities and Glauber relaxation.

[Spectral independence](entries/spectral-independence-local-to-global.md) replaces worst-case influence sums by spectral control of conditional influence matrices and transfers linkwise expansion to the global Glauber chain. A different finite-to-large-scale route is the [finite-size strong-mixing criterion](entries/finite-size-strong-mixing-criterion.md): prove a sufficiently strong boundary-mixing estimate on one mesoscopic reference cube and bootstrap it by block decimation.

## Functional inequalities, comparison, and multiscale coercivity

The [Poincare/spectral-gap method](entries/poincare-spectral-gap.md) converts a static variance inequality into exponential \(L^2\) relaxation. [Logarithmic Sobolev and modified logarithmic Sobolev inequalities](entries/log-sobolev-modified-log-sobolev.md) strengthen this to hypercontractivity or entropy decay. The [discrete Bochner--Bakry--Emery method](entries/bochner-bakry-emery-discrete-entropy.md) is one way to prove entropy coercivity by controlling the second entropy derivative through the algebra of jump moves.

Several pages concern recursive or comparative ways to prove coercive inequalities. [Canonical-path and Dirichlet-form comparison](entries/dirichlet-form-canonical-path-comparison.md) routes moves of a tractable reference chain through legal moves of the target chain. [Block dynamics and bisection](entries/block-dynamics-bisection-variance.md) recursively decomposes variance across overlapping regions. The [Lu--Yau martingale method](entries/lu-yau-martingale-conditional-variance.md) follows a filtration and controls conditional expectations under a conservation law, while [two-scale coarse graining](entries/two-scale-coarse-graining-conservative-lsi.md) separates microscopic fibers from a coarse marginal and lifts coercivity back from a renormalized scale. [Block factorization of entropy](entries/block-factorization-entropy.md) first proves entropy contraction for large updates and then reduces it to single-site factorization.

[Holley--Stroock bounded-perturbation transfer](entries/holley-stroock-bounded-perturbation.md) transports an existing Poincare or log-Sobolev inequality across a uniformly bounded change of density. For symmetric exclusion, the [moving-particle lemma](entries/moving-particle-long-jump-exclusion.md) replaces an illegal long exchange by the full local exclusion energy at an effective-resistance cost, while the [Aldous interchange-process theorem](entries/aldous-interchange-exclusion-gap.md) gives an exact reduction of the many-particle spectral gap to the one-particle random-walk gap.

When a positive gap is false, a [Liggett--Nash inequality](entries/liggett-nash-polynomial-relaxation.md) can still convert energy dissipation plus a stronger seminorm into polynomial relaxation. [Large-set conductance](entries/large-set-conductance-warm-start.md) is an isoperimetric analogue adapted to warm starts: weak expansion of non-negligible sets can yield polynomial total-variation mixing even when tiny traps rule out a useful uniform gap.

The [Kob--Andersen renormalized Glauber comparison](entries/kclg-renormalized-glauber-comparison.md) is deliberately model-specific. It first manufactures a high-probability good-block process with useful coercivity, then compares auxiliary long-range refreshes back to legal conservative KCLG moves.

## Graphical ancestry, duality, and exact sampling

[Finite-ancestor duality plus extinction](entries/duality-extinction-finite-ancestor-process.md) rewrites local memory as survival of a finite graphical dual. [Coalescing-random-walk duality](entries/voter-coalescing-random-walk-duality.md) is different: voter ancestors need not die; their information content decreases when ancestral walks merge.

[Coupling from the past](entries/coupling-from-the-past.md) seeks backward coalescence of a common random map and produces an exact stationary sample. [Clan-of-ancestors perfect simulation](entries/clan-of-ancestors-perfect-simulation.md) instead proves that only a finite backward dependency graph is needed to reconstruct the target. [Information percolation](entries/information-percolation-backward-histories.md) is weaker still: backward histories may survive, provided the clusters carrying initial information are sparse enough to be hidden by equilibrium noise.

The [distinguished-zero method for the East model](entries/east-distinguished-zero-screening.md) is a model-specific regeneration mechanism. A moving vacancy creates an exact conditional-equilibrium region behind it, allowing equilibrium spectral information to be used in a nonequilibrium convergence proof.

## How to use the section

For a new model, first identify the object that carries memory or obstructs coercivity: an ordered disagreement, an influence matrix, a space-time dependency path, a boundary perturbation, a Dirichlet form, a finite ancestor set, a conserved slow mode, or a regeneration interface. Then consult the corresponding page for the exact criterion, the mechanism that turns that criterion into relaxation, a representative IPS application, and the main failure modes. Failure of one criterion is generally failure of that method, not evidence of nonergodicity.
