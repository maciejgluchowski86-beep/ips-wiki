---
title: Spin system
status: definition
tags:
  - spin systems
  - flip rates
  - two-state systems
---

# Spin system

A spin system is a continuous-time interacting particle system with two possible states at each site. The state space is usually written as \(\{0,1\}^I\), or equivalently as \(\{-1,+1\}^I\). The defining feature is that updates are single-site flips.

**Related pages.** [Lattice and graph](lattice-and-graph.md), [local functions](local-functions.md), [interacting particle system](interacting-particle-system.md), [ergodicity](ergodicity.md).

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*.

## Definition

Let \(I\) be a countable site set. A configuration is an element

$$
\eta\in \Omega=\{0,1\}^I.
$$

For \(i\in I\), let \(\eta^i\) be the configuration obtained from \(\eta\) by flipping the value at \(i\):

$$
\eta^i(j)=
\begin{cases}
1-\eta(i), & j=i,\\
\eta(j), & j\ne i.
\end{cases}
$$

A spin system is a continuous-time Markov process on \(\Omega\) whose generator acts on local functions by

$$
\cL f(\eta)
=
\sum_{i\in I} c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr),
$$

where \(c_i(\eta)\ge0\) is the flip rate at site \(i\) in configuration \(\eta\).

## Locality

The flip rate \(c_i\) is usually assumed to be local: there is a finite neighbourhood \(N_*(i)\subset I\), often containing \(i\), such that \(c_i(\eta)\) depends only on \(\eta|_{N_*(i)}\). On a translation-invariant lattice one often writes \(N_*(i)=i+N_*\) for a fixed finite neighbourhood shape \(N_*\subset\Z^d\).

## Positive rates

For a finite-range spin system, positive rates means that every local flip rate allowed by the model is strictly positive for every local neighbourhood configuration. In the translation-invariant two-state case this is often stated as

$$
\inf_i \inf_\eta c_i(\eta)>0,
$$

or, when the rates are translation-invariant and depend on finitely many coordinates, as positivity of the finite list of local rates.

## Relation to general IPS

A spin system is a special case of an interacting particle system. If the single-site space has more than two states, or if updates are not single-site flips, the object is better called an interacting particle system rather than a spin system.
