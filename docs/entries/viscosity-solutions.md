---
title: Viscosity solutions
status: definition
audit: current
tags:
  - PDE
  - viscosity solution
  - comparison principle
  - fully nonlinear PDE
---

# Viscosity solutions

Viscosity solutions give a notion of solution for nonlinear second-order PDEs that does not require the unknown function to possess classical second derivatives. Derivatives are tested through smooth functions that touch the solution from above or below. This is the solution notion used in the HLOTW branching representation.

**References.** Michael G. Crandall, Hitoshi Ishii, and Pierre-Louis Lions, *User's guide to viscosity solutions of second order partial differential equations*, *Bulletin of the American Mathematical Society* **27** (1992), 1--67, arXiv:math/9207212. See [References](../meta/references.md).

**Prerequisite.** [Elliptic, parabolic, and hyperbolic equations](elliptic-parabolic-and-hyperbolic-equations.md) fixes the principal-part and parabolic terminology used below, including the distinction between uniform and degenerate parabolicity.

## Standard parabolic form

Write a forward second-order parabolic equation as

$$
\partial_tu+F(t,x,u,D_xu,D_x^2u)=0.
\tag{1}
$$

Here $F$ acts on the spatial jet; the time derivative is written separately. This separation is the standard parabolic viscosity convention.

The operator $F$ is **degenerate elliptic** if for every fixed $(t,x,r,p)$ and symmetric matrices $X\leq Y$,

$$
F(t,x,r,p,X)\geq F(t,x,r,p,Y).
\tag{2}
$$

Thus increasing the Hessian in the matrix order cannot increase $F$. For example, the heat equation

$$
\partial_tu-\frac12\Delta u=0
$$

has $F(t,x,r,p,X)=-\frac12\operatorname{tr}X$, which satisfies (2).

Degenerate ellipticity is an operator monotonicity property. It is not, by itself, a comparison theorem. A second common structural property is **properness**: $F$ is nondecreasing in the scalar value variable,

$$
r\leq s
\quad\Longrightarrow\quad
F(t,x,r,p,X)\leq F(t,x,s,p,X).
\tag{3}
$$

Which continuity, properness, growth, structure, and boundary hypotheses are needed for comparison depends on the particular theorem and domain.

## Definition: subsolution

An upper-semicontinuous function $u$ is a *viscosity subsolution* of (1) if, whenever $\varphi\in C^{1,2}$ and $u-\varphi$ has a local maximum at $(t_0,x_0)$, one has

$$
\partial_t\varphi(t_0,x_0)
+F\left(
 t_0,x_0,u(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\leq0.
\tag{4}
$$

The test function $\varphi$ is said to *touch $u$ from above* at $(t_0,x_0)$.

## Definition: supersolution

A lower-semicontinuous function $u$ is a *viscosity supersolution* if, whenever $u-\varphi$ has a local minimum at $(t_0,x_0)$, the reverse inequality holds:

$$
\partial_t\varphi(t_0,x_0)
+F\left(
 t_0,x_0,u(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\geq0.
\tag{5}
$$

A continuous function is a *viscosity solution* if it is both a viscosity subsolution and a viscosity supersolution. For a continuous initial or terminal-value problem, the prescribed data are imposed in the ordinary pointwise sense unless a weaker boundary convention is explicitly stated.

## Classical solutions are viscosity solutions

Suppose $u\in C^{1,2}$ solves (1) pointwise and $F$ is degenerate elliptic. If $u-\varphi$ has a local maximum at $(t_0,x_0)$, then

$$
\partial_tu=\partial_t\varphi,
\qquad
D_xu=D_x\varphi,
\qquad
D_x^2u\leq D_x^2\varphi
$$

at the touching point. By (2),

$$
\begin{aligned}
&\partial_t\varphi
+F(t_0,x_0,u,D\varphi,D^2\varphi)\\
&\qquad\leq
\partial_tu
+F(t_0,x_0,u,Du,D^2u)
=0,
\end{aligned}
$$

which is the subsolution inequality. The supersolution statement is analogous.

The monotonicity convention may be written with the opposite sign in other sources. Multiplying the PDE by $-1$ reverses the corresponding inequalities, so the sign convention should be fixed before invoking a viscosity theorem.

## Terminal problems and time reversal

Branching representations on this wiki are often written as backward terminal-value equations,

$$
\partial_tu+\frac12\Delta u+f(t,x,u,D_xu)=0,
\tag{6}
$$

with terminal datum $\phi$ prescribed at time $T$. Setting $v(s,x)=u(T-s,x)$ converts (6) to a forward equation. This removes ambiguity about which parabolic sign convention is being used when applying a forward comparison or stability theorem.

## Comparison and uniqueness

A *comparison principle* is a theorem of the form: if $u$ is a viscosity subsolution and $v$ is a viscosity supersolution with compatible initial, terminal, or boundary data, then $u\leq v$. Whenever comparison holds in the chosen function class, there is at most one viscosity solution in that class.

Comparison is not automatic from degenerate ellipticity. Standard comparison theorems additionally impose hypotheses such as continuity of $F$, properness or a suitable substitute, structural continuity conditions compatible with the doubling-of-variables argument, growth restrictions when the domain is unbounded, and boundary hypotheses appropriate to the problem. The assumptions must be checked against the specific theorem being invoked.

This is why the [HLOTW marked branching entry](marked-branching-diffusion-for-gradient-nonlinearities.md) separates two statements: their branching expectation is identified as a viscosity solution under their representation hypotheses, while uniqueness requires a separate comparison result or an explicit uniqueness assumption.

## Why this notion appears in branching representations

A branching construction often first produces a continuous expectation and a mild integral identity. Differentiability of that expectation may be insufficient to verify the PDE pointwise. Viscosity stability can identify limits of approximations as solutions under weaker differentiability, provided the hypotheses of the relevant stability theorem are satisfied; uniqueness then still depends on a comparison principle in the chosen class.
