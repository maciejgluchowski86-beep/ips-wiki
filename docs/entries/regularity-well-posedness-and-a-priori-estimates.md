---
title: Regularity, well-posedness, and a priori estimates
status: standard fact
audit: current
tags:
  - PDE
  - regularity
  - well-posedness
  - a priori estimate
---

# Regularity, well-posedness, and a priori estimates

A PDE theorem has several logically different parts. It may assume regularity of the data or of a candidate solution, prove additional regularity, establish existence, prove uniqueness, or control how solutions depend on the data. An estimate for a solution that is already assumed to exist does not by itself construct that solution.

**References.** These distinctions and the examples below are standard in PDE theory. See Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, especially Chapters 2, 6, and 7 for classical equations, weak solutions, energy estimates, and existence arguments. See [References](../meta/references.md).

## Prerequisites

The placement of initial, terminal, and boundary data is fixed in [Initial, terminal, and boundary value problems](initial-terminal-and-boundary-value-problems.md). The meaning of the word *solution* depends on the chosen class; see [Classical, weak/distributional, mild, and viscosity solutions](classical-weak-mild-and-viscosity-solutions.md).

## Hypotheses versus conclusions

A **regularity assumption** is a hypothesis such as

$$
g\in C^2(\overline\Omega),
\qquad
f\in L^2(\Omega),
$$

or an assumption that a candidate solution belongs to a specified Sobolev or Hölder class. Such an assumption tells us which derivatives, traces, or integrals are meaningful.

A **regularity conclusion** says that a solution known to exist is actually smoother than the definition initially requires. For example, a theorem may begin with a weak solution and prove that it is classical in the interior. The function space occurring in the conclusion is therefore not automatically a hypothesis.

Keeping these directions separate matters when reading a theorem: one should ask which regularity is supplied as input and which is produced by the PDE.

## Existence, uniqueness, and stability

For a PDE problem with data $d$, three basic questions are:

- **existence:** does at least one solution corresponding to $d$ exist?
- **uniqueness:** can there be more than one solution in the stated solution class?
- **stability or continuous dependence:** if the data change slightly, do the corresponding solutions change slightly in the topology under consideration?

A problem is called **well posed** in the Hadamard sense when existence, uniqueness, and continuous dependence hold in the specified classes. The classes are part of the statement: a problem can be well posed in one topology and ill posed in another.

Uniqueness is often proved by applying an estimate to the difference of two solutions. Existence usually needs an additional construction or compactness argument, such as an explicit formula, semigroup method, Galerkin approximation, variational method, fixed-point argument, or approximation followed by a limit.

## A priori estimates

An **a priori estimate** is an inequality derived for every sufficiently regular solution of a problem, before one has used the estimate to construct a solution. Schematically,

$$
\lVert u\rVert_X
\leq
C\bigl(\lVert f\rVert_Y+\lVert g\rVert_Z\bigr).
\tag{1}
$$

The constant $C$ should depend only on parameters stated in the theorem, such as the domain, time horizon, or ellipticity constants, and not on the particular solution $u$.

Such an estimate can have several uses. Applied to the difference of two solutions with the same data, it may imply uniqueness. Applied to an approximating sequence, it may give the uniform bounds needed for compactness. Applied to two different data sets, it may yield stability. But these consequences require the corresponding argument; the inequality alone is not an existence theorem.

## Local, interior, and global estimates

A **local** estimate controls a solution on a small region using information on a somewhat larger region. An **interior** estimate is local and stays a positive distance from the spatial boundary. Its constants may deteriorate as the interior region approaches the boundary.

A **global** estimate controls the solution up to the boundary. Such a statement normally requires boundary regularity, compatibility of the data, and boundary conditions appropriate to the equation. Thus an interior regularity theorem cannot be used as a boundary regularity theorem without additional input.

For time-dependent equations the same distinction applies near the initial or terminal time. Estimates valid only for positive times may improve regularity away from the temporal boundary without controlling the trace at that boundary.

## Canonical example: an energy estimate for the heat equation

Consider the forced heat equation on the one-dimensional torus,

$$
\partial_tu-\partial_x^2u=f,
\tag{2}
$$

with initial datum $g$ prescribed at time zero. Assume for the moment that $u$ is smooth enough for the following calculation. Multiplying (2) by $u$, integrating over the torus, and integrating by parts gives

$$
\frac12\frac{d}{dt}\lVert u(t)\rVert_2^2
+
\lVert \partial_xu(t)\rVert_2^2
=
\int f(t,x)u(t,x)\,dx.
\tag{3}
$$

Cauchy--Schwarz and Young's inequality turn (3) into a bound for the size of an assumed solution in terms of $g$ and $f$. The same calculation applied to the difference of two solutions with identical data gives uniqueness in an appropriate energy class.

Equation (3), however, does **not** prove that a solution of (2) exists. An existence proof must still construct approximate solutions or invoke a separate theorem, obtain uniform bounds such as (3), and pass to a limit while checking that the limiting object satisfies the equation and data. This separation between estimate and construction is fundamental throughout PDE theory.

## Reading a PDE theorem

When using a PDE result, identify four pieces explicitly: the data and their regularity, the solution notion, the asserted existence/uniqueness/stability conclusion, and the exact estimate with its domain of validity. In particular, check whether an estimate is interior or global and whether the theorem assumes the solution whose norm it bounds.
