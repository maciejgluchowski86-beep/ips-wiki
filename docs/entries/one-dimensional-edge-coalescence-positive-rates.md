---
title: One-dimensional edge coalescence for positive-rates spin systems
status: literature
audit: current
tags:
  - positive rates
  - attractiveness
  - coupling
  - one-dimensional spin systems
---

# One-dimensional edge coalescence for positive-rates spin systems

## Criterion

Gray's Theorem 1 states that a binary spin system on the integers is ergodic if its flip rates are periodic, attractive, nearest-neighbour, and strictly positive. Section 3, Theorem 2, extends the conclusion to repulsive nearest-neighbour rates by alternating the identities of zero and one.

The proof does not stop at the standard attractive reduction to upper and lower invariant laws. Its extra one-dimensional criterion is Proposition 3: for attractive nearest-neighbour systems with uniformly bounded rates, ergodicity is equivalent to a strictly positive limiting probability that the processes started from all ones and all zeros agree on an arbitrary fixed interval. Gray proves this block agreement through a family of moving **left and right edges** attached to half-line initial conditions.

## Mechanism

All initial states are built on one Harris graphical construction. For every half-line initial condition, Gray inserts an edge at the interface between a hybrid process and an extremal process. Properties E1-E3 say that the edge is always between a zero and a one and, crucially, that on one side of the edge the half-line process agrees exactly with one extremal process while on the other side it agrees with the other. Proposition 2 shows that once the upper and lower extremal copies agree between a suitable left/right edge pair, this agreement is propagated as long as the two edges remain separated.

The one-dimensional geometry makes the collection of edges ordered. Property E4 says edges cannot cross, and E5 says two edges that meet coalesce forever. The Lemma in Section 2 proves that neighboring left edges, and neighboring right edges, eventually coalesce with probability tending to one uniformly in their starting position. If a positive density of distinct edges survived, periodicity and the spatial ergodic theorem would force a positive density of bounded gaps. Strict positivity of the flip rates gives a uniform positive chance for each such nearby pair to move together and collide in the next unit time, contradicting persistence of that density. Periodicity then also implies that, at large times, no edge remains in a fixed spatial window with high probability.

Gray combines this with a negative-correlation inequality for left and right edge locations to find, with probability bounded below, an edge pair lying on opposite sides of a prescribed interval. Trace that pair backward to its last time of being close. Proposition 2 reduces agreement of the extremal copies on the whole target interval to agreement at at most one specially chosen site at that close encounter. The final use of **positive rates** is local and quantitative: the graphical update coin at that site retains, uniformly over all histories and interval sizes, a fixed positive conditional probability of forcing the required spin value; equations (18)-(23) establish this bound. Hence the upper and lower processes have a uniformly positive chance to agree on every fixed block, and Proposition 3 closes ergodicity.

## Representative IPS use

Theorem 1 solves the positive-rates problem for periodic attractive nearest-neighbour spin systems on the integers. Theorem 2 gives the analogous result for repulsive nearest-neighbour rates. Translation invariance is not needed; periodicity suffices.

## Limitations

The proof is intrinsically one-dimensional and nearest-neighbour: it relies on scalar ordered interfaces that cannot cross and on the fact that agreement between two edges is protected by nearest-neighbour dynamics. Periodicity is used essentially in Gray's edge-coalescence/escape Lemma to turn a hypothetical surviving edge density into a spatial ergodic contradiction; Gray explicitly notes that the rest of the proof only needs uniform upper and positive lower rate bounds. The method therefore contains substantially more structure than the generic live attractive-coupling page: attractiveness supplies the extremal coupling, while edge coalescence and the local positive-rate repair are what force the two extremal laws to coincide.

## Sources

Primary source: Lawrence F. Gray, *The positive rates problem for attractive nearest neighbor spin systems on Z*, Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 61 (1982), 389-404, DOI 10.1007/BF00539839. Section 1 defines the edge processes and proves their hybrid identities and agreement propagation. Section 2 contains Proposition 3, the edge-coalescence/escape Lemma, and Theorem 1; equations (18)-(23) are the uniform positive-rate local agreement estimate. Section 3 gives the repulsive transformation and Theorem 2.
