---
title: Separated tagged-vacancy reproduction for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - chronology
  - graphical construction
  - regeneration
  - coarse graining
---

# Separated tagged-vacancy reproduction for one-dimensional FA-1f

This entry strengthens the [iterated moving-edge splitting lemma](iterated-moving-edge-splitting-for-fa-1f.md). For every prescribed separation scale, one tagged physical vacancy can be converted into two tagged physical vacancies at that separation, with exponentially decaying time and spatial tails. The construction is uniform over the exterior FA history.

The main random reset is chronology averaged: complete moving-edge branch/coalescence excursions are repeated until an adjacent vacant pair is obtained. A finite legal cleanup word is then used only to separate the two children. If the cleanup fails, all but one surviving tag are discarded and the chronology-averaged reset is started again. Thus no favorable word is assumed to succeed, and failure never kills the parent lineage.

Use vacancy variables, with vacancy state \(1\), equilibrium vacancy density \(q\in(0,1)\), and \(p=1-q\).

## Immortal tag

A tag is always attached to a physical vacancy. If its host vacancy becomes occupied, the update was legal, so immediately before the update at least one neighboring site was vacant. Transfer the tag to one such neighboring vacancy; if both are vacant, use an independent tie-breaking coin. Thus a tag can be followed for all times. Its jumps are nearest-neighbor and can occur only at occupation proposals at its host, hence at total rate at most \(p\).

Tags are auxiliary and may be discarded. When several tags temporarily occupy the same physical vacancy, all but one may be discarded whenever the construction is restarted.

## A finite separation word

Fix \(R\ge2\). Starting from two adjacent vacancies, there exists a finite sequence of legal FA updates, supported on an interval of length depending only on \(R\), whose final configuration contains two vacancies at distance \(R\).

For example, after translating and reflecting, start with vacancies at \(0,1\). Successively propose vacancies at \(2,3,\ldots,R\). Each proposal is legal because the site immediately to its left is vacant. The sites \(0,1,\ldots,R\) are then all vacant. Next successively propose occupation at \(1,2,\ldots,R-1\), always keeping both endpoints \(0,R\) vacant. Each occupation proposal is legal because, when site \(j\) is filled, site \(j+1\) is still vacant. The terminal pattern on \([0,R]\) therefore has vacancies at \(0,R\) and occupied sites in between.

Choose disjoint small time windows for these prescribed proposals and require that no conflicting proposal occurs at the finitely many sites used before the word is completed. The resulting graphical event, denoted \(\mathcal S_R\), has probability

$$
\delta_R>0,
\tag{1}
$$

where \(\delta_R\) depends only on \(q\) and \(R\). Since legality of every prescribed update is certified by vacancies already created inside the word, the event is valid for every exterior configuration. Extra exterior vacancies do not invalidate it; the exclusion of conflicting proposals on the finitely many sites prevents them from changing the prescribed local state before completion.

The cleanup word is not itself a chronology average. Its role is only to turn the already regenerated adjacent pair into a separated pair with a fixed positive probability.

## Repeated reproduction attempts

Start at an arbitrary stopping time \(\sigma\) with one tagged vacancy. One reproduction attempt consists of two stages.

1. Run the [iterated moving-edge splitting construction](iterated-moving-edge-splitting-for-fa-1f.md) until two adjacent vacancies have been obtained.
2. From that adjacent pair, attempt the finite event \(\mathcal S_R\). If it succeeds, attach one child tag to each terminal vacancy and stop. If it fails, retain any one immortal tag, discard all other auxiliary tags, and restart stage 1 from the resulting tagged vacancy.

By the strong Markov property, after every restart the future proposal processes are fresh. Conditional on the entire past and on the exterior configuration, stage 2 succeeds with probability at least \(\delta_R\). Consequently the number \(J_R\) of attempts before successful separated reproduction satisfies

$$
\mathbb P(J_R>m)\le(1-\delta_R)^m.
\tag{2}
$$

The duration and spatial displacement of stage 1 have exponential tails by the iterated splitting lemma. Stage 2 takes a deterministic bounded time and uses a deterministic bounded spatial interval. Since an immortal tag itself jumps at rate at most \(p\), failure of a cleanup attempt also produces an exponentially bounded displacement before the next restart. A standard exponential-moment estimate for a geometric sum therefore gives constants

$$
c_R,C_R>0
$$

depending only on \(q,R\) such that, if \(\tau_R\) is the successful reproduction time and \(W_R\) is the maximal distance from the initial tag reached by any retained tag before success,

$$
\mathbb P(\tau_R-\sigma>u)\le C_Re^{-c_Ru},
\qquad u\ge0,
\tag{3}
$$

and

$$
\mathbb P(W_R>m)\le C_Re^{-c_Rm},
\qquad m\ge0.
\tag{4}
$$

At time \(\tau_R\) the physical FA configuration contains two tagged vacancies whose mutual distance is exactly \(R\) for the explicit word above.

Equivalently, for every \(\varepsilon>0\) there are deterministic \(T,W<\infty\), depending only on \(q,R,\varepsilon\), such that, from any tagged vacancy and in every exterior FA history, with conditional probability at least \(1-\varepsilon\) the construction produces two tagged physical vacancies at distance \(R\) before time \(T\) and without any retained tag leaving the radius-\(W\) spatial buffer.

## Role in the out-of-equilibrium problem

The lemma supplies a local reproduction mechanism at every \(q>0\) with arbitrarily reliable completion on a sufficiently long time window. It is stronger than a one-shot favorable-word argument: unsuccessful cleanup words do not consume the parent seed, because the moving-edge tag is immortal and the complete regeneration stage can be restarted.

What is still needed for a global vacancy-gap argument is a spatial bookkeeping rule for descendants from different parents. Two child lineages can later enter the same region and their tags may temporarily share a physical vacancy. A block construction must select descendants so that enough lineages remain in distinct coarse regions. The exponential buffer estimate (4) is intended for that selection step.
