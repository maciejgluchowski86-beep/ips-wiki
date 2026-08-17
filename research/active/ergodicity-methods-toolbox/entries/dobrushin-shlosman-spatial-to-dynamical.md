---
method_id: dobrushin-shlosman-spatial-to-dynamical
title: Dobrushin-Shlosman spatial mixing implies dynamical relaxation
category: spatial-mixing
targets:
  - log-sobolev
  - convergence
  - mixing
  - spectral-gap
model_scope: Finite-range Gibbs spin systems with strong uniform spatial mixing and Glauber dynamics
source_status: primary-checked
primary_source: Daniel W. Stroock and Boguslaw Zegarlinski, The equivalence of the logarithmic Sobolev inequality and the Dobrushin-Shlosman mixing condition, Communications in Mathematical Physics 144 (1992), 303-323.
primary_pinpoint: Theorem 1.2 for uniform LSI versus Dobrushin-Shlosman mixing; Theorems 3.2 and 3.6 for uniform Glauber relaxation
primary_url: https://doi.org/10.1007/BF02101094
application_source: Daniel W. Stroock and Boguslaw Zegarlinski, The equivalence of the logarithmic Sobolev inequality and the Dobrushin-Shlosman mixing condition, Communications in Mathematical Physics 144 (1992), 303-323.
application_pinpoint: Theorems 3.2 and 3.6 on uniform convergence rates for the associated Glauber dynamics
application_url: https://doi.org/10.1007/BF02101094
wiki_candidate: yes
---

# Dobrushin-Shlosman spatial mixing implies dynamical relaxation

## Criterion

Dobrushin--Shlosman mixing is a uniform finite-volume condition saying, roughly, that changing boundary conditions far from a local region changes its Gibbs marginal by an amount decaying with the separation, uniformly over volumes and admissible boundaries. For finite-range lattice gases with compact spin space, Stroock--Zegarlinski Theorem 1.2 proves that this spatial condition is equivalent to a **uniform logarithmic Sobolev inequality** for the corresponding finite-volume specifications. Their Theorems 3.2 and 3.6 further identify these conditions with a uniform rate at which the associated Glauber dynamics approaches equilibrium. Thus a static boundary-influence estimate can imply hypercontractivity, a positive spectral gap, and quantitative dynamical relaxation without constructing a coupling trajectory by trajectory.

## Mechanism

The bridge works by turning spatial decoupling into functional-inequality tensorization. If distant boundary perturbations have uniformly small influence, conditional expectations over blocks are close to independent projections. One can then decompose entropy or variance into local conditional pieces while controlling the error caused by interaction across block boundaries. Iterating this decomposition yields a finite-volume log-Sobolev constant bounded uniformly in the volume and boundary condition.

Once the uniform LSI is available, the usual semigroup consequences give hypercontractivity and, through the implication LSI \(\Rightarrow\) Poincare, uniform exponential \(L^2\) relaxation. Stroock--Zegarlinski go further: in their finite-range setting the spatial mixing condition and the uniform dynamical relaxation property are equivalent, making this a genuine static-to-dynamic criterion rather than a one-way perturbative estimate.

## Representative IPS use

The method is formulated precisely for stochastic Glauber dynamics of lattice spin systems. Stroock--Zegarlinski's Theorems 3.2 and 3.6 turn the Dobrushin--Shlosman spatial criterion into a uniform convergence rate for the associated Glauber dynamics. The archetypal use is a high-temperature or otherwise strongly mixing Ising-type system: first establish uniform decay of boundary influence for the Gibbs specification, then inherit a volume-uniform functional inequality and rapid dynamical relaxation.

A companion paper by the same authors treats finite spin spaces explicitly. This route is conceptually distinct from the elementary single-site Dobrushin contraction criterion. Dobrushin--Shlosman conditions are block/spatial mixing conditions and can hold in parameter regimes where a simple one-site influence matrix is too crude.

## Limitations

The theorem requires a strong **uniform** spatial mixing condition, not merely uniqueness of the infinite-volume Gibbs measure or decay of correlations under one preferred boundary condition. Its classical form is tailored to finite-range reversible Gibbs dynamics. Verifying Dobrushin--Shlosman mixing can itself be difficult, especially near critical points, phase coexistence, or with hard constraints. The exact relationship between named notions such as strong mixing, complete analyticity, and strong spatial mixing depends on the source and geometry; they should not be silently identified outside the theorem's hypotheses. For non-Gibbsian IPS with no static specification, this bridge may have no direct object to which it applies.

## Sources

- Stroock, Zegarlinski, *The equivalence of the logarithmic Sobolev inequality and the Dobrushin-Shlosman mixing condition*, Theorem 1.2 and Theorems 3.2, 3.6, https://doi.org/10.1007/BF02101094.
- Stroock, Zegarlinski, *The logarithmic Sobolev inequality for discrete spin systems on a lattice*, Communications in Mathematical Physics 149 (1992), 175-193, https://doi.org/10.1007/BF02096629.
