---
title: Branching diffusions and Duhamel trees
status: standard fact
audit: current
tags:
  - PDE
  - branching process
  - branching diffusion
  - Duhamel formula
  - Monte Carlo
---

# Branching diffusions and Duhamel trees

A branching diffusion is a random tree whose particles move according to a diffusion between branching times. In probabilistic representations of nonlinear parabolic PDEs, diffusion edges realize the linear semigroup and offspring reproduce products in the mild nonlinearity.

**References.** Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Ann. Inst. H. Poincaré Probab. Statist.* 55(1) (2019), 184--210. Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, arXiv:2201.03882. See [References](../meta/references.md).

## Duhamel trees

For an integral equation

$$
u(t)=P_t\phi+\int_0^tP_{t-s}[B(u(s),u(s))]\,ds,
\tag{1}
$$

with bilinear $B$, repeatedly substituting the right-hand side for each occurrence of $u$ generates rooted binary trees. Internal vertices carry integration times, edges carry semigroup transfers, and leaves carry initial or terminal data. Higher-degree polynomial terms produce the corresponding offspring numbers.

A finite Duhamel tree is deterministic bookkeeping. A branching diffusion randomizes the same time and offspring choices.

## Randomizing an integration time

Let $\tau$ have density $\rho>0$ on the relevant interval. For integrable $F$,

$$
\int_0^hF(s)\,ds
=
\mathbb E\left[\mathbf1_{\{\tau<h\}}\frac{F(\tau)}{\rho(\tau)}\right].
\tag{2}
$$

The reciprocal density is an [importance-sampling compensator](importance-sampling-compensators.md). Offspring types may likewise be sampled with positive probabilities and compensated by their reciprocals.

## Branching diffusion data

On a finite horizon, a standard construction specifies for each particle a birth time and position, a positive lifetime, an offspring type, and possibly a mark. Between branch times the particle follows the underlying diffusion. At a branching vertex, finitely many children are born at the parent position.

The load-bearing independence condition is recursive: conditional on the data exposed at a branching vertex, distinct descendant subtrees are independent copies of the construction with the prescribed child types. Brownian increments on disjoint descendant branches are correspondingly independent after their common ancestral history is fixed.

The genealogy, branch times, types, and marks form a branching skeleton. Exactly which variables are included in a skeleton depends on the representation, so conditional-independence statements should always specify the sigma-field being conditioned on.

## Products from independent descendants

If a monomial contains $m$ factors and children $Y_1,\ldots,Y_m$ are conditionally independent given the branching data, then

$$
\mathbb E\left[\prod_{i=1}^mY_i\,\middle|\,\mathcal G\right]
=
\prod_{i=1}^m\mathbb E[Y_i\mid\mathcal G],
\tag{3}
$$

provided the product is integrable. Equation (3) is the probabilistic counterpart of multiplication in the mild equation.

## Nonexplosion and integrability

The [age-dependent branching theorem](age-dependent-branching-and-nonexplosion.md) gives a simple sufficient condition for finite-horizon nonexplosion in the Bellman--Harris setting: positive lifetimes and finite mean offspring, with the stated independence assumptions. Nonexplosion means every realized finite-horizon product has finitely many factors.

It does not imply $L^1$ integrability. Exact first-branch conditioning, moment bounds, [uniform integrability](uniform-integrability-and-passage-to-expectations.md), and passage from finite to infinite expansions are logically separate steps.

## Derivative marks

When the nonlinearity contains gradient factors, a child may carry an automatic-differentiation mark. The [HLOTW marked branching construction](marked-branching-diffusion-for-gradient-nonlinearities.md) uses finitely many gradient-mark types and Malliavin/Bismut weights. Other constructions may propagate differential codes instead. In either case, the short-time singularity of derivative weights enters the moment analysis but does not alter the elementary product mechanism (3).
