---
title: Random fields in function spaces
status: definition
tags:
  - probability
  - random field
  - Banach space
  - Holder regularity
  - PDE
---

# Random fields in function spaces

A pointwise family of random variables \(Y(x)\) does not by itself provide a random function with useful spatial regularity. To ask whether a branching estimator has a Holder, Sobolev, or Besov norm, the values at different space-time points must be coupled on one probability space and the resulting sample path must belong to the chosen function space. Moment estimates are then estimates of the random function-space norm.

**References.** The definitions below are standard Bochner-integration notions; see Joseph Diestel and John J. Uhl Jr., *Vector Measures*, American Mathematical Society, 1977. See [References](../meta/references.md).

## Banach-valued random variables

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space and let \(X\) be a Banach space with norm \(\lVert\cdot\rVert_X\). An \(X\)-valued random variable is a measurable map

$$
Y:\Omega\longrightarrow X.
$$

For \(1\leq p<\infty\), write

$$
Y\in L^p(\Omega;X)
$$

if

$$
\mathbb E\lVert Y\rVert_X^p<\infty.
\tag{1}
$$

The corresponding norm is

$$
\lVert Y\rVert_{L^p(\Omega;X)}
=
\left(
\mathbb E\lVert Y\rVert_X^p
\right)^{1/p}.
\tag{2}
$$

For separable \(X\), ordinary Borel measurability is enough for the applications on this wiki. For nonseparable function spaces such as a full \(L^\infty\) space, measurability should be checked for the concrete random field or formulated through a separable subspace in which the sample paths live.

## Random spatial Holder fields

Suppose \(Y(\omega,t,x)\) is a jointly defined random field on \([0,T]\times\mathbb T\). The statement

$$
Y\in L^p\left(
\Omega;
L^\infty([0,T];C^\alpha(\mathbb T))
\right)
\tag{3}
$$

means that, after choosing one version of the field,

$$
\mathbb E\left[
\sup_{0\leq t\leq T}
\lVert Y(t,\cdot)\rVert_{C^\alpha}^p
\right]<\infty.
\tag{4}
$$

This is stronger than the collection of pointwise moment estimates

$$
\sup_{t,x}\mathbb E|Y(t,x)|^p<\infty.
$$

The latter gives no control on spatial increments and therefore does not imply (3).

Similarly,

$$
Y\in L^p\left(
\Omega;
C^{\alpha/2,\alpha}([0,T]\times\mathbb T)
\right)
\tag{5}
$$

requires the realized sample paths to have a finite [parabolic Holder norm](parabolic-holder-spaces.md) and asks for a finite \(p\)-th moment of that norm.

## Coupling is part of a random-field statement

Suppose an estimator is defined separately for each starting point \(x\). If independent randomness is used for every \(x\), the resulting family has no reason to be continuous in \(x\), even when each marginal distribution is smooth in \(x\). To obtain a random field one normally uses common auxiliary randomness: for example, the same branching skeleton and the same Brownian increments are translated with the starting point.

The law of each pointwise estimator may be unchanged by this coupling, but its sample-path regularity depends strongly on the coupling. Regularity estimates for random branching fields must therefore state which randomness is shared across the space-time parameters.

## Pathwise regularity versus averaged regularity

A raw lifetime-based branching estimator can change its realized genealogy when the observation horizon crosses a sampled lifetime. Under the most direct common-randomness coupling in the horizon variable, the sample path in time can therefore jump even though its expectation is smooth. Thus pathwise parabolic Holder regularity may fail for a natural estimator.

This does not rule out weaker useful estimates. Possible targets include

$$
L^p\left(
\Omega;L^\infty_tC^\alpha_x
\right),
$$

integrated-in-time spatial regularity, or a [Besov norm](besov-spaces-on-the-torus.md) that averages or takes moments of scale-localized increments differently.

## Why this matters for random patches

The deterministic Holder patch estimate in the [\(L^1\) random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md) is geometric once the side profiles have controlled spatial \(C^\alpha\) norms. To turn that estimate into an \(L^1\) theorem, one must construct the side-patch estimators as random fields and control moments of the corresponding function-space norms recursively through the patch genealogy. Pointwise unbiasedness alone does not provide such control.