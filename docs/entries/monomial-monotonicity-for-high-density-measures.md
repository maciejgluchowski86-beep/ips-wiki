---
title: Monomial monotonicity for high-density measures
status: proved here
tags:
  - patch positivity
  - high-density measure
  - monomials
  - monotonicity
---

# Monomial monotonicity for high-density measures

For a spin system with the [patch positivity property](patch-positivity-property.md), evolved [monomials](monomials.md) are monotone under coordinatewise ordering of the mixing profiles of [high-density measures](high-density-measure.md).

**References.** None yet.

## Theorem

For \(k\in\{0,1\}\), let

$$
\nu_k
=
\int\mu_{\mathbf p}\,\Pi_k(d\mathbf p),
$$

where \(\Pi_k\) is supported on one-density profiles satisfying \(\mathbf p\ge\mathbf p^\star\). Suppose that \(\Pi_0\) and \(\Pi_1\) admit a coupling \((\mathbf p_0,\mathbf p_1)\) such that

$$
\mathbf p_0\le\mathbf p_1
\qquad\text{almost surely}.
$$

Then, for every \(A\Subset\Lambda\) and \(t\ge0\),

$$
\nu_0\bigl(P_t(\chi_A)\bigr)
\le
\nu_1\bigl(P_t(\chi_A)\bigr).
$$

In particular, every \(\nu\in\mathcal M_\star\) satisfies

$$
\mu_{\mathbf p^\star}\bigl(P_t(\chi_A)\bigr)
\le
\nu\bigl(P_t(\chi_A)\bigr)
\le
\mu_{\mathbf 1}\bigl(P_t(\chi_A)\bigr).
$$

## Proof

First fix deterministic profiles

$$
\mathbf p^\star\le\mathbf p\le\mathbf q.
$$

Integrating the [patch representation](patch-representation-of-spin-systems.md) against the Bernoulli product measure \(\mu_{\mathbf p}\) gives

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P)
\right].
$$

Indeed, distinct end patches are based at distinct sites, so independence replaces each terminal spin by its one-site density. Patch positivity gives \(C(P)\ge0\) for every bulk patch. The definition of the [patch critical density](patch-critical-density.md) and monotonicity of the affine end contributions give

$$
0
\le
C^{\mathbf p}(P)
\le
C^{\mathbf q}(P)
$$

for every end patch. The patch products are therefore ordered for every successful-interaction skeleton, and taking \(\mathbb E_A\) yields

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
\le
\mu_{\mathbf q}\bigl(P_t(\chi_A)\bigr).
$$

Apply this inequality to the coupled profiles \(\mathbf p_0\le\mathbf p_1\) and average over their coupling.
