# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

The principal has supplied a standing scientific-taste rule, now codified in `CHATGPT.md`:

> Running an existing method at a larger window, order, degree, truncation level, parameter budget, or analogous complexity parameter to obtain a quantitatively better constant does not count as a new project result, even when the computation is exact.

Such calculations may remain mathematically verified and useful, but they do not justify contribution claims or programme continuation by themselves. A qualifying result must add structural mathematics beyond that instantiation, for example a theorem about the method's full regime, a genuine qualitative extension, a new mechanism, or a proof/refutation of the target problem.

## Active scientific direction

**Residual positive-rates conjecture / noisy East for simple one-sided one-dimensional IPS.**

- Research branch: `research/noisy-east-positive-rates`
- Planned workspace: `research/active/noisy-east-positive-rates/`
- Positive target: prove ergodicity in the remaining noisy-East region for simple one-sided one-dimensional positive-rate IPS, with the long-term target of completing the positive-rates conjecture for simple IPS.
- Why this target now: Student A's opportunity-cost reconnaissance ranked it above BABP unless BABP produced a genuinely new small-parameter theorem. After the Sudbury full-text comparison and the standing novelty ruling, BABP did not meet that condition. The noisy-East problem has stronger group-specific leverage from the principal's recent work and an inexpensive decisive first falsification test.
- First bottleneck: test whether the one-site common-state wall mechanism can be genuinely strengthened to a **two-site agreed block** under the canonical coupling.
- First task: construct the exact killed finite-state chain/operator for a length-two agreed block with adversarial exterior state, where killing means disagreement crosses the block before regeneration to full agreement. Determine the corresponding next-generation/spectral factor and its behavior in the residual noisy-East region, especially approaching the East boundary.
- Professor: persistent ChatGPT Professor.
- Graduate Students A and B: idle with their prior lineages.
- Because this is a genuinely new direction, a new persistent graduate student may be created for the noisy-East programme.

The cheap two-site calculation is intentionally an early exit test. If it fails sharply near the East boundary, the straightforward finite-wall extension should be killed before a long proof programme is built around it.

## Most recently closed programme: BABP finite seed

The 1D BABP finite-seed programme closed at Group Meeting 006 on expected-value/opportunity-cost grounds.

### Mathematical facts retained

`BABP-EDGE-001` remains mathematically verified by audit `d1ef2ca`: at

$$
\lambda=\frac1{40},\qquad k=10,
$$

a bounded rational finite-window corrector has exact minimum statewise drift

$$
\frac{1033}{40000000}>0.
$$

`BABP-CONV-001` remains mathematically verified by reviews `abb05f6` and `1aeb5a5`: a uniformly positive statewise finite-window corrector implies finite-seed local convergence. The self-contained tagged-gap proof is retained in `research/results/babp-finite-seed-convergence.md`.

### Research-contribution correction

Neither BABP item counts as a project research result under the standing novelty standard.

The full Sudbury (1999) text shows that his Section 3 is the same finite-window robust edge-submartingale framework. After reflection, his window `m`, block state, unresolved end-value, correction vector, and corrected gain are the project `k`, edge word `u`, exterior bit `z`, corrector `phi`, and drift `D_{k,lambda}`. His Maxwell's-demon condition is exactly the statewise both-`z` robustness requirement. Lemma 7 gives free extension from any successful window to every larger window.

Thus the exact ten-site `lambda=1/40` certificate is a correct larger-window instance of an existing arbitrary-`m` method. It is useful verified technical mathematics but not a project contribution. Sudbury also explicitly states before Theorem 7 that the finite-seed convergence argument relies on the suitable submartingale condition and proceeds unchanged once that condition is extended, so the corrector-to-convergence implication is classical prior work.

BABP therefore closed **without a new project result** under the standing standard.

### Dormant structural BABP reduction

Student B's commits `5c357ef` and `1365840` remain useful dormant mathematics. For fixed `lambda>0`, the finite-window optimization was reduced to invariant laws of the infinite right-front process:

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1),
$$

with

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Every singleton-selected Cesaro front law has positive current for every `lambda>0`; the only possible obstruction is an additional invariant semi-infinite-tail phase. Proving or refuting positivity for **all** invariant front laws would be a genuine structural result under the standing novelty standard. No proof was obtained, and the evident coupling/entropy routes currently lack a concrete closing mechanism.

Do not reopen BABP merely to increase the finite window, refine numerical thresholds, or change finite-window coordinates. A future return requires a genuinely new idea for the invariant-front structural problem or an equivalent all-parameter theorem.

## Opportunity-cost decision

Student A's `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md` ranked the residual positive-rates/noisy-East target above BABP on present evidence, conditional on BABP failing to produce genuinely new small-parameter mathematics. The standing novelty ruling makes that condition applicable.

The noisy-East candidate has unusually strong group-specific leverage:

- the principal authored the recent reduction to the residual noisy-East region;
- the simple-IPS parameterization, time-scaling reduction, canonical coupling, disagreement geometry, and long-lived-state wall mechanism are already part of the principal's work;
- the one-site wall failure region is explicit;
- the next candidate mechanism admits a finite exact two-site falsification test.

This is a better expected-value use of the next research block than asking BABP for another variant of an unresolved hostile-front uniqueness theorem.

## Neuhauser--Sudbury (1993), Section 5

If conveniently available from the principal, it is still worth inspecting solely to settle attribution of the BABP tagged-gap proof architecture. It is not a dependency of any active programme and should not consume a research session.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. No BABP `proved here` update is warranted because the verified BABP calculations do not satisfy the standing novelty standard for project contributions.

## Stable claims

`research/claim-registry.md` remains the mathematical status index.

- `BABP-EDGE-001`: `verified` mathematics, audit `d1ef2ca`; explicitly not a project result under the standing novelty standard.
- `BABP-CONV-001`: `verified` mathematics, reviews `abb05f6` and `1aeb5a5`; classical implication, not a new project theorem.

No all-parameter BABP convergence claim is registered.

## Closed programmes and routes

Closed programmes not to be retried by renaming include:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on centered-transform / unnormalized patch-transfer routes;
- 1D BABP finite-seed programme based on finite-window submartingales and the unresolved invariant-front continuation described above.

Broader mathematical problems may remain open. What is closed is the recorded programme/mechanism at its present expected value.