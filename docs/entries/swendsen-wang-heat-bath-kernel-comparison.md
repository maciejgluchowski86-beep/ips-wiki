---
title: Swendsen-Wang cluster dynamics by Edwards-Sokal kernel comparison
status: literature
audit: current
tags:
  - spectral gap
  - mixing
  - Potts model
  - cluster dynamics
---

# Swendsen-Wang cluster dynamics by Edwards-Sokal kernel comparison

## Criterion

Let `P_SW` be Swendsen-Wang dynamics and `P_HB` the single-site heat-bath dynamics for the same finite q-state ferromagnetic Potts measure on a graph `G` of maximum degree `Delta`. Ullrich's Theorem 1 proves

`gap(P_SW) >= c_SW(G,beta,q) gap(P_HB)`,

with the explicit comparison constant

`c_SW = (1/(2 q^2)) (q exp(2 beta))^(-4 Delta)`.

Thus on any bounded-degree family, a polynomial or uniform lower bound for the heat-bath spectral gap transfers directly to Swendsen-Wang. Corollary 2 applies this to the two-dimensional square lattice above the Potts critical temperature and at the critical temperature for the Ising case; Corollary 3 gives a bounded-degree high-temperature regime.

## Mechanism

The cluster update is handled through the Edwards-Sokal coupling rather than decomposed into a path of local spin moves. Section 2.3 introduces the joint Potts/random-cluster law. The conditional kernel `T` samples FK bonds from a spin configuration and the adjoint conditional kernel `T*` recolors FK components. The Swendsen-Wang operator is exactly `P_SW = T T*` on Potts configurations; reversing the conditionals gives the corresponding random-cluster chain.

For comparison with heat bath, Section 3.1 introduces the reversible sandwich

`Q = P_HB P_SW P_HB`.

Lemma 5 proves `gap(Q) >= gap(P_HB)`: inserting the Markov contraction `P_SW` between two centered heat-bath operators cannot enlarge the relevant operator norm.

It remains to compare `Q` back to one Swendsen-Wang step. Lemma 6 compares Swendsen-Wang transition probabilities when edges are removed from the underlying graph. Lemma 7 uses this to show that changing one endpoint spin in the initial and final configurations changes a Swendsen-Wang transition probability by at most a degree-dependent factor. Since the two heat-bath factors in `Q` alter at most one spin at each endpoint, this gives a pointwise kernel domination of `Q` by a constant multiple of `P_SW`. A standard reversible comparison then yields Theorem 1.

The load-bearing interface is therefore an **exact joint-representation/operator factorization plus pointwise kernel comparison**. It is not the canonical-path method: no reference transition is routed through a sequence of target-chain transitions, and there is no path-congestion count.

## Representative IPS use

For the q-state Potts model on an `L x L` square lattice, known heat-bath gap estimates can be imported wholesale. Corollary 2 obtains polynomial-time Swendsen-Wang relaxation for every temperature above the critical point, and also at criticality when `q=2`. The comparison separates the difficult equilibrium/local-mixing input from the nonlocal cluster algorithm: once a heat-bath gap theorem is available, Theorem 1 turns it into a cluster-dynamics gap theorem.

This is useful more broadly whenever a nonlocal Monte Carlo update admits an auxiliary joint representation whose conditional kernels can be composed and compared to a tractable local chain.

## Limitations

The constant deteriorates exponentially with the maximum degree, so the theorem is principally useful on bounded-degree graph families. It does not show that Swendsen-Wang has its conjecturally much faster intrinsic relaxation scale; Ullrich explicitly notes that the comparison is expected to lose a factor related to system size.

The method also relies strongly on the ferromagnetic Potts/FK Edwards-Sokal representation and positivity of the associated conditional probabilities. It is a spectral-gap comparison, not by itself a logarithmic-Sobolev or entropy-contraction theorem.

## Sources

Primary source: Ullrich, *Comparison of Swendsen-Wang and Heat-Bath Dynamics*, Random Struct. Algorithms 42 (2013), Section 2.3, Theorem 1, and Lemmas 5-7 in Section 3.1, DOI `10.1002/rsa.20431`.
