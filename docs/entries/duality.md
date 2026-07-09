---
title: Duality
status: definition
tags:
  - duality
  - Feynman-Kac
  - Markov process
---

# Duality

Let \((\eta_t)_{t\ge0}\) be a Markov process with generator \(L\), and let \((Y_t)_{t\ge0}\) be another Markov process with generator \(D\). The state \(Y_t\) may include signs or other bookkeeping variables.

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

The second form is the Feynman--Kac duality form. The first form is the special case \(V=0\).
