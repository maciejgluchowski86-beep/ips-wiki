---
title: Kinetically constrained spin model
status: definition
tags:
  - KCSM
  - constrained dynamics
  - Bernoulli refresh
---

# Kinetically constrained spin model

A kinetically constrained spin model is a [spin system](spin-system.md) whose single-site refreshes are allowed only when a local vacancy constraint is satisfied. The invariant reference measure is a Bernoulli product measure, but the kinetic constraints can create slow relaxation, blocked configurations, and non-attractive dynamics.

**References.** Hartarsky and Toninelli, *Kinetically constrained models*; Cancrini, Martinelli, Roberto, and Toninelli, *Kinetically constrained spin models*.

## Convention

The configuration space is

$$
\Omega=\{0,1\}^\Lambda.
$$

The KCSM convention in this wiki is that \(0\) is the facilitating or vacant state. The parameter \(q\) is the density of zeros, and

$$
p=1-q
$$

is the density of ones. The corresponding Bernoulli product measure is \(\mu_q\).

## Generator

Let \(\mathcal U_i\) be an [update family](update-family.md) at each site \(i\in\Lambda\), and let \(c_i\) be the induced constraint. The KCSM generator is

$$
\cL f(\eta)
=
\sum_{i\in\Lambda} c_i(\eta)\bigl(E_i^q f(\eta)-f(\eta)\bigr),
$$

where \(E_i^q\) is the [Bernoulli refresh operator](bernoulli-refresh-operator.md):

$$
E_i^q f(\eta)=q f(\eta^{i,0})+p f(\eta^{i,1}).
$$

A clock ring at site \(i\) is legal if \(c_i(\eta)=1\). At a legal ring, the spin at \(i\) is refreshed from Bernoulli\((p)\) on \(\{0,1\}\), equivalently from \(q\delta_0+p\delta_1\).

## Constraint does not use the updated spin

In the standard KCSM setup, \(c_i\) depends on neighbours of \(i\), not on \(\eta(i)\) itself. In the notation of [lattice and graph](lattice-and-graph.md), the constraint uses subsets of \(N(i)\), while the refreshed site is \(i\).

## Relation to spin systems

The refresh form is equivalent to a flip generator with constrained state-dependent flip rates:

$$
\cL f(\eta)
=
\sum_{i\in\Lambda} c_i(\eta)igl(q\eta(i)+p(1-\eta(i))\bigr)igl(f(\eta^i)-f(\eta)\bigr).
$$

Thus every KCSM is a spin system, but its flip rates are degenerate whenever the constraint is not satisfied.

## Reversibility

Because legal updates refresh from the one-site marginal of \(\mu_q\), and because \(c_i\) does not depend on \(\eta(i)\), the measure \(\mu_q\) is reversible for the KCSM dynamics. Reversibility does not by itself imply [ergodicity](ergodicity.md), since constraints may create blocked classes or several invariant measures.
