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

This is the patchwise form of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), after applying [patch factorization](patch-factorization.md) at the finite horizon \(t\). It expresses each evolved monomial as an average of products of bulk and end contributions.

Let \((P_t)_{t\ge0}\) be the spin-system semigroup, and let the signed additive dual start from \((A,+)\). Let \(\mathcal B_t\) and \(\mathcal E_t\) be the bulk and end patch families from the [patch](patch.md) entry. Let \(C(P)\) and \(C(\xi,P)\) be the [patch contributions](patch-contribution.md).

Write \(\mathbb E_A\) for expectation with respect to the successful-interaction skeleton of the dual started from \((A,+)\). The integrand below is \(\cG_t\)-measurable.

## Statement

For every \(A\Subset\Lambda\), every \(\xi\in\{0,1\}^\Lambda\), and every \(t\ge0\),

$$
P_t(\chi_A)(\xi)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P)
\right].
\tag{1}
$$

## Averaging over a general initial law

Let \(\mu\) be any probability measure on \(\{0,1\}^\Lambda\). Integrating (1) gives

$$
\mu(P_t\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal B_t}C(P)\,
\mu\left(
\prod_{P\in\mathcal E_t}
C(\eta(i(P)),P)
\right)
\right].
$$

Suppose now that the spin system has the [patch positivity property](patch-positivity-property.md), with critical profile \(\mathbf p^\star\) and centered monomials \(\chi_A^\star\) from the [high-density measure](high-density-measure.md) entry. Every end contribution is affine and can be written as

$$
C(z,P)
=
C(p_{i(P)}^\star,P)
+b(P)(z-p_{i(P)}^\star),
\qquad
C(p_{i(P)}^\star,P)\ge0,
\quad
b(P)\ge0.
$$

Distinct end patches are based at distinct sites. Hence

$$
\begin{aligned}
\mu\left(
\prod_{P\in\mathcal E_t}
C(\eta(i(P)),P)
\right)
=
\sum_{\mathcal Q\subseteq\mathcal E_t}
&\mu\left(
\chi_{\{i(P):P\in\mathcal Q\}}^\star
\right)
\prod_{P\in\mathcal Q}b(P)
\\
&{}\times
\prod_{P\in\mathcal E_t\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\end{aligned}
$$

In particular, every skeleton weight is nonnegative when \(\mu\in\mathcal M_\star\). This uses only the ordinary monomial patch representation.

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

For every

$$
P\in\mathcal B_t\cup\mathcal E_t,
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

For \(P\in\mathcal E_t\), also set

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
\qquad P\in\mathcal E_t.
$$

These are the unaveraged factors from the [patch contribution](patch-contribution.md) entry.

Every nonempty-target successful interaction contributes its sign to exactly one outgoing-initial patch. Pure deaths contribute no sign because

$$
a_i^\delta(\vn)=c_i(\mathbf 0)\ge0.
$$

Moreover, \(V(A_u)=\sum_{i\in A_u}V_i\), the patches partition the relevant site-time regions up to time \(t\), and the end patches record the state at time \(t\). Therefore

$$
\begin{aligned}
\sigma_t
&=
\prod_{P\in\mathcal B_t}\sigma_P
\prod_{P\in\mathcal E_t}\sigma_P,
\\
\int_0^tV(A_u)\,du
&=
\sum_{P\in\mathcal B_t}
V_{i(P)}\int_{s(P)}^{e(P)}X_u^P\,du
+
\sum_{P\in\mathcal E_t}
V_{i(P)}\int_{s(P)}^tX_u^P\,du,
\\
\chi_{A_t}(\xi)
&=
\prod_{P\in\mathcal E_t}
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
\prod_{P\in\mathcal E_t}F_t(\xi,P).
\tag{6}
$$

The factors in (6) are functions of the corresponding patch interaction data. Hence [patch factorization](patch-factorization.md) applied conditionally on \(\cG_t\) gives

$$
\begin{aligned}
\mathbb E_{(A,+)}\left[
\sigma_t
\exp\left(
\int_0^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
\middle|\cG_t
\right]
&=
\prod_{P\in\mathcal B_t}
\mathbb E_P^{\mathrm{con}}[F(P)]
\prod_{P\in\mathcal E_t}
\mathbb E_P^{\mathrm{con}}[F_t(\xi,P)]
\\
&=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P).
\end{aligned}
\tag{7}
$$

Taking expectation in (7) and using (2) proves (1).

The deterministic ordering convention for simultaneous successful touches handles the null exceptional events without changing the formulas.
