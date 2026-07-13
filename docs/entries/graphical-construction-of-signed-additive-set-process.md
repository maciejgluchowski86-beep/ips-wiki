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

The graphical construction realizes a [signed additive set process](signed-additive-set-process.md) from an initial interaction and independent Poisson interactions in spacetime. Together, these interactions determine the full path \((A_t,\sigma_t)\).

## Poisson interaction sets

For every \(i\in\Lambda\) and \(S\subseteq N(i)\), let

$$
I_{i,S}^\delta\subseteq(0,\infty)
$$

be a Poisson point process of rate \(\delta_i(S)\). Its times are deaths when \(S=\vn\), and splits when \(S\ne\vn\).

For every \(i\in\Lambda\) and nonempty \(S\subseteq N(i)\), let

$$
I_{i,S}^\beta\subseteq(0,\infty)
$$

be a Poisson point process of rate \(\beta_i(S)\). Its times are births.

All processes

$$
\{I_{i,S}^\delta\}_{i,S}
\qquad\text{and}\qquad
\{I_{i,S}^\beta\}_{i,S\ne\vn}
$$

are independent. Their marked interaction set is

$$
I^{\mathrm{P}}
=
\{(i,t,\delta,S):t\in I_{i,S}^\delta\}
\cup
\{(i,t,\beta,S):t\in I_{i,S}^\beta\}.
$$

For \((i,t,\alpha,S)\in I^{\mathrm P}\), the site \(i\) is the interaction source and \(S\) is the interaction target. Deaths have empty target. Splits and births have nonempty target.

## Initial interaction

Adjoin a formal source

$$
\infty\notin\Lambda
$$

and a special interaction kind \(\mathsf{init}\notin\{\delta,\beta\}\). For the prescribed initial state \(Y_0=(A_0,\sigma_0)\), define the deterministic signed initial interaction

$$
\iota_0
=
(\infty,0,\mathsf{init},A_0;\sigma_0).
$$

Its source is \(\infty\), its target is \(A_0\), its sign is \(\sigma_0\), and it has no rate. The full interaction set is

$$
I
=
\{\iota_0\}\cup I^{\mathrm P}.
$$

The initial interaction creates the initial active set and assigns its sign. Formally, start from

$$
Y_{0-}=(\vn,+)
$$

and apply \(\iota_0\) by setting

$$
Y_0=(A_0,\sigma_0).
$$

The formal source is not a lattice site and never becomes active. The initial interaction creates no source-side patch; it records the creation of its target together with the sign \(\sigma_0\).

Assume the usual local-finiteness condition: starting from any finite active set, only finitely many relevant Poisson interactions are encountered on every bounded time interval. This holds, for example, in the finite-range bounded-rate setting.

## Pathwise construction

After the initial interaction, read the interactions of \(I^{\mathrm P}\) in increasing time order. If several interactions occur at the same time, use any fixed deterministic ordering; this convention is irrelevant almost surely.

At an interaction \((i,t,\delta,S)\), set

$$
Y_t=
\begin{cases}
D_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

At an interaction \((i,t,\beta,S)\), set

$$
Y_t=
\begin{cases}
B_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

Between interactions, keep \(Y_t\) constant. Write

$$
Y_t=(A_t,\sigma_t).
$$

Thus inactive-source Poisson interactions are ignored, while active-source Poisson interactions apply the corresponding update operator.

## Lemma

For every prescribed initial state \(Y_0=(A_0,\sigma_0)\), the process \((Y_t)_{t\ge0}\) constructed from \(I\) is the signed additive set process with generator \(\cD\).

## Proof

The deterministic interaction \(\iota_0\) only installs the prescribed initial state. After time zero, fix a state \(Y=(A,\sigma)\). Conditional on \(Y_t=Y\), only Poisson interactions whose source lies in \(A\) can change the state. For \(h\downarrow0\), the probability that exactly one relevant death or split \((i,\cdot,\delta,S)\) occurs in \((t,t+h]\) is

$$
\delta_i(S)h+o(h),
$$

and the resulting state is \(D_{i,S}Y\). Similarly, for \(S\ne\vn\), the probability that exactly one relevant birth \((i,\cdot,\beta,S)\) occurs in \((t,t+h]\) is

$$
\beta_i(S)h+o(h),
$$

and the resulting state is \(B_{i,S}Y\). The probability of two or more relevant Poisson interactions in \((t,t+h]\) is \(o(h)\).

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
