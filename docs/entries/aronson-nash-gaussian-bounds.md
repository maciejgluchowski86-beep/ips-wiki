---
title: Aronson and Nash Gaussian bounds
status: literature
tags:
  - PDE
  - parabolic equation
  - heat kernel
  - Aronson bound
  - Nash estimate
---

# Aronson and Nash Gaussian bounds

Gaussian kernel estimates compare the fundamental solution of a uniformly parabolic equation with the ordinary heat kernel. The classical measurable-coefficient Aronson theory applies to divergence-form equations. For nondivergence equations and their adjoints, pointwise Gaussian bounds require additional structure or regularity; one must not transfer the divergence-form theorem by analogy alone.

**References.** Donald G. Aronson, *Bounds for the fundamental solution of a parabolic equation*, *Bulletin of the American Mathematical Society* **73** (1967), 890--896. Hongjie Dong, Seick Kim, and Sungjin Lee, *Estimates for fundamental solutions of parabolic equations in non-divergence form*, *Journal of Differential Equations* **340** (2022), 557--591, arXiv:2201.03811. See [References](../meta/references.md).

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

For uniformly elliptic divergence-form equations with bounded measurable coefficients, the fundamental solution satisfies two-sided Gaussian estimates of the schematic form

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

where the constants depend on dimension, ellipticity, and the structural bounds of the equation. These are usually called *Aronson bounds*. Nash's regularity ideas are one of the historical ingredients behind this theory.

A one-dimensional example of the divergence-form class is

$$
\partial_tu
=
\partial_x(a(t,x)\partial_xu),
\qquad
0<\kappa\leq a\leq K.
\tag{2}
$$

For periodic coefficients or equations on the torus, corresponding periodic kernels can be obtained by periodicization or by compact-manifold parabolic theory under the applicable hypotheses.

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

unless the derivative of \(a\) is absent or vanishes.

The measurable-coefficient Aronson theorem for (2) therefore does not automatically imply a pointwise Gaussian estimate, or a uniform \(L^\infty\)-operator bound for the adjoint evolution, for (3)--(4).

Dong--Kim--Lee construct fundamental solutions for nondivergence equations under Dini mean oscillation of the coefficients in the spatial variables and obtain sub-Gaussian estimates; under Dini continuity in space and measurability in time they obtain Gaussian bounds. Their results illustrate the additional spatial regularity that enters the nondivergence theory.

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

therefore requires an actual kernel or regularity estimate; it is not a consequence of ellipticity alone.

This distinction is load-bearing for the PDE project. A previous candidate proof attempted to use a universal adjoint \(L^\infty\) bound depending only on an ellipticity window for (4). The measurable-coefficient Aronson theory does not provide such a lemma. The repaired positive route instead uses the [maximum principle and Schauder estimates](parabolic-maximum-principle-and-schauder-estimates.md) at the level of the direct equation.