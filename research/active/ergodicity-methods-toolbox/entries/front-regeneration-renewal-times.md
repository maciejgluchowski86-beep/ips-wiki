---
method_id: front-regeneration-renewal-times
title: Front regeneration and renewal times
category: lyapunov-regeneration
targets:
  - convergence
model_scope: One-dimensional interacting particle systems with a propagating front that exposes a fresh region and admits regeneration times
source_status: primary-checked
primary_source: Milton Jara, Gregorio Moreno and Alejandro F. Ramírez, "Front Propagation in an Exclusion One-dimensional Reactive Dynamics," Markov Processes and Related Fields 14 (2008), 185--206
primary_pinpoint: Theorems 1--2; Section 2.4; Propositions 1, 3 and 4; Section 3
primary_url: https://arxiv.org/abs/math/0703173
application_source: same as primary source
application_pinpoint: Theorem 2 and Propositions 3--4
application_url: https://math-mprf.org/journal/articles/id1150/
wiki_candidate: yes
---

# Front regeneration and renewal times

## Criterion

Suppose an interacting particle system has a distinguished front \(r_t\) separating an already explored region from a fresh region. A regeneration method seeks random times
\[
0<\kappa_1<\kappa_2<\cdots
\]
at which the future of the front, after translation to the regeneration point, has a law independent of the pre-regeneration history. If the first regeneration is almost surely finite, later regeneration increments are independent and identically distributed, and the required time/front increments have finite first or second moments, renewal theory gives long-time laws for the front and for the environment viewed from it.

Jara--Moreno--Ramírez implement this architecture for an exclusion reactive process. Section 2.4 defines candidate times \(S_k\), failure times \(D_k\), the successful index \(K\), and the first regeneration time \(\kappa=S_K\). Proposition 1 proves finiteness and moment estimates. Proposition 3 identifies the conditional post-regeneration law after every \(\kappa_n\). Proposition 4 then proves that the successive regeneration-time increments are independent, with all increments after the first identically distributed; the corresponding front pieces have the analogous independence structure. Theorem 2 concludes that the process of activated particles as seen from the moving front converges to a unique nontrivial invariant measure. The same renewal structure also gives the law of large numbers and functional central limit theorem for the front in Theorem 1.

## Mechanism

The essential construction is a **fresh-start event at the interface**. A naive stopping time at which the front advances is not regenerative, because particles behind the front can later catch it and transmit information from the past. The authors therefore alternate times when a new front particle is created with tests of whether old particles can ever violate a protective space-time separation. The first candidate whose failure time is infinite becomes a regeneration time.

At such a time, the process to the right of the front depends only on previously unused randomness and has the same law, after translation, as a reference process conditioned on the successful separation event. This gives an exact renewal decomposition rather than merely approximate decorrelation. Once the increments are independent with controlled tails, standard renewal theorems identify asymptotic speeds and the limiting age distribution inside the current regeneration cycle. That last observation is what turns front regeneration into convergence of the process viewed from the front, not only a law of large numbers for \(r_t\).

## Representative IPS use

The model contains exclusion-moving \(X\) particles and initially static \(Y\) particles on \(\mathbb Z\). When an \(X\) reaches a \(Y\), the \(Y\) is activated into an \(X\); the rightmost visited position is the reactive front. Theorem 1 proves deterministic positive speeds for both the front and the number of activated particles and Brownian scaling limits. More directly for ergodic-method purposes, Theorem 2 proves convergence, for every nontrivial initial condition in the stated state space, of the particle configuration seen from the front to a unique nontrivial invariant measure. The proof in Section 3 is explicitly a renewal argument based on Propositions 3--4.

## Limitations

Regeneration is highly structural. One needs a distinguished moving interface, a genuinely fresh source of randomness ahead of it, and a positive-probability event preventing old particles from re-entering the future front dynamics. Proving that the first successful regeneration occurs and has adequate moments can require substantial model-specific estimates; in the cited paper this occupies Section 4. The regeneration time need not itself be an ordinary stopping time, so the correct sigma-field at regeneration must be handled carefully. Finally, this method studies the process in a moving frame; convergence of the front environment does not by itself imply global convergence of the original translation-invariant process.

## Sources

Primary checked source: Jara, Moreno and Ramírez, *Front Propagation in an Exclusion One-dimensional Reactive Dynamics*, Markov Process. Related Fields 14 (2008), 185--206. Section 2.4 constructs regeneration times; Propositions 1, 3 and 4 give finiteness, restart and independence; Section 3 uses that renewal structure to prove Theorems 1--2.