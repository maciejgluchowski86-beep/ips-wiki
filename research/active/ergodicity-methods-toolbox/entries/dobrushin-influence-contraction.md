---
method_id: dobrushin-influence-contraction
title: Dobrushin influence contraction for Glauber dynamics
category: coupling
targets:
  - mixing
model_scope: Finite spin systems with single-site Glauber updates and uniformly summable site-to-site influences
source_status: primary-checked
primary_source: Martin Dyer, Leslie Ann Goldberg and Mark Jerrum, Matrix norms and rapid mixing for spin systems, Annals of Applied Probability 19 (2009), 71-107
primary_pinpoint: Definition of site influence/dependency matrix, p. 81; Section 3.2, Lemmas 28-30, pp. 90-92; Corollary 18, pp. 84-85
primary_url: https://doi.org/10.1214/08-AAP532
application_source: Martin Dyer, Leslie Ann Goldberg and Mark Jerrum, Matrix norms and rapid mixing for spin systems, Annals of Applied Probability 19 (2009), 71-107
application_pinpoint: Section 4 and Example 2, p. 95, for heat-bath Glauber dynamics of graph colorings
application_url: https://doi.org/10.1214/08-AAP532
wiki_candidate: yes
---

# Dobrushin influence contraction for Glauber dynamics

## Criterion

Let a finite spin system have sites $1,\dots,n$. For the single-site update kernel at site $j$, write $\mu_j(x,\cdot)$ for the conditional distribution of the new spin when the current configuration is $x$. If $S_i$ is the set of pairs of configurations differing only at site $i$, define the influence

\[
\widehat\rho_{ij}
=\max_{(x,y)\in S_i}
 d_{\mathrm{TV}}\bigl(\mu_j(x,\cdot),\mu_j(y,\cdot)\bigr).
\]

A dependency matrix is any nonnegative matrix $R=(\rho_{ij})$ with $\rho_{ij}\geq\widehat\rho_{ij}$. The classical Dobrushin condition in the convention of Dyer--Goldberg--Jerrum is

\[
\alpha:=\|R\|_1<1,
\]

where $\|R\|_1$ is the maximum column sum. Corollary 18 of their paper states that if $\alpha\leq\mu<1$, random-update Glauber dynamics satisfies

\[
\tau_r(\varepsilon)
\leq \frac{n}{1-\mu}\log\frac{n}{\varepsilon}.
\]

Thus a uniform deficit of total incoming influence below one gives rapid total-variation mixing. Their more general theorem allows other matrix norms, but the $\ell^1$ condition is the Dobrushin criterion itself.

## Mechanism

Dobrushin's method tracks sensitivity of observables rather than a single scalar distance between two configurations. For a function $f$ on the configuration space define its coordinate oscillations

\[
\delta_i(f)=\max_{(x,y)\in S_i}|f(x)-f(y)|,
\qquad
\delta(f)=(\delta_1(f),\ldots,\delta_n(f))^T.
\]

For an update at site $j$, Lemma 28 gives the vector inequality

\[
\delta(P^{[j]}f)\leq R_j\delta(f),
\]

where $R_j$ replaces the $j$th column of the identity by the corresponding influence column. Averaging over the uniformly chosen update site yields the random-update matrix

\[
R^\dagger=\frac{n-1}{n}I+\frac1nR.
\]

If $\|R\|\leq\mu<1$, then $\|R^\dagger\|\leq 1-(1-\mu)/n<1$. Iterating the oscillation inequality therefore contracts dependence on every initial coordinate. Lemma 29 converts this decay into a total-variation estimate by applying it to indicator functions of arbitrary events.

This is closely related to path coupling, and the checked source explicitly develops both approaches. The conceptual distinction is useful: Dobrushin starts from a matrix of conditional influences and propagates a vector seminorm of observables; path coupling starts from a metric and a coupling for neighboring configurations. In single-site Glauber systems either can often prove the same numerical contraction.

## Representative IPS use

Dyer--Goldberg--Jerrum treat finite spin systems under heat-bath or more general single-site Glauber updates. Section 4 applies dependency-matrix estimates to graph-coloring spin systems. Example 2 notes that for heat-bath Glauber dynamics on a $\Delta$-regular graph with $2\Delta+1$ colors, the dependency matrix has spectral radius $\Delta/(\Delta+1)<1$, illustrating how local conditional sensitivity becomes a global mixing bound. The paper also discusses analogous influence-matrix analyses for Ising and hard-core Glauber chains.

## Limitations

The criterion is perturbative: it requires the cumulative worst-case influence on each updated site to be strictly below one. Strong local dependence, hard constraints, low temperature, or a highly influential neighbor can violate this even when the dynamics is nevertheless ergodic and rapidly mixing by another method. The bound is based on worst-case boundary configurations, so rare bad configurations are not averaged away.

The finite-volume mixing theorem does not by itself prove an infinite-volume spectral gap or convergence theorem; a uniform finite-to-infinite argument is additional. Conversely, the classical infinite-volume Dobrushin uniqueness theorem concerns uniqueness of Gibbs measures, a related but logically different conclusion. Finally, weighted or spectral matrix norms can succeed when the plain Dobrushin column-sum condition fails, and should not be conflated with the strict $\|R\|_1<1$ criterion.

## Sources

Primary source: Martin Dyer, Leslie Ann Goldberg and Mark Jerrum, *Matrix norms and rapid mixing for spin systems*, Annals of Applied Probability 19 (2009), 71-107, especially pp. 81, 84-85 and Section 3.2, pp. 90-92. https://doi.org/10.1214/08-AAP532

The paper attributes the infinite-volume uniqueness condition $\|R\|_1<1$ to R. L. Dobrushin. The entry uses the later checked primary spin-dynamics theorem above for its quantitative mixing statement.
