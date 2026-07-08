---
title: Interacting particle system
status: definition
tags:
  - interacting particle systems
  - Markov generators
  - local updates
---

# Interacting particle system

An interacting particle system is a continuous-time Markov process on a product configuration space over a countable [site set](lattice-and-graph.md). Unlike a [spin system](spin-system.md), the single-site state space need not be two-state and the allowed updates need not be single-site flips.

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*.

## Configuration space

Let \(I\) be a countable site set and let \(E\) be a finite or countable single-site state space. The configuration space is

$$
\Omega=E^I.
$$

A configuration \(\eta\in\Omega\) assigns a state \(\eta(i)\in E\) to each site \(i\in I\).

## Single-site update form

A common finite-state form has rates \(c_i^a(\eta)\ge0\) for replacing the state at site \(i\) by \(a\in E\). Let \(\eta^{i,a}\) be defined by

$$
\eta^{i,a}(j)=
\begin{cases}
a, & j=i,\\
\eta(j), & j\ne i.
\end{cases}
$$

Then the generator acts on [local functions](local-functions.md) by

$$
\cL f(\eta)
=
\sum_{i\in I}\sum_{a\in E} c_i^a(\eta)\bigl(f(\eta^{i,a})-f(\eta)\bigr),
$$

with the convention that terms with \(a=\eta(i)\) may be omitted or assigned rate zero.

## General local update form

More generally, an IPS may use local maps \(\theta:\Omega\to\Omega\), each changing only finitely many coordinates. A formal generator then has the form

$$
\cL f(\eta)
=
\sum_{\theta} r_\theta(\eta)\bigl(f(\theta\eta)-f(\eta)\bigr),
$$

where each rate \(r_\theta\) is local and nonnegative, and the family of maps is locally finite enough for \(\cL f\) to be well-defined on local functions.

## Ergodicity

The long-time behaviour of an IPS is often formulated in terms of invariant measures and [ergodicity](ergodicity.md). In infinite volume, convergence to equilibrium is typically checked against local functions.

## Relation to spin systems

A spin system is the special case \(E=\{0,1\}\) with only the flip update \(\eta\mapsto\eta^i\) at each site. Thus every spin system is an interacting particle system, but not every interacting particle system is a spin system.
