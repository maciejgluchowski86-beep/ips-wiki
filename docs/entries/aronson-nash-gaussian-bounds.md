---
title: Aronson and Nash Gaussian bounds
status: literature
audit: current
tags:
  - PDE
  - parabolic equation
  - heat kernel
  - Aronson bound
  - Nash estimate
---

# Aronson and Nash Gaussian bounds

Gaussian kernel estimates compare the fundamental solution of a uniformly parabolic equation with the ordinary heat kernel. Classical Aronson estimates include divergence-form equations with bounded measurable leading coefficients under the corresponding structural hypotheses. For nondivergence equations and their adjoints, pointwise Gaussian bounds require theorem-specific assumptions; one must not transfer a divergence-form result by analogy alone.

**References.** Donald G. Aronson, *Bounds for the fundamental solution of a parabolic equation*, *Bulletin of the American Mathematical Society* **73** (1967), 890--896. Donald G. Aronson, *Gaussian estimates: a brief history*, arXiv:1707.04620. Hongjie Dong, Seick Kim, and Sungjin Lee, *Estimates for fundamental solutions of parabolic equations in non-divergence form*, *Journal of Differential Equations* **340** (2022), 557--591, arXiv:2201.03811. See [References](../meta/references.md).

## Fundamental solutions

A fundamental solution or transition kernel \(p(s,x;t,y)\) for a forward parabolic equation is a kernel such that, for suitable initial data \(h\),

$$
u(t,y)
=
\int p(s,x;t,y)h(x)\,dx
$$

solves the equation for \(t>s\). For the heat equation in \(d\) dimensions,

$$
p_0(s,x;t,y)
=
\frac{1}{(2\pi(t-s))^{d/2}}
\exp\left(-\frac{|y-x|^2}{2(t-s)}\right).
$$

## Classical Aronson bounds

For uniformly parabolic divergence-form operators with bounded measurable leading coefficients and lower-order terms satisfying the structural assumptions of the theorem, the fundamental solution satisfies two-sided Gaussian estimates of the schematic form

$$
\frac{c_1}{(t-s)^{d/2}}
\exp\left(-c_2\frac{|x-y|^2}{t-s}\right)
\leq
p(s,x;t,y)
\leq
\frac{C_1}{(t-s)^{d/2}}
\exp\left(-C_2\frac{|x-y|^2}{t-s}\right),
\tag{1}
$$

where the constants depend on dimension, ellipticity, and the structural bounds of the equation. These are usually called **Aronson bounds**. Nash's regularity argument is an important historical precursor; Aronson's 1967--1968 work established Gaussian estimates for a broad class of linear parabolic equations under minimal regularity assumptions.

A one-dimensional example of the divergence-form class is

$$
\partial_tu
=
\partial_x(a(t,x)\partial_xu),
\qquad
0<\kappa\leq a\leq K.
\tag{2}
$$

## Nondivergence form is different

The equation

$$
\partial_tv
=
a(t,x)\partial_x^2v
\tag{3}
$$

is in nondivergence form. Its formal adjoint density equation is

$$
\partial_t\rho
=
\partial_x^2(a(t,x)\rho).
\tag{4}
$$

Equations (2), (3), and (4) are different operators when \(a\) depends on space. In particular,

$$
\partial_x(a\partial_xu)
\neq
 a\partial_x^2u
$$

unless the additional derivative term vanishes.

The measurable-coefficient divergence-form theory therefore does not automatically imply a pointwise Gaussian estimate for (3)--(4). Dong--Kim--Lee construct fundamental solutions for nondivergence equations when the coefficients have Dini mean oscillation in the spatial variables and prove sub-Gaussian estimates; under Dini continuity in space and measurability in time they obtain Gaussian bounds. The point is structural: the assumptions for a kernel theorem must be checked for the operator actually under consideration.

## Operator-norm caution

For a Markov transition operator associated with the direct equation (3), positivity and preservation of constants give

$$
\lVert S(t,s)h\rVert_\infty
\leq
\lVert h\rVert_\infty.
$$

The adjoint operator acts naturally on densities or measures. It need not be an \(L^\infty\)-contraction, because the direct evolution need not preserve Lebesgue measure. A bound

$$
\lVert S^*(t,s)h\rVert_\infty
\leq C\lVert h\rVert_\infty
$$

therefore requires an actual kernel or regularity estimate in the relevant operator class; it is not a consequence of uniform ellipticity alone. This direct-versus-adjoint distinction should be checked before importing a Gaussian or \(L^\infty\) estimate into a parabolic argument.
