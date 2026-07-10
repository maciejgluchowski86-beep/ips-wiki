---
title: Patch factorization
status: proved here
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
  - factorization
---

# Patch factorization

Fix a [signed additive set process](signed-additive-set-process.md), its graphical construction, and a horizon \(T<\infty\). Let \(\cG_T\) be the [successful-interaction](successful-interaction.md) sigma algebra, and let \(\mathcal P_T\) be the set of [patches](patch.md).

For \(P\in\mathcal P_T\), let \(\Pi_P\), \(\Omega_P\), \(\mathbb P_P\), \(\mathbb E_P\), \(\operatorname{Cons}(P)\), \(\mathbb P_P^{\operatorname{cons}}\), and \(\mathbb E_P^{\operatorname{cons}}\) be as in the [patch consistency event](patch-consistency-event.md) entry. Set

$$
\mathcal F_P=\sigma(\Pi_P).
$$

The patch sigma algebra is

$$
\mathcal F_T^{\operatorname{patch}}
=
\bigvee_{P\in\mathcal P_T}\mathcal F_P.
$$

## Statement

Conditional on \(\cG_T\), the law of the patch interaction data factors over patches:

$$
\mathbb P\left(\cdot\mid\cG_T\right)\big|_{\mathcal F_T^{\operatorname{patch}}}
=
\bigotimes_{P\in\mathcal P_T}\mathbb P_P^{\operatorname{cons}}.
$$

Equivalently, for bounded measurable functions \(f_P:\Omega_P\to\mathbb R\),

$$
\mathbb E\left[
\prod_{P\in\mathcal P_T} f_P(\Pi_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\operatorname{cons}}[f_P(\Pi_P)].
$$

The product is finite under the local-finiteness assumption in the graphical construction.

## Proof

Condition on \(\cG_T\). This fixes the successful interactions, hence also the patch set \(\mathcal P_T\), the boundary times, the boundary types, and the initial interaction contained in each \(\Pi_P\).

The patches cover all active spacetime. Every initially active site begins a patch at time \(0\). Every successful interaction touches its source and all its target sites; at each touched site it is both the terminal boundary of the preceding patch and the initial boundary of the following patch, except at the endpoints \(0\) and \(T\). Thus an interaction outside patches is either a revealed successful boundary interaction or has inactive source and does not change the process.

For

$$
Z=\prod_{P\in\mathcal P_T} f_P(\Pi_P),
$$

use the tower property in the form

$$
\mathbb E[Z\mid\cG_T]
=
\mathbb E\left[
\mathbb E\left[Z\middle|\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\right]
\middle|\cG_T
\right].
$$

Here the patch family and the boundary types are those fixed by \(\cG_T\). Once these are fixed, the event \(\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\) contains the same successful-interaction information as \(\cG_T\): the initial boundary condition \(C_-(P)\) gives the interaction that begins each patch, the interior condition excludes further successful interactions inside patches, and \(C_+(P)\) gives the required activity before outgoing terminal boundaries.

It remains to compute the inner conditional expectation. The initial boundary interaction in each \(\Pi_P\) is fixed by the corresponding condition \(C_-(P)\). The remaining random interactions in \(\Pi_P\) have source \(i\) and times \(s<u<t\) for \(P=\{i\}\times[s,t)\). These source-time regions are pairwise disjoint: distinct sites use independent Poisson processes, while two patches at the same site have disjoint time intervals. Hence the remaining patch interaction data are independent before conditioning.

Moreover, \(\operatorname{Cons}(P)\) depends only on \(\Pi_P\). Therefore conditioning on the intersection of all consistency events conditions independent factors by their own patchwise events. Thus, in the regular conditional sense,

$$
\mathbb E\left[Z\middle|\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\right]
=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\operatorname{cons}}[f_P(\Pi_P)].
$$

Substituting this identity into the tower-property formula gives the claim.