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
e=e(P).
$$

Let \(I\) be the interaction set of the underlying [signed additive set process](signed-additive-set-process.md). A patch beginning at a successful interaction retains that interaction skeleton as attached boundary data. Thus an \(\mathsf I\)-initial patch retains the incoming source-time-target skeleton, while an \(\mathsf O\)-initial patch retains its source-time-target skeleton without revealing whether the interaction is a split or a birth.

## Patch interaction data

The interaction data assigned to \(P\) are

$$
\begin{aligned}
\Sigma_P
&=
\Sigma_P^-\cup\Sigma_P^\circ,
\\
\Sigma_P^\circ
&=
\{(i,u,\alpha,S)\in I:s<u<e\},
\\
\Sigma_P^-
&=
\begin{cases}
\vn,
& \mathsf X(P)=\mathsf S,
\\
\{(j,s,S):S\ne\vn,\ i\in S,\ (j,s,\alpha,S)\in I
\text{ for some }\alpha\in\{\delta,\beta\}\},
& \mathsf X(P)=\mathsf I,
\\
\{(i,s,\alpha,S)\in I:S\ne\vn\},
& \mathsf X(P)=\mathsf O.
\end{cases}
\end{aligned}
$$

An incoming initial boundary contributes only its source-time-target skeleton to \(\Sigma_P\). An outgoing initial boundary contributes the update kind as well, because a birth keeps the source active while a split removes it.

The reference patch measure \(\mathbb P_P\) is the law of \(\Sigma_P\) conditional on the initial skeleton attached to \(P\). If \(\mathsf X(P)=\mathsf S\), this means only that site \(i\) is initially active. If \(\mathsf X(P)=\mathsf I\), the incoming skeleton \((j,s,S)\), with \(i\in S\), is fixed. If \(\mathsf X(P)=\mathsf O\), the source-time-target skeleton \((i,s,S)\) is fixed, but the update kind is sampled according to

$$
\mathbb P_P((i,s,\beta,S)\in\Sigma_P)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)},
\qquad
\mathbb P_P((i,s,\delta,S)\in\Sigma_P)
=
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)}.
$$

The source-\(i\) interaction processes in \((s,e)\) have their original Poisson law. This includes the entire interval \((s,\infty)\) when \(e=\infty\). Write \(\mathbb E_P\) for expectation under \(\mathbb P_P\).

## Local active process

Under \(\mathbb P_P\), define the local active indicator by

$$
X_u^P
=
\mathbf 1_{\{i\in A_u\}},
\qquad
s\le u<e.
$$

Its initial value is determined by the initial label and, for an outgoing initial boundary, the sampled update kind:

$$
X_s^P
=
\begin{cases}
1,
& \mathsf X(P)\in\{\mathsf S,\mathsf I\},
\\
\mathbf 1_{\{(i,s,\beta,S)\in\Sigma_P
\text{ for some }S\ne\vn\}},
& \mathsf X(P)=\mathsf O.
\end{cases}
$$

Inside \((s,e)\), deaths and splits set \(X^P\) to zero when it is active, births leave it active, and interactions arriving while it is inactive are ignored.

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
& \mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\end{cases}
$$

where \(\Omega_P\) is the sample space of the local interaction process after the initial skeleton has been fixed. The consistency event of \(P\) is

$$
\operatorname{Con}(P)
=
\left\{
X_{u-}^P=0
\text{ for every }(i,u,\alpha,S)\in\Sigma_P^\circ
\text{ with }S\ne\vn
\right\}
\cap
\operatorname{Con}_+(P).
$$

The interior condition says that no split or birth from source \(i\) is attempted while \(i\) is active in the interior of the patch. The terminal condition says that an outgoing terminal boundary can occur only if its source is active immediately before the boundary. Incoming and end terminal labels impose no terminal activity condition.

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

Thus \(\mathbb E_P^{\mathrm{con}}\) includes both the initial-skeleton conditioning built into \(\mathbb E_P\) and the consistency conditioning.

## Full patches and truncations

The same definition applies to finite-horizon and full patches because the conditioning horizon is encoded by the labeled patch itself. If \(Q\in\mathcal E_t\), then

$$
e(Q)=t,
\qquad
\mathsf Y(Q)=\mathsf E,
$$

so \(\mathbb P_Q^{\mathrm{con}}\) imposes consistency only through time \(t\) and has no terminal activity condition. If \(P\in\mathcal C_t\) is the corresponding full patch, then \(\mathbb P_P^{\mathrm{con}}\) imposes consistency through the actual end time \(e(P)\) and uses its full terminal label \(\mathsf Y(P)\).

In particular, for \(Q=P^{(t)}\), the two laws

$$
\mathbb P_{P^{(t)}}^{\mathrm{con}}
\qquad\text{and}\qquad
\mathbb P_P^{\mathrm{con}}
$$

usually differ. No additional horizon index is needed: later formulas range over \(Q\in\mathcal E_t\) when the first law is intended and over \(P\in\mathcal C_t\) when the second is intended.

The consistent patch laws are the local input to [patch factorization](patch-factorization.md).
