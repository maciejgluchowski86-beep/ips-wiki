---
title: Finite directional radius obstruction
status: proved here
tags:
  - PDE
  - coding tree
  - integrability
  - analytic function
  - jet
---

# Finite directional radius obstruction

Finite radius of the terminal Taylor series in one jet direction forces the derivative growth required by the [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md) on a bounded set of positive measure. Separating the even and odd Taylor subsequences shows that a finite ordinary directional radius obstructs the all-code \(L^1\) hypothesis in the [Nguwi--Penent--Privault Feynman--Kac theorem](npp-coding-tree-feynman-kac-theorem.md), although the odd case alone does not imply nonintegrability of the identity-rooted tree. The role of this result in the negative chain is summarized in the [PDE branching-representations overview](../pde-branching-representations.md).

**References.** The directional-radius terminology is recorded in [Directional jet radius](directional-jet-radius.md). The coding mechanism is that of Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882. The corollaries below are proved here.

## Setup and hypotheses

Fix a terminal time \(T>0\), an integer \(n\geq0\), a smooth nonlinearity

$$
f\in C^\infty(\mathbb R^{n+1}),
$$

and smooth terminal data

$$
\phi\in C^\infty(\mathbb R).
$$

These are the data of the [heat-reference terminal PDE](heat-reference-fully-nonlinear-pde.md)

$$
\partial_tu+rac12u_{xx}+f(J_nu)=0,
\qquad
u(T)=\phi.
$$

Let \(H(\mathcal T_{t,x,c})\) denote the [NPP coding-tree functional](npp-coding-tree.md) rooted at code \(c\), built with a strictly positive lifetime density and positive mechanism-selection probabilities as in that construction. Fix a jet direction

$$
j\in\{0,\ldots,n\}
$$

such that

$$
\phi^{(j+1)}\not\equiv0.
$$

Let \(g^*\) be an allowed composite code, so

$$
g
=
a\,\partial_{z_0}^{\lambda_0}\cdots\partial_{z_n}^{\lambda_n}f
$$

for some \(a\neq0\) and nonnegative integers \(\lambda_0,\ldots,\lambda_n\). For \(y\in\mathbb R\), define the formal directional coefficients

$$
a_r^g(y)
=
\frac{\partial_{z_j}^r g(J_n\phi(y))}{r!}.
$$

Define the even directional radius of \(g\) at \(y\) by

$$
R_{j,g}^{\mathrm{even}}(y)
=
\left(
\limsup_{m\to\infty}
|a_{2m}^g(y)|^{1/(2m)}
\right)^{-1}.
\tag{1}
$$

When \(g=f\), this is the even radius from [Directional jet radius](directional-jet-radius.md).

## Corollary

Suppose

$$
E
=
\left\{
 y\in\mathbb R:
 R_{j,g}^{\mathrm{even}}(y)<\infty
\right\}
$$

has positive Lebesgue measure. Then, for every \(t<T\) and every \(x\in\mathbb R\),

$$
\mathbb E\left[
\left|H(\mathcal T_{t,x,g^*})\right|
\right]
=
\infty.
\tag{2}
$$

## Proof

Since \(E\) has positive measure,

$$
E
=
\bigcup_{N,k\geq1}
\left(
E\cap[-N,N]\cap
\{R_{j,g}^{\mathrm{even}}\leq k\}
\right)
$$

contains a set

$$
E_0
=
E\cap[-N,N]\cap
\{R_{j,g}^{\mathrm{even}}\leq k\}
$$

of positive measure for some \(N,k\). Choose \(a\in(0,1/k)\), and set

$$
A_m
=
\left\{
 y\in E_0:
 \left|
 \partial_{z_j}^{2m}g(J_n\phi(y))
 \right|
 \geq
 (2m)!a^{2m}
\right\}.
\tag{3}
$$

For every \(y\in E_0\), the definition of the limsup in (1) implies that \(y\in A_m\) for infinitely many \(m\). Hence

$$
\sum_{m\geq1}\ind(A_m)(y)=\infty
\qquad(y\in E_0).
$$

[Tonelli's theorem](tonelli-markov-and-borel-cantelli.md) gives

$$
\sum_{m\geq1}|A_m|=\infty.
\tag{4}
$$

Consequently, for every \(\varepsilon>0\),

$$
|A_m|\geq e^{-\varepsilon m}
\tag{5}
$$

for infinitely many \(m\); otherwise the series in (4) would be eventually dominated by a convergent geometric series.

Take \(B=[-N,N]\). Along the subsequence in (5),

$$
D_m(B;g,j)
\geq
|A_m|(2m)!a^{2m},
$$

where \(D_m\) is the quantity defined in the [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md). Therefore

$$
\left(
\frac{D_m(B;g,j)}{m!}
\right)^{1/m}
\geq
 e^{-\varepsilon}a^2
\left(
\frac{(2m)!}{m!}
\right)^{1/m}.
$$

The last factor tends to infinity by Stirling's formula. The hypothesis of the repeated-Hessian obstruction is satisfied, which proves (2).

## Corollary

Let \(R_j(y)\) be the ordinary formal directional radius of

$$
w\longmapsto f(J_n\phi(y)+we_j).
$$

If

$$
\left|
\{y:R_j(y)<\infty\}
\right|>0,
\tag{6}
$$

then at least one of the two code-rooted functionals

$$
H(\mathcal T_{t,x,f^*}),
\qquad
H(\mathcal T_{t,x,(\partial_{z_j}f)^*})
$$

fails to belong to \(L^1\) for every \(t<T\) and every \(x\). In particular, the all-code integrability hypothesis of Nguwi--Penent--Privault Theorem 4.2 fails.

## Proof

The [even--odd radius identity](directional-jet-radius.md) gives

$$
R_j(y)
=
\min\left\{
R_j^{\mathrm{even}}(y),
R_j^{\mathrm{odd}}(y)
\right\}.
$$

Thus (6) implies that either the even radius is finite on a set of positive measure or the odd radius is finite on such a set. In the first case, the preceding corollary applies directly to \(g=f\).

In the second case, put \(g=\partial_{z_j}f\). Its even Taylor coefficients satisfy

$$
\frac{\partial_{z_j}^{2m}g(J_n\phi(y))}{(2m)!}
=
(2m+1)
\frac{\partial_{z_j}^{2m+1}f(J_n\phi(y))}{(2m+1)!}.
$$

The polynomial factor \(2m+1\) does not change finiteness of the corresponding radius, so \(g\) has finite even directional radius on a set of positive measure. Since \((\partial_{z_j}f)^*\) is an allowed composite code, the preceding corollary again applies.

The conclusion concerns the all-code hypothesis of Theorem 4.2. In the odd case it does not, by itself, imply

$$
\mathbb E\left[
|H(\mathcal T_{t,x,\operatorname{Id}})|
\right]
=
\infty.
$$

Such a statement would require a separate argument showing that the obstructed code contributes through an appropriate identity-rooted genealogy.