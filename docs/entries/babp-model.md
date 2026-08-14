---
title: Biased annihilating branching process
status: definition
audit: current
tags:
  - KCSM
  - BABP
  - branching process
---

# Biased annihilating branching process

The biased annihilating branching process, abbreviated BABP, is a Bernoulli-refresh [spin system](spin-system.md) in which the update rate at a site equals the number of vacant neighbours. It is the additive-rate analogue of the [FA-1f model](fa-1f-model.md): the two models permit updates in exactly the same configurations, but BABP counts the facilitating neighbours instead of replacing their number by an indicator.

**References.** Neuhauser and Sudbury, *The biased annihilating branching process*; Hartarsky and Toninelli, *Kinetically constrained models*; Martinelli, Shapira, and Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*.

## Definition on a lattice

Let \(\Lambda\) be a [lattice](lattice-and-graph.md) with finite neighbour sets \(N(i)\). In the KCSM convention, \(0\) is the facilitating state, \(q\) is its equilibrium density, and \(p=1-q\). Define the update rate

$$
c_i(\eta)
=
\sum_{j\in N(i)}(1-\eta(j)).
$$

Thus \(c_i(\eta)\) is the number of vacant neighbours of \(i\). With the [Bernoulli refresh operator](bernoulli-refresh-operator.md) \(E_i^q\), the generator is

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}
c_i(\eta)\bigl(E_i^qf(\eta)-f(\eta)\bigr).
\tag{1}
$$

Equivalently, (1) has the flip form

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}
c_i(\eta)
\bigl(q\eta(i)+p(1-\eta(i))\bigr)
\bigl(f(\eta^i)-f(\eta)\bigr).
\tag{2}
$$

## Relation to FA-1f

The FA-1f constraint is

$$
\ind\{c_i(\eta)>0\}.
$$

Consequently, BABP and FA-1f have the same legal updates and the same blocked configurations. If \(i\) has exactly \(k\) vacant neighbours, however, BABP refreshes \(i\) at rate \(k\), whereas FA-1f refreshes it at rate \(1\).

On \(\Z^d\) with nearest-neighbour sets,

$$
c_i(\eta)
=
\sum_{k=1}^d
\left(
2-\eta(i-e_k)-\eta(i+e_k)
\right).
$$

This nearest-neighbour process is the standard BABP in the KCSM convention.

## Particle convention

The name of the process comes from the complementary variables

$$
\xi(i)=1-\eta(i),
$$

where \(\xi(i)=1\) means that a particle is present. In these variables, (2) becomes

$$
\cL f(\xi)
=
\sum_{i\in\Lambda}
\left(\sum_{j\in N(i)}\xi(j)\right)
\bigl(q(1-\xi(i))+p\xi(i)\bigr)
\bigl(f(\xi^i)-f(\xi)\bigr).
$$

Assume \(p>0\). Multiplying the generator by \(p^{-1}\) and writing

$$
\lambda=\frac qp,
$$

the generator is

$$
p^{-1}\cL f(\xi)
=
\sum_{i\in\Lambda}
\left(\sum_{j\in N(i)}\xi(j)\right)
\bigl(\lambda(1-\xi(i))+\xi(i)\bigr)
\bigl(f(\xi^i)-f(\xi)\bigr).
\tag{3}
$$

Formula (3) explains both parts of the name. A particle is born at an empty site at rate \(\lambda\) for each neighbouring particle, while a particle is removed at rate \(1\) for each neighbouring particle. The equilibrium particle density is

$$
q=\frac{\lambda}{1+\lambda},
\qquad
p=\frac1{1+\lambda}.
$$

## Reversibility and absorbing state

The update rate \(c_i\) does not depend on \(\eta(i)\), and the refresh law is the one-site marginal of \(\mu_q\). Hence \(\mu_q\) is reversible. The all-one configuration is absorbing because every update rate vanishes there. BABP is not attractive in the usual product order.

Known convergence results are recorded under [BABP out of equilibrium](babp-out-of-equilibrium.md).
