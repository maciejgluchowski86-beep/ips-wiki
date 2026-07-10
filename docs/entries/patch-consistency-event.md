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

before horizon \(T\). Let \(I\) be the interaction set of the underlying [signed additive set process](signed-additive-set-process.md). The internal interaction set of \(P\) is

$$
\Pi_P
=
\{(i,u,\alpha,S)\in I:s<u<t\}.
$$

The local patch measure \(\mathbb P_P\) is the law of the source-\(i\) Poisson interaction processes restricted to \((s,t)\). Under \(\mathbb P_P\), the local active indicator is

$$
X^P_u=\mathbf 1_{\{i\in A_u\}},
\qquad s\le u<t.
$$

Its initial value is fixed by the initial boundary of \(P\):

$$
X^P_s
=
\begin{cases}
1, & \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\
\mathbf 1_{\{(i,s,\beta,S)\in\mathcal I_T^S\text{ for some }S\ne\vn\}}, & \operatorname{type}_-(P)=\mathsf O.
\end{cases}
$$

Inside \((s,t)\), source-killing interactions set \(X^P\) to \(0\) when \(X^P\) is active, source-keeping interactions leave it active, and interactions arriving while \(X^P\) is inactive are ignored.

The consistency event of \(P\) is

$$
\operatorname{Cons}(P)
=
\left\{
X^P_{u-}=0
\text{ for every }(i,u,\alpha,S)\in\Pi_P\text{ with }S\ne\vn
\right\}
\cap C_+(P),
$$

where

$$
C_+(P)
=
\begin{cases}
\{X^P_{t-}=1\}, & \operatorname{type}_+(P)=\mathsf O,\\
\Omega_P, & \operatorname{type}_+(P)\ne\mathsf O.
\end{cases}
$$

Here \(\Omega_P\) is the sample space of the local interaction process. The first condition says that no nonempty-target source interaction from \(i\) is attempted while \(i\) is active in the interior of the patch. The second condition says that an outgoing terminal boundary can occur only if the source is active immediately before that boundary.

When \(\mathbb P_P(\operatorname{Cons}(P))>0\), define the conditioned patch measure by

$$
\mathbb P_P^{\operatorname{cons}}(\cdot)
=
\mathbb P_P(\cdot\mid\operatorname{Cons}(P)).
$$
