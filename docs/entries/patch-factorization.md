---
title: Patch factorization
status: proved here
tags:
  - duality
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
  - factorization
---

# Patch factorization

Fix a [signed additive set process](signed-additive-set-process.md), its graphical construction, and \(T\le\infty\). Let \(\cG_T\) be the [successful-interaction](successful-interaction.md) sigma algebra, with \(\mathcal I_\infty=\mathcal I\), and let \(\mathcal P_T\) be the [patch](patch.md) family, with \(\mathcal P_\infty=\mathcal P\). This factorization is the probabilistic input for the [patch contribution](patch-contribution.md) formulas and the [patch representation of spin systems](patch-representation-of-spin-systems.md).

For \(P\in\mathcal P_T\), let \(\Sigma_P\), \(\Omega_P\), \(\mathbb P_P\), \(\mathbb E_P\), \(\operatorname{Cons}(P)\), \(\mathbb P_P^{\operatorname{cons}}\), and \(\mathbb E_P^{\operatorname{cons}}\) be as in the [patch consistency event](patch-consistency-event.md) entry.

## Statement

Conditional on \(\cG_T\), the patch interaction data factor over patches. More precisely, for every finite \(\cG_T\)-measurable subfamily \(\mathcal Q\subseteq\mathcal P_T\) and bounded measurable functions \(f_P:\Omega_P\to\mathbb R\),

$$
\mathbb E\left[
\prod_{P\in\mathcal Q} f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal Q}
\mathbb E_P^{\operatorname{cons}}[f_P(\Sigma_P)].
\tag{1}
$$

When \(T<\infty\), local finiteness makes \(\mathcal P_T\) finite almost surely, so one may take \(\mathcal Q=\mathcal P_T\). When \(T=\infty\), the family \(\mathcal P\) can be infinite; (1) is the finite-dimensional statement that characterizes its conditional product law.

## Proof

Condition on \(\cG_T\). This fixes the successful-interaction skeleton, hence the patch family, boundary times, boundary types, and initial skeleton of each patch. It does not reveal whether an outgoing successful interaction is a split or a birth.

For an outgoing initial skeleton \((i,s,S)\), the update kind is sampled by

$$
\mathbb P\left(
(i,s,\beta,S)\in I
\middle|
(i,s,\delta,S)\in I\text{ or }(i,s,\beta,S)\in I
\right)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)},
$$

and the split probability is \(\delta_i(S)/(\delta_i(S)+\beta_i(S))\). These choices are independent for distinct outgoing skeletons. They are also independent of the source-time Poisson processes strictly inside the patches.

The remaining data of \(P=\{i\}\times[s,t)\) use only source-\(i\) interactions at times \(s<u<t\). These source-time regions are pairwise disjoint: patches at different sites use independent Poisson processes, while patches at the same site have disjoint time intervals. Thus the reference patch data have product law \(\bigotimes_P\mathbb P_P\).

The condition that the fixed skeleton is the successful-interaction skeleton is local to these coordinates. For each patch it is exactly \(\operatorname{Cons}(P)\): no additional nonempty-target interaction may have active source in the patch interior, and an outgoing terminal interaction must have active source. Since \(\operatorname{Cons}(P)\) depends only on \(\Sigma_P\), conditioning the product reference law on these coordinatewise events gives

$$
\mathbb E\left[
\prod_{P\in\mathcal Q} f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal Q}
\mathbb E_P\left[
f_P(\Sigma_P)
\middle|
\operatorname{Cons}(P)
\right],
$$

which is (1).

For \(T=\infty\), apply the same calculation first to cylinder events involving finitely many patches and bounded time intervals. Conditional martingale convergence and the monotone-class theorem extend it to every bounded \(f_P\) in a finite family \(\mathcal Q\). No infinite product of test functions is required.
