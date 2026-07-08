---
title: Ergodicity
status: definition
tags:
  - invariant measure
  - convergence to equilibrium
  - mixing
---

# Ergodicity

This entry fixes the wiki convention for ergodicity of a spin system. The convention is convergence to a unique limiting invariant law, not merely extremality of an invariant measure or measure-preserving ergodicity of a shift action.

**Status.** Definition and convention.

**Links.** Depends on [spin system](spin-system.md).

**Main references.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*; Levin, Peres, and Wilmer, *Markov Chains and Mixing Times*.

Let \((S(t))_{t\ge0}\) be the Markov semigroup of a [spin system](spin-system.md) on \(\Omega=E^\Lambda\). If \(\mu\) is a probability measure on \(\Omega\), then \(\mu S(t)\) denotes the law at time \(t\) started from \(\mu\).

!!! definition "Ergodicity"
    A spin system is ergodic if there is a probability measure \(\nu\) on \(\Omega\) such that, for every initial probability measure \(\mu\) on \(\Omega\),
    \[
        \mu S(t) \Rightarrow \nu
        \qquad\text{as }t\to\infty,
    \]
    where \(\Rightarrow\) denotes weak convergence of probability measures on \(\Omega\).

In particular, \(\nu\) is invariant. Indeed, if \(s\ge0\), then
\[
    \nu S(s)
    =\lim_{t\to\infty} \mu S(t+s)
    =\nu,
\]
whenever the semigroup is continuous enough to pass the limit through the fixed-time map. This is the usual situation for Feller spin systems on compact product spaces.

!!! remark "Uniqueness"
    The definition implies uniqueness of the invariant measure. If \(\rho\) is invariant, then \(\rho S(t)=\rho\) for all \(t\), while ergodicity gives \(\rho S(t)\Rightarrow\nu\). Hence \(\rho=\nu\).

!!! remark "Finite versus infinite state space"
    For a finite irreducible continuous-time Markov chain, ergodicity is equivalent to convergence to the unique stationary distribution. Infinite spin systems require more care: convergence may be weak convergence against local functions, and uniqueness of an invariant measure alone need not be the most convenient formulation in a proof.

!!! convention "Wiki convention"
    When an entry says that a spin system is ergodic without further qualification, it means the convergence above. Stronger statements, such as exponential ergodicity, uniform convergence over initial states, spectral gap bounds, or quantitative mixing, must be stated separately.

!!! remark "Relation to the Positive Rates Conjecture"
    For the Positive Rates Conjecture program, the target conclusion is ergodicity in the above convergence-to-equilibrium sense for one-dimensional positive-rate spin systems. Project-specific routes should state whether they prove this conclusion directly, prove a stronger quantitative version, or only establish a conditional reduction.
