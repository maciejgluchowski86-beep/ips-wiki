---
title: Potential-theoretic capacity for metastable spin relaxation
status: literature
audit: current
tags:
  - metastability
  - capacity
  - Glauber dynamics
---

# Potential-theoretic capacity for metastable spin relaxation

## Criterion

For a reversible Markov chain with invariant law \(\mu\), potential theory encodes the difficulty of moving from one region of state space to another by the capacity
\[
\operatorname{cap}(A,B)
=\sum_{x\in A}\mu(x)\,\mathbb P_x(\tau_B<\tau_A^+),
\]
for disjoint sets \(A,B\). The central analytic interface is variational. For the Glauber system studied by Bovier--den Hollander--Marello, Section 5.1 writes the capacity between a metastable valley and the lower-free-energy target set through the Dirichlet principle
\[
\operatorname{cap}(A,B)
=\inf\{\mathcal E(u,u):u|_A=1,\ u|_B=0\}.
\]
A complementary flow variational principle is used for the matching lower bound. Sharp asymptotics of this capacity, together with the stationary mass of the metastable valley, determine the metastable crossover scale.

Theorem 1.1 gives a sharp \(1+o_n(1)\) asymptotic for the average time to leave a metastable state for the set of states of lower free energy. Theorem 1.2 shows that, after normalization by its mean, the crossover time converges to an exponential law.

## Mechanism

The equilibrium free-energy landscape identifies local minima and the saddle that a transition must cross, but a free-energy barrier alone does not determine the prefactor of the transition time. Capacity inserts the dynamics. Its Dirichlet variational problem asks for the least dissipative function separating the two valleys; equivalently, the equilibrium potential solves the harmonic boundary-value problem between them.

The source first coarse-grains the disordered spin system by its level magnetizations. It obtains a sharp approximation of the Dirichlet form near the relevant saddle, then chooses a near-harmonic test function for the upper capacity bound and uses the Berman--Konsowa flow principle for the lower bound. Matching the two estimates produces sharp capacity asymptotics. Valley-mass estimates and potential-theoretic hitting-time identities then give the mean crossover and exponential-law conclusions.

## Representative IPS use

The application is an Ising spin system on the complete graph with random nonnegative coupling weights \(n^{-1}J(i)J(j)\), external field \(h\), and single-spin Metropolis dynamics at inverse temperature \(\beta\). The paper identifies the metastable parameter region and computes the transition from every metastable free-energy minimum to the set of lower minima. Disorder changes the correction terms in the crossover asymptotics, so the capacity analysis must retain more than the deterministic mean-field barrier.

## Limitations

Capacity methods are especially effective for metastable relaxation, not automatically for global total-variation mixing or a positive spectral gap. One must have enough control of the energy/free-energy landscape to identify the relevant valleys and saddles, and sharp prefactors require precise local approximations near those saddles.

This page is deliberately not a [conductance](large-set-conductance-warm-start.md) page. Conductance controls global bottlenecks; potential theory fixes physically relevant source and target sets and estimates their capacity sharply, often in the exponentially small regime where metastability occurs. The source proves crossover asymptotics and an exponential exit-time law, not rapid equilibrium mixing.

## Sources

- Bovier, den Hollander, Marello, *Metastability for Glauber Dynamics on the Complete Graph with Coupling Disorder*, Theorems 1.1-1.2, Section 5.1, equations (5.1), (5.3), and Sections 4-6, https://doi.org/10.1007/s00220-022-04351-8.
- Open preprint: https://arxiv.org/abs/2107.04543.
