---
title: Common invariant limit under uniform pure deaths
status: proved here
audit: current
tags:
  - spin systems
  - invariant measures
  - local functions
  - patch positivity
  - pure death
---

# Common invariant limit under uniform pure deaths

This is Theorem C of the canonical paper *Patch representations and convergence for facilitated spin systems*, with its proof. Assume the standing spin-system hypotheses of uniformly bounded finite-range rates and Feynman-Kac integrability. Suppose in addition that $\Lambda$ has polynomial growth of exponent $D$, the spin system is [patch positive](patch-positivity-property.md), and it contains a pure-death component of rate $\varepsilon>0$.

Use the centered-moment classes $\mathcal M_*$, $\mathcal M_{-,K}$, and $\mathcal M_-$ from [centered-moment order and cones](high-density-measure.md).

## Theorem

There is an invariant probability measure $\pi$ such that, for every local function $f$, there is $K_f<\infty$ satisfying

$$
\sup_{\mu\in\mathcal M_{-,K}}
\left|
(\mu P_t)(f)-\pi(f)
\right|
\le
(1+2K)K_f(1+t)^D e^{-\varepsilon t/2}
\tag{1}
$$

for every $K\ge0$ and $t\ge0$. Consequently,

$$
\mu P_t\Rightarrow\pi
$$

for every

$$
\mu\in\mathcal M_-
=
\bigcup_{K\ge0}\mathcal M_{-,K}.
$$

The limiting monomial moments are

$$
\pi(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\mathbf1_{\{|\mathcal P|<\infty\}}
\right]
\qquad
(A\Subset\Lambda).
\tag{2}
$$

## Proof for initial laws in $\mathcal M_*$

Fix $A\Subset\Lambda$. For $\mu\in\mathcal M_*$, let $W_t^\mu$ and $W$ be the finite and limiting nonnegative patch weights from [late interactions and no-late relaxation](exponential-relaxation-under-confined-late-interactions.md). The patch representation gives

$$
(\mu P_t)(\chi_A)=\mathbb E_A[W_t^\mu].
\tag{3}
$$

For $A\subseteq R\Subset\Lambda$ and $0\le T<t$, decompose the difference between (3) and $\mathbb E_A[W]$ according to whether the pre-$T$ skeleton leaves $R$, whether a successful interaction occurs after $T$, and whether no such late interaction occurs:

$$
\begin{aligned}
(\mu P_t)(\chi_A)-\mathbb E_A[W]
={}&
\mathbb E_A\left[W_t^\mu\mathbf1_{(E_T^R)^c}\right]
-
\mathbb E_A\left[W\mathbf1_{(E_T^R)^c}\right]\\
&+
\mathbb E_A\left[W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}^c}\right]
-
\mathbb E_A\left[W\mathbf1_{E_T^R\cap L_T^c}\right]\\
&+
\mathbb E_A\left[W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}}\right]
-
\mathbb E_A\left[W\mathbf1_{E_T^R\cap L_T}\right].
\end{aligned}
\tag{4}
$$

The [spatial-confinement lemma](undoing-duality-under-confined-interactions.md) bounds the absolute contribution of the first line by

$$
2\rho_A(T,R),
$$

where

$$
\rho_A(T,R)
=
\|(P_T-P_T^{R,0})\chi_A\|_\infty.
$$

The late-interaction estimate bounds the second line by

$$
2e^{-\varepsilon T},
$$

and the no-late-interaction relaxation estimate bounds the third line by

$$
(1+|R|)e^{-\varepsilon(t-T)}.
$$

Thus

$$
\left|
(\mu P_t)(\chi_A)-\mathbb E_A[W]
\right|
\le
2\rho_A(T,R)
+2e^{-\varepsilon T}
+(1+|R|)e^{-\varepsilon(t-T)}.
\tag{5}
$$

By [finite propagation](finite-propagation-for-zero-boundary-restrictions.md), choose $v<\infty$ such that, for

$$
R_T=B(A,\lceil vT\rceil),
$$

one has

$$
\rho_A(T,R_T)\le C_Ae^{-\varepsilon T}.
\tag{6}
$$

Polynomial growth of exponent $D$ gives

$$
|R_T|\le C_A(1+T)^D.
\tag{7}
$$

Take $T=t/2$ in (5), with $R=R_T$. Equations (6)-(7) yield

$$
\sup_{\mu\in\mathcal M_*}
\left|
(\mu P_t)(\chi_A)-\mathbb E_A[W]
\right|
\le
K_A(1+t)^D e^{-\varepsilon t/2}.
\tag{8}
$$

The right-hand limit in (8) does not depend on $\mu$. Every local function is a finite linear combination of monomials, so for every local $f$ there is $K_f<\infty$ and a number $\ell(f)$ such that

$$
\sup_{\mu\in\mathcal M_*}
|(\mu P_t)(f)-\ell(f)|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{9}
$$

For a monomial, (8) identifies

$$
\ell(\chi_A)=\mathbb E_A[W],
$$

which is exactly the right-hand side of (2).

## Construction and invariance of the limiting law

The all-one product law $\mu_{\mathbf1}$ belongs to $\mathcal M_*$. Since the configuration space $\{0,1\}^\Lambda$ is compact in the product topology, the family $\mu_{\mathbf1}P_t$ has subsequential weak limits. Estimate (9) shows that every subsequential limit has the same value on every local function, hence there can be at most one such limit. Denote it by $\pi$. Therefore

$$
\mu_{\mathbf1}P_t\Rightarrow\pi.
$$

Equation (8) identifies the monomial moments of $\pi$ with (2), and (9) now becomes

$$
\sup_{\mu\in\mathcal M_*}
|(\mu P_t)(f)-\pi(f)|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{10}
$$

It remains to check invariance. Let $g$ be local and $s\ge0$. The Feller property gives continuity of $P_sg$. Hence

$$
\begin{aligned}
(\pi P_s)(g)
&=
\lim_{t\to\infty}(\mu_{\mathbf1}P_tP_s)(g)\\
&=
\lim_{t\to\infty}(\mu_{\mathbf1}P_{t+s})(g)\\
&=
\pi(g).
\end{aligned}
$$

Thus $\pi P_s=\pi$ for every $s\ge0$.

## Extension from $\mathcal M_*$ to $\mathcal M_{-,K}$

Let $\mu\in\mathcal M_{-,K}$. By definition,

$$
\overline\mu
=
\frac{\mu+K\mu_{\mathbf1}}{1+K}
\in\mathcal M_*.
\tag{11}
$$

Solving for $\mu$ gives

$$
\mu
=(1+K)\overline\mu-K\mu_{\mathbf1}.
\tag{12}
$$

For every local $f$, apply (10) separately to $\overline\mu$ and $\mu_{\mathbf1}$:

$$
\begin{aligned}
|(\mu P_t)(f)-\pi(f)|
&\le
(1+K)|(\overline\mu P_t)(f)-\pi(f)|\\
&\qquad+
K|(\mu_{\mathbf1}P_t)(f)-\pi(f)|\\
&\le
(1+2K)K_f(1+t)^D e^{-\varepsilon t/2}.
\end{aligned}
$$

This proves (1). Since every $\mu\in\mathcal M_-$ belongs to some $\mathcal M_{-,K}$, weak convergence to $\pi$ follows for every law in $\mathcal M_-$.

The factor $1+2K$ is part of the theorem. There is no uniform estimate over the full union $\mathcal M_-$ with a constant independent of $K$.

## Corollary: uniform exponential ergodicity when $\mathbf p^\star\le\frac12\mathbf1$

Suppose additionally that

$$
\mathbf p^\star\le\tfrac12\mathbf1.
\tag{13}
$$

Then $\pi$ is the unique invariant measure and, for every local $f$,

$$
\sup_{\eta\in\{0,1\}^\Lambda}
|P_tf(\eta)-\pi(f)|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{14}
$$

### Proof

For every configuration $\eta$ and every $A\Subset\Lambda$,

$$
\chi_A^*(\eta)
=
\prod_{i\in A}(\eta(i)-p_i^\star)
\ge
-\prod_{i\in A}(1-p_i^\star)
=
-\mu_{\mathbf1}(\chi_A^*),
\tag{15}
$$

because (13) gives $p_i^\star\le1-p_i^\star$. Averaging (15) under any probability measure $\mu$ gives

$$
\frac{\mu+\mu_{\mathbf1}}2(\chi_A^*)\ge0
$$

for every finite $A$. Hence every probability measure belongs to $\mathcal M_{-,1}$.

Apply (1) with $K=1$. In particular, it applies uniformly to every point mass $\delta_\eta$, proving (14) after absorbing the numerical factor into $K_f$. If $\nu$ is any invariant probability measure, then $\nu\in\mathcal M_{-,1}$ and

$$
|\nu(f)-\pi(f)|
=|(\nu P_t)(f)-\pi(f)|
\longrightarrow0
$$

for every local $f$. Thus $\nu=\pi$, proving uniqueness.

## Scope of the argument

The proof uses $\mathcal M_-$ only to control signs in centered expansions. Outside this class, the argument discards cancellations between terms of different signs. It does not prove that convergence fails from other initial laws.
