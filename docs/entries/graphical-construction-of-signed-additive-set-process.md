---
title: Graphical construction of signed additive set process
status: proved here
tags:
  - signed additive set process
  - graphical construction
  - Poisson construction
  - IPS
---

# Graphical construction of signed additive set process

The graphical construction realizes a [signed additive set process](signed-additive-set-process.md) from independent Poisson marks in spacetime. The marks, together with the initial state, determine the full path \((A_t,\sigma_t)\).

## Poisson mark sets

For every \(i\in\Lambda\) and \(S\subseteq N(i)\), let

$$
P_{i,S}^\delta\subseteq [0,\infty)
$$

be a Poisson point process of rate \(\delta_i(S)\). Its times are the source-killing marks of type \((i,S,\delta)\).

For every \(i\in\Lambda\) and nonempty \(S\subseteq N(i)\), let

$$
P_{i,S}^\beta\subseteq [0,\infty)
$$

be a Poisson point process of rate \(\beta_i(S)\). Its times are the source-keeping marks of type \((i,S,\beta)\).

All processes

$$
\{P_{i,S}^\delta\}_{i,S}
\qquad\text{and}\qquad
\{P_{i,S}^\beta\}_{i,S\ne\vn}
$$

are independent. Define the total mark set

$$
P
=
\{(i,t,\delta,S):t\in P_{i,S}^\delta\}
\cup
\{(i,t,\beta,S):t\in P_{i,S}^\beta\}.
$$

Assume the usual local-finiteness condition: starting from any finite active set, only finitely many relevant marks are encountered on every bounded time interval. This holds, for example, in the finite-range bounded-rate setting.

## Pathwise construction

Fix an initial state

$$
Y_0=(A_0,\sigma_0).
$$

Read the marks of \(P\) in increasing time order. If several marks occur at the same time, use any fixed deterministic ordering; this convention is irrelevant almost surely.

At a mark \((i,t,\delta,S)\), set

$$
Y_t=
\begin{cases}
D_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

At a mark \((i,t,\beta,S)\), set

$$
Y_t=
\begin{cases}
B_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

Between marks, keep \(Y_t\) constant. Write

$$
Y_t=(A_t,\sigma_t).
$$

Thus inactive-source marks are ignored, while active-source marks apply the corresponding update operator.

## Lemma

The process \((Y_t)_{t\ge0}\) constructed from the mark set \(P\) is the signed additive set process with generator \(\cD\).

## Proof

Fix a state \(Y=(A,\sigma)\). Conditional on \(Y_t=Y\), only marks whose source lies in \(A\) can change the state. For \(h\downarrow0\), the probability that exactly one relevant source-killing mark \((i,\cdot,\delta,S)\) occurs in \((t,t+h]\) is

$$
\delta_i(S)h+o(h),
$$

and the resulting state is \(D_{i,S}Y\). Similarly, for \(S\ne\vn\), the probability that exactly one relevant source-keeping mark \((i,\cdot,\beta,S)\) occurs in \((t,t+h]\) is

$$
\beta_i(S)h+o(h),
$$

and the resulting state is \(B_{i,S}Y\). The probability of two or more relevant marks in \((t,t+h]\) is \(o(h)\).

Therefore, for any bounded test function \(f\),

$$
\begin{aligned}
\frac{\E[f(Y_{t+h})-f(Y_t)\mid Y_t=Y]}{h}
\to{}&
\sum_{i\in A}\sum_{S\subseteq N(i)}
\delta_i(S)\left(f(D_{i,S}Y)-f(Y)\right)
\\
&+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\ne\vn}}
\beta_i(S)\left(f(B_{i,S}Y)-f(Y)\right).
\end{aligned}
$$

This is exactly the generator \(\cD\) of the signed additive set process.
