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
Q=\{i\}\times[s,t)
$$

before horizon \(T\). Let \(P\) be the graphical mark set of the underlying [signed additive set process](signed-additive-set-process.md). The internal mark set of \(Q\) is

$$
\Pi_Q
=
\{(i,u,\alpha,R)\in P:s<u<t\}.
$$

The local patch measure \(\mathbb P_Q\) is the law of \(\Pi_Q\), with the source-\(i\) Poisson mark processes restricted to \((s,t)\). Under \(\mathbb P_Q\), define the local active indicator \(X^Q_u\), \(s\le u<t\), by \(X^Q_s=1\). Source-killing marks set \(X^Q\) to \(0\) when \(X^Q\) is active; source-keeping marks leave it active. Marks arriving while \(X^Q\) is inactive are ignored.

The consistency event of \(Q\) is

$$
\operatorname{Cons}(Q)
=
\left\{
X^Q_{u-}=0
\text{ for every }(i,u,\alpha,R)\in\Pi_Q\text{ with }R\ne\vn
\right\}
\cap C_+(Q),
$$

where

$$
C_+(Q)
=
\begin{cases}
\{X^Q_{t-}=1\}, & \operatorname{type}_+(Q)=\mathsf O,\\
\Omega_Q, & \operatorname{type}_+(Q)\ne\mathsf O.
\end{cases}
$$

Here \(\Omega_Q\) is the sample space of the local mark process. The first condition says that no nonempty-target source mark from \(i\) is attempted while \(i\) is active in the interior of the patch. The second condition says that an outgoing terminal boundary can occur only if the source is active immediately before that boundary.

When \(\mathbb P_Q(\operatorname{Cons}(Q))>0\), define the conditioned patch measure by

$$
\mathbb P_Q^{\operatorname{cons}}(\cdot)
=
\mathbb P_Q(\cdot\mid\operatorname{Cons}(Q)).
$$
