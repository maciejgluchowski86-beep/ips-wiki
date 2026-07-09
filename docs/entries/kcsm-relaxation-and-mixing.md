---
title: KCSM relaxation and mixing
status: definition
tags:
  - KCSM
  - relaxation time
  - mixing time
---

# KCSM relaxation and mixing

Relaxation and mixing quantify the approach to equilibrium of a finite-volume [kinetically constrained spin model](kinetically-constrained-spin-model.md). They are distinct from qualitative [ergodicity](ergodicity.md) and from infinite-volume [out-of-equilibrium](kcsm-out-of-equilibrium.md) convergence.

## Spectral gap and relaxation time

For a finite-volume reversible KCSM with invariant measure \(\mu_q\), the spectral gap is the smallest nonzero eigenvalue of \(-\cL\) in \(L^2(\mu_q)\). The relaxation time is

$$
T_{\mathrm{rel}}=\operatorname{gap}(\cL)^{-1}.
$$

Equivalently, \(T_{\mathrm{rel}}\) is the best constant in the corresponding variance decay estimate.

## Mixing time

Let \(P_t\) be the finite-volume Markov semigroup and let \(\mu_q\) be the invariant measure on the finite state space. The total-variation mixing time at accuracy \(\varepsilon\in(0,1)\) is

$$
t_{\mathrm{mix}}(\varepsilon)
=
\inf\left\{t\ge0:
\sup_\eta \|P_t(\eta,\cdot)-\mu_q\|_{\mathrm{TV}}\le\varepsilon
\right\}.
$$

For a sequence of boxes or finite graphs, one studies the growth of \(t_{\mathrm{mix}}(\varepsilon)\) with system size and with the vacancy density \(q\). Model-specific behaviour differs strongly between examples such as the [FA-1f model](fa-1f-model.md) and the [East model](east-model.md).

## Precutoff

A sequence of finite chains has precutoff if the mixing window is bounded up to constant factors: for fixed \(0<\varepsilon<\delta<1\),

$$
\sup_n \frac{t_{\mathrm{mix}}^{(n)}(\varepsilon)}{t_{\mathrm{mix}}^{(n)}(\delta)}<\infty.
$$

Linear-time precutoff means that the mixing time is of the same order as the linear size of the system, up to constants depending on \(q\), the model, and the accuracy parameters.

## Relation to out-of-equilibrium convergence

Finite-volume mixing estimates and infinite-volume out-of-equilibrium convergence are related but not identical. Mixing starts from worst-case finite configurations and converges to the finite-volume invariant law. Out-of-equilibrium convergence usually fixes an infinite-volume initial law and tests convergence against [local functions](local-functions.md).
