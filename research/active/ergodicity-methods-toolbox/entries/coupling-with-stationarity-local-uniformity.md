---
method_id: coupling-with-stationarity-local-uniformity
title: Coupling with stationarity and local uniformity
category: coupling
targets:
  - mixing
  - convergence
model_scope: Finite Glauber-type chains where typical stationary configurations admit contraction although worst-case configuration pairs do not.
source_status: primary-checked
primary_source: Thomas P. Hayes and Eric Vigoda, "Coupling with the stationary distribution and improved sampling for colorings and independent sets," Annals of Applied Probability 16 (2006), 1297-1318.
primary_pinpoint: Theorem 1.2 and its proof in Section 3; Theorem 1.4 for Glauber dynamics on graph colorings.
primary_url: https://doi.org/10.1214/105051606000000330
application_source: Thomas P. Hayes and Eric Vigoda, same paper.
application_pinpoint: Theorem 1.4 and Section 1 discussion of local uniformity for heat-bath Glauber dynamics on colorings.
application_url: https://arxiv.org/abs/math/0610188
wiki_candidate: yes
---

# Coupling with stationarity and local uniformity

## Criterion

Let $(\Omega,P,\pi)$ be a finite Markov chain equipped with a metric $\rho$ of diameter $D$. Hayes--Vigoda call a pair $(x,y)$ distance-decreasing when one can couple one transition from $x$ and $y$ so that the expected next distance is smaller by a fixed amount. Their Theorem 1.2 replaces the usual worst-case requirement by a high-stationary-mass requirement: if there is a set $S\subset\Omega$ with

$$
\pi(S)\ge 1-\frac{\varepsilon}{16D}
$$

and every pair in $S\times\Omega$ admits an $\varepsilon$-decreasing coupling, then coupling an arbitrary chain to a chain started from $\pi$ gives a quantitative total-variation mixing bound of order

$$
O\!\left(\frac{\log D\,\log(1/\delta)}{\varepsilon}\right)
$$

steps to reach total-variation error $\delta$, with the paper giving explicit ceiling constants. The stationary copy remains in $S$ with overwhelmingly high probability, so the coupling need not contract on rare bad stationary configurations.

## Mechanism

Traditional path coupling asks for a contraction for every adjacent pair, including configurations that are combinatorially possible but extremely atypical in equilibrium. Here one chain is instead started exactly from stationarity. At every time its marginal remains $\pi$, so a high-probability structural property of $\pi$ can be used repeatedly during the coupling.

The proof divides time into epochs. Unless the stationary chain visits the exceptional set $S^c$, the metric has negative drift under the chosen coupling. The small stationary mass of $S^c$ pays for the exceptional epochs. Repeating the argument drives the two chains together with high probability, and the coupling inequality converts coalescence into a total-variation estimate for the arbitrary initial chain.

The second ingredient in applications is therefore **local uniformity**: prove that a random equilibrium configuration has many locally available moves. This can hold well beyond the parameter range where worst-case configurations permit Hamming contraction.

## Representative IPS use

For heat-bath Glauber dynamics on proper $k$-colorings of a triangle-free graph of maximum degree $\Delta$, Hayes--Vigoda combine local-uniformity estimates with coupling to stationarity. Their Theorem 1.4 yields $O(n\log n)$ mixing when $\Delta=\Omega(\log n)$ and $k/\Delta$ exceeds approximately $1.764$ (with the theorem stating the precise finite-parameter condition). The obstruction to simpler path coupling is that a worst-case coloring can leave too few colors available around a vertex; under the stationary coloring law such configurations are sufficiently rare.

The paper also develops the same philosophy for weighted independent sets in the hard-core model, again exploiting typical stationary neighborhoods instead of worst-case pairs.

## Limitations

This method requires useful information about the stationary distribution before the mixing proof is complete. Establishing the high-mass good set $S$ can be as difficult as the coupling itself, and model-specific concentration or spatial arguments are usually needed.

The theorem is finite-state and quantitative; an infinite-volume ergodicity statement requires a separate uniform finite-volume passage. It also does not remove the need for a valid coupling on $S\times\Omega$: the gain is that contraction may fail on a small stationary exceptional set, not that contraction can fail typically. Finally, unlike one-site path coupling, the method is not purely local in configuration space because it explicitly uses global equilibrium mass.

## Sources

- Hayes and Vigoda, *Annals of Applied Probability* 16 (2006), Theorem 1.2 and Section 3; coloring application Theorem 1.4. DOI: https://doi.org/10.1214/105051606000000330. Preprint: https://arxiv.org/abs/math/0610188.
