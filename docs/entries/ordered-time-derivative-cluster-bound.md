---
title: Ordered-time derivative-cluster bound
status: observation
audit: current
tags:
  - PDE
  - heat semigroup
  - Hessian
  - Holder regularity
  - ordered time
---

# Ordered-time derivative-cluster bound

This entry records the audited analytic derivative-cluster estimate that survives from the terminated quadratic-Hessian programme. It does not assert a coarsened branching representation.

## Setup

Fix
\[
0<\alpha<1,
\qquad
T>0,
\]
and write
\[
X=C^{\alpha/2,\alpha}([0,T]\times\mathbb T).
\]
For $m\geq1$, let
\[
0<s_1<\cdots<s_m<t\leq T.
\]
Given $G\in C^\alpha(\mathbb T)$ and $b_1,\ldots,b_m\in X$, define
\[
\Xi_1=b_1(s_1)P_{s_1}G,
\]
and, for $2\leq r\leq m$,
\[
\Xi_r
=b_r(s_r)
\partial_x^2P_{s_r-s_{r-1}}\Xi_{r-1}.
\]
Set
\[
I_m[b_1,\ldots,b_m;G](t,x;\mathbf s)
=
\partial_x^2P_{t-s_m}\Xi_m(x).
\tag{1}
\]
Define
\[
\mathfrak P_m(\alpha,T)
=
\sup
\frac{
\displaystyle
\sup_{t\leq T,x\in\mathbb T}
\int_{0<s_1<\cdots<s_m<t}|I_m|\,d\mathbf s
}{
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X
},
\tag{2}
\]
where the supremum is over nonzero inputs.

Let
\[
H_\alpha
=
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2},
\qquad
D_{\alpha,T}
=
\frac{2T^{\alpha/2}}{\alpha},
\qquad
A_{\alpha,T}=H_\alpha D_{\alpha,T}.
\tag{3}
\]

## Derivative-cluster estimate

For every $m\geq1$,
\[
\boxed{
\mathfrak P_m(\alpha,T)
\leq
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}.
}
\tag{4}
\]
Equivalently,
\[
\begin{aligned}
&\sup_{t\leq T,x\in\mathbb T}
\int_{0<s_1<\cdots<s_m<t}
|I_m[b_1,\ldots,b_m;G](t,x;\mathbf s)|\,d\mathbf s\\
&\qquad\leq
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X.
\end{aligned}
\tag{5}
\]

## Proof

Write
\[
K_r^{(k)}=\partial_x^{2k}P_r,
\qquad
M_Bf=Bf,
\]
and
\[
c_{2k,\alpha}
=
\mathbb E[|He_{2k}(Z)|\,|Z|^\alpha].
\]
The Hermite cancellation and multiplication-commutator bounds used here are
\[
\|K_R^{(k)}f\|_\infty
\leq
c_{2k,\alpha}R^{-k+\alpha/2}[f]_{C^\alpha},
\tag{6}
\]
and
\[
\|[K_R^{(k)},M_B]f\|_\infty
\leq
c_{2k,\alpha}R^{-k+\alpha/2}
[B]_{C^\alpha}\|f\|_\infty.
\tag{7}
\]

Set $s_{m+1}=t$ and
\[
r_j=s_{j+1}-s_j,
\qquad 1\leq j\leq m.
\]
Then $r_j>0$, $\sum_jr_j<t$, and
\[
s_1=t-\sum_{j=1}^m r_j.
\]
The change of variables from $(s_1,\ldots,s_m)$ to $(r_1,\ldots,r_m)$ has unit Jacobian. In particular, the initial heat interval is not an extra integration variable. With $B_j=b_j(s_j,\cdot)$,
\[
I_m
=
K_{r_m}^{(1)}M_{B_m}
K_{r_{m-1}}^{(1)}M_{B_{m-1}}
\cdots
K_{r_1}^{(1)}M_{B_1}P_{s_1}G.
\tag{8}
\]

Expand repeatedly with
\[
K_R^{(k)}M_B
=
M_BK_R^{(k)}+[K_R^{(k)},M_B].
\tag{9}
\]
Passing a multiplier joins the current derivative block to the next Hessian edge because
\[
K_R^{(k)}K_r^{(1)}=K_{R+r}^{(k+1)}.
\]
Taking the commutator terminates the current derivative cluster. Thus every term partitions the $m$ derivative edges into consecutive clusters. A term with $q$ clusters has $q-1$ cluster boundaries among the first $m-1$ multipliers, and the innermost multiplier has two terminal choices: the last cluster may end in its commutator or pass through it and reach $P_{s_1}G$. Hence the exact number of $q$-cluster terms is
\[
2\binom{m-1}{q-1}.
\tag{10}
\]

Consider a cluster of length $\ell$ and total derivative duration $R$. For fixed $R$, the simplex of its $\ell$ positive edge durations has volume
\[
\frac{R^{\ell-1}}{(\ell-1)!}.
\]
If the cluster ends at a multiplier, apply (7). If the innermost cluster reaches $G$, apply (6) and
\[
[P_{s_1}G]_{C^\alpha}\leq [G]_{C^\alpha}.
\]
After the internal subdivision is integrated, the cluster contributes at most
\[
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{11}
\]
Every multiplier appears exactly once and costs at most $\|b_j\|_X$.

By Cauchy--Schwarz and Hermite orthogonality,
\[
c_{2\ell,\alpha}
\leq
H_\alpha\sqrt{(2\ell)!}.
\]
Furthermore,
\[
\frac{\sqrt{(2\ell)!}}{(\ell-1)!}
=
\ell\sqrt{\binom{2\ell}{\ell}}
\leq
\ell2^\ell
\leq
4^\ell.
\]
Therefore
\[
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
\leq
H_\alpha4^\ell.
\tag{12}
\]

For a $q$-cluster term, the cluster lengths sum to $m$, so (12) contributes $H_\alpha^q4^m$. If the cluster totals are $R_1,\ldots,R_q$, then
\[
\int_{\substack{R_i>0\\\sum_iR_i<t}}
\prod_{i=1}^qR_i^{-1+\alpha/2}\,d\mathbf R
\leq
\prod_{i=1}^q
\int_0^T R^{-1+\alpha/2}\,dR
=
D_{\alpha,T}^q.
\tag{13}
\]
Hence each $q$-cluster term is bounded by
\[
4^mA_{\alpha,T}^q
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X.
\]
Summing (10) over $q$ gives
\[
\begin{aligned}
\mathfrak P_m(\alpha,T)
&\leq
2\,4^m
\sum_{q=1}^m
\binom{m-1}{q-1}A_{\alpha,T}^q\\
&=
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1},
\end{aligned}
\]
which is (4).
