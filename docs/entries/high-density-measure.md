---
title: Centered-moment order and cones
status: definition
audit: current
tags:
  - centered moments
  - patch threshold profile
  - invariant class
  - moment order
---

# Centered-moment order and cones

Fix a patch-positive spin system with [patch threshold profile](patch-critical-density.md)

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}.
$$

For $A\Subset\Lambda$, define

$$
\chi_A^*(\eta)
=
\prod_{i\in A}(\eta(i)-p_i^\star),
\qquad
\chi_\vn^*=1.
$$

## Centered-moment order

For probability measures $\mu$ and $\nu$, write

$$
\mu\preceq_*\nu
$$

when

$$
\mu(\chi_A^*)\le\nu(\chi_A^*)
\qquad
\text{for every }A\Subset\Lambda.
\tag{1}
$$

This is an order of centered joint moments. On the full space of probability measures it need not have a largest or smallest element, so it is kept distinct from ordinary stochastic order.

## The cone $\mathcal M_*$

Define

$$
\mathcal M_*
=
\left\{
\mu:
\mu(\chi_A^*)\ge0
\text{ for every }A\Subset\Lambda
\right\}.
\tag{2}
$$

Equivalently,

$$
\mathcal M_*
=
\{\mu:\mu_{\mathbf p^\star}\preceq_*\mu\}.
$$

The class is convex and weakly closed. For a Bernoulli product measure $\mu_{\mathbf p}$,

$$
\mu_{\mathbf p}(\chi_A^*)
=
\prod_{i\in A}(p_i-p_i^\star),
$$

hence

$$
\mu_{\mathbf p}\in\mathcal M_*
\quad\Longleftrightarrow\quad
\mathbf p\ge\mathbf p^\star.
\tag{3}
$$

The class is generally larger than mixtures of product measures above $\mathbf p^\star$.

## The affine classes $\mathcal M_{-,K}$

For $K\ge0$, define

$$
\mathcal M_{-,K}
=
\left\{
\mu:
\frac{\mu+K\mu_{\mathbf1}}{1+K}
\in\mathcal M_*
\right\},
$$

and

$$
\mathcal M_-
=
\bigcup_{K\ge0}\mathcal M_{-,K}.
\tag{4}
$$

Thus $\mathcal M_{-,0}=\mathcal M_*$. The older wiki convention identified $\mathcal M_-$ with the single class $\mathcal M_{-,1}$; (4) is the definition used in the canonical paper and in the common-limit theorem.

Set

$$
p_i^-=(2p_i^\star-1)\vee0.
$$

Then a product measure belongs to $\mathcal M_{-,1}$ exactly when

$$
\mathbf p\ge\mathbf p^-.
\tag{5}
$$

If $\mathbf p^\star\le\frac12\mathbf1$, every probability measure belongs to $\mathcal M_{-,1}$ and hence to $\mathcal M_-$.

The semigroup preservation of $\preceq_*$ and $\mathcal M_*$ is stated on [centered-moment order preservation](monomial-monotonicity-for-high-density-measures.md).
