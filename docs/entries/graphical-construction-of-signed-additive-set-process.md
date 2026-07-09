---
title: Graphical construction of signed additive set process
status: definition
tags:
  - signed additive set process
  - graphical construction
  - Poisson construction
  - IPS
---

# Graphical construction of signed additive set process

A graphical construction realizes a [signed additive set process](signed-additive-set-process.md) from independent Poisson marks in spacetime. The marks, together with the initial finite set and initial sign, determine the whole trajectory. This is the concrete pathwise version of the process used in [monomial duality for spin systems](monomial-duality-for-spin-systems.md).

**References.** None yet.

## Setup

Let \(\Lambda\) be a countable [lattice](lattice-and-graph.md). A state of the signed additive set process is

$$
Y=(A,\sigma),
$$

where \(A\Subset\Lambda\) is a finite active set and \(\sigma\in\{+,-\}\) is a sign.

For each active source site \(i\), the process has two kinds of local updates indexed by finite sets \(S\Subset N(i)\):

- a source-killing update \(D_{i,S}\), which removes \(i\) and adds \(S\);
- a source-keeping update \(B_{i,S}\), which keeps \(i\) and adds \(S\).

Explicitly,

$$
D_{i,S}(A,\sigma)
=
((A\setminus\{i\})\cup S,\sigma\sigma_i^\delta(S)),
$$

and

$$
B_{i,S}(A,\sigma)
=
(A\cup S,\sigma\sigma_i^\beta(S)).
$$

Here \(\sigma_i^\delta(S),\sigma_i^\beta(S)\in\{+,-\}\) are the signs attached to the corresponding update. Multiplication of signs uses the usual convention \(+\sigma=\sigma\) and \(-\sigma\) flips the sign.

The source-keeping update with \(S=n\) is usually omitted in monomial duality and absorbed into the Feynman--Kac potential. Thus \(B_{i,n}\) is not included unless the specific process explicitly declares it.

## Poisson marks

For every ordered update label \((i,S,\delta)\), place an independent Poisson process on \([0,\infty)\) of rate

$$
\delta_i(S)\ge0.
$$

For every ordered update label \((i,S,eta)\) with \(S
en\), place an independent Poisson process on \([0,\infty)\) of rate

$$
eta_i(S)\ge0.
$$

Equivalently, a mark is a spacetime point \((i,t)\) together with its type and target set:

$$
(i,t;\delta,S)
\qquad\text{or}\qquad
(i,t;eta,S).
$$

The mark is attached to the source site \(i\). The set \(S\) records the sites activated by the mark.

## Evolution rule

Fix an initial condition \(Y_0=(A_0,\sigma_0)\). Read all Poisson marks in increasing time order. At a mark with source \(i\):

- if \(i
otin A_{t-}\), the mark is ignored;
- if \(i\in A_{t-}\) and the mark is \((i,t;\delta,S)\), set

$$
Y_t=D_{i,S}Y_{t-};
$$

- if \(i\in A_{t-}\) and the mark is \((i,t;eta,S)\), set

$$
Y_t=B_{i,S}Y_{t-}.
$$

Between marks the state is constant. Since each \(S\) is finite and only finitely many active-source marks are relevant over bounded time intervals under the usual finite-range and locally finite rate assumptions, this gives a càdlàg pure-jump path on finite active sets.

## Generator

The graphical construction has generator

$$
\begin{aligned}
\cD F(A,\sigma)
={}&
\sum_{i\in A}\sum_{S\Subset N(i)}
\delta_i(S)
\bigl(F(D_{i,S}(A,\sigma))-F(A,\sigma)\bigr)\\
&+
\sum_{i\in A}\sum_{\substack{S\Subset N(i)\\ S
en}}
\beta_i(S)
\bigl(F(B_{i,S}(A,\sigma))-F(A,\sigma)\bigr).
\end{aligned}
$$

Thus the graphical construction is a pathwise construction of the same [interacting particle system](interacting-particle-system.md) on the countable state space of finite signed subsets.

## Relation to monomial duality

For a [spin system](spin-system.md), the coefficients in [monomial duality for spin systems](monomial-duality-for-spin-systems.md) determine the rates \(\delta_i(S)\), \(eta_i(S)\), and signs \(\sigma_i^\delta(S)\), \(\sigma_i^\beta(S)\). The graphical construction then gives the dual process appearing in the Feynman--Kac representation.

This entry only records the underlying Poisson construction. Successful interactions, revealed skeletons, and patch decompositions are additional structures imposed on a realized graphical construction.