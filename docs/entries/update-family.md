---
title: Update family
status: definition
tags:
  - KCSM
  - constraints
  - update rules
---

# Update family

An update family specifies which local vacancy patterns allow a constrained refresh. It is the combinatorial input for a [kinetically constrained spin model](kinetically-constrained-spin-model.md).

## Definition

Let \(\Lambda\) be a [lattice](lattice-and-graph.md). For each \(i\in\Lambda\), let \(N(i)\) be the set of neighbours of \(i\), with \(i\notin N(i)\). An update family at \(i\) is a collection

$$
\mathcal U_i\subseteq \{U:U\Subset N(i)\}.
$$

The elements \(U\in\mathcal U_i\) are update rules. In KCSM, an update rule is satisfied when all sites in \(U\) are vacant, meaning equal to \(0\).

## Constraint induced by an update family

The constraint associated with \(\mathcal U_i\) is

$$
c_i(\eta)
=
\ind\{\exists U\in\mathcal U_i\text{ such that }\eta(j)=0\text{ for every }j\in U\}.
$$

Equivalently, using vacancy indicators,

$$
c_i(\eta)
=
1-\prod_{U\in\mathcal U_i}
\left(1-\prod_{j\in U}(1-\eta(j))\right),
$$

with the convention that an empty product over update rules gives \(1\), so \(\mathcal U_i=\varnothing\) gives \(c_i\equiv0\).

## Homogeneous lattice case

On \(\Lambda=\Z^d\), a translation-invariant update family is often specified by a finite collection

$$
\mathcal U=\{U_1,\ldots,U_m\},
\qquad
U_k\Subset\Z^d\setminus\{0\}.
$$

Then the update family at \(i\) is

$$
\mathcal U_i=\{i+U:U\in\mathcal U\}.
$$

The constraint becomes

$$
c_i(\eta)=1
\quad\Longleftrightarrow\quad
\exists U\in\mathcal U\text{ such that }\eta(i+u)=0\text{ for all }u\in U.
$$

## Monotonicity

With the convention that \(0\) is facilitating, constraints are decreasing in the product order on configurations: changing more sites from \(0\) to \(1\) can only destroy legal updates. This monotonicity is a property of the constraint, not of the full dynamics, and KCSM are generally non-attractive.
