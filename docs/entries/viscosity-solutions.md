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

## Parabolic sign convention

For a forward parabolic problem, write

$$
F(t,x,u,\partial_tu,D_xu,D_x^2u)=0.
\tag{1}
$$

The standard viscosity comparison convention assumes that the second-order part is *degenerate elliptic*: if $X\leq Y$ as symmetric matrices, then

$$
F(t,x,r,q,p,X)\geq F(t,x,r,q,p,Y).
\tag{2}
$$

For example, the forward heat equation

$$
\partial_tv-\frac12\partial_x^2v=0
$$

corresponds to

$$
F(t,x,r,q,p,X)=q-\frac12X,
$$

which satisfies (2).

The branching papers on this wiki are often written as backward terminal-value equations,

$$
\partial_tu+\frac12\partial_x^2u+f(t,x,u,\partial_xu)=0,
\qquad
u(T,\cdot)=\phi.
\tag{3}
$$

To apply the standard forward viscosity convention without changing signs implicitly, set $v(s,x)=u(T-s,x)$. Then (3) becomes

$$
\partial_sv-\frac12\partial_x^2v
-f(T-s,x,v,\partial_xv)=0,
\qquad
v(0,\cdot)=\phi,
\tag{4}
$$

whose second-order part is degenerate elliptic in the sense of (2). Statements about viscosity solutions of the terminal problem are understood through this equivalent time reversal.

## Definition: subsolution

An upper-semicontinuous function $v$ is a *viscosity subsolution* of (1) if, whenever $\varphi\in C^{1,2}$ and $v-\varphi$ has a local maximum at $(t_0,x_0)$, one has

$$
F\left(
 t_0,x_0,v(t_0,x_0),
 \partial_t\varphi(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\leq0.
\tag{5}
$$

The test function $\varphi$ is said to *touch $v$ from above* at $(t_0,x_0)$.

## Definition: supersolution

A lower-semicontinuous function $v$ is a *viscosity supersolution* if, whenever $v-\varphi$ has a local minimum at $(t_0,x_0)$, the reverse inequality holds:

$$
F\left(
 t_0,x_0,v(t_0,x_0),
 \partial_t\varphi(t_0,x_0),
 D_x\varphi(t_0,x_0),
 D_x^2\varphi(t_0,x_0)
\right)
\geq0.
\tag{6}
$$

A continuous function is a *viscosity solution* if it is both a viscosity subsolution and a viscosity supersolution. For a continuous initial or terminal-value problem, the prescribed data are imposed in the ordinary pointwise sense unless a weaker boundary convention is explicitly stated.

## Classical solutions are viscosity solutions

Suppose $v\in C^{1,2}$ solves (1) pointwise and $F$ is degenerate elliptic in the sense of (2). If $v-\varphi$ has a local maximum at $(t_0,x_0)$, then

$$
\partial_tv=\partial_t\varphi,
\qquad
D_xv=D_x\varphi,
\qquad
D_x^2v\leq D_x^2\varphi
$$

at the touching point. By (2),

$$
F(t_0,x_0,v,\varphi_t,D\varphi,D^2\varphi)
\leq
F(t_0,x_0,v,v_t,Dv,D^2v)
=0,
$$

which is the subsolution inequality. The supersolution statement is analogous.

The monotonicity convention may be written with the opposite sign in other sources. Multiplying the PDE by $-1$ reverses the subsolution and supersolution inequalities, so the sign convention should always be fixed before invoking comparison.

## Comparison and uniqueness

A *comparison principle* is a theorem of the form: if $u$ is a viscosity subsolution and $v$ is a viscosity supersolution with compatible boundary or terminal data, then $u\leq v$. Whenever comparison holds in the chosen function class, there is at most one viscosity solution in that class.

Comparison is not automatic for every nonlinear PDE. It depends on continuity, ellipticity, growth, and domain assumptions. This is why the [HLOTW marked branching entry](marked-branching-diffusion-for-gradient-nonlinearities.md) separates two statements: their branching expectation is shown to be a viscosity solution under their integrability hypotheses, while uniqueness requires a separate comparison result or an explicit uniqueness assumption.

## Why this notion appears in branching representations

A branching construction often first produces a continuous expectation and a mild integral identity. Differentiability of that expectation may be insufficient to verify the PDE pointwise. Viscosity stability permits one to identify limits of approximations as solutions under much weaker differentiability, provided the appropriate stability and comparison hypotheses are available.
