---
title: High-density measure
status: definition
tags:
  - Bernoulli product measure
  - patch critical density
  - mixture
---

# High-density measure

A high-density measure for a patch-positive spin system is a mixture of [Bernoulli product measures](bernoulli-product-measure.md) whose one-density profiles lie above the [patch critical density](patch-critical-density.md).

**References.** None yet.

## Definition

Let

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

be the patch critical density profile. A probability measure \(\nu\) on \(\{0,1\}^\Lambda\) is high-density if there is a probability measure \(\Pi\), supported on

$$
\left\{
\mathbf p\in[0,1]^\Lambda:
\mathbf p\ge\mathbf p^\star
\right\},
$$

such that

$$
\nu
=
\int
\mu_{\mathbf p}\,\Pi(d\mathbf p).
$$

The family of high-density measures is denoted by \(\mathcal M_\star\). Equivalently, under a measure in \(\mathcal M_\star\), the spins are conditionally independent given a possibly random and spatially inhomogeneous one-density profile \(\mathbf p\ge\mathbf p^\star\).

## Basic properties

The family \(\mathcal M_\star\) is convex and weakly closed. Every high-density measure stochastically dominates the critical Bernoulli product measure:

$$
\nu\in\mathcal M_\star
\quad\Longrightarrow\quad
\mu_{\mathbf p^\star}\le_{\mathrm{st}}\nu.
$$

The converse does not hold in general.
