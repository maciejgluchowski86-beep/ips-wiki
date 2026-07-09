---
title: Successful interaction
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
---

# Successful interaction

Fix a [signed additive set process](signed-additive-set-process.md) with graphical mark set \(P\), constructed as in the [graphical construction](graphical-construction-of-signed-additive-set-process.md). For \(S\ne\vn\), a type-\(S\) successful interaction is a mark

$$
(i,t,\alpha,S)\in P,
\qquad
\alpha\in\{\delta,\beta\},
$$

whose source is active when the mark occurs:

$$
i\in A_{t-}.
$$

For a time horizon \(T<\infty\), let

$$
\mathcal I_T^S
=
\{(i,t,\alpha,S)\in P:t\le T,\ i\in A_{t-}\}.
$$

Thus \(\mathcal I_T^S\) is the set of type-\(S\) successful interactions before time \(T\).

The successful-interaction sigma algebra is

$$
\cG_T
=
\sigma\left(Y_0,\{\mathcal I_T^S:S\ne\vn\}\right).
$$

It reveals all successful interactions with nonempty target set up to time \(T\). If the initial state is deterministic, this reduces to

$$
\cG_T
=
\sigma\left(\{\mathcal I_T^S:S\ne\vn\}\right).
$$
