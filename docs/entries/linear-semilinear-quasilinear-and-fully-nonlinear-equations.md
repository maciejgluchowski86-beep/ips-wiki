---
title: Linear, semilinear, quasilinear, and fully nonlinear equations
status: standard fact
audit: current
tags:
  - PDE
  - linear PDE
  - semilinear PDE
  - quasilinear PDE
  - fully nonlinear PDE
---

# Linear, semilinear, quasilinear, and fully nonlinear equations

This entry distinguishes four standard classes of PDEs according to how the unknown and its derivatives enter the equation. It is the third vocabulary item in the [PDE reading path](../pde-reading-path.md).

## Prerequisites

The notation for unknowns, derivatives, Hessians, differential operators, and order is fixed in [Partial differential equations: basic vocabulary](partial-differential-equations-basic-vocabulary.md). The placement of initial, terminal, and boundary data is covered in [Initial, terminal, and boundary value problems](initial-terminal-and-boundary-value-problems.md).

## Highest-order derivatives

For a scalar second-order equation, write schematically

$$
F\bigl(x,u(x),Du(x),D^2u(x)\bigr)=0.
$$

The distinction between semilinear, quasilinear, and fully nonlinear equations is governed by the dependence on the highest-order derivatives, here $D^2u$. Nonlinear dependence on lower-order quantities such as $u$ or $Du$ does not by itself make a second-order equation fully nonlinear.

For a parabolic equation written as

$$
\partial_tu+F(t,x,u,Du,D^2u)=0,
$$

the same terminology is normally applied to the spatial second-order part.

## Linear equations

A PDE is **linear** when the unknown and all of its derivatives enter linearly, with coefficients independent of the unknown. A scalar second-order linear equation has the form

$$
\sum_{i,j=1}^d a_{ij}(x)\partial_{ij}u
+\sum_{i=1}^d b_i(x)\partial_i u
+c(x)u=f(x).
$$

The prescribed forcing $f$ may make the equation inhomogeneous without changing the classification. The heat equation $\partial_tu-\Delta u=0$ is linear.

## Semilinear equations

A second-order PDE is **semilinear** when the highest-order derivatives enter linearly with coefficients independent of $u$ and its derivatives, while lower-order terms may depend nonlinearly on $u$ or $Du$. A typical form is

$$
\sum_{i,j=1}^d a_{ij}(x)\partial_{ij}u+G(x,u,Du)=0.
$$

For example, $\partial_tu-\Delta u+u^3=0$ is semilinear.

## Quasilinear equations

A second-order PDE is **quasilinear** when the highest-order derivatives still enter linearly, but their coefficients may depend on the independent variables, the unknown, or lower-order derivatives. A typical form is

$$
\sum_{i,j=1}^d a_{ij}(x,u,Du)\partial_{ij}u+G(x,u,Du)=0.
$$

For example, $\partial_tu-a(u)\Delta u=0$ is quasilinear when $a$ is prescribed.

## Fully nonlinear equations

A second-order PDE is **fully nonlinear** when the dependence on $D^2u$ itself is nonlinear. The Monge--Ampère equation

$$
\det D^2u=f
$$

is a canonical example: the determinant is nonlinear in the Hessian entries. Questions such as ellipticity additionally depend on the solution class and on the principal part; that is a separate classification.

## Comparison at a glance

For a second-order equation, ask how $D^2u$ enters:

- **linear:** all dependence on $u$, $Du$, and $D^2u$ is linear, with coefficients independent of the unknown;
- **semilinear:** $D^2u$ enters linearly with coefficients independent of $u$ and $Du$, but lower-order terms may be nonlinear;
- **quasilinear:** $D^2u$ enters linearly, but its coefficients may depend on $u$ or $Du$;
- **fully nonlinear:** the dependence on $D^2u$ is nonlinear.

This classification is separate from the [elliptic/parabolic/hyperbolic classification](elliptic-parabolic-and-hyperbolic-equations.md), which concerns the principal part and principal symbol and is the next item in the reading path.

## Further reading

For standard terminology and examples, see Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, especially Chapters 1, 2, 6, and 7.
