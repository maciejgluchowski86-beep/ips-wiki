---
title: East model
status: definition
tags:
  - KCSM
  - East model
  - oriented model
---

# East model

The East model is an [oriented](oriented-spin-system.md) [KCSM](kinetically-constrained-spin-model.md). A site may refresh only when at least one specified predecessor is vacant.

**References.** Hartarsky and Toninelli, *Kinetically constrained models*; Cancrini, Martinelli, Schonmann, and Toninelli, *Facilitated oriented spin models: some non equilibrium results*; Marêché, *Exponential convergence to equilibrium for the \(d\)-dimensional East model*.

## Definition on an oriented lattice

Let \(\Lambda\) be an oriented lattice. Write \(j\to i\) when \(j\) may facilitate the update at \(i\), and let \(D(i)\Subset\operatorname{Pred}(i)\) be the chosen East predecessor set at \(i\). The East update family is

$$
\mathcal U_i=\bigl\{\{j\}:j\in D(i)\bigr\}.
$$

Therefore

$$
c_i(\eta)=\ind\{\exists j\in D(i):\eta(j)=0\}
=1-\chi_{D(i)}(\eta).
$$

The one-predecessor East model is the special case \(D(i)=\{j_i\}\), giving

$$
c_i(\eta)=1-\eta(j_i).
$$

## Generator

With vacancy density \(q\), occupied density \(p=1-q\), and [Bernoulli refresh operator](bernoulli-refresh-operator.md) \(E_i^q\), the generator is

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}\bigl(1-\chi_{D(i)}(\eta)\bigr)
\bigl(E_i^q f(\eta)-f(\eta)\bigr).
$$

## One-dimensional East model

On \(\Lambda=\Z\), the right-facilitated East convention has arrows

$$
i+1\to i.
$$

Thus \(D(i)=\{i+1\}\), and

$$
c_i(\eta)=1-\eta(i+1).
$$

The site \(i\) can update exactly when its right neighbour is vacant.

## Higher-dimensional East model

On \(\Z^d\), one standard East-like choice is

$$
D(i)=\{i+e_1,\ldots,i+e_d\},
$$

so that a site can update if at least one forward coordinate neighbour is vacant. This corresponds to the update family with singleton rules in the positive coordinate directions.
