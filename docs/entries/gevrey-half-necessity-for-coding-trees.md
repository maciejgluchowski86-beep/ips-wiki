---
title: Gevrey-1/2 necessity for coding trees
status: proved here
tags:
  - PDE
  - coding tree
  - integrability
  - Gevrey class
  - entire function
---

# Gevrey-1/2 necessity for coding trees

Finite absolute expectation of a composite-code [Nguwi--Penent--Privault coding tree](npp-coding-tree.md) imposes a factorial bound on the corresponding even terminal jet derivatives. If the trees rooted at both \(f^*\) and \((\partial_{z_j}f)^*\) are integrable, the even and odd bounds combine into a pointwise Gevrey-\(1/2\) bound almost everywhere. Under the smoothness assumptions of the coding-tree construction, this conclusion concerns the formal directional Taylor series; coincidence with the original directional germ requires an additional analyticity hypothesis.

**References.** The coding-tree construction is from Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882. The Gevrey and entire-function terminology is recorded in [Directional jet radius](directional-jet-radius.md). The necessity statements below are proved here.

Fix \(j\in\{0,\ldots,n\}\) with \(\phi^{(j+1)}\not\equiv0\), and let \(g^*\) be an allowed composite code. Recall

$$
D_m(B;g,j)
=
\int_B
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|\,dy
$$

from the [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md).

## Theorem

Suppose that for some \(t<T\) and \(x\in\mathbb R\),

$$
M
=
\mathbb E\left[
\left|H(\mathcal T_{t,x,g^*})\right|
\right]
<\infty.
\tag{1}
$$

Then there is a constant \(A<\infty\) such that, for every bounded measurable \(B\subseteq\mathbb R\), there is \(C_B<\infty\) with

$$
D_m(B;g,j)
\leq
C_B A^m m!
\qquad(m\geq1).
\tag{2}
$$

## Proof

The proof of the [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md) gives, for the fixed \((t,x)\), constants \(\alpha>0\), \(\beta>0\), and, for each bounded \(B\), a constant \(\kappa_B>0\) such that

$$
M
\geq
\alpha\kappa_B
\left(\frac{(T-t)\beta^2}{4}\right)^m
\frac{D_m(B;g,j)}{m!}.
$$

Rearranging gives (2), for example with

$$
A
=
\frac{4}{(T-t)\beta^2},
\qquad
C_B
=
\frac{M}{\alpha\kappa_B}.
$$

The exponential base \(A\) is independent of \(B\); only \(C_B\) depends on the bounded set.

## Proposition

Under the hypothesis of the theorem, for Lebesgue-almost every \(y\in\mathbb R\) there are constants \(C_y,A_y<\infty\) such that

$$
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|
\leq
C_y A_y^{2m}m!
\qquad(m\geq0).
\tag{3}
$$

## Proof

Fix a bounded set \(B\). By (2) and Markov's inequality,

$$
\left|
\left\{
 y\in B:
 \left|
 \partial_{z_j}^{2m}g(J_n\phi(y))
 \right|
>
C_B(2A)^m m!
\right\}
\right|
\leq
2^{-m}.
\tag{4}
$$

The right-hand side is summable in \(m\). The Borel--Cantelli lemma therefore implies that for almost every \(y\in B\), inequality

$$
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|
\leq
C_B(2A)^m m!
$$

holds for all sufficiently large \(m\). Absorbing the finitely many remaining values of \(m\) into a point-dependent constant gives (3) on \(B\). Applying this argument to the countable family \([-N,N]\), \(N\geq1\), and taking the union of the exceptional null sets gives the assertion on \(\mathbb R\).

## Corollary

Suppose that each of the two functionals rooted at

$$
f^*,
\qquad
(\partial_{z_j}f)^*
$$

has finite absolute expectation for at least one positive remaining time. Then for Lebesgue-almost every \(y\in\mathbb R\) there are constants \(C_y,A_y<\infty\) such that

$$
\left|
\partial_{z_j}^r f(J_n\phi(y))
\right|
\leq
C_y A_y^r\Gamma\left(\frac r2+1\right)
\qquad(r\geq0).
\tag{5}
$$

Consequently, for almost every such \(y\), the formal directional Taylor series

$$
F_y(w)
=
\sum_{r=0}^\infty
\frac{\partial_{z_j}^r f(J_n\phi(y))}{r!}w^r
\tag{6}
$$

converges on all of \(\mathbb C\). Moreover, there are constants \(C'_y,B_y<\infty\) such that

$$
|F_y(w)|
\leq
C'_y\exp(B_y|w|^2),
\qquad w\in\mathbb C.
\tag{7}
$$

Thus \(F_y\) has entire order at most \(2\); if its order is exactly \(2\), it has finite type.

## Proof

Apply the proposition first with \(g=f\). This gives the even derivatives of \(f\). Apply it again with \(g=\partial_{z_j}f\). Since

$$
\partial_{z_j}^{2m}g
=
\partial_{z_j}^{2m+1}f,
$$

the second application gives the odd derivatives. Intersecting the two full-measure sets and enlarging the point-dependent constants yields (5); for even \(r=2m\), \(\Gamma(r/2+1)=m!\), while for odd \(r=2m+1\), the factor \(m!\) from the proposition is bounded by a constant multiple of \(\Gamma(m+3/2)\).

The bound (5) is equivalent, up to changing the exponential constant, to

$$
\left|
\partial_{z_j}^r f(J_n\phi(y))
\right|
\leq
\widetilde C_y\widetilde A_y^r\sqrt{r!}.
$$

Hence the coefficients in (6) are bounded by

$$
\frac{\widetilde C_y\widetilde A_y^r}{\sqrt{r!}}.
$$

The series therefore has infinite radius of convergence, and the standard estimate for \(\sum_r s^r/\sqrt{r!}\) gives the Gaussian growth bound (7). The order and type conclusion follows from the [entire-function growth facts](directional-jet-radius.md).

## Analyticity remark

The conclusion above is deliberately about the formal Taylor series. Nguwi--Penent--Privault assume \(f\in C^\infty\), and a smooth one-variable germ need not agree with its Taylor series: a flat perturbation can have every Taylor coefficient equal to zero without vanishing near the base point.

If, in addition, the directional map

$$
w\longmapsto f(J_n\phi(y)+we_j)
$$

is real analytic near \(w=0\), then its germ agrees with the Taylor series (6). In that case \(F_y\) is an entire extension of the actual directional germ and satisfies the Gaussian bound (7). Without this added analyticity, no germ-extension conclusion is asserted.