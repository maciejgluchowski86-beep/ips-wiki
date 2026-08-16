---
title: Patch
status: definition
audit: current
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Patch

Fix the [graphical construction](graphical-construction-of-signed-additive-set-process.md) of a signed additive set process and its all-time [successful-interaction](successful-interaction.md) skeleton $\mathcal I$. The deterministic initial record is $(\infty,0,A_0)$.

A record $(j,t,S)\in\mathcal I$ gives an **incoming** successful interaction at every site in $S$. If $j\ne\infty$, it also gives an **outgoing** successful interaction at its source $j$. Thus the initial record gives only incoming interactions, while every ordinary record gives one outgoing interaction and one incoming interaction at each target site.

For $i\in\Lambda$, put

$$
\mathcal T^{\mathsf I}(i)
=
\{t\ge0:(j,t,S)\in\mathcal I\text{ for some }j,S\text{ with }i\in S\},
$$

$$
\mathcal T^{\mathsf O}(i)
=
\{t>0:(i,t,S)\in\mathcal I\text{ for some }S\},
$$

and

$$
\mathcal T(i)
=
\mathcal T^{\mathsf I}(i)\cup\mathcal T^{\mathsf O}(i).
$$

For $s\in\mathcal T(i)$ define the next successful interaction involving $i$ by

$$
e_i(s)
=
\inf\{u>s:u\in\mathcal T(i)\},
\qquad
\inf\varnothing=\infty.
\tag{1}
$$

## Definition

Let $(j,s,S)\in\mathcal I$ be a record involving $i$, meaning that $i\in S$ or $i=j$. The patch beginning at $(i,s)$ is the labeled tuple

$$
P
=
\bigl(i(P),[s(P),e(P)),\mathsf X(P)\mathsf Y(P),S(P)\bigr),
\tag{2}
$$

where

$$
i(P)=i,
\qquad
s(P)=s,
\qquad
e(P)=e_i(s),
\qquad
S(P)=S.
$$

Its initial label is

$$
\mathsf X(P)
=
\begin{cases}
\mathsf I,&i(P)\in S(P),\\
\mathsf O,&i(P)\notin S(P),
\end{cases}
\tag{3}
$$

and its terminal label is

$$
\mathsf Y(P)
=
\begin{cases}
\mathsf I,&e(P)<\infty\text{ and }e(P)\in\mathcal T^{\mathsf I}(i(P)),\\
\mathsf O,&e(P)<\infty\text{ and }e(P)\in\mathcal T^{\mathsf O}(i(P)),\\
\mathsf E,&e(P)=\infty.
\end{cases}
\tag{4}
$$

Thus the boundary labels have the following meanings:

- $\mathsf I$ at the initial boundary means the patch begins with an incoming successful interaction;
- $\mathsf O$ at the initial boundary means it begins with an outgoing successful interaction;
- $\mathsf I$ at the terminal boundary means the next successful interaction at the site is incoming;
- $\mathsf O$ at the terminal boundary means the next successful interaction at the site is outgoing;
- $\mathsf E$ means there is no later successful interaction involving the site.

The six possible boundary types are

$$
\mathsf{II},\ \mathsf{IO},\ \mathsf{IE},
\qquad
\mathsf{OI},\ \mathsf{OO},\ \mathsf{OE}.
$$

Let $\mathcal P$ be the family of all patches. Every patch with terminal label $\mathsf E$ is infinite, and every other full patch is finite.

The successful-interaction skeleton fixes the patch boundaries but deliberately omits the split/birth kind of an outgoing successful interaction, all empty-target death clocks, and all rings at inactive sources. Those omitted marks are the random data averaged under the [consistent patch law](patch-consistency-event.md).

## Finite-horizon truncation

Fix $t\ge0$. For a patch $P\in\mathcal P$ with $s(P)\le t$, define its truncation $P^{\downarrow t}$ by

$$
P^{\downarrow t}
=
\left(
 i(P),
 [s(P),\min\{e(P),t\}),
 \mathsf X(P)\mathsf Y^{\downarrow t}(P),
 S(P)
\right),
\tag{5}
$$

where

$$
\mathsf Y^{\downarrow t}(P)
=
\begin{cases}
\mathsf Y(P),&e(P)\le t,\\
\mathsf E,&t<e(P).
\end{cases}
$$

The bulk and end patch families are

$$
\mathcal B_t
=
\{P\in\mathcal P:e(P)\le t\},
$$

and

$$
\mathcal E_t
=
\{P^{\downarrow t}:P\in\mathcal P,\ s(P)\le t<e(P)\}.
$$

The finite-horizon patch family is

$$
\mathcal P_t
=
\mathcal B_t\cup\mathcal E_t.
\tag{6}
$$

It is finite almost surely. Distinct end patches have distinct base sites because the successful-interaction times partition each site line into consecutive intervals.

The canonical paper formulates its finite-horizon representation directly with $\mathcal B_t$ and $\mathcal E_t$; no separate cut-patch family is needed.

## Geometric extension

If $P$ is an end patch and $u\ge e(P)$ is finite, its extension through time $u$ is the geometric patch

$$
P^{\uparrow u}
=
\bigl(i(P),[s(P),u),\mathsf X(P)\mathsf E,S(P)\bigr).
\tag{7}
$$

Thus $P^{\uparrow e(P)}=P$. This notation changes only the patch shape. It does **not** assert that the extension occurs in the realized successful-interaction skeleton, and it does **not** include the probability that no successful interaction interrupts the added interval. The ordinary contribution of $P^{\uparrow u}$ is given by the [patch contribution](patch-contribution.md) formulas. The probability-weighted continuation identity is a separate result proved in [late interactions and no-late relaxation](exponential-relaxation-under-confined-late-interactions.md).
