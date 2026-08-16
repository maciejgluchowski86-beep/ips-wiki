---
title: Patch contribution
status: proved here
audit: current
tags:
  - signed additive set process
  - patch
  - spin systems
  - duality
---

# Patch contribution

Fix a labeled [patch](patch.md) $P$ based at $i=i(P)$. Let $X^P$ be its one-site active process under the [consistent patch law](patch-consistency-event.md). If $\mathsf X(P)=\mathsf O$, let $\alpha(P)\in\{\delta,\beta\}$ be the kind of its initial outgoing interaction.

The sign attached to the initial boundary is

$$
\sigma(P)
=
\begin{cases}
+,&\mathsf X(P)=\mathsf I,\\
\sigma_i^{\alpha(P)}(S(P)),&\mathsf X(P)=\mathsf O.
\end{cases}
$$

For a full patch $P\in\mathcal P$, define

$$
F(P)
=
\sigma(P)
\exp\left(
V_i\int_{s(P)}^{e(P)}X_u^P\,du
\right),
$$

$$
C(P)=\mathbb E_P^{\mathrm{con}}[F(P)].
$$

When $e(P)=\infty$, the exponential and expectation are interpreted by the finite-endpoint limit.

For an end patch $P\in\mathcal E_t$ and $z\in[0,1]$, define

$$
F(z,P)
=
\sigma(P)
\exp\left(
V_i\int_{s(P)}^tX_u^P\,du
\right)
z^{X_t^P},
$$

$$
C(z,P)=\mathbb E_P^{\mathrm{con}}[F(z,P)].
$$

Every end contribution is affine in $z$.

## Closed formulas

Set

$$
\alpha_i
=
\sum_{R\subseteq N(i)}\delta_i(R)
+
\sum_{\substack{R\subseteq N(i)\\R\ne\vn}}\beta_i(R),
$$

so $V_i=\alpha_i+a_i^\beta(\vn)$. For $\Delta\in[0,\infty]$ and $z\in[0,1]$, define

$$
\varphi_i(\Delta)
=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{-\alpha_i u}\,du,
$$

$$
\psi_i(\Delta,z)
=
\delta_i(\vn)
\int_0^\Delta e^{a_i^\beta(\vn)u}\,du
+
z e^{a_i^\beta(\vn)\Delta}.
$$

For an end patch of length $\Delta=e(P)-s(P)$,

$$
C(z,P)
=
\begin{cases}
\displaystyle
\frac{\psi_i(\Delta,z)}{\varphi_i(\Delta)},
&\mathsf X(P)=\mathsf I,\\[1.2em]
\displaystyle
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,z)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
&\mathsf X(P)=\mathsf O.
\end{cases}
\tag{1}
$$

For a full patch of length $\Delta=e(P)-s(P)$,

$$
C(P)
=
\begin{cases}
\displaystyle
\frac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
&\mathsf X(P)\mathsf Y(P)\in\{\mathsf{II},\mathsf{IE}\},\\[1.2em]
e^{V_i\Delta},
&\mathsf X(P)\mathsf Y(P)=\mathsf{IO},\\[0.8em]
\displaystyle
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,1)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
&\mathsf X(P)\mathsf Y(P)\in\{\mathsf{OI},\mathsf{OE}\},\\[1.2em]
\sigma_i^\beta(S)e^{V_i\Delta},
&\mathsf X(P)\mathsf Y(P)=\mathsf{OO}.
\end{cases}
\tag{2}
$$

A denominator can vanish only for a labeled patch having zero probability of occurring; every realized patch has positive normalizer.

The dual-to-spin substitutions are

$$
\delta_i(S)\sigma_i^\delta(S)=c_i^0(S),
\qquad
\beta_i(S)\sigma_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

In particular, if

$$
r_i=c_i^0(\vn)+c_i^1(\vn)>0,
\qquad
p_i^\circ=\frac{c_i^0(\vn)}{r_i},
$$

then

$$
\psi_i(u,z)=p_i^\circ+(z-p_i^\circ)e^{-r_i u}.
\tag{3}
$$

## Extension versus continuation probability

For an end patch $P$ and $u\ge e(P)$, the geometric extension $P^{\uparrow u}$ is defined on the [patch](patch.md) page. Its ordinary contribution is obtained from (1) using the extended length $u-s(P)$.

It is important that $C(z,P^{\uparrow u})$ is normalized only by the consistency probability of the **extended patch**. It does not contain the probability that the realized skeleton has no successful interaction during $[e(P),u)$. Probability-weighted continuation identities belong to the [late-interaction and relaxation](exponential-relaxation-under-confined-late-interactions.md) estimates.
