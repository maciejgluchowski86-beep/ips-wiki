---
title: East model
status: definition
tags:
  - KCSM
  - East model
  - oriented model
---

# East model

The East model is an [oriented spin system](oriented-spin-system.md) and a [KCSM](kinetically-constrained-spin-model.md). A site may refresh only when at least one oriented neighbour is vacant. Equivalently, it is the [FA-1f model](fa-1f-model.md) on an oriented lattice.

**References.** Hartarsky and Toninelli, *Kinetically constrained models*; Cancrini, Martinelli, Schonmann, and Toninelli, *Facilitated oriented spin models: some non equilibrium results*; Marêché, *Exponential convergence to equilibrium for the \(d\)-dimensional East model*.

## Definition on an oriented lattice

Let \(\Lambda\) be an oriented [lattice](lattice-and-graph.md) with neighbour sets \(N(i)\). The East [update family](update-family.md) at \(i\) is

$$
\mathcal U_i=\bigl\{\{j\}:j\in N(i)\bigr\}.
$$

Therefore, in [monomial](monomials.md) notation,

$$
c_i(\eta)=\ind\{\exists j\in N(i):\eta(j)=0\}
=1-\chi_{N(i)}(\eta).
$$

The one-neighbour East model is the special case \(N(i)=\{j_i\}\), giving

$$
c_i(\eta)=1-\eta(j_i).
$$

## Generator

With vacancy density \(q\), occupied density \(p=1-q\), and [Bernoulli refresh operator](bernoulli-refresh-operator.md) \(E_i^q\), the generator is

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}\bigl(1-\chi_{N(i)}(\eta)\bigr)
\bigl(E_i^q f(\eta)-f(\eta)\bigr).
$$

Equivalently, a clock ring is a [legal update](legal-update.md) exactly when at least one oriented neighbour is vacant.

## One-dimensional East model

For the right-facilitated East model on \(\Lambda=\Z\), take

$$
N(i)=\{i+1\}.
$$

The corresponding constraint is

$$
c_i(\eta)=1-\eta(i+1).
$$

The site \(i\) can update exactly when its right neighbour is vacant. In this convention, \(i\to j\) means that \(j\) is reachable from \(i\) by repeatedly moving through neighbour sets, so the one-dimensional right-facilitated East lattice satisfies \(i\to j\) exactly when \(j\ge i\).

## Higher-dimensional East model

On \(\Z^d\), one standard East-like choice is

$$
N(i)=\{i+e_1,\ldots,i+e_d\},
$$

so that a site can update if at least one forward coordinate neighbour is vacant. Known convergence results are recorded in [East out of equilibrium](east-out-of-equilibrium.md).
