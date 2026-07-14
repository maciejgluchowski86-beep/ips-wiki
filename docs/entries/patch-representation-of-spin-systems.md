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

This is the patchwise form of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), after applying [patch factorization](patch-factorization.md). Conditioning on \(\cG_t\) gives a representation in terms of bulk and end patches. Conditioning on \(\cG_\infty\) gives a representation in terms of bulk and cut patches.

Let \((P_t)_{t\ge0}\) be the spin-system semigroup, and let the signed additive dual start from \((A,+)\). Let \(\mathcal B_t\), \(\mathcal C_t\), and \(\mathcal E_t\) be the bulk, cut, and end patch families from the [patch](patch.md) entry. Let \(C(P)\), \(C(\xi,P)\), and \(C_t(\xi,P)\) be the [patch contributions](patch-contribution.md).

Write \(\mathbb E_A\) for expectation with respect to the successful-interaction skeleton of the dual started from \((A,+)\). In the first representation below the integrand is \(\cG_t\)-measurable, while in the second it is \(\cG_\infty\)-measurable.

## Statement

For every \(A\Subset\Lambda\), every \(\xi\in\{0,1\}^\Lambda\), and every \(t\ge0\),

$$
\begin{aligned}
P_t(\chi_A)(\xi)
&=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P)
\right]
\\
&=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal C_t}C_t(\xi,P)
\right].
\end{aligned}
\tag{1}
$$

## Proof

The Feynman--Kac monomial duality formula gives

$$
P_t(\chi_A)(\xi)
=
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(
\int_0^t V(A_u)\,du
\right)
\chi_{A_t}(\xi)
\right].
\tag{2}
$$

Fix

$$
T\in\{t,\infty\}
$$

and condition on \(\cG_T\). To treat the two choices simultaneously, set

$$
\mathcal X_t^T
=
\begin{cases}
\mathcal E_t, & T=t,\\
\mathcal C_t, & T=\infty.
\end{cases}
$$

For every

$$
P\in\mathcal B_t\cup\mathcal X_t^T,
$$

let \(\alpha_P\in\{\delta,\beta\}\) be the kind of its initial interaction when \(\mathsf X(P)=\mathsf O\), and define

$$
\sigma_P
=
\begin{cases}
1,
& \mathsf X(P)=\mathsf I,
\\
\sigma_{i(P)}^{\alpha_P}(S(P)),
& \mathsf X(P)=\mathsf O,
\end{cases}
\tag{3}
$$

and

$$
X_u^P
=
\ind\{i(P)\in A_u\},
\qquad
s(P)\le u<e(P).
\tag{4}
$$

For \(P\in\mathcal X_t^T\), also set

$$
X_t^P
=
\ind\{i(P)\in A_t\}.
$$

When \(t=s(P)\), this is the state created by the initial interaction of \(P\); when \(t>s(P)\), it agrees almost surely with \(X_{t-}^P\).

Thus (3) is the local sign variable from the [patch contribution](patch-contribution.md) entry. On \(\operatorname{Con}(P)\), the process in (4) agrees with the local active indicator defined from \(\Sigma_P\).

Define

$$
F(P)
=
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
\right),
\qquad P\in\mathcal B_t,
$$

and

$$
F_t(\xi,P)
=
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^tX_u^P\,du
\right)
\xi(i(P))^{X_t^P},
\qquad P\in\mathcal X_t^T.
$$

These are the unaveraged factors from the [patch contribution](patch-contribution.md) entry.

Every nonempty-target successful interaction contributes its sign to exactly one outgoing-initial patch. Pure deaths contribute no sign because

$$
a_i^\delta(\vn)=c_i(\mathbf 0)\ge0.
$$

Moreover, \(V(A_u)=\sum_{i\in A_u}V_i\), the patches partition the relevant site-time regions up to time \(t\), and the patches in \(\mathcal X_t^T\) record the state at time \(t\). Therefore

$$
\begin{aligned}
\sigma_t
&=
\prod_{P\in\mathcal B_t}\sigma_P
\prod_{P\in\mathcal X_t^T}\sigma_P,
\\
\int_0^tV(A_u)\,du
&=
\sum_{P\in\mathcal B_t}
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
+
\sum_{P\in\mathcal X_t^T}
V_{i(P)}\int_{s(P)}^tX_u^P\,du,
\\
\chi_{A_t}(\xi)
&=
\prod_{P\in\mathcal X_t^T}
\xi(i(P))^{X_t^P}.
\end{aligned}
\tag{5}
$$

By the definitions of \(F(P)\) and \(F_t(\xi,P)\), these three equalities give the exact patchwise decomposition

$$
\sigma_t
\exp\left(
\int_0^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
=
\prod_{P\in\mathcal B_t}F(P)
\prod_{P\in\mathcal X_t^T}F_t(\xi,P).
\tag{6}
$$

The factors in (6) are functions of the corresponding patch interaction data. Hence [patch factorization](patch-factorization.md) applied conditionally on \(\cG_T\) gives

$$
\begin{aligned}
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(
\int_0^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
\middle|\cG_T
\right]
&=
\prod_{P\in\mathcal B_t}
\mathbb E_P^{\mathrm{con}}[F(P)]
\prod_{P\in\mathcal X_t^T}
\mathbb E_P^{\mathrm{con}}[F_t(\xi,P)]
\\
&=
\begin{cases}
\displaystyle
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P),
& T=t,
\\[1.2em]
\displaystyle
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal C_t}C_t(\xi,P),
& T=\infty.
\end{cases}
\end{aligned}
\tag{7}
$$

Taking expectation in (7), first with \(T=t\) and then with \(T=\infty\), and using (2), gives the two equalities in (1).

The deterministic ordering convention for simultaneous successful touches handles the null exceptional events without changing the formulas.
