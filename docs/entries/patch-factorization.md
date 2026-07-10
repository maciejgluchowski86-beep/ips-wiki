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

The patch-interior sigma algebra is

$$
\mathcal F_T^{\operatorname{patch}}
=
\bigvee_{P\in\mathcal P_T}\mathcal F_P.
$$

## Statement

Conditional on \(\cG_T\), the law of the patch interiors factors over patches:

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

Condition on \(\cG_T\). This fixes the successful interactions, hence also the patch set \(\mathcal P_T\), the boundary times, and the boundary types.

The patches cover all active spacetime. Every initially active site begins a patch at time \(0\). Every successful interaction touches its source and all its target sites; at each touched site it is both the terminal boundary of the preceding patch and the initial boundary of the following patch, except at the endpoints \(0\) and \(T\). Thus an interaction outside patch interiors is either a revealed successful boundary interaction or has inactive source and does not change the process.

Let

$$
C_T=igcap_{P\in\mathcal P_T}\operatorname{Cons}(P).
$$

Since \(\cG_T\) records the actual successful interactions, the event \(C_T\) holds almost surely after conditioning on \(\cG_T\). Hence, by the tower property, for

$$
Z=\prod_{P\in\mathcal P_T} f_P(\Pi_P),
$$

we have

$$
\mathbb E[Z\mid\cG_T]
=
\mathbb E\left[\mathbb E[Z\mid\cG_T,C_T]\mid\cG_T\right].
$$

Given \(\cG_T\), the boundary interactions are fixed. For distinct patches \(P\), the sets \(\Pi_P\) use disjoint source-time restrictions of the independent Poisson interaction processes. Moreover, \(\operatorname{Cons}(P)\) depends only on \(\Pi_P\). Therefore the inner conditional expectation factors:

$$
\begin{aligned}
\mathbb E[Z\mid\cG_T,C_T]
&=
\frac{
\prod_{P\in\mathcal P_T}
\mathbb E_P\left[f_P(\Pi_P)\mathbf 1_{\operatorname{Cons}(P)}\right]
}{
\prod_{P\in\mathcal P_T}
\mathbb P_P(\operatorname{Cons}(P))
}
\\
&=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\operatorname{cons}}[f_P(\Pi_P)].
\end{aligned}
$$

The right-hand side is \(\cG_T\)-measurable, because \(\cG_T\) fixes the patches and their boundary types. Substituting into the tower-property identity gives the stated formula.