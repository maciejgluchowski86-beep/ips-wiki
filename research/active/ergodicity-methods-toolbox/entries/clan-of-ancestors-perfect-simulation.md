---
method_id: clan-of-ancestors-perfect-simulation
title: Clan-of-ancestors perfect simulation
category: graphical-duality
targets:
  - uniqueness
  - convergence
  - mixing
model_scope: Infinite-volume interacting point processes, loss networks, contour systems, and Gibbs models with a finite backward dependency clan.
source_status: primary-checked
primary_source: Roberto Fernández, Pablo A. Ferrari, and Nancy L. Garcia, "Perfect simulation for interacting point processes, loss networks and Ising models," Stochastic Processes and their Applications 102 (2002), 63-88.
primary_pinpoint: Theorem 1(ii), pp. 19-20; Section 4, especially equations (4.1)-(4.4) and the subcriticality condition alpha_q<1; Section 5.
primary_url: https://doi.org/10.1016/S0304-4149(02)00180-1
application_source: Roberto Fernández, Pablo A. Ferrari, and Nancy L. Garcia, same paper.
application_pinpoint: Sections 2 and 5; Ising contour and random-cluster examples described in the construction and applications.
application_url: https://arxiv.org/abs/math/9911162
wiki_candidate: yes
---

# Clan-of-ancestors perfect simulation

## Criterion

Represent the target interacting process as a thinning or cleaning of a free marked Poisson birth-and-death process. For a proposed object $C$, define its first-generation ancestors to be earlier objects whose presence can affect whether $C$ is accepted; iterate this relation backward and write $A^C$ for the resulting clan of ancestors. Fernández--Ferrari--Garcia's Theorem 1(ii) states, in their cylinder construction, that if $A^C$ is finite almost surely for every cylinder $C$, then the stationary interacting process can be constructed on all times $t\in\mathbb R$ by applying the cleaning rule to each finite clan. Its time-zero marginal is the desired stationary measure.

A practical sufficient condition comes from Section 4. Dominate the backward ancestor exploration by a multitype branching process. With a positive weight $q$ on types, the paper defines an offspring-load parameter $\alpha_q$; the condition $\alpha_q<1$ makes the majorizing branching process subcritical. Hence every relevant clan is finite almost surely, making the perfect construction feasible. Quantitative tails for clan size or backward depth transfer to convergence and mixing estimates for finite windows.

## Mechanism

The proof separates generation from interaction. First generate all potentially relevant births in a free Poisson process. Starting from the finite set of target objects intersecting the observation window, trace potential influences backward. If this exploration terminates, there is a finite oldest generation. One can then sweep forward through this finite dependency graph and accept or reject each birth using the actual interaction rule. The result in the target window is therefore determined without any boundary condition or arbitrary initial state in the remote past.

The crucial comparison is geometric rather than metric. The ancestor relation defines a backward oriented-percolation problem. Subcriticality rules out an infinite path to time $-\infty$; the branching majorant is a convenient sufficient test for that nonpercolation. This is different from coupling from the past: no grand coupling of trajectories from all initial configurations is required, and no monotone top/bottom sandwich is needed.

## Representative IPS use

The paper treats Gibbsian objects including Peierls-contour representations of the Ising model and random-cluster models. A local spin sample can be reconstructed from the finite collection of contour or cluster objects whose acceptance may influence the requested window. Under the ancestor-subcriticality condition, this gives exact infinite-volume samples using only a random finite space-time region.

The same architecture applies to loss networks and interacting point processes: proposed calls, particles, animals, or grains are generated freely, their conflict ancestry is explored backward, and only the finite relevant clan is cleaned forward.

## Limitations

Almost-sure clan finiteness is load-bearing. If backward oriented percolation survives, the algorithm need not terminate and the argument gives neither uniqueness nor perfect simulation. The simple condition $\alpha_q<1$ is only sufficient; it can fail even when the actual dependency clan is finite because the branching comparison ignores exclusions and other cancellations between potential ancestors.

The method also requires a graphical representation in which all possible dependencies can be exposed from a dominating free process. Strong interactions, high activities, or long-range incompatibility enlarge the clan and can destroy the subcritical comparison. Perfect simulation is a stronger output than ordinary forward convergence, but its criterion is correspondingly restrictive.

## Sources

- Fernández, Ferrari and Garcia, *Stochastic Processes and their Applications* 102 (2002), Theorem 1(ii), pp. 19-20, Sections 4-5. DOI: https://doi.org/10.1016/S0304-4149(02)00180-1. Preprint: https://arxiv.org/abs/math/9911162.
