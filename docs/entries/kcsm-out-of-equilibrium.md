---
title: KCSM out of equilibrium
status: standard fact
tags:
  - KCSM
  - out of equilibrium
  - convergence
---

# KCSM out of equilibrium

Out-of-equilibrium KCSM questions concern convergence when the initial law is not the Bernoulli product invariant measure \(\mu_q\). They are motivated by quenches and by the failure of many standard tools for constrained non-attractive dynamics. This infinite-volume topic is distinct from finite-volume [KCSM relaxation and mixing](kcsm-relaxation-and-mixing.md).

**References.** Hartarsky and F. Toninelli, *Kinetically constrained models out of equilibrium*, Theorem 3.3; Hartarsky and Toninelli, *Kinetically constrained models*.

## Setup

Let \((\eta_t)_{t\ge0}\) be a [KCSM](kinetically-constrained-spin-model.md) with vacancy density \(q\), semigroup \((P_t)_{t\ge0}\), and invariant Bernoulli product measure \(\mu_q\). Given an initial law \(\nu\), out-of-equilibrium convergence asks whether

$$
\lim_{t\to\infty}\nu(P_t f)=\mu_q(f)
$$

for suitable [local functions](local-functions.md) \(f\).

## High-vacancy theorem

Let \(\mathcal U\) be a translation-invariant [update family](update-family.md) on \(\Z^d\). Let \(\widetilde q_c^{\mathrm{KCM}}\) be the critical vacancy density for positive spectral gap of the corresponding infinite-volume KCSM.

**Theorem.** Fix \(\alpha>0\). There exist constants \(\varepsilon\in(0,1)\) and \(c>0\), depending on \(\mathcal U\) and \(\alpha\), such that the following holds. Let \((\eta_t)_{t\ge0}\) be the infinite-volume \(\mathcal U\)-KCSM with equilibrium vacancy density

$$
q\in[1-\varepsilon,1]
$$

and initial law \(\mu_{q_0}\), where

$$
q_0\in[\widetilde q_c^{\mathrm{KCM}}+\alpha,1].
$$

Then for every local function \(f:\{0,1\}^{\Z^d}\to\R\) and every \(t\ge0\),

$$
\left|\E_{\mu_{q_0}}[f(\eta_t)]-\mu_q(f)\right|
\le
c^{-1}e^{-ct}\|f\|_\infty |\supp(f)|.
$$

This is Hartarsky--F. Toninelli, Theorem 3.3, translated from their convention in which the facilitating state is \(1\) to the wiki convention in which the facilitating state is \(0\).

## Initial laws beyond product measures

The product initial law in the theorem is not essential. The proof also applies to initial laws whose vacancy field stochastically dominates \(\mu_{q_0}\) in the natural product order.

## Model-specific pages

The [FA-1f out-of-equilibrium](fa-1f-out-of-equilibrium.md) and [East out-of-equilibrium](east-out-of-equilibrium.md) pages record model-specific results. These should be kept separate from the definitions of the [FA-1f model](fa-1f-model.md) and the [East model](east-model.md).
