# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate student: Graduate Student B

Graduate Student A: idle after full-text literature comparison

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: `meetings/006-sudbury-correction-and-front-reduction.md`

## Target

For every `lambda>0`, prove that one-dimensional BABP started from a finite nonempty particle set converges locally to Bernoulli equilibrium of density

$$
q=\frac{\lambda}{1+\lambda}.
$$

The programme remains active.

## Verified mathematics

### `BABP-EDGE-001`

At `lambda=1/40`, `k=10`, there is a bounded rational finite-window corrector with

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

for all `2048` edge/exterior states. The exact certificate and its ballistic liminf/limsup consequences were independently audited in commit `d1ef2ca`.

### `BABP-CONV-001`

For fixed `lambda>0`, a bounded finite-window corrector with uniform statewise positive drift implies local convergence from every finite nonempty deterministic initial set. The project has a self-contained tagged-gap proof, independently accepted in commits `abb05f6` and `1aeb5a5`, with the Review A localization and finite-spatial-truncation repairs incorporated.

Combining the two verified claims gives finite-seed convergence at

$$
\lambda=\frac1{40}=0.025.
$$

## Historical/novelty correction after Sudbury full text

Meeting 006 corrects the earlier novelty framing.

Sudbury (1999), Section 3, is literally the same finite-window robust edge-submartingale framework. After reflection:

- `m=k`;
- his `m`-block is the project edge word `u`;
- his one unresolved end-value is `z`;
- his correction `S_i` is `phi`;
- his local gain `a_i+sum_j q_ij(S_j-S_i)` is `D_{k,lambda}`.

His Maxwell's-demon end-value can depend on the current block state, and Lemma 5 requires one correction vector to work for every assignment of end-values. Since each row depends only on its own one-bit end-value, this is exactly the statewise both-`z` robust condition. Lemma 7 gives free extension from any window `m_1` to every larger `m_2` by ignoring the additional sites.

Table 2 reports the trial-and-error sequence ending with `m=8`, `lambda_m=0.0347`, and explicitly does not assert that these decimals are exact critical values. Thus the project `k=8` crossing `0.0346195434755...` refines the same eight-site problem.

Immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used existence of a suitable submartingale to rule out the null stationary limit; his Section 3 extends that condition to `0.0347`, after which their Section 5 argument proceeds unchanged. Therefore the corrector-to-convergence implication itself is prior art.

Correct contribution statement:

> The project extends Sudbury's published finite-window computation from the reported `m=8`, `0.0347` range to an exact rational `m=10` certificate at `lambda=1/40`, yielding the corresponding finite-seed convergence range extension. The project also gives a self-contained tagged-gap proof of the classical implication. No novelty claim is made for that proof architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

The mathematical statuses of `BABP-EDGE-001` and `BABP-CONV-001` remain `verified`; the correction is to provenance and novelty.

## Current all-parameter reduction

Student B's `students/student-b/003-front-gap.md`, commits `5c357ef` and `1365840`, validates the infinite-front reduction after supplying the missing cylinder-core argument.

For each fixed `lambda>0`, let `I_lambda` be the invariant laws of the environment seen from the rightmost particle. Then

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

Hence the exact fixed-parameter finite-window target is

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda.
$$

Student B also shows that every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`, using the all-parameter finite-seed cardinality-growth theorem and reflection symmetry. Thus the only possible obstruction to the finite-window route is an additional invariant semi-infinite-tail phase with smaller current that is not selected from finite seeds.

A sufficient stronger statement is uniqueness of the invariant law of the infinite front process. This is not proved. A nearest-gap-only corrector cannot improve the old `1/3` threshold, so deeper tail correlations are genuinely necessary.

## Current bottleneck

Exclude hostile invariant semi-infinite-tail phases, preferably by proving front uniqueness or directly proving positive current for every invariant front law.

Student B assignment: `students/student-b/assignment-004.md`.

## Opportunity cost

The full Sudbury comparison materially lowers the standalone novelty of the `lambda=1/40` result: it is a range extension within a classical mechanism. BABP nevertheless remains active for one further substantial block because the all-parameter problem is still open and the front reduction has sharply localized the remaining obstruction.

If the next hostile-phase/uniqueness attack produces no theorem-level narrowing, the next group meeting should explicitly compare continuation against Student A's noisy-East reserve rather than continue by enlarging LP windows.

## Neuhauser--Sudbury (1993), Section 5

Worth obtaining if the principal can provide it, for publication attribution and to determine whether the tagged-gap proof architecture is already present. It is not a dependency of the verified range extension or current all-parameter mathematics. No separate session should be spent solely acquiring it.

## Wiki freeze

Recommendation remains: keep the live wiki frozen. The full-text correction makes a `proved here` BABP page inappropriate until the stable research note is reframed around the exact range certificate and prior art is fully attributed.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `students/student-a/writeup-001-literature-and-manuscript-plan.md`, Sudbury (1999) Section 3/Table 2/Lemmas 5 and 7/Theorem 7, `students/student-b/003-front-gap.md`, and `meetings/006-sudbury-correction-and-front-reduction.md`.

Consecutive no-narrowing meetings: 0

## Direction

`continue`.