---
title: Besov spaces on the torus
status: definition
tags:
  - functional analysis
  - PDE
  - Besov space
  - Fourier analysis
  - regularity
---

# Besov spaces on the torus

Besov spaces measure regularity frequency scale by frequency scale. They include Holder spaces as an endpoint case but also allow scale contributions to be combined in \(L^p\) or \(\ell^q\) norms. This flexibility is useful when a random field is too irregular for a pathwise Holder norm but still has controlled frequency-localized moments.

**References.** Hajer Bahouri, Jean-Yves Chemin, and Raphaël Danchin, *Fourier Analysis and Nonlinear Partial Differential Equations*, Springer, 2011. Hans Triebel, *Theory of Function Spaces*, Birkhäuser, 1983. See [References](../meta/references.md).

Throughout, functions are defined on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\).

## Fourier coefficients and dyadic blocks

For a periodic distribution \(f\), write

$$
\widehat f(k)
=
\frac1{2\pi}
\int_0^{2\pi}f(x)e^{-ikx}\,dx,
\qquad k\in\mathbb Z,
$$

when the integral representation is available.

Choose smooth functions \(\chi,\varphi:\mathbb R\to[0,1]\) such that \(\chi\) is supported near the origin, \(\varphi\) is supported away from the origin, and

$$
\chi(\xi)
+
\sum_{j\geq0}\varphi(2^{-j}\xi)
=1
$$

for every \(\xi\in\mathbb R\). Define the dyadic Fourier blocks

$$
\Delta_{-1}f
=
\sum_{k\in\mathbb Z}
\chi(k)\widehat f(k)e^{ikx},
$$

and, for \(j\geq0\),

$$
\Delta_jf
=
\sum_{k\in\mathbb Z}
\varphi(2^{-j}k)\widehat f(k)e^{ikx}.
\tag{1}
$$

The block \(\Delta_jf\) contains frequencies of order \(2^j\).

## Definition

Let \(s\in\mathbb R\) and \(1\leq p,q\leq\infty\). The periodic Besov norm is

$$
\lVert f\rVert_{B^s_{p,q}}
=
\left\lVert
\left(
2^{js}\lVert\Delta_jf\rVert_{L^p}
\right)_{j\geq-1}
\right\rVert_{\ell^q}.
\tag{2}
$$

The Besov space \(B^s_{p,q}(\mathbb T)\) consists of periodic distributions with finite norm (2). Different smooth dyadic partitions give equivalent norms.

For \(q=\infty\), formula (2) means

$$
\lVert f\rVert_{B^s_{p,\infty}}
=
\sup_{j\geq-1}
2^{js}\lVert\Delta_jf\rVert_{L^p}.
$$

## Relation to Holder regularity

For noninteger \(0<\alpha<1\),

$$
B^\alpha_{\infty,\infty}(\mathbb T)
=
C^\alpha(\mathbb T)
$$

with equivalent norms. More generally, \(B^s_{\infty,\infty}\) is the Holder--Zygmund scale.

Thus replacing a spatial \(C^\alpha\) norm by \(B^\alpha_{\infty,\infty}\) does not weaken the regularity requirement. A genuinely different estimate uses other values of \(p\) or \(q\), or an integrated time norm.

## Heat-semigroup characterization

For \(0<s<2\), the Holder--Besov norm is equivalently characterized by heat-semigroup smoothing:

$$
\lVert f\rVert_{B^s_{\infty,\infty}}
\asymp
\lVert f\rVert_\infty
+
\sup_{0<r\leq1}
 r^{1-s/2}
\lVert\partial_x^2P_rf\rVert_\infty.
\tag{3}
$$

More generally, for finite \(q\), one replaces the supremum in (3) by an \(L^q(dr/r)\) norm. Formula (3) makes the connection with [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md) explicit: a positive regularity exponent compensates part of the \(r^{-1}\) Hessian singularity.

## Parabolic scaling

For space-time problems, the natural anisotropic scaling is

$$
x\mapsto Lx,
\qquad
t\mapsto L^2t.
$$

Parabolic Besov spaces implement this scaling in their dyadic decomposition. The full anisotropic construction is not needed elsewhere on this wiki yet; when such a norm is used in a theorem, its precise indices and time-space convention should be stated there.

## Why this may matter for branching fields

The random-patch problem requires a random regularity estimate, not merely a deterministic patch bound. A pathwise [parabolic Holder norm](parabolic-holder-spaces.md) may be too strong for a raw branching estimator because its genealogy can change discontinuously with the horizon. Besov norms offer alternative ways to measure the same short-scale oscillations, for example by combining frequency-localized random estimates in \(L^p(\Omega)\) or by integrating their scale dependence rather than taking a pathwise supremum.

No Besov estimate for the random patch field is currently proved. The [random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md) records this only as a possible function-space route.