---
title: Regeneration at a recurrent particle-collapse atom
status: literature
audit: current
tags:
  - regeneration
  - particle systems
  - recurrence
---

# Regeneration at a recurrent particle-collapse atom

## Criterion

A regenerative proof becomes available when an interacting Markov process repeatedly reaches a state, or a set of states with identical post-hit law, from which its future starts afresh. If regeneration times
\[
0<\tau_1<\tau_2<\cdots
\]
have independent identically distributed cycles after the first and finite mean cycle length, renewal theory gives positive recurrence and a unique stationary cycle law.

Baryshnikov--Stolyar exhibit this mechanism directly. Their system has \(n\) particles on \(\mathbb R\): particles make independent forward jumps and synchronization jumps that move a particle to the location of a randomly chosen particle lying ahead. Global translation prevents the raw configuration from being positive recurrent, so they center the empirical distribution at a fixed quantile. In the centered state space, whenever all particles occupy one location the state is the same deterministic collapsed configuration. Section 3 shows that for every fixed \(\varepsilon>0\), there is
\[
\delta(\varepsilon,n)>0
\]
such that, from every current configuration, all particles are at one location at the end of the next interval of length \(\varepsilon\) with probability at least \(\delta\). Hence the first collapse time has finite mean. Collapse times are regeneration times, so the centered process is positive recurrent with a unique stationary distribution.

## Mechanism

The key step is identifying an atom created by the interaction itself. Synchronization can successively absorb lagging particles into a common location. Once all particles coincide, centering removes the common spatial coordinate and erases all information about the pre-collapse shape. The strong Markov property then makes successive excursions from the collapsed state genuine renewal cycles.

The uniform lower bound \(\delta(\varepsilon,n)\) rules out cycles with infinite mean. Regenerative formulas can then express stationary statistics as expected rewards accumulated during a typical cycle divided by its expected length. The source also uses the regeneration structure to justify almost-sure long-time speed limits independently of the initial state.

## Representative IPS use

The application is the synchronization particle system itself. After centering, repeated collapse events yield the unique stationary shape distribution used to define the steady-state advance speed. This gives an example where ergodic structure is obtained neither from a spectral inequality nor from a coupling contraction, but from an exact renewal state produced by collective interaction.

## Limitations

The atom is highly model-specific. For a generic infinite IPS the probability that all coordinates simultaneously enter one configuration is zero. Even for finite particle systems, a useful regeneration event must have a return time with finite mean. Here \(n\) is fixed and the lower bound \(\delta(\varepsilon,n)\) may deteriorate badly with \(n\), so this argument alone gives no uniform-in-\(n\) mixing rate.

This differs from [Foster--Lyapunov plus Harris recurrence](foster-lyapunov-harris-geometric-ergodicity.md): Harris theory uses drift and small-set minorization without requiring exact regeneration. It is also not Nummelin splitting, since no auxiliary randomization is introduced to manufacture an atom.

## Sources

- Baryshnikov, Stolyar, *A large-scale particle system with independent jumps and distributed synchronization*, Section 3, centered-process regeneration and finite-mean cycle argument, https://doi.org/10.1017/apr.2024.53.
- Open preprint: https://arxiv.org/abs/2311.17052.
