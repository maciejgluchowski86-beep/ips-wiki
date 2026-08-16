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
S\ne\varnothing
\qquad\text{and}\qquad
i\in A_{t-}.
\tag{1}
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
(i,t,S):t\le T
\text{ and }(i,t,\alpha,S)\text{ is successful for some }\alpha\in\{\delta,\beta\}
\right\}.
\tag{2}
$$

Set

$$
\mathcal I=\bigcup_{T<\infty}\mathcal I_T,
\qquad
\mathcal G_T=\sigma(Y_0,\mathcal I_T).
\tag{3}
$$

The skeleton omits all empty-target death clocks, all rings at inactive sources, and the split/birth kind of each ordinary successful interaction. These omitted marks are precisely the local randomness averaged inside [patches](patch.md).

## Local finiteness

The canonical paper uses the following graphical fact repeatedly.

Let

$$
\overline c
=
\sup_{i\in\Lambda,\eta}c_i(\eta),
\qquad
m_0
=
\sup_{i\in\Lambda}|N(i)|.
$$

Möbius inversion of the local flip rates gives a uniform bound on every multilinear coefficient, and therefore

$$
\overline\alpha
=
\sup_{i\in\Lambda}
\left(
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\varnothing}}\beta_i(S)
\right)
<\infty.
\tag{4}
$$

If the current active set is $B$, the total rate of relevant dual clocks is at most

$$
\overline\alpha|B|.
$$

One interaction activates at most $m_0$ new sites. Hence both the active-set size and the number of relevant rings are dominated by a continuous-time branching process in which each particle rings at rate $\overline\alpha$ and creates at most $m_0$ new particles. That branching process is nonexplosive.

It follows that, from every finite initial active set, almost surely only finitely many relevant interactions occur on every bounded time interval. Independent Poisson clocks have no simultaneous points almost surely, and a countable union over pairs of clocks preserves this property. Consequently:

- $\mathcal I_T$ is finite for every $T<\infty$;
- the finite-horizon patch family $\mathcal P_T$ is finite;
- positive interaction times are distinct; and
- every maximal backward predecessor chain of patches with outgoing terminal boundary reaches time $0$ after finitely many steps.

The last point is the finiteness input used in the backward-chain proof in [late interactions and no-late relaxation](exponential-relaxation-under-confined-late-interactions.md).

If $L_T$ denotes the event that no successful interaction occurs after time $T$, then local finiteness also gives

$$
\{|\mathcal P|<\infty\}
=
\bigcup_{n\in\mathbb N}L_n.
\tag{5}
$$

Indeed, a finite all-time patch family contains only finitely many successful interactions and therefore has a last one. Conversely, on $L_T$ there are finitely many successful interactions before $T$ and none afterward.

The records in $\mathcal I$ determine the incoming and outgoing patch boundaries. Conditioning on $\mathcal G_T$ leaves exactly the patch-local randomness described by the [consistent patch law](patch-consistency-event.md) and factorized by the [patch factorization theorem](patch-factorization.md).
