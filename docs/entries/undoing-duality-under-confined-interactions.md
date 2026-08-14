---
title: Undoing duality under confined interactions
status: conditional
audit: current
tags:
  - patch
  - duality
  - spin systems
  - Feynman-Kac
---

# Undoing duality under confined interactions

This page records the project confined-interaction identity as a **conditional statement**. It depends on the conditional Feynman--Kac duality and [patch representation of spin systems](patch-representation-of-spin-systems.md); those prerequisites are not currently verified project theorems.

Fix the notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md). For a finite initial set $A$, write

$$
Z_t^\xi
=
\sigma_t\exp\left(\int_0^tV(A_r)\,dr\right)\chi_{A_t}(\xi)
$$

and

$$
W_t^\xi
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P).
$$

Assume the conditional patch representation is valid, so that

$$
W_t^\xi=\mathbb E_{(A,+)}\left[Z_t^\xi\mid\cG_t\right].
\tag{1}
$$

## Confined interactions

For $0\le s\le u\le t$ and $R\subseteq\Lambda$, define

$$
E_{s,u}^R
=
\left\{
\text{every ordinary successful interaction }(i,r,S)\text{ with }s<r\le u
\text{ has }i\in R\text{ and }S\subseteq R
\right\}.
$$

Deaths have empty target and are unrestricted. Write $E_T^R=E_{0,T}^R$. When $A\subseteq R$, the project notation identifies this event with confinement of the [interaction cone](interaction-cone.md) to $R$ through time $T$. The event of no successful interaction in $(s,u]$ is $L_{s,u}=E_{s,u}^{\vn}$.

## Modified and zero-boundary systems

For $Q\subseteq\Lambda$, let $\xi^{Q,0}$ agree with $\xi$ on $Q$ and vanish on $Q^c$. Define

$$
c_{i,R}(\xi)
=
\begin{cases}
c_i(\xi^{R,0}),&i\in R,\\
c_i(\xi^{\{i\},0}),&i\notin R.
\end{cases}
\tag{2}
$$

Let $\cL_R$ be the spin-system generator with rates $c_{i,R}$ and let $P_t^R$ be its semigroup. Inside $R$ this is the original spin system with zero boundary condition. Outside $R$, sites evolve independently with constant empty-neighbour rates.

For $R\Subset\Lambda$, define the zero-boundary generator on $R$ by

$$
\cL^{R,0}f(\xi)
=
\sum_{i\in R}c_i(\xi^{R,0})\bigl(f(\xi^i)-f(\xi)\bigr),
$$

with semigroup $P_t^{R,0}$. For functions supported in $R$, the intended identification is $P_t^Rf=P_t^{R,0}f$.

## Conditional confined-interaction identity

Assume, in addition to (1), that the restricted dual/Feynman--Kac calculation used by the project is valid: forbidden successful interactions can be represented by killing, and the resulting restricted signed dual is the dual of the modified generator $\cL_R$ with the corresponding potential. Under these hypotheses, the project identity is

$$
\mathbb E_A\left[W_t^\xi\ind(E_{s,u}^R)\right]
=
\mathbb E_{(A,+)}\left[Z_t^\xi\ind(E_{s,u}^R)\right]
=
\left(P_{t-u}P_{u-s}^RP_s\chi_A\right)(\xi).
\tag{3}
$$

In particular, when $A\subseteq R$,

$$
\mathbb E_A\left[W_t^\xi\ind(E_T^R)\right]
=
\left(P_{t-T}P_T^{R,0}\chi_A\right)(\xi),
\tag{4}
$$

and

$$
\mathbb E_A\left[W_t^\xi\ind(E_{T,t}^R)\right]
=
\left(P_{t-T}^RP_T\chi_A\right)(\xi).
\tag{5}
$$

Equations (3)--(5) remain conditional until the dual restriction and the upstream patch representation complete independent verification.
