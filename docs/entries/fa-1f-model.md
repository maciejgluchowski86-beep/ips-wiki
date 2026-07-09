---
title: FA-1f model
status: definition
tags:
  - KCSM
  - FA-1f
  - noncooperative model
---

# FA-1f model

The Fredrickson-Andersen one-spin facilitated model, abbreviated FA-1f, is the [KCSM](kinetically-constrained-spin-model.md) in which a site may refresh when at least one neighbour is vacant. It is the basic nonoriented analogue of the [East model](east-model.md).

**References.** Hartarsky and Toninelli, *Kinetically constrained models*; Blondel, Cancrini, Martinelli, Roberto, and Toninelli, *Fredrickson-Andersen one spin facilitated model out of equilibrium*.

## Definition on a lattice

Let \(\Lambda\) be a [lattice](lattice-and-graph.md) with finite neighbour sets \(N(i)\). The FA-1f [update family](update-family.md) at \(i\) is

$$
\mathcal U_i=\bigl\{\{j\}:j\in N(i)\bigr\}.
$$

Thus the constraint is satisfied exactly when some neighbour of \(i\) is in the facilitating state \(0\):

$$
c_i(\eta)=\ind\{\exists j\in N(i):\eta(j)=0\}.
$$

Using the [monomials](monomials.md)

$$
\chi_A(\eta)=\prod_{j\in A}\eta(j),
$$

the same constraint is

$$
c_i(\eta)=1-\chi_{N(i)}(\eta).
$$

Here \(\chi_{N(i)}=1\) means that all neighbours of \(i\) are occupied, so no facilitating vacancy is present.

## Generator

With vacancy density \(q\), occupied density \(p=1-q\), and [Bernoulli refresh operator](bernoulli-refresh-operator.md) \(E_i^q\), the generator is

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}\bigl(1-\chi_{N(i)}(\eta)\bigr)
\bigl(E_i^q f(\eta)-f(\eta)\bigr).
$$

A refresh occurs only at a [legal update](legal-update.md), meaning a clock ring whose site has at least one vacant neighbour. The corresponding finite-set dual is recorded in [monomial duality for FA-1f](monomial-duality-for-fa-1f.md).

## Nearest-neighbour FA-1f on \(\Z^d\)

On \(\Lambda=\Z^d\) with nearest-neighbour graph,

$$
N(i)=\{i\pm e_k:1\le k\le d\}.
$$

Then a site updates if at least one nearest neighbour is vacant. This is the standard FA-1f model.

## Noncooperative character

FA-1f is noncooperative: a single vacancy can facilitate the motion and creation of further vacancies through legal updates. This distinguishes it from cooperative models such as FA-2f, where larger local vacancy patterns are required. Known convergence results are recorded in [FA-1f out of equilibrium](fa-1f-out-of-equilibrium.md).
