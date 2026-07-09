---
title: KCSM out of equilibrium
status: standard fact
tags:
  - KCSM
  - out of equilibrium
  - convergence
---

# KCSM out of equilibrium

Out-of-equilibrium KCSM questions concern convergence when the initial law is not the Bernoulli product invariant measure \(\mu_q\). They are motivated by quenches and by the failure of many standard tools for constrained non-attractive dynamics.

**References.** Hartarsky and Toninelli, *Kinetically constrained models*; Hartarsky and F. Toninelli, *Kinetically constrained models out of equilibrium*.

## Setup

Let \((\eta_t)_{t\ge0}\) be a [KCSM](kinetically-constrained-spin-model.md) with vacancy density \(q\), semigroup \((P_t)_{t\ge0}\), and invariant Bernoulli product measure \(\mu_q\). Given an initial law \(\nu\), out-of-equilibrium convergence asks whether

$$
\lim_{t\to\infty}\nu(P_t f)=\mu_q(f)
$$

for suitable [local functions](local-functions.md) \(f\).

A common quench initial law is another Bernoulli product measure \(\mu_{q_0}\) with \(q_0\ne q\). Deterministic initial configurations are also important, especially for oriented models and front problems.

## Obstructions

KCSM may have blocked configurations or regions that cannot be legally updated. Therefore convergence can depend on the model, the lattice, the vacancy density \(q\), and the initial law \(\nu\). The invariant measure \(\mu_q\) may be reversible without being the unique invariant measure on the full configuration space.

## High-vacancy regime

For general KCSM, the most robust out-of-equilibrium results are in high vacancy density regimes. In the current convention this means \(q\) close to \(1\). Hartarsky and F. Toninelli prove exponential convergence to equilibrium in infinite volume and linear-time precutoff in finite volume for a broad class of KCSM in this regime, including critical models covered by their hypotheses.

## Model-specific pages

The [FA-1f out-of-equilibrium](fa-1f-out-of-equilibrium.md) and [East out-of-equilibrium](east-out-of-equilibrium.md) pages record model-specific results. These should be kept separate from the definitions of the [FA-1f model](fa-1f-model.md) and the [East model](east-model.md).
