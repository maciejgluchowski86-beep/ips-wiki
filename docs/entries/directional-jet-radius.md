---
title: Directional jet radius
status: definition
audit: current
tags:
  - PDE
  - analytic function
  - jet
  - Gevrey class
  - entire function
---

# Directional jet radius

For a smooth or analytic function of several jet variables, a directional jet radius is simply the one-variable Taylor radius obtained by varying one coordinate and holding the others fixed. It is useful when repeated derivatives in one jet coordinate must be controlled separately from the remaining variables.

**References.** The jet notation used in the PDE applications is described in [Spatial jets, total derivatives, and Faà di Bruno](spatial-jets-total-derivative-and-faa-di-bruno.md). The radius, even/odd decomposition, Cauchy estimates, and entire-function growth statements below are standard one-variable complex analysis.

Fix $f:\mathbb C^{n+1}\to\mathbb C$ near a point $z=(z_0,\ldots,z_n)$ and a coordinate $j\in\{0,\ldots,n\}$. Let $e_j$ be the $j$-th coordinate vector and define

$$
g_{z,j}(w)=f(z+w e_j).
\tag{1}
$$

If $g_{z,j}$ is analytic near $0$, write

$$
g_{z,j}(w)=\sum_{m=0}^\infty a_m(z,j)w^m,
\qquad
a_m(z,j)=\frac{\partial_{z_j}^m f(z)}{m!}.
\tag{2}
$$

## Directional radius

The directional jet radius at $(z,j)$ is

$$
R_j(z)
=
\left(\limsup_{m\to\infty}|a_m(z,j)|^{1/m}\right)^{-1},
\tag{3}
$$

with $1/0=\infty$ and $1/\infty=0$. This is exactly the radius of convergence of the one-variable Taylor series (2). If $f$ is merely smooth, (3) still defines the radius of its formal directional Taylor series, but the series need not represent the original smooth germ.

## Even and odd radii

Define

$$
R_j^{\mathrm{even}}(z)
=
\left(\limsup_{k\to\infty}|a_{2k}(z,j)|^{1/(2k)}\right)^{-1},
$$

and

$$
R_j^{\mathrm{odd}}(z)
=
\left(\limsup_{k\to\infty}|a_{2k+1}(z,j)|^{1/(2k+1)}\right)^{-1}.
$$

These are the radii, in the original variable $w$, of the even and odd parts

$$
\frac{g_{z,j}(w)+g_{z,j}(-w)}{2},
\qquad
\frac{g_{z,j}(w)-g_{z,j}(-w)}{2}.
$$

Since the limsup over all coefficients is the maximum of the two subsequential limsups,

$$
R_j(z)=\min\{R_j^{\mathrm{even}}(z),R_j^{\mathrm{odd}}(z)\}.
\tag{4}
$$

## Ultra-analytic derivative growth

A directional germ satisfies the derivative bound sometimes called Gevrey-$1/2$ or ultra-analytic growth if there are constants $C,A<\infty$ such that

$$
|\partial_{z_j}^m f(z)|\le C A^m\sqrt{m!},
\qquad m\ge0.
\tag{5}
$$

Equivalently,

$$
|a_m(z,j)|\le \frac{C A^m}{\sqrt{m!}}.
\tag{6}
$$

Some authors reserve the word *Gevrey* for orders at least one; (5) is the convention meant here.

The bound (5) implies that (2) extends to an entire function of $w$. More precisely, after changing constants,

$$
|g_{z,j}(w)|\le C'\exp(B|w|^2),
\qquad w\in\mathbb C.
\tag{7}
$$

Conversely, an entire function satisfying (7) obeys (5). For the forward implication, (6) makes the power series entire and the standard estimate for $\sum_m r^m/\sqrt{m!}$ gives Gaussian-exponential growth. For the reverse implication, Cauchy's estimate on $|w|=r$ gives

$$
|g_{z,j}^{(m)}(0)|
\le m!\,C'\frac{e^{Br^2}}{r^m}.
$$

Choosing $r^2=m/(2B)$ and using Stirling's formula yields (5).

For a nonconstant entire function $g$, let

$$
M_g(r)=\max_{|w|=r}|g(w)|,
\qquad
\rho(g)=\limsup_{r\to\infty}\frac{\log\log M_g(r)}{\log r}.
$$

If $0<\rho(g)<\infty$, its type is

$$
\sigma(g)=\limsup_{r\to\infty}\frac{\log M_g(r)}{r^{\rho(g)}}.
$$

Thus (7) gives order at most $2$, and finite type when the order is exactly $2$. This is different from *exponential type*, which conventionally concerns order $1$.

## Example

For

$$
f(z)=\frac{\eta}{1+z_j^2}
$$

at a point with $z_j=a\in\mathbb R$, the directional function is

$$
g_{z,j}(w)=\frac{\eta}{1+(a+w)^2}.
$$

Its nearest complex poles are at $-a\pm i$, so

$$
R_j(z)=\sqrt{a^2+1}.
$$

At $a=0$ the germ is even, hence $R_j^{\mathrm{even}}(z)=1$ and $R_j^{\mathrm{odd}}(z)=\infty$.

In a jet-dependent PDE one may specialize $z$ to a jet such as $J_n\phi(y)$, but the definition and the one-variable facts above do not depend on any particular branching representation or PDE programme.