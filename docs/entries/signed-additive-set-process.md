---
title: Signed additive set process
status: definition
tags:
  - duality
  - additive process
  - spin systems
---

# Signed additive set process

A signed additive set process is a Markov process on finite subsets of a [lattice](lattice-and-graph.md), with an additional sign coordinate,

$$
(A_t,\sigma_t)\in\{A:A\Subset\Lambda\}\times\{+,-\}.
$$

Signs are multiplied by the usual sign rule, and act on real numbers by \(+x=x\) and \(-x=-x\). The process is designed for finite-set [duality](duality.md) formulas for [spin systems](spin-system.md). In [monomial duality for spin systems](monomial-duality-for-spin-systems.md), the set coordinate indexes the [monomial](monomials.md) and the sign coordinate records signs of coefficients.

It is specified by nonnegative rates

$$
\delta_i(S),\quad \beta_i(S)\ge0,
\qquad i\in\Lambda,
\quad S\subseteq N(i),
$$

and sign labels

$$
\sigma_i^\delta(S),\quad \sigma_i^\beta(S)\in\{+,-\}.
$$

The convention is

$$
\beta_i(\vn)=0.
$$

For \(Y=(A,\sigma)\) with \(i\in A\), define

$$
D_{i,S}Y=\left((A\setminus\{i\})\cup S,\sigma\sigma_i^\delta(S)\right),
$$

and

$$
B_{i,S}Y=\left(A\cup S,\sigma\sigma_i^\beta(S)\right).
$$

The update \(D_{i,\vn}\) is a death. It removes the source site \(i\) and changes the sign by \(\sigma_i^\delta(\vn)\).

For \(S\ne\vn\), the update \(D_{i,S}\) is a split. It removes the source site \(i\), activates \(S\), and changes the sign by \(\sigma_i^\delta(S)\). It occurs at rate \(\delta_i(S)\).

For \(S\ne\vn\), the update \(B_{i,S}\) is a birth. It keeps the source site \(i\), activates \(S\), and changes the sign by \(\sigma_i^\beta(S)\). It occurs at rate \(\beta_i(S)\). The convention \(\beta_i(\vn)=0\) removes the empty birth.

## Generator

The generator is

$$
\begin{aligned}
\cD f(Y)
={}&
\sum_{i\in A}\sum_{S\subseteq N(i)}\delta_i(S)
\left(f(D_{i,S}Y)-f(Y)\right)\\
&+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\ne\vn}}
\beta_i(S)\left(f(B_{i,S}Y)-f(Y)\right),
\qquad Y=(A,\sigma).
\end{aligned}
$$

Ignoring the sign coordinate, deaths, splits, and births preserve unions. The sign is an additional coordinate carried by the dual process.