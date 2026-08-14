---
title: Patch representation of spin systems
status: conditional
audit: current
tags:
  - spin systems
  - duality
  - patch
  - representation theorem
---

# Patch representation of spin systems

This page records the project patch representation as a **conditional statement**. It is not currently a verified theorem.

## Prerequisites

For the time horizon and initial finite set under consideration, assume all of the following:

1. the conditional Feynman--Kac formula in [monomial duality for spin systems](monomial-duality-for-spin-systems.md), including its nonexplosion and integrability hypotheses;
2. the unverified conditional [patch factorization](patch-factorization.md); and
3. the contribution definitions and closed-form identities used from [patch contribution](patch-contribution.md).

Let $(P_t)_{t\ge0}$ be the spin-system semigroup and let the signed dual start from $(A,+)$. Let $\mathcal B_t$ and $\mathcal E_t$ be the bulk and end patch families, and let $C(P)$ and $C(\xi,P)$ denote the corresponding contributions.

## Conditional representation

Under the prerequisites above, the current project argument gives, for every $A\Subset\Lambda$, $\xi\in\{0,1\}^\Lambda$, and $t\ge0$,

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P)
\right].
\tag{1}
$$

Here $\mathbb E_A$ is expectation with respect to the successful-interaction skeleton of the dual started from $(A,+)$.

The project derivation starts from the Feynman--Kac integrand, decomposes its sign, potential integral, and terminal monomial into patch-local factors, and then applies the conditional factorization. Because the factorization and the patch contribution calculation remain unaudited, equation (1) remains conditional.

## Averaging over an initial law

Still under the same prerequisites, integrating (1) against a probability measure $\mu$ gives

$$
\mu(P_t\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)\,
\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)
\right].
\tag{2}
$$

If one additionally assumes the conditional [patch positivity property](patch-positivity-property.md), its critical profile $\mathbf p^\star$, and the affine end-contribution decomposition

$$
C(z,P)=C(p_{i(P)}^\star,P)+b(P)(z-p_{i(P)}^\star),
$$

then the end factor in (2) expands algebraically as

$$
\begin{aligned}
\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)
=
\sum_{\mathcal Q\subseteq\mathcal E_t}
&\mu\left(
\chi_{\{i(P):P\in\mathcal Q\}}^\star
\right)
\prod_{P\in\mathcal Q}b(P)
\\
&\times
\prod_{P\in\mathcal E_t\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\end{aligned}
\tag{3}
$$

Equation (3) is an algebraic expansion once the affine coefficients are supplied; any sign conclusions drawn from those coefficients inherit the unresolved status of the contribution and positivity calculations.
