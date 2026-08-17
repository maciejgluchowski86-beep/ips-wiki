---
method_id: coupling-independence-coarse-grained-comparison
title: Coupling independence and coarse-grained Glauber comparison
category: coupling
targets:
  - spectral-gap
  - mixing
model_scope: Finite spin systems on high- or unbounded-degree graphs, with list-colouring and hard-core applications
source_status: primary-checked
primary_source: Xiaoyu Chen and Weiming Feng, "Rapid Mixing via Coupling Independence for Spin Systems with Unbounded Degree," APPROX/RANDOM 2025, LIPIcs 353, Article 68 (2025)
primary_pinpoint: Definition 7 and Theorem 9, Sections 2.1--2.2, pp. 68:7--68:9; Theorem 1 application, pp. 68:3--68:5
primary_url: https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2025.68
application_source: Xiaoyu Chen and Weiming Feng, same paper
application_pinpoint: Theorem 1 and proof sketch following Theorem 9; Theorem 5 for the hard-core application
application_url: https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2025.68
wiki_candidate: yes
---

# Coupling independence and coarse-grained Glauber comparison

## Criterion

Let $\mu$ be a Gibbs distribution on spins in $[q]^V$. For a positive vertex weight $\rho$, write

\[
H_\rho(\sigma,\tau)=\sum_{v:\,\sigma(v)\ne\tau(v)}\rho(v).
\]

Chen--Feng call $\mu$ **$C$-coupling independent** if, whenever two feasible pinnings $\sigma_1,\sigma_2$ differ at one pinned vertex $v_0$, there is a coupling $(X,Y)$ of the two corresponding conditional Gibbs laws such that

\[
\mathbb E H_\rho(X,Y)\le C\rho(v_0).
\]

This is Definition 7. Their Theorem 9 gives the local-to-global relaxation step. If $\mu$ is $M$-coupling independent, $0<\eta\le 1/(2\lceil M\rceil)$, and the maximum degree $\Delta$ is above an explicit threshold, then

\[
T_{\rm rel}^{\rm GD}(\mu)
 \le 2^{O(M/\eta)}T_{\rm rel}^{(\eta)}(\mu),
\]

where $T_{\rm rel}^{(\eta)}$ is the worst Glauber relaxation time among conditional systems whose unpinned induced graph has maximum degree at most $\eta\Delta$. Thus a coupling estimate for *pinned conditional laws* transfers a relaxation bound from a lower-degree regime to the original high-degree system.

## Mechanism

The proof object is not a one-step coupling of two Glauber trajectories. Coupling independence controls how much an imposed single-site discrepancy can change an entire conditional sample. Chen--Feng partition the vertices into a bounded number of coarse parts so that every part has much smaller internal degree. A down-up walk refreshes coarse parts rather than individual vertices. Coupling independence supplies the transportation control needed to show that this coarse chain has bounded relaxation cost; the remaining within-part dynamics are precisely the low-degree pinned chains represented by $T_{\rm rel}^{(\eta)}$.

This also explains the distinction from spectral independence. The paper notes that coupling independence implies spectral independence, but Theorem 9 uses the stronger coupling object itself to compare the hard high-degree dynamics with easier conditional systems. It is likewise distinct from ordinary path coupling, which asks for contraction of neighboring *dynamic states*, and from block coupling, which changes the physical update to a joint block resampling and then analyzes that new chain directly.

## Representative IPS use

For proper list-colourings on triangle-free graphs, Theorem 1 proves optimal $O_\delta(n)$ relaxation when every list has size at least $(\alpha_*+\delta)\Delta$, where $\alpha_*\approx1.763$ solves $\alpha=e^{1/\alpha}$. The proof explicitly proceeds by verifying coupling independence and applying Theorem 9. After pinning most vertices, the remaining induced graph is sufficiently low-degree that elementary path coupling controls the conditional Glauber dynamics; the comparison theorem lifts that estimate back to the original graph.

The same framework is also developed for hard-core systems, including balanced bipartite graphs with strongly asymmetric local degrees.

## Limitations

Coupling independence is a uniform statement over feasible pinnings, so it may fail even when the unconditioned model mixes rapidly. The comparison theorem also requires a genuinely tractable low-degree conditional regime and, in its stated form, a sufficiently large maximum degree; bounded-degree instances are handled by other results once coupling independence gives spectral independence. The method is finite-volume and proves quantitative Glauber relaxation/mixing, not by itself infinite-volume uniqueness. Finally, verifying coupling independence can be model-specific: in the applications it requires recursive/tree-based coupling estimates rather than following automatically from weak correlations.

## Sources

- Chen and Feng, *Rapid Mixing via Coupling Independence for Spin Systems with Unbounded Degree*, Definition 7 and Theorem 9, Sections 2.1--2.2; Theorem 1 for list-colouring. DOI: https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2025.68.
