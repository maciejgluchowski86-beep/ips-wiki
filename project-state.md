# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Active scientific direction

**1D BABP from a finite seed — active.**

- Branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Target: prove local convergence from every finite nonempty seed for every `lambda>0`.
- Latest meeting: `research/active/babp-finite-seed/meetings/006-sudbury-correction-and-front-reduction.md`, `state_narrowed: yes`.
- Active development: Graduate Student B, assignment `students/student-b/assignment-004.md`.
- Graduate Student A: idle after full-text literature comparison.

## Verified project mathematics

`BABP-EDGE-001` is verified by audit `d1ef2ca`: at

$$
\lambda=\frac1{40},\qquad k=10,
$$

a bounded rational statewise corrector has exact minimum drift

$$
\frac{1033}{40000000}>0.
$$

`BABP-CONV-001` is mathematically verified by independent reviews `abb05f6` and `1aeb5a5`: a uniformly positive **statewise** finite-window corrector implies local convergence from every finite nonempty deterministic seed. The stable self-contained proof is `research/results/babp-finite-seed-convergence.md`.

Consequently BABP at `lambda=1/40=0.025` converges locally from every finite nonempty deterministic seed to Bernoulli equilibrium of density `1/41`.

## Sudbury full-text correction

The full text of Sudbury (1999) materially changes the novelty assessment and corrects the framing used in Meetings 003--005.

Sudbury's Section 3 is the same finite-window robust edge-submartingale framework. After reflection:

- his window size `m` is the project `k`;
- his `m`-block is the project edge word `u`;
- his single unresolved end-value is the project exterior bit `z`;
- his correction `S_i` is the project `phi`;
- his local gain `a_i+sum_j q_ij(S_j-S_i)` is the project drift `D_{k,lambda}`.

The Maxwell's-demon formulation is exactly the robust exterior-bit issue: the end-value may depend on the current block state, and Lemma 5 requires one correction vector to work for every assignment of those one-bit end-values. Because the drift in each row depends only on that row's end-value, this is equivalent to imposing the inequality for both `z=0,1` in every state.

Sudbury's Lemma 7 gives free extension from any window `m_1` to every larger `m_2` by ignoring the extra sites. Table 2 reports the trial-and-error values through `m=8`, `lambda_m=0.0347`, and explicitly does not claim the decimal is an exact critical value. The project crossing `0.0346195434755...` therefore refines the same eight-site optimization.

Immediately before Theorem 7, Sudbury states that the Neuhauser--Sudbury (1993) stationary-state argument relied on existence of a suitable submartingale, that his Section 3 extends that condition from the old `1/3` range to `0.0347`, and that their Section 5 argument then proceeds unchanged.

**Correct contribution statement:** the finite-window mechanism and the corrector-to-convergence principle are prior art. The project contribution is the exact audited `k=10`, `lambda=1/40` range certificate inside Sudbury's framework, together with a self-contained modern convergence proof. No novelty claim is made for the tagged-gap proof architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

The mathematical verification statuses of `BABP-EDGE-001` and `BABP-CONV-001` are unchanged; this is a provenance/priority correction.

## Current all-parameter bottleneck

Student B's `003-front-gap.md`, commits `5c357ef` and `1365840`, validates the infinite-front reduction after adding the missing cylinder-core argument.

For fixed `lambda>0`, let `I_lambda` be the invariant laws of the environment seen from the right edge. Then

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

Thus the exact fixed-parameter corrector target is

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda.
$$

Every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`, by the all-parameter finite-seed cardinality-growth theorem plus reflection symmetry. Therefore the only possible obstruction to the finite-window route is an additional invariant semi-infinite-tail phase not selected from finite seeds.

The current first unresolved edge is to **exclude hostile invariant front phases**. Front uniqueness is sufficient but stronger than necessary. A direct theorem that every invariant front law has positive current would also close the all-parameter route.

## Opportunity cost

The full Sudbury comparison lowers the standalone novelty of the `lambda=1/40` result: it is a strict range extension inside a classical mechanism, not a new mechanism or new general convergence criterion.

BABP nevertheless continues for one further substantial block because the all-parameter problem remains open and the invariant-front reduction sharply localizes the obstruction. If Student B's hostile-phase/uniqueness attack produces no theorem-level narrowing, the next group meeting must explicitly compare continuation against the noisy-East reserve rather than continue by increasing finite windows.

## Neuhauser--Sudbury (1993), Section 5

Worth obtaining from the principal if conveniently available. Its role is publication attribution: it can settle whether the project's tagged-gap nonescape proof is already present in substance. It is not a dependency of the verified range extension or the current all-parameter proof spine.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. The prior-art correction should be settled in the research note before any `proved here` BABP wiki update.

## Stable surface

`research/claim-registry.md` records:

- `BABP-EDGE-001`: `verified`, audit `d1ef2ca`;
- `BABP-CONV-001`: `verified` for mathematical correctness, reviews `abb05f6` and `1aeb5a5`, with the implication explicitly identified as classical after the Sudbury full-text comparison.

The stable theorem note is `research/results/babp-finite-seed-convergence.md`.

## Closed programmes and routes

Closed programmes remain closed: quadratic-Hessian; Fresnel integrability; Navier--Stokes stochastic cascade; Strong-KPP uniqueness; supercritical dissipative SQG; long-maturity marked branching; Gaussian bridge coarsening; and the 1D hard FA-1f finite-seed programme based on the centered-transform / unnormalized patch-transfer routes.

Closed screened routes remain as recorded in Git history and prior `project-state.md` versions. Broader mathematical problems may remain open; the recorded mechanisms are not to be revived by renaming.