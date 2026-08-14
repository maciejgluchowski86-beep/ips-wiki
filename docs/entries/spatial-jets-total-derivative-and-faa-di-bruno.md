---
title: Spatial jets, total derivatives, and Faà di Bruno
status: standard fact
tags:
  - PDE
  - jet
  - chain rule
  - Faà di Bruno
---

# Spatial jets, total derivatives, and Faà di Bruno

A spatial jet records finitely many derivatives of a function at one point. When a nonlinear function is evaluated on that jet, differentiating in the spatial variable acts simultaneously on every jet coordinate. The resulting total-derivative formulas are the deterministic source of the product terms encoded by the Nguwi--Penent--Privault mechanism.

**References.** Gregory M. Constantine and Thomas H. Savits, *A multivariate Faà di Bruno formula with applications*, *Transactions of the American Mathematical Society* **348** (1996), 503--520. Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, arXiv:2201.03882. See [References](../meta/references.md).

## Spatial jets

For a sufficiently differentiable function \(u=u(t,x)\), its spatial \(n\)-jet is

$$
J_nu(t,x)
=
\bigl(u,\partial_xu,\ldots,\partial_x^nu\bigr)(t,x).
$$

A generic jet coordinate is denoted by \(z_j\), so that after substitution

$$
z_j=\partial_x^ju.
$$

The [heat-reference PDE](heat-reference-fully-nonlinear-pde.md) uses precisely this convention.

## Total spatial derivative

Let \(g:\mathbb R^{n+1}\to\mathbb R\) be smooth. Along the jet of \(u\), the ordinary chain rule gives

$$
\partial_x\bigl[g(J_nu)\bigr]
=
\sum_{j=0}^n
\partial_{z_j}g(J_nu)\,
\partial_x^{j+1}u.
\tag{1}
$$

It is convenient to write the operator acting on jet functions as

$$
D_x
=
\sum_{j=0}^n z_{j+1}\partial_{z_j},
\tag{2}
$$

with the understanding that after applying \(D_x\) one substitutes \(z_{j+1}=\partial_x^{j+1}u\). Formula (2) is a bookkeeping device: it is not differentiation with respect to one jet coordinate, but differentiation along the spatially generated jet curve.

## Second total derivative

Differentiating (1) once more gives

$$
\begin{aligned}
\partial_x^2[g(J_nu)]
={}&
\sum_{j=0}^n
\partial_{z_j}g(J_nu)\,
\partial_x^{j+2}u\\
&+
\sum_{j,l=0}^n
\partial_{z_l}\partial_{z_j}g(J_nu)\,
\partial_x^{j+1}u\,
\partial_x^{l+1}u.
\end{aligned}
\tag{3}
$$

The second line is the Hessian term in jet space. In the NPP code mechanism, each summand becomes a three-child branch consisting of one composite code involving \(\partial_{z_l}\partial_{z_j}g\) and two spatial-derivative codes.

## Faà di Bruno formula

Let \(F:\mathbb R\to\mathbb R^d\) and \(g:\mathbb R^d\to\mathbb R\) be sufficiently smooth. For a set partition \(\pi\) of \(\{1,\ldots,k\}\), write \(|\pi|\) for its number of blocks and \(|B|\) for the size of a block \(B\in\pi\). Then

$$
\frac{d^k}{dx^k}g(F(x))
=
\sum_{\pi}
D^{|\pi|}g(F(x))
\left[
F^{(|B_1|)}(x),\ldots,F^{(|B_{|\pi|}|)}(x)
\right],
\tag{4}
$$

where the sum runs over all set partitions and \(D^r g\) denotes the symmetric \(r\)-linear derivative of \(g\).

Formula (4) is a compact coordinate-free form of Faà di Bruno. Expanding the multilinear forms into coordinates produces sums of products of derivatives of \(g\) and derivatives of the components of \(F\), together with the familiar combinatorial multiplicities.

For \(F(x)=J_nu(t,x)\), every derivative \(F^{(r)}\) is a vector of higher spatial derivatives of \(u\). Hence repeated differentiation of \(g(J_nu)\) produces exactly the kind of finite products of derivative codes used in the [NPP coding tree](npp-coding-tree.md).

## Why coefficients can be absorbed into codes

Different set partitions may produce the same ordered collection of spatial derivative orders, so coordinate expansions of (4) contain positive integer combinatorial coefficients. The NPP code class permits arbitrary nonzero scalar multiples of derivatives of \(f\). Their mechanism therefore absorbs these deterministic coefficients into the scalar attached to the corresponding composite code rather than introducing a separate coefficient variable at each branch.