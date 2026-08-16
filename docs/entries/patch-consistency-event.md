---
title: Consistent patch law
status: definition
audit: current
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Consistent patch law

Fix a labeled [patch](patch.md) $P$, either in $\mathcal P$ or in a finite-horizon family $\mathcal P_T$. Write

$$
i=i(P),\qquad s=s(P),\qquad e=e(P),\qquad S=S(P).
$$

The interior marks are the interactions outgoing from $i$ strictly between the endpoints:

$$
\Sigma_P^\circ
=
\{(i,u,\gamma,R)\in I:s<u<e\}.
$$

Under the reference law, the type-$(\delta,R)$ and type-$(\beta,R)$ points in this interval are independent Poisson processes with their graphical-construction rates.

## Reference patch law

If $\mathsf X(P)=\mathsf I$, the initial interaction is incoming from another source, so set

$$
\Sigma_P=\Sigma_P^\circ.
$$

If $\mathsf X(P)=\mathsf O$, the initial interaction is outgoing from $i$ with target $S$, but the successful-interaction skeleton does not record whether it is a split or a birth. Let $\alpha(P)\in\{\delta,\beta\}$ satisfy

$$
\mathbb P_P(\alpha(P)=\delta)
=
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)},
$$

$$
\mathbb P_P(\alpha(P)=\beta)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)},
$$

independently of $\Sigma_P^\circ$, and set

$$
\Sigma_P
=
\Sigma_P^\circ\cup\{(i,s,\alpha(P),S)\}.
$$

Write $\mathbb E_P$ for expectation under this reference law $\mathbb P_P$.

## Local active process

Reconstruct the one-site active indicator $X^P$ from $\Sigma_P$. Its initial value is

$$
X_s^P
=
\begin{cases}
1,&\mathsf X(P)=\mathsf I,\\
\mathbf 1_{\{\alpha(P)=\beta\}},&\mathsf X(P)=\mathsf O.
\end{cases}
$$

Read $\Sigma_P^\circ$ chronologically. A $\delta$-mark sends an active source to $0$; a $\beta$-mark leaves an active source at $1$; every mark at an inactive source is ignored. Between marks, $X^P$ is constant.

## Consistency

The candidate one-site process is consistent with the prescribed successful-interaction skeleton when it creates no additional successful interaction in the patch and, if the patch ends with an outgoing interaction, makes that terminal interaction successful. Thus

$$
\operatorname{Con}(P)
=
\left\{
X_{u-}^P=0
\text{ for every }(i,u,\gamma,R)\in\Sigma_P^\circ
\text{ with }R\ne\vn
\right\}
\cap
\begin{cases}
\{X_{e-}^P=1\},&\mathsf Y(P)=\mathsf O,\\
\Omega_P,&\mathsf Y(P)\in\{\mathsf I,\mathsf E\}.
\end{cases}
$$

For every realized patch,

$$
\mathbb P_P(\operatorname{Con}(P))>0.
$$

The consistent patch law is

$$
\mathbb P_P^{\mathrm{con}}(\cdot)
=
\mathbb P_P(\cdot\mid\operatorname{Con}(P)),
$$

with expectation $\mathbb E_P^{\mathrm{con}}$.

Conditional on the finite successful-interaction skeleton, the patch data are independent with precisely these laws; this is the [patch factorization theorem](patch-factorization.md).
