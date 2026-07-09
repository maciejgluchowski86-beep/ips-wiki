---
title: Signed additive set process
status: definition
tags:
  - duality
  - additive process
  - spin systems
---

# Signed additive set process

A signed additive set process is a Markov process

$$
(A_t,\sigma_t)\in\{A:A\Subset\Lambda\}\times\{-1,+1\}.
$$

It is specified by nonnegative rates

$$
\delta_i(S),\quad \beta_i(S)\ge0,
\qquad i\in\Lambda,\quad S\subseteq N(i),
$$

and sign labels

$$
\sigma_i^\delta(S),\quad \sigma_i^\beta(S)\in\{-1,+1\}.
$$

For \(i\in A\), define the source-killing and source-keeping set maps

$$
D_{i,S}A=(A\setminus\{i\})\cup S,
\qquad
B_{i,S}A=A\cup S.
$$

A source-killing update with source \(i\) and activated neighbour set \(S\) is

$$
(A,\sigma)\to(D_{i,S}A,\sigma\sigma_i^\delta(S))
$$

and occurs at rate \(\delta_i(S)\). It removes the source site \(i\) and activates \(S\).

A source-keeping update with source \(i\) and activated neighbour set \(S\) is

$$
(A,\sigma)\to(B_{i,S}A,\sigma\sigma_i^\beta(S))
$$

and occurs at rate \(\beta_i(S)\). It keeps the source site \(i\) and activates \(S\). This update is still included when \(B_{i,S}A=A\); in that case it may only change the sign coordinate.

## Generator

The generator is

$$
\begin{aligned}
\cD F(A,\sigma)
={}&
\sum_{i\in A}\sum_{S\subseteq N(i)}\delta_i(S)
\left(F(D_{i,S}A,\sigma\sigma_i^\delta(S))-F(A,\sigma)\right)\\
&+
\sum_{i\in A}\sum_{S\subseteq N(i)}\beta_i(S)
\left(F(B_{i,S}A,\sigma\sigma_i^\beta(S))-F(A,\sigma)\right).
\end{aligned}
$$

Ignoring the sign coordinate, the source-killing and source-keeping maps preserve unions. The sign is an additional coordinate carried by the dual process.
