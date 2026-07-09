---
title: Oriented spin system
status: definition
tags:
  - oriented lattice
  - spin systems
---

# Oriented spin system

An oriented spin system is a [spin system](spin-system.md) on an oriented [lattice](lattice-and-graph.md).

## Oriented lattice

The lattice \(\Lambda\) is equipped with neighbour sets \(N(i)\). Write

$$
i\to j
$$

if there is a finite chain

$$
i=i_0,i_1,\ldots,i_n=j
$$

such that \(i_{k+1}\in N(i_k)\) for every \(k<n\). The lattice is oriented if, whenever \(i\to j\) and \(i\ne j\), one has not \(j\to i\).

Thus information can follow neighbour sets, but it cannot return to where it started.

## Oriented spin system

A spin system on an oriented lattice is called an oriented spin system. No extra notation is needed: the orientation is already contained in the neighbour sets \(N(i)\).

For a local spin system, the flip rate at site \(i\) is still written as \(c_i(\eta)\), and it is still a function of finitely many coordinates in \(N_*(i)=N(i)\cup\{i\}\).

## Oriented KCSM

A [kinetically constrained spin model](kinetically-constrained-spin-model.md) on an oriented lattice is an oriented KCSM. Its update families satisfy

$$
\mathcal U_i\subseteq\{U:U\Subset N(i)\}.
$$

The [East model](east-model.md) is the basic example.
