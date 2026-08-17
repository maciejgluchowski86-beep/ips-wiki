---
title: Asymptotic coupling for infinite-dimensional stochastic dynamics
status: literature
audit: current
tags:
  - coupling
  - SPDE
  - mixing
---

# Asymptotic coupling for infinite-dimensional stochastic dynamics

## Criterion

Ordinary successful coupling asks two copies of a Markov process to become exactly equal after a finite random time. Hairer's **asymptotic coupling** replaces this by a weaker but useful event: after a binding attempt, the two coupled trajectories may remain distinct forever, but their distance decays exponentially while the modified noise used to produce that approach has a law absolutely continuous with respect to the original noise.

In the abstract random-dynamical-system setting of Sections 2--3, the coupling is combined with a Lyapunov function that repeatedly returns pairs of trajectories to a region where a binding attempt has uniformly positive success probability. Assumptions A1--A5 quantify the Lyapunov recurrence, the probability and cost of failed binding attempts, and exponential contraction after a successful binding. Theorem 4.1 then yields constants $C,\gamma>0$ such that

\[
\|P_x^n-P_y^n\|_{L}
   \le C\bigl(1+\widetilde V(x,y)\bigr)e^{-\gamma n},
\]

where $\|\cdot\|_L$ is the dual norm to bounded Lipschitz observables. Corollary 4.3 gives a unique invariant probability measure and exponential convergence to it in this Lipschitz/Wasserstein-type distance.

## Mechanism

The useful freedom is that the second copy is not required to use exactly the same future noise. During a binding attempt one perturbs the driving noise by a feedback chosen to damp the difference in the dynamically determining directions. Girsanov-type control bounds the discrepancy between the perturbed-noise law and the true-noise law. If the attempt succeeds, the two states approach one another exponentially even though they need never coincide.

A failed attempt is not fatal. The coupling is returned to an ordinary evolution until a Lyapunov-controlled region is reached again, after which another binding attempt begins. Theorem 4.1 turns exponential tails for this restart structure, plus the asymptotic contraction on successful attempts, into exponential decay of the bounded-Lipschitz distance between transition laws.

This bypasses a basic obstruction in infinite-dimensional systems: transition probabilities from different initial states can be mutually singular at every finite time, so a total-variation successful coupling may be impossible. Exact coalescence is replaced by convergence in a topology compatible with the dynamics.

## Representative IPS use

Section 5 applies the method to stochastic differential equations on a separable Hilbert space,

\[
dX=(AX+F(X))\,dt+Q\,dW,
\]

including possibly infinite-dimensional equations. The feedback acts through the noise on determining directions and dissipativity controls the remaining modes. Section 6 gives parabolic SPDE examples, including degenerate-noise cases where not every determining mode is forced directly. The conclusion is uniqueness of the invariant law and exponential convergence in the Lipschitz/Wasserstein metric.

Although these are SPDE rather than lattice spin systems, they are interacting infinite-dimensional Markov systems and expose a coupling interface absent from finite Hamming-space methods: approximate synchronization under an absolutely continuous change of noise.

## Limitations

One must identify determining directions that can be stabilized by admissible changes of noise and prove quantitative absolute-continuity bounds for those changes. Strong dissipation or a Lyapunov recurrence mechanism is also needed to make repeated attempts effective. The conclusion is generally in a Wasserstein/bounded-Lipschitz topology rather than total variation. If the noise cannot influence the unstable modes, or if the feedback requires a singular change of law, asymptotic binding fails. The method is therefore not a replacement for ordinary graphical coupling when exact agreement is available cheaply.

## Sources

Martin Hairer, *Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling*, Probability Theory and Related Fields **124** (2002), 345--380. Section 2.3 introduces binding in which trajectories approach without finite-time coalescence; Section 3 states assumptions A1--A5; Theorem 4.1 proves exponential bounded-Lipschitz contraction and Corollary 4.3 gives the unique invariant measure and convergence. Sections 5--6 verify the architecture for stochastic differential equations and parabolic SPDE examples. DOI: https://doi.org/10.1007/s004400200216. Preprint: https://arxiv.org/abs/math/0109115
