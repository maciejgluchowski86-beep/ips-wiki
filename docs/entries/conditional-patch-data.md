---
title: Conditional patch data
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Conditional patch data

Fix a [patch](patch.md)

$$
P=\{i\}\times[s,t)
$$

before horizon \(T\). The conditional patch data of \(P\) is the \(\cG_T\)-measurable endpoint data attached to its two boundary times.

Write \(\operatorname{type}_-(P)\) and \(\operatorname{type}_+(P)\) for the initial and terminal boundary types of \(P\). Define the initial boundary mark by

$$
M_-(P)=
\begin{cases}
\vn, & \operatorname{type}_-(P)=\mathsf S,\\
(j,s,\alpha,R), & \operatorname{type}_-(P)=\mathsf I,\ (j,s,\alpha,R)\in\mathcal I_T^R,\ i\in R,\\
(i,s,\beta,R), & \operatorname{type}_-(P)=\mathsf O,\ (i,s,\beta,R)\in\mathcal I_T^R.
\end{cases}
$$

Define the terminal boundary mark by

$$
M_+(P)=
\begin{cases}
\vn, & \operatorname{type}_+(P)=\mathsf E,\\
(j,t,\alpha,R), & \operatorname{type}_+(P)=\mathsf I,\ (j,t,\alpha,R)\in\mathcal I_T^R,\ i\in R,\\
(i,t,\alpha,R), & \operatorname{type}_+(P)=\mathsf O,\ (i,t,\alpha,R)\in\mathcal I_T^R.
\end{cases}
$$

The conditional patch data is

$$
\mathfrak D_T(P)
=
\left(i,s,t,\operatorname{type}_-(P),\operatorname{type}_+(P),M_-(P),M_+(P)\right).
$$

The collection

$$
\mathfrak D_T=\{\mathfrak D_T(P):P\in\mathcal P_T\}
$$

is determined by \(\cG_T\). On the null event of non-unique boundary marks, use the deterministic ordering fixed in the graphical construction.