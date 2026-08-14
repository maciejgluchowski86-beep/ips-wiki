---
title: Graphical construction of signed additive set process
status: definition
audit: current
tags:
  - signed additive set process
  - graphical construction
  - Poisson construction
  - IPS
---

# Graphical construction of signed additive set process

The graphical construction realizes a [signed additive set process](signed-additive-set-process.md) from a deterministic initial interaction and independent Poisson interactions in spacetime. Together these interactions determine the càdlàg path $(A_t,\sigma_t)$.

## Poisson interaction sets

For every $i\in\Lambda$ and $S\subseteq N(i)$, let

$$
I_{i,S}^\delta\subseteq(0,\infty)
$$

be a Poisson point process of rate $\delta_i(S)$. Its times are deaths when $S=\vn$ and splits when $S\ne\vn$.

For every $i\in\Lambda$ and nonempty $S\subseteq N(i)$, let

$$
I_{i,S}^\beta\subseteq(0,\infty)
$$

be a Poisson point process of rate $\beta_i(S)$. Its times are births. All the processes $I_{i,S}^\delta$ and $I_{i,S}^\beta$ are independent. Their marked Poisson interaction set is

$$
I^{\mathrm P}
=
\{(i,t,\delta,S):t\in I_{i,S}^\delta\}
\cup
\{(i,t,\beta,S):t\in I_{i,S}^\beta\}.
$$

For $(i,t,\alpha,S)\in I^{\mathrm P}$, the site $i$ is the interaction source and $S$ is the interaction target. Deaths have empty target; splits and births have nonempty target.

## Initial interaction

Adjoin a formal source $\infty\notin\Lambda$ and a special interaction kind $\mathsf{init}\notin\{\delta,\beta\}$. For the prescribed initial state $Y_0=(A_0,\sigma_0)$, define the deterministic signed initial interaction

$$
\iota_0=(\infty,0,\mathsf{init},A_0;\sigma_0).
$$

Its source is $\infty$, its target is $A_0$, its sign is $\sigma_0$, and it has no rate. The full interaction set is

$$
I=\{\iota_0\}\cup I^{\mathrm P}.
$$

Start formally from $Y_{0-}=(\vn,+)$ and apply $\iota_0$ by setting $Y_0=(A_0,\sigma_0)$. The formal source is not a lattice site and never becomes active. The initial interaction creates no source-side patch; it records the creation of its target together with the sign $\sigma_0$. In the [successful-interaction](successful-interaction.md) convention, this initial interaction is declared successful and has source-time-target skeleton $(\infty,0,A_0)$.

Assume the usual local-finiteness condition: starting from any finite active set, only finitely many relevant Poisson interactions are encountered on every bounded time interval. This holds, for example, in the finite-range bounded-rate setting.

## Pathwise construction

After the initial interaction, read the interactions in $I^{\mathrm P}$ in increasing time order. If several occur at the same time, use any fixed deterministic ordering; simultaneous Poisson times have probability zero under the usual construction.

At an interaction $(i,t,\delta,S)$, set

$$
Y_t=
\begin{cases}
D_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

At an interaction $(i,t,\beta,S)$, set

$$
Y_t=
\begin{cases}
B_{i,S}Y_{t-}, & i\in A_{t-},\\
Y_{t-}, & i\notin A_{t-}.
\end{cases}
$$

Between interactions keep $Y_t$ constant and write $Y_t=(A_t,\sigma_t)$. Thus an interaction with inactive source is ignored, whereas an interaction with active source applies the corresponding update operator. For nonempty target $S$, an active-source split or birth is an ordinary successful interaction; deaths have empty target and are not successful interactions.

## Generator consistency

Fix a state $Y=(A,\sigma)$ after time zero. Conditional on $Y_t=Y$, only Poisson interactions with source in $A$ can change the state. During an interval of length $h$, a single death or split $(i,\cdot,\delta,S)$ occurs with probability $\delta_i(S)h+o(h)$ and sends $Y$ to $D_{i,S}Y$; a single birth $(i,\cdot,\beta,S)$ occurs with probability $\beta_i(S)h+o(h)$ and sends $Y$ to $B_{i,S}Y$. Local finiteness makes the probability of two or more relevant interactions $o(h)$. Hence, for bounded $f$,

$$
\begin{aligned}
\frac{\E[f(Y_{t+h})-f(Y_t)\mid Y_t=Y]}{h}
\longrightarrow{}&
\sum_{i\in A}\sum_{S\subseteq N(i)}
\delta_i(S)\bigl(f(D_{i,S}Y)-f(Y)\bigr)
\\
&+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\ne\vn}}
\beta_i(S)\bigl(f(B_{i,S}Y)-f(Y)\bigr).
\end{aligned}
$$

This is the generator $\cD$ in the [signed additive set process](signed-additive-set-process.md) definition.