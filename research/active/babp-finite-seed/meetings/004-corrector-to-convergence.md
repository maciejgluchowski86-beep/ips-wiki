# Group meeting 004: finite-window corrector to finite-seed convergence

Date: 2026-08-15

Professor review of Graduate Student B assignment 002, commit `f79d0fb`.

state_narrowed: yes

Evidence pointer: `students/student-b/002-edge-speed-to-convergence.md`, `notes/professor-corrector-to-convergence-verification.md`, and later reviews `audits/002-convergence-review-a.md` and `audits/002-convergence-review-b.md`.

## Mathematical decision

Student B proved that the load-bearing hypothesis is the full statewise corrector inequality

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge state, not merely the resulting outer liminf/limsup velocity bounds.

The proof applies the same corrector to the two populations bordering each internal vacant gap. Positive gaps are born at width one, cannot split, and distinct positive gaps cannot merge. The corrected gap width has drift at most `-2v` until closure. After localization, exponential tilting gives uniform gap lifetime and maximal-width tails; Poisson boundary displacement and a finite-spatial-truncation compensator sum give

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Together with stationarity of weak limit points and the one-dimensional stationary-law classification, this forces convergence to Bernoulli equilibrium from every finite nonempty deterministic seed.

At the meeting this was registered as `BABP-CONV-001`, initially `claimed`, and two fresh independent reviews were requested. Both later passed the proof, and Meeting 005 promoted the claim to `verified` for mathematical correctness.

## Full-text novelty correction after Meeting 006

The original Meeting 004 note called this a "central new theorem." That novelty characterization was too strong and is explicitly withdrawn.

The full text of Sudbury (1999) shows that the theorem-level implication is prior art. Immediately before Theorem 7, Sudbury states that the Neuhauser--Sudbury (1993) stationary-state argument relied on existence of a suitable submartingale, that his Section 3 extends that condition from the old `1/3` range to `0.0347`, and that the argument of their Section 5 then proceeds unchanged.

Moreover, Sudbury's suitable submartingale is the same robust finite-window object as the project statewise corrector: his Maxwell's-demon end-value can be chosen state-by-state, and Lemma 5 requires one correction vector to work for every assignment. Hence the general implication `statewise finite-window corrector => finite-seed convergence` must not be advertised as a project discovery.

What remains valid and useful from Meeting 004 is the project's independently checked, self-contained tagged-gap proof of this classical implication. Whether that particular proof architecture is novel remains unresolved until Neuhauser--Sudbury (1993), Section 5, is inspected.

Combined with the exact audited ten-site certificate, the implication yields a genuine range extension to `lambda=1/40`, but inside Sudbury's established mechanism.

## Direction

The mathematical bridge remains `verified`. Meeting 006 supersedes Meeting 004's novelty language.