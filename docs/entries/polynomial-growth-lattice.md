---
title: Polynomial-growth lattice
status: definition
tags:
  - lattice
  - graph distance
  - polynomial growth
---

# Polynomial-growth lattice

Polynomial growth is a volume-growth condition on the graph determined by a [lattice](lattice-and-graph.md) and its neighbour sets. It is used in several out-of-equilibrium estimates for interacting particle systems, including the [FA-1f model](fa-1f-model.md).

## Graph distance

Let \(\Lambda\) be a connected lattice or graph with finite neighbour sets \(N(i)\). The graph distance is denoted by

$$
d(i,j).
$$

The ball of radius \(r\) around \(i\) is

$$
B(i,r)=\{j\in\Lambda:d(i,j)\le r\}.
$$

## Polynomial growth

The lattice has \((k,D)\)-polynomial growth if there are constants \(k<\infty\) and \(D>0\) such that

$$
\sup_{i\in\Lambda}|B(i,r)|\le k r^D
\qquad\text{for all }r\ge1.
$$

When only the existence of some such constants matters, one says that \(\Lambda\) has polynomial growth.

## Examples

The nearest-neighbour lattice \(\Z^d\) has polynomial growth with exponent \(D=d\), up to changing the constant \(k\). More generally, bounded-degree graphs with polynomial volume growth satisfy this condition for some \((k,D)\).

## Use in out-of-equilibrium estimates

Polynomial growth controls how many sites can be reached within distance \(r\). In the FA-1f out-of-equilibrium theorem, the exponent \(D\) determines the decay form: exponential for \(D=1\), and stretched exponential with exponent depending on \(D\) for \(D>1\).
