---
title: Patch
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Patch

Fix a [signed additive set process](signed-additive-set-process.md), its [graphical construction](graphical-construction-of-signed-additive-set-process.md), and the full successful-interaction set \(\mathcal I\). A successful interaction \((i,t,S)\) touches its source \(i\) as an outgoing touch and each target \(j\in S\) as an incoming touch.

For \(i\in\Lambda\), define

$$
\begin{aligned}
\mathcal T^{\mathsf I}(i)
&=
\left\{
t\ge0:
\text{some }(j,t,S)\in\mathcal I
\text{ satisfies }i\in S
\right\},
\\
\mathcal T^{\mathsf O}(i)
&=
\left\{
t\ge0:
\text{some }(i,t,S)\in\mathcal I
\right\}.
\end{aligned}
$$

The possible starting times at \(i\) are

$$
\mathcal S(i)
=
\mathcal S^0(i)
\cup\mathcal T^{\mathsf I}(i)
\cup\mathcal T^{\mathsf O}(i),
\qquad
\mathcal S^0(i)
=
\begin{cases}
\{0\}, & i\in A_0,\\
\vn, & i\notin A_0.
\end{cases}
$$

For \(s\in\mathcal S(i)\), let

$$
r_i(s)
=
\inf\left\{
u>s:
u\in\mathcal T^{\mathsf I}(i)\cup\mathcal T^{\mathsf O}(i)
\right\},
$$

with \(\inf\vn=\infty\). The patch beginning at \((i,s)\) is

$$
P=\{i\}\times[s,r_i(s)).
$$

The set of all patches is denoted by \(\mathcal P\). A patch is finite when \(r_i(s)<\infty\), and infinite when \(r_i(s)=\infty\).

Every initially active site begins a patch at time \(0\). Every successful interaction cuts spacetime at its source and target sites, ending the preceding patches and beginning new ones at those sites. Every active spacetime point belongs to a patch.

Under the local-finiteness assumption, starting from \(A_0\Subset\Lambda\),

$$
\left|\mathcal P\right|<\infty
\quad\Longleftrightarrow\quad
\left|\mathcal I\right|<\infty.
$$

Indeed, every successful interaction creates patch boundaries. Conversely, finitely many successful interactions touch only finitely many sites and create only finitely many patches, including the final infinite patches.

## Finite time horizon

For \(T<\infty\) and \(P=\{i\}\times[s,r)\in\mathcal P\) with \(s<T\), define its truncation at \(T\) by

$$
P^{(T)}
=
\{i\}\times[s,\min\{r,T\}).
$$

The family of all such truncations is denoted by \(\mathcal P_T\). Its incoming and outgoing touch-time sets are

$$
\mathcal T_T^{\mathsf I}(i)
=
\mathcal T^{\mathsf I}(i)\cap[0,T],
\qquad
\mathcal T_T^{\mathsf O}(i)
=
\mathcal T^{\mathsf O}(i)\cap[0,T].
$$

For \(P^{(T)}=\{i\}\times[s,t)\), the initial and terminal types are

$$
\operatorname{type}_-(P^{(T)})
=
\begin{cases}
\mathsf S, & s=0,\\
\mathsf I, & s\in\mathcal T_T^{\mathsf I}(i),\\
\mathsf O, & s\in\mathcal T_T^{\mathsf O}(i),
\end{cases}
\qquad
\operatorname{type}_+(P^{(T)})
=
\begin{cases}
\mathsf E, & t=T,\\
\mathsf I, & t\in\mathcal T_T^{\mathsf I}(i),\\
\mathsf O, & t\in\mathcal T_T^{\mathsf O}(i).
\end{cases}
$$

The patch type is

$$
\operatorname{type}(P^{(T)})
=
\operatorname{type}_-(P^{(T)})
\operatorname{type}_+(P^{(T)}).
$$

The possible types are

$$
\mathsf{SI},\ \mathsf{SO},\ \mathsf{SE},\quad
\mathsf{II},\ \mathsf{IO},\ \mathsf{IE},\quad
\mathsf{OI},\ \mathsf{OO},\ \mathsf{OE}.
$$

The end and bulk patch sets at horizon \(T\) are

$$
\mathcal E_T
=
\left\{
P\in\mathcal P_T:
\operatorname{type}_+(P)=\mathsf E
\right\},
\qquad
\mathcal B_T
=
\mathcal P_T\setminus\mathcal E_T.
$$

Thus bulk patches end at successful touches, while end patches are truncations of full patches at the time horizon. Their local factors are defined in [patch contribution](patch-contribution.md).

On the null event of simultaneous successful touches at the same site, use the deterministic ordering fixed in the graphical construction.
