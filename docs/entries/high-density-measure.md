---
title: High-density measure
status: definition
tags:
  - centered moments
  - patch critical density
  - invariant class
---

# High-density measure

For a [spin system](spin-system.md) with the [patch positivity property](patch-positivity-property.md), high density is expressed by nonnegativity of all joint moments centered at the [patch critical density](patch-critical-density.md). This class contains, but is generally larger than, mixtures of [Bernoulli product measures](bernoulli-product-measure.md) with profiles above the critical profile.

**References.** None yet.

## Definition

Let

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

be the patch critical density profile. For \(A\Subset\Lambda\), define the centered monomial

$$
\chi_A^\star(\eta)
=
\prod_{i\in A}\left(\eta(i)-p_i^\star\right),
\qquad
\chi_\vn^\star=1.
$$

A probability measure \(\mu\) on \(\{0,1\}^\Lambda\) is **high-density** if

$$
\mu\left(\chi_A^\star\right)\ge0
\qquad
\text{for every }A\Subset\Lambda.
$$

The family of high-density measures is

$$
\mathcal M_\star
=
\left\{
\mu:
\mu\left(\chi_A^\star\right)\ge0
\text{ for every }A\Subset\Lambda
\right\}.
$$

The accompanying lower class is

$$
\mathcal M_-
=
\left\{
\mu:
\mu\left(\chi_A^\star\right)
\ge
-\chi_A^\star(\mathbf1)
\text{ for every }A\Subset\Lambda
\right\}.
$$

Equivalently,

$$
\mu\in\mathcal M_-
\quad\Longleftrightarrow\quad
\frac{\mu+\mu_{\mathbf1}}2\in\mathcal M_\star,
\tag{1}
$$

where \(\mu_{\mathbf1}\) is the point mass at the all-one configuration.

## Basic properties

Both \(\mathcal M_\star\) and \(\mathcal M_-\) are convex and weakly closed, and

$$
\mathcal M_\star\subseteq\mathcal M_-.
$$

Weak closedness follows because every \(\chi_A^\star\) is a bounded cylinder function. The [centered-moment monotonicity theorem](monomial-monotonicity-for-high-density-measures.md) also shows that the high-density class is preserved by the semigroup of every uniformly bounded finite-range patch-positive spin system:

$$
\mu\in\mathcal M_\star
\quad\Longrightarrow\quad
\mu P_t\in\mathcal M_\star
\qquad(t\ge0).
\tag{2}
$$

The class is nonempty because \(\mu_{\mathbf p^\star}\in\mathcal M_\star\). Under the usual Feller hypotheses, its convexity, weak closedness, and preservation imply that it contains an [invariant probability measure](invariant-measure.md).

Expanding an ordinary [monomial](monomials.md) around \(\mathbf p^\star\) gives

$$
\chi_A
=
\sum_{B\subseteq A}
\left(\prod_{i\in A\setminus B}p_i^\star\right)
\chi_B^\star.
$$

Consequently every \(\mu\in\mathcal M_\star\) satisfies

$$
\mu(\chi_A)
\ge
\mu_{\mathbf p^\star}(\chi_A)
\qquad(A\Subset\Lambda).
$$

This is an order of joint occupation moments; it is not, in general, stochastic domination.

## Bernoulli product measures

For a one-density profile \(\mathbf p\), independence gives

$$
\mu_{\mathbf p}\left(\chi_A^\star\right)
=
\prod_{i\in A}\left(p_i-p_i^\star\right).
$$

It follows that

$$
\mu_{\mathbf p}\in\mathcal M_\star
\quad\Longleftrightarrow\quad
\mathbf p\ge\mathbf p^\star.
\tag{3}
$$

Similarly, set

$$
\mathbf p^-=(p_i^-)_{i\in\Lambda},
\qquad
p_i^-
=
\left(2p_i^\star-1\right)\vee0.
$$

Then

$$
\mu_{\mathbf p}\in\mathcal M_-
\quad\Longleftrightarrow\quad
\mathbf p\ge\mathbf p^-.
\tag{4}
$$

Indeed, the singleton inequalities in the definition of \(\mathcal M_-\) give the necessity in (4). When \(p_i^\star<1\), division by \(1-p_i^\star\) reduces the remaining inequalities to the fact that a finite product of numbers in \([-1,1]\) is at least \(-1\). The case \(p_i^\star=1\) follows directly from the singleton inequality.

By convexity, mixtures of product measures with profiles above \(\mathbf p^\star\), respectively \(\mathbf p^-\), belong to \(\mathcal M_\star\), respectively \(\mathcal M_-\). These sufficient mixture descriptions do not characterize either class. If

$$
\mathbf p^\star\le\frac12\mathbf1,
$$

then every probability measure belongs to \(\mathcal M_-\), since the defining inequality holds pointwise after normalization by \(\chi_A^\star(\mathbf1)\).
