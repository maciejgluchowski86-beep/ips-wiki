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

The patch representation is Theorem A of the canonical paper *Patch representations and convergence for facilitated spin systems*. It is an exact representation of monomial expectations obtained by conditioning the signed Feynman-Kac dual on its successful-interaction skeleton.

Assume the spin-system setup and Feynman-Kac integrability hypothesis from [monomial Feynman-Kac duality](monomial-duality-for-spin-systems.md). Fix $A\Subset\Lambda$ and start the signed monomial dual from $(A,+)$. At time $t$, let $\mathcal B_t$ and $\mathcal E_t$ be the bulk and end [patch](patch.md) families. A bulk patch has contribution $C(P)$ and an end patch based at $i(P)$ has affine contribution $C(z,P)$.

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

For the Bernoulli product law $\mu_{\mathbf p}$,

$$
(\mu_{\mathbf p}P_t)(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(p_{i(P)},P)
\right].
\tag{3}
$$

## Proof of the pathwise factorization

On the graphical probability space, let $X^P$, $\alpha(P)$, and $\sigma(P)$ denote the actual patch-local variables induced by the signed dual. The [monomial Feynman-Kac duality](monomial-duality-for-spin-systems.md) has integrand

$$
Z_t^\eta
=
\sigma_t
\exp\left(\int_0^tV(A_u)\,du\right)
\chi_{A_t}(\eta).
\tag{4}
$$

We factor each of its three components over patches.

### Sign

Every nonempty-target successful interaction contributes its sign to exactly one patch: the patch beginning at the interaction source. Empty-target deaths have positive sign because

$$
a_i^\delta(\varnothing)=c_i^0(\varnothing)\ge0.
$$

Therefore

$$
\sigma_t
=
\prod_{P\in\mathcal B_t}\sigma(P)
\prod_{P\in\mathcal E_t}\sigma(P).
\tag{5}
$$

### Feynman-Kac potential

Since

$$
V(A_u)=\sum_{i\in A_u}V_i,
$$

the patch intervals partition the dual-active time spent by each site. Consequently,

$$
\int_0^tV(A_u)\,du
=
\sum_{P\in\mathcal B_t}
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
+
\sum_{P\in\mathcal E_t}
V_{i(P)}\int_{s(P)}^tX_u^P\,du.
\tag{6}
$$

### Terminal monomial

The end patches are exactly the site-line intervals reaching the horizon. They record the active set at time $t$. Distinct end patches have distinct base sites, and

$$
\chi_{A_t}(\eta)
=
\prod_{P\in\mathcal E_t}
\eta(i(P))^{X_t^P}.
\tag{7}
$$

Insert (5)-(7) into (4). With the raw patch factors from [patch contribution](patch-contribution.md), this gives the pathwise identity

$$
Z_t^\eta
=
\prod_{P\in\mathcal B_t}F(P)
\prod_{P\in\mathcal E_t}F(\eta(i(P)),P).
\tag{8}
$$

## Conditioning on the skeleton

The Feynman-Kac integrability hypothesis makes $Z_t^\eta$ integrable. Condition (8) on

$$
\mathcal G_t=\sigma(Y_0,\mathcal I_t).
$$

By the [patch factorization theorem](patch-factorization.md), conditional on $\mathcal G_t$ the patch data are independent and each patch has its consistent patch law. Hence

$$
\begin{aligned}
\mathbb E_A[Z_t^\eta\mid\mathcal G_t]
&=
\prod_{P\in\mathcal B_t}
\mathbb E_P^{\mathrm{con}}[F(P)]
\prod_{P\in\mathcal E_t}
\mathbb E_P^{\mathrm{con}}[F(\eta(i(P)),P)]\\
&=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P).
\end{aligned}
\tag{9}
$$

Taking expectation and applying the monomial Feynman-Kac formula to the left-hand side proves (1).

## General initial laws

Integrate (1) against an arbitrary probability law $\mu$ on the spin configuration. The dual graphical randomness is independent of the sampled initial spin configuration, so Fubini's theorem gives

$$
\begin{aligned}
(\mu P_t)(\chi_A)
&=
\int P_t\chi_A(\eta)\,\mu(d\eta)\\
&=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\,\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)
\right],
\end{aligned}
$$

which is (2).

## Bernoulli product initial laws

If $\mu=\mu_{\mathbf p}$ is a Bernoulli product law, the sites $i(P)$ for $P\in\mathcal E_t$ are distinct and each $C(z,P)$ is affine in $z$. Therefore independence of the product spins gives

$$
\mu_{\mathbf p}\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)
=
\prod_{P\in\mathcal E_t}C(p_{i(P)},P).
$$

Substituting this into (2) proves (3).

## What is averaged

The successful-interaction skeleton retains the source, time, and nonempty target of every interaction that acts on the signed dual. It deliberately forgets death marks, rings at inactive sources, and the split/birth kind of an outgoing successful interaction. Those omitted marks between consecutive patch boundaries are integrated inside $C(P)$ and $C(z,P)$ before any global comparison is made. The representation therefore retains cancellations between successive local updates that would be lost by taking absolute values directly on the raw dual trajectory.
