# Project claim registry

This file is the mechanical status index for project-specific mathematical claims that appear on `main` outside the scratch research workspace.

Allowed statuses are `claimed`, `verified`, and principal-designated `canonical`. A `verified` claim must point to a durable independent audit record. Mathematical verification and novelty/priority are separate questions.

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

## Active or later project claims

### BABP-EDGE-001

Status: `verified`

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

Historical identification, corrected after full-text comparison with Sudbury (1999): Sudbury's Section 3 uses the same finite-window robust submartingale mechanism. His `m` is the window size, his `m`-block is the edge word, the single end-value is the exterior bit, and his corrected local gain

$$
a_i+\sum_jq_{ij}(S_j-S_i)
$$

is the reflected form of `D_{k,lambda}`. His Maxwell's-demon formulation permits the end-value to depend on the current block state, and Lemma 5 requires one corrector to work for every assignment of those end-values; because only the current row's single end-value enters its drift, this is exactly the robust requirement that both exterior-bit values work in every edge state. Table 2 reports `m=8`, `lambda_m=0.0347`, explicitly as a trial-and-error value rather than an exact critical value. Lemma 7 states that a submartingale at `m_1` extends to every larger `m_2` by ignoring the extra sites.

Novelty boundary: the finite-window submartingale mechanism is Sudbury's, not a project invention. The project contribution recorded here is the independently audited **exact rational ten-site certificate at `lambda=1/40`**, together with the exact drift margin above. The project `k=8` crossing `0.0346195434755...` refines Sudbury's reported decimal for the same eight-site optimization problem.

### BABP-CONV-001

Status: `verified`

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

The project proof applies the corrector to both populations bordering a tagged internal gap. After localization, exponential tilting gives uniform gap lifetime/width tails; Poisson displacement and a finite-spatial-truncation compensator sum followed by monotone convergence yield local nonescape. Jahnel--Köppl (2026), Theorem 2.5, supplies stationarity of weak limit points, and Martinelli--Shapira--Toninelli (2025), Corollary 2.9, supplies the stationary-law classification after the explicit time rescaling `lambda=q/p`, `L_project=p^{-1}L_MST`.

Concrete consequence: together with `BABP-EDGE-001`, this proves finite-seed convergence at `lambda=1/40=0.025`.

**Historical/novelty correction.** The implication from a suitable robust finite-window submartingale to finite-seed convergence is not new. Sudbury (1999), immediately before Theorem 7, states that Neuhauser--Sudbury (1993) used existence of a suitable submartingale to exclude the null stationary limit, that his Section 3 extends this condition from the old `1/3` range to `0.0347`, and that the argument of Neuhauser--Sudbury Section 5 then proceeds unchanged. Thus `BABP-CONV-001` is retained as a verified, self-contained project formulation/proof of a **classical implication**, not as a new general criterion.

The verified new range datum is the exact `k=10`, `lambda=1/40` certificate inside Sudbury's established mechanism. Whether the project's particular tagged-gap proof architecture is itself new remains unresolved because Neuhauser--Sudbury (1993), Section 5, has not yet been inspected in full. No priority claim is made for that proof architecture.

Claim boundary: no all-parameter theorem, no convergence rate, and no initial laws beyond finite nonempty deterministic sets are claimed.