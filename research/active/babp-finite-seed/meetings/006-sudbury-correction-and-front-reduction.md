# Group meeting 006: Sudbury correction, novelty ruling, and BABP closure

Date: 2026-08-15

Professor review of:

- Graduate Student A, `students/student-a/writeup-001-literature-and-manuscript-plan.md`, commits `0239d37` and `87d59d8`;
- the full text of Aidan Sudbury (1999), especially Section 3, Table 2, Lemmas 5 and 7, and Theorem 7;
- Graduate Student B, `students/student-b/003-front-gap.md`, commits `5c357ef` and `1365840`;
- Graduate Student A's earlier opportunity-cost reconnaissance `students/student-a/recon-001-open-problem-scan.md`;
- the principal's standing scientific-taste ruling that a quantitatively better instance obtained only by running an existing arbitrary-size method at a larger window/order/degree or analogous complexity parameter does not count as a new result.

state_narrowed: yes

Evidence pointer: Student A's full-text source comparison; Sudbury (1999), pp. 847--852, especially the Maxwell's-demon construction, Lemma 5, Table 2, Lemma 7, and the paragraph immediately before Theorem 7; Student B's `003-front-gap.md`; and Student A's noisy-East opportunity-cost comparison.

## Standing novelty standard and correction to the programme record

The principal's ruling is adopted as a general protocol rule in `CHATGPT.md`, not as a BABP-specific exception.

A larger-window/order/degree instantiation of a method already formulated at arbitrary size does not become a project research result merely because it produces a better numerical constant or an exact certificate. Such mathematics may remain verified and useful, but it is not to be counted as a contribution, used to justify continuation, or framed as discovery.

This changes the BABP programme's scorecard.

The exact ten-site certificate

$$
\lambda=\frac1{40},\qquad
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

remains mathematically verified. The resulting finite-seed convergence at `lambda=1/40` also remains mathematically correct. But neither counts as a project result under the standing novelty standard, because Sudbury's method is explicitly defined for arbitrary finite window size and Lemma 7 gives free extension in window size. The project ran that existing mechanism at `m=10` after Sudbury reported computations only through `m=8`.

Likewise, `BABP-CONV-001` remains a verified self-contained proof/formulation, but the corrector-to-convergence implication is classical prior work and is not a project theorem-level contribution.

Earlier Meeting 004/005 language treating the `lambda=1/40` theorem as the programme's central new result is therefore superseded. The registry and stable note may retain the verified mathematics, but must mark it as non-contributory under the standing novelty standard.

## Source-verified Sudbury identification

The historical identification is exact.

Sudbury uses the same BABP normalization

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

He follows one outer particle, records an `m`-site binary block and one unresolved end-value, and adds a correction vector `S`. After reflection,

- his `m` is the project `k`;
- his block state is the project edge word `u`;
- his end-value is the project exterior bit `z`;
- his correction vector is `phi`;
- his corrected gain
  $$
  a_i+\sum_jq_{ij}(S_j-S_i)
  $$
  is the project `D_{k,lambda}(u,z;phi)`.

The Maxwell's-demon equivalence is exact at the robust-condition level. Sudbury permits the exterior bit to be chosen as a function of the current block state and Lemma 5 requires one correction vector to work for every such assignment. Since the drift in row `i` depends only on the end-value assigned to row `i`, this is equivalent to requiring both `z=0` and `z=1` inequalities in every state.

Lemma 7 gives free window extension: a successful `m_1` correction remains successful for any `m_2>m_1` by ignoring the extra coordinates. Table 2 reports trial values through `m=8`, `lambda_8=0.0347`; Sudbury explicitly does not claim those decimals are exact critical values. The project `k=8` crossing `0.0346195434755...` is therefore a refinement of exactly the same optimization problem.

Immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used a suitable submartingale in the finite-seed stationary-state argument and that, once his Section 3 extends that condition to `0.0347`, their Section 5 proceeds unchanged. Thus the corrector-to-convergence principle is prior art.

## Student B's all-parameter reduction

The one part of the BABP direction that could satisfy the standing novelty standard is the structural all-parameter question: does the finite-window method eventually work for every `lambda>0`, or is there a genuine positive floor?

Student B materially narrowed that question. For fixed `lambda>0`, after adding the cylinder-core repair,

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1),
$$

where `I_lambda` is the invariant-law set of the infinite environment seen from the right edge. Stationarity of the first bit gives

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Hence the finite-window method succeeds at a fixed parameter exactly when every invariant front law has uniformly positive current, equivalently when

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda.
$$

Student B also shows that every Cesaro invariant front law selected from the singleton has positive current for every `lambda>0`. Thus any obstruction must be an additional invariant semi-infinite-tail phase not selected from finite seeds.

This is real target-relevant narrowing. It does **not** close the all-parameter problem. The remaining theorem is an infinite-volume phase-selection/uniqueness problem. At `lambda=0` there is a large absorbing family of hard-core tails, so the endpoint is singular. Student B has no proof of front uniqueness or positive current for all invariant laws; the obvious reset coupling is circular because later left shifts can re-expose the untouched tail. The entropy/current idea still requires a nontrivial no-incoming-flux theorem from particle-index infinity.

## Opportunity-cost decision

**close BABP and pivot.**

This is not a judgment that the all-parameter BABP problem is unimportant. It is an expected-value judgment for this group now.

After applying the principal's standing novelty standard, the programme has produced useful verified technical mathematics but **no completed project research result**. The only qualifying target left is the all-parameter structural theorem, and the current reduction moves it into a difficult semi-infinite invariant-phase problem for which the group has no concrete proof mechanism beyond speculative uniqueness/entropy routes.

Graduate Student A's earlier reconnaissance ranked the residual positive-rates/noisy-East problem above BABP unless BABP produced a genuinely new small-parameter theorem rather than a reconstruction/instance of the historical mechanism. Under the standing novelty standard, that condition has now been met in the negative. The noisy-East target also has stronger group-specific leverage from the principal's recent work and a cheap decisive first falsification test: replace the one-site common-state wall by a two-site agreed block and compute the exact killed finite-state crossing/regeneration operator under adversarial exterior input.

Sunk effort does not justify another BABP variant. Student B's front reduction is preserved as durable dormant mathematics and may be revisited if an independent idea for hostile-phase exclusion appears. The already-created `assignment-004.md`, if present, is superseded by this closure and should not be executed.

## Programme outcome

BABP finite-seed programme: **closed without a new project result under the standing novelty standard**.

Useful retained mathematics:

- independently audited ten-site rational corrector at `lambda=1/40`;
- independently checked self-contained tagged-gap convergence proof;
- source-verified identification with Sudbury's arbitrary-window framework;
- infinite-front LP dual/reduction to hostile invariant front phases, presently research-branch mathematics rather than a promoted theorem.

The broader all-parameter BABP problem remains open and worthwhile.

## Next direction

Open a new programme on the residual positive-rates conjecture for simple one-sided one-dimensional IPS, focused first on the noisy-East region left by the principal's recent results.

The first research block should be a cheap falsification test of the smallest genuinely stronger wall mechanism: a length-two agreed block under the canonical coupling, with adversarial exterior state. Construct the exact killed finite-state chain/operator controlling whether disagreement crosses the block before regeneration to full agreement. Determine whether its next-generation factor is uniformly `<1` in any meaningful part of the residual noisy-East region and, especially, how it behaves when approaching the East boundary.

Graduate Students A and B become idle with their existing lineages. Because this is a genuinely new scientific direction, a new persistent graduate student may be created for it.

## Neuhauser--Sudbury (1993), Section 5

It is still worth inspecting if the principal supplies it conveniently, solely for attribution of the tagged-gap proof architecture. It is no longer a dependency of any active programme and should not consume a research session.

## Wiki

Keep the live-wiki freeze in force. No BABP `proved here` update is warranted: the verified computations are retained as technical records but do not satisfy the standing novelty standard for project contributions.