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

Fix a labeled [patch](patch.md) $P$ based at $i=i(P)$. Let $X^P$ be its one-site active process under the [consistent patch law](patch-consistency-event.md). If $\mathsf X(P)=\mathsf O$, let $\alpha(P)\in\{\delta,\beta\}$ be the hidden kind of its initial outgoing interaction.

The sign assigned to the initial boundary is

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
\qquad
C(P)=\mathbb E_P^{\mathrm{con}}[F(P)].
\tag{1}
$$

When $e(P)=\infty$, the exponential is interpreted through finite upper endpoints; the contribution formulas below have a well-defined limit as the patch length tends to infinity.

For an end patch $P\in\mathcal E_t$ and $z\in[0,1]$, define

$$
F(z,P)
=
\sigma(P)
\exp\left(
V_i\int_{s(P)}^tX_u^P\,du
\right)z^{X_t^P},
\qquad
C(z,P)=\mathbb E_P^{\mathrm{con}}[F(z,P)].
\tag{2}
$$

The function $z\mapsto C(z,P)$ is affine.

## Closed formulas

Set

$$
\alpha_i
=
\sum_{R\subseteq N(i)}\delta_i(R)
+
\sum_{\substack{R\subseteq N(i)\\R\ne\varnothing}}\beta_i(R).
\tag{3}
$$

Thus $\alpha_i$ is the total rate of outgoing marked interactions at $i$ and

$$
V_i=\alpha_i+a_i^\beta(\varnothing).
$$

For $\Delta\in[0,\infty]$ and $z\in[0,1]$, put

$$
\varphi_i(\Delta)
=
e^{-\alpha_i\Delta}
+
\delta_i(\varnothing)
\int_0^\Delta e^{-\alpha_i u}\,du,
\tag{4}
$$

and

$$
\psi_i(\Delta,z)
=
\delta_i(\varnothing)
\int_0^\Delta e^{a_i^\beta(\varnothing)u}\,du
+
z e^{a_i^\beta(\varnothing)\Delta}.
\tag{5}
$$

At $\Delta=\infty$, both expressions are read by their limits.

### End patches

Let $P$ be an end patch, write

$$
i=i(P),
\qquad
S=S(P),
\qquad
\Delta=e(P)-s(P).
$$

Then

$$
C(z,P)
=
\begin{cases}
\displaystyle
\frac{\psi_i(\Delta,z)}{\varphi_i(\Delta)},
&\mathsf X(P)=\mathsf I,\\[1.3em]
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
\tag{6}
$$

This makes the affine dependence on $z$ explicit.

### Full patches

For a full patch of length $\Delta=e(P)-s(P)$,

$$
C(P)
=
\begin{cases}
\displaystyle
\frac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
&\mathsf X(P)\mathsf Y(P)\in\{\mathsf{II},\mathsf{IE}\},\\[1.3em]
e^{V_i\Delta},
&\mathsf X(P)\mathsf Y(P)=\mathsf{IO},\\[0.9em]
\displaystyle
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,1)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
&\mathsf X(P)\mathsf Y(P)\in\{\mathsf{OI},\mathsf{OE}\},\\[1.3em]
\sigma_i^\beta(S)e^{V_i\Delta},
&\mathsf X(P)\mathsf Y(P)=\mathsf{OO}.
\end{cases}
\tag{7}
$$

An infinite full patch has type $\mathsf{IE}$ or $\mathsf{OE}$, and the corresponding row of (7) is evaluated at $\Delta=\infty$. If a denominator in (6) or (7) vanishes, the corresponding labeled patch has zero probability of occurring. Every realized patch has a positive consistency normalizer.

## Spin-rate form

The dual data are related to the multilinear flip-rate coefficients by

$$
\begin{aligned}
\alpha_i
&=
\sum_{R\subseteq N(i)}|c_i^0(R)|
+
\sum_{\substack{R\subseteq N(i)\\R\ne\varnothing}}
|c_i^0(R)+c_i^1(R)|,\\
a_i^\beta(\varnothing)
&=-c_i^0(\varnothing)-c_i^1(\varnothing),\\
\delta_i(S)\sigma_i^\delta(S)&=c_i^0(S),
&\delta_i(S)&=|c_i^0(S)|,\\
\beta_i(S)\sigma_i^\beta(S)&=-c_i^0(S)-c_i^1(S),
&\beta_i(S)&=|c_i^0(S)+c_i^1(S)|.
\end{aligned}
\tag{8}
$$

Since $c_i^0(\varnothing)\ge0$, (4)-(5) become

$$
\varphi_i(\Delta)
=
e^{-\alpha_i\Delta}
+
c_i^0(\varnothing)
\int_0^\Delta e^{-\alpha_i u}\,du,
\tag{9}
$$

and

$$
\psi_i(\Delta,z)
=
c_i^0(\varnothing)
\int_0^\Delta
e^{-\left(c_i^0(\varnothing)+c_i^1(\varnothing)\right)u}\,du
+
z e^{-\left(c_i^0(\varnothing)+c_i^1(\varnothing)\right)\Delta}.
\tag{10}
$$

## Derivation of the formulas

### Incoming initial boundary

Suppose first that the patch starts with an incoming interaction, so $X_s^P=1$, and has terminal label $\mathsf I$ or $\mathsf E$. Consistency can occur in exactly two ways before the endpoint: either there is no outgoing mark, or the first outgoing mark is an empty-target death. Hence

$$
\mathbb P_P(\operatorname{Con}(P))
=
e^{-\alpha_i\Delta}
+
\delta_i(\varnothing)
\int_0^\Delta e^{-\alpha_i u}\,du
=
\varphi_i(\Delta).
\tag{11}
$$

The corresponding unnormalized weighted expectation with terminal variable $z$ is

$$
\delta_i(\varnothing)
\int_0^\Delta e^{(V_i-\alpha_i)u}\,du
+
z e^{(V_i-\alpha_i)\Delta}
=
\psi_i(\Delta,z),
\tag{12}
$$

because $V_i-\alpha_i=a_i^\beta(\varnothing)$. Dividing (12) by (11) proves the incoming row of (6). Setting $z=1$ gives the $\mathsf{II}$ and $\mathsf{IE}$ row of (7).

### Outgoing initial boundary

Suppose next that the patch starts outgoing with target $S$ and has terminal label $\mathsf I$ or $\mathsf E$. Conditional on the successful-interaction record at the initial boundary, the hidden kind has probabilities

$$
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)}
\qquad\text{and}\qquad
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)}.
$$

If $\alpha(P)=\delta$, the source leaves the dual-active set immediately, so consistency is automatic and the local factor is $\sigma_i^\delta(S)$. If $\alpha(P)=\beta$, the source remains active and the incoming calculation applies. Thus the consistency normalizer is

$$
\frac{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
}{
\delta_i(S)+\beta_i(S)
},
\tag{13}
$$

while the unnormalized weighted expectation is

$$
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,z)
}{
\delta_i(S)+\beta_i(S)
}.
\tag{14}
$$

Taking the ratio of (14) and (13) proves the outgoing row of (6), and setting $z=1$ gives the $\mathsf{OI}$ and $\mathsf{OE}$ row of (7).

### Outgoing terminal boundary

An outgoing terminal boundary requires the source to remain dual-active for the entire patch. If the patch starts incoming, this forces the local active indicator to stay $1$, so the factor is simply

$$
e^{V_i\Delta}.
$$

If the patch also starts outgoing, consistency forces the initial hidden kind to be $\beta$; the contribution is therefore

$$
\sigma_i^\beta(S)e^{V_i\Delta}.
$$

These are the $\mathsf{IO}$ and $\mathsf{OO}$ rows of (7). Taking $\Delta\to\infty$ proves the formulas for infinite patches whenever they occur.

## Empty-neighbour relaxation

Put

$$
r_i=c_i^0(\varnothing)+c_i^1(\varnothing).
$$

If $r_i>0$, define

$$
p_i^\circ=\frac{c_i^0(\varnothing)}{r_i}.
$$

Then (10) reduces to

$$
\psi_i(u,z)
=
p_i^\circ+(z-p_i^\circ)e^{-r_i u}.
\tag{15}
$$

Consequently,

$$
\psi_i(u+v,z)
=
\psi_i\bigl(u,\psi_i(v,z)\bigr).
\tag{16}
$$

If $r_i=0$, then $\psi_i(u,z)=z$, and (16) still holds.

## Geometric extension and continuation probability

Let $P$ be an end patch, let $u\ge e(P)$ be finite, and let $P^{\uparrow u}$ be its geometric extension. Its ordinary contribution is obtained from (6) by replacing the original length with $u-s(P)$:

$$
C(z,P^{\uparrow u})
=
\begin{cases}
\displaystyle
\frac{\psi_i(u-s(P),z)}{\varphi_i(u-s(P))},
&\mathsf X(P)=\mathsf I,\\[1.3em]
\displaystyle
\frac{
\delta_i(S(P))\sigma_i^\delta(S(P))
+
\beta_i(S(P))\sigma_i^\beta(S(P))
\psi_i(u-s(P),z)
}{
\delta_i(S(P))+\beta_i(S(P))\varphi_i(u-s(P))
},
&\mathsf X(P)=\mathsf O.
\end{cases}
\tag{17}
$$

The normalization in (17) is the consistency probability of the **extended patch shape**. It does not include the probability that the realized successful-interaction skeleton has no successful interaction during the added interval. The probability-weighted continuation identity used in the convergence proof is a separate statement and is proved on [late interactions and no-late relaxation](exponential-relaxation-under-confined-late-interactions.md).
