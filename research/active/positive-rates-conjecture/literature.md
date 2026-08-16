# Literature and source map

This file is a working map, not a substitute for reading the primary sources.

## Primary target sources

### Głuchowski--Menz (2026)

Maciej Głuchowski, Georg Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*, Electronic Communications in Probability 31 (2026), DOI `10.1214/26-ECP767`, arXiv:`2508.08459`.

Load-bearing items:

- Definition of simple IPS: one-dimensional, homogeneous, binary, one-sided nearest-neighbour.
- PRC for simple IPS: every simple IPS with positive rates is ergodic.
- Parameterization by `P_0(1|11), P_0(1|10), P_0(1|01), P_0(1|00)`.
- Time-scaling reduction and state-symmetry discussion inherited from the companion article.
- Theorem 3.1: the long-lived-state criterion `delta < sqrt(2) beta`.
- Discussion after Theorem 3.1: the remaining unproved region lies next to the noisy-East boundary.

This paper is authoritative for the fixed target formulation in this programme.

### Głuchowski--Menz (2025)

Maciej Głuchowski, Georg Menz, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, Journal of Statistical Physics 192 (2025), article 6.

Load-bearing items for this programme:

- time-scaling lemma;
- classification/reduction of simple IPS;
- Chapter/Section 7 sufficient ergodicity regions;
- published Corollary 7.2, whose actual theorem statement is used in the source-corrected residual chamber.

The previous noisy-East programme found a prose inequality mismatch between the 2026 summary and the 2025 published theorem. Whenever a boundary inequality matters, use the primary theorem/proof rather than the summary prose.

## Previous project work that remains relevant

Branch `research/noisy-east-positive-rates`:

- `research/active/noisy-east-positive-rates/state.md`;
- `research/active/noisy-east-positive-rates/proof-spine.md`;
- `research/active/noisy-east-positive-rates/students/student-c/001-two-site-wall.md`;
- `research/active/noisy-east-positive-rates/students/student-c/002-uniform-three-site-wall.md`;
- `research/active/noisy-east-positive-rates/notes/professor-wall-test-verification.md`;
- `research/active/noisy-east-positive-rates/meetings/001-two-site-wall-review.md`;
- `research/active/noisy-east-positive-rates/meetings/002-three-site-gap-and-wall-closure.md`.

Use this branch as negative knowledge about fixed finite walls, not as a template that forces the new programme back into the same route.

## Canonical project technical source

`paper/`, *Patch representations and convergence for facilitated spin systems*.

For patch factorization, successful-interaction skeletons, conditional averaging, confined-interaction identities, and backward chains of outgoing patches, the paper is canonical. These tools may overlap conceptually with the principal's remembered last-successful-interaction route. They should be used if they genuinely shorten or verify the needed decomposition, but the new programme must not assume that the old route is already contained in the patch theorem.

Relevant canonical ingredients likely worth checking:

- exact signed monomial/Feynman--Kac dual;
- successful/transmitting interaction skeleton;
- patch factorization;
- confined-interaction identity;
- backward chains of outgoing patches and their exponential factors;
- finite propagation / zero-boundary restrictions.

## East-model comparison sources

The 2026 target paper points to standard East results showing that the hard East model is non-ergodic because of the all-zero extremal state, but is otherwise strongly mixing from configurations with sufficiently many facilitating states and has a positive spectral gap under its nontrivial equilibrium law.

For any perturbative/noisy-East argument, identify and cite the exact East theorem used rather than relying on the qualitative summary. The first students should build an exact bibliography if East front/regeneration or out-of-equilibrium results become load-bearing.

## Classical positive-rates context

Larry Gray's positive-rates theorem for attractive nearest-neighbour spin systems in one dimension is the main classical comparison. It is useful for understanding what monotonicity buys and what is missing in the non-attractive residual simple-IPS problem. Do not import an attractive argument without checking which order property actually survives.

## Literature discipline for the current programme

The target is fixed, so literature review is not a gate for whether to work on it. It remains a gate for:

- whether a proposed intermediate theorem is already known;
- whether a claimed new finite-box/density estimate is classical under another name;
- whether a purported East perturbation theorem already exists;
- whether a new representation is actually just standard graphical duality.

The previous voter and BABP programmes both produced correct mathematics that failed contribution audit because the source already contained the mechanism. Check closest prior work before promoting an intermediate theorem as new.
