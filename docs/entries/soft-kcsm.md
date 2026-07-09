---
title: Soft KCSM
status: definition
tags:
  - KCSM
  - soft constraints
  - constrained dynamics
---

# Soft KCSM

A soft KCSM is a [KCSM](kinetically-constrained-spin-model.md) in which the hard kinetic constraint is relaxed by allowing updates at a small unconstrained rate.

Let \(c_i\) be the hard constraint induced by an [update family](update-family.md), and let \(arepsilon_i\in[0,1]\). The softened constraint is

$$
c_i^arepsilon(\eta)=arepsilon_i+(1-arepsilon_i)c_i(\eta).
$$

Equivalently, a site that is legal for the hard KCSM still refreshes at rate \(1\), while a site that is illegal for the hard KCSM refreshes at rate \(arepsilon_i\).

With vacancy density \(q\), occupied density \(p=1-q\), and [Bernoulli refresh operator](bernoulli-refresh-operator.md) \(E_i^q\), the soft KCSM generator is

$$
\cL^arepsilon f(\eta)
=
\sum_{i\in\Lambda}c_i^arepsilon(\eta)(E_i^qf(\eta)-f(\eta)).
$$

The hard KCSM is the case \(arepsilon_i=0\) for all \(i\). If \(arepsilon_i=1\), the constraint at site \(i\) is fully removed.

## Flip form

Since Bernoulli refresh KCSM are [spin systems](spin-system.md), the generator can also be written as

$$
\cL^arepsilon f(\eta)
=
\sum_{i\in\Lambda}c_i^arepsilon(\eta)\left(q\eta(i)+p(1-\eta(i))ight)\left(f(\eta^i)-f(\eta)ight).
$$

If the hard constraint \(c_i\) does not depend on \(\eta(i)\), then neither does \(c_i^arepsilon\), and the Bernoulli product measure \(\mu_q\) remains reversible.

## Soft FA-1f

For the [FA-1f model](fa-1f-model.md),

$$
c_i(\eta)=1-\chi_{N(i)}(\eta).
$$

The softened constraint is therefore

$$
c_i^arepsilon(\eta)=1-(1-arepsilon_i)\chi_{N(i)}(\eta).
$$

The same formula gives the soft [East model](east-model.md) when the underlying lattice is oriented. The corresponding finite-set dual coefficients are recorded in [monomial duality for FA-1f](monomial-duality-for-fa-1f.md).
