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

For \(P\in\mathcal P_T\), let \(\Sigma_P\), \(\Omega_P\), \(\mathbb P_P\), \(\mathbb E_P\), \(\operatorname{Con}(P)\), \(\mathbb P_P^{\mathrm{con}}\), and \(\mathbb E_P^{\mathrm{con}}\) be as in the [patch consistency event](patch-consistency-event.md) entry.

## Statement

Conditional on \(\cG_T\), the patch interaction data \((\Sigma_P)_{P\in\mathcal P_T}\) are independent, and the conditional law of \(\Sigma_P\) is \(\mathbb P_P^{\mathrm{con}}\) for every \(P\in\mathcal P_T\).

Equivalently, for every finite \(\cG_T\)-measurable subfamily \(\mathcal Q\subseteq\mathcal P_T\) and bounded measurable functions \(f_P:\Omega_P\to\mathbb R\),

$$
\mathbb E\left[
\prod_{P\in\mathcal Q}f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal Q}
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\tag{1}
$$

When \(T<\infty\), local finiteness makes \(\mathcal P_T\) finite almost surely, so one may take \(\mathcal Q=\mathcal P_T\). When \(T=\infty\), (1) is understood as the corresponding finite-dimensional statement.

## Proof

Condition on \(\cG_T\). This fixes the successful-interaction skeleton and hence the complete labeled patch family \(\mathcal P_T\). For each patch \(P\), the unrevealed variables are

$$
\Sigma_P^\circ
\qquad\text{if }\mathsf X(P)=\mathsf I,
$$

and

$$
(\alpha_P,\Sigma_P^\circ)
\qquad\text{if }\mathsf X(P)=\mathsf O,
$$

with the notation of the [patch consistency event](patch-consistency-event.md) entry. Every \(f_P(\Sigma_P)\) is a function only of these variables. The interior source-time regions of distinct patches are disjoint, and the variables \(\alpha_P\) associated with distinct outgoing initial interactions are independent of one another and of all interior Poisson data. Moreover, the fixed successful-interaction skeleton imposes on the variables of patch \(P\) only the local event \(\operatorname{Con}(P)\). Thus the patch variables remain independent conditionally on \(\cG_T\), and

$$
\mathbb E\left[
\prod_{P\in\mathcal Q}f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal Q}
\mathbb E\left[
f_P(\Sigma_P)
\middle|\cG_T
\right].
\tag{2}
$$

For a fixed patch \(P\), its reference law is \(\mathbb P_P\), and \(\operatorname{Con}(P)\) is precisely the event that its local interaction data are consistent with the revealed successful-interaction skeleton. Therefore

$$
\mathbb E\left[
f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\mathbb E_P\left[
f_P(\Sigma_P)
\middle|\operatorname{Con}(P)
\right]
=
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\tag{3}
$$

Substituting (3) into (2) proves (1).
