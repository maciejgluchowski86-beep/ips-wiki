---
title: Parabolic Holder spaces
status: standard fact
audit: current
tags:
  - PDE
  - Holder space
  - parabolic regularity
  - heat equation
---

# Parabolic Holder spaces

Parabolic equations scale one time derivative like two spatial derivatives. The corresponding Holder spaces therefore measure spatial increments with exponent \(\alpha\) and time increments with exponent \(\alpha/2\). This is the regularity scale used by classical parabolic Schauder theory.

**References.** Avner Friedman, *Partial Differential Equations of Parabolic Type*, Prentice-Hall, 1964. Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010. See [References](../meta/references.md).

Throughout, \(0<\alpha<1\) and \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Distances on \(\mathbb T\) are shortest periodic distances.

## Spatial Holder norm

For \(f:\mathbb T\to\mathbb R\), define

$$
[f]_{C^\alpha(\mathbb T)}
=
\sup_{x\neq y}
\frac{|f(x)-f(y)|}{|x-y|^\alpha},
$$

and

$$
\lVert f\rVert_{C^\alpha}
=
\lVert f\rVert_\infty+[f]_{C^\alpha}.
\tag{1}
$$

The product estimate

$$
[fg]_{C^\alpha}
\leq
\lVert f\rVert_\infty[g]_{C^\alpha}
+
\lVert g\rVert_\infty[f]_{C^\alpha}
\tag{2}
$$

shows that \(C^\alpha(\mathbb T)\) is an algebra.

## Parabolic Holder norm

For a function \(u=u(t,x)\) on \([0,T]\times\mathbb T\), define

$$
[u]_{C^{\alpha/2,\alpha}}
=
\sup_{(t,x)\neq(s,y)}
\frac{|u(t,x)-u(s,y)|}
{|t-s|^{\alpha/2}+|x-y|^\alpha}.
\tag{3}
$$

The norm is

$$
\lVert u\rVert_{C^{\alpha/2,\alpha}}
=
\lVert u\rVert_\infty
+[u]_{C^{\alpha/2,\alpha}}.
\tag{4}
$$

Equivalent definitions use the parabolic metric

$$
d_{\mathrm p}((t,x),(s,y))
=|t-s|^{1/2}+|x-y|
$$

and the denominator \(d_{\mathrm p}^\alpha\). On a fixed compact cylinder these conventions give equivalent norms.

The parabolic norm controls the spatial Holder norm uniformly in time:

$$
\sup_{0\leq t\leq T}
[u(t,\cdot)]_{C^\alpha}
\leq
[u]_{C^{\alpha/2,\alpha}}.
\tag{5}
$$

The converse is false without a separate time-regularity estimate.

## Heat-semigroup contraction

Let \(P_r\) be the heat semigroup on \(\mathbb T\). Coupling the two values with the same Brownian increment gives

$$
|P_rf(x)-P_rf(y)|
\leq
\mathbb E|f(x+B_r)-f(y+B_r)|
\leq
[f]_{C^\alpha}|x-y|^\alpha.
$$

Therefore

$$
[P_rf]_{C^\alpha}
\leq
[f]_{C^\alpha},
\qquad
\lVert P_rf\rVert_{C^\alpha}
\leq
\lVert f\rVert_{C^\alpha}.
\tag{6}
$$

This is a spatial statement. No time Holder regularity is asserted merely by applying one fixed heat-semigroup operator.

## Parabolic scaling of oscillatory packets

For an integer \(N\geq1\),

$$
[\cos(Nx)]_{C^\alpha}
\asymp
N^\alpha,
\tag{7}
$$

with constants depending only on \(\alpha\). For the lower bound, compare \(x=0\) and \(y=\pi/N\). For the upper bound, use

$$
|\cos(Nx)-\cos(Ny)|
\leq
\min\{2,N|x-y|\}.
$$

Let \(\chi\in C_c^\infty(\mathbb R)\), assume that \(\chi(\tau_0)\neq0\) for some \(\tau_0\geq0\), and fix \(T>0\). For all sufficiently large \(N\), so that \(\tau_0/N^2\leq T\), the parabolically scaled packet

$$
u_N(t,x)
=
\chi(N^2t)\cos(Nx),
\qquad
0\leq t\leq T,
\tag{8}
$$

satisfies

$$
\lVert u_N\rVert_{C^{\alpha/2,\alpha}([0,T]\times\mathbb T)}
\asymp
N^\alpha,
$$

with constants depending on \(\alpha\), \(\chi\), and the chosen nonzero value of \(\chi\). The spatial lower bound follows by evaluating at the time \(t=\tau_0/N^2\) and using (7). For the time part, the scaling identity

$$
|N^2(t-s)|^{\alpha/2}
=
N^\alpha|t-s|^{\alpha/2}
$$

and the smooth compact support of \(\chi\) give the matching upper bound. Thus high spatial frequencies localized to time intervals of length \(N^{-2}\) naturally carry parabolic Holder size of order \(N^\alpha\).

## Relation to parabolic regularity

The coefficient and forcing classes in [Parabolic maximum principle and Schauder estimates](parabolic-maximum-principle-and-schauder-estimates.md) are measured in parabolic Holder norms. The heat equation and its perturbations respect the scaling $t\sim x^2$, so frequency localization in space and localization on the corresponding $N^{-2}$ time scale contribute at the same Holder order. Uniform spatial Holder control alone is weaker because it contains no information about temporal increments.
