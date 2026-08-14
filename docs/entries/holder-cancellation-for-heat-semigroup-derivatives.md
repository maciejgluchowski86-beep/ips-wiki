---
title: Holder cancellation for heat-semigroup derivatives
status: standard fact
tags:
  - PDE
  - heat semigroup
  - Holder space
  - Hermite polynomial
  - commutator
---

# Holder cancellation for heat-semigroup derivatives

A heat-semigroup derivative has a singular short-time kernel, but every positive-order Hermite weight has mean zero. Subtracting a constant therefore converts spatial Holder regularity into a positive power of the edge length. The same cancellation controls commutators between heat-semigroup derivatives and spatial multiplication operators.

**References.** The Gaussian derivative formula and Hermite normalization are recorded in [Gaussian integration by parts and automatic differentiation](gaussian-integration-by-parts-and-automatic-differentiation.md) and [Hermite polynomials and Gaussian chaos](hermite-polynomials-and-gaussian-chaos.md). The estimates below are standard consequences of those formulas.

Fix \(0<\alpha<1\). Let \(Z\sim N(0,1)\), let \(P_r\) be the heat semigroup on \(\mathbb R\) or \(\mathbb T\), and write

$$
K_r^{(k)}
=
\partial_x^{2k}P_r,
\qquad k\geq1.
$$

## Mean-zero Hermite cancellation

The probabilists' Hermite polynomials satisfy

$$
\mathbb E[He_n(Z)]=0,
\qquad n\geq1,
\tag{1}
$$

because \(He_n\) is orthogonal in Gaussian \(L^2\) to the constant polynomial \(He_0=1\). Hence the heat-derivative formula may be written as

$$
K_r^{(k)}f(x)
=
r^{-k}
\mathbb E\left[
He_{2k}(Z)
\bigl(f(x+\sqrt r\,Z)-f(x)\bigr)
\right].
\tag{2}
$$

For \(k=1\), this is

$$
\partial_x^2P_rf(x)
=
\frac1r
\mathbb E\left[
(Z^2-1)
\bigl(f(x+\sqrt r\,Z)-f(x)\bigr)
\right].
\tag{3}
$$

Thus the subtraction in (2)--(3) is licensed exactly by the zero mean in (1).

## Holder gain

If \(f\in C^\alpha\), then

$$
|f(x+\sqrt r\,Z)-f(x)|
\leq
[f]_{C^\alpha}r^{\alpha/2}|Z|^\alpha.
$$

Define

$$
c_{2k,\alpha}
=
\mathbb E\left[
|He_{2k}(Z)|\,|Z|^\alpha
\right].
\tag{4}
$$

Equation (2) gives

$$
\lVert K_r^{(k)}f\rVert_\infty
\leq
c_{2k,\alpha}
 r^{-k+\alpha/2}
[f]_{C^\alpha}.
\tag{5}
$$

In particular,

$$
\lVert\partial_x^2P_rf\rVert_\infty
\leq
c_{2,\alpha}
 r^{-1+\alpha/2}
[f]_{C^\alpha},
$$

where

$$
c_{2,\alpha}
=
\mathbb E\left[
|Z^2-1|\,|Z|^\alpha
\right].
\tag{6}
$$

By Cauchy--Schwarz and Hermite orthogonality,

$$
\begin{aligned}
c_{2k,\alpha}
&\leq
\left(\mathbb E He_{2k}(Z)^2\right)^{1/2}
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2}\\
&=
\sqrt{(2k)!}\,
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2}.
\end{aligned}
\tag{7}
$$

The Gaussian moment in (7) depends only on \(\alpha\).

## Multiplication commutator

For a bounded function \(B\), let \(M_Bg=Bg\). The commutator is

$$
[K_R^{(k)},M_B]
=
K_R^{(k)}M_B-M_BK_R^{(k)}.
$$

Using the same Gaussian in both terms gives the exact identity

$$
\begin{aligned}
[K_R^{(k)},M_B]g(x)
={}&R^{-k}
\mathbb E\Bigl[
He_{2k}(Z)
\bigl(B(x+\sqrt R\,Z)-B(x)\bigr)\\
&\hspace{39mm}\times g(x+\sqrt R\,Z)
\Bigr].
\end{aligned}
\tag{8}
$$

Consequently,

$$
\lVert[K_R^{(k)},M_B]g\rVert_\infty
\leq
c_{2k,\alpha}
R^{-k+\alpha/2}
[B]_{C^\alpha}
\lVert g\rVert_\infty.
\tag{9}
$$

This estimate requires one Holder increment of \(B\), regardless of the derivative order \(2k\).

## Cluster time factor

Suppose \(k\) consecutive second-derivative heat edges have lengths \(r_1,\ldots,r_k>0\) and total length

$$
R=r_1+\cdots+r_k.
$$

Because heat derivatives commute with the heat semigroup,

$$
K_{r_k}^{(1)}\cdots K_{r_1}^{(1)}
=
K_R^{(k)}.
\tag{10}
$$

For fixed \(R\), the simplex of positive \((r_1,\ldots,r_k)\) with this sum has volume

$$
\frac{R^{k-1}}{(k-1)!}.
\tag{11}
$$

Combining (5) or (9) with (11) leaves the integrable singularity

$$
\frac{c_{2k,\alpha}}{(k-1)!}
R^{-1+\alpha/2}.
\tag{12}
$$

The coefficient in (12) grows at most geometrically in \(k\). Indeed, by (7),

$$
\frac{c_{2k,\alpha}}{(k-1)!}
\leq
C_\alpha\,
 k\sqrt{\binom{2k}{k}}
\leq
C_\alpha\,k2^k
\leq
C_\alpha4^k.
\tag{13}
$$

Thus composing a derivative cluster before taking absolute values removes the factorial edge-by-edge scale. What remains in a spatially varying patch is the problem of controlling the Holder norms of the multipliers at the cluster boundaries.

For time-dependent multipliers \(B(s,\cdot)\), estimates (8)--(13) are applied at each fixed sampled time \(s\). Uniform spatial \(C^\alpha\) control in time is sufficient; full [parabolic Holder regularity](parabolic-holder-spaces.md) is stronger than this local requirement.