---
title: Successful interaction
status: definition
audit: current
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
---

# Successful interaction

Fix a [signed additive set process](signed-additive-set-process.md) with marked Poisson interaction set $I^{\mathrm P}$ from its [graphical construction](graphical-construction-of-signed-additive-set-process.md). The deterministic initial interaction is declared successful and has record

$$
(\infty,0,A_0).
$$

An ordinary interaction $(i,t,\alpha,S)\in I^{\mathrm P}$ is **successful** when

$$
S\ne\vn
\qquad\text{and}\qquad
i\in A_{t-}.
$$

Its successful-interaction **record** is the triple

$$
(i,t,S).
$$

Thus a record retains the source, time, and nonempty target of an interaction that acts on the dual process, but it does not retain whether the interaction is a split or a birth.

For $T<\infty$, the **successful-interaction skeleton** is

$$
\mathcal I_T
=
\{(\infty,0,A_0)\}
\cup
\left\{
(i,t,S):0<t\le T
\text{ and }(i,t,\alpha,S)\text{ is successful for some }\alpha\in\{\delta,\beta\}
\right\}.
$$

Set

$$
\mathcal I=\bigcup_{T<\infty}\mathcal I_T,
\qquad
\mathcal G_T=\sigma(Y_0,\mathcal I_T).
$$

The skeleton omits all death clocks, all rings at inactive sources, and the split/birth kind of each ordinary successful interaction. In the finite-range bounded-rate setting, $\mathcal I_T$ is finite almost surely for every finite $T$.

The records in $\mathcal I$ determine the incoming and outgoing boundaries of [patches](patch.md). Conditioning on $\mathcal G_T$ leaves exactly the patch-interior randomness averaged by the [patch factorization theorem](patch-factorization.md).
