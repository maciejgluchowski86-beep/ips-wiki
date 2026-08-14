---
title: Conditional expectation and fluctuations of random fields
status: standard fact
tags:
  - probability
  - conditional expectation
  - random field
  - Banach space
  - branching process
  - PDE
---

# Conditional expectation and fluctuations of random fields

For a random field, taking a function-space norm before averaging and averaging before taking the norm are different operations. This distinction is important in branching representations with signed derivative weights: pathwise regularity can be poor even when conditional averaging restores a smooth deterministic operator. The natural decomposition is into a conditional mean and a centered fluctuation.

**References.** Conditional expectation is standard measure-theoretic probability. For Banach-valued integration and conditional expectation, see Joseph Diestel and John J. Uhl Jr., *Vector Measures*, American Mathematical Society, 1977. See [References](../meta/references.md).

## Scalar conditional expectation

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space, let \(Y\in L^1(\Omega)\), and let \(\mathcal G\subseteq\mathcal F\) be a sigma-field. The conditional expectation

$$
\mathbb E[Y\mid\mathcal G]
$$

is the \(\mathcal G\)-measurable integrable random variable characterized by

$$
\mathbb E\left[
\ind(A)\mathbb E[Y\mid\mathcal G]
\right]
=
\mathbb E[\ind(A)Y]
$$

for every \(A\in\mathcal G\).

If \(Y=Y(x)\) is a random field, the pointwise conditional mean is

$$
m(x)
:=
\mathbb E[Y(x)\mid\mathcal G].
\tag{1}
$$

When the field is jointly measurable, one can usually choose a jointly measurable version of \(m\) in the concrete constructions considered on this wiki.

## Banach-valued conditional expectation

Let \(X\) be a separable Banach space and let \(Y\in L^1(\Omega;X)\) in the Bochner sense described in [Random fields in function spaces](random-fields-in-function-spaces.md). Then there is an \(X\)-valued conditional expectation

$$
\mathbb E[Y\mid\mathcal G]
\in L^1(\Omega;X),
$$

characterized by the scalar conditional expectations obtained after applying continuous linear functionals on \(X\).

Conditional Jensen gives

$$
\left\lVert
\mathbb E[Y\mid\mathcal G]
\right\rVert_X
\leq
\mathbb E\left[
\lVert Y\rVert_X
\,\middle|\,
\mathcal G
\right]
$$

almost surely.

This inequality is one-way. A direct estimate of the right-hand side can be much worse than a direct analysis of the conditional mean on the left. Signed cancellations can occur inside the conditional expectation before the nonlinear norm is taken.

## Conditional mean versus expected pathwise norm

For a random spatial field \(Y(x)\), compare

$$
\mathbb E\lVert Y\rVert_{C^\alpha}
$$

with

$$
\left\lVert
\mathbb E[Y\mid\mathcal G]
\right\rVert_{C^\alpha}.
\tag{2}
$$

The first quantity measures the regularity of individual sample paths. The second measures the regularity remaining after the randomness outside \(\mathcal G\) has been averaged out. There is no reason for estimates of the two quantities to have the same short-scale behavior.

In particular, a centered random derivative weight may have a large pathwise \(C^\alpha\) norm while its conditional mean is a heat-semigroup derivative enjoying the cancellation estimates in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md).

## Mean-fluctuation decomposition

Define

$$
m
=
\mathbb E[Y\mid\mathcal G],
\qquad
R
=
Y-m.
\tag{3}
$$

Then

$$
\mathbb E[R\mid\mathcal G]=0.
\tag{4}
$$

We call \(m\) the *conditional mean field* and \(R\) the *conditional fluctuation field*. A proof can therefore separate two questions:

- regularity and size of the conditional mean \(m\);
- moments or weaker function-space bounds for the centered fluctuation \(R\).

The second problem can remain difficult even when the first is controlled by an exact cancellation identity.

## Conditional factorization

Suppose random variables or random fields \(Y_1,\ldots,Y_k\) are conditionally independent given \(\mathcal G\). Whenever the products are integrable,

$$
\mathbb E\left[
\prod_{j=1}^kY_j
\,\middle|\,
\mathcal G
\right]
=
\prod_{j=1}^k
\mathbb E[Y_j\mid\mathcal G].
\tag{5}
$$

Equation (5) is pointwise in any external spatial parameter. If the conditional means belong to a function space, the right side can then be estimated using deterministic product, commutator, or semigroup bounds in that space.

For branching constructions the sigma-field \(\mathcal G\) typically contains the exposed genealogy, branch times, offspring types, and ancestral positions, while independent Brownian increments and descendant auxiliary randomness remain to be averaged. The exact choice of \(\mathcal G\) must be stated in each application.

## Why this matters for patches

At finite depth, the [Duhamel patch regrouping](finite-depth-duhamel-patch-regrouping.md) can be randomized so that distinct side patches are conditionally independent given the patch skeleton. The deterministic Holder estimate for a complete patch acts naturally on the conditional mean side fields appearing after (5), not on the pathwise Holder norms of the raw side estimators.

The current [random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md) therefore separates conditional-mean regularity from fluctuation control. The former is compatible with Hermite centering and patch factorization; the latter remains an open source of absolute-moment growth.