---
title: Patch representation of spin systems
status: proved here
audit: current
tags:
  - spin systems
  - duality
  - patch
  - representation theorem
---

# Patch representation of spin systems

The patch representation is Theorem A of the canonical paper *Patch representations and convergence for facilitated spin systems*. It is an exact representation, not a conditional project statement.

Fix $A\Subset\Lambda$ and start the signed monomial dual from $(A,+)$. At time $t$, let $\mathcal B_t$ and $\mathcal E_t$ be the bulk and end [patch](patch.md) families. A bulk patch has contribution $C(P)$ and an end patch based at $i(P)$ has affine terminal contribution $C(z,P)$.

## Theorem

For every $A\Subset\Lambda$, $t\ge0$, and configuration $\eta$,

$$
P_t\chi_A(\eta)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right].
\tag{1}
$$

For any initial probability law $\mu$,

$$
(\mu P_t)(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\,\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)
\right].
\tag{2}
$$

For the Bernoulli product law $\mu_{\mathbf p}$, distinct end patches have distinct sites and the end contributions are affine, so

$$
(\mu_{\mathbf p}P_t)(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(p_{i(P)},P)
\right].
\tag{3}
$$

## Derivation

The [monomial Feynman-Kac duality](monomial-duality-for-spin-systems.md) has integrand

$$
\sigma_t
\exp\left(\int_0^tV(A_u)\,du\right)
\chi_{A_t}(\eta).
$$

The patch intervals partition the local active-time contributions. Pathwise,

$$
\sigma_t
\exp\left(\int_0^tV(A_u)\,du\right)
\chi_{A_t}(\eta)
=
\prod_{P\in\mathcal B_t}F(P)
\prod_{P\in\mathcal E_t}F(\eta(i(P)),P).
\tag{4}
$$

Conditioning (4) on the successful-interaction sigma algebra $\mathcal G_t$ and applying [patch factorization](patch-factorization.md) replaces each local factor by its consistent patch expectation, giving (1).

The point of the representation is the order of operations: marked interactions between consecutive successful-interaction boundaries are averaged inside $C(P)$ or $C(z,P)$ before global comparison or absolute values are taken. This preserves cancellations that are invisible in the raw signed dual trajectory.
