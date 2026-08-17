---
method_id: maximal-local-coupling-nonmonotone-potts
title: Maximal local coupling for nonmonotone Potts dynamics
category: coupling
targets:
  - coupling-agreement
  - mixing
model_scope: Nonmonotone finite-volume Potts/Glauber dynamics where local conditional update laws can be maximally coupled
source_status: primary-checked
primary_source: Kyunghoo Mun, Dynamical Phase Transition for the homogeneous multi-component Curie-Weiss-Potts model, Journal of Statistical Physics 193 (2026), Article 16
primary_pinpoint: Theorem 1; Section 3.1, Lemmas 3.2–3.3; Section 3.2, Lemmas 3.6, 3.7 and 3.10
primary_url: https://doi.org/10.1007/s10955-026-03571-9
application_source: same as primary source
application_pinpoint: Theorem 1 and Sections 3.1–3.2
application_url: https://doi.org/10.1007/s10955-026-03571-9
wiki_candidate: yes
---

# Maximal local coupling for nonmonotone Potts dynamics

## Criterion

For two configurations $\sigma,\tau$ of a single-site heat-bath dynamics, choose the same update site $v$ in both copies. Let

\[
q_{v,\sigma},\qquad q_{v,\tau}
\]

be the two conditional laws for the new spin at $v$. A **maximal local coupling** chooses the two new spins so that

\[
\mathbb P(\sigma'_v\neq\tau'_v)
   =\|q_{v,\sigma}-q_{v,\tau}\|_{\mathrm{TV}},
\]

which is the smallest mismatch probability possible for any coupling of these two update laws.

Mun uses exactly this greedy/maximal coupling for the homogeneous multi-component Curie--Weiss--Potts model. Lemma 3.2 records maximal-coupling optimality, and Lemma 3.3 expresses the expected one-step Hamming-distance drift through the change of the local update map. The direct local estimate is then combined with the aggregate path method of Section 3.2. In the subcritical regime $\beta<\beta_s(q)$, Lemmas 3.6, 3.7 and 3.10 provide the required aggregate contraction, yielding Theorem 1: mixing time of order $N\log N$.

## Mechanism

For an Ising system, monotonicity often supplies a canonical common-uniform update: ordered inputs remain ordered and disagreements can be counted. With $q\ge3$ Potts spins there is no comparable scalar order carrying all spin proportions. Mun explicitly notes that the monotone Ising coupling does not extend to this setting.

The replacement optimizes each local update probabilistically rather than order-theoretically. At an update site, all common mass of the two conditional spin distributions is matched; only their total-variation remainder can produce a disagreement. This converts local coupling quality into an explicit function of the difference between the two macroscopic proportion vectors.

A second ingredient is important. Maximal local coupling alone need not give worst-case contraction for every adjacent pair. Instead of requiring a direct path-coupling inequality everywhere, the aggregate-path construction joins macroscopic states by a path along which the cumulative change of the update map is controlled. The proof therefore has two layers: optimal **local** agreement of nonordered conditional laws, followed by a global geometric estimate on how those local total-variation discrepancies accumulate.

This is distinct from the live block-resampling method, which enlarges an update to a whole block, and from ordinary path coupling, where contraction on neighboring configurations is itself the decisive hypothesis.

## Representative IPS use

The application is heat-bath Glauber dynamics for the homogeneous multi-component Curie--Weiss--Potts model. Below the spinodal threshold $\beta_s(q)$, the maximal update coupling plus aggregate-path estimates gives rapid mixing $O(N\log N)$. The method is especially natural for nonmonotone finite-spin systems whose conditional distributions are explicit enough that their total-variation distance can be controlled through a low-dimensional order parameter.

## Limitations

A maximal coupling always exists for two probability laws, but that fact alone does not imply contraction. One must still estimate how the local conditional laws vary with the surrounding configuration and aggregate those estimates globally. The cited application is mean-field and exploits the finite-dimensional vector of color proportions. In spatial models, local TV distances can depend on complicated boundary geometry, and maximal local coupling may reproduce a Dobrushin-type high-temperature condition rather than improve it. The argument proves finite-volume mixing in the stated Potts regime, not infinite-volume uniqueness by itself.

## Sources

Kyunghoo Mun, *Dynamical Phase Transition for the homogeneous multi-component Curie-Weiss-Potts model*, Journal of Statistical Physics **193** (2026), Article 16. Theorem 1 is the subcritical $O(N\log N)$ mixing result. Section 3.1 defines the greedy coupling; Lemma 3.2 gives maximal-coupling optimality and Lemma 3.3 gives its Hamming-distance drift. Section 3.2, especially Lemmas 3.6, 3.7 and 3.10, supplies the aggregate-path contraction used to complete the proof. DOI: https://doi.org/10.1007/s10955-026-03571-9
