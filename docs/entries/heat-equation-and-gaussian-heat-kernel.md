---
title: Heat equation and Gaussian heat kernel
status: standard fact
audit: current
tags:
  - PDE
  - heat equation
  - heat kernel
  - Gaussian kernel
  - torus
---

# Heat equation and Gaussian heat kernel

The heat equation is the model linear parabolic PDE. This entry fixes the normalization used by the probability-facing part of the wiki and records the elementary Gaussian-kernel facts needed later. Brownian interpretation and abstract semigroup/generator theory are deliberately left to later entries in the [PDE reading path](../pde-reading-path.md).

**References.** Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, §2.3 (the heat equation). For the one-dimensional heat equation in probabilistic normalization, see Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991, §4.3. See [References](../meta/references.md).

## Normalization on Euclidean space

Throughout this entry the default heat equation on $\mathbb R^d$ is

$$
\partial_tu
=\frac12\Delta u,
\qquad t>0,
$$

where $\Delta=\sum_{j=1}^d\partial_{jj}$. Its Gaussian kernel is

$$
p_t(x)
=(2\pi t)^{-d/2}
\exp\left(-\frac{|x|^2}{2t}\right),
\qquad t>0,
\quad x\in\mathbb R^d.
\tag{1}
$$

For a function $f$ for which the convolution is defined, write

$$
P_tf(x)
=(p_t*f)(x)
=\int_{\mathbb R^d}p_t(x-y)f(y)\,dy.
\tag{2}
$$

This notation is used later for the heat operators; no abstract semigroup theory is needed here.

## Positivity, mass, and convolution

The kernel in (1) is strictly positive. Gaussian integration gives

$$
\int_{\mathbb R^d}p_t(x)\,dx=1.
\tag{3}
$$

For $s,t>0$,

$$
p_s*p_t=p_{s+t}.
\tag{4}
$$

One way to verify (4) is to complete the square in the convolution integral. Equivalently, the Fourier transform of $p_t$ is $e^{-t|\xi|^2/2}$, so multiplication of the transforms gives the parameter $s+t$.

Equations (3)--(4) imply $P_sP_tf=P_{s+t}f$ whenever the displayed convolutions are defined, but the operator-theoretic consequences are postponed to the later heat-semigroup entry.

## Approximate identity

The family $(p_t)_{t>0}$ is an approximate identity as $t\downarrow0$.

If $f:\mathbb R^d\to\mathbb R$ is bounded and uniformly continuous, then

$$
\|P_tf-f\|_\infty\longrightarrow0.
\tag{5}
$$

Indeed,

$$
|P_tf(x)-f(x)|
\leq
\int p_t(y)|f(x-y)-f(x)|\,dy,
$$

and one splits the integral into $|y|<\delta$ and $|y|\geq\delta$: uniform continuity controls the first part uniformly in $x$, while the Gaussian tail of the second tends to zero as $t\downarrow0$.

If $1\leq p<\infty$ and $f\in L^p(\mathbb R^d)$, then

$$
\|P_tf-f\|_{L^p}\longrightarrow0.
\tag{6}
$$

This is the standard $L^p$ approximate-identity theorem, using translation continuity in $L^p$ and the unit mass in (3).

## Solving the heat equation for positive time

Let $f\in L^\infty(\mathbb R^d)$ and set $u(t,x)=P_tf(x)$. For every $t_0>0$, all spatial derivatives of $p_t$ and $\partial_t p_t$ are integrable in $x$, uniformly for $t$ in compact subintervals of $[t_0,\infty)$. Hence differentiation under the integral in (2) is justified on such intervals by dominated convergence. Since direct differentiation of (1) gives

$$
\partial_tp_t=\frac12\Delta p_t,
\tag{7}
$$

we obtain

$$
\partial_tu(t,x)=\frac12\Delta u(t,x),
\qquad t>0.
\tag{8}
$$

Thus bounded measurable data produce a smooth classical solution for every positive time. If the datum is bounded and uniformly continuous, (5) also gives the initial condition uniformly. If $f\in L^p$, $1\leq p<\infty$, equation (6) gives the initial condition in $L^p$.

## Alternative normalization

Many PDE texts instead write

$$
\partial_tu=\Delta u.
$$

The corresponding kernel is

$$
\widetilde p_t(x)
=(4\pi t)^{-d/2}
\exp\left(-\frac{|x|^2}{4t}\right).
\tag{9}
$$

This is the same family after the time rescaling $\widetilde p_t=p_{2t}$. Every formula above therefore remains valid after making this normalization change consistently.

## Periodization on the torus

Let

$$
\mathbb T^d
=\mathbb R^d/(2\pi\mathbb Z)^d.
$$

The heat kernel for $\partial_tu=\frac12\Delta u$ on $\mathbb T^d$ is obtained by periodizing the Euclidean kernel:

$$
p_t^{\mathbb T^d}(x)
=
\sum_{k\in\mathbb Z^d}p_t(x+2\pi k).
\tag{10}
$$

For every $t>0$ the series and all of its spatial derivatives converge locally uniformly on $\mathbb R^d$. The result is $2\pi\mathbb Z^d$-periodic, strictly positive, has unit mass on one fundamental domain, and satisfies the same convolution identity with torus convolution. Thus

$$
P_t^{\mathbb T^d}f(x)
=\int_{\mathbb T^d}p_t^{\mathbb T^d}(x-y)f(y)\,dy
$$

solves the periodic heat equation for positive time under the same bounded-data differentiation argument.

## Reader check

After this entry, a reader should be able to:

- fix the convention $\partial_tu=\frac12\Delta u$ and write $p_t(x)=(2\pi t)^{-d/2}e^{-|x|^2/(2t)}$;
- explain why $\partial_tu=\Delta u$ instead uses $(4\pi t)^{-d/2}e^{-|x|^2/(4t)}$;
- verify positivity, unit mass, and $p_s*p_t=p_{s+t}$;
- define $P_tf=p_t*f$;
- state uniform convergence $P_tf\to f$ for bounded uniformly continuous $f$ and $L^p$ convergence for $1\leq p<\infty$;
- justify, under the hypotheses above, differentiation of the Gaussian kernel under the integral and hence the heat equation for $t>0$;
- construct the kernel on $\mathbb T^d=\mathbb R^d/(2\pi\mathbb Z)^d$ by periodization.
