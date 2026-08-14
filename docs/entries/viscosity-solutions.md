---
title: Viscosity solutions
status: definition
tags:
  - PDE
  - viscosity solution
  - comparison principle
  - fully nonlinear PDE
---

# Viscosity solutions

Viscosity solutions give a notion of solution for nonlinear second-order PDEs that does not require the unknown function to possess classical second derivatives. Derivatives are tested through smooth functions that touch the solution from above or below. This is the solution notion used in the HLOTW branching representation.

**References.** Michael G. Crandall, Hitoshi Ishii, and Pierre-Louis Lions, *User's guide to viscosity solutions of second order partial differential equations*, *Bulletin of the American Mathematical Society* **27** (1992), 1--67, arXiv:math/9207212. See [References](../meta/references.md).

## Parabolic equation

Consider a scalar parabolic PDE written as

$$
F(t,x,u,\partial_tu,D_xu,D_x^2u)=0
\tag{1}
$$

on an open space-time region. For the one-dimensional semilinear equation

$$
\partial_tu+\frac12\partial_x^2u+f(t,x,u,\partial_xu)=0,
$$

one may take

$$
F(t,x,r,q,p,X)
=
q+\frac12X+f(t,x,r,p).
$$

## Definition: subsolution

An upper-semicontinuous function \(u\) is a *viscosity subsolution* of (1) if, whenever \(\varphi\in C^{1,2}\) and \(u-\varphi\) has a local maximum at \((t_0,x_0)\), one has

$$
F\left(
 t_0,x_0,u(t_0,x_0),
 \partial_t\varphi(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\leq0.
\tag{2}
$$

The test function \(\varphi\) is said to *touch \(u\) from above* at \((t_0,x_0)\).

## Definition: supersolution

A lower-semicontinuous function \(u\) is a *viscosity supersolution* if, whenever \(u-\varphi\) has a local minimum at \((t_0,x_0)\), the reverse inequality holds:

$$
F\left(
 t_0,x_0,u(t_0,x_0),
 \partial_t\varphi(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\geq0.
\tag{3}
$$

A continuous function is a *viscosity solution* if it is both a viscosity subsolution and a viscosity supersolution.

For a continuous terminal-value problem, the terminal condition is imposed in the ordinary pointwise sense unless a weaker boundary convention is explicitly stated.

## Classical solutions are viscosity solutions

Suppose \(u\in C^{1,2}\) solves (1) pointwise. If \(u-\varphi\) has a local maximum at \((t_0,x_0)\), then

$$
\partial_tu=\partial_t\varphi,
\qquad
D_xu=D_x\varphi,
\qquad
D_x^2u\leq D_x^2\varphi
$$

at the touching point. For a proper degenerate-elliptic equation, substituting these inequalities into the PDE gives the subsolution condition; the supersolution condition is analogous. Thus the viscosity notion extends the classical one.

The monotonicity convention in the definition of a *proper* operator depends on whether the equation is written as \(F=0\) or with the opposite sign. When applying a comparison theorem, the sign convention and structural hypotheses on \(F\) should therefore be stated explicitly.

## Comparison and uniqueness

A *comparison principle* is a theorem of the form: if \(u\) is a viscosity subsolution and \(v\) is a viscosity supersolution with compatible boundary or terminal data, then \(u\leq v\). Whenever comparison holds in the chosen function class, there is at most one viscosity solution in that class.

Comparison is not automatic for every nonlinear PDE. It depends on continuity, ellipticity, growth, and domain assumptions. This is why the [HLOTW marked branching entry](marked-branching-diffusion-for-gradient-nonlinearities.md) separates two statements: their branching expectation is shown to be a viscosity solution under their integrability hypotheses, while uniqueness requires a separate comparison result or an explicit uniqueness assumption.

## Why this notion appears in branching representations

A branching construction often first produces a continuous expectation and a mild integral identity. Differentiability of that expectation may be insufficient to verify the PDE pointwise. Viscosity stability permits one to identify limits of approximations as solutions under much weaker differentiability. In the [representation-level dichotomy](representation-level-dichotomy.md), the HLOTW estimator is identified with a continuous viscosity solution, while no solution is attributed to the nonintegrable NPP functional.