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

A function

$$
H(y,\eta)
$$

is a duality function if

$$
L_\eta H(y,\eta)=D_yH(y,\eta).
$$

Then

$$
\E_\eta[H(y,\eta_t)]
=
\E_y[H(Y_t,\eta)].
$$

More generally, if

$$
L_\eta H(y,\eta)=D_yH(y,\eta)+V(y)H(y,\eta),
$$

then

$$
\E_\eta[H(y,\eta_t)]
=
\E_y\left[
\exp\left(\int_0^t V(Y_s)\,ds\right)H(Y_t,\eta)
\right].
$$

The second form is the Feynman--Kac duality form. The first form is the special case \(V=0\). The [monomial duality for spin systems](monomial-duality-for-spin-systems.md) is a concrete finite-set example, and the [duality noise lemma](duality-noise-lemma.md) records a basic perturbation rule for comparison arguments.
