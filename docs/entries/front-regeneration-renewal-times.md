---
title: Front regeneration and renewal times
status: literature
audit: current
tags:
  - regeneration
  - fronts
  - renewal
---

# Front regeneration and renewal times

## Criterion

Suppose an interacting particle system has a distinguished front \(r_t\) separating an already explored region from a fresh region. A regeneration method seeks random times
\[
0<\kappa_1<\kappa_2<\cdots
\]
at which the future of the front, after translation to the regeneration point, has a law independent of the pre-regeneration history. If the first regeneration is almost surely finite, later regeneration increments are independent and identically distributed, and the required time/front increments have finite moments, renewal theory gives long-time laws for the front and for the environment viewed from it.

Jara--Moreno--Ramírez implement this architecture for an exclusion reactive process. Section 2.4 defines candidate times, failure times, and the first successful regeneration. Proposition 1 proves finiteness and moment estimates. Propositions 3 and 4 identify the conditional post-regeneration law and independence of successive regeneration increments. Theorem 2 concludes that the activated-particle configuration seen from the moving front converges to a unique nontrivial invariant measure. The same renewal structure gives the law of large numbers and functional central limit theorem for the front in Theorem 1.

## Mechanism

The essential construction is a fresh-start event at the interface. A naive stopping time at which the front advances is not regenerative, because particles behind the front can later catch it and transmit information from the past. The authors therefore alternate times when a new front particle is created with tests of whether old particles can ever violate a protective space-time separation. The first candidate whose failure time is infinite becomes a regeneration time.

At such a time, the process to the right of the front depends only on previously unused randomness and has the same law, after translation, as a reference process conditioned on the successful separation event. This gives an exact renewal decomposition rather than merely approximate decorrelation. Once the increments are independent with controlled tails, renewal theory identifies asymptotic speeds and the limiting environment seen from the front.

## Representative IPS use

The model contains exclusion-moving \(X\) particles and initially static \(Y\) particles on \(\mathbb Z\). When an \(X\) reaches a \(Y\), the \(Y\) is activated into an \(X\); the rightmost visited position is the reactive front. Theorem 2 proves convergence, for every nontrivial initial condition in the stated state space, of the particle configuration seen from the front to a unique nontrivial invariant measure.

This differs from [East distinguished-zero screening](east-distinguished-zero-screening.md): the East vacancy screens an equilibrium region, whereas here a moving physical front creates renewal times. It also differs from [regeneration at a collapse atom](particle-collapse-regeneration.md), where the entire centered finite-particle state returns to one deterministic atom.

## Limitations

Regeneration is highly structural. One needs a distinguished moving interface, a genuinely fresh source of randomness ahead of it, and a positive-probability event preventing old particles from re-entering the future front dynamics. Proving the first successful regeneration and adequate moments can require substantial model-specific estimates. The regeneration time need not be an ordinary stopping time, so the correct sigma-field at regeneration must be handled carefully. Convergence of the front environment also does not by itself imply global convergence of the original translation-invariant process.

## Sources

- Jara, Moreno and Ramírez, *Front Propagation in an Exclusion One-dimensional Reactive Dynamics*, Markov Process. Related Fields 14 (2008), 185--206, Section 2.4, Propositions 1, 3 and 4, and Sections 3--4, https://arxiv.org/abs/math/0703173.
