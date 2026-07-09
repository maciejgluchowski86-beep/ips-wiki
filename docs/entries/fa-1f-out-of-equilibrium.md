---
title: FA-1f out of equilibrium
status: standard fact
tags:
  - FA-1f
  - out of equilibrium
  - convergence
---

# FA-1f out of equilibrium

This entry records a convergence-to-equilibrium theorem for the [FA-1f model](fa-1f-model.md) started from a non-stationary initial law. It is a model-specific instance of the broader [KCSM out-of-equilibrium](kcsm-out-of-equilibrium.md) problem.

**Reference.** Blondel, Cancrini, Martinelli, Roberto, and Toninelli, *Fredrickson-Andersen one spin facilitated model out of equilibrium*, Theorem 2.1 and Remarks 2.3--2.4.

## Theorem

Let \((\eta_t)_{t\ge0}\) be FA-1f with vacancy density \(q>1/2\) on an infinite connected [polynomial-growth lattice](polynomial-growth-lattice.md) with \((k,D)\)-polynomial growth. Let \(\mu_q\) be its invariant Bernoulli product measure.

For \(i\in\Lambda\), let

$$
R_i(\eta)=\inf\{d(i,j):\eta(j)=0\}
$$

be the distance from \(i\) to the nearest vacancy. Let \(\nu\) be an initial law such that, for some \(\theta_0>1\),

$$
\kappa:=\sup_{i\in\Lambda}\E_\nu\left[\theta_0^{R_i(\eta)}\right]<\infty.
$$

Then for every [local function](local-functions.md) \(f\), there is a constant

$$
c=c(q,k,D,\kappa,|\supp(f)|)<\infty
$$

such that, for every \(t\ge2\),

$$
\left|\E_\nu[f(\eta_t)]-\mu_q(f)\right|
\le
c\|f\|_\infty
\begin{cases}
\exp(-t/c), & D=1,\\
\exp\left(-\left(t/(c\log t)\right)^{1/D}\right), & D>1.
\end{cases}
$$

## Product initial laws

If \(\nu=\mu_{q_0}\) is a Bernoulli product initial law with vacancy density \(q_0>0\), then the exponential-moment hypothesis on \(R_i\) holds for a suitable \(\theta_0>1\). Thus the theorem applies to every non-degenerate product initial law \(\mu_{q_0}\) with \(q_0>0\). The analogous model-specific oriented result is recorded under [East out of equilibrium](east-out-of-equilibrium.md).
