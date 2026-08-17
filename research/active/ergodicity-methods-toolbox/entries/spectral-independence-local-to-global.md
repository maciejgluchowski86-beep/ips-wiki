---
method_id: spectral-independence-local-to-global
title: Spectral independence and local-to-global influence
category: spatial-mixing
targets:
  - spectral-gap
  - mixing
model_scope: Finite spin/Gibbs distributions and Glauber dynamics on graphs, especially hard-core and antiferromagnetic spin systems
source_status: primary-checked
primary_source: Nima Anari, Kuikui Liu, and Shayan Oveis Gharan, Spectral Independence in High-Dimensional Expanders and Applications to the Hardcore Model, SIAM Journal on Computing 53 (2024), FOCS20-1--FOCS20-37.
primary_pinpoint: Definitions 1.1-1.2; Theorem 1.3; Theorems 1.5-1.6 and their proof of Theorem 1.3; Theorem 1.8 and Remark 1.10 for hard-core
primary_url: https://doi.org/10.1137/20M1367696
application_source: Nima Anari, Kuikui Liu, and Shayan Oveis Gharan, Spectral Independence in High-Dimensional Expanders and Applications to the Hardcore Model.
application_pinpoint: Theorem 1.8 and Remark 1.10, hard-core Glauber dynamics below the tree uniqueness threshold
application_url: https://arxiv.org/abs/2001.00303
wiki_candidate: yes
---

# Spectral independence and local-to-global influence

## Criterion

For a spin distribution \(\mu\), form a matrix \(\Psi_\mu\) whose off-diagonal entries measure how conditioning one coordinate changes the marginal of another. Anari--Liu--Oveis Gharan call \(\mu\) spectrally independent when the largest eigenvalue of this signed influence matrix is bounded, and require analogous bounds for **all feasible conditional distributions**. In their notation one has parameters \((\eta_0,\ldots,\eta_{n-2})\) controlling successive conditionings. Theorem 1.3 gives a quantitative lower bound on the spectral gap of the natural single-site Glauber dynamics in terms of these spectral-independence parameters.

The reusable criterion is therefore not a maximum row-sum bound but an operator/spectral bound on conditional influence matrices. If the relevant \(\eta_i\)'s remain controlled as coordinates are pinned, the Glauber chain has a positive quantitative spectral gap and hence rapid \(L^2\) relaxation; standard finite-state estimates then convert this to total-variation mixing bounds.

## Mechanism

The proof is a local-to-global spectral argument. A spin distribution is encoded as a weighted high-dimensional simplicial complex. Theorem 1.5 shows that spectral independence of every conditional measure implies spectral expansion of every link of this complex, with better link expansion at lower dimension. A high-dimensional local-to-global theorem, quoted as Theorem 1.6, then converts these linkwise spectral estimates into a gap for the top-dimensional down-up walk. In the spin encoding that walk is exactly Glauber dynamics, yielding Theorem 1.3.

This differs from classical Dobrushin contraction. Dobrushin typically controls an absolute row sum of influences and obtains direct metric/coupling contraction. Spectral independence can exploit cancellation and global matrix structure invisible to a row-sum norm. It also differs from Dobrushin--Shlosman spatial mixing: the input here is a spectral statement about pairwise conditional influences on a finite graph, and the proof proceeds through high-dimensional local-to-global expansion rather than geometric block boundary screening.

## Representative IPS use

For the hard-core model, Theorem 1.8 proves uniform spectral independence, including after conditioning, throughout the tree uniqueness regime \(\lambda<(1-\delta)\lambda_c(\Delta)\). Combined with Theorem 1.3, this gives polynomial-time Glauber mixing up to the uniqueness threshold on arbitrary bounded-degree graphs; Remark 1.10 records the resulting quantitative mixing estimate.

Later work strengthens the local-to-global machinery to optimal \(O(n\log n)\) mixing and extends the method to general antiferromagnetic two-spin systems, colorings, and matchings. Those refinements are related toolbox items, but the original spectral-independence criterion already isolates the essential method: bound conditional influence spectra, then transfer those local spectral bounds to the global Glauber chain.

## Limitations

Spectral independence must be stable under arbitrary feasible pinning; a bound only for the unconditioned measure is insufficient for the theorem. Establishing the influence eigenvalue bound can be the hard model-specific step and often uses correlation decay, recursions on trees, or complex-analytic estimates. The original theorem gives polynomial rather than automatically optimal \(O(n\log n)\) mixing. The method is formulated for finite Gibbs/sampling problems; passing to an infinite-volume IPS requires separate finite-volume uniformity and exhaustion arguments. Finally, a small spectral radius need not imply pathwise contraction of any particular coupling, so this method should not be conflated with coupling agreement.

## Sources

- Anari, Liu, Oveis Gharan, *Spectral Independence in High-Dimensional Expanders and Applications to the Hardcore Model*, Definitions 1.1--1.2, Theorems 1.3, 1.5, 1.6, and Theorem 1.8, https://doi.org/10.1137/20M1367696; accessible preprint https://arxiv.org/abs/2001.00303.
