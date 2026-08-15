---
title: Itô diffusions and the backward Kolmogorov representation
status: standard fact
audit: current
tags:
  - probability
  - stochastic calculus
  - diffusion
  - PDE
  - Feynman-Kac formula
---

# Itô diffusions and the backward Kolmogorov representation

A second-order parabolic operator can be realized as the generator of a diffusion. For equations without a zeroth-order potential, the resulting Feynman--Kac formula is the backward Kolmogorov representation: evaluate the initial or terminal datum along the diffusion and take expectation.

**Background.** The constant-coefficient model is [Heat equation and Gaussian heat kernel](heat-equation-and-gaussian-heat-kernel.md).

**References.** Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991. The strong SDE existence theorem used below is Theorem 5.2.9 in §5.2; the connection between diffusions and parabolic PDEs is developed in §5.7. See [References](../meta/references.md).

Throughout, coefficients on $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ are identified with periodic coefficients on $\mathbb R$.

## Itô diffusion

Let $W$ be a standard Brownian motion and consider

$$
dX_s
=b(s,X_s)\,ds
+\sigma(s,X_s)\,dW_s,
\qquad
X_0=x.
\tag{1}
$$

A *weak solution* consists of a probability space carrying $(X,W)$ on which the integral form of (1) holds. Uniqueness in law means that the distribution of $X$ is uniquely determined by the coefficients and the starting point, even if different probability spaces are used.

For a clean sufficient existence hypothesis, assume that $b$ and $\sigma$ are continuous, globally Lipschitz in the spatial variable with one common constant, and satisfy a linear-growth bound

$$
|b(s,x)|+|\sigma(s,x)|
\leq C(1+|x|)
\tag{2}
$$

uniformly in $s$ on the finite time interval. Karatzas--Shreve, Theorem 5.2.9, then gives a unique strong solution and hence a uniquely determined diffusion law. Bounded periodic Lipschitz coefficients are a special case. This page uses that sufficient regime rather than a broader weak-existence assertion for merely Hölder coefficients.

## Generator and martingale problem

For a smooth test function $f$, define

$$
L_sf(x)
=b(s,x)f'(x)
+\frac12\sigma(s,x)^2f''(x).
\tag{3}
$$

A continuous process $X$ solves the *martingale problem* for $(L_s)$ started from $x$ if $X_0=x$ and, for every smooth periodic test function $f$,

$$
M_t^f
:=f(X_t)-f(X_0)
-\int_0^tL_sf(X_s)\,ds
\tag{4}
$$

is a martingale.

The martingale-problem formulation characterizes the diffusion law without specifying a Brownian motion on the underlying probability space. In the Lipschitz regime above, the strong solution of (1) supplies the law needed below, so no additional weak-SDE theorem is required here.

## Itô's formula

If $F\in C^{1,2}$, then along the solution of (1),

$$
\begin{aligned}
dF(s,X_s)
={}&
\left(
F_s+bF_x+\frac12\sigma^2F_{xx}
\right)(s,X_s)\,ds\\
&+\sigma(s,X_s)F_x(s,X_s)\,dW_s.
\end{aligned}
\tag{5}
$$

Thus the operator in (3) is the infinitesimal generator of the diffusion.

## Backward Kolmogorov representation

Let $a:[0,t]\times\mathbb T\to(0,\infty)$ be continuous, uniformly elliptic, and uniformly Lipschitz in the spatial variable: for some $0<\kappa\leq K<\infty$ and $L<\infty$,

$$
\kappa\leq a(r,x)\leq K,
\qquad
|a(r,x)-a(r,y)|\leq L|x-y|
\tag{6}
$$

for all $r,x,y$, using periodic distance in the last inequality. Then $\sigma(r,x)=\sqrt{2a(r,x)}$ is bounded and uniformly Lipschitz in $x$, so Theorem 5.2.9 supplies a unique strong solution to the time-reversed SDE below.

Suppose $v\in C^{1,2}$ solves

$$
\partial_rv(r,x)
=a(r,x)\partial_x^2v(r,x),
\qquad
v(0,x)=\phi(x).
\tag{7}
$$

For this fixed observation time $t$, let

$$
dX_s
=\sqrt{2a(t-s,X_s)}\,dW_s,
\qquad
X_0=x,
\qquad
0\leq s\leq t.
\tag{8}
$$

Then

$$
v(t,x)
=\mathbb E_x[\phi(X_t)].
\tag{9}
$$

## Proof

Apply Itô's formula to

$$
F(s,y)=v(t-s,y).
$$

The drift in (5) is

$$
-v_t(t-s,X_s)
+a(t-s,X_s)v_{xx}(t-s,X_s),
$$

which vanishes by (7). On the compact torus, the derivatives of the classical solution are bounded, so the stochastic integral is square-integrable on the finite interval and hence a true martingale. Therefore

$$
v(t,x)
=\mathbb E_x[v(0,X_t)]
=\mathbb E_x[\phi(X_t)].
$$

The time reversal in (8) is important: equation (7) evolves the initial datum from time $0$ to time $t$, while the stochastic path in (9) starts at the observation point $(t,x)$ and follows the coefficient backward through the deterministic time profile.

## Relation to branching representations

Formula (9) contains no branching. Once a nonlinear problem has been reduced to a linear equation with a self-consistent deterministic coefficient, the diffusion itself gives an integrable representation whenever the payoff is bounded. This is logically different from constructing an infinite random branching estimator from the original Duhamel series.
