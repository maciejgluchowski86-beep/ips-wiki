---
title: Duality
status: definition
tags:
  - duality
  - Feynman-Kac
  - Markov process
---

# Duality

Let \((\eta_t)_{t\ge0}\) be a Markov process with generator \(L\), and let \((Y_t)_{t\ge0}\) be another Markov process with generator \(D\). In [interacting particle system](interacting-particle-system.md) applications, \(\eta_t\) is usually the physical process and \(Y_t\) is an auxiliary process chosen to make selected observables tractable. The state \(Y_t\) may include signs or other bookkeeping variables, as in a [signed additive set process](signed-additive-set-process.md).

A duality function is a function \(H(y,\eta)\) satisfying the generator identity

$$
L_\eta H(y,\eta)=D_yH(y,\eta).
$$

The generator identity gives the semigroup identity

$$
\E_\eta[H(y,\eta_t)]
=
\E_y[H(Y_t,\eta)].
$$

The Feynman--Kac version replaces the generator identity by

$$
L_\eta H(y,\eta)=D_yH(y,\eta)+V(y)H(y,\eta).
$$

The corresponding semigroup identity is

$$
\E_\eta[H(y,\eta_t)]
=
\E_y\left[
\exp\left(\int_0^t V(Y_s)\,ds\right)H(Y_t,\eta)
\right].
$$

The ordinary duality relation is the special case \(V=0\). The [monomial duality for spin systems](monomial-duality-for-spin-systems.md) is a concrete finite-set example, its patchwise form is recorded in the [patch representation of spin systems](patch-representation-of-spin-systems.md), and [undoing duality under confined late interactions](undoing-duality-under-confined-late-interactions.md) identifies a skeleton-restricted dual expectation with a modified spin-system semigroup. The [duality noise lemma](duality-noise-lemma.md) records a basic perturbation rule for comparison arguments.