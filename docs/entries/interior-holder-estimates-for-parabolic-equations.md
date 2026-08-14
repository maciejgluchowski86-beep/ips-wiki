---
title: Interior Holder estimates for parabolic equations
status: standard fact
tags:
  - PDE
  - parabolic equation
  - Holder regularity
  - Krylov-Safonov
  - De Giorgi-Nash-Moser
---

# Interior Holder estimates for parabolic equations

Uniform parabolicity produces interior continuity even when the coefficients are only bounded and measurable. The precise theorem depends on whether the equation is in divergence or nondivergence form. These estimates are weaker than Schauder theory: they control the solution itself in a Holder norm but do not produce classical second derivatives.

**References.** Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010. Gary M. Lieberman, *Second Order Parabolic Differential Equations*, World Scientific, 1996. See [References](../meta/references.md).

## Parabolic cylinders

For \(r>0\), write

$$
Q_r
=
(-r^2,0]\times B_r
$$

for a backward parabolic cylinder. The time length is \(r^2\) because the heat equation has scaling \(t\sim x^2\).

## Nondivergence form: Krylov--Safonov

Consider

$$
\partial_tu
-a_{ij}(t,x)\partial_{ij}u
=0
\tag{1}
$$

in \(Q_1\), with bounded measurable coefficients satisfying the uniform ellipticity bounds

$$
\kappa|\xi|^2
\leq
a_{ij}(t,x)\xi_i\xi_j
\leq
K|\xi|^2.
\tag{2}
$$

For bounded solutions in the appropriate strong or viscosity class, Krylov--Safonov theory gives numbers

$$
0<\alpha<1,
\qquad
C<\infty,
$$

depending only on the dimension and the ellipticity ratio, such that

$$
[u]_{C^{\alpha/2,\alpha}(Q_{1/2})}
\leq
C\lVert u\rVert_{L^\infty(Q_1)}.
\tag{3}
$$

After parabolic rescaling, the same estimate holds on smaller cylinders with the corresponding scale factors.

## Divergence form: De Giorgi--Nash--Moser

For

$$
\partial_tu
-
\partial_i\bigl(a_{ij}(t,x)\partial_ju\bigr)
=0,
\tag{4}
$$

with the same bounded measurable ellipticity assumptions, De Giorgi--Nash--Moser theory gives an analogous local Holder estimate for weak solutions:

$$
[u]_{C^{\alpha/2,\alpha}(Q_{1/2})}
\leq
C\lVert u\rVert_{L^\infty(Q_1)}.
\tag{5}
$$

The values of \(\alpha\) and \(C\) are not generally the same as in the nondivergence theorem, but they again depend only on dimension and ellipticity data.

## What these estimates do not give

Neither (3) nor (5) is a Schauder estimate. With merely measurable coefficients one should not expect bounds for \(u_{xx}\) or for a \(C^{1+\alpha/2,2+\alpha}\) norm. To obtain those derivatives one needs additional coefficient regularity, as in [Parabolic maximum principle and Schauder estimates](parabolic-maximum-principle-and-schauder-estimates.md).

The operator form also matters. The direct equation

$$
\partial_tu=a(t,x)u_{xx}
$$

and its adjoint density equation

$$
\partial_t\rho=\partial_x^2(a\rho)
$$

are not interchangeable with the divergence-form equation \(u_t=\partial_x(au_x)\). Pointwise kernel bounds require separate hypotheses; see [Aronson and Nash Gaussian bounds](aronson-nash-gaussian-bounds.md).

## Compactness consequence

Suppose \((u_n)\) is uniformly bounded and solves equations of the same structural class on a common cylinder, with a common ellipticity window. The estimates above give a common Holder modulus on every strictly smaller cylinder. By Arzela--Ascoli, one may therefore extract subsequences converging locally uniformly.

This is the role of interior Holder estimates in compactness arguments. In the audited quadratic-Hessian theorem the stronger uniform Schauder ball is available, so its convergence proof does not need to rely on the rough-coefficient theorem.