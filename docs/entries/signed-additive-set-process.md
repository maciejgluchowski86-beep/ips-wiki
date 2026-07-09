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

It is specified by signed coefficients

$$
\delta_i(S),\quad \beta_i(S)\in\R,
\qquad i\in\Lambda,\quad S\subseteq N(i).
$$

The coefficient \(\delta_i(S)\) kills the source site \(i\) and activates \(S\). The coefficient \(\beta_i(S)\) keeps the source site \(i\) and activates \(S\).

For \(i\in A\), define

$$
D_{i,S}A=(A\setminus\{i\})\cup S,
\qquad
B_{i,S}A=A\cup S.
$$

The transitions are

$$
(A,\sigma)\to(D_{i,S}A,\sigma\operatorname{sgn}\delta_i(S))
$$

at rate \(|\delta_i(S)|\), and, when \(S\not\subseteq A\),

$$
(A,\sigma)\to(B_{i,S}A,\sigma\operatorname{sgn}\beta_i(S))
$$

at rate \(|\beta_i(S)|\). Coefficients equal to \(0\) produce no transition.

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

The omitted terms with \(S\subseteq A\) in the \(\beta\)-sum are null set updates. In duality formulas they contribute the diagonal coefficient

$$
\Gamma(A)=\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\subseteq A}}\beta_i(S).
$$

The unsigned set maps \(A\mapsto D_{i,S}A\) and \(A\mapsto B_{i,S}A\), applied only when \(i\in A\), preserve unions. The sign is an additional coordinate.
