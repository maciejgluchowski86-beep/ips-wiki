---
method_id: toom-error-graph-expansion-pca
title: Toom error-graph expansion for low-noise PCA
category: graphical-duality
targets:
  - convergence
  - mixing
model_scope: Low-noise probabilistic cellular automata obtained from eroding monotone binary tessellations without memory
source_status: primary-checked
primary_source: Augustin de Maere and Lise Ponselet, Exponential Decay of Correlations for Strongly Coupled Toom Probabilistic Cellular Automata, Journal of Statistical Physics 147 (2012), 634-652
primary_pinpoint: Theorem 1; Theorem 2; Sections 3-6, especially Section 5 and equations (16), (23)-(26)
primary_url: https://doi.org/10.1007/s10955-012-0487-9
application_source: same as primary source
application_pinpoint: Theorem 1 and Theorem 2; North-East-Center and other eroding monotone binary tessellations discussed in Sections 1-2
application_url: https://arxiv.org/abs/1110.1540
wiki_candidate: yes
---

# Toom error-graph expansion for low-noise PCA

## Criterion

Consider a probabilistic cellular automaton obtained by adding noise to a monotone binary tessellation without memory. Assume the deterministic update rule is nonconstant and satisfies Toom's erosion criterion. De Maere and Ponselet impose two quantitative perturbation conditions: an update that disagrees with the deterministic prescription has probability at most `epsilon` (A1), while changing a spin without changing that prescription perturbs the relevant local transition probability by at most a relative factor `alpha` (A2).

Their Theorem 1 states that there are `alpha_* > 0` and a decreasing positive threshold `epsilon_*(alpha)` such that, for `alpha < alpha_*` and `epsilon < epsilon_*(alpha)`, every initial law in the plus-phase basin `B^(+)(K,epsilon')`, with `epsilon' < epsilon_*(alpha)`, converges exponentially to the plus extremal invariant law. Quantitatively, for local-continuous observables the error is bounded by a constant times the one-site oscillation seminorm times `sigma^n` for some `sigma < 1`. Theorem 2 then gives exponential temporal correlation decay for finite-support observables; the corollary after Theorem 1 gives exponential spatial correlation decay.

## Mechanism

The proof expands the dependence of an observable backwards along **influence paths**. In a region where the deterministic prescription is in the plus phase, assumption A2 gives a small decoupling factor. A path becomes dangerous when it encounters a minus spin, because pure-phase decoupling no longer suffices.

At every such encounter the proof attaches a **Toom graph**. Section 5 reformulates Toom's truss construction as a space-time graph rooted at the observed minus spin. The graph traces that spin backwards through deterministic propagation until it identifies a distinguished set of actual update errors. Each identified error costs a factor at most `epsilon` by A1. Erosion supplies the crucial geometry: the graph cannot grow without producing proportionally many identified errors, while the number of possible graphs grows only exponentially in their number of edges. Thus sufficiently small noise makes the energetic error factors beat the combinatorial graph entropy.

Sections 5-6 combine collections of these graphs with the influence-path expansion. The resulting estimate simultaneously pays an `alpha` factor for good-phase path portions and error factors for bad-phase portions, yielding a geometric series uniform in time. This is the load-bearing object that turns deterministic erosion into quantitative stochastic relaxation.

## Representative IPS use

The paper applies the construction to low-noise perturbations of any memoryless monotone binary tessellation satisfying Toom erosion, including the North-East-Center PCA. It proves exponential attraction to the chosen plus-phase invariant law from a nontrivial basin and exponential space-time correlation decay of that law.

The theorem is deliberately phase-specific. In symmetric low-noise Toom models there can also be a minus extremal invariant law, so exponential convergence inside the plus basin is not a uniqueness theorem for the whole PCA.

## Limitations

The method uses monotonicity of the deterministic cellular automaton, Toom's geometric erosion criterion, low error probability, and the additional pure-phase decoupling assumption A2. The paper restricts to tessellations without memory. Its graphical expansion is more structured than ordinary disagreement percolation: the argument must reconstruct enough improbable historical errors behind each bad spin, not merely dominate a disagreement path by a subcritical independent process. It is also not a generic Peierls proof of Gibbs uniqueness; the graphs live in space-time and are inserted into a dynamical influence expansion to prove convergence and correlation decay.

## Sources

Primary source: Augustin de Maere and Lise Ponselet, *Exponential Decay of Correlations for Strongly Coupled Toom Probabilistic Cellular Automata*, Journal of Statistical Physics 147 (2012), 634-652, DOI 10.1007/s10955-012-0487-9. Theorem 1 is stated on arXiv version p. 6; Theorem 2 on p. 7; the influence-path/graph mechanism is developed in Sections 3-6, with Toom graphs in Section 5 and the graph-weight estimates in Sections 5-6. Stable preprint: https://arxiv.org/abs/1110.1540.