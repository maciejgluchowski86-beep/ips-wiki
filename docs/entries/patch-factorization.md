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

Condition on \(\cG_T\). This fixes the successful-interaction set \(\mathcal I_T\), hence also the patch set \(\mathcal P_T\), the boundary times, the boundary types, and the initial interaction contained in each \(\Pi_P\).

The patches cover all active spacetime. Every initially active site begins a patch at time \(0\). Every successful interaction touches its source and all its target sites; at each touched site it is both the terminal boundary of the preceding patch and the initial boundary of the following patch, except at the endpoints \(0\) and \(T\). Thus an interaction outside patches is either a revealed successful boundary interaction or has inactive source and does not change the process.

For a finite family \(A\) of interactions, write

$$
R_A=\{A\subseteq I\}.
$$

Thus \(R_A\) is the event that all interactions in \(A\) occur in the graphical construction; it does not assert that these are the only interactions.

Let

$$
Z=\prod_{P\in\mathcal P_T} f_P(\Pi_P).
$$

Since \(R_{\mathcal I_T}\) reveals that every listed successful interaction occurs, while \(\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\) guarantees that no additional successful interaction occurs inside any patch and that outgoing terminal boundaries have active source, the pair of conditions

$$
R_{\mathcal I_T},
\qquad
\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)
$$

reveals the same successful-interaction information as \(\cG_T\), after \(Y_0\) is fixed. Hence the tower property gives

$$
\mathbb E[Z\mid\cG_T]
=
\mathbb E\left[
\mathbb E\left[Z\middle|R_{\mathcal I_T},\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\right]
\middle|\cG_T
\right].
$$

It remains to compute the inner conditional expectation. Condition on \(R_{\mathcal I_T}\). This fixes the initial boundary interaction in each \(\Pi_P\). The remaining random interactions in \(\Pi_P\) have source \(i\) and times \(s<u<t\) for \(P=\{i\}\times[s,t)\). These source-time regions are pairwise disjoint: distinct sites use independent Poisson processes, while two patches at the same site have disjoint time intervals. Therefore the remaining patch interaction data are independent under the conditional law given \(R_{\mathcal I_T}\).

For each patch, \(\operatorname{Cons}(P)\) depends only on \(\Pi_P\), and after conditioning on \(R_{\mathcal I_T}\) it has positive probability. Therefore the elementary product-conditioning identity applies: if \((X_k,B_k)\) are independent and \(\mathbb P(B_k)>0\), then

$$
\mathbb E\left[\prod_k X_k\middle|\bigcap_k B_k\right]
=
\prod_k \mathbb E[X_k\mid B_k].
$$

Applying this identity to the independent patch data under \(R_{\mathcal I_T}\), with \(X_P=f_P(\Pi_P)\) and \(B_P=\operatorname{Cons}(P)\), gives

$$
\mathbb E\left[Z\middle|R_{\mathcal I_T},\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P)\right]
=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\operatorname{cons}}[f_P(\Pi_P)].
$$

The right-hand side is \(\cG_T\)-measurable, because \(\cG_T\) fixes the patches and their boundary types. Substituting this identity into the tower-property formula gives the claim.