# Project state

This branch is the archived technical record of the 1D BABP finite-seed programme. Current project-wide state lives on `main`.

## Programme status

**Closed at Group Meeting 006.**

Branch: `research/babp-finite-seed`

Workspace: `research/active/babp-finite-seed/`

Original target: finite-seed local convergence for every `lambda>0`.

Latest meeting: `research/active/babp-finite-seed/meetings/006-sudbury-correction-and-front-reduction.md`, `state_narrowed: yes`.

Graduate Students A and B are idle after closure. The previously created `students/student-b/assignment-004.md` is superseded and should not be executed.

## Standing novelty correction

The principal's standing scientific-taste rule, now codified in `CHATGPT.md`, is that a quantitatively improved instance obtained only by running an existing arbitrary-size method at a larger window/order/degree or analogous complexity parameter does not count as a new project result, even when exact.

Applied to this programme:

- `BABP-EDGE-001` remains mathematically verified, but the exact `k=10`, `lambda=1/40` certificate is not a project result because Sudbury's method already allows arbitrary `m` and Lemma 7 gives free window extension;
- `BABP-CONV-001` remains mathematically verified, but the corrector-to-convergence implication is classical prior work;
- the resulting `lambda=1/40` convergence statement is a correct larger-window quantitative instantiation inside Sudbury's mechanism and is not counted as a project contribution.

The claim registry and stable technical note retain these facts for reuse with explicit non-contribution status.

## Source-verified Sudbury mapping

Sudbury (1999), Section 3, is exactly the same robust finite-window edge-submartingale problem after reflection:

- his `m` is project `k`;
- his block state is `u`;
- his unresolved end-value is `z`;
- his correction vector is `phi`;
- his corrected local gain is `D_{k,lambda}`.

The Maxwell's-demon condition is exactly the statewise both-`z` requirement, and Lemma 7 gives free extension to larger windows. Table 2 reports trial values through `m=8`, `lambda_m=0.0347`.

Immediately before Theorem 7, Sudbury states that the Neuhauser--Sudbury finite-seed argument relies on a suitable submartingale and proceeds unchanged once his Section 3 extends that condition. Thus the general convergence implication is classical.

## Dormant structural result path

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

Every singleton-selected Cesaro front law has positive current for every `lambda>0`; the only possible obstruction is an additional invariant semi-infinite-tail phase.

A genuine future BABP result under the standing novelty standard would have to address this structural all-parameter question, for example proving positive current for every invariant front law or proving a genuine positive floor for the finite-window method. No such theorem was obtained.

## Closure rationale

The remaining structural problem is an infinite-volume phase-selection/uniqueness problem. The obvious reset coupling is circular, the `lambda=0` endpoint has many absorbing hard-core phases, and the entropy/current route still lacks a no-incoming-flux theorem from particle-index infinity.

Student A's earlier opportunity-cost reconnaissance ranked the residual positive-rates/noisy-East target above BABP unless BABP produced genuinely new small-parameter mathematics. Under the standing novelty standard, that condition was met in the negative.

The project therefore pivots to `research/noisy-east-positive-rates` rather than extending BABP by another finite-window or hostile-phase variant.

## Reopen condition

Do not reopen BABP merely to increase `k`, improve a threshold, or change finite-window coordinates. Reopening requires a genuinely new structural idea for the invariant-front/all-parameter problem.

## Wiki

Keep the live wiki frozen. No BABP `proved here` update is warranted from this programme.