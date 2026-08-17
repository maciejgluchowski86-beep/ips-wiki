---
method_id: block-coupling-joint-resampling
title: Block coupling by joint block resampling
category: coupling
targets:
  - mixing
model_scope: Finite spin-like configuration spaces with an ordered block-resampling dynamics that can be compared back to local updates
source_status: primary-checked
primary_source: Stefan Felsner, Daniel Heldt, Sandro Roch and Peter Winkler, "Block coupling and rapidly mixing k-heights," arXiv:2410.08992 (2024)
primary_pinpoint: Theorem 1; Sections 2.3--2.4 and 3.2; Theorems 6--8
primary_url: https://doi.org/10.48550/arXiv.2410.08992
application_source: same as primary source
application_pinpoint: Theorems 6--8 and Section 5
application_url: https://arxiv.org/abs/2410.08992
wiki_candidate: yes
---

# Block coupling by joint block resampling

## Criterion

Suppose a finite configuration space is partially ordered and is covered by a family of blocks \(\mathcal B\). Introduce an auxiliary chain that, instead of changing one coordinate, chooses a block \(B\in\mathcal B\) and resamples the entire configuration inside \(B\) conditionally on the outside configuration. For two ordered boundary conditions that differ at one boundary site \(v\in\partial B\), let \(E_{B,v}\) be the expected distance between the two block fillings under a monotone coupling of their conditional laws; Felsner--Heldt--Roch--Winkler call this the **block divergence**.

Their Theorem 1 gives a quantitative rapid-mixing criterion: if the chosen block family makes the total expected disagreement created through block boundaries strictly smaller than the amount of disagreement removed by updating blocks containing the discrepant site -- expressed by their block-divergence inequality with a constant \(\beta<1\) -- then the block chain contracts. Because each block move can be simulated by a sequence of moves of the original up/down chain, a comparison theorem transfers the resulting polynomial mixing bound to the original local dynamics. Corollary 1 gives a simpler sufficient condition using a uniform bound \(E_{\max}\) on block divergences and incidence counts of sites in blocks and block boundaries.

## Mechanism

The extra freedom is that the coupling acts on a **joint conditional distribution on many sites**. A one-site update may create too much expected distance for path coupling to contract, even though a larger region can equilibrate internally and screen the boundary discrepancy. The block chain exposes exactly that screening.

For the ordered state space of \(k\)-heights, admissible fillings of a block under two neighboring ordered exterior configurations are themselves stochastically ordered. Section 2.4 uses a finite Strassen-type argument to couple those fillings monotonically. Section 3.2 then applies this coupling to neighboring global configurations and measures the expected post-update distance by \(E_{B,v}\). Path coupling is used only after the **block-level** transition has been constructed, to extend the resulting contraction from neighboring states to arbitrary pairs. Finally the block transition is routed through legal one-site transitions of the original chain, so rapid mixing of the boosted chain is not mistaken for rapid mixing of a different model.

This is therefore distinct from ordinary one-site path coupling: the load-bearing estimate concerns a conditional block law, not the outcome of a single-site update. It is also distinct from coupling with stationarity, which relaxes worst-case contraction by excluding rare equilibrium states rather than by enlarging the update region.

## Representative IPS use

A \(k\)-height is a map \(V\to\{0,\ldots,k\}\) whose values at adjacent vertices differ by at most one. Section 5 identifies these configurations with a finite spin system with uniform weights. The original up/down chain is a one-site Glauber-type dynamics. The authors report that direct standard coupling did not yield the needed rapid-mixing estimate, introduce block resampling for this reason, and verify the block-divergence criterion for concrete graph families. Theorems 6--8 give polynomial mixing bounds for \(2\)- and \(3\)-heights on toroidal rectangular and hexagonal grids and on several planar cubic graph families.

## Limitations

The method needs tractable conditional laws on blocks and a coupling of those laws with a quantitatively small divergence. Choosing useful blocks can be highly model-specific, and estimating \(E_{B,v}\) may be the main computation. The cited theorem is finite-state and exploits a distributive-lattice order; it is not a generic block-dynamics theorem for arbitrary nonmonotone spin systems. A second comparison step is also required when the desired chain performs only local moves. Thus successful contraction of an artificial block chain is insufficient unless its block transitions can be simulated with controlled congestion or another valid comparison estimate.

## Sources

Primary checked source: Felsner, Heldt, Roch and Winkler, *Block coupling and rapidly mixing k-heights*, arXiv:2410.08992 (2024), especially Theorem 1, Sections 2.3--2.4 and 3.2, and Theorems 6--8. The paper explicitly distinguishes the auxiliary whole-block resampling chain from the original one-site up/down chain and carries out the comparison back to the latter.