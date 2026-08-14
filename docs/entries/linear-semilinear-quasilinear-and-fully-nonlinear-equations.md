---
title: Linear, semilinear, quasilinear, and fully nonlinear equations
status: standard fact
tags:
  - PDE
  - linear PDE
  - semilinear PDE
  - quasilinear PDE
  - fully nonlinear PDE
---

# Linear, semilinear, quasilinear, and fully nonlinear equations

This entry distinguishes four standard classes of PDEs according to how the unknown function and its derivatives enter the equation. It is the third vocabulary item in the [PDE reading path](../pde-reading-path.md).

## Prerequisites

The notation for unknowns, derivatives, Hessians, differential operators, and order is fixed in [Partial differential equations: basic vocabulary](partial-differential-equations-basic-vocabulary.md). The placement of initial, terminal, and boundary data is covered in [Initial, terminal, and boundary value problems](initial-terminal-and-boundary-value-problems.md).

## The highest-order derivatives are decisive

For a scalar second-order equation, write schematically

$$
F\bigl(x,u(x),Du(x),D^2u(x)\bigr)=0.
$$

The classification below is governed primarily by the dependence on the highest-order derivatives, here the Hessian $D^2u$. Nonlinear dependence on lower-order quantities such as $u$ or $Du$ does not by itself make a second-order equation fully nonlinear.

For parabolic equations of the form

$$
\partial_tu+F(t,x,u,Du,D^2u)=0,
$$

the same terminology is normally applied to the dependence on the spatial second derivatives $D^2u$, while $\partial_tu$ appears linearly in this standard form.

## Linear equations

A PDE is **linear** when the unknown and all of its derivatives enter linearly, with coefficients that do not depend on the unknown. A second-order linear equation has the form

$$
\sum_{i,j=1}^d a_{ij}(x)\,\partial_{ij}u
+
\sum_{i=1}^d b_i(x)\,\partial_i u
+
c(x)u
=
f(x).
$$

The differential operator on the left is linear in $u$. The term $f$ is prescribed data and may make the equation inhomogeneous without changing the classification.

The heat equation

$$
\partial_tu-\Delta u=0
$$

is linear.

## Semilinear equations

A second-order PDE is **semilinear** when the highest-order derivatives enter linearly with coefficients independent of the unknown and its derivatives, while lower-order terms may depend nonlinearly on $u$ or $Du$. A typical form is

$$
\sum_{i,j=1}^d a_{ij}(x)\,\partial_{ij}u
+
G(x,u,Du)
=
0.
$$

For example,

$$
\partial_tu-\Delta u+u^3=0
$$

is semilinear: the second spatial derivatives occur only through the linear term $-\Delta u$, while the zeroth-order term is nonlinear.

## Quasilinear equations

A second-order PDE is **quasilinear** when the highest-order derivatives still enter linearly, but their coefficients may depend on the independent variables, the unknown, or lower-order derivatives. A typical form is

$$
\sum_{i,j=1}^d
a_{ij}(x,u,Du)\,\partial_{ij}u
+
G(x,u,Du)
=
0.
$$

For example,

$$
\partial_tu-a(u)\Delta u=0
$$

is quasilinear when $a$ is a prescribed function: the Hessian enters linearly, but its coefficient depends on $u$.

## Fully nonlinear equations

A second-order PDE is **fully nonlinear** when the highest-order derivatives themselves enter nonlinearly. In the schematic equation

$$
F(x,u,Du,D^2u)=0,
$$

this means that the dependence on $D^2u$ is nonlinear.

The quadratic-Hessian equation used in the current research programme is

$$
\partial_tv
=
\frac12 v_{xx}
+
\lambda(v_{xx})^2.
$$

It is fully nonlinear as a second-order spatial equation because the highest spatial derivative $v_{xx}$ appears quadratically. The equation and its branching representation are developed later in the [probabilistic representations for nonlinear PDEs](../pde-branching-representations.md) part of the wiki.

## Comparison at a glance

For a second-order equation, the distinction can be summarized by asking how $D^2u$ enters:

- **linear:** all dependence on $u$, $Du$, and $D^2u$ is linear, with coefficients independent of the unknown;
- **semilinear:** $D^2u$ enters linearly with coefficients independent of $u$ and $Du$, but lower-order terms may be nonlinear;
- **quasilinear:** $D^2u$ enters linearly, but its coefficients may depend on $u$ or $Du$;
- **fully nonlinear:** the dependence on $D^2u$ is nonlinear.

This classification is separate from the elliptic/parabolic/hyperbolic classification, which concerns the principal second-order part and is the next item in the reading path.

## Further reading

For standard PDE terminology and examples, see Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, especially Chapters 1, 2, 6, and 7.
