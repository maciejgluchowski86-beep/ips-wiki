---
title: Invariant measure
status: standard fact
tags:
  - invariant measure
  - Markov semigroup
  - Cesaro averages
  - Krylov-Bogoliubov
---

# Invariant measure

An invariant measure for an [interacting particle system](interacting-particle-system.md) is a probability measure unchanged by the evolution. On a compact configuration space, every nonempty weakly closed convex class of probability measures preserved by the IPS semigroup contains an invariant measure.

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*; Krylov and Bogoliubov, *La théorie générale de la mesure dans son application à l'étude des systèmes dynamiques de la mécanique non linéaire*.

## Definition

Let ((P_t)_{t\ge0}) be the Markov semigroup of an interacting particle system on a configuration space (Omega). A probability measure (
u) on (Omega) is invariant if

$$

u P_t=
u
qquad	ext{for every }tge0.
$$

Equivalently,

$$
int_Omega P_t f(eta),
u(deta)
=
int_Omega f(eta),
u(deta)
$$

for every bounded continuous function (f) and every (tge0).

## Existence in a preserved class

Suppose that (Omega) is a compact metrizable space and that ((P_t)_{tge0}) is a Feller semigroup on (Omega). Let (mathcal M) be a nonempty weakly closed convex subset of the space (mathcal P(Omega)) of probability measures on (Omega). Assume that (mathcal M) is preserved by the IPS evolution:

$$
mu P_tinmathcal M
qquad
	ext{for every }muinmathcal M
	ext{ and }tge0.
$$

Then (mathcal M) contains an invariant probability measure.

This is the continuous-time Krylov--Bogoliubov existence theorem.

## Proof

Fix (muinmathcal M). For (T>0), define the Cesàro mean

$$
mu_T=rac1Tint_0^Tmu P_s,ds.
$$

Since (mathcal M) is convex, weakly closed, and preserved by (P_s), each (mu_T) belongs to (mathcal M). Compactness of (Omega) implies compactness of (mathcal P(Omega)) in the weak topology. Hence there are (T_n	oinfty) and (
uinmathcal M) such that

$$
mu_{T_n}Rightarrow
u.
$$

For fixed (tge0) and every bounded continuous function (f), the semigroup property gives

$$
egin{aligned}
int_Omega f,d(mu_TP_t)-int_Omega f,dmu_T
&=
rac1Tleft(
int_T^{T+t}int_Omega f,d(mu P_s),ds
-
int_0^tint_Omega f,d(mu P_s),ds
ight).
end{aligned}
$$

Therefore

$$
left|
int_Omega f,d(mu_TP_t)-int_Omega f,dmu_T
ight|
le
rac{2t}{T}|f|_infty.
$$

The right-hand side tends to zero. Since the Feller property makes (P_tf) continuous, weak convergence along (T_n) yields

$$
int_Omega f,d(
u P_t)=int_Omega f,d
u.
$$

Thus (
u P_t=
u). Since (tge0) was arbitrary, (
u) is invariant.

## Application to interacting particle systems

If the single-site state space (mathcal S) is finite and the [lattice](lattice-and-graph.md) (Lambda) is countable, then

$$
Omega=mathcal S^Lambda
$$

is compact and metrizable in the product topology. Taking (mathcal M=mathcal P(Omega)) shows that every Feller IPS on (Omega) has at least one invariant probability measure.

More restrictive choices of (mathcal M) produce invariant measures with additional properties. For example, if a translation-invariant IPS preserves the nonempty weakly closed convex class of translation-invariant probability measures, then that class contains an invariant measure.

## Relation to ergodicity

Existence of an invariant measure is weaker than uniqueness or [ergodicity](ergodicity.md). The Cesàro construction produces at least one invariant measure but generally gives neither uniqueness nor convergence of (mu P_t) without averaging.
