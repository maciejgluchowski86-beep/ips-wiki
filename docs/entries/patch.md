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

Fix a [signed additive set process](signed-additive-set-process.md), its [graphical construction](graphical-construction-of-signed-additive-set-process.md), and a horizon \(T<\infty\). Let \(\mathcal I_T^S\) be the type-\(S\) [successful interaction](successful-interaction.md) set.

A type-\(S\) successful interaction \((i,t,S)\) touches its source \(i\) as an outgoing touch and each target \(j\in S\) as an incoming touch. For \(i\in\Lambda\), define the incoming and outgoing successful-touch times by

$$
\begin{aligned}
\mathcal T_T^{\mathsf I}(i)
&=
\{t\le T:\exists j\in\Lambda,\ \exists S\ne\vn
\text{ with }(j,t,S)\in\mathcal I_T^S\text{ and }i\in S\},
\\
\mathcal T_T^{\mathsf O}(i)
&=
\{t\le T:\exists S\ne\vn
\text{ with }(i,t,S)\in\mathcal I_T^S\}.
\end{aligned}
$$

The initial activity contribution to possible starting times is

$$
\mathcal S_T^0(i)
=
\begin{cases}
\{0\}, & i\in A_0,\\
\vn, & i\notin A_0.
\end{cases}
$$

The possible initial and terminal boundary times are

$$
\begin{aligned}
\mathcal S_T(i)
&=
\mathcal S_T^0(i)
\cup\mathcal T_T^{\mathsf I}(i)
\cup\mathcal T_T^{\mathsf O}(i),
\\
\mathcal R_T(i)
&=
\{T\}\cup\mathcal T_T^{\mathsf I}(i)\cup\mathcal T_T^{\mathsf O}(i).
\end{aligned}
$$

A patch at \(i\) is a spacetime interval

$$
P=\{i\}\times [s,t)
$$

where \(s\in\mathcal S_T(i)\), \(t\in\mathcal R_T(i)\), \(s<t\), and there is no element of \(\mathcal S_T(i)\cup\mathcal R_T(i)\) strictly between \(s\) and \(t\). The set of all patches before horizon \(T\) is denoted by \(\mathcal P_T\).

For \(P=\{i\}\times[s,t)\), the initial and terminal types are

$$
\operatorname{type}_-(P)
=
\begin{cases}
\mathsf S, & s=0,\\
\mathsf I, & s\in\mathcal T_T^{\mathsf I}(i),\\
\mathsf O, & s\in\mathcal T_T^{\mathsf O}(i),
\end{cases}
\qquad
\operatorname{type}_+(P)
=
\begin{cases}
\mathsf E, & t=T,\\
\mathsf I, & t\in\mathcal T_T^{\mathsf I}(i),\\
\mathsf O, & t\in\mathcal T_T^{\mathsf O}(i).
\end{cases}
$$

The patch type is

$$
\operatorname{type}(P)
=
\operatorname{type}_-(P)\operatorname{type}_+(P).
$$

The possible types are

$$
\mathsf{SI},\ \mathsf{SO},\ \mathsf{SE},\quad
\mathsf{II},\ \mathsf{IO},\ \mathsf{IE},\quad
\mathsf{OI},\ \mathsf{OO},\ \mathsf{OE}.
$$

The end patches and bulk patches are

$$
\mathcal E_T
=
\{P\in\mathcal P_T:\operatorname{type}_+(P)=\mathsf E\},
\qquad
\mathcal B_T
=
\mathcal P_T\setminus\mathcal E_T.
$$

Equivalently, \(\mathcal B_T\) consists of patches whose terminal boundary is a successful incoming or outgoing touch, while \(\mathcal E_T\) consists of patches reaching the time horizon. The distinction is used in [patch contributions](patch-contribution.md): bulk patches have contribution \(C(P)\), while end patches have contribution \(C(\xi,P)\).

Every initially active site begins a patch at time \(0\). Every successful interaction cuts spacetime at both its source and target sites, so it is a terminal boundary for the patch immediately before the interaction, if such a patch is present, and an initial boundary for the patch immediately after the interaction at each touched site.

Every active spacetime point is contained in a patch. Interactions outside patches have inactive source, except for interactions on successful boundary times already recorded by \(\mathcal I_T^S\).

On the null event of simultaneous successful touches at the same site, use the deterministic ordering of interactions fixed in the graphical construction.
