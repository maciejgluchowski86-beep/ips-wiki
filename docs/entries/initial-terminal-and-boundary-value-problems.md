---
title: Initial, terminal, and boundary value problems
status: standard fact
tags:
  - PDE
  - initial value problem
  - terminal value problem
  - boundary value problem
  - heat equation
---

# Initial, terminal, and boundary value problems

A PDE does not usually determine an unknown function until additional data are prescribed. This entry distinguishes the basic ways those data are attached to time and space. It is the second vocabulary item in the [PDE reading path](../pde-reading-path.md).

## Prerequisites

The notation for unknowns, independent variables, derivatives, and differential operators is fixed in [Partial differential equations: basic vocabulary](partial-differential-equations-basic-vocabulary.md).

## A spacetime cylinder and its boundary

Let $\Omega\subseteq\mathbb R^d$ be a spatial domain and let $T>0$. For a time-dependent equation on

$$
Q=(0,T)\times\Omega,
$$

the boundary of the spacetime cylinder has two different kinds of pieces. The sets

$$
\{0\}\times\overline\Omega
\qquad\text{and}\qquad
\{T\}\times\overline\Omega
$$

are the **temporal boundary** at the initial and terminal times, while

$$
[0,T]\times\partial\Omega
$$

is the **spatial** or **lateral boundary**. These pieces meet at the corners $\{0,T\}\times\partial\Omega$.

For the heat equation below, write

$$
\Delta u=\sum_{i=1}^d \partial_{ii}u.
$$

## Initial-value problems

An **initial-value problem** prescribes the value of the unknown at the starting time and asks for its subsequent evolution. On all of space, the basic heat-equation example is

$$
\partial_t u(t,x)=\Delta u(t,x),
\qquad
0<t<T,\quad x\in\mathbb R^d,
$$

together with

$$
u(0,x)=g(x).
$$

The function $g$ is the **initial datum**. The data are attached to the temporal boundary at $t=0$.

## Terminal-value problems

A **terminal-value problem** prescribes the value of the unknown at the final time. A standard backward heat-equation convention is

$$
\partial_t u(t,x)+\Delta u(t,x)=0,
\qquad
0\leq t<T,
$$

with

$$
u(T,x)=g(x).
$$

Here $g$ is the **terminal datum**. The word *backward* refers to the placement of the data at $T$: one determines values at earlier times from data prescribed at the terminal time.

The change of variables

$$
s=T-t,
\qquad
v(s,x)=u(T-s,x)
$$

turns this into the forward heat equation. Indeed,

$$
\partial_s v(s,x)
=
-\partial_t u(T-s,x)
=
\Delta u(T-s,x)
=
\Delta v(s,x),
$$

and $v(0,x)=g(x)$. Thus initial and terminal formulations differ by the orientation of the time variable.

## Boundary-value problems

A **boundary-value problem** prescribes data on a spatial boundary. For the heat equation on $Q=(0,T)\times\Omega$, a basic boundary condition is

$$
u(t,x)=h(t,x),
\qquad
0<t<T,\quad x\in\partial\Omega.
$$

This condition is imposed on the lateral boundary. For an evolution equation on a finite time interval, lateral boundary data are normally accompanied by initial or terminal data, which leads to an initial-boundary or terminal-boundary value problem.

## Initial-boundary and terminal-boundary value problems

An **initial-boundary value problem** combines initial data with spatial boundary data. For example,

$$
\partial_t u=\Delta u
\quad\text{in }(0,T)\times\Omega,
$$

with

$$
u(0,x)=g(x)
\quad\text{for }x\in\Omega,
\qquad
u(t,x)=h(t,x)
\quad\text{for }0<t<T,\ x\in\partial\Omega.
$$

A **terminal-boundary value problem** uses the terminal face instead. For the backward heat equation one may prescribe

$$
u(T,x)=g(x)
\quad\text{for }x\in\Omega,
\qquad
u(t,x)=h(t,x)
\quad\text{for }0<t<T,\ x\in\partial\Omega.
$$

The present entry only identifies where the data are imposed. Questions about what regularity the data should have, whether a solution exists or is unique, and what notion of solution is intended belong to later entries.

## Convention for backward equations and Feynman--Kac formulas

Later probabilistic representations use a current time $t$ and a fixed terminal time $T$. A terminal payoff $g(X_T)$ naturally corresponds to a condition of the form

$$
u(T,x)=g(x).
$$

Accordingly, the associated PDE is written with terminal data and is read backward from $T$ toward earlier times, even though the stochastic process itself runs forward from $t$ to $T$. This is the time convention used later in the [Itô diffusion and backward Kolmogorov](ito-diffusions-and-backward-kolmogorov-representation.md) and [Feynman--Kac](feynman-kac-formula-for-linear-parabolic-equations.md) entries.

The classification of PDEs and the distinction between classical, weak, mild, and viscosity solutions are intentionally deferred to later items in the reading path.

## Further reading

For standard examples of initial and boundary data for second-order PDEs and evolution equations, see Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, Chapters 2 and 7.
