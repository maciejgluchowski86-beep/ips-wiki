---
title: Late interactions and no-late relaxation
status: proved here
audit: current
tags:
  - patch
  - ergodicity
  - spin systems
  - convergence
  - pure deaths
---

# Late interactions and no-late relaxation

This entry records the two temporal estimates used with [spatial confinement](undoing-duality-under-confined-interactions.md) in the canonical paper's convergence proof. It replaces the older wiki statement based on an assumed uniform mixing theorem for finite-volume modified processes.

Suppose the spin system is patch positive and contains a pure-death component of rate $\varepsilon>0$. Removing that component gives a comparison system with patch contributions $C^\varepsilon$. For every patch with outgoing terminal boundary,

$$
C(P)
=
e^{-\varepsilon(e(P)-s(P))}C^\varepsilon(P).
\tag{1}
$$

Let $L_{T,t}$ be the event that no successful interaction occurs in $(T,t]$, and let $L_T$ be the event that no successful interaction occurs after $T$.

## Backward chain of outgoing patches

If $(i,u,S)$ is a successful-interaction record with $u>0$, there are distinct patches $P_1,\ldots,P_n$, each with outgoing terminal boundary, such that

$$
s(P_1)=0,
\qquad
e(P_n)=u,
$$

$$
e(P_k)=s(P_{k+1}),
\qquad
i(P_{k+1})\in N_*(i(P_k)),
$$

and hence

$$
\sum_{k=1}^n(e(P_k)-s(P_k))=u.
\tag{2}
$$

Multiplying (1) along this chain gives the exact survival factor $e^{-\varepsilon u}$.

## Late-interaction bound

For $\mu\in\mathcal M_*$ and $A\subseteq R\Subset\Lambda$,

$$
0
\le
\mathbb E_A\left[
W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}^c}
\right]
\le
e^{-\varepsilon T},
\tag{3}
$$

and

$$
0
\le
\mathbb E_A\left[
W\mathbf1_{E_T^R\cap L_T^c}
\right]
\le
e^{-\varepsilon T}.
\tag{4}
$$

## No-late-interaction relaxation

On $L_{T,t}$ the bulk factors are already fixed at time $T$. Every end patch at horizon $t$ contains the full interval $[T,t]$. The dependence of each affine end contribution on its terminal spin therefore relaxes at rate at least $\varepsilon$. Confinement bounds the number of end patches by $|R|$.

Consequently,

$$
\left|
\mathbb E_A\left[
W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}}
\right]
-
\mathbb E_A\left[
W\mathbf1_{E_T^R\cap L_T}
\right]
\right|
\le
(1+|R|)e^{-\varepsilon(t-T)}.
\tag{5}
$$

Together, spatial confinement, (3)-(4), and (5) give

$$
\left|
(\mu P_t)(\chi_A)-\mathbb E_A[W]
\right|
\le
2\rho_A(T,R)
+2e^{-\varepsilon T}
+(1+|R|)e^{-\varepsilon(t-T)}.
\tag{6}
$$

Taking $R$ to be a linearly growing confinement ball and $T=t/2$ yields the exponential-polynomial rate in the [common invariant-limit theorem](common-invariant-limit-under-uniform-pure-deaths.md).
