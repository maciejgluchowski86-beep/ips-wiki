---
title: Successful interaction
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
---

# Successful interaction

Fix a [signed additive set process](signed-additive-set-process.md) with interaction set \(I\), constructed as in the [graphical construction](graphical-construction-of-signed-additive-set-process.md). For \(S\ne\vn\), a type-\(S\) successful interaction is a source-time-target skeleton

$$
(i,t,S)
$$

such that

$$
(i,t,\alpha,S)\in I
\quad\text{for some }\alpha\in\{\delta,\beta\},
$$

and whose source is active when the interaction occurs:

$$
i\in A_{t-}.
$$

The successful-interaction skeleton records the source, time, and target set, but not whether the interaction is a split or a birth.

For a time horizon \(T<\infty\), let

$$
\mathcal I_T^S
=
\{(i,t,S):t\le T,\ i\in A_{t-},\ (i,t,\alpha,S)\in I\text{ for some }\alpha\in\{\delta,\beta\}\}.
$$

The set of all successful interactions before time \(T\) is

$$
\mathcal I_T
=
\bigcup_{\substack{i\in\Lambda,\ S\subseteq N(i)\\ S\ne\vn}}
\{(i,t,S):(i,t,S)\in\mathcal I_T^S\}.
$$

Thus \(I\) is the full interaction set, \(\mathcal I_T^S\) is the set of type-\(S\) successful-interaction skeletons before time \(T\), and \(\mathcal I_T\) is the set of all successful-interaction skeletons before time \(T\). Deaths have target set \(\vn\), so they are not successful interactions.

The successful-interaction sigma algebra is

$$
\cG_T
=
\sigma\left(Y_0,\mathcal I_T\right).
$$

It reveals all successful interactions with nonempty target set up to time \(T\), but it does not reveal whether an outgoing successful interaction is a split or a birth.