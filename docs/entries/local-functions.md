---
title: Local functions
status: definition
tags:
  - local functions
  - cylinder functions
  - product topology
---

# Local functions

Local functions are observables that depend on only finitely many lattice sites. They form the natural initial domain for generators of infinite-volume [interacting particle systems](interacting-particle-system.md) and [spin systems](spin-system.md).

## Definition

Let \(\Lambda\) be a [lattice](lattice-and-graph.md), let \(\mathcal S\) be a single-site state space, and let \(\Omega=\mathcal S^\Lambda\). A function \(f:\Omega\to\R\) is local if there is a finite set \(A\Subset\Lambda\) such that

$$
\eta|_A=\xi|_A
\quad\Longrightarrow\quad
f(\eta)=f(\xi).
$$

In this case one says that \(f\) depends on \(A\). A finite set \(A\) with this property is a dependence set for \(f\).

## Support

If a minimal dependence set exists, it is denoted by \(\supp(f)\). More generally, \(\supp(f)\) may denote any chosen finite dependence set when minimality is irrelevant.

## Cylinder functions

Local functions are also called cylinder functions. If \(A\Subset\Lambda\) and \(g:\mathcal S^A\to\R\), then

$$
f(\eta)=g(\eta|_A)
$$

defines a local function. Conversely, every local function has this form for some finite \(A\Subset\Lambda\).

## Role in generators

For an infinite-volume spin system with formal generator

$$
\cL f(\eta)=\sum_{i\in\Lambda}c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr),
$$

the expression is initially interpreted for local \(f\). If \(f\) depends only on \(A\), then \(f(\eta^i)-f(\eta)=0\) for \(i\notin A\), so only finitely many summands can be nonzero.

## Topological role

When \(\mathcal S\) is finite and \(\Lambda\) is countable, \(\Omega=\mathcal S^\Lambda\) is compact in the product topology. Local functions are continuous and form a convergence-determining algebra. Thus weak convergence of probability measures, as in the local-function formulation of [ergodicity](ergodicity.md), can often be checked against local functions.
