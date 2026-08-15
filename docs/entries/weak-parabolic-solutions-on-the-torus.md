---
title: Weak parabolic solutions on the torus
status: definition
audit: current
tags:
  - PDE
  - weak solution
  - distribution
  - parabolic equation
  - torus
---

# Weak parabolic solutions on the torus

For an evolution equation in which two spatial derivatives fall on a flux, the weak formulation moves those derivatives onto a smooth test function. This permits the equation to be interpreted when the solution or flux does not have classical second derivatives and supplies the natural interface with distributional and energy methods.

**References.** Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010, for distributions, Sobolev spaces, and weak formulations of evolution equations. See [References](../meta/references.md).

Throughout,

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

## Definition

Let \(z_0\in L^2(\mathbb T)\), and suppose \(z,G\in L^2((0,T)\times\mathbb T)\). We say that \(z\) is a *weak solution* of

$$
\partial_tz
=
\partial_x^2G,
\qquad
z(0)=z_0,
\tag{1}
$$

if, for every smooth periodic test function \(\psi\in C^\infty([0,T]\times\mathbb T)\) with \(\psi(T,\cdot)=0\),

$$
\int_0^T\int_{\mathbb T}
\left(
 z\,\partial_t\psi
+G\,\partial_x^2\psi
\right)\,dx\,dt
+
\int_{\mathbb T}z_0(x)\psi(0,x)\,dx
=0.
\tag{2}
$$

Formula (2) is obtained from (1) by integration by parts once in time and twice in space. No spatial boundary term occurs because the domain is periodic.

The definition does not require a particular constitutive law relating \(G\) to \(z\). In a nonlinear diffusion equation, for example, one may have \(G=F(z)\) provided the resulting flux has the integrability required in (2).

## Conservation of the mean

Taking test functions that approximate a function constant in space shows that a weak solution of (1) satisfies

$$
\int_{\mathbb T}z(t,x)\,dx
=
\int_{\mathbb T}z_0(x)\,dx
$$

for almost every \(t\). Equivalently, the spatial integral of a periodic second derivative vanishes in the distributional sense. Hence two weak solutions with the same initial mean have a difference of zero spatial mean, which is the condition needed to invert \(-\partial_x^2\) in the [\(H^{-1}\) energy method](h-minus-one-energy-method.md).

## Difference of two flux equations

Suppose \(z\) and \(\widetilde z\) satisfy

$$
\partial_tz=\partial_x^2G,
\qquad
\partial_t\widetilde z=\partial_x^2\widetilde G
$$

in the weak sense, with fluxes \(G\) and \(\widetilde G\) having the required integrability. Then their difference \(w=z-\widetilde z\) satisfies

$$
\partial_tw
=
\partial_x^2\left(G-\widetilde G\right)
\tag{3}
$$

in distributions. This follows by subtracting the two weak formulations. If the two solutions have the same initial datum, then \(w(0)=0\); if they only have the same initial mean, then \(w\) still has zero spatial mean for almost every time.

## Interface with the \(H^{-1}\) method

Equation (3) is in the form needed for the [\(H^{-1}\) energy method](h-minus-one-energy-method.md) whenever the flux difference can be decomposed as

$$
G-\widetilde G
=
a w+F.
\tag{4}
$$

For example, if \(a\) is bounded below by a positive constant and the remaining term \(F\) has suitable integrability, testing the zero-mean difference through the inverse Laplacian yields an \(H^{-1}\) energy estimate. The hypotheses and resulting estimate depend on the particular decomposition (4); the weak formulation itself supplies only the distributional equation and mean conservation needed to begin that argument.
