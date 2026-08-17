---
title: Block coupling by joint block resampling
status: literature
audit: current
tags:
  - coupling
  - block dynamics
  - mixing
---

# Block coupling by joint block resampling

## Criterion

Suppose a finite configuration space is partially ordered and covered by a family of blocks \(\mathcal B\). Introduce an auxiliary chain that chooses a block \(B\in\mathcal B\) and resamples the entire configuration inside \(B\) conditionally on the outside configuration. For two ordered boundary conditions differing at one boundary site \(v\in\partial B\), let \(E_{B,v}\) be the expected distance between the two block fillings under a monotone coupling of their conditional laws; Felsner--Heldt--Roch--Winkler call this the block divergence.

Their Theorem 1 gives a quantitative rapid-mixing criterion: if the total expected disagreement created through block boundaries is strictly smaller than the disagreement removed by updating blocks containing the discrepant site, expressed by their block-divergence inequality with a constant \(\beta<1\), then the block chain contracts. Each block move is then simulated by moves of the original local chain and a comparison argument transfers the polynomial mixing bound back to that chain.

## Mechanism

The extra freedom is that the coupling acts on a joint conditional distribution on many sites. A one-site update may create too much expected distance for ordinary [path coupling](path-coupling-glauber-dynamics.md) to contract, even though a larger region can equilibrate internally and screen the boundary discrepancy.

For \(k\)-heights, admissible fillings of a block under two neighboring ordered exterior configurations are stochastically ordered. The authors couple these fillings monotonically and measure the expected post-update distance by \(E_{B,v}\). Path coupling is used only after the block-level transition has been constructed, to extend contraction from neighboring global states. Finally the block transition is routed through legal one-site transitions of the original chain.

This is also distinct from [coupling with stationarity](coupling-with-stationarity-local-uniformity.md), which weakens worst-case contraction by excluding rare equilibrium configurations rather than enlarging the update region.

## Representative IPS use

A \(k\)-height is a map \(V\to\{0,\ldots,k\}\) whose values at adjacent vertices differ by at most one. The original up/down chain is a one-site Glauber-type dynamics. The authors introduce block resampling because direct standard coupling does not yield the needed estimate, and verify the block-divergence criterion for concrete graph families. Theorems 6--8 give polynomial mixing bounds for \(2\)- and \(3\)-heights on toroidal rectangular and hexagonal grids and on several planar cubic graph families.

## Limitations

The method needs tractable conditional laws on blocks and a quantitatively effective coupling of those laws. Choosing useful blocks can be model-specific, and estimating block divergence may be the main computation. The cited theorem exploits a distributive-lattice order and is not a generic theorem for arbitrary nonmonotone spin systems. Successful contraction of an artificial block chain is also insufficient unless its block transitions can be simulated with controlled comparison cost in the target chain.

## Sources

- Felsner, Heldt, Roch and Winkler, *Block coupling and rapidly mixing k-heights*, arXiv:2410.08992 (2024), Theorem 1, Sections 2.3--2.4 and 3.2, and Theorems 6--8, https://arxiv.org/abs/2410.08992.
