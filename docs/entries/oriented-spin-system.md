---
title: Oriented spin system
status: definition
tags:
  - oriented lattice
  - spin systems
  - KCSM
---

# Oriented spin system

An oriented spin system is a [spin system](spin-system.md) on a directed lattice whose update rates depend only on sites in the allowed direction of information flow. The basic condition is that information cannot return to where it started.

## Oriented lattice

An oriented lattice is a lattice \(\Lambda\) equipped with a directed graph structure and no directed cycles. Write

$$
j\to i
$$

when information is allowed to flow from \(j\) to \(i\), or equivalently when \(j\) may influence the update at \(i\). Define the predecessor and successor sets by

$$
\operatorname{Pred}(i)=\{j\in\Lambda:j\to i\},
\qquad
\operatorname{Succ}(i)=\{j\in\Lambda:i\to j\}.
$$

The absence of directed cycles means there is no finite sequence

$$
i_0\to i_1\to\cdots\to i_n=i_0
$$

with \(n\ge1\). This is the structural condition that prevents information from flowing back.

## Oriented spin system

A spin system on an oriented lattice is oriented if the flip rate at \(i\) depends only on the spin at \(i\) and on finitely many predecessors of \(i\). Thus there is a finite set

$$
D(i)\Subset \operatorname{Pred}(i)\cup\{i\}
$$

such that \(c_i(\eta)\) depends only on \(\eta|_{D(i)}\).

## Oriented KCSM

A [kinetically constrained spin model](kinetically-constrained-spin-model.md) is oriented if each update rule at \(i\) uses only predecessors of \(i\):

$$
\mathcal U_i\subseteq\{U:U\Subset\operatorname{Pred}(i)\}.
$$

The [East model](east-model.md) is the basic example. With the convention \(j\to i\) meaning that \(j\) facilitates \(i\), the one-dimensional East model has arrows \(i+1\to i\).
