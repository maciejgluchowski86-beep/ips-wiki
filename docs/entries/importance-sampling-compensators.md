---
title: Importance-sampling compensators in branching representations
status: standard fact
tags:
  - probability
  - PDE
  - branching process
  - importance sampling
  - Monte Carlo
---

# Importance-sampling compensators in branching representations

Branching representations introduce auxiliary randomness to sample time integrals, monomial types, and terminal survival events. A *compensator* is the reciprocal sampling factor inserted so that averaging over this auxiliary randomness reproduces the original deterministic integral. The choice of sampling law changes the variance and integrability of the estimator, but not the formal first-branch recursion when the compensators are correct.

**References.** This mechanism is used explicitly in Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, arXiv:1603.01727, and Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, arXiv:2201.03882. See [References](../meta/references.md).

## Sampling an integral

Let \(\tau\) have density \(\rho>0\) on \((0,\infty)\). If \(F\) is integrable on \((0,h)\), then

$$
\mathbb E\left[
\ind(\tau<h)\frac{F(\tau)}{\rho(\tau)}
\right]
=
\int_0^hF(s)\,ds.
\tag{1}
$$

The factor \(1/\rho(\tau)\) is the compensator for sampling the integration time with density \(\rho\).

More generally, if \(I\) is sampled from a countable set with probabilities \(p_i>0\), then for an absolutely summable family \((a_i)\),

$$
\mathbb E\left[\frac{a_I}{p_I}\right]
=
\sum_i a_i.
\tag{2}
$$

Thus a reciprocal offspring-type probability converts a randomly selected summand back into the full sum.

## Survival compensation

Write

$$
\overline F(r)
=
\mathbb P(\tau\geq r)
=
\int_r^\infty\rho(s)\,ds.
$$

If a particle born with remaining horizon \(r\) contributes a terminal value \(G\) only when it survives to the horizon, then

$$
\mathbb E\left[
\ind(\tau\geq r)\frac{G}{\overline F(r)}
\right]
=G,
\tag{3}
$$

provided \(G\) is independent of the survival decision or the identity is read conditionally on the other data. This is the terminal compensator used in the NPP coding tree and in standard age-dependent branching representations.

## Multiplicative functionals

A *multiplicative functional* on a finite branching tree is a product of local factors attached to internal vertices and terminal leaves. A typical internal factor is

$$
\frac{c_I}{p_I\rho(\tau)},
$$

where \(c_I\) is the coefficient of the sampled nonlinear term. A typical terminal factor is

$$
\frac{G}{\overline F(r)}.
$$

The product over the whole tree is random because the branch times, offspring types, particle positions, and terminal data are random.

## First-branch cancellation

Let a root particle have remaining horizon \(h\). Split according to whether its lifetime exceeds \(h\). On survival, (3) cancels the survival probability and returns the linear semigroup transfer of the terminal datum. On branching at elapsed time \(s<h\) with type \(i\), the joint sampling factor is

$$
\rho(s)\,ds\,p_i.
$$

Multiplying by \(c_i/(p_i\rho(s))\) leaves \(c_i\,ds\). Conditional independence of the descendant subtrees then converts the product of descendant random variables into the product of their conditional expectations. Summing over \(i\) recovers the nonlinear Duhamel term.

This calculation is the common probabilistic skeleton behind the [branching-Duhamel tree](branching-diffusions-and-duhamel-trees.md), the [NPP coding-tree functional](npp-coding-tree.md), and HLOTW's marked branching estimator.

## Integrability warning

The cancellation above is an identity before absolute values. It does not imply

$$
\mathbb E|H|<\infty.
$$

Indeed, a small sampling probability creates a large reciprocal compensator. Likewise, a lifetime density that is too small near zero can amplify short-time derivative weights. Importance sampling therefore has two logically separate aspects:

- **unbiasedness:** the sampling law cancels algebraically in the expectation;
- **moment control:** the resulting compensated random variable must still belong to the required \(L^p\) space.

The [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md) exploits the first point in the opposite direction: on selected genealogies the auxiliary probabilities cancel exactly, exposing derivative growth that forces the absolute first moment to diverge.