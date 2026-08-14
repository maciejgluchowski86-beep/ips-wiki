---
title: Antithetic and ghost branching schemes
status: literature
tags:
  - PDE
  - branching process
  - Monte Carlo
  - variance reduction
  - Malliavin calculus
---

# Antithetic and ghost branching schemes

Ghost-particle and antithetic branching schemes modify derivative-weight branching estimators by coupling nearby Brownian descendants before applying the singular Malliavin weight. They are variance-reduction and renormalization devices built on the [branching-diffusion representation](mild-formulation-and-branching-diffusion-representation.md), rather than an analogue of the infinite differential-code mechanism in the [Nguwi--Penent--Privault coding tree](npp-coding-tree.md). Xavier Warin developed these constructions for semilinear gradient equations and explored extensions involving Hessian nonlinearities.

**References.** Xavier Warin, *Variations on branching methods for non linear PDEs*, arXiv:1701.07660. Xavier Warin, *Monte Carlo for high-dimensional degenerated Semi Linear and Full Non Linear PDEs*, arXiv:1805.05078; see [References](../meta/references.md).

## Ghost renormalization

For a first-derivative Malliavin weight, a raw factor has the short-time form

$$
\frac{\Delta W}{\Delta t}\,\Phi(X_{t+\Delta t}),
$$

whose weight has size \((\Delta t)^{-1/2}\). The renormalized construction introduces a *ghost* descendant that shares the ancestral history but suppresses the Brownian increment on the current edge. The weighted terminal factor is replaced schematically by

$$
\frac{\Delta W}{\Delta t}
\bigl(
\Phi(X_{t+\Delta t})-\Phi(X^{\mathrm{ghost}}_{t+\Delta t})
\bigr).
\tag{1}
$$

The subtracted term has zero contribution after averaging against the centered Brownian weight and therefore acts as a control variate. At the same time, regularity of \(\Phi\) makes the difference in (1) small when \(\Delta t\) is small. In the semilinear construction of Section 2.2 of arXiv:1701.07660, this removes the need to force the lifetime law to concentrate strongly near zero and permits exponential branching times in the examples discussed there.

The ghost construction is recursive. A ghost particle has its own descendants, with the relevant Brownian increment omitted from its path, so the same subtraction is available at later derivative-marked branches.

## Antithetic branching

Warin also pairs a Brownian increment \(\Delta W\) with its antithetic increment \(-\Delta W\). For value factors the two descendants are averaged, while for gradient factors the Malliavin weight multiplies a half-difference. Schematically,

$$
\Phi(X^+)
\quad\longmapsto\quad
\frac{\Phi(X^+)+\Phi(X^-)}{2}
$$

for an unmarked value factor, whereas a derivative factor uses

$$
\frac{\Delta W}{\Delta t}
\frac{\Phi(X^+)-\Phi(X^-)}{2}.
\tag{2}
$$

Section 2.2.2 of arXiv:1701.07660 combines this antithetic symmetry with the ghost subtraction. The paper checks the same finite-variance mechanism for the gradient term and reports substantial numerical variance reduction in its test cases.

## Hessian variants

A raw second-order Malliavin weight is more singular at short times. Warin therefore uses higher-dimensional families of ghosts and antithetic descendants to form second differences before the Hessian weight is applied. Section 3 of arXiv:1701.07660 gives several such representations for nonlinearities involving \(D^2u\); its third representation is an antithetic version using a six-ghost construction. The resulting combinations are discrete second differences designed to cancel the low-order terms responsible for the large variance.

The later paper arXiv:1805.05078 combines antithetic random variables with control variates for Hessian estimation in a Monte Carlo scheme that also accommodates degenerate diffusions. It proves convergence results for the semilinear part of the method and discusses a convergent setting with a driver linear in \(D^2u\), then tests more general fully nonlinear equations numerically.

## Convergence scope

The fully nonlinear extensions in these papers should not be read as a general proved branching representation theorem. *Variations on branching methods for non linear PDEs* explicitly describes the fully nonlinear scheme as numerically effective without a proof of convergence. *Monte Carlo for high-dimensional degenerated Semi Linear and Full Non Linear PDEs* likewise states that convergence of its fully nonlinear scheme is not proved, and its general Hamilton--Jacobi--Bellman examples are presented as numerical tests.

Thus the established role of the ghost and antithetic constructions is narrower: they provide control-variate and symmetry mechanisms that substantially improve derivative-weight estimators, with rigorous results in the semilinear and specified linear-Hessian regimes, while the general fully nonlinear use in these papers remains numerical.