---
title: Weak parabolic solutions on the torus
status: definition
tags:
  - PDE
  - weak solution
  - distribution
  - parabolic equation
  - torus
---

# Weak parabolic solutions on the torus

For equations with two spatial derivatives on a flux, the weak formulation moves those derivatives onto a smooth test function. This permits uniqueness and stability estimates even when the solution itself does not have classical second derivatives. The \(H^{-1}\) uniqueness argument for the quadratic-Hessian equation is used in this sense.

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

## Nonlinear fluxes

For the quadratic diffusion equation

$$
\partial_tz
=
\partial_x^2\left(
\frac12z+\lambda z^2
\right),
\tag{3}
$$

a bounded weak solution is a function \(z\in L^\infty((0,T)\times\mathbb T)\) satisfying (2) with

$$
G
=
\frac12z+\lambda z^2.
$$

Boundedness makes \(G\) integrable on the finite space-time cylinder. The initial datum in the quadratic-Hessian problem is \(z_0=\phi''\), whose spatial mean is zero.

## Conservation of the mean

Taking test functions that approach a function constant in space shows that a weak solution of (1) satisfies

$$
\int_{\mathbb T}z(t,x)\,dx
=
\int_{\mathbb T}z_0(x)\,dx
$$

for almost every \(t\). Equivalently, the spatial integral of a second derivative flux vanishes. Thus differences of two solutions with the same initial datum have zero spatial mean, which is the condition needed to invert \(-\partial_x^2\) in the [\(H^{-1}\) energy method](h-minus-one-energy-method.md).

## Difference equation for the quadratic flux

If \(z\) and \(\widetilde z\) are bounded weak solutions of (3), then their difference \(w=z-\widetilde z\) satisfies

$$
\partial_tw
=
\partial_x^2\left[
\left(
\frac12+\lambda(z+\widetilde z)
\right)w
\right]
\tag{4}
$$

in distributions. This is just the factorization

$$
\left(
\frac12z+\lambda z^2
\right)
-
\left(
\frac12\widetilde z+\lambda\widetilde z^2
\right)
=
\left(
\frac12+\lambda(z+\widetilde z)
\right)(z-\widetilde z).
$$

When the coefficient in (4) is bounded below by a positive constant, the \(H^{-1}\) test can be justified by standard time regularization or approximation of weak solutions. The resulting estimate is the one recorded in [The \(H^{-1}\) energy method on the torus](h-minus-one-energy-method.md).
