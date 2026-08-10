---
title: Coarse chronology contraction route for one-dimensional FA-1f
status: heuristic
tags:
  - FA-1f
  - out of equilibrium
  - chronology
  - coarse graining
  - projections
---

# Coarse chronology contraction route for one-dimensional FA-1f

This entry records a proposed route to the remaining Bernoulli-quench problem for one-dimensional two-sided [FA-1f](fa-1f-model.md). It is deliberately weaker than the finite-time positivity targets in the [chronology-averaged sign route](chronology-averaged-sign-route-for-fa-1f.md). No new convergence theorem is claimed here.

## Diagnosis of the existing reductions

The exact centered dual reduces the unresolved range to an oscillatory negative-fugacity moment. Several further reductions then ask for a nonnegative quantity at every finite time: the shield inequality, adjacent-vacancy repulsion, fixed-count coefficient positivity, or rooted punctured positivity. These statements would solve the problem, but the local FA-1f kernel already has signed entries after the natural BABP-type change of basis. Deterministic update words can also have the wrong sign. Thus a proof cannot be local in one update and cannot be pathwise in chronology.

The simulations motivating the present route suggest a different phenomenon: after a region experiences several updates and their order is averaged, the local law rapidly loses memory of the initial discrepancy even though individual update orders may contribute with opposite signs. The proposed target is therefore **regional contraction after chronology averaging**, rather than regional positivity.

A second reason to coarse-grain in time is geometric. A single isolated vacancy cannot disappear by itself. Apparent loss of a vacancy occurs through an adjacent-vacancy excursion; after several local updates that excursion can return with the vacancy displaced, coalesced with another vacancy, or with an additional separated vacancy created. A one-ring Lyapunov estimate stops before this excursion has resolved and consequently misses the effective diffusive/branching motion of vacancies.

## Projection structure of one-site updates

Work in vacancy variables and let \(\mu_q\) be equilibrium. For a site \(i\), let \(E_i\) be Bernoulli-\(q\) resampling at \(i\), let \(c_i\) be the FA-1f constraint, and write the one-ring heat-bath operator as

$$
T_i=(1-c_i)I+c_iE_i.
$$

Since \(c_i\) does not depend on the state at \(i\), it commutes with \(E_i\). Hence on \(L^2(\mu_q)\),

$$
T_i^*=T_i,
\qquad
T_i^2=T_i.
$$

Thus every legal one-site heat-bath step is an orthogonal projection. Moreover \(T_i\) and \(T_j\) commute when \(|i-j|\ge 2\). In particular, all even-site projections commute with one another, as do all odd-site projections. If

$$
P_{\mathrm e}=\prod_{i\text{ even}}T_i,
\qquad
P_{\mathrm o}=\prod_{i\text{ odd}}T_i,
$$

on a finite interval, then one even-odd sweep is the alternating-projection operator \(P_{\mathrm e}P_{\mathrm o}\). Also

$$
-\mathcal L=\sum_i(I-T_i),
$$

so finite-volume spectral-gap information controls contraction of alternating products of the local projections. This is the same abstract structure underlying the detectability lemma for frustration-free local Hamiltonians; see Anshu--Arad--Vidick, [arXiv:1602.01210](https://arxiv.org/abs/1602.01210).

This observation does not by itself solve the out-of-equilibrium problem. Ordinary \(L^2(\mu_q)\) bounds are worst-case bounds and pay exponentially for a large initial density ratio. The useful statement must instead exploit the special Bernoulli initial law and the one-dimensional vacancy geometry.

## Proposed regional contraction lemma

Let \(I\) be a mesoscopic interval. Supply \(I\) with an admissible facilitating boundary transcript coming from vacancy paths or from a barrier/scaffold decomposition of the graphical construction. Let \(K_{I,T}^{\beta}\) denote the operator obtained by averaging all internal FA-1f rings in a time slab of length \(T\), conditional on the boundary transcript \(\beta\).

The desired statement is not that every coefficient of \(K_{I,T}^{\beta}\) is nonnegative in the negative-fugacity basis. Rather, one seeks a norm \(\|\cdot\|_\star\), tailored to the Bernoulli mismatch, and a projection \(Q_I\) removing the local equilibrium component, such that

$$
\sup_{\beta\in\mathcal B_I}
\|Q_I K_{I,T}^{\beta}\|_{\star\to\star}
\le \varepsilon
$$

once the slab contains sufficiently many effective internal updates. Ideally \(\varepsilon<1\) is uniform in the mesoscopic scale after that scale is chosen as a function of \(q\). An equivalent scalar version would bound the absolute value of the regional contribution to the negative-fugacity or shield observable rather than its sign.

The fixed-count formulation is particularly natural. Conditional on the number of rings at each site, the continuous-time kernel averages uniformly over all words with that site content. The local problem is therefore to prove contraction for this **symmetrized multiset-word operator** once every relevant site has been updated enough times. The deterministic-word counterexamples are then irrelevant rather than obstacles.

## How the one-dimensional geometry should enter

The barrier/scaffold construction can be reused, but its role should be changed. Its useful output is a factorization of unrevealed graphical randomness into one-dimensional spacetime regions. It should not be asked to make each region nonnegative.

For a long history contributing to a local observable, expose a two-sided collection of vacancy/barrier trajectories and decompose the history into regional slabs. Then prove a dichotomy.

1. A region is old or internally busy. Its averaged transfer is small by the regional contraction lemma.
2. A region is short or poorly updated. A long spacetime ancestry must then cross many such regions. Their probabilities, or weaker transfer norms, multiply to something small.

This would turn convergence into a product-of-contractions estimate. The required cancellation occurs inside each time-coarse region before absolute values are taken.

A useful geometric guide is the excursion of an isolated vacancy. Averaging until the local configuration again has no adjacent vacancies produces effective moves of the isolated-vacancy skeleton: displacement, coalescence, and branching into separated vacancies. The regional state space should remember only the data needed to control those return states, rather than the full microscopic update word.

## First finite problem

Before attempting a global proof, the route should be tested on the smallest genuinely two-sided region.

Take a path of three, then five, internal sites with facilitating boundary states. For each vector of site-ring counts, form the exact average over all compatible update orders and proposal coins. Compute the transfer operator on the centered/three-colour basis used in the chronology calculation. Search for a weighted \(\ell^1\), Bernstein, or small cone norm in which the non-equilibrium block has norm strictly below one after a bounded number of rings per site.

The target is **strict contraction**, not coefficientwise positivity. The test should be repeated over all admissible boundary transcripts. If no such norm exists on three sites, enlarge the block. A stable contraction visible at increasing block sizes would identify the correct finite-dimensional lemma to prove.

## What would count as progress

The main missing lemma should be stated quantitatively. A result of the form

$$
\|Q_I K_{I,T}^{\beta}\|_{\star\to\star}
\le C e^{-\kappa m(I,T,\beta)}
$$

for an effective update count \(m\), with constants controlled in the mesoscopic scale, would directly address the cancellation seen in simulations. By contrast, replacing rooted punctured positivity by another hierarchy of nonnegative observables would not change the basic obstruction unless the hierarchy itself supplies such a contraction.
