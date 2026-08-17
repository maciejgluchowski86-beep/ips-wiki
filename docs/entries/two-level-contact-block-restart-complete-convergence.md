---
title: Block-and-restart complete convergence in a two-level contact process
status: literature
audit: current
tags:
  - contact process
  - block construction
  - complete convergence
---

# Block-and-restart complete convergence in a two-level contact process

## Criterion

A block construction becomes a complete-convergence method when it provides more than survival. One needs finite space-time events that can be restarted repeatedly, dominate a supercritical oriented percolation on survival, and can be built for both the forward process and a suitable graphical dual so that two surviving histories are forced to meet.

Ma implements this architecture for a two-level contact process: host animals form a supercritical contact process and fleas reproduce only through host-supported space-time paths. Theorem 3.5 gives finite block conditions equivalent to flea survival. Proposition 3.6 verifies these conditions for sufficiently large flea birth rate, and the construction is compared with supercritical oriented percolation. Section 4 then rebuilds the graphical representation on the whole time line so that the same block construction applies backward to the flea dual. Running the forward and dual systems toward time $T/2$, survival on both sides makes intersection overwhelmingly likely. This yields Theorem 2, the complete-convergence decomposition into extinction and the upper invariant state.

## Mechanism

The first role of the block construction is a **restart theorem**. If fleas survive, then with high probability a sufficiently large occupied seed generates another fully occupied seed in a prescribed neighboring space-time block. Because the event depends only on finitely many Poisson marks, after success the argument can restart from the new seed. Choosing the block error small enough gives domination of supercritical oriented percolation.

Survival alone does not identify the limiting law. For complete convergence the proof must also show that any fixed observation in the distant future has forgotten its finite initial state, conditional on survival. Ma extends the stationary host graphical environment to negative times using Kolmogorov extension and defines a backward flea process. The forward flea cluster from the initial state and the backward cluster from the test set each have their own good-block percolation when they survive. Their coarse percolation paths are arranged to meet around the midpoint. Graphical duality then converts this meeting into agreement of the relevant finite-dimensional event with the upper invariant process.

Thus the decisive object is the repeated **seed-to-seed restart** coupled with a forward/backward meeting argument. This is materially different from the live ADBARW block-construction page: there the same source family of coarse percolation is tied to a parity-preserving branching-annihilating system and its parity-duality classification. Here the model is contact-like in a dynamic host environment and the complete-convergence proof is built from restartable occupied blocks and dual intersection.

## Representative IPS use

The two-level process has four site states: empty, host only, fleas without host, and host with fleas. Animals evolve autonomously as a contact process; fleas see that process as a dynamic random environment. Theorem 1 shows finite critical flea birth rate when the host process percolates. Theorem 2 proves that, whenever flea survival has positive probability, a finite initial flea population converges to the mixture of extinction and the upper invariant flea law dictated by its survival probability.

## Limitations

The construction needs a robust finite-seed survival event that can be localized in space-time and made arbitrarily reliable after enlarging the blocks. It also uses positive dependence/monotonicity and a dual graphical representation compatible with the random environment. Some surviving IPS lack compact occupied seeds or have interfaces whose future cannot be restarted from finite data. A supercritical block comparison by itself proves only survival; the forward/dual meeting or an equivalent local-coupling step is additional mathematics needed for complete convergence.

## Sources

Ruibo Ma, *Complete convergence theorem for a two-level contact process*, ALEA **19** (2022), 943--976. Theorem 3.5 states the finite block conditions equivalent to survival and Proposition 3.6 verifies them in the supercritical-host regime. Section 4, especially Section 4.1, extends the graphical representation backward and applies the block construction to the dual; Theorem 2 is the resulting complete-convergence theorem. DOI: https://doi.org/10.30757/ALEA.v19-37. Preprint: https://arxiv.org/abs/1904.08401
