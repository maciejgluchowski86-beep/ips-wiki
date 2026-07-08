---
title: Ergodicity
status: definition
tags:
  - invariant measure
  - convergence to equilibrium
  - mixing
---

# Ergodicity

Ergodicity is the property that the process forgets its initial distribution and converges to a unique invariant law. For infinite-volume spin systems and interacting particle systems, convergence is usually tested against local functions.

**Related pages.** [Spin system](spin-system.md), [interacting particle system](interacting-particle-system.md), [local functions](local-functions.md).

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*; Levin, Peres, and Wilmer, *Markov Chains and Mixing Times*.

## Definition

Let \((S(t))_{t\ge0}\) be the Markov semigroup of a process on a configuration space \(\Omega\). A probability measure \(\nu\) on \(\Omega\) is invariant if

$$
\nu S(t)=\nu
\qquad\text{for every }t\ge0.
$$

The process is ergodic if there is a probability measure \(\nu\) such that, for every initial probability measure \(\mu\),

$$
\mu S(t)\Rightarrow \nu
\qquad\text{as }t\to\infty.
$$

Here \(\Rightarrow\) denotes weak convergence of probability measures.

## Local-function formulation

For a spin system on \(\{0,1\}^I\) with \(I\) countable, the product topology makes \(\Omega\) compact and metrizable. In this setting the convergence above is equivalent to

$$
\lim_{t\to\infty} \int S(t)f(\eta)\,\mu(d\eta)
=
\int f(\eta)\,\nu(d\eta)
$$

for every continuous function \(f\). Since local functions form a convergence-determining algebra, it is often enough to verify the same limit for every local function \(f\).

## Uniqueness of the invariant measure

Ergodicity implies uniqueness of the invariant measure. Indeed, if \(\rho\) is invariant, then \(\rho S(t)=\rho\) for all \(t\ge0\). By ergodicity, \(\rho S(t)\Rightarrow\nu\), hence \(\rho=\nu\).

## Quantitative variants

Ergodicity is qualitative. Stronger notions include exponential convergence, uniform convergence over initial states, spectral-gap estimates, logarithmic Sobolev estimates, and mixing-time bounds. These require separate hypotheses and should not be inferred from ergodicity alone.
