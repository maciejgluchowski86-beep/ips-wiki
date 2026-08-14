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

A second-order parabolic operator can be realized as the generator of a diffusion. For equations without a zeroth-order potential, the resulting Feynman--Kac formula is simply the backward Kolmogorov representation: evaluate the initial or terminal datum along the diffusion and take expectation.

**References.** Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, second edition, Springer, 1991, especially the chapters on stochastic integration, Brownian motion and PDEs, and stochastic differential equations. Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes*, Springer, 2006 reprint. See [References](../meta/references.md).

Throughout, coefficients on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) are identified with periodic coefficients on \(\mathbb R\).

## Itô diffusion

Let \(W\) be a standard Brownian motion and consider

$$
dX_s
=
b(s,X_s)\,ds
+\sigma(s,X_s)\,dW_s,
\qquad
X_0=x.
\tag{1}
$$

A *weak solution* consists of a probability space carrying \((X,W)\) on which the integral form of (1) holds. Uniqueness in law means that the distribution of \(X\) is uniquely determined by the coefficients and the starting point, even if different probability spaces are used.

If \(\sigma\) is Lipschitz in space, the usual strong existence and pathwise-uniqueness theorem gives a stronger formulation in which \(X\) is constructed as a measurable functional of a prescribed Brownian motion. The discussion below only needs the weaker diffusion law.

## Generator and martingale problem

For a smooth test function \(f\), define

$$
L_sf(x)
=
b(s,x)f'(x)
+\frac12\sigma(s,x)^2f''(x).
\tag{2}
$$

A continuous process \(X\) solves the *martingale problem* for \((L_s)\) started from \(x\) if \(X_0=x\) and, for every smooth periodic test function \(f\),

$$
M_t^f
:=
f(X_t)-f(X_0)
-
\int_0^tL_sf(X_s)\,ds
\tag{3}
$$

is a martingale.

The martingale problem characterizes the diffusion law without specifying a Brownian motion on the underlying probability space. Existence and uniqueness for the martingale problem are therefore a convenient route to weak existence and uniqueness in law for (1).

For the one-dimensional periodic setting used here, bounded Hölder coefficients together with uniform nondegeneracy

$$
0<c\leq |\sigma(s,x)|\leq C<\infty
\tag{4}
$$

are sufficient for the weak diffusion law needed below. The representation theorem uses only that law, not pathwise uniqueness.

## Itô's formula

If \(F\in C^{1,2}\), then along a weak solution of (1),

$$
\begin{aligned}
dF(s,X_s)
={}&
\left(
F_s+bF_x+\frac12\sigma^2F_{xx}
\right)(s,X_s)\,ds\\
&+
\sigma(s,X_s)F_x(s,X_s)\,dW_s.
\end{aligned}
\tag{5}
$$

Thus the operator in (2) is the infinitesimal generator of the diffusion.

## Backward Kolmogorov representation

Let \(a:[0,t]\times\mathbb T\to(0,\infty)\) be continuous and uniformly elliptic, and suppose \(v\in C^{1,2}\) solves

$$
\partial_rv(r,x)
=
a(r,x)\partial_x^2v(r,x),
\qquad
v(0,x)=\phi(x).
\tag{6}
$$

For this fixed observation time \(t\), let \(X\) have the diffusion law with time-reversed generator

$$
a(t-s,x)\partial_x^2.
$$

Equivalently, on a probability space carrying a suitable weak solution, one may write

$$
dX_s
=
\sqrt{2a(t-s,X_s)}\,dW_s,
\qquad
X_0=x,
\qquad
0\leq s\leq t.
\tag{7}
$$

Then

$$
v(t,x)
=
\mathbb E_x[\phi(X_t)].
\tag{8}
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

which vanishes by (6). Hence \(v(t-s,X_s)\) is a local martingale. On the compact torus, the derivatives of the classical solution are bounded, so the stochastic integral is a true martingale on the finite interval. Therefore

$$
v(t,x)
=
\mathbb E_x[v(0,X_t)]
=
\mathbb E_x[\phi(X_t)].
$$

The time reversal in (7) is important: equation (6) evolves the initial datum from time \(0\) to time \(t\), while the stochastic path in (8) starts at the observation point \((t,x)\) and follows the coefficient backward through the deterministic time profile.

## Relation to branching representations

Formula (8) contains no branching. Once a nonlinear problem has been reduced to a linear equation with a self-consistent deterministic coefficient, the diffusion itself gives an integrable representation whenever the payoff is bounded. This is logically different from constructing an infinite random branching estimator from the original Duhamel series.
