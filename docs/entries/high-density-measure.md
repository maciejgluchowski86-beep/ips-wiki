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

For $A\Subset\Lambda$, define the centered monomial

$$
\chi_A^*(\eta)
=
\prod_{i\in A}(\eta(i)-p_i^\star),
\qquad
\chi_\varnothing^*=1.
\tag{1}
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
\tag{2}
$$

This compares all joint moments centered at the patch threshold profile. On the full space of probability measures, $\preceq_*$ need not have a largest or smallest element, so it is distinct from ordinary stochastic order.

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
\tag{3}
$$

Equivalently,

$$
\mathcal M_*
=
\{\mu:\mu_{\mathbf p^\star}\preceq_*\mu\}.
\tag{4}
$$

The class is convex and weakly closed. Its singleton conditions imply

$$
\mu(\eta(i))\ge p_i^\star.
$$

The ordinary monomial expands as

$$
\chi_A
=
\sum_{B\subseteq A}
\left(\prod_{i\in A\setminus B}p_i^\star\right)
\chi_B^*.
\tag{5}
$$

Thus every $\mu\in\mathcal M_*$ satisfies

$$
\mu(\chi_A)
\ge
\prod_{i\in A}p_i^\star.
\tag{6}
$$

For a Bernoulli product law $\mu_{\mathbf p}$,

$$
\mu_{\mathbf p}(\chi_A^*)
=
\prod_{i\in A}(p_i-p_i^\star).
\tag{7}
$$

The singleton moments show that

$$
\mu_{\mathbf p}\in\mathcal M_*
\quad\Longleftrightarrow\quad
\mathbf p\ge\mathbf p^\star.
\tag{8}
$$

The class $\mathcal M_*$ is generally larger than mixtures of product measures with profiles above $\mathbf p^\star$. Its semigroup invariance follows from [centered-moment order preservation](monomial-monotonicity-for-high-density-measures.md).

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
\tag{9}
$$

and

$$
\mathcal M_-
=
\bigcup_{K\ge0}\mathcal M_{-,K}.
\tag{10}
$$

Thus $\mathcal M_{-,0}=\mathcal M_*$. The affine definition is equivalent to the family of lower bounds

$$
\mu(\chi_A^*)
\ge
-K\mu_{\mathbf1}(\chi_A^*)
=
-K\prod_{i\in A}(1-p_i^\star)
\qquad(A\Subset\Lambda).
\tag{11}
$$

The union over all $K$ is the class used in the common invariant-limit theorem. In particular, $\mathcal M_-$ is not the single class $\mathcal M_{-,1}$.

## Product measures in $\mathcal M_{-,1}$

Set

$$
p_i^-=\max\{2p_i^\star-1,0\}.
\tag{12}
$$

Then

$$
\mu_{\mathbf p}\in\mathcal M_{-,1}
\quad\Longleftrightarrow\quad
\mathbf p\ge\mathbf p^-.
\tag{13}
$$

Indeed, by (7), membership in $\mathcal M_{-,1}$ is equivalent to

$$
\prod_{i\in A}(p_i-p_i^\star)
+
\prod_{i\in A}(1-p_i^\star)
\ge0
$$

for every finite $A$. The singleton condition is

$$
p_i-p_i^\star\ge-(1-p_i^\star),
$$

or $p_i\ge2p_i^\star-1$. Together with $p_i\ge0$, this gives $p_i\ge p_i^-$. Conversely, under these coordinatewise inequalities,

$$
|p_i-p_i^\star|\le1-p_i^\star
$$

whenever $p_i-p_i^\star<0$, while positive factors cause no obstruction; hence every finite product is bounded below by the negative of the all-one centered moment.

If

$$
\mathbf p^\star\le\tfrac12\mathbf1,
$$

then $\mathbf p^-=\mathbf0$, so every Bernoulli product law belongs to $\mathcal M_{-,1}$. In fact every probability measure belongs to $\mathcal M_{-,1}$: for every configuration $\eta$ and finite $A$,

$$
\chi_A^*(\eta)
\ge
-\prod_{i\in A}(1-p_i^\star)
=
-\mu_{\mathbf1}(\chi_A^*),
$$

because $p_i^\star\le1-p_i^\star$. Averaging over $\eta$ gives (11) with $K=1$.

## Configurations with finitely many facilitating sites

Under the hypotheses of the common invariant-limit theorem, the uniform pure-death component implies

$$
p_i^\star
\le
\frac{c_i^0(\varnothing)}{c_i^0(\varnothing)+c_i^1(\varnothing)}
<1.
\tag{14}
$$

Let $\eta$ have only finitely many facilitating sites

$$
F=\{i:\eta(i)=0\}.
$$

Then the point mass $\delta_\eta$ belongs to $\mathcal M_-$. One sufficient choice in (9) is any

$$
K
\ge
\prod_{i\in F}
\max\left\{1,\frac{p_i^\star}{1-p_i^\star}\right\}.
\tag{15}
$$

To see this, write

$$
\chi_A^*(\eta)
=
\prod_{i\in A\cap F}(-p_i^\star)
\prod_{i\in A\setminus F}(1-p_i^\star).
$$

If the sign is nonnegative there is no restriction. If it is negative, dividing its absolute value by $\mu_{\mathbf1}(\chi_A^*)=\prod_{i\in A}(1-p_i^\star)$ leaves

$$
\prod_{i\in A\cap F}\frac{p_i^\star}{1-p_i^\star},
$$

which is bounded by the right-hand side of (15). Hence (11) holds.
