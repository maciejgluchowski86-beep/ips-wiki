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

This entry states the patch representation obtained by combining [monomial duality for spin systems](monomial-duality-for-spin-systems.md), [patch factorization](patch-factorization.md), and the [patch contribution](patch-contribution.md) formulas.

Let \((P_t)_{t\ge0}\) be the semigroup of a [spin system](spin-system.md). For \(A\Subset\Lambda\), write

$$
\chi_A(\xi)=\prod_{i\in A}\xi(i).
$$

Let \((A_s,\sigma_s)\) be the signed additive dual process started from \((A,+)\), using the rates and signs associated with the monomial duality construction. Let \(\mathcal B_t\) and \(\mathcal E_t\) be the bulk and end [patch](patch.md) sets before horizon \(t\). The patch contribution functions are those in the [patch contribution](patch-contribution.md) entry.

Write \(\mathbb E_A\) for expectation over the successful-interaction skeleton, equivalently over the graphical construction after the patch-internal randomness has been integrated through the local contribution functions.

## Statement

For every finite \(A\Subset\Lambda\), every configuration \(\xi\in\{0,1\}^\Lambda\), and every \(t\ge0\),

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t} C(P)
\prod_{P\in\mathcal E_t} C(\xi,P)
\right].
$$

The first product runs over bulk patches, whose terminal boundary is a successful incoming or outgoing touch. The second product runs over end patches, which reach time \(t\) and therefore carry the terminal dependence on \(\xi\).

## Proof

The monomial duality formula gives

$$
P_t(\chi_A)(\xi)
=
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(\int_0^t V(A_s)\,ds\right)
\chi_{A_t}(\xi)
\right].
$$

The sign \(\sigma_t\), the Feynman--Kac factor, and the terminal monomial split over patches. A bulk patch contributes only its local sign and Feynman--Kac weight. An end patch contributes the same local sign and Feynman--Kac weight, together with the terminal factor \(\xi(i)\) if the site \(i\) is active at time \(t\).

Condition on the successful-interaction sigma algebra \(\cG_t\). This fixes the successful-interaction skeleton and hence the patch family, boundary times, boundary types, and initial skeletons. By patch factorization, the remaining patch data are independent after conditioning, with the local conditioned laws \(\mathbb P_P^{\operatorname{cons}}\). Therefore the conditional expectation of the duality weight is

$$
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(\int_0^t V(A_s)\,ds\right)
\chi_{A_t}(\xi)
\middle|\cG_t
\right]
=
\prod_{P\in\mathcal B_t} C(P)
\prod_{P\in\mathcal E_t} C(\xi,P).
$$

Taking expectation over \(\cG_t\) gives the displayed representation.

As usual for graphical constructions, simultaneous successful touches and successful touches exactly at the terminal time are null events; the fixed deterministic ordering convention handles them without changing the formula.
