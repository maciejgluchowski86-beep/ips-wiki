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

It is specified by two families of real weights

$$
\delta_i(S),\quad \beta_i(S)\in\R,
\qquad i\in\Lambda,\quad S\subseteq N(i).
$$

For \(i\in A\), define the source-killing and source-keeping set maps

$$
D_{i,S}A=(A\setminus\{i\})\cup S,
\qquad
B_{i,S}A=A\cup S.
$$

A nonzero weight \(\delta_i(S)\) gives the source-killing update

$$
(A,\sigma)\to(D_{i,S}A,\sigma\operatorname{sgn}\delta_i(S))
$$

at rate \(|\delta_i(S)|\). This update removes the source site \(i\) and activates the neighbour set \(S\).

A nonzero weight \(\beta_i(S)\) gives the source-keeping update

$$
(A,\sigma)\to(B_{i,S}A,\sigma\operatorname{sgn}\beta_i(S))
$$

at rate \(|\beta_i(S)|\), provided \(S\not\subseteq A\). This update keeps the source site \(i\) and activates the neighbour set \(S\).

The restriction \(S\not\subseteq A\) only removes null set updates from the Markov generator.

## Generator

The generator is

$$
\begin{aligned}
\cD F(A,\sigma)
={}&
\sum_{i\in A}\sum_{S\subseteq N(i)}|\delta_i(S)|
\left(F(D_{i,S}A,\sigma\operatorname{sgn}\delta_i(S))-F(A,\sigma)\right)\\
&+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\not\subseteq A}}|\beta_i(S)|
\left(F(B_{i,S}A,\sigma\operatorname{sgn}\beta_i(S))-F(A,\sigma)\right).
\end{aligned}
$$

The omitted source-keeping updates with \(S\subseteq A\) contribute the diagonal coefficient

$$
\Gamma(A)=\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\subseteq A}}\beta_i(S)
$$

in duality equations.

Ignoring the sign coordinate, the source-killing and source-keeping maps preserve unions. The sign is an additional coordinate carried by the dual process.
