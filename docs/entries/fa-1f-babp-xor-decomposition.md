---
title: BABP plus interface-stirring decomposition of one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - BABP
  - domain walls
  - graphical construction
  - chronology
---

# BABP plus interface-stirring decomposition of one-dimensional FA-1f

This entry records an exact generator decomposition for one-dimensional two-sided [FA-1f](fa-1f-model.md). It separates a slowed [BABP](babp-model.md) reaction layer from a reversible layer that only moves domain walls. The identity is useful for chronology-averaged constructions; it is not by itself an out-of-equilibrium convergence theorem.

Use vacancy variables \(z_x\in\{0,1\}\), with \(z_x=1\) vacant, equilibrium vacancy density \(q\in(0,1)\), and \(p=1-q\). Let \(E_x\) denote Bernoulli-\(q\) refresh at \(x\).

## Generator decomposition

The FA-1f constraint is

$$
c_x^{\rm FA}(z)=z_{x-1}\vee z_{x+1}.
$$

For binary variables,

$$
z_{x-1}\vee z_{x+1}
=\frac12(z_{x-1}+z_{x+1})
+\frac12\lvert z_{x-1}-z_{x+1}\rvert.
\tag{1}
$$

The first term is one half of the BABP constraint. Consequently

$$
L_{\rm FA}=\frac12L_{\rm BABP}+L_{\rm xor},
\tag{2}
$$

where

$$
L_{\rm xor}f(z)
=\frac12\sum_x
\mathbf 1\{z_{x-1}\ne z_{x+1}\}
(E_x-I)f(z).
\tag{3}
$$

Both summands in (2) are genuine Markov generators. Since their constraints do not depend on the refreshed spin, both are reversible with respect to the Bernoulli product equilibrium \(\mu_q\).

Formula (2) gives a literal chronology average through the Trotter product formula. On finite volume, and hence locally in infinite volume,

$$
e^{tL_{\rm FA}}
=\lim_{n\to\infty}
\left(
 e^{\frac{t}{2n}L_{\rm BABP}}
 e^{\frac{t}{n}L_{\rm xor}}
\right)^n.
\tag{4}
$$

Thus FA-1f can be viewed as alternating short BABP reaction intervals and short residual intervals, with the order averaged in the continuous-time limit.

## Domain-wall geometry of the residual layer

Put

$$
d_{x+1/2}=z_x\oplus z_{x+1}\in\{0,1\}.
$$

The XOR constraint in (3) is active exactly when

$$
d_{x-1/2}+d_{x+1/2}=1.
\tag{5}
$$

A refresh at \(x\) can only change these two adjacent walls. If (5) holds, after the refresh there is again exactly one wall among the two bonds: depending on the Bernoulli proposal, it either remains on its current bond or moves across \(x\). Therefore the residual layer neither creates nor annihilates domain walls; it only moves them.

On a finite cycle the total number of domain walls is consequently conserved by \(L_{\rm xor}\). In the spin picture, the residual layer moves an interface between a vacancy domain and an occupied domain but cannot create a new interface pair or delete an existing pair.

The BABP part of (2) is therefore the reaction layer, while \(L_{\rm xor}\) is an interface-stirring layer. This differs from the less useful identity obtained by subtracting the double-facilitation overlap from BABP: after slowing BABP by one half, the remainder has nonnegative rates.

## Relation to the exact FA--AA similarity transform

Jack, Mayer and Sollich give an exact tensor-product similarity transform between an FA model and the reversible reaction--diffusion process \(A+A\leftrightarrow0\). Their FA convention is the additive-rate model: a site with two facilitating neighbours refreshes at twice the rate of a site with one facilitating neighbour. In the present notation this is precisely BABP, not the OR-rate FA-1f generator in (1).

They explicitly distinguish the alternative convention in which the refresh rate is independent of whether one or two facilitating neighbours are present and state that their exact mapping applies only to the additive-rate convention. Consequently the FA--AA similarity transform proves statements about the BABP term in (2), but cannot be applied directly to \(L_{\rm FA}\). The residual interface-stirring layer is a genuine additional generator, and its transform under the BABP change of basis is not positivity preserving.

## Limitation

The decomposition does not imply that FA-1f inherits BABP's quasi-duality or its all-density convergence theorem. A change of basis that turns BABP into its positive quasi-dual need not preserve positivity of an additional Markov generator. Thus (2) should presently be used at the graphical or semigroup level: BABP intervals perform branching/coalescing reactions, and the residual intervals transport interfaces without changing their number.

This geometry is compatible with the [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md): complete local branch/coalescence excursions average the BABP-type reaction chronology, while intervening interface motion can be absorbed into moving connectors.
