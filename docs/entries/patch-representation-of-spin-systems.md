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

This is the patchwise form of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), after applying [patch factorization](patch-factorization.md). Conditioning on \(\cG_t\) gives a representation in terms of completed and finite-horizon end patches. Conditioning on \(\cG_\infty\) gives a representation in terms of completed and full cut patches.

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

Every nonempty-target successful interaction before time \(t\) contributes its sign to exactly one outgoing-initial patch. The only active-source interactions not represented by such patch boundaries are pure deaths, and their signed coefficient satisfies

$$
a_i^\delta(\vn)
=
c_i^0(\vn)
=
c_i(\mathbf 0)
\ge0.
$$

Hence \(\sigma_i^\delta(\vn)=+\), so pure deaths do not change the sign. Since the dual starts with sign \(+\),

$$
\sigma_t
=
\prod_{P\in\mathcal B_t}\sigma_P
\prod_{P\in\mathcal X_t^T}\sigma_P.
\tag{5}
$$

Since

$$
V(A_u)
=
\sum_{i\in A_u}V_i,
$$

and the patches partition the relevant site-time regions up to time \(t\),

$$
\begin{aligned}
\exp\left(
\int_0^tV(A_u)\,du
\right)
&=
\exp\left(
\sum_{P\in\mathcal B_t}
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
+
\sum_{P\in\mathcal X_t^T}
V_{i(P)}\int_{s(P)}^tX_u^P\,du
\right)
\\
&=
\prod_{P\in\mathcal B_t}
\exp\left(
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
\right)
\\
&\qquad\times
\prod_{P\in\mathcal X_t^T}
\exp\left(
V_{i(P)}\int_{s(P)}^tX_u^P\,du
\right).
\end{aligned}
\tag{6}
$$

The patches in \(\mathcal X_t^T\) are in one-to-one correspondence with the sites present in the patch family at time \(t\), and

$$
\begin{aligned}
\chi_{A_t}(\xi)
&=
\prod_{i\in A_t}\xi(i)
\\
&=
\prod_{P\in\mathcal X_t^T}
\xi(i(P))^{X_t^P}.
\end{aligned}
\tag{7}
$$

Multiplying (5)--(7) gives the exact patchwise decomposition

$$
\begin{aligned}
&\sigma_t
\exp\left(
\int_0^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
\\
&\quad=
\prod_{P\in\mathcal B_t}
\left[
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
\right)
\right]
\\
&\qquad\times
\prod_{P\in\mathcal X_t^T}
\left[
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^tX_u^P\,du
\right)
\xi(i(P))^{X_t^P}
\right].
\end{aligned}
\tag{8}
$$

The variables in distinct brackets are functions of the corresponding patch interaction data. Hence [patch factorization](patch-factorization.md) applied conditionally on \(\cG_T\) gives

$$
\begin{aligned}
&\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(
\int_0^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
\middle|\cG_T
\right]
\\
&\quad=
\prod_{P\in\mathcal B_t}
\mathbb E_P^{\mathrm{con}}\left[
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
\right)
\right]
\\
&\qquad\times
\prod_{P\in\mathcal X_t^T}
\mathbb E_P^{\mathrm{con}}\left[
\sigma_P
\exp\left(
V_{i(P)}\int_{s(P)}^tX_u^P\,du
\right)
\xi(i(P))^{X_t^P}
\right]
\\
&\quad=
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
\tag{9}
$$

Taking expectation in (9) and using (2) yields, when \(T=t\),

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P)
\right],
\tag{10}
$$

and, when \(T=\infty\),

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal C_t}C_t(\xi,P)
\right].
\tag{11}
$$

Equations (10) and (11) are the two equalities in (1).

The deterministic ordering convention for simultaneous successful touches handles the null exceptional events without changing the formulas.
