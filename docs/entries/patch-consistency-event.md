---
title: Patch consistency event
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Patch consistency event

Fix \(T\le\infty\) and a labeled [patch](patch.md) \(P\in\mathcal P_T\). Write

$$
i=i(P),
\qquad
s=s(P),
\qquad
e=e(P),
\qquad
S=S(P).
$$

Let \(I\) be the full marked interaction set in the [graphical construction](graphical-construction-of-signed-additive-set-process.md). The interior interaction data of \(P\) are all interactions outgoing from \(i\) strictly between its start and end times:

$$
\Sigma_P^\circ
=
\left\{
(i,u,\gamma,R)\in I:
s<u<e
\right\}.
$$

For every \(R\subseteq N(i)\), the times

$$
\left\{
u\in(s,e):
(i,u,\delta,R)\in\Sigma_P^\circ
\right\}
$$

form a Poisson point process of rate \(\delta_i(R)\). For every nonempty \(R\subseteq N(i)\), the times

$$
\left\{
u\in(s,e):
(i,u,\beta,R)\in\Sigma_P^\circ
\right\}
$$

form a Poisson point process of rate \(\beta_i(R)\). All these point processes are independent.

## Reference patch measure

Suppose first that \(\mathsf X(P)=\mathsf I\). The interaction that begins \(P\) is incoming from another source, possibly the formal source \(\infty\) at time zero. It is therefore not an interaction outgoing from \(i\). Set

$$
\Sigma_P=\Sigma_P^\circ
$$

and define \(\mathbb P_P\) to be the law of \(\Sigma_P^\circ\) described above.

Suppose instead that \(\mathsf X(P)=\mathsf O\). The interaction that begins \(P\) is outgoing from \(i\), occurs at time \(s\), and has target \(S\). Let

$$
\alpha\in\{\delta,\beta\}
$$

record whether this initial interaction is a split or a birth. Its law is

$$
\begin{aligned}
\mathbb P_P(\alpha=\delta)
&=
\frac{\delta_i(S)}
{\delta_i(S)+\beta_i(S)},
\\
\mathbb P_P(\alpha=\beta)
&=
\frac{\beta_i(S)}
{\delta_i(S)+\beta_i(S)}.
\end{aligned}
$$

The denominator is positive because the outgoing successful-interaction skeleton beginning \(P\) has target \(S\). The displayed probabilities arise by conditioning the union of the independent type-\(S\) split and birth clocks to have the initial interaction at time \(s\): its mark is selected proportionally to the two rates.

Under \(\mathbb P_P\), the variable \(\alpha\) is independent of \(\Sigma_P^\circ\), and

$$
\Sigma_P
=
\Sigma_P^\circ
\cup
\{(i,s,\alpha,S)\}.
$$

Thus, for an \(\mathsf{IY}\)-patch, \(\mathbb P_P\) is the law of \(\Sigma_P^\circ\). For an \(\mathsf{OY}\)-patch, it is the product law of \(\alpha\) and \(\Sigma_P^\circ\). Equivalently, the latter is the law of all interactions outgoing from \(i\) in \([s,e)\), conditional on the initial interaction being

$$
(i,s,\delta,S)
\qquad\text{or}\qquad
(i,s,\beta,S).
$$

Write \(\mathbb E_P\) for expectation under \(\mathbb P_P\), and let \(\Omega_P\) denote its sample space. The terminal label \(\mathsf Y(P)\) does not enter the reference measure.

## Local active process

Under \(\mathbb P_P\), define the local active indicator \((X_u^P)_{s\le u<e}\) from \(\Sigma_P\). Its initial value is

$$
X_s^P
=
\begin{cases}
1,
& \mathsf X(P)=\mathsf I,
\\
\mathbf 1_{\{\alpha=\beta\}},
& \mathsf X(P)=\mathsf O.
\end{cases}
$$

Read the interactions in \(\Sigma_P^\circ\) in chronological order. At \((i,u,\gamma,R)\), set

$$
X_u^P
=
\begin{cases}
X_{u-}^P,
& X_{u-}^P=0,
\\
0,
& X_{u-}^P=1\text{ and }\gamma=\delta,
\\
1,
& X_{u-}^P=1\text{ and }\gamma=\beta.
\end{cases}
$$

Between interactions, keep \(X^P\) constant. Thus inactive-source interactions are ignored, a death or split removes an active source, and a birth leaves an active source active.

## Consistency event

The terminal consistency event is

$$
\operatorname{Con}_+(P)
=
\begin{cases}
\{X_{e-}^P=1\},
& \mathsf Y(P)=\mathsf O,
\\
\Omega_P,
& \mathsf Y(P)\in\{\mathsf I,\mathsf E\}.
\end{cases}
$$

The consistency event of \(P\) is

$$
\operatorname{Con}(P)
=
\left\{
X_{u-}^P=0
\text{ for every }(i,u,\gamma,R)\in\Sigma_P^\circ
\text{ with }R\ne\vn
\right\}
\cap
\operatorname{Con}_+(P).
$$

The interior condition says that every nonempty-target interaction strictly inside the patch has inactive source. Otherwise it would be an additional successful interaction and would cut the patch. The terminal condition says that an outgoing terminal boundary can occur only if its source is active immediately before that boundary. Incoming and end terminal labels impose no terminal activity condition.

When \(\mathbb P_P(\operatorname{Con}(P))>0\), define the consistent patch measure by

$$
\mathbb P_P^{\mathrm{con}}(\cdot)
=
\mathbb P_P(\cdot\mid\operatorname{Con}(P)).
$$

Write \(\mathbb E_P^{\mathrm{con}}\) for expectation under \(\mathbb P_P^{\mathrm{con}}\). Equivalently,

$$
\mathbb E_P^{\mathrm{con}}[f]
=
\mathbb E_P[f\mid\operatorname{Con}(P)].
$$

## Cut and end patches

Let \(P\in\mathcal C_t\) be a cut patch and let \(Q=P^{(t)}\in\mathcal E_t\) be its end patch. Since \(e(Q)=t\) and \(\mathsf Y(Q)=\mathsf E\), the law \(\mathbb P_Q^{\mathrm{con}}\) uses only the interior interactions before \(t\) and imposes consistency only through time \(t\).

By contrast, \(\mathbb P_P^{\mathrm{con}}\) uses the interior interactions before the actual end time \(e(P)\) and the actual terminal label \(\mathsf Y(P)\). Thus the labeled objects \(P\) and \(Q\) determine the two consistency laws without an additional horizon index.

The consistent patch laws are the local input to [patch factorization](patch-factorization.md).
