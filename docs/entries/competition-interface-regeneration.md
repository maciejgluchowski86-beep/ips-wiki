---
title: Regeneration of a competition interface
status: literature
audit: current
tags:
  - regeneration
  - contact process
  - interface
---

# Regeneration of a competition interface

## Criterion

Consider the one-dimensional symmetric two-type contact process started from a Heaviside state, with type 1 occupying the left half-line and type 2 the right half-line. The two species use the same supercritical contact-process birth and death rates, so the principal slow object is the random interface separating their descendant regions.

Mountford and Valesin establish an **interface regeneration** statement: at suitable deterministic observation times, the future interface can be coupled to a fresh copy of the process started from a canonical Heaviside configuration translated to the current interface location, with the discrepancy between the two interface positions controlled with high probability. Theorem 2.11 is the central restart estimate. Iterating this regeneration comparison over long time blocks produces approximately stationary, weakly dependent increments. Together with tight control of the interface width, this yields Theorem 1.2: after diffusive rescaling the interface position converges to Brownian motion.

The usable criterion is therefore not extinction of either species. It is localization of the competition zone plus a restart coupling that repeatedly replaces the complicated past behind the interface by a translated canonical two-phase configuration while changing the future interface only by a controlled error.

## Mechanism

The graphical contact-process construction contains many ancestral paths, so the interface position is not itself Markov. Regeneration isolates times at which most of that ancestral information can be discarded. A fresh graphical process is started from the simple left/right split at the current interface location and is coupled to the original future evolution using common Poisson marks.

Theorem 2.11 says, in effect, that the fresh and original interfaces remain close after the restart except on a small event. The supercritical one-type contact-process estimates provide the spatial screening needed for this: deep inside either occupied region, the future is overwhelmingly determined by local surviving ancestry rather than details on the opposite side of the interface.

Applying the restart construction successively produces long blocks whose interface displacements can be compared to independent copies with a common translated law. Standard renewal/martingale approximation arguments then supply a law of large numbers scale and, in the symmetric case, the functional central limit theorem.

This is distinct from regeneration of a **physical reaction front**, where a front particle or empty region itself creates an exact fresh state behind it. Here the regenerative object is the boundary between two competing populations; neither side is erased, and the restart is a coupling approximation built from graphical ancestry.

## Representative IPS use

The source treats the finite-range symmetric multitype contact process on $\mathbb Z$ with supercritical birth rate. The interface width is tight, and the regenerated interface increments are used to prove Brownian diffusive scaling of the interface position. This gives a reusable architecture for competition systems in which the full configuration is high-dimensional but a localized interface can periodically forget most of its past.

## Limitations

The method depends on a localized interface and strong one-type contact-process control on both sides. If the competition zone spreads macroscopically, if one species has no stable bulk phase, or if long-range dependence prevents graphical screening, the restart error need not be small. The cited theorem is symmetric; asymmetric systems require a deterministic interface speed and different control. Regeneration proves a long-time law for the interface, not global mixing of the entire infinite configuration.

## Sources

Thomas Mountford and Daniel Valesin, *Functional Central Limit Theorem for the Interface of the Symmetric Multitype Contact Process*, ALEA **13** (2016), 481--519. Theorem 1.2 gives the functional CLT. Sections 2.3--2.4 develop the interface-regeneration comparison, with Theorem 2.11 as the central restart statement; Section 3 uses it in the limit theorem. DOI: https://doi.org/10.30757/ALEA.v13-20. Preprint: https://arxiv.org/abs/1509.04339
