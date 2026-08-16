---
title: Spatial confinement of patch weights
status: proved here
audit: current
tags:
  - patch
  - finite propagation
  - spin systems
  - convergence
---

# Spatial confinement of patch weights

This entry records the confined-interaction identity and the spatial-confinement estimate used in the canonical paper's proof of the common invariant limit.

Fix $A\Subset\Lambda$. Let

$$
\mathbf{Cone}_T
=
\bigcup_{(i,u,S)\in\mathcal I_T}
(\{i\}\cup S)\setminus\{\infty\}
$$

be the [interaction cone](interaction-cone.md). For $A\subseteq R\Subset\Lambda$, set

$$
E_T^R=\{\mathbf{Cone}_T\subseteq R\}
\tag{1}
$$

and

$$
\rho_A(T,R)
=
\left\|(P_T-P_T^{R,0})\chi_A\right\|_\infty,
\tag{2}
$$

where $P_t^{R,0}$ is the original spin system restricted to $R$ with zero boundary.

Assume the spin system is patch positive and contains a pure-death component. For $\mu\in\mathcal M_*$ define

$$
W_t^\mu
=
\prod_{P\in\mathcal B_t}C(P)
\,\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right),
\tag{3}
$$

and

$$
W
=
\prod_{P\in\mathcal P}C(P)
\mathbf1_{\{|\mathcal P|<\infty\}}.
\tag{4}
$$

## Modified spin system

For a configuration $\eta$, let $\eta^{R,0}$ agree with $\eta$ on $R$ and be zero outside $R$. Define modified flip rates

$$
c_{i,R}(\eta)
=
\begin{cases}
c_i(\eta^{R,0}),&i\in R,\\
c_i(\eta^{\{i\},0}),&i\notin R.
\end{cases}
\tag{5}
$$

and let $\mathcal L^R$ and $P_t^R$ be the corresponding generator and semigroup. Inside $R$, this is the original system with zero boundary, while sites outside $R$ evolve independently. Hence, whenever $f$ depends only on spins in $R$,

$$
P_t^Rf=P_t^{R,0}f.
\tag{6}
$$

## Proposition: confined-interaction identity

For every $A\subseteq R\Subset\Lambda$, $0\le T\le t$, and every probability measure $\mu$,

$$
\mathbb E_A\left[W_t^\mu\mathbf1_{E_T^R}\right]
=
(\mu P_{t-T}P_T^{R,0})(\chi_A).
\tag{7}
$$

### Proof

First take a deterministic spin configuration $\eta$. Let

$$
Z_t^\eta
=
\sigma_t
\exp\left(\int_0^tV(A_s)\,ds\right)
\chi_{A_t}(\eta)
$$

be the signed-dual Feynman-Kac variable. By the Feynman-Kac integrability hypothesis, $Z_t^\eta$ is integrable. The pathwise patch factorization together with the [patch factorization theorem](patch-factorization.md) gives

$$
W_t^{\delta_\eta}
=
\mathbb E_A[Z_t^\eta\mid\mathcal G_t].
$$

Since $E_T^R\in\mathcal G_t$,

$$
\mathbb E_A\left[W_t^{\delta_\eta}\mathbf1_{E_T^R}\right]
=
\mathbb E_A\left[Z_t^\eta\mathbf1_{E_T^R}\right].
\tag{8}
$$

During the dual interval $[0,T]$, retain every empty-target death and retain a nonempty-target split or birth only when its source and all its targets lie in $R$. Let $\mathcal D_R$ be this truncated signed-dual generator. If the active set is $B$, the total rate of discarded nonempty-target interactions is

$$
\kappa_R(B)
=
\sum_{i\in B}
\sum_{\substack{
\varnothing\ne S\subseteq N(i)\\
i\notin R\text{ or }S\nsubseteq R
}}
\bigl(\delta_i(S)+\beta_i(S)\bigr).
\tag{9}
$$

The indicator $\mathbf1_{E_T^R}$ kills the signed dual at the first discarded successful interaction, so the Feynman-Kac operator on $[0,T]$ is

$$
\mathcal D_R+V-\kappa_R.
$$

For a signed active set $Y=(B,\sigma)$ with $B\subseteq R$, the multilinear expansion of the zero-boundary rates gives

$$
\begin{aligned}
\mathcal L_\eta^R H(Y,\eta)
={}&
\sigma\sum_{i\in B}
\sum_{S\subseteq N(i)\cap R}
a_i^\delta(S)
\chi_{(B\setminus\{i\})\cup S}(\eta)\\
&+
\sigma\sum_{i\in B}
\sum_{S\subseteq N(i)\cap R}
a_i^\beta(S)
\chi_{B\cup S}(\eta).
\end{aligned}
\tag{10}
$$

On the dual side, $\mathcal D_RH$ contains the same signed monomial terms with $S\subseteq R$ and subtracts the retained jump rate. Moreover,

$$
V(B)-\kappa_R(B)
=
\sum_{i\in B}
\left[
\sum_{S\subseteq N(i)\cap R}\delta_i(S)
+
\sum_{\substack{\varnothing\ne S\subseteq N(i)\cap R}}\beta_i(S)
+
a_i^\beta(\varnothing)
\right].
$$

Adding this potential cancels the jump-rate subtraction and restores the diagonal empty-target birth coefficient. Thus

$$
\mathcal L_\eta^R H(Y,\eta)
=
\mathcal D_RH(Y,\eta)
+
\bigl(V(B)-\kappa_R(B)\bigr)H(Y,\eta).
\tag{11}
$$

Use (11) on the dual time interval $[0,T]$ and the original monomial duality on $[T,t]$. Dual intervals act from right to left on observables, giving

$$
\mathbb E_A\left[Z_t^\eta\mathbf1_{E_T^R}\right]
=
(P_{t-T}P_T^R\chi_A)(\eta).
\tag{12}
$$

Since $A\subseteq R$, $\chi_A$ depends only on spins in $R$, so (6) changes $P_T^R$ into $P_T^{R,0}$. Combining (8) and (12), then integrating over $\mu$, proves (7).

## Lemma: spatial confinement

For every $\mu\in\mathcal M_*$,

$$
0
\le
\mathbb E_A\left[W_t^\mu\mathbf1_{(E_T^R)^c}\right]
\le
\rho_A(T,R),
\tag{13}
$$

and

$$
0
\le
\mathbb E_A\left[W\mathbf1_{(E_T^R)^c}\right]
\le
\rho_A(T,R).
\tag{14}
$$

### Proof

The patch representation gives

$$
\mathbb E_A[W_t^\mu]
=(\mu P_t)(\chi_A)
=(\mu P_{t-T}P_T)(\chi_A).
$$

Subtract (7):

$$
\mathbb E_A\left[W_t^\mu\mathbf1_{(E_T^R)^c}\right]
=
(\mu P_{t-T})\bigl((P_T-P_T^{R,0})\chi_A\bigr).
\tag{15}
$$

The left-hand side is nonnegative because patch positivity and $\mu\in\mathcal M_*$ make the skeleton weights nonnegative. The absolute value of the right-hand side is at most the sup norm in (2), proving (13).

For (14), apply (13) with the all-one initial law and a horizon $u\ge T$. On the event $|\mathcal P|<\infty$, the finite-horizon all-one patch weight converges to $W$ as $u\to\infty$, while $W=0$ on the complementary event. Fatou's lemma therefore gives

$$
\mathbb E_A\left[W\mathbf1_{(E_T^R)^c}\right]
\le
\liminf_{u\to\infty}
\mathbb E_A\left[W_u^{\mu_{\mathbf1}}\mathbf1_{(E_T^R)^c}\right]
\le
\rho_A(T,R).
$$

## Finite-propagation consequence

By [finite propagation for zero-boundary restrictions](finite-propagation-for-zero-boundary-restrictions.md), for any prescribed $a>0$ one can choose a directed ball

$$
R_T=B(A,\lceil vT\rceil)
$$

with $v<\infty$ such that

$$
\rho_A(T,R_T)\le C_Ae^{-aT}.
\tag{16}
$$

Polynomial growth is not needed for (16). It enters later, in the common-limit theorem, to give

$$
|R_T|\le C_A(1+T)^D.
$$

Spatial confinement is the first of the three estimates in the [common invariant-limit proof](common-invariant-limit-under-uniform-pure-deaths.md). The temporal estimates are proved on [late interactions and no-late relaxation](exponential-relaxation-under-confined-late-interactions.md).
