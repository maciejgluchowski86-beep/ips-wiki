---
title: Dynamical disagreement domination by space-time percolation
status: literature
audit: current
tags:
  - coupling
  - percolation
  - convergence
---

# Dynamical disagreement domination by space-time percolation

## Criterion

Couple two copies $\eta_t,\xi_t$ of the same local spin dynamics with common update randomness. Construct an oriented space-time percolation process so that a disagreement at $(x,t)$ can occur only if an open path connects $(x,t)$ backward to the initial disagreement set $D_0$:

$$
\{\eta_t(x)\ne\xi_t(x)\}
\subseteq
\{(x,t)\longleftrightarrow D_0\times\{0\}\}.
$$

If the associated connectivity function tends to zero uniformly over possible initial disagreements reaching a fixed finite observation set, then the coupling forgets its initial condition locally. In particular, for a local $f$,

$$
|P_t f(\eta)-P_t f(\xi)|
\le
\sum_{x\in\operatorname{supp} f}\operatorname{osc}_x(f)\,
\mathbb P((x,t)\longleftrightarrow D_0\times\{0\}),
$$

so decay of the percolation connectivity gives coupling agreement and convergence. If the bound is uniform over $\eta,\xi$, any two invariant laws coincide.

Gielis--Maes--Vande Velde make this comparison explicit. Section 4.1.2(i) couples two copies of a probabilistic cellular automaton (PCA) and bounds their discrepancies by time-oriented open paths in the space-time graph. Section 4.1.2(iii) gives the continuous-time spin-flip analogue, where vertical Poisson lines are cut by noise events and dependence arrows generate a contact-process-type oriented percolation on $\mathbb Z^d\times\mathbb R$. Propositions 1-2 provide decay estimates for the corresponding connectivity functions in a random environment.

## Mechanism

The basic coupling separates updates into those that erase dependence on the previous local state and those at which neighbouring spins can transmit dependence. Mark an update as open whenever disagreement can pass through it. A disagreement cannot appear spontaneously away from an earlier disagreement: tracing any discrepancy backward therefore produces a directed open path through the update graph.

The spin problem is thus reduced to extinction or weak connectivity of a purely geometric process. In a uniform high-noise regime this comparison may be a genuinely subcritical contact or oriented-percolation process. In the disordered setting of the source, local open probabilities can be arbitrarily close to one, so a multiscale percolation estimate replaces a single uniform subcritical parameter. Either way the load-bearing quantity is the probability of a long open disagreement path.

This differs from [static disagreement percolation](disagreement-percolation-gibbs-uniqueness.md). Here the path lives in **space-time** and records propagation of an actual dynamical disagreement between coupled trajectories.

## Representative IPS use

The source treats directed random versions of Stavskaya's one-dimensional PCA and Toom-type two-dimensional PCA. Their local update probabilities are allowed to contain spatially random, unbounded interaction strengths. Theorems 1-2 combine the disagreement coupling with oriented-percolation estimates to obtain almost-sure uniqueness/convergence bounds and disorder-averaged relaxation estimates for the directed PCA class.

The same paper formulates the continuous-time comparison for random spin-flip IPS: under the basic coupling, influence from an initial discrepancy to $(x,t)$ is bounded by connectivity in the associated cut-and-arrow continuous percolation process. This is the direct contact-process version of the same proof interface.

## Limitations

The quality of the result is only as good as the dominating percolation process. A naive construction that marks too many updates open may percolate even when the original spin dynamics is ergodic. The method therefore loses cancellations and other state-dependent mechanisms that suppress disagreements without literally blocking every dependency path.

Uniform subcriticality is also not necessary. Random environments can contain arbitrarily large low-noise regions, and then proving sufficient decay of connectivity may require a separate multiscale analysis, as in the cited work. Conversely, if the disagreement comparison is supercritical, failure of this method does not prove nonergodicity of the spin system.

Finally, the method naturally controls local coupling and invariant-law uniqueness. Spectral gaps, logarithmic Sobolev inequalities, or sharp finite-volume mixing generally require additional quantitative arguments beyond mere extinction of disagreement paths.

## Sources

- Gielis, Maes and Vande Velde, *Annales de l'Institut Henri Poincare, Physique theorique* 70 (1999), Sections 4.1.1-4.1.2, Propositions 1-2, Theorems 1-2. Full primary text: https://www.numdam.org/item/AIHPA_1999__70_5_445_0/.
- The closely related earlier spin-flip treatment is G. Gielis and C. Maes, "Percolation techniques in disordered spin flip dynamics: relaxation to the unique invariant measure," *Communications in Mathematical Physics* 177 (1996), 83-101.
