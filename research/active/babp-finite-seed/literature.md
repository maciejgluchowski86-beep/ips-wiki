# Literature note

## Target

One-dimensional biased annihilating branching process (BABP), finite nonempty initial particle set, convergence to Bernoulli equilibrium for every `lambda>0`.

Use particle variables with

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x,
\qquad
q=\frac{\lambda}{1+\lambda}.
$$

## Neuhauser--Sudbury (1993)

Claudia Neuhauser and Aidan Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38.

Foundational stationary-law/spreading work. Sudbury (1999) states that their Section 5 stationary-state argument used existence of a suitable edge submartingale in the then-known `lambda>1/3` range.

The full body of Neuhauser--Sudbury Section 5 has not yet been inspected in this project. It is now the only important remaining historical comparison for the **proof architecture** of the project's tagged-gap reproof; it is not a dependency of the current mathematics.

## Sudbury (1999): full-text comparison completed

Aidan Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854.

The full text is now available and settles the provenance questions that were previously open.

### Exact finite-window identification

Sudbury uses the same BABP normalization as the project. In Section 3 he follows an outer particle, records an `m`-site block and one additional end-value, and corrects the edge score by a vector `S` indexed by the block state. After reflection:

- `m=k`;
- the block state is `u`;
- the end-value is `z`;
- `S_i=phi(u)`;
- the local gain `a_i+sum_j q_ij(S_j-S_i)` is `D_{k,lambda}(u,z;phi)`.

The Maxwell's-demon formulation permits the end-value to depend on the current block state. Lemma 5 requires one correction vector to give a submartingale for every possible assignment of these end-values. Since the drift in state `i` depends only on the one bit assigned to `i`, this is exactly the robust statewise condition over both `z=0,1` for every `u`.

Lemma 7 states that if a suitable submartingale exists for window `m_1`, then one exists for every `m_2>m_1`; the proof simply uses the `m_1` correction on the first `m_1` coordinates and treats the next coordinate as the arbitrary end-value. This is the historical version of the project's window-nesting lemma.

Table 2 reports trial values

```text
m    lambda_m
2    0.2653
3    0.1832
4    0.1154
5    0.0805
6    0.0589
7    0.0443
8    0.0347
```

Sudbury explicitly says these values were found by trial and error and does not claim the displayed decimals are exact critical values. The project value `0.0346195434755...` therefore refines the same eight-site optimization problem.

### Corrector-to-convergence implication is prior art

Immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used existence of a suitable submartingale in their stationary-state argument, that his Section 3 extends this condition from `1/3` to `0.0347`, and that the argument of their Section 5 then proceeds unchanged. Theorem 7 gives finite-seed convergence in the resulting range.

Therefore the implication “suitable robust finite-window edge submartingale => finite-seed convergence” is classical. The project `BABP-CONV-001` is a verified self-contained reproof/formulation, not a new general criterion.

## Current verified project contribution

### `BABP-EDGE-001`

At `lambda=1/40`, `k=10`, an exact rational corrector has statewise drift

$$
\frac{1033}{40000000}>0.
$$

Independent hostile audit: commit `d1ef2ca`.

This is a new exact range certificate inside Sudbury's classical finite-window framework.

### `BABP-CONV-001`

The project has a self-contained tagged-gap proof that the statewise corrector condition implies finite-seed local convergence. Correctness was independently accepted in commits `abb05f6` and `1aeb5a5`.

The implication itself is prior art by the Sudbury/Neuhauser--Sudbury chain above. The project proof remains useful for self-contained exposition and for making the exact statewise hypothesis transparent. Its proof-architecture novelty is unresolved pending Neuhauser--Sudbury (1993), Section 5.

Together, the exact certificate and the classical implication prove finite-seed convergence at `lambda=1/40=0.025`, below Sudbury's published `0.0347` range.

## Martinelli--Shapira--Toninelli (2025)

Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461.

Relevant items:

- Corollary 2.9: stationary one-dimensional BABP laws are convex combinations of the empty state and Bernoulli equilibrium;
- Theorem 5.2: all-parameter DFP exponential ergodicity;
- Application 1: finite-seed BABP particle number grows linearly for every `lambda>0`;
- Remark 5.4: the historical finite-seed range is recorded at `0.0347`;
- Application 2 / Remark 5.5: convergence from Bernoulli and certain inhomogeneous product initial laws.

Application 1 is now used in the infinite-front analysis to prove positive current for every singleton-selected Cesaro front law. It is not used in the self-contained corrector-to-convergence bridge.

## Jahnel--Köppl (2026)

Benedikt Jahnel and Jonas Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817.

Theorem 2.5 supplies stationarity of weak limit points for one-dimensional IPS under `(L1)` and `(R1)--(R3)` with exponential influence. BABP satisfies these directly by bounded single-site rates and nearest-neighbour influence. This is the source-checked stationary-limit input used in the project proof.

## Current all-parameter literature boundary

No checked source currently removes the finite-seed restriction for every `lambda>0`. The active project reduction is no longer a claim of a new finite-window method; it asks whether the infinite environment seen from the front has hostile invariant semi-infinite-tail phases.

Student B's `003-front-gap.md` reduces positive finite-window drift at fixed `lambda` to positive current for **every** invariant front law. Every front law selected by the singleton has positive current; the unresolved issue is phase selection/uniqueness at the semi-infinite tail.

## Other background

Lloyd--Sudbury (1997) supplies quasi-duality/thinning algebra; Sudbury (1997) supplies qualitative convergence background for translation-invariant initial laws. The DFP black-box route remains demoted for finite-seed convergence because the finite-test signed representation has an exponentially growing coefficient norm.

The principal's canonical patch paper remains authoritative for patch construction/proofs but is not the active BABP mechanism.