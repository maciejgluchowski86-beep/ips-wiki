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

This section is a toolbox of proof mechanisms used for spin systems, interacting particle systems, kinetically constrained models, Glauber-type dynamics, and closely related interacting Markov systems. It is organized by **proof interface**, not by a hierarchy of strength. The conclusions are not interchangeable: uniqueness of an invariant law, convergence from specified initial states, coupling agreement, a positive spectral gap, logarithmic Sobolev inequalities, exact sampling, metastable crossover estimates, and finite-volume total-variation mixing each require their own hypotheses.

The useful question for each page is: *what object must be controlled to make the argument go through?* Some methods are deliberately model-specific.

## Coupling and local influence

[Attractive monotone coupling](entries/attractive-monotone-coupling-extremal-laws.md) preserves the partial order and reduces uniqueness to equality of upper and lower invariant laws. [Dobrushin influence contraction](entries/dobrushin-influence-contraction.md) propagates a matrix of one-site conditional sensitivities, while [path coupling](entries/path-coupling-glauber-dynamics.md) asks only for contraction on neighboring configurations in a path metric.

[Coupling with stationarity](entries/coupling-with-stationarity-local-uniformity.md) requires contraction only when one copy lies in a high-probability equilibrium set. [Block coupling](entries/block-coupling-joint-resampling.md) instead enlarges the update itself and couples whole conditional block laws. [Weighted Wasserstein contraction](entries/weighted-wasserstein-contraction-infinite-ips.md) adapts the metric to a countable-site continuous-spin system and closes a global transportation contraction from dissipative drift.

[Refined discrepancy coupling](entries/refined-discrepancy-coupling-general-exclusion.md) treats the coupled transition rates themselves as variables, allowing different microscopic exclusion jumps in the two marginals when ordinary basic coupling is not attractive. [Censoring inequalities](entries/censoring-monotone-glauber-dynamics.md) show that, for ordered starts in a monotone system, deleting updates can only delay mixing. [Dynamical disagreement percolation](entries/dynamical-disagreement-space-time-percolation.md) encodes the actual spread of coupled discrepancies by oriented space-time connectivity.

## Spatial mixing and local-to-global transfer

[Disagreement percolation](entries/disagreement-percolation-gibbs-uniqueness.md) turns static boundary disagreements into a geometric percolation problem and yields Gibbs uniqueness when long disagreement paths die out. [Dobrushin--Shlosman spatial mixing](entries/dobrushin-shlosman-spatial-to-dynamical.md) uses strong uniform boundary screening to obtain volume-uniform functional inequalities and Glauber relaxation.

[Spectral independence](entries/spectral-independence-local-to-global.md) replaces worst-case influence sums by spectral control of conditional influence matrices and transfers linkwise expansion to the global Glauber chain. A different finite-to-large-scale route is the [finite-size strong-mixing criterion](entries/finite-size-strong-mixing-criterion.md): prove a sufficiently strong boundary-mixing estimate on one mesoscopic reference cube and bootstrap it by block decimation.

## Functional inequalities, comparison, and multiscale coercivity

The [Poincare/spectral-gap method](entries/poincare-spectral-gap.md) converts a static variance inequality into exponential \(L^2\) relaxation. [Logarithmic Sobolev and modified logarithmic Sobolev inequalities](entries/log-sobolev-modified-log-sobolev.md) strengthen this to hypercontractivity or entropy decay. The [discrete Bochner--Bakry--Emery method](entries/bochner-bakry-emery-discrete-entropy.md) proves entropy coercivity by controlling the second entropy derivative through the algebra of jump moves.

Several pages concern recursive or comparative ways to prove coercive inequalities. [Canonical-path and Dirichlet-form comparison](entries/dirichlet-form-canonical-path-comparison.md) routes moves of a tractable reference chain through legal moves of the target chain. [Block dynamics and bisection](entries/block-dynamics-bisection-variance.md) recursively decomposes variance across overlapping regions. The [Lu--Yau martingale method](entries/lu-yau-martingale-conditional-variance.md) follows a filtration under a conservation law, while [two-scale coarse graining](entries/two-scale-coarse-graining-conservative-lsi.md) separates microscopic fibers from a coarse marginal. [Block factorization of entropy](entries/block-factorization-entropy.md) proves entropy contraction for large updates and then reduces it to single-site factorization.

[Holley--Stroock bounded-perturbation transfer](entries/holley-stroock-bounded-perturbation.md) transports an existing Poincare or log-Sobolev inequality across a bounded density perturbation. For symmetric exclusion, the [moving-particle lemma](entries/moving-particle-long-jump-exclusion.md) replaces an illegal long exchange by local exclusion energy at an effective-resistance cost, while the [Aldous interchange-process theorem](entries/aldous-interchange-exclusion-gap.md) exactly reduces the many-particle spectral gap to the one-particle random-walk gap.

When a positive gap is not the right object, a [Liggett--Nash inequality](entries/liggett-nash-polynomial-relaxation.md) can yield polynomial relaxation, while a [weak Poincare inequality](entries/weak-poincare-glauber-relaxation.md) encodes nonuniform one-spin influence tails into subexponential relaxation. [Large-set conductance](entries/large-set-conductance-warm-start.md) is an isoperimetric route adapted to warm starts.

Two KCSM/KCLG comparison mechanisms are deliberately kept separate. The [Kob--Andersen renormalized Glauber comparison](entries/kclg-renormalized-glauber-comparison.md) manufactures a mesoscopic good-block auxiliary process before comparison. [Constraint domination](entries/kcsm-constraint-domination-reference-process.md) simply deletes legal moves until a slower oriented reference process remains, then imports its spectral gap by Dirichlet-form monotonicity.

## Recurrence and regeneration

[Foster--Lyapunov drift plus Harris recurrence](entries/foster-lyapunov-harris-geometric-ergodicity.md) combines return toward a controlled region with small-set minorization to obtain weighted-total-variation contraction. [Regeneration at a particle-collapse atom](entries/particle-collapse-regeneration.md) uses an actual recurrent atom and finite-mean iid renewal cycles instead. [Front regeneration](entries/front-regeneration-renewal-times.md) constructs fresh-start times for a moving interface and uses renewal theory to obtain convergence in the front frame.

## Finite-to-infinite transfer and qualitative ergodicity

[Finite-volume coercivity plus semigroup exhaustion](entries/finite-volume-coercivity-exhaustion-uniqueness.md) couples box size to time and combines finite-volume functional inequalities, semigroup locality, and Gibbs compactness to prove infinite-volume uniqueness. [Finite-speed transfer](entries/finite-speed-finite-volume-transfer.md) is the graphical counterpart: a common-clock restriction coupling controls the boundary-influence error while a growing finite box supplies quantitative relaxation.

[Number rigidity and tail triviality](entries/number-rigidity-tail-dirichlet-ergodicity.md) take a different route. They identify the zero-energy functions of an infinite-particle Dirichlet form through local conditional irreducibility and tail structure, yielding qualitative \(L^2\) ergodicity without a spectral gap.

## Graphical ancestry, duality, and exact sampling

[Finite-ancestor duality plus extinction](entries/duality-extinction-finite-ancestor-process.md) rewrites local memory as survival of a finite graphical dual. [Coalescing-random-walk duality](entries/voter-coalescing-random-walk-duality.md) instead loses information when ancestral walks merge. [Parity duality](entries/parity-duality-branching-annihilating.md) allows a branching-annihilating dual to survive and grow; invariant-law identification comes from asymptotic parity randomization rather than extinction.

A [supercritical block construction](entries/supercritical-block-construction-complete-convergence.md) coarse-grains a surviving interface process and dominates oriented percolation from below, feeding survival and overlap information into a complete-convergence theorem. This is the opposite direction of comparison from subcritical disagreement domination.

[Coupling from the past](entries/coupling-from-the-past.md) seeks backward coalescence of a common random map and produces an exact stationary sample. [Clan-of-ancestors perfect simulation](entries/clan-of-ancestors-perfect-simulation.md) instead proves that only a finite backward dependency graph is needed to reconstruct the target. [Information percolation](entries/information-percolation-backward-histories.md) allows some histories to survive, provided those carrying initial information are sparse enough. The [distinguished-zero method for the East model](entries/east-distinguished-zero-screening.md) is a model-specific screening/regeneration mechanism based on a moving vacancy.

## Potential theory and metastable relaxation

[Potential-theoretic capacity](entries/potential-theoretic-capacity-metastability.md) is included as a closely related spin-relaxation tool. Dirichlet and flow variational principles estimate the capacity between metastable and stable valleys, which in turn gives sharp crossover-time asymptotics and exponential exit laws. This page is about metastable transitions, not a claim of global rapid mixing or a positive spectral gap.

## How to use the section

For a new model, first identify the object that carries memory or obstructs coercivity: an ordered disagreement, an influence matrix, a transportation distance, a space-time dependency path, a boundary perturbation, a Dirichlet form, a finite ancestor set, a conserved slow mode, a regeneration interface, or a metastable bottleneck. Then consult the corresponding page for the exact criterion, the mechanism that turns that criterion into a relaxation statement, a representative interacting-process application, and the main failure modes. Failure of one criterion is generally failure of that method, not evidence of nonergodicity.
