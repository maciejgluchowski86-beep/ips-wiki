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

This is Theorem C of the canonical paper *Patch representations and convergence for facilitated spin systems*.

Let $\Lambda$ have polynomial growth of exponent $D$. Suppose the spin system is [patch positive](patch-positivity-property.md) and contains an environment-independent pure-death component of rate $\varepsilon>0$.

## Theorem

There is an invariant probability measure $\pi$ such that, for every local function $f$, there is $K_f<\infty$ with

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

for every $\mu\in\mathcal M_- = \bigcup_{K\ge0}\mathcal M_{-,K}$.

The dependence on $K$ in (1) is essential to the statement. The older wiki version incorrectly wrote a uniform supremum over the whole union $\mathcal M_-$.

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

## Proof mechanism

For $\mu\in\mathcal M_*$, the patch representation gives a nonnegative finite-horizon weight $W_t^\mu$ and limiting full-patch weight $W$. Three estimates control their difference:

1. [spatial confinement](undoing-duality-under-confined-interactions.md) bounds skeletons leaving a finite region by the zero-boundary finite-propagation error;
2. [late successful interactions](exponential-relaxation-under-confined-late-interactions.md) cost at most $e^{-\varepsilon T}$ because an outgoing-patch ancestry chain spans the full time to the interaction; and
3. on the event of no successful interaction after $T$, the end factors relax at rate $e^{-\varepsilon(t-T)}$.

For a suitable ball $R_T$,

$$
\left|
(\mu P_t)(\chi_A)-\mathbb E_A[W]
\right|
\le
2\rho_A(T,R_T)
+2e^{-\varepsilon T}
+(1+|R_T|)e^{-\varepsilon(t-T)}.
$$

Finite propagation gives $\rho_A(T,R_T)\le C_Ae^{-\varepsilon T}$ and polynomial growth gives $|R_T|\le C_A(1+T)^D$. Taking $T=t/2$ yields the rate in (1) for $\mathcal M_*$.

For $\mu\in\mathcal M_{-,K}$, set

$$
\overline\mu
=
\frac{\mu+K\mu_{\mathbf1}}{1+K}
\in\mathcal M_*.
$$

Since $\mu=(1+K)\overline\mu-K\mu_{\mathbf1}$, the $\mathcal M_*$ estimate gives the factor $1+2K$.

## Uniform exponential ergodicity

If

$$
\mathbf p^\star\le\frac12\mathbf1,
$$

then every probability measure belongs to $\mathcal M_{-,1}$. Hence $\pi$ is the unique invariant measure and

$$
\sup_{\eta\in\{0,1\}^\Lambda}
|P_tf(\eta)-\pi(f)|
\le
K_f(1+t)^D e^{-\varepsilon t/2}
$$

for every local $f$.
