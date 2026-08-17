---
title: Finite-size strong-mixing criterion for uniform Glauber relaxation
status: literature
audit: current
tags:
  - ergodicity methods
  - finite-to-infinite
  - Glauber dynamics
---

# Finite-size strong-mixing criterion for uniform Glauber relaxation

## Criterion

Martinelli--Olivieri give a **finite-size** route to volume-uniform functional inequalities. Consider a finite-range discrete spin system and its reversible single-spin Glauber dynamics. Their hypothesis is a strong-mixing estimate verified in one sufficiently large reference cube $\Lambda_0$, uniformly over the boundary conditions appearing in that finite-volume condition. Theorems 1.2--1.3 show that, once the reference scale is large enough compared with the interaction range and mixing constants, this finite-scale hypothesis propagates to larger volumes assembled as "multiples" of $\Lambda_0$ and yields a logarithmic Sobolev inequality with a constant uniform in the large volume and admissible boundary condition. Consequently the Glauber semigroup is hypercontractive and converges exponentially to equilibrium, with uniform quantitative control.

The toolbox point is the quantifier order: one does **not** assume a Dobrushin--Shlosman mixing estimate already known for every large region. It is enough to verify a suitable mixing property on one controlled mesoscopic box and then bootstrap it to arbitrarily large structured volumes.

## Mechanism

The proof uses a renormalization/block-decimation construction. Tile a large region by copies of the basic cube. Spins are decimated in finitely many sublattice classes so that, after conditioning on the already exposed classes, the remaining effective interactions between well-separated blocks are weak. The finite-cube strong-mixing assumption controls how boundary conditions perturb each block law. Iterating the decimation therefore turns the original interacting measure into a hierarchy of progressively weaker conditional interactions.

At the terminal scale, standard perturbative/tensorization estimates give a [logarithmic Sobolev inequality](log-sobolev-modified-log-sobolev.md). The argument is then reconstructed through the finite decimation steps; because the number and geometry of those steps are scale-independent, the resulting LSI constant does not deteriorate with the total volume. Standard semigroup theory converts the uniform LSI into hypercontractivity and exponential relaxation of Glauber dynamics.

This differs from the [Dobrushin--Shlosman](dobrushin-shlosman-spatial-to-dynamical.md) entry. There the reusable input is a strong spatial-mixing condition already formulated uniformly through the specification. Here the reusable architecture is a **finite-size certification theorem**: prove mixing on one large enough cube, then use block decimation to manufacture the uniform large-volume functional inequality.

## Representative IPS use

The method is itself formulated for finite-range lattice spin systems with Glauber dynamics. Martinelli--Olivieri developed it to reach one-phase regimes where criteria demanding mixing for regions of arbitrary shape are unnecessarily restrictive. Their main result gives uniform logarithmic-Sobolev control, hypercontractivity, and exponential approach to equilibrium in the family of volumes that are multiples of the reference cube $\Lambda_0$. In attractive systems, the companion Part I develops related finite-volume mixing criteria and applications deeper into the one-phase region.

As a proof strategy, this is useful whenever a model permits sharp control of a single mesoscopic box--by cluster expansion, correlation decay, monotonicity, or direct finite-volume estimates--but a global uniform spatial-mixing theorem is harder to establish directly.

## Limitations

The finite-scale hypothesis is still a strong **uniform boundary-mixing** statement on the reference cube; checking one equilibrium correlation under one boundary condition is not enough. The reference cube may need to be very large as parameters approach criticality, and the theorem does not cross a phase transition where boundary influence remains macroscopic.

The original geometric conclusion is for a controlled family of large volumes--the paper calls them volumes "multiples" of $\Lambda_0$--rather than an unrestricted assertion for every irregular finite region. Extending to arbitrary shapes requires additional geometric arguments. The method is also built for finite-range reversible Gibbs/Glauber systems; nonreversible IPS, conservative dynamics, and hard kinetic constraints require different decimation and coercivity inputs. Finally, a finite-size criterion is useful only when the finite-box hypothesis can itself be proved analytically; numerical verification of one box is not, without error control uniform over all configurations and boundary conditions, a rigorous substitute.

## Sources

- Martinelli, Olivieri, *Approach to equilibrium of Glauber dynamics in the one phase region. II. The general case*, Section 1 and Theorems 1.2--1.3; Sections 2--3 for block decimation, https://doi.org/10.1007/BF02101930.
- Original MP_ARC preprint record and abstract, explicitly stating the finite-cube strong-mixing hypothesis and LSI/hypercontractive/exponential-convergence conclusion on volumes multiple of $\Lambda_0$: https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=93-21.
