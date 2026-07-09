---
title: Legal update
status: definition
tags:
  - KCSM
  - graphical construction
  - constraints
---

# Legal update

A legal update is a clock ring at which the local kinetic constraint is satisfied. The term is used for [kinetically constrained spin models](kinetically-constrained-spin-model.md) and their graphical constructions.

## Definition

Let \((\eta_t)_{t\ge0}\) be a KCSM with constraints \((c_i)_{i\in\Lambda}\). Suppose the clock at site \(i\) rings at time \(t\). The ring is legal if

$$
c_i(\eta_{t-})=1.
$$

If the ring is legal, the spin at \(i\) is refreshed according to the [Bernoulli refresh operator](bernoulli-refresh-operator.md): it becomes \(0\) with probability \(q\) and \(1\) with probability \(p=1-q\). If the ring is not legal, the configuration does not change.

## Legal paths

A finite sequence of configurations

$$
\eta_0,\eta_1,\ldots,\eta_n
$$

is a legal path if each transition \(\eta_k\to\eta_{k+1}\) changes at most one site and, whenever it changes site \(i\), the constraint at \(i\) is satisfied in \(\eta_k\).

Legal paths are used to describe communication classes, blocked configurations, and the connection between KCSM and bootstrap percolation.
