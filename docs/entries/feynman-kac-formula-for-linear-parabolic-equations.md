---
title: Feynman-Kac formula for linear parabolic equations
status: standard fact
audit: current
tags:
  - PDE
  - probability
  - Feynman-Kac formula
  - diffusion
  - semigroup
---

# Feynman-Kac formula for linear parabolic equations

The classical Feynman--Kac formula represents a linear parabolic equation by an expectation over a diffusion path. The Gaussian heat equation is the basic case; a bounded potential produces an exponential path weight, and a bounded source produces a time integral along the path.

**Prerequisite.** The normalization $\partial_tu=\frac12\Delta u$ and the Gaussian heat operators are fixed in [Heat equation and Gaussian heat kernel](heat-equation-and-gaussian-heat-kernel.md).

**References.** Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991, §4.3 for the heat equation and §4.4, especially the multidimensional and one-dimensional Feynman--Kac formulas. For diffusion generators and their PDE connection, see §5.7 of the same book. See [References](../meta/references.md).

Throughout the first three sections, let $X_s=x+W_s-W_t$ be Brownian motion started from $x$ at time $t$. To keep every expectation automatically finite, assume the terminal datum $\phi$ is bounded and continuous and, when present, the potential $V$ and source $g$ are bounded and continuous on $[0,T]\times\mathbb R$. These are convenient sufficient hypotheses for the probabilistic formulas below. Stronger regularity may be imposed when a classical $C^{1,2}$ solution is required.

## Heat equation

For the backward heat equation

$$
\partial_tu
+\frac12\partial_x^2u
=0,
\qquad
u(T,x)=\phi(x),
\tag{1}
$$

we have

$$
u(t,x)
=\mathbb E_{t,x}[\phi(X_T)]
=P_{T-t}\phi(x).
\tag{2}
$$

For bounded uniformly continuous $\phi$, the [approximate-identity theorem](heat-equation-and-gaussian-heat-kernel.md#approximate-identity) gives the terminal condition uniformly as $t\uparrow T$. On the torus, use the periodized kernel or read $X$ modulo $2\pi$.

## Adding a bounded potential

Let $V\in C_b([0,T]\times\mathbb R)$. For

$$
\partial_tu
+\frac12\partial_x^2u
+V(t,x)u
=0,
\qquad
u(T,x)=\phi(x),
\tag{3}
$$

the Feynman--Kac formula is

$$
u(t,x)
=\mathbb E_{t,x}\left[
\exp\left(
\int_t^T V(s,X_s)\,ds
\right)
\phi(X_T)
\right].
\tag{4}
$$

Because $V$ and $\phi$ are bounded, the random variable in (4) is bounded in absolute value by $e^{T\|V\|_\infty}\|\phi\|_\infty$.

## Adding a bounded source term

Let in addition $g\in C_b([0,T]\times\mathbb R)$. For

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

The second expectation is absolutely integrable because its integrand is bounded by $e^{T\|V\|_\infty}\|g\|_\infty$. Equation (6) is the probabilistic version of the Duhamel/variation-of-constants formula.

## Verification by Itô's formula

Suppose, in addition to the boundedness assumptions above, that $u$ is a bounded $C^{1,2}$ solution of (3). Define

$$
M_s
=
\exp\left(
\int_t^sV(r,X_r)\,dr
\right)u(s,X_s).
$$

Applying [Itô's formula](ito-diffusions-and-backward-kolmogorov-representation.md) gives

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

The drift vanishes. If $u_x$ is bounded, the stochastic integral is square-integrable, hence a true martingale, and taking expectations gives (4). For (5), the same calculation leaves the drift $-g(s,X_s)$ and yields (6). Thus the stochastic representation and the analytic theorem constructing a sufficiently regular solution are logically separate statements.

## General diffusion

Let

$$
dX_s
=b(s,X_s)\,ds
+\sigma(s,X_s)\,dW_s.
\tag{7}
$$

A convenient sufficient hypothesis is that $b$ and $\sigma$ are bounded and continuous, globally Lipschitz in the spatial variable uniformly in time, and that $\sigma$ is uniformly nondegenerate. Then (7) has a unique strong solution, and its generator is

$$
\mathcal L_s
=b(s,x)\partial_x
+\frac12\sigma(s,x)^2\partial_x^2.
\tag{8}
$$

If $\phi\in C_b(\mathbb R)$ and $V,g\in C_b([0,T]\times\mathbb R)$, the path functional

$$
\begin{aligned}
u(t,x)
={}&\mathbb E_{t,x}\left[
e^{\int_t^T V(r,X_r)\,dr}\phi(X_T)
\right]\\
&+\mathbb E_{t,x}\left[
\int_t^T e^{\int_t^s V(r,X_r)\,dr}g(s,X_s)\,ds
\right]
\end{aligned}
\tag{9}
$$

is finite. Under the additional regularity needed to identify a classical solution, Itô's formula verifies

$$
\partial_tu+\mathcal L_tu+Vu+g=0,
\qquad u(T,\cdot)=\phi.
$$

More general weak-diffusion and coefficient hypotheses are possible, but are not needed for the sufficient version recorded here.

## Relation to branching formulas

The formula above is linear in the unknown $u$. If the PDE contains nonlinear products of $u$ or its derivatives, one diffusion path does not directly represent those products. [Duhamel trees](branching-diffusions-and-duhamel-trees.md) and branching randomizations create descendants whose conditionally independent contributions multiply. That is an additional construction with its own integrability requirements, not part of the classical Feynman--Kac theorem.
