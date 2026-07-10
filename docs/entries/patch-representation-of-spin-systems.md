---
title: Patch representation of spin systems
status: proved here
tags:
  - spin systems
  - duality
  - patch
  - representation theorem
---

# Patch representation of spin systems

This is the patchwise form of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), after applying [patch factorization](patch-factorization.md).

Let \((P_t)_{t\ge0}\) be the spin-system semigroup. Let the signed additive dual start from \((A,+)\). Let \(\mathcal B_t\) and \(\mathcal E_t\) be the bulk and end patch sets, and let \(C(P)\) and \(C(\xi,P)\) be the [patch contribution](patch-contribution.md) functions.

Write \(\mathbb E_A\) for expectation over the successful-interaction skeleton after the patch-internal randomness has been integrated out.

## Statement

For every \(A\Subset\Lambda\), every \(\xi\in\{0,1\}^\Lambda\), and every \(t\ge0\),

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P)
\right].
$$

## Proof

Start from the Feynman--Kac monomial duality formula. The sign, potential integral, and terminal monomial split into one factor per patch. Conditional on the successful-interaction sigma algebra, patch factorization makes the remaining patch data independent. The conditional expectation of each local factor is exactly \(C(P)\) for a bulk patch and \(C(\xi,P)\) for an end patch. Multiplying these conditional expectations and then averaging over the successful-interaction skeleton gives the displayed identity.

The deterministic ordering convention for simultaneous successful touches handles the null exceptional events without changing the formula.
