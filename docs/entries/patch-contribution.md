---
title: Patch contribution
status: definition
audit: current
tags:
  - signed additive set process
  - patch
  - spin systems
  - duality
---

# Patch contribution

Fix a labeled [patch](patch.md) $P$ and write

$$
i=i(P),\qquad s=s(P),\qquad e=e(P),\qquad S=S(P).
$$

Let $(X_u^P)_{s\le u<e}$ be the local active indicator under the [reference patch measure](patch-consistency-event.md#reference-patch-measure). If $\mathsf X(P)=\mathsf O$, let $\alpha_P\in\{\delta,\beta\}$ be the kind of its initial interaction. Define

$$
\sigma_P
=
\begin{cases}
1,&\mathsf X(P)=\mathsf I,\\
\sigma_i^{\alpha_P}(S),&\mathsf X(P)=\mathsf O.
\end{cases}
$$

When a patch is evaluated at $q\in[s,e]$, use

$$
X_q^P=
\begin{cases}
X_s^P,&q=s,\\
X_{q-}^P,&q>s.
\end{cases}
$$

## Definition

For a full patch $P\in\mathcal P$, define

$$
F(P)
=
\sigma_P\exp\left(V_i\int_s^eX_u^P\,du\right),
\qquad
C(P)=\mathbb E_P^{\mathrm{con}}[F(P)],
$$

where an infinite endpoint is interpreted by the corresponding increasing-endpoint limit whenever that limit exists.

For $s\le t\le e$, $t<\infty$, and $z\in[0,1]$, define

$$
F_t(z,P)
=
\sigma_P\exp\left(V_i\int_s^tX_u^P\,du\right)z^{X_t^P},
\qquad
C_t(z,P)=\mathbb E_P^{\mathrm{con}}[F_t(z,P)].
$$

For an end patch $P\in\mathcal E_t$, write $C(z,P)=C_t(z,P)$. For a configuration $\xi$ and a one-density profile $\mathbf p=(p_j)$, use

$$
C_t(\xi,P)=C_t(\xi(i),P),
\qquad
C_t(\mathbf p,P)=C_t(p_i,P),
$$

and analogously for $C$.

These are definitions. Their use in a representation theorem additionally requires the conditional [patch factorization](patch-factorization.md).

## Conditional closed-form identities

The project contains explicit formulas for the quantities above in terms of the dual rates. Those formulas depend on the unaudited patch calculations and are therefore recorded only conditionally.

Define

$$
\begin{aligned}
\alpha_i
&=
\sum_{R\subseteq N(i)}\delta_i(R)
+
\sum_{\vn\ne R\subseteq N(i)}\beta_i(R),\\
V_i&=\alpha_i+a_i^\beta(\vn),\\
\varphi_i(\Delta)
&=e^{-\alpha_i\Delta}
+\delta_i(\vn)\int_0^\Delta e^{-\alpha_i w}\,dw,\\
\psi_i(\Delta_-,\Delta_+,z)
&=\delta_i(\vn)\int_0^{\Delta_-}e^{a_i^\beta(\vn)w}\,dw
+z e^{a_i^\beta(\vn)\Delta_-}\varphi_i(\Delta_+).
\end{aligned}
$$

Assuming the current patch calculation is correct, with $\Delta_-=t-s$, $\Delta_+=e-t$, and $\Delta=e-s$,

$$
C_t(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta_-,\Delta_+,z)}{\varphi_i(\Delta)},
&\mathsf X(P)=\mathsf I,\ \mathsf Y(P)\in\{\mathsf I,\mathsf E\},\\[1.2em]
z e^{V_i\Delta_-},
&(\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),\\[1.2em]
\dfrac{\delta_i(S)\sigma_i^\delta(S)+\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta_-,\Delta_+,z)}
{\delta_i(S)+\beta_i(S)\varphi_i(\Delta)},
&\mathsf X(P)=\mathsf O,\ \mathsf Y(P)\in\{\mathsf I,\mathsf E\},\\[1.5em]
\sigma_i^\beta(S)z e^{V_i\Delta_-},
&(\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{1}
$$

The corresponding spin-system coefficient form follows from

$$
\delta_i(S)\sigma_i^\delta(S)=c_i^0(S),
\qquad
\beta_i(S)\sigma_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

No closed-form identity on this page is currently promoted beyond this conditional status.

## No-interaction continuation

Let $Q$ be an end patch based at $i$, and let $u\ge e(Q)$. Write $Q^{\uparrow u}$ for the continuation of $Q$ through time $u$ without an intervening successful interaction. Define its contribution, including the conditional probability of the continuation, by

$$
C(z,Q^{\uparrow u})
:=
C\left(\psi_i(u-e(Q),z),Q\right).
$$

This is the project convention for no-interaction continuation. If

$$
r_i=c_i^0(\vn)+c_i^1(\vn)>0,
\qquad
q_i=\frac{c_i^0(\vn)}{r_i},
$$

then the current unaudited closed-form calculation gives

$$
\psi_i(v,z)=q_i+(z-q_i)e^{-r_i v}
$$

and consequently, conditionally on that calculation,

$$
\partial_z C(z,Q^{\uparrow u})
=e^{-r_i(u-e(Q))}\,\partial_zC(z,Q),
$$

and

$$
C(Q^{\uparrow\infty})
:=\lim_{u\to\infty}C(z,Q^{\uparrow u})
=C(q_i,Q).
$$
