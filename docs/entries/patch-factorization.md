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

Condition on a value of \(\cG_T\). This fixes the successful interactions, hence also the patch set \(\mathcal P_T\), the boundary times, and the boundary types.

The patches cover all active spacetime between successful interactions. Indeed, every initially active site begins a patch at time \(0\), every incoming successful interaction begins a patch at its target, and every source-keeping outgoing successful interaction begins the next patch at its source. A source-killing outgoing successful interaction only terminates the source patch. Therefore any interaction outside patch interiors either occurs at a revealed successful boundary or has inactive source and does not change the process.

For distinct patches \(P\), the sets \(\Pi_P\) use disjoint source-time restrictions of the independent Poisson interaction processes. Hence the unrestricted variables \(\{\Pi_P:P\in\mathcal P_T\}\) are independent, with laws \(\mathbb P_P\).

After the successful boundary interactions are fixed, the condition that there are no additional successful interactions inside the patch interiors is exactly

$$
\bigcap_{P\in\mathcal P_T}\operatorname{Cons}(P).
$$

This event is a product event: \(\operatorname{Cons}(P)\) depends only on \(\Pi_P\). Thus, by independence,

$$
\begin{aligned}
&\mathbb E\left[
\prod_{P\in\mathcal P_T} f_P(\Pi_P)
\middle|\cG_T
\right]
\\
&\qquad=
\frac{
\prod_{P\in\mathcal P_T}
\mathbb E_P\left[f_P(\Pi_P)\mathbf 1_{\operatorname{Cons}(P)}\right]
}{
\prod_{P\in\mathcal P_T}
\mathbb P_P(\operatorname{Cons}(P))
}
\\
&\qquad=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\operatorname{cons}}[f_P(\Pi_P)].
\end{aligned}
$$

This proves the factorization.