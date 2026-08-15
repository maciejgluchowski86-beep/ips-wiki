# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Graduate Student B: idle after programme closure

Graduate Student A: idle after full-text literature comparison

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: `meetings/006-sudbury-correction-and-front-reduction.md`

## Target

Original target: prove finite-seed local convergence for every `lambda>0`.

Programme status: **closed** at Group Meeting 006 on expected-value/opportunity-cost grounds after applying the principal's standing novelty standard.

The all-parameter BABP problem remains open and worthwhile. The project is not claiming it is intractable in principle.

## Retained verified mathematics

### `BABP-EDGE-001`

At `lambda=1/40`, `k=10`, there is a bounded rational finite-window corrector with

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

for all `2048` edge/exterior states. The certificate and its ballistic liminf/limsup consequences were independently audited in commit `d1ef2ca`.

Under the standing novelty standard, this is **not counted as a project research result**. Sudbury's finite-window submartingale construction is defined for arbitrary window size and Lemma 7 gives free extension in window size; the ten-site certificate is a correct larger-window instance of that classical method.

### `BABP-CONV-001`

For fixed `lambda>0`, a bounded finite-window corrector with uniform statewise positive drift implies local convergence from every finite nonempty deterministic initial set. The project has a self-contained tagged-gap proof, independently accepted in commits `abb05f6` and `1aeb5a5`.

The implication itself is classical prior work: Sudbury (1999), immediately before Theorem 7, states that the Neuhauser--Sudbury (1993) finite-seed argument relies on a suitable submartingale and proceeds unchanged once his Section 3 extends that condition to `0.0347`.

Combining the two verified claims gives mathematically valid convergence at `lambda=1/40`, but this quantitative larger-window extension is **not counted as a project result** under the standing novelty standard.

## Source-verified Sudbury identification

Sudbury (1999), Section 3, is the same finite-window robust edge-submartingale framework. After reflection:

- `m=k`;
- his `m`-block is the project edge word `u`;
- his one unresolved end-value is `z`;
- his correction `S_i` is `phi`;
- his local gain `a_i+sum_j q_ij(S_j-S_i)` is `D_{k,lambda}`.

His Maxwell's-demon end-value may depend on the current block state, and Lemma 5 requires one correction vector to work for every assignment of end-values. Since each row depends only on its own one-bit end-value, this is exactly the statewise both-`z` robust condition.

Lemma 7 gives free extension from any window `m_1` to every larger `m_2` by ignoring the additional sites. Table 2 reports trial-and-error values through `m=8`, `lambda_m=0.0347`, without claiming exact criticality. The project `k=8` crossing `0.0346195434755...` is a refinement of the same eight-site optimization.

## Dormant structural reduction

Student B's `students/student-b/003-front-gap.md`, commits `5c357ef` and `1365840`, gives target-relevant structural mathematics that is preserved for possible future return.

For each fixed `lambda>0`, let `I_lambda` be the invariant laws of the environment seen from the rightmost particle. The note establishes, for research-branch use,

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1),
$$

and every invariant front law satisfies

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Thus the finite-window method reaches a fixed parameter exactly if every invariant front law has positive current. Every Cesaro front law selected from a singleton has positive current for every `lambda>0`; the only possible obstruction is an additional hostile invariant semi-infinite-tail phase.

This reduction does not prove the all-parameter theorem. The remaining problem is a difficult infinite-volume phase-selection/uniqueness question. The obvious reset coupling is circular, the `lambda=0` endpoint has many absorbing hard-core phases, and the entropy/current route still lacks a no-incoming-flux theorem from particle-index infinity.

The pre-existing `students/student-b/assignment-004.md` is superseded by programme closure and should not be executed.

## Closure rationale

The programme is closed because, after applying the principal's standing novelty standard, it has **no completed project research result**. Its only potentially qualifying remaining target is the all-parameter structural theorem, while the current route has reached a difficult semi-infinite invariant-phase problem without a concrete proof mechanism.

Student A's opportunity-cost reconnaissance had ranked the residual positive-rates/noisy-East problem above BABP unless BABP produced a genuinely new small-parameter theorem rather than only reconstructing or instantiating the historical mechanism. Under the standing novelty standard, that condition is now met in the negative.

The noisy-East candidate has stronger group-specific leverage and a cheap exact first falsification test through a two-site agreed-block wall under the canonical coupling. Sunk effort is not a reason to continue BABP.

## Programme outcome

Closed without a new project result under the standing novelty standard.

Useful retained assets:

- audited exact ten-site BABP certificate;
- audited self-contained tagged-gap convergence proof;
- exact source mapping to Sudbury's finite-window construction;
- dormant infinite-front reduction and hostile-phase formulation.

## Wiki freeze

Keep the live wiki frozen. No BABP `proved here` update is warranted.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `students/student-a/writeup-001-literature-and-manuscript-plan.md`, Sudbury (1999), `students/student-b/003-front-gap.md`, `students/student-a/recon-001-open-problem-scan.md`, and `meetings/006-sudbury-correction-and-front-reduction.md`.

Consecutive no-narrowing meetings: 0

## Direction

`close`.