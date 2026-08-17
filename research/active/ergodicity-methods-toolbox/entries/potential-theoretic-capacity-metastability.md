---
method_id: potential-theoretic-capacity-metastability
title: Potential-theoretic capacity for metastable spin relaxation
category: other
targets:
  - metastable-relaxation
model_scope: Reversible Glauber/Metropolis spin systems with metastable and stable valleys, illustrated by a disordered Curie-Weiss model
source_status: primary-checked
primary_source: Anton Bovier, Frank den Hollander, Saeda Marello, Metastability for Glauber Dynamics on the Complete Graph with Coupling Disorder, Communications in Mathematical Physics 392 (2022), 307-345.
primary_pinpoint: Theorems 1.1-1.2 (mean crossover and exponential law); Section 5.1, equations (5.1) and (5.3) (capacity and Dirichlet principle); Sections 4-5 for Dirichlet-form and capacity asymptotics
primary_url: https://doi.org/10.1007/s00220-022-04351-8
application_source: Anton Bovier, Frank den Hollander, Saeda Marello, Metastability for Glauber Dynamics on the Complete Graph with Coupling Disorder, Communications in Mathematical Physics 392 (2022), 307-345.
application_pinpoint: Theorems 1.1-1.2 and Sections 4-6
application_url: https://arxiv.org/abs/2107.04543
wiki_candidate: yes
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
\tag{5.3}
\]
A complementary flow variational principle is used for the matching lower bound. Sharp asymptotics of this capacity, together with the stationary mass of the metastable valley, determine the metastable crossover scale.

In their disordered Curie--Weiss Glauber dynamics, Theorem 1.1 gives a sharp \(1+o_n(1)\) asymptotic for the average time to leave any metastable state for the set of states of lower free energy. Theorem 1.2 shows that after normalization by its mean, the crossover time converges to an exponential law. Thus the capacity computation is not merely an equilibrium bottleneck diagnostic: it quantitatively identifies the stochastic relaxation time between metastable and stable regions.

## Mechanism

The equilibrium free-energy landscape identifies local minima and the saddle that a transition must cross, but a free-energy barrier alone does not determine the prefactor of the transition time. Capacity inserts the dynamics. Its Dirichlet variational problem asks for the least dissipative function separating the two valleys; equivalently, the equilibrium potential solves the harmonic boundary-value problem between them.

The source first coarse-grains the disordered spin system by its level magnetizations. Section 4 obtains a sharp approximation of the Dirichlet form near the relevant saddle. Section 5 then chooses a near-harmonic test function in the Dirichlet principle for the upper capacity bound and uses the Berman--Konsowa flow principle for the lower bound. Matching both estimates produces the sharp capacity asymptotics. Valley-mass estimates and standard potential-theoretic hitting-time identities then convert this static variational calculation into the mean crossover and exponential-law conclusions of Theorems 1.1--1.2.

The method therefore separates naturally into three reusable tasks: identify metastable/stable valleys, estimate the capacity by variational principles, and combine capacity with valley mass to control transition times.

## Representative IPS use

The application is an Ising spin system on the complete graph with random nonnegative coupling weights \(n^{-1}J(i)J(j)\), external field \(h\), and single-spin Metropolis dynamics at inverse temperature \(\beta\). The paper identifies the metastable parameter region and computes the transition from every metastable free-energy minimum to the set of lower minima. Disorder changes the correction terms in the crossover asymptotics, so the capacity analysis must retain more than the deterministic mean-field barrier.

This potential-theoretic architecture is widely adapted to finite-volume Glauber dynamics and other reversible interacting systems when rare transitions, rather than a uniform spectral gap, control observable relaxation.

## Limitations

Capacity methods are especially effective for **metastable relaxation**, not automatically for global total-variation mixing or a positive spectral gap. One must already have enough control of the energy/free-energy landscape to identify the relevant valleys and saddles, and sharp prefactors require precise local approximations near those saddles. Multiple competing saddles or strongly nonreversible dynamics complicate the variational problem substantially.

This page is deliberately not a Cheeger/conductance page. Conductance takes an infimum over cuts to bound a global gap or mixing time; potential theory fixes physically relevant source and target sets and estimates their capacity sharply, often in the exponentially small regime where metastability occurs. It is also distinct from canonical paths: the lower bound here comes from a variational flow principle optimized at the valley scale rather than routing every state-space edge through prescribed paths.

The source proves metastable crossover asymptotics and an exponential exit-time law. It does **not** claim rapid equilibrium mixing, so the target is recorded as metastable relaxation rather than mixing or spectral gap.

## Sources

- Bovier, den Hollander, Marello, *Metastability for Glauber Dynamics on the Complete Graph with Coupling Disorder*, Theorems 1.1-1.2, Section 5.1, equations (5.1), (5.3), and Sections 4-6, https://doi.org/10.1007/s00220-022-04351-8.
- Open preprint: https://arxiv.org/abs/2107.04543.
