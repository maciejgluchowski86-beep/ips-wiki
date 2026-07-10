---
title: Ergodicity
status: definition
tags:
  - invariant measure
  - convergence to equilibrium
  - uniform exponential ergodicity
---

# Ergodicity

For an [interacting particle system](interacting-particle-system.md), ergodicity is a convergence-to-equilibrium property. It is stronger than uniqueness of an [invariant measure](invariant-measure.md) and weaker than uniform exponential ergodicity.

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*; Levin, Peres, and Wilmer, *Markov Chains and Mixing Times*.

## Setup

Let \(\Lambda\) be a countable [lattice](lattice-and-graph.md), let \(\mathcal S\) be a finite single-site state space, and let

$$
\Omega=\mathcal S^\Lambda.
$$

Let \((P_t)_{t\ge0}\) be the Markov semigroup of an interacting particle system on \(\Omega\). For a probability measure \(\mu\) on \(\Omega\), write \(\mu P_t\) for the law at time \(t\) started from \(\mu\):

$$
\int_\Omega f(\eta)\, (\mu P_t)(d\eta)
=
\int_\Omega P_t f(\eta)\,\mu(d\eta).
$$

## Invariant measure

A probability measure \(\nu\) on \(\Omega\) is [invariant](invariant-measure.md) if

$$
\nu P_t=\nu
\qquad\text{for every }t\ge0.
$$

An IPS has a unique invariant measure if exactly one probability measure \(\nu\) satisfies this identity. Uniqueness alone does not assert that \(\mu P_t\) converges to \(\nu\) as \(t\to\infty\).

## Ergodicity

The IPS is ergodic if there is a probability measure \(\nu\) such that, for every initial probability measure \(\mu\) on \(\Omega\),

$$
\mu P_t\Rightarrow \nu
\qquad\text{as }t\to\infty.
$$

Here \(\Rightarrow\) denotes weak convergence of probability measures on \(\Omega\). The limiting measure \(\nu\) is invariant, and ergodicity implies uniqueness of the invariant measure.

Indeed, if \(\rho\) is invariant, then \(\rho P_t=\rho\) for all \(t\ge0\). By ergodicity, \(\rho P_t\Rightarrow\nu\), hence \(\rho=\nu\).

## Local-function formulation

When \(\mathcal S\) is finite and \(\Lambda\) is countable, the product topology makes \(\Omega\) compact and metrizable. In this setting, \(\mu P_t\Rightarrow\nu\) is equivalent to

$$
\lim_{t\to\infty} \int_\Omega P_t f(\eta)\,\mu(d\eta)
=
\int_\Omega f(\eta)\,\nu(d\eta)
$$

for every continuous function \(f\). Since [local functions](local-functions.md) form a convergence-determining algebra, it is often enough to verify the same limit for every local function \(f\).

For point-mass initial laws, this reads

$$
\lim_{t\to\infty} P_t f(\eta)
=
\int_\Omega f(\xi)\,\nu(d\xi)
$$

for every initial configuration \(\eta\in\Omega\) and every local function \(f\).

## Uniform exponential ergodicity

Uniform exponential ergodicity is a quantitative strengthening of ergodicity. One common local-function formulation is that there are constants \(C<\infty\) and \(\gamma>0\) such that

$$
\sup_{\eta\in\Omega}
\left|P_t f(\eta)-\int_\Omega f(\xi)\,\nu(d\xi)\right|
\le
C e^{-\gamma t}\,\|f\|_*
$$

for all \(t\ge0\) and all functions \(f\) in a specified class, with a specified norm \(\|\cdot\|_*\). The choice of function class and norm is part of the statement. For example, \(\|f\|_*\) might be a weighted local-dependence norm rather than the sup norm.

Uniform exponential ergodicity implies ergodicity. It is not implied by uniqueness of the invariant measure, and it should not be inferred from qualitative ergodicity unless a quantitative estimate is proved.

## Hierarchy

The relevant implication chain is

$$
\text{uniform exponential ergodicity}
\quad\Longrightarrow\quad
\text{ergodicity}
\quad\Longrightarrow\quad
\text{unique invariant measure}.
$$

Neither reverse implication holds in general without additional hypotheses.
