# Project claim registry

This file is the mechanical status index for project-specific mathematical claims that appear on `main` outside the scratch research workspace.

Allowed mathematical statuses are `claimed`, `verified`, and principal-designated `canonical`. A `verified` claim must point to a durable independent audit record. **Mathematical verification is separate from research-contribution status.** Under the standing novelty standard in `CHATGPT.md`, a verified calculation obtained only by instantiating an existing arbitrary-size method at a larger window/order/degree or analogous complexity parameter is not a new project result merely because it improves a numerical constant.

## Canonical patch results

### PATCH-FACTOR-001

Status: `canonical`

Claim: conditional on the successful-interaction skeleton up to a finite horizon, the patch interaction data are independent with their consistent patch laws; equivalently, the patch factorization theorem holds.

Source: `paper/sections/representation.tex`, theorem `Patch factorization`.

Basis: principal designation of `paper/` as the canonical patch source.

### PATCH-REP-001

Status: `canonical`

Claim: the signed monomial Feynman--Kac representation factors over patches and yields the exact patch representation of the spin-system semigroup stated as Theorem A.

Source: `paper/sections/main-results.tex` and `paper/sections/representation.tex`.

Basis: principal designation of `paper/` as the canonical patch source.

## Verified BABP mathematics retained for reuse

The two entries below remain mathematically verified and may be used as technical inputs. After the Sudbury full-text comparison and the principal's standing novelty ruling, **neither counts as a project research result or contribution**. Sudbury's finite-window method is defined for arbitrary window size, so the ten-site computation is exactly the kind of larger-window quantitative instantiation excluded by the protocol's novelty standard. The corrector-to-convergence implication is classical prior work.

### BABP-EDGE-001

Status: `verified`

Research-contribution status: **not a project result under the standing novelty standard**.

Claim: for one-dimensional BABP in particle variables with rates

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x,
$$

at

$$
\lambda=\frac1{40}
$$

there is a bounded corrector depending on the first ten sites behind the rightmost particle such that

$$
D_{10,1/40}(u,z;\phi)
\ge \frac{1033}{40000000}>0
$$

for every `u in {0,1}^10` and `z in {0,1}`. Consequently, for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

No existence of limiting edge speeds is asserted.

Source proof/certificate:

- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`;
- `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

Professor check:

- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`.

Independent hostile audit:

- commit `d1ef2ca`;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

Historical identification: Sudbury (1999), Section 3, uses the same finite-window robust submartingale mechanism. After reflection, his window size `m`, block state, unresolved end-value, correction vector, and corrected local gain are respectively the present `k`, edge word `u`, exterior bit `z`, corrector `phi`, and drift `D_{k,lambda}`. His Maxwell's-demon formulation is exactly the robust both-`z` condition: the exterior value may be assigned independently as a function of the current block state, and Lemma 5 requires one corrector to work for every such assignment. Lemma 7 extends any successful `m_1` construction to every larger `m_2` by ignoring the extra sites. Table 2 reports the trial value `m=8`, `lambda_m=0.0347`.

The independently computed project value `0.0346195434755...` refines the same eight-site optimization, and the exact `k=10`, `lambda=1/40` witness is a correct larger-window instance. It is useful verified technical data but, under the principal's standing standard, not a substantive new result.

### BABP-CONV-001

Status: `verified`

Research-contribution status: **not a new project theorem; verified self-contained formulation/proof of a classical implication**.

Claim: fix `lambda>0` and the BABP convention above. If there exist `k>=1`, bounded `phi:{0,1}^k->R`, and `v>0` such that

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every edge state `(u,z)`, then, for every finite nonempty deterministic initial particle set `B`,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_{\lambda/(1+\lambda)}
\qquad(t\to\infty)
$$

locally on `{0,1}^Z`.

The statewise drift hypothesis is load-bearing in the project proof; bare liminf/limsup edge bounds are not asserted to imply convergence.

Stable self-contained proof:

- `research/results/babp-finite-seed-convergence.md`.

Source proof:

- commit `f79d0fb`, `research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`.

Professor proof with reviewer repairs:

- `research/active/babp-finite-seed/notes/professor-corrector-to-convergence-verification.md`.

Independent correctness reviews:

- commit `abb05f6`, `research/active/babp-finite-seed/audits/002-convergence-review-a.md`;
- commit `1aeb5a5`, `research/active/babp-finite-seed/audits/002-convergence-review-b.md`.

Historical/novelty status: Sudbury (1999), immediately before Theorem 7, states that the Neuhauser--Sudbury (1993) finite-seed convergence argument relies on existence of a suitable finite-window submartingale, that his Section 3 extends this condition from the old `1/3` range to `0.0347`, and that their Section 5 proceeds unchanged. Thus the implication from the appropriate finite-window submartingale to finite-seed convergence is classical rather than a project discovery.

The project's tagged-internal-gap proof is a useful self-contained proof architecture, but no novelty claim is made for that architecture until Neuhauser--Sudbury (1993), Section 5, is inspected. Combining this classical implication with `BABP-EDGE-001` yields mathematically valid convergence at `lambda=1/40`; because the only new input is the larger-window instance of Sudbury's arbitrary-`m` method, that quantitative range extension is **not counted as a project result** under the standing novelty standard.

Claim boundary: no all-parameter theorem, no convergence rate, and no initial laws beyond finite nonempty deterministic sets are claimed.