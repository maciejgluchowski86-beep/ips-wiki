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

before horizon \(T\). Let \(I\) be the interaction set of the underlying [signed additive set process](signed-additive-set-process.md). The patch interaction data are

$$
\Pi_P
=
\Pi_P^-\cup\Pi_P^\circ,
$$

where

$$
\Pi_P^\circ
=
\{(i,u,\alpha,S)\in I:s<u<t\},
$$

and the initial-boundary data are

$$
\Pi_P^-
=
\begin{cases}
\vn, & s=0,\\
\{(j,s,S):S\ne\vn,\ i\in S,\ (j,s,\alpha,S)\in I\text{ for some }\alpha\in\{\delta,\beta\}\},
& \operatorname{type}_-(P)=\mathsf I,\\
\{(i,s,\alpha,S)\in I:S\ne\vn\},
& \operatorname{type}_-(P)=\mathsf O.
\end{cases}
$$

Thus an incoming initial boundary contributes only its source-time-target skeleton to \(\Pi_P\). An outgoing initial boundary contributes the update kind as well, because a birth keeps the source active while a split removes it.

The local patch measure \(\mathbb P_P\) is the law of \(\Pi_P\) conditional on the initial skeleton that begins the patch. If \(s=0\), this means only that the site is initially active. If \(\operatorname{type}_-(P)=\mathsf I\), the incoming skeleton \((j,s,S)\) with \(i\in S\) is fixed. If \(\operatorname{type}_-(P)=\mathsf O\), the source-time-target skeleton \((i,s,S)\) is fixed, but the update kind is sampled by

$$
\mathbb P_P((i,s,\beta,S)\in\Pi_P)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)},
\qquad
\mathbb P_P((i,s,\delta,S)\in\Pi_P)
=
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)}.
$$

The source-\(i\) interaction processes in \((s,t)\) have their original Poisson law. Write \(\mathbb E_P\) for expectation under \(\mathbb P_P\).

Under \(\mathbb P_P\), the local active indicator is

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
\left\{
X^P_{u-}=0
\text{ for every }(i,u,\alpha,S)\in\Pi_P\text{ with }s<u<t\text{ and }S\ne\vn
\right\}
\cap C_+(P).
$$

Here \(\Omega_P\) is the sample space of the local interaction process after the initial skeleton has been fixed. The interior condition says that no split or birth from source \(i\) is attempted while \(i\) is active in the interior of the patch. The condition \(C_+(P)\) says that an outgoing terminal boundary can occur only if the source is active immediately before that boundary.

When \(\mathbb P_P(\operatorname{Cons}(P))>0\), define the conditioned patch measure by

$$
\mathbb P_P^{\operatorname{cons}}(\cdot)
=
\mathbb P_P(\cdot\mid\operatorname{Cons}(P)).
$$

Write \(\mathbb E_P^{\operatorname{cons}}\) for expectation under \(\mathbb P_P^{\operatorname{cons}}\). Equivalently,

$$
\mathbb E_P^{\operatorname{cons}}[f]
=
\mathbb E_P[f\mid\operatorname{Cons}(P)].
$$

Thus \(\mathbb E_P^{\operatorname{cons}}\) includes both the initial-skeleton conditioning built into \(\mathbb E_P\) and the patch consistency conditioning.