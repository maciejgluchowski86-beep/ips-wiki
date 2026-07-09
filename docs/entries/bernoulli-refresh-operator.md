---
title: Bernoulli refresh operator
status: definition
tags:
  - Bernoulli product measure
  - refresh dynamics
  - KCSM
---

# Bernoulli refresh operator

The Bernoulli refresh operator replaces the spin at one lattice site by an independent Bernoulli variable. It is the basic local update in [kinetically constrained spin models](kinetically-constrained-spin-model.md).

## Bernoulli product measure

Let \(\Lambda\) be a countable [lattice](lattice-and-graph.md) and let

$$
\Omega=\{0,1\}^\Lambda.
$$

In the KCSM convention, \(0\) is the facilitating or vacant state. Write

$$
q=\mu_q(\eta(i)=0),
\qquad
p=1-q=\mu_q(\eta(i)=1).
$$

The Bernoulli product measure with vacancy density \(q\) is

$$
\mu_q=\bigotimes_{i\in\Lambda}\bigl(q\delta_0+p\delta_1\bigr).
$$

## Refresh operator

For a function \(f:\Omega\to\R\), define

$$
E_i^q f(\eta)
=
q f(\eta^{i,0})+p f(\eta^{i,1}),
$$

where \(\eta^{i,a}\) is the configuration obtained from \(\eta\) by setting site \(i\) to \(a\). Equivalently,

$$
E_i^q f(\eta)=\int f(\xi)\,\mu_q(d\xi(i)\mid \xi(j)=\eta(j)\text{ for }j\ne i).
$$

Thus \(E_i^q\) averages over the spin at \(i\) and leaves all other spins fixed.

## Relation to flips

On \(\{0,1\}^\Lambda\), the refresh generator \(E_i^q-I\) can be written as a flip generator with state-dependent flip rate. If \(\eta(i)=1\), the spin changes to \(0\) with probability \(q\). If \(\eta(i)=0\), the spin changes to \(1\) with probability \(p\). Hence

$$
(E_i^q-I)f(\eta)
=
\bigl(q\eta(i)+p(1-\eta(i))\bigr)igl(f(\eta^i)-f(\eta)\bigr).
$$

This identity explains why Bernoulli-refresh KCSM are special cases of [spin systems](spin-system.md).
