---
title: Elliptic, parabolic, and hyperbolic equations
status: standard fact
audit: current
tags:
  - PDE
  - elliptic equation
  - parabolic equation
  - hyperbolic equation
  - principal symbol
---

# Elliptic, parabolic, and hyperbolic equations

Elliptic, parabolic, and hyperbolic are classifications of the principal part of a differential equation. They describe the geometry of the highest-order derivatives and are independent of whether the equation is linear, semilinear, quasilinear, or fully nonlinear.

## Prerequisites

The notation for derivatives and differential operators is fixed in [Partial differential equations: basic vocabulary](partial-differential-equations-basic-vocabulary.md). The separate classification by dependence on the unknown is covered in [Linear, semilinear, quasilinear, and fully nonlinear equations](linear-semilinear-quasilinear-and-fully-nonlinear-equations.md).

## Canonical examples

The Laplace and Poisson equations

$$
-\Delta u=0,
\qquad
-\Delta u=f,
$$

are the model **elliptic** equations. Their second-order part acts in every spatial direction with the same positive strength.

The heat equation

$$
\partial_tu-\Delta u=0
$$

is the model **parabolic** equation. It is first order in time and second order in space, and its spatial second-order part is elliptic.

The wave equation

$$
\partial_t^2u-c^2\Delta u=0
$$

is the model **hyperbolic** equation. For a spatial frequency $\xi\neq0$, the characteristic polynomial in the temporal frequency $\tau$ is

$$
\tau^2-c^2|\xi|^2,
$$

with the two real roots $\tau=\pm c|\xi|$. This real characteristic propagation is the feature relevant to the elementary scalar hyperbolic picture.

## Principal part and principal symbol

Consider a scalar second-order operator in spatial variables,

$$
Lu
=
\sum_{i,j=1}^d a^{ij}(x)\partial_{ij}u
+
\text{lower-order terms}.
$$

Because $\partial_{ij}u=\partial_{ji}u$ for smooth $u$, only the symmetric part of the coefficient matrix $A=(a^{ij})$ matters for the second-order term. The **principal part** is

$$
L_{\mathrm{prin}}u
=
\sum_{i,j=1}^d a^{ij}(x)\partial_{ij}u,
$$

and its quadratic **principal symbol** is

$$
p_x(\xi)
=
\sum_{i,j=1}^d a^{ij}(x)\xi_i\xi_j.
$$

Some Fourier-transform conventions insert an overall minus sign in the symbol. That sign does not change the classifications below. Lower-order terms do not enter the principal symbol.

## Ellipticity and uniform ellipticity

A real scalar second-order operator is **elliptic** at $x$ when its principal quadratic form is definite, after multiplying the whole equation by $-1$ if necessary. With the positive convention, this means

$$
p_x(\xi)>0
\qquad\text{for every }\xi\neq0.
$$

It is **uniformly elliptic** on a set when there are constants $0<\lambda\leq\Lambda<\infty$ such that

$$
\lambda|\xi|^2
\leq
\sum_{i,j=1}^d a^{ij}(x)\xi_i\xi_j
\leq
\Lambda|\xi|^2
$$

for every relevant $x$ and every $\xi\in\mathbb R^d$. The Laplacian has $A=I$, so one may take $\lambda=\Lambda=1$.

## First-order-in-time parabolic equations

For the scalar evolution equation

$$
\partial_tu
-
\sum_{i,j=1}^d a^{ij}(t,x)\partial_{ij}u
+
\text{lower-order terms}
=0,
$$

the elementary parabolic classification used in this wiki comes from the spatial second-order matrix $A(t,x)$. If $A$ is positive semidefinite, the equation is **degenerate parabolic** in this sense. If there are constants $0<\lambda\leq\Lambda<\infty$ with

$$
\lambda|\xi|^2
\leq
\sum_{i,j=1}^d a^{ij}(t,x)\xi_i\xi_j
\leq
\Lambda|\xi|^2
$$

uniformly in $(t,x)$, the equation is **uniformly parabolic**.

Thus the heat equation is uniformly parabolic. An equation in which the spatial diffusion coefficient can vanish may be degenerate parabolic and requires different regularity theory.

## Hyperbolic equations: the scoped scalar picture

For a scalar second-order equation with a distinguished time variable, the principal symbol can be viewed as a polynomial in the temporal frequency $\tau$, with spatial frequency $\xi$ fixed. Hyperbolicity with respect to time is characterized by real characteristic roots in $\tau$; strict hyperbolicity requires the relevant roots to be distinct. For the wave equation these roots are exactly $\pm c|\xi|$.

This entry uses only that scalar second-order principal-symbol picture, which is sufficient for the PDE reading path. Hyperbolic systems, multiple characteristics, and the general theory of hyperbolic operators require additional definitions and are not being classified here.

## Independent classifications

Elliptic/parabolic/hyperbolic and linear/semilinear/quasilinear/fully nonlinear answer different questions. The first concerns the principal differential geometry; the second concerns how the unknown and its derivatives enter the equation.

For example,

- $\partial_tu-\Delta u=0$ is linear and parabolic;
- $\partial_tu-\Delta u+u^3=0$ is semilinear and parabolic;
- $\partial_tu-a(u)\Delta u=0$ is quasilinear and is uniformly parabolic only on a class where $a(u)$ stays between two positive constants;
- $\det D^2u=f$ is fully nonlinear, while ellipticity is considered on an appropriate branch such as the convex one.

Knowing one classification therefore does not determine the other.

## Reader check

After this entry, a reader should be able to identify the principal part and principal symbol of a scalar second-order equation; explain why Laplace/Poisson, heat, and wave are the canonical elliptic, parabolic, and hyperbolic examples; state uniform ellipticity and the elementary uniform-parabolic condition above; and keep this classification separate from linearity versus nonlinearity.

## Further reading

For the standard second-order classification and the elliptic, parabolic, and hyperbolic model equations, see Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, especially Chapters 2, 6, 7, and 12.
