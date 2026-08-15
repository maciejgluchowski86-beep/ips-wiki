# Literature note

## Target

One-dimensional biased annihilating branching process (BABP), finite nonempty initial particle set, convergence to Bernoulli equilibrium for every branching parameter `lambda>0`.

Use

$$
q=\frac{\lambda}{1+\lambda},
\qquad
p=\frac1{1+\lambda}
$$

for particle/vacancy density versus the canonical patch-paper convention.

## Current recorded state of the art

### Neuhauser--Sudbury (1993)

Claudia Neuhauser and Aidan Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38.

Foundational BABP stationary-law and spreading results.

### Mountford (1993) and Sudbury (1999)

The finite-seed convergence theorem was known for `lambda>1/3`; Sudbury's 1999 paper

Aidan Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854,

improved the range to the published numerical boundary `0.0347`.

The accessible publisher record confirms the convergence threshold, the submartingale framing and edge-speed bounds. The full body has not been obtained, so literal identity of Sudbury's internal calculation with the project's `k=8` LP remains unverified.

### Martinelli--Shapira--Toninelli (2025)

Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025).

Relevant items checked in the primary arXiv text:

- Corollary 2.9: every stationary measure of one-dimensional BABP is a convex combination of the completely healthy configuration and Bernoulli equilibrium;
- Theorem 5.2: DFP exponential ergodicity for every `lambda>0`;
- Application 1: BABP from any finite nonempty seed has linear particle-number growth for every `lambda>0`;
- Remark 5.4: finite-seed convergence is recorded as known for `lambda>1/3` by Mountford and improved to `lambda>0.0347` by Sudbury;
- Application 2 / Remark 5.5: convergence from Bernoulli and certain inhomogeneous product initial laws.

The new project's corrector-to-convergence proof does **not** use the 2025 particle-number growth theorem. Corollary 2.9 is used for stationary-law classification.

### Jahnel--Köppl (2026): stationary weak limit points

Benedikt Jahnel and Jonas Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026).

Theorem 2.5 states that for a one-dimensional IPS satisfying assumptions `(L1)` and `(R1)--(R3)` with an exponential profile, every weak limit point of the measure-valued dynamics is stationary.

BABP fits the theorem directly for every fixed `lambda>0`:

- finite local state space `{0,1}`;
- single-site updates, hence uniformly bounded update diameter `(R1)`;
- each site's total flip rate is bounded by `2 max(1,lambda)`, giving `(L1)`;
- the rate at a site depends only on its two nearest neighbours, so the influence kernel has finite range and satisfies `(R3)` for an exponential profile; the exponential profile satisfies `(R2)` by the triangle inequality.

This is a cleaner current source for the subsequential-limit invariance input than relying on inaccessible details of Mountford / Ramírez--Varadhan.

Audit 003 is tasked with independently checking this theorem interface.

## Current project claims and literature boundary

### `BABP-EDGE-001` — verified

At `lambda=1/40`, a ten-site statewise corrector has exact drift `1033/40000000>0` and yields verified two-sided liminf/limsup ballistic edge bounds. Independent hostile audit: commit `d1ef2ca`.

This is not a convergence theorem by itself.

### `BABP-CONV-001` — claimed

Student B assignment 002 proves, and the Professor has independently reconstructed, the following candidate theorem:

> existence of a uniformly positive **statewise** finite-window BABP edge corrector implies local convergence from every finite nonempty deterministic initial set to Bernoulli equilibrium.

The proof controls internal vacant gaps via the same corrector, derives exponential gap tails and local nonescape, then uses Jahnel--Köppl Theorem 2.5 and Martinelli--Shapira--Toninelli Corollary 2.9.

Combining the bridge with `BABP-EDGE-001` gives claimed finite-seed convergence at `lambda=1/40=0.025`, below the `0.0347` range recorded in Martinelli--Shapira--Toninelli Remark 5.4.

This is **not yet a verified novelty claim**. Two independent correctness audits are pending, and a later publication-level successor/citation search is still required before any manuscript claim that this is the current best finite-seed range.

## Other background

Lloyd--Sudbury (1997) supplies quasi-duality/thinning algebra; Sudbury (1997) supplies qualitative convergence background for translation-invariant initial laws. The DFP change-of-basis route is currently demoted because the finite-test cylinder has no probability-law DFP representation and its exact finite-window signed representation has exponentially growing coefficient norm.

## Canonical project source

The principal's paper `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for patch construction/proofs. Its BABP subsection and discussion record finite-seed BABP as an unresolved hard-model problem at manuscript time. The current BABP proof does not use patch contraction.

## Successor / novelty status

At programme initialization, a targeted search found no post-2025 theorem removing the recorded `0.0347` finite-seed restriction. This is not yet publication-level novelty verification.

Before promoting `BABP-CONV-001` beyond verified project status or drafting a publication claim, search 2025--2026 successors, citations to Sudbury and Martinelli--Shapira--Toninelli, alternate BABP/jumping-voter terminology, theses/preprints, and any results on finite initial configurations.