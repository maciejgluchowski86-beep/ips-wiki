---
title: Feynman-Kac formula for linear parabolic equations
status: standard fact
tags:
  - PDE
  - probability
  - Feynman-Kac formula
  - diffusion
  - semigroup
---

# Feynman-Kac formula for linear parabolic equations

The classical Feynman--Kac formula represents a linear parabolic PDE by an expectation over a diffusion path. Nonlinear branching formulas generalize this idea: the diffusion still carries the linear part, while branching or auxiliary random weights encode nonlinear terms that a single path cannot represent directly.

**References.** Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, second edition, Springer, 1991. Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes*, Springer, 2006 reprint. See [References](../meta/references.md).

## Heat equation

Let \(X_s=x+W_s-W_t\) be Brownian motion started from \(x\) at time \(t\). For bounded continuous terminal data \(\phi\), the backward heat equation

$$
\partial_tu
+\frac12\partial_x^2u
=0,
\qquad
u(T,x)=\phi(x),
\tag{1}
$$

has the representation

$$
u(t,x)
=
\mathbb E_{t,x}[\phi(X_T)]
=
P_{T-t}\phi(x).
\tag{2}
$$

On the torus, \(X\) is read modulo \(2\pi\), or equivalently one uses the periodic heat semigroup.

## Adding a potential

Consider

$$
\partial_tu
+\frac12\partial_x^2u
+V(t,x)u
=0,
\qquad
u(T,x)=\phi(x),
\tag{3}
$$

with bounded continuous \(V\). Then

$$
u(t,x)
=
\mathbb E_{t,x}\left[
\exp\left(
\int_t^T V(s,X_s)\,ds
\right)
\phi(X_T)
\right].
\tag{4}
$$

The exponential factor is often called a *Feynman--Kac weight*.

## Adding a source term

For

$$
\partial_tu
+\frac12\partial_x^2u
+V(t,x)u
+g(t,x)
=0,
\qquad
u(T,x)=\phi(x),
\tag{5}
$$

the formula becomes

$$
\begin{aligned}
u(t,x)
={}&
\mathbb E_{t,x}\left[
 e^{\int_t^T V(r,X_r)\,dr}
 \phi(X_T)
\right]\\
&+
\mathbb E_{t,x}\left[
\int_t^T
 e^{\int_t^s V(r,X_r)\,dr}
 g(s,X_s)\,ds
\right].
\end{aligned}
\tag{6}
$$

Equation (6) is the probabilistic analogue of the Duhamel formula.

## Proof idea by Ito's formula

Define

$$
M_s
=
\exp\left(
\int_t^sV(r,X_r)\,dr
\right)
u(s,X_s).
$$

Applying [Ito's formula](ito-diffusions-and-backward-kolmogorov-representation.md) gives

$$
\begin{aligned}
dM_s
={}&
e^{\int_t^sV}
\left(
\partial_su
+\frac12u_{xx}
+Vu
\right)(s,X_s)\,ds\\
&+
e^{\int_t^sV}
u_x(s,X_s)\,dW_s.
\end{aligned}
$$

For equation (3) the drift vanishes, so \(M\) is a martingale after the usual integrability check. Taking expectations between \(t\) and \(T\) yields (4). For equation (5), integrating the remaining drift gives (6).

## General diffusions

If

$$
dX_s
=b(s,X_s)\,ds
+\sigma(s,X_s)\,dW_s,
$$

then the second-order operator

$$
\mathcal L_s
=b(s,x)\partial_x
+\frac12\sigma(s,x)^2\partial_x^2
$$

replaces \(\frac12\partial_x^2\). Under standard regularity and integrability assumptions, solutions of

$$
\partial_tu+\mathcal L_tu+Vu+g=0
$$

have the analogous path representation.

## Relation to branching formulas

The classical formula is linear in \(u\). If the PDE contains a nonlinear term such as

$$
f(u,\partial_xu,\partial_x^2u),
$$

a single diffusion path does not directly turn products of unknown solution values into an expectation. [Duhamel trees](branching-diffusions-and-duhamel-trees.md) and their branching randomizations address this by creating descendants whose conditionally independent contributions multiply.

Thus titles such as the [Nguwi--Penent--Privault coding-tree Feynman--Kac theorem](npp-coding-tree-feynman-kac-theorem.md) use “Feynman--Kac” in an extended sense: the representation remains probabilistic and diffusion-based, but nonlinearities are encoded by a random tree rather than by one exponential weight along one path.