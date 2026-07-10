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

The Feynman--Kac monomial duality formula gives

$$
P_t(\chi_A)(\xi)
=
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(\int_0^t V(A_s)\,ds\right)
\chi_{A_t}(\xi)
\right].
$$

We split the random weight inside this expectation into one factor per patch. Fix the successful-interaction sigma algebra \(\cG_t\), so that the patch family, boundary types, and initial skeletons are fixed. For a patch \(P=\{i\}\times[s_-,s_+)\), let \(X^P\) be the local active indicator from the [patch consistency event](patch-consistency-event.md). Write \(\sigma_i^\alpha(S)=\sigma_i^\delta(S)\) when \(\alpha=\delta\), and \(\sigma_i^\alpha(S)=\sigma_i^\beta(S)\) when \(\alpha=\beta\). Define the sign assigned to \(P\) by

$$
\begin{aligned}
\Sigma_P^-&=
\begin{cases}
\sigma_i^\alpha(S),
& \operatorname{type}_-(P)=\mathsf O
\text{ and }(i,s_-,\alpha,S)\in\Pi_P^-,\\
1, & \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},
\end{cases}
\\
\Sigma_P^\circ
&=
\prod_{\substack{(i,u,\alpha,S)\in\Pi_P^\circ\\ X^P_{u-}=1}}
\sigma_i^\alpha(S),
\\
\Sigma_P&=\Sigma_P^-\Sigma_P^\circ.
\end{aligned}
$$

The assignment is source-side. A successful split or birth contributes its sign to the \(\mathsf O\)-initial patch at its source, while incoming target patches carry no sign from that interaction. Interior interactions contribute a sign exactly when their source is active. On the consistency event, there are no active-source split or birth interactions in the interior of a patch, so the only possible interior sign contributions are active deaths.

The local Feynman--Kac factor of \(P\) is

$$
R_P
=
\exp\left(V_i\int_{s_-}^{s_+}X^P_u\,du\right).
$$

For an end patch \(P\in\mathcal E_t\), define the terminal factor

$$
T_P^\xi
=
\begin{cases}
\xi(i), & X^P_{t-}=1,\\
1, & X^P_{t-}=0.
\end{cases}
$$

The pre-averaged patch factors are

$$
f_P=\Sigma_P R_P,
\qquad
f_P^\xi=\Sigma_P R_P T_P^\xi.
$$

The global sign, potential, and terminal monomial split exactly as

$$
\begin{aligned}
\sigma_t
&=
\prod_{P\in\mathcal P_t}\Sigma_P,
\\
\exp\left(\int_0^t V(A_s)\,ds\right)
&=
\prod_{P\in\mathcal P_t}
\exp\left(V_{i(P)}\int_{s_-(P)}^{s_+(P)}X^P_u\,du\right),
\\
\chi_{A_t}(\xi)
&=
\prod_{P\in\mathcal E_t}T_P^\xi.
\end{aligned}
$$

The first identity uses that the dual starts with sign \(+\) and every sign-changing interaction is assigned to exactly one source patch. The second identity uses \(V(A_s)=\sum_{i\in A_s}V_i\) and the fact that the patches cover active spacetime. The third identity uses that only end patches reach time \(t\); an active site at time \(t\) contributes the factor \(\xi(i)\), while an inactive end patch contributes \(1\). Hence, conditional on \(\cG_t\), the duality weight equals

$$
\prod_{P\in\mathcal B_t} f_P
\prod_{P\in\mathcal E_t} f_P^\xi.
$$

By [patch factorization](patch-factorization.md), the remaining patch data are independent under the conditioned laws \(\mathbb P_P^{\operatorname{cons}}\). Therefore

$$
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(\int_0^t V(A_s)\,ds\right)
\chi_{A_t}(\xi)
\middle|\cG_t
\right]
=
\prod_{P\in\mathcal B_t}
\mathbb E_P^{\operatorname{cons}}[f_P]
\prod_{P\in\mathcal E_t}
\mathbb E_P^{\operatorname{cons}}[f_P^\xi].
$$

The [patch contribution](patch-contribution.md) formulas are precisely

$$
C(P)=\mathbb E_P^{\operatorname{cons}}[f_P],
\qquad
C(\xi,P)=\mathbb E_P^{\operatorname{cons}}[f_P^\xi].
$$

Taking expectation over \(\cG_t\), equivalently over the successful-interaction skeleton, gives the stated representation.

The deterministic ordering convention for simultaneous successful touches handles the null exceptional events without changing the formula.
