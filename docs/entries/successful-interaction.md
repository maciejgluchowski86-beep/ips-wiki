---
title: Successful interaction
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
---

# Successful interaction

Fix a [signed additive set process](signed-additive-set-process.md) with full interaction set \(I\), constructed as in the [graphical construction](graphical-construction-of-signed-additive-set-process.md). Its deterministic initial interaction

$$
(\infty,0,\mathsf{init},A_0)
$$

is declared successful, with successful-interaction skeleton

$$
(\infty,0,A_0).
$$

For \(i\in\Lambda\) and \(S\ne\vn\), an ordinary type-\(S\) successful interaction is a source-time-target skeleton \((i,t,S)\) such that

$$
(i,t,\alpha,S)\in I
\quad\text{for some }\alpha\in\{\delta,\beta\},
\qquad
i\in A_{t-}.
$$

An ordinary successful-interaction skeleton records the interaction source and target, but not whether the interaction is a split or a birth. The initial skeleton has the special kind \(\mathsf{init}\), so there is no hidden split-or-birth choice at time zero.

For a time horizon \(T<\infty\) and nonempty \(S\), let

$$
\mathcal I_T^S
=
\left\{
(i,t,S):
i\in\Lambda,
\ 0<t\le T,
\ i\in A_{t-},
\ (i,t,\alpha,S)\in I
\text{ for some }\alpha\in\{\delta,\beta\}
\right\}.
$$

The set of all successful-interaction skeletons through time \(T\) is

$$
\mathcal I_T
=
\{(\infty,0,A_0)\}
\cup
\bigcup_{\substack{S\Subset\Lambda\\S\ne\vn}}
\mathcal I_T^S.
$$

The full successful-interaction set is

$$
\mathcal I
=
\bigcup_{T<\infty}\mathcal I_T,
$$

and \(\mathcal I_\infty=\mathcal I\).

Thus \(I\) contains the marked deterministic initial interaction and every marked Poisson interaction, while \(\mathcal I_T\) contains the initial skeleton and every ordinary successful-interaction skeleton through time \(T\). Deaths have empty target and are not successful interactions.

For \(T\le\infty\), the successful-interaction sigma algebra is

$$
\cG_T
=
\sigma\left(Y_0,\mathcal I_T\right).
$$

It reveals the initial interaction and every ordinary successful interaction through time \(T\), but it does not reveal whether an ordinary outgoing successful interaction is a split or a birth. The resulting boundary data define [patches](patch.md), and the lattice sites they touch form the [interaction cone](interaction-cone.md).
