---
title: Hörmander-Malliavin propagation of noise to asymptotic smoothing
status: literature
audit: current
tags:
  - ergodicity
  - asymptotic strong Feller
  - Malliavin calculus
  - SPDE
---

# Hörmander-Malliavin propagation of noise to asymptotic smoothing

## Criterion

Consider a semilinear parabolic SPDE on a Hilbert space with additive noise acting in only finitely many directions and with a polynomial nonlinearity. Hairer and Mattingly develop an infinite-dimensional Hörmander scheme in which iterated brackets of the drift and forced constant vector fields generate sufficiently many regular directions.

The central quantitative object is the Malliavin covariance operator `M_t`. Section 6 proves that the bracket condition prevents `M_t` from being nearly singular on any fixed sufficiently regular finite-dimensional projection: directions with very small Malliavin covariance can have only a very small component in that projected subspace. Theorems 6.7 and 6.12 are the main quantitative nondegeneracy statements implementing this principle under the paper's moment and regularity assumptions.

Sections 5.2-5.6 then turn this partial nondegeneracy into a smoothing estimate. A perturbation of the initial condition is transferred, as far as possible, to a perturbation of the driving Wiener path. The remaining error is pushed into strongly dissipative directions. Control of the noise variation and of the residual error yields the derivative estimate required for asymptotic strong Feller smoothing.

## Mechanism

Finite-dimensional Hörmander theory uses Lie brackets to show that noise spreads to unforced directions and that the transition density becomes smooth. In an SPDE, the Malliavin covariance cannot generally be bounded below on the entire infinite-dimensional state space. The paper replaces global ellipticity by a two-part argument.

First, bracket generation gives quantitative Malliavin nondegeneracy on the finitely many dynamically relevant low or unstable directions. The hard step is nonadapted: coefficients in the bracket expansion depend on the future noise. Section 7 proves lower bounds for stochastic **Wiener polynomials** with nonadapted Lipschitz coefficients, replacing the usual Norris lemma.

Second, parabolic dissipation contracts the complementary high modes. The Malliavin control therefore only has to reproduce the initial perturbation in the low modes; dissipation removes the residual high-mode derivative. This produces asymptotic, rather than finite-time, smoothing.

This is taxonomically separate from the asymptotic-strong-Feller uniqueness criterion itself. ASF says what smoothing property is enough to separate invariant supports; the present method is a reusable way to **prove** ASF from degenerate noise and nonlinear bracket propagation. It is also not a coupling argument: the principal calculation is Malliavin covariance and transfer of derivatives to Wiener space.

## Representative IPS use

Sections 8.3-8.4 treat stochastic reaction-diffusion equations and the stochastic Ginzburg-Landau equation with highly degenerate finite-dimensional forcing. The polynomial reaction term generates new directions through brackets with the forced modes. Once the bracket-generation and a priori estimates required by the abstract theory are checked, the Malliavin scheme supplies ASF; combined with the accessibility/support criterion from the authors' earlier ASF theory, this gives uniqueness of the invariant law in the stated examples.

The same paper also shows that the two-dimensional stochastic Navier-Stokes equations fit the general framework, demonstrating that the method is not tied to a single reaction polynomial.

## Limitations

The method requires strong analytic structure: a semilinear parabolic equation, polynomial-type nonlinearities, detailed moment/regularity bounds, and a verifiable bracket-generation condition. Malliavin nondegeneracy is only obtained in a projected sense, so dissipation of the complementary directions is essential.

The Hörmander-Malliavin estimates prove smoothing, not invariant-measure existence. Unique ergodicity still needs an existence argument and the weak irreducibility/accessibility input required by the ASF support-separation criterion. Nor does this theorem chain by itself provide a general total-variation mixing rate.

## Sources

Primary source: Hairer and Mattingly, *A Theory of Hypoellipticity and Unique Ergodicity for Semilinear Stochastic PDEs*, Electron. J. Probab. 16 (2011), Sections 5-7, especially Theorems 6.7 and 6.12, and applications in Sections 8.3-8.4, DOI `10.1214/EJP.v16-875`.
