---
title: Patch factorization
status: proved here
tags:
  - duality
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
  - factorization
---

# Patch factorization

Fix a [signed additive set process](signed-additive-set-process.md), its graphical construction, and \(T\le\infty\). Let \(\cG_T\) be the [successful-interaction](successful-interaction.md) sigma algebra, with \(\mathcal I_\infty=\mathcal I\), and let \(\mathcal P_T\) be the [patch](patch.md) family, with \(\mathcal P_\infty=\mathcal P\). This factorization is the probabilistic input for the [patch contribution](patch-contribution.md) formulas and the [patch representation of spin systems](patch-representation-of-spin-systems.md).

For \(P\in\mathcal P_T\), let \(\Sigma_P\), \(\Omega_P\), \(\mathbb P_P\), \(\mathbb E_P\), \(\operatorname{Con}(P)\), \(\mathbb P_P^{\mathrm{con}}\), and \(\mathbb E_P^{\mathrm{con}}\) be as in the [patch consistency event](patch-consistency-event.md) entry.

## Statement

Conditional on \(\cG_T\), the patch interaction data \((\Sigma_P)_{P\in\mathcal P_T}\) are independent, and the conditional law of \(\Sigma_P\) is \(\mathbb P_P^{\mathrm{con}}\) for every \(P\in\mathcal P_T\).

Equivalently, for every finite \(\cG_T\)-measurable subfamily \(\mathcal Q\subseteq\mathcal P_T\) and bounded measurable functions \(f_P:\Omega_P\to\mathbb R\),

$$
\mathbb E\left[
\prod_{P\in\mathcal Q}f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal Q}
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\tag{1}
$$

When \(T<\infty\), local finiteness makes \(\mathcal P_T\) finite almost surely, so one may take \(\mathcal Q=\mathcal P_T\). When \(T=\infty\), (1) is understood as the corresponding finite-dimensional statement. All displayed consistent expectations are understood for patches with \(\mathbb P_P(\operatorname{Con}(P))>0\).

## Proof

Write

$$
G_T=(Y_0,\mathcal I_T),
\qquad
\cG_T=\sigma(G_T),
$$

and fix a version of the regular conditional law given \(G_T\). Fix a skeleton realization \(g\) outside the corresponding null set. Since \(\mathcal Q\) is \(\cG_T\)-measurable,

$$
\mathcal R=\mathcal Q(g)
$$

is now a fixed finite subfamily of the fixed labeled patch family \(\mathcal P_T(g)\).

For the selected patches, define the reference product measure

$$
\mathbb P_g^{\mathcal R}
=
\bigotimes_{P\in\mathcal R}\mathbb P_P
$$

on

$$
\Omega_g^{\mathcal R}
=
\prod_{P\in\mathcal R}\Omega_P,
$$

and write \(\mathbb E_g^{\mathcal R}\) for its expectation. Define the selected and outside patch sigma algebras by

$$
\mathcal F_{\mathcal R}
=
\sigma(\Sigma_P:P\in\mathcal R),
\qquad
\mathcal F_{\mathcal R}^c
=
\sigma(\Sigma_P:P\in\mathcal P_T(g)\setminus\mathcal R).
$$

Once the patch geometry and boundary data in \(g\) have been fixed, the source-time regions of distinct patches are disjoint. Independent Poisson increments, together with the rate-proportional law of each outgoing initial mark, therefore make

$$
\mathcal F_{\mathcal R}
\quad\text{and}\quad
\mathcal F_{\mathcal R}^c
$$

independent in the skeleton-fixed Poisson--Palm reference construction.

The consistency condition imposed by \(g\) on the selected coordinates is

$$
A_{\mathcal R}(g)
=
\bigcap_{P\in\mathcal R}\operatorname{Con}(P)
\in\mathcal F_{\mathcal R}.
$$

Let

$$
B_{\mathcal R}(g)\in\mathcal F_{\mathcal R}^c
$$

denote the condition that the patch data outside \(\mathcal R\) are consistent with the remaining part of the skeleton \(g\). Thus, after the geometric boundary information in \(g\) has been fixed, agreement with the complete revealed skeleton imposes \(A_{\mathcal R}(g)\) on the selected coordinates and \(B_{\mathcal R}(g)\) on the outside coordinates. Poisson data outside the patch regions are independent and integrate out.

We use the following elementary conditional-independence fact. If \(\mathcal A\) and \(\mathcal B\) are independent sigma algebras, \(X\) is \(\mathcal A\)-measurable, \(A\in\mathcal A\), and \(\mathcal H\subseteq\mathcal B\), then

$$
\mathbb E[X\mid\sigma(A)\vee\mathcal H]
=
\mathbb E[X\mid\sigma(A)].
\tag{2}
$$

Indeed, for \(C\in\sigma(A)\) and \(D\in\mathcal H\), independence gives

$$
\begin{aligned}
\mathbb E[X\ind(C)\ind(D)]
&=
\mathbb E[X\ind(C)]\mathbb P(D)
\\
&=
\mathbb E\left[
\mathbb E[X\mid\sigma(A)]\ind(C)
\right]\mathbb P(D)
\\
&=
\mathbb E\left[
\mathbb E[X\mid\sigma(A)]\ind(C)\ind(D)
\right],
\end{aligned}
$$

which proves (2) by a monotone-class argument.

Apply (2) with

$$
\mathcal A=\mathcal F_{\mathcal R},
\qquad
\mathcal B=\mathcal F_{\mathcal R}^c,
\qquad
A=A_{\mathcal R}(g),
\qquad
\mathcal H=\sigma(B_{\mathcal R}(g)).
$$

The outside consistency information can therefore be removed from the conditional law of the selected coordinates. In the regular conditional Poisson--Palm disintegration over \(g\), this gives

$$
\begin{aligned}
&\mathbb E\left[
\prod_{P\in\mathcal Q}f_P(\Sigma_P)
\middle|\cG_T
\right](g)
\\
&\qquad=
\mathbb E_g^{\mathcal R}\left[
\prod_{P\in\mathcal R}f_P(\Sigma_P)
\middle|A_{\mathcal R}(g)
\right].
\end{aligned}
\tag{3}
$$

The exact skeleton realization \(g\) may have probability zero under the original law; equation (3) is an identity of regular conditional kernels, not ordinary conditioning on the event \(\{G_T=g\}\). By contrast,

$$
\mathbb P_g^{\mathcal R}(A_{\mathcal R}(g))
=
\prod_{P\in\mathcal R}
\mathbb P_P(\operatorname{Con}(P))
>0,
$$

so the conditional expectation on the right of (3) is well defined.

Finally, the selected patch variables are independent under \(\mathbb P_g^{\mathcal R}\), and each consistency event depends only on its corresponding coordinate. Hence

$$
\begin{aligned}
&\mathbb E_g^{\mathcal R}\left[
\prod_{P\in\mathcal R}f_P(\Sigma_P)
\middle|A_{\mathcal R}(g)
\right]
\\
&\quad=
\frac{
\displaystyle
\prod_{P\in\mathcal R}
\mathbb E_P\left[
f_P(\Sigma_P)\ind(\operatorname{Con}(P))
\right]
}{
\displaystyle
\prod_{P\in\mathcal R}
\mathbb P_P(\operatorname{Con}(P))
}
\\
&\quad=
\prod_{P\in\mathcal R}
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\end{aligned}
\tag{4}
$$

Substituting \(\mathcal R=\mathcal Q(g)\) into (3)--(4) proves (1). The randomness of \(\mathcal Q\) causes no additional conditioning issue because it is fixed on each skeleton fiber. If desired, one may choose a measurable ordering of patch labels, enumerate the finite family \(\mathcal Q\), and apply the argument on each event \(\{|\mathcal Q|=n\}\).

For \(T=\infty\), the same proof is applied directly to the finite selected family \(\mathcal R\). No product measure over all of \(\mathcal P_\infty(g)\), and no ordinary conditioning on an infinite intersection of consistency events, is required.
