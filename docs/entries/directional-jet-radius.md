---
title: Directional jet radius
status: definition
tags:
  - PDE
  - analytic function
  - jet
  - Gevrey class
  - entire function
---

# Directional jet radius

A nonlinearity \(f(z_0,\ldots,z_n)\) can be analytic in some jet directions and have a finite complex singularity distance in others. The directional jet radius isolates one coordinate at a fixed terminal [jet](heat-reference-fully-nonlinear-pde.md) and measures the radius of convergence seen by repeated differentiation in that coordinate. Even and odd radii record the two derivative subsequences separately.

**References.** Jet notation follows Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882; see [References](../meta/references.md). The radius, order, and type statements below are standard one-variable complex-analysis facts and are included with their definitions.

Fix terminal data \(\phi\), an integer \(j\in\{0,\ldots,n\}\), and a point \(y\in\mathbb R\). Let \(e_j\) denote the \(j\)-th coordinate vector of \(\mathbb R^{n+1}\).

## Definition

The directional one-variable function at \((y,j)\) is

$$
g_{y,j}(w)
=
f\bigl(J_n\phi(y)+w e_j\bigr).
\tag{1}
$$

When \(g_{y,j}\) is analytic near \(w=0\), write its Taylor germ as

$$
g_{y,j}(w)
=
\sum_{m=0}^\infty a_m(y,j)w^m,
\qquad
 a_m(y,j)
=
\frac{\partial_{z_j}^m f(J_n\phi(y))}{m!}.
\tag{2}
$$

The *directional jet radius* is the radius of convergence of (2):

$$
R_j(y)
=
\left(
\limsup_{m\to\infty}|a_m(y,j)|^{1/m}
\right)^{-1},
\tag{3}
$$

with the conventions \(1/0=\infty\) and \(1/\infty=0\). If \(f\) is only smooth, formula (3) still defines the radius of its formal directional Taylor series, but that series need not represent the original smooth germ.

## Definition

The even and odd directional radii are

$$
R_j^{\mathrm{even}}(y)
=
\left(
\limsup_{k\to\infty}|a_{2k}(y,j)|^{1/(2k)}
\right)^{-1},
$$

and

$$
R_j^{\mathrm{odd}}(y)
=
\left(
\limsup_{k\to\infty}|a_{2k+1}(y,j)|^{1/(2k+1)}
\right)^{-1}.
$$

These are the radii, in the original variable \(w\), of the even and odd parts

$$
\frac{g_{y,j}(w)+g_{y,j}(-w)}{2},
\qquad
\frac{g_{y,j}(w)-g_{y,j}(-w)}{2}.
$$

## Proposition

The full directional radius satisfies

$$
R_j(y)
=
\min\left\{
R_j^{\mathrm{even}}(y),
R_j^{\mathrm{odd}}(y)
\right\}.
\tag{4}
$$

## Proof

The limsup over all Taylor coefficients is the maximum of the limsups over the even and odd subsequences. Taking reciprocals gives (4), including the conventions at \(0\) and \(\infty\).

## Definition

An analytic directional germ satisfies a *Gevrey-\(1/2\) directional bound* at \((y,j)\) if there are constants \(C,A<\infty\) such that

$$
\left|
\partial_{z_j}^m f(J_n\phi(y))
\right|
\leq
C A^m\sqrt{m!}
\qquad(m\geq0).
\tag{5}
$$

Equivalently, its Taylor coefficients satisfy

$$
|a_m(y,j)|
\leq
\frac{C A^m}{\sqrt{m!}}.
\tag{6}
$$

The terminology *Gevrey-\(1/2\)* or *ultra-analytic* refers here to the derivative-growth convention (5). Some texts reserve the word *Gevrey* for orders at least one, so the explicit bound (5) is the operative definition on this page.

## Proposition

If (5) holds, the Taylor germ extends to an entire function of \(w\). More quantitatively, there exist \(C',B<\infty\) such that

$$
|g_{y,j}(w)|
\leq
C'\exp(B|w|^2),
\qquad w\in\mathbb C.
\tag{7}
$$

Conversely, an entire extension satisfying a bound of the form (7) satisfies (5), after changing the constants.

## Proof

Under (6), the power series in (2) converges for every \(w\), since \((m!)^{1/(2m)}\to\infty\). Standard estimates for the series \(\sum_m r^m/\sqrt{m!}\) give a Gaussian-exponential bound of the form (7). Conversely, Cauchy's estimate on the circle \(|w|=r\) gives

$$
|g_{y,j}^{(m)}(0)|
\leq
m!\,C'\frac{e^{Br^2}}{r^m}.
$$

Optimizing at \(r^2=m/(2B)\) and using Stirling's formula yields (5), with a possibly larger value of \(A\).

## Definition

For a nonconstant entire function \(g\), let

$$
M_g(r)=\max_{|w|=r}|g(w)|.
$$

Its *order* is

$$
\rho(g)
=
\limsup_{r\to\infty}
\frac{\log\log M_g(r)}{\log r}.
$$

If \(0<\rho(g)<\infty\), its *type* at that order is

$$
\sigma(g)
=
\limsup_{r\to\infty}
\frac{\log M_g(r)}{r^{\rho(g)}}.
$$

A bound of the form (7) means that the entire function has order at most \(2\), and if its order is exactly \(2\), then it has finite type. Thus Gevrey-\(1/2\) directional growth gives order at most \(2\), with finite type when the order is exactly \(2\); it is not the same as *exponential type*, which conventionally refers to order \(1\).

## Example

For

$$
f(z)=\frac{\eta}{1+z_j^2}
$$

and a base point with \((J_n\phi(y))_j=a\in\mathbb R\), the directional function is

$$
g_{y,j}(w)=\frac{\eta}{1+(a+w)^2}.
$$

Its nearest complex poles are at \(-a\pm i\), so

$$
R_j(y)=\sqrt{a^2+1}.
$$

At \(a=0\), the germ is even: \(R_j^{\mathrm{even}}(y)=1\) and \(R_j^{\mathrm{odd}}(y)=\infty\).
