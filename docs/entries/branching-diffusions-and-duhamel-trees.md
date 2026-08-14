---
title: Branching diffusions and Duhamel trees
status: standard fact
tags:
  - PDE
  - branching process
  - branching diffusion
  - Duhamel formula
  - Monte Carlo
---

# Branching diffusions and Duhamel trees

A branching diffusion is a random tree whose particles move by diffusion between branching times. In probabilistic representations of nonlinear parabolic PDEs, the tree is obtained by randomizing the time integrals in a [mild or Duhamel formulation](mild-formulation-and-branching-diffusion-representation.md): diffusion edges realize the linear semigroup, while offspring reproduce products appearing in the nonlinearity.

**References.** Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, arXiv:1603.01727. Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882. See [References](../meta/references.md).

## From Duhamel to a tree

Consider, in forward time, an integral equation of the form

$$
u(t)
=P_t\phi
+\int_0^t P_{t-s}\bigl[B(u(s),u(s))\bigr]\,ds,
\tag{1}
$$

where \((P_t)_{t\geq0}\) is a diffusion semigroup and \(B\) is bilinear. Substituting the right-hand side of (1) for either occurrence of \(u\) produces another time integral. Repeating the substitution produces rooted binary trees: every occurrence of the bilinear term has two children, and every edge carries one semigroup transfer.

A *binary Duhamel tree* is this deterministic bookkeeping object. Its internal vertices are integration times and its leaves carry the terminal or initial data. Before randomization, the contribution of a fixed finite tree is an iterated time integral of products of semigroup transfers.

## Randomizing one time integral

Let \(\tau\) be a positive random variable with density \(\rho\), strictly positive on the time interval of interest. For an integrable function \(F\),

$$
\int_0^h F(s)\,ds
=
\mathbb E\left[
\ind(\tau<h)\frac{F(\tau)}{\rho(\tau)}
\right].
\tag{2}
$$

Thus an integration time may be sampled instead of integrated. The reciprocal factor \(1/\rho(\tau)\) is an [importance-sampling compensator](importance-sampling-compensators.md).

If the sampled lifetime exceeds the remaining horizon, the particle becomes a leaf. If it falls inside the horizon, the corresponding nonlinear term is evaluated and the particle branches.

## Definition

Fix a finite horizon. A *branching diffusion* consists of the following data.

1. Each particle has a birth time, birth position, and possibly a mark or code.
2. Between birth and death it follows a diffusion, independently of the motions of particles outside its ancestral line once the common past is fixed.
3. It receives a positive lifetime. If the lifetime reaches beyond the horizon, the particle is terminal.
4. If it dies before the horizon, an offspring type is sampled and a finite family of children is born at the death position.
5. Conditional on the information at a branching vertex, the descendant subtrees are independent copies of the construction with the prescribed child types.

The *branching skeleton* is the combinatorial information consisting of the genealogy, branch times, and offspring types. Conditional on this skeleton, the remaining Brownian increments and, in the standard construction, the descendant subtree data are independent across different branches.

## Products and offspring

Suppose a Duhamel integrand contains a monomial

$$
c\,u_1\cdots u_m.
$$

A branching event can create \(m\) children, one for each factor. If the descendants are conditionally independent and their expected contributions are \(u_1,\ldots,u_m\), then

$$
\mathbb E\left[
\prod_{i=1}^m Y_i
\,\middle|\,\text{branching data}
\right]
=
\prod_{i=1}^m\mathbb E[Y_i\mid\text{branching data}].
\tag{3}
$$

Equation (3) is the probabilistic counterpart of the product in the mild equation. The offspring probabilities may themselves be randomized; their reciprocals then appear as additional compensators.

## Nonexplosion

A representation on a finite horizon requires the random tree to contain only finitely many particles almost surely. The [age-dependent branching nonexplosion theorem](age-dependent-branching-and-nonexplosion.md) shows that, for the Bellman--Harris-type construction used here, strictly positive lifetimes together with finite mean offspring are enough. No deterministic positive lower bound on the lifetimes is required.

Nonexplosion guarantees that the random functional is defined as a finite product on every realized finite-horizon tree. It does **not** imply that the product is integrable.

## What exactness does and does not say

Conditioning on the first branching event and cancelling the sampling densities recovers the mild recursion whenever the relevant expectations may be interchanged. This is the basic exactness mechanism behind both the [HLOTW marked branching construction](marked-branching-diffusion-for-gradient-nonlinearities.md) and the [Nguwi--Penent--Privault coding tree](npp-coding-tree.md).

Exact first-branch conditioning is only an algebraic identity. Absolute integrability, [uniform integrability](uniform-integrability-and-passage-to-expectations.md), interchange of infinite sums with expectations, and convergence of an infinite Duhamel expansion are additional analytic questions. The negative results for the NPP tree concern precisely this distinction.
