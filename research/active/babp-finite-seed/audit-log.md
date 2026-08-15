# Audit log

## 2026-08-15 — programme initialization

The Professor closed the preceding FA-1f finite-seed programme after Group Meeting 002 and selected BABP finite-seed convergence as a genuinely new scientific direction.

Target: prove convergence of one-dimensional BABP from every finite nonempty particle set for all `lambda>0`, removing the remaining classical small-parameter gap.

Selection evidence inspected directly:

- canonical patch paper `paper/sections/applications.tex` and `paper/sections/discussion.tex`;
- Martinelli--Shapira--Toninelli (2025), Section 5, including Theorem 5.2, self-duality, quasi-duality, all-parameter finite-seed linear growth, and Remark 5.4 recording the `lambda>0.0347` convergence range;
- Sudbury (1999) bibliographic/theorem-level record of the `0.0347` improvement.

Graduate Student B was assigned the BABP obstruction audit. Graduate Student A concurrently performed a bounded opportunity-cost scan.

## 2026-08-15 — Group Meeting 003: edge-corrector breakthrough

Student B derived the finite-window right-edge corrector problem, recovered `lambda>1/3` at `k=1`, numerically obtained the `k=8` crossing near `0.0346195435`, and supplied an exact rational certificate at `k=10`, `lambda=1/40` with minimum drift `1033/40000000>0`.

The Professor independently checked the generator, the liminf/limsup ballistic consequence, the `k=1` algebra, and a separate `k=8`/`k=10` LP implementation.

Meeting 003 recorded `state_narrowed: yes`, committed to BABP, and requested a fresh hostile audit.

## 2026-08-15 — Independent audit 001 completed

Audit:

- commit `d1ef2ca`;
- `audits/001-edge-corrector-audit.md`.

The auditor independently rederived the edge generator, checked all `2048` exact certificate inequalities, reconstructed `k=8`, and verified the martingale bounds. `BABP-EDGE-001` was promoted to `verified` with the precise liminf/limsup ballistic conclusion.

The audit corrected three overstatements: no speed-limit existence is proved; literal historical identity with Sudbury's exact `k=8` computation is unverified; and the edge certificate alone does not improve Sudbury's convergence theorem.

## 2026-08-15 — Group Meeting 004: corrector-to-convergence bridge

Student B committed `students/student-b/002-edge-speed-to-convergence.md`, commit `f79d0fb`.

The key distinction is that convergence is proved from the stronger statewise corrector hypothesis

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge state, not from the outer liminf/limsup bounds alone.

The proof applies the corrector to internal gaps, obtains uniform exponential gap tails, sums over gap nucleations, proves local nonescape, and combines this with stationary-limit invariance and stationary-law classification. The Professor independently reconstructed the argument in `notes/professor-corrector-to-convergence-verification.md`.

New claim `BABP-CONV-001` was entered with status `claimed`. Meeting 004 recorded `state_narrowed: yes` and requested two fresh independent correctness reviews.

## 2026-08-15 — Independent convergence reviews completed

Review A:

- commit `abb05f6`;
- `audits/002-convergence-review-a.md`.

Review B:

- commit `1aeb5a5`;
- `audits/002-convergence-review-b.md`.

Both independently reconstructed the tagged-gap argument and accepted `BABP-CONV-001`.

Review A requested two standard rigor repairs:

1. localize before applying Dynkin/optional stopping to the unbounded exponential test `exp(theta Z)`;
2. write the nucleation compensator first over `|x|<=N` and pass to the infinite spatial sum by monotone convergence.

Both repairs are incorporated in the Professor proof and `research/results/babp-finite-seed-convergence.md` with no added hypothesis.

Review B independently checked the original BABP convention and the external source interfaces. Mountford (1993) was available only through its published abstract and Ramírez--Varadhan (1996) was not available in full, so neither is used as an unchecked load-bearing hypothesis. Instead Jahnel--Köppl (2026), Theorem 2.5, was checked in full and directly supplies stationarity of every weak limit point. BABP satisfies `(L1)` and `(R1)--(R3)` because it has bounded single-site rates and nearest-neighbour influence. Martinelli--Shapira--Toninelli (2025), Corollary 2.9, supplies the stationary-law classification after the explicit rescaling `lambda=q/p`, `L_project=p^{-1}L_MST`.

## 2026-08-15 — Group Meeting 005: convergence theorem promotion

Meeting:

- `meetings/005-convergence-promotion.md`;
- `state_narrowed: yes`;
- direction: `continue`.

`BABP-CONV-001` is promoted to `verified` for mathematical use.

Concrete verified consequence: at `lambda=1/40=0.025`, BABP started from every finite nonempty deterministic particle set converges locally to Bernoulli equilibrium. Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the previous range as `lambda>0.0347`.

Publication-level closest-prior-work/priority audit remains pending; the mathematical theorem is verified independently of any priority claim.

The next development edge is the infinite right-edge environment. Student B's commit `b9fdc55` proposes an exact LP-dual/invariant-front reduction and a front-gap target `sup_mu mu(01)<2lambda`. Graduate Student B resumes on this edge; Graduate Student A begins a focused writeup and closest-prior-work audit.

The wiki-freeze review trigger has fired. Professor recommendation: keep the live wiki frozen until the focused manuscript and novelty audit are complete; the principal controls the decision.