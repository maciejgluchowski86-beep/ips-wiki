---
title: Partial differential equations: basic vocabulary
status: standard fact
audit: current
tags:
  - PDE
  - differential operator
  - derivatives
  - analysis
---

# Partial differential equations: basic vocabulary

This entry fixes the basic objects used when a PDE is written down. It covers only the first vocabulary layer in the [PDE reading path](../pde-reading-path.md).

## Prerequisites

The entry assumes standard multivariable calculus and Euclidean-space notation. Repository-wide symbol conventions are recorded in [Notation](../meta/notation.md).

## Domain and independent variables

In standard PDE terminology, a **domain** is an open connected set $\Omega\subseteq\mathbb R^d$. When connectedness or openness is not intended, this wiki will instead say **spatial set** or name the set directly.

A point

$$
x=(x_1,\ldots,x_d)\in\Omega
$$

collects the **independent variables**. When one variable plays the role of time it is often written separately, for example $(t,x)$ with $x\in\Omega$.

For a set $A\subseteq\mathbb R^d$, its closure is denoted by $\overline A$ and its boundary by $\partial A$. In particular, because a domain $\Omega$ is open,

$$
\partial\Omega
=
\overline\Omega\setminus\Omega.
$$

These notations are used in the next entry when initial, terminal, and spatial boundary data are distinguished.

## Scalar and vector unknowns

A **scalar unknown** is a function

$$
u:\Omega\to\mathbb R.
$$

A **vector unknown** takes values in $\mathbb R^m$,

$$
u:\Omega\to\mathbb R^m,
$$

and its components may be written $u=(u^1,\ldots,u^m)$.

The function $u$ is the object to be determined from the equation together with whatever additional data are imposed later.

## Partial derivatives

For a scalar function $u$, write

$$
\partial_i u
=
\frac{\partial u}{\partial x_i},
\qquad
\partial_{ij}u
=
\frac{\partial^2u}{\partial x_i\,\partial x_j}.
$$

The gradient and Hessian are

$$
Du=(\partial_1u,\ldots,\partial_du),
\qquad
D^2u=(\partial_{ij}u)_{1\leq i,j\leq d}.
$$

For a multi-index $\alpha=(\alpha_1,\ldots,\alpha_d)\in\mathbb N_0^d$, set

$$
|\alpha|=\alpha_1+\cdots+\alpha_d,
\qquad
D^\alpha u
=
\partial_1^{\alpha_1}\cdots\partial_d^{\alpha_d}u.
$$

For vector-valued $u$, these derivatives are taken componentwise.

## Differential operators and PDE notation

A **differential operator** forms a new expression from a function and finitely many of its derivatives. For example,

$$
Lu
=
\sum_{i,j=1}^d a_{ij}(x)\,\partial_{ij}u
+
\sum_{i=1}^d b_i(x)\,\partial_i u
+
c(x)u
$$

is a differential operator acting on scalar functions.

A second-order scalar PDE is often written schematically as

$$
F\bigl(x,u(x),Du(x),D^2u(x)\bigr)=0.
$$

This notation says that, at each point $x$, the equation relates the point $x$, the value of $u$, its first derivatives, and its second derivatives. The displayed form is notation only; later entries distinguish important classes of such equations.

## Order

The **order** of a differential equation is the highest derivative order that appears in it. Thus an equation involving first derivatives but no second derivatives is first order, while one involving some second derivative and no higher derivative is second order.

## ODE and PDE contrast

An ordinary differential equation has one independent variable. For example,

$$
y'(t)=-y(t)
$$

asks for a function of one variable $t$.

A partial differential equation involves partial derivatives with respect to independent variables. A basic example is the one-dimensional heat equation

$$
\partial_t u(t,x)=\partial_{xx}u(t,x),
$$

whose unknown $u$ depends on time $t$ and space $x$. Its order is two because the highest derivative appearing is $\partial_{xx}u$.

## Further reading

For a standard PDE introduction and the surrounding basic terminology, see Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, Chapter 1.
