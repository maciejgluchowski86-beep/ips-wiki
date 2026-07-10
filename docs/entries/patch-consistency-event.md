---
title: Patch consistency event
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Patch consistency event

Fix a [patch](patch.md)

$$
P=\{i\}\times[s,t)
$$

before horizon \(T\). Let \(I\) be the interaction set of the underlying [signed additive set process](signed-additive-set-process.md). The patch interaction set is

$$
\Pi_P
=
\{(j,s,\alpha,S)\in I:s>0,\ S\ne\vn,\ j=i\text{ or }i\in S\}
\cup
\{(i,u,\alpha,S)\in I:s<u<t\}.
$$

Thus \(\Pi_P\) contains the interaction that begins the patch, unless \(s=0\), together with the source-\(i\) interactions strictly inside the patch.

The local patch measure \(\mathbb P_P\) is the law of \(\Pi_P\). Write \(\mathbb E_P\) for expectation under \(\mathbb P_P\). Under \(\mathbb P_P\), the local active indicator is

$$
X^P_u=\mathbf 1_{\{i\in A_u\}},
\qquad s\le u<t.
$$

Its initial value is read from the initial boundary of \(P\):

$$
X^P_s
=
\begin{cases}
1, & \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\
\mathbf 1_{\{(i,s,\beta,S)\in\Pi_P\text{ for some }S\ne\vn\}}, & \operatorname{type}_-(P)=\mathsf O.
\end{cases}
$$

Inside \((s,t)\), deaths and splits set \(X^P\) to \(0\) when \(X^P\) is active, births leave it active, and interactions arriving while \(X^P\) is inactive are ignored.

The initial boundary consistency event is

$$
C_-(P)
=
\begin{cases}
\{i\in A_0\}, & \operatorname{type}_-(P)=\mathsf S,\\
\{(j,s,\alpha,S)\in\Pi_P\text{ for some }j,\alpha,S\text{ with }i\in S\}, & \operatorname{type}_-(P)=\mathsf I,\\
\{(i,s,\alpha,S)\in\Pi_P\text{ for some }\alpha\in\{\delta,\beta\},\ S\ne\vn\}, & \operatorname{type}_-(P)=\mathsf O.
\end{cases}
$$

The terminal boundary consistency event is

$$
C_+(P)
=
\begin{cases}
\{X^P_{t-}=1\}, & \operatorname{type}_+(P)=\mathsf O,\\
\Omega_P, & \operatorname{type}_+(P)\ne\mathsf O.
\end{cases}
$$

The consistency event of \(P\) is

$$
\operatorname{Cons}(P)
=
C_-(P)
\cap
\left\{
X^P_{u-}=0
\text{ for every }(i,u,\alpha,S)\in\Pi_P\text{ with }s<u<t\text{ and }S\ne\vn
\right\}
\cap C_+(P).
$$

Here \(\Omega_P\) is the sample space of the local interaction process. The condition \(C_-(P)\) says that the patch begins at an active site at time \(0\), at an incoming successful interaction, or at an outgoing successful interaction, according to its initial type. The interior condition says that no split or birth from source \(i\) is attempted while \(i\) is active in the interior of the patch. The condition \(C_+(P)\) says that an outgoing terminal boundary can occur only if the source is active immediately before that boundary.

Define \(\mathbb P_P^{\operatorname{cons}}\) as the regular conditional law of \(\mathbb P_P\) given \(\operatorname{Cons}(P)\). Write \(\mathbb E_P^{\operatorname{cons}}\) for expectation under \(\mathbb P_P^{\operatorname{cons}}\).
