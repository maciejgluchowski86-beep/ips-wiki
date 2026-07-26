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

Fix a [signed additive set process](signed-additive-set-process.md), its graphical construction, and a finite horizon \(T<\infty\). Let \(\cG_T\) be the [successful-interaction](successful-interaction.md) sigma algebra and let \(\mathcal P_T\) be the corresponding finite-horizon [patch](patch.md) family. This factorization is the probabilistic input for the [patch contribution](patch-contribution.md) formulas and the [patch representation of spin systems](patch-representation-of-spin-systems.md).

For \(P\in\mathcal P_T\), let \(\Sigma_P\), \(\Omega_P\), \(\mathbb P_P\), \(\mathbb E_P\), \(\operatorname{Con}(P)\), \(\mathbb P_P^{\mathrm{con}}\), and \(\mathbb E_P^{\mathrm{con}}\) be as in the [patch consistency event](patch-consistency-event.md) entry.

## Theorem

Conditional on \(\cG_T\), the patch interaction data \((\Sigma_P)_{P\in\mathcal P_T}\) are independent, and the conditional law of \(\Sigma_P\) is \(\mathbb P_P^{\mathrm{con}}\) for every \(P\in\mathcal P_T\).

Equivalently, for bounded measurable functions \(f_P:\Omega_P\to\mathbb R\),

$$
\mathbb E\left[
\prod_{P\in\mathcal P_T}f_P(\Sigma_P)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal P_T}
\mathbb E_P^{\mathrm{con}}[f_P(\Sigma_P)].
\tag{1}
$$

The products are finite almost surely by local finiteness of the graphical construction.

## Proof

Write

$$
G_T=(Y_0,\mathcal I_T),
\qquad
\cG_T=\sigma(G_T),
$$

and fix a regular conditional law given \(G_T\). A realization \(g\) of \(G_T\) fixes a finite collection of boundary interactions and a finite labeled patch family

$$
\mathcal R=\mathcal P_T(g).
$$

We first describe the Poisson data after the boundary locations in \(g\) have been fixed, but before requiring that these are exactly the successful interactions. Distinct patches have disjoint source-time regions. Independent Poisson increments therefore give the product reference law

$$
\mathbb P_g^0
=
\bigotimes_{P\in\mathcal R}\mathbb P_P
\tag{2}
$$

for the raw patch data. At an outgoing boundary with source \(i\) and target \(S\), the boundary point belongs to the union of the type-\(S\) split and birth clocks. Its unrecorded kind is independent of the interior data and satisfies

$$
\mathbb P(\alpha=\delta)
=
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)},
\qquad
\mathbb P(\alpha=\beta)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)}.
\tag{3}
$$

This is precisely the initial-mark law included in \(\mathbb P_P\) for an outgoing patch. Formally, (2)--(3) follow by disintegrating the joint law of the finitely many ordered Poisson points. They do not treat an event of the form “there is a point at this prescribed time” as having positive probability.

It remains to identify the restriction on the raw patch data that makes \(g\) the complete successful skeleton. The required identity is

$$
\{\text{the successful skeleton through time \(T\) is \(g\)}\}
\quad\Longleftrightarrow\quad
\bigcap_{P\in\mathcal R}\operatorname{Con}(P),
\tag{4}
$$

relative to the fixed boundary points of \(g\).

The forward implication follows directly from the definition of consistency. For the reverse implication, read the boundary interactions in chronological order. At time zero the incoming patches reproduce the prescribed active set. Between consecutive boundary times, each local indicator \(X^P\) follows the global active state at its site: empty-target deaths act in both processes, while the interior consistency condition ensures that every nonempty-target interaction inside a patch has inactive source and hence is not an unrecorded successful interaction. At an outgoing boundary, terminal consistency makes the source active immediately before the boundary interaction. That interaction is therefore successful, its hidden kind gives the prescribed source state after the interaction, and its targets begin the prescribed incoming patches. This reconstructs the active process and the skeleton up to the next boundary time. Induction proves (4).

By (2) and (4), the regular conditional kernel given \(G_T=g\) is

$$
\begin{aligned}
\mathbb P\left(
d(\Sigma_P)_{P\in\mathcal R}
\middle|G_T=g
\right)
&=
\frac{
\prod_{P\in\mathcal R}
\ind(\operatorname{Con}(P))\,\mathbb P_P(d\Sigma_P)
}{
\prod_{P\in\mathcal R}
\mathbb P_P(\operatorname{Con}(P))
}
\\
&=
\bigotimes_{P\in\mathcal R}
\mathbb P_P^{\mathrm{con}}(d\Sigma_P).
\end{aligned}
\tag{5}
$$

The denominator in (5) is positive for almost every realized skeleton \(g\). Integrating the product functions against (5) proves (1).

Although the graphical construction contains clocks at every site of \(\Lambda\), a finite-horizon skeleton started from a finite active set contains only finitely many relevant interactions and touches only finitely many sites. Thus (2)--(5) involve only finitely many source-time strips, and no separate infinite-volume argument is needed.

The theorem is a finite-horizon statement. Full patches and their limiting contributions can be used without conditioning on the all-time successful skeleton.
