---
method_id: coupling-from-the-past
title: Coupling from the past
category: coupling
targets:
  - convergence
  - mixing
model_scope: Finite ergodic Markov chains admitting a common random-map representation, especially monotone finite spin systems and Glauber/heat-bath dynamics.
source_status: primary-checked
primary_source: James Gary Propp and David Bruce Wilson, "Exact sampling with coupled Markov chains and applications to statistical mechanics," Random Structures & Algorithms 9 (1996), 223-252.
primary_pinpoint: Section 2 (simulation from the past), especially Section 2.2 (monotone Monte Carlo); Section 3.1 (attractive spin systems); Section 4.1 (Ising model).
primary_url: https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O
application_source: James Gary Propp and David Bruce Wilson, same paper.
application_pinpoint: Sections 3.1 and 4.1; ferromagnetic Ising heat-bath dynamics.
application_url: https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O
wiki_candidate: yes
---

# Coupling from the past

## Criterion

Let $P$ be an ergodic Markov kernel on a finite state space $S$, represented by i.i.d. random update maps $F_t:S\to S$ such that $F_t(x)$ has law $P(x,\cdot)$. For $T\ge1$, compose the stored maps from time $-T$ to time $0$,

$$
\Phi_{-T,0}=F_{-1}\circ F_{-2}\circ\cdots\circ F_{-T}.
$$

The Propp--Wilson coupling-from-the-past criterion is: if for the realized past there is a finite $T$ for which $\Phi_{-T,0}$ is constant on $S$, then its common value is an exact sample from the stationary distribution $\pi$. Reusing the same past randomness while increasing $T$ is essential. If the backward coalescence time is finite almost surely, the algorithm terminates almost surely and returns an unbiased stationary sample.

For a monotone chain on a partially ordered state space with least and greatest states $\hat0,\hat1$, Section 2.2 gives the crucial reduction

$$
\Phi_{-T,0}(\hat0)=\Phi_{-T,0}(\hat1)
\quad\Longrightarrow\quad
\Phi_{-T,0}(x)\text{ is the same for every }x\in S.
$$

Thus one need only evolve the two extremal histories rather than all starting states.

## Mechanism

The argument reverses the usual role of coupling. A forward coupling started at a fixed time can show that initialization has probably been forgotten, but stopping when two selected trajectories meet generally leaves residual initialization bias. CFTP instead fixes the observation time $0$ and moves the starting time farther into the past while preserving all previously generated update maps. Once every possible state at time $-T$ is mapped to the same state at time $0$, the output is independent of the unknown state in the remote past.

To see exact stationarity, imagine an actual stationary chain running through the same random maps. Its state at time $-T$ is some element of $S$, hence on the coalescence event its time-zero state must equal the common image. Since the stationary chain's time-zero marginal is $\pi$, the common image has law $\pi$ as well. The stopping rule is valid because it is formulated entirely from the stored past maps.

## Representative IPS use

Propp--Wilson Section 3.1 considers finite attractive spin systems with single-site heat-bath updates. The natural coordinatewise order is preserved by using the same update site and uniform random variable in every configuration. Section 4.1 applies this to a ferromagnetic Ising model: the all-minus and all-plus configurations are the extremal states, and coalescence of their backward heat-bath histories certifies an exact Ising Gibbs sample.

This is stronger than merely bounding the mixing time of the heat-bath chain: the returned sample has exactly the equilibrium law, not a law within a prescribed total-variation error.

## Limitations

CFTP requires a usable common random-map representation and an almost surely finite backward coalescence time. The generic construction may require tracking all states, which is computationally prohibitive. Monotonicity makes the method practical by reducing this to extremal trajectories, but non-attractive spin systems lose that simplification.

Exact sampling and forward dynamical convergence should not be conflated. A finite CFTP coalescence time proves that the random maps have forgotten every finite-state initial condition for that realization and gives perfect sampling; a separate quantitative analysis is needed to turn its tail into a useful mixing-time estimate. Conversely, ordinary forward mixing does not by itself give an implementable CFTP stopping certificate.

The method is also distinct from clan-of-ancestors perfect simulation: CFTP detects coalescence of a grand random map over initial states, whereas ancestor-clan methods prove that a finite backward dependency graph suffices to reconstruct the target without such a grand coupling.

## Sources

- Propp and Wilson, *Random Structures & Algorithms* 9 (1996), Section 2 and especially Section 2.2; attractive spin systems in Section 3.1 and Ising application in Section 4.1. DOI: https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O.
