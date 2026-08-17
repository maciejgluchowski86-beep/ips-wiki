---
method_id: second-class-particle-shock-random-walk
title: Second-class particle coupling for microscopic shocks
category: coupling
targets:
  - shock-dynamics
  - interface-stability
model_scope: One-dimensional conservative particle systems with product shock measures and a single coupled discrepancy
source_status: primary-checked
primary_source: Márton Balázs, György Farkas, Péter Kovács and Attila Rákos, Random walk of second class particles in product shock measures, Journal of Statistical Physics 139 (2010), 252–279
primary_pinpoint: Section 3.1, Theorem 3.1 and Remark 3.2
primary_url: https://doi.org/10.1007/s10955-010-9933-8
application_source: same as primary source
application_pinpoint: Theorem 3.1, ASEP case and the model-specific cases in Section 3
application_url: https://arxiv.org/abs/0909.3071
wiki_candidate: yes
---

# Second-class particle coupling for microscopic shocks

## Criterion

Couple two conservative particle systems $\omega(t)\leq\zeta(t)$ by the basic graphical coupling and suppose initially they differ by exactly one particle. The discrepancy is then a **second-class particle**. A particularly strong situation occurs when there is a one-parameter family of shock measures $\nu_j$ indexed by the discrepancy position $j$ such that the coupled process closes on this family:

\[
\left.\frac{d}{dt}\nu_j S(t)\right|_{t=0}
   =P(\nu_{j+1}-\nu_j)+Q(\nu_{j-1}-\nu_j).
\]

Theorem 3.1 of Balázs--Farkas--Kovács--Rákos gives explicit parameter relations under which this identity holds for several one-dimensional particle systems. Consequently, if the initial coupled law is $\nu_j$, then at later times it is a mixture of the same shock measures, with the mixing weights given by a continuous-time nearest-neighbour random walk of rates $P,Q$.

For ASEP with left and right bulk densities satisfying the paper's shock relation, the second-class particle therefore performs an asymmetric random walk. Remark 3.2 identifies its drift with the Rankine--Hugoniot shock velocity.

## Mechanism

A basic coupling converts one unit of difference between two conservative configurations into a marked particle. Usually that marked discrepancy remains strongly entangled with the environment. The shock-measure calculation is stronger: after averaging over the product backgrounds on the two sides of the marker, the full coupled generator maps the family $\{\nu_j\}$ into the discrete span of its translates. The infinite interacting system has therefore reduced a moving interface to a one-particle Markov chain.

This gives an exact microscopic description of shock stability. The bulk distributions on the two sides retain their prescribed product forms while the random shock location evolves autonomously. In the reference frame of the second-class particle, the shock profile is stationary in the corresponding sense; in the laboratory frame its location has the law of the random walk. The law of large numbers and fluctuations of that random walk then immediately transfer to the microscopic shock.

The proof interface is distinct from a general attractiveness or discrepancy-nonincreasing coupling. Those methods control whether discrepancies can be created or ordered. Here the distinguished discrepancy is retained deliberately and its own stochastic motion carries the macroscopic interface information.

## Representative IPS use

For ASEP, Theorem 3.1 gives the density relation under which the single second-class particle marks a product shock and specifies its jump rates. The same paper applies the closure calculation to other conservative systems, including the exponential bricklayers process and zero-range-type examples. In each case the useful object is not global coalescence of two copies but an exact random-walk law for the unique discrepancy separating two equilibrium backgrounds.

## Limitations

Exact closure of a shock family is highly model-specific. It relies on algebraic relations between the jump rates and the left/right product measures, and it is much stronger than the mere existence of a second-class particle. In generic conservative systems the discrepancy interacts with a dynamically changing environment and is not Markov by itself. The method describes shock motion and stability; it does not by itself imply uniqueness of the invariant measure for the full conservative system, whose conserved density normally leaves a family of equilibrium states.

## Sources

Márton Balázs, György Farkas, Péter Kovács and Attila Rákos, *Random walk of second class particles in product shock measures*, Journal of Statistical Physics **139** (2010), 252--279. Section 3.1 and Theorem 3.1 give the generator identity closing translated shock measures; Remark 3.2 interprets the second-class-particle drift as the shock velocity. DOI: https://doi.org/10.1007/s10955-010-9933-8. Preprint: https://arxiv.org/abs/0909.3071
