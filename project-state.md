# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Active scientific direction

**1D BABP from a finite seed — active.**

- Research branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Target: prove local convergence from every finite nonempty seed for every `lambda>0`.
- Latest group meeting on the research branch: `meetings/006-sudbury-correction-and-front-reduction.md`, `state_narrowed: yes`.
- Active development: Graduate Student B, hostile invariant-front phase problem.

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

The full text of Sudbury (1999) materially changes the novelty assessment and corrects the stronger framing previously promoted to `main`.

Sudbury's Section 3 is the same finite-window robust edge-submartingale framework. After reflection, his window size `m`, block state, single unresolved end-value, correction vector `S`, and corrected gain

$$
a_i+\sum_jq_{ij}(S_j-S_i)
$$

are respectively the project `k`, edge word `u`, exterior bit `z`, corrector `phi`, and drift `D_{k,lambda}`.

His Maxwell's-demon formulation permits the end-value to depend on the current block state. Lemma 5 requires one correction vector to work for every assignment of those end-values; because the drift in each row depends only on that row's one-bit end-value, this is exactly the robust statewise requirement over both `z=0,1`.

Sudbury's Lemma 7 gives free extension from any window `m_1` to every larger `m_2` by ignoring the additional sites. Table 2 reports trial-and-error values through `m=8`, `lambda_m=0.0347`, and explicitly does not claim those decimals are exact critical values. The project crossing `0.0346195434755...` therefore refines the same eight-site optimization problem.

Immediately before Theorem 7, Sudbury states that the Neuhauser--Sudbury (1993) stationary-state argument relied on existence of a suitable submartingale, that his Section 3 extends that condition from the old `1/3` range to `0.0347`, and that their Section 5 argument then proceeds unchanged.

**Correction:** the finite-window mechanism and the corrector-to-convergence principle are prior art. The stable project contribution is the independently audited exact rational `k=10`, `lambda=1/40` range certificate inside Sudbury's framework, together with a self-contained modern proof of the classical convergence implication. No novelty claim is made for the tagged-gap proof architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

The mathematical verification statuses of `BABP-EDGE-001` and `BABP-CONV-001` are unchanged; the correction is to provenance and priority.

## Current all-parameter bottleneck

Student B's commits `5c357ef` and `1365840` validate the infinite-front reduction on the research branch after adding the missing cylinder-core argument.

For fixed `lambda>0`, let `I_lambda` be the invariant laws of the environment seen from the right edge. The research reduction is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1),
$$

with the stationary identity

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`. Therefore the only possible obstruction to this finite-window route is an additional invariant semi-infinite-tail phase not selected from finite seeds.

The current first unresolved edge is to exclude such hostile invariant front phases. Front uniqueness is sufficient but stronger than necessary; positive current for every invariant front law also closes the route.

This infinite-front reduction is research-branch mathematics and is not yet promoted as an independently audited stable theorem.

## Opportunity cost

The full Sudbury comparison lowers the standalone novelty of the `lambda=1/40` result: it is a strict range extension inside a classical mechanism, not a new mechanism or new general convergence criterion.

BABP continues for one further substantial hostile-phase block because the all-parameter target remains open and the front reduction sharply localizes the remaining obstruction. If that block produces no theorem-level narrowing, the next Professor meeting should explicitly compare continuation against the noisy-East reserve rather than continue by merely enlarging finite windows.

## Neuhauser--Sudbury (1993), Section 5

Worth obtaining from the principal if conveniently available, solely to settle publication attribution of the tagged-gap proof architecture. It is not a dependency of the verified range extension or the current all-parameter programme.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. The prior-art correction should be fully reflected in the research note before any `proved here` BABP wiki update.

## Stable surface

`research/claim-registry.md` records:

- `BABP-EDGE-001`: `verified`, audit `d1ef2ca`;
- `BABP-CONV-001`: `verified` for mathematical correctness, reviews `abb05f6` and `1aeb5a5`, with the implication explicitly identified as classical after the Sudbury full-text comparison.

Stable theorem/range note: `research/results/babp-finite-seed-convergence.md`.

The exploratory front-process work remains on `research/babp-finite-seed`.

## Closed programmes and routes

Closed programmes remain closed: quadratic-Hessian; Fresnel integrability; Navier--Stokes stochastic cascade; Strong-KPP uniqueness; supercritical dissipative SQG; long-maturity marked branching; Gaussian bridge coarsening; and the 1D hard FA-1f finite-seed programme based on the centered-transform / unnormalized patch-transfer routes.

Broader mathematical problems may remain open; closed mechanisms are not to be revived by renaming.