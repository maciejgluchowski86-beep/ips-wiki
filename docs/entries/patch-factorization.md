---
title: Patch factorization
status: conditional
audit: current
tags:
  - duality
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
  - factorization
---

# Patch factorization

Fix a [signed additive set process](signed-additive-set-process.md), its graphical construction, and a finite horizon $T<\infty$. Let $\cG_T$ be the [successful-interaction](successful-interaction.md) sigma algebra and let $\mathcal P_T$ be the corresponding finite-horizon [patch](patch.md) family. For $P\in\mathcal P_T$, use the reference data and conditioned law from [patch consistency event](patch-consistency-event.md).

The factorization below is an **unverified project hypothesis**. It is retained because later patch formulas state their dependence on it explicitly; it must not be used as an established theorem.

## Conditional factorization assertion

Assume that, conditional on $\cG_T$, the patch interaction data $(\Sigma_P)_{P\in\mathcal P_T}$ are independent and that the conditional law of each $\Sigma_P$ is $\mathbb P_P^{\mathrm{con}}$. Equivalently, assume that for every family of bounded measurable functions $f_P:\Omega_P\to\mathbb R$,

$$
\mathbb E\left[
\prod_{P\in\mathcal P_T}f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\tag{1}
$$

The products are finite whenever the finite-horizon graphical construction produces only finitely many relevant patches from the finite initial active set.

## What remains unaudited

The project proof of (1) uses disintegration of the underlying Poisson data after the successful-interaction skeleton is fixed and identifies the event producing a prescribed skeleton with the intersection of the patch consistency events. That argument has not completed the current independent verification protocol. In particular, this page does not certify the regular-conditional-law construction, the skeleton/consistency equivalence, or the resulting product kernel.

The [patch contribution](patch-contribution.md) and [patch representation of spin systems](patch-representation-of-spin-systems.md) therefore treat (1) as an explicit prerequisite rather than as a proved input.
