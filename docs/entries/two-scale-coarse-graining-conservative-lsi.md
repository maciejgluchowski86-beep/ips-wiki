---
title: Two-scale coarse-graining for conservative coercivity
status: literature
audit: current
tags:
  - log-Sobolev
  - conservative dynamics
  - coarse graining
---

# Two-scale coarse-graining for conservative coercivity

## Criterion

A two-scale coercivity argument decomposes a constrained Gibbs measure into conditional microscopic fibers and a lower-dimensional coarse marginal. In Menz--Otto, pair neighboring spins and let \(P\) record their coarse averages. Disintegrate the canonical ensemble as

$$
\mu(dx)=\mu(dx\mid y)\,\bar\mu(dy),\qquad y=Px.
$$

Their Proposition 2.1 is a hierarchical LSI criterion: uniform logarithmic Sobolev control of the conditional measures \(\mu(dx\mid y)\), together with an LSI for the coarse marginal \(\bar\mu\) and a uniform estimate transferring gradients through conditional expectation, yields an LSI for \(\mu\) with constants independent of system size and conserved mean. Theorem 2.6 supplies the multiscale closure: after finitely many pair-renormalization steps, the renormalized single-site potential is uniformly strictly convex, so the terminal coarse measure satisfies LSI by convexity criteria. Iterating Proposition 2.1 lifts that coercivity back to the microscopic scale.

## Mechanism

Entropy has an exact two-scale decomposition:

$$
\operatorname{Ent}_{\mu}(f)
=
\int \operatorname{Ent}_{\mu(\cdot\mid y)}(f)\,\bar\mu(dy)
+
\operatorname{Ent}_{\bar\mu}(\bar f),
\qquad
\bar f(y)=\int f\,d\mu(\cdot\mid y).
$$

The first term is controlled by a microscopic conditional LSI. The second is controlled by a coarse LSI, provided \(|\nabla \bar f|^2/\bar f\) can be bounded by the microscopic Fisher information. In the conservative setting this derivative produces a covariance term; the principal technical input is an asymmetric Brascamp--Lieb-type covariance estimate.

The proof is then genuinely multiscale. Pairing spins replaces the original potential by a renormalized potential. Repeating the map averages progressively larger blocks. A local Cramer theorem shows that these coarse potentials eventually become uniformly strictly convex even when the original potential is only a bounded perturbation of a strictly convex function. Bakry--Emery gives coercivity at that terminal scale; the hierarchical criterion propagates it downward.

## Representative IPS use

Menz--Otto consider a continuous-spin canonical ensemble with fixed empirical mean and single-site potential

$$
\psi=\psi_c+\delta\psi,
$$

where \(\psi_c''\) is bounded below by a positive constant and \(|\delta\psi|+|\delta\psi'|\) is uniformly bounded. Theorem 1.6 proves an LSI for the canonical ensemble with a constant uniform in both system size \(N\) and conserved mean \(m\).

The ambient-gradient form corresponds to conservative relaxation on the mean hyperplane. Remark 1.7 uses the discrete Poincare inequality on a lattice cube of width \(L\) to convert this into the Kawasaki metric, obtaining an LSI constant of order \(L^{-2}\), the diffusive scaling expected for a conserved dynamics. Thus the method yields quantitative entropy relaxation for a conservative spin system rather than merely equilibrium concentration.

## Limitations

The two-scale route requires a coarse-graining map for which both the fibers and the marginal remain analytically tractable. The covariance estimate linking coarse and microscopic gradients is load-bearing and can fail for strongly interacting or nonconvex systems. Convexification after renormalization is also a substantive theorem, not an automatic consequence of averaging.

This architecture differs from the [Lu--Yau martingale method](lu-yau-martingale-conditional-variance.md). Lu--Yau reveals one coordinate or block through a filtration and closes a recursion for conditional variance/entropy. Two-scale coarse-graining instead simultaneously separates microscopic fibers from macroscopic variables and proves coercivity at the macroscopic level before lifting it back. Both may use equivalence-of-ensembles ideas, but their recursive interfaces are different.

The cited theorem treats a noninteracting Hamiltonian subject to a global conservation law; extensions to genuinely interacting conservative spins require additional coarse-Hamiltonian and covariance estimates. Uniform canonical LSI also does not imply an order-one Kawasaki gap: conservation enforces the diffusive \(L^{-2}\) dynamical scale.

## Sources

- Menz, Otto, *Uniform logarithmic Sobolev inequalities for conservative spin systems with super-quadratic single-site potential*, Theorem 1.6, Remark 1.7, Proposition 2.1 and Theorem 2.6, https://doi.org/10.1214/11-AOP715.
- Open primary version: https://arxiv.org/abs/1307.2338.
