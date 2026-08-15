# Audit log

## 2026-08-15 — programme initialization

The Professor closed the preceding FA-1f finite-seed programme after Group Meeting 002 and selected BABP finite-seed convergence as a genuinely new scientific direction.

Target: prove convergence of one-dimensional BABP from every finite nonempty particle set for all `lambda>0`, removing the remaining classical small-parameter gap.

Selection evidence inspected directly:

- canonical patch paper `paper/sections/applications.tex` and `paper/sections/discussion.tex`;
- Martinelli--Shapira--Toninelli (2025), Section 5, including Theorem 5.2, self-duality, quasi-duality, all-parameter finite-seed linear growth, and Remark 5.4 recording the `lambda>0.0347` convergence range;
- Sudbury (1999) bibliographic/theorem-level record of the `0.0347` improvement.

The Professor's initial case for tractability was not a patch-contraction heuristic. BABP already has classical duality structure, and the 2025 DFP theorem supplies an all-parameter auxiliary mixing result unavailable in the historical proofs. The first assignment was designed to test whether that new theorem actually removes the historical threshold obstruction.

Graduate Student B was assigned the BABP obstruction audit. Graduate Student A concurrently performed a bounded open-problem/opportunity-cost scan rather than a second active programme.

## 2026-08-15 — Group Meeting 003: edge-corrector breakthrough

Student B's decisive output:

- `students/student-b/001-threshold-and-dfp.md`;
- `students/student-b/edge-corrector-certificate.py`.

Student B derived the finite-window right-edge corrector/submartingale problem, analytically recovered the `lambda>1/3` threshold at `k=1`, numerically obtained a `k=8` zero-drift threshold `0.0346195435...`, and supplied an exact rational certificate at `k=10`, `lambda=1/40` with minimum drift `1033/40000000>0`.

The human principal independently executed the exact standard-library certificate and reproduced the asserted minimum and argmin. This was a mechanical arithmetic check only.

The Professor independently checked the mathematical encoding and consequence in `notes/professor-edge-corrector-verification.md`:

- rederived the finite-window generator drift from the BABP event rates;
- checked that one exterior bit suffices for the instantaneous generator;
- derived the liminf right-edge and limsup left-edge ballistic consequences from uniform positive drift;
- rederived the `k=1` threshold exactly;
- separately implemented the LP and reproduced the `k=8` zero crossing near `0.0346195435` and strict feasibility at `k=10, lambda=0.025`.

Historical-source qualification at the meeting: the accessible Sudbury (1999) publisher record explicitly states the `0.0347` finite-seed improvement and edge-speed bounds, and the title explicitly concerns hunting submartingales. The exact full proof text was not available, so literal line-by-line identity between Sudbury's internal construction and the present `k=8` encoding was not certified.

Scientific status at Meeting 003:

- `BABP-EDGE-001` entered `research/claim-registry.md` with status `claimed`;
- no claim was made that finite-seed convergence holds at `lambda=1/40`;
- the current first unresolved edge became the edge-bound-to-local-convergence bridge;
- DFP quasi-duality was demoted as a black-box route after Student B showed the finite-test cylinder has no probability-law DFP representation and the exact finite-window signed representation has exponentially growing coefficient norm.

Opportunity-cost review: Student A's reconnaissance had favored the residual simple-IPS positive-rates/noisy-East problem over provisional BABP unless Student B found a genuinely new small-parameter handle. The exact certificate supplied such a handle, so the Professor committed to BABP for the next substantial block while retaining noisy East as the strongest current reserve candidate.

Group Meeting 003:

- path: `meetings/003-edge-corrector-breakthrough.md`;
- `state_narrowed: yes`;
- direction: `continue`;
- BABP status: committed active programme.

Because one finite-state calculation carried the strategy, the Professor requested a fresh independent hostile audit at `audits/001-edge-corrector-request.md`.

Graduate Student B's next assignment is `students/student-b/assignment-002.md`: reconstruct or reprove the bridge from the verified ballistic edge bounds to finite-seed local convergence, first at `lambda=1/40`, and isolate any second parameter-dependent hypothesis before work begins on proving the finite-window threshold tends to zero.

## 2026-08-15 — Independent audit 001 completed

Audit:

- commit `d1ef2ca`;
- `audits/001-edge-corrector-audit.md`.

The fresh auditor rederived the BABP edge generator from the transition rules, independently decoded the certificate, evaluated all `2048` window/exterior states exactly, independently rebuilt the `k=8` LP, and checked the martingale argument.

Verified mathematical core:

- one unresolved bit beyond the `k`-window is sufficient;
- no event class is missing;
- there is no hidden total-particle-number dependence in the drift or martingale bounds;
- at `k=10`, `lambda=1/40`, the exact minimum drift is `1033/40000000>0`;
- for every finite nonempty initial state,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-\frac{1033}{40000000}
\quad\text{a.s.};
$$

- `k=1` strict feasibility is exactly `lambda>1/3`;
- the independently rebuilt `k=8` LP has numerical zero crossing `0.0346195434755...` and changes sign between `0.03461954` and `0.03461955`.

The audit required three corrections to the Meeting 003 record:

1. “asymptotic edge speed” was too strong if read as existence of a limiting speed; only the displayed `liminf/limsup` conclusion is proved by the corrector argument;
2. literal historical identity with Sudbury's internal `k=8` construction is not source-verified because the full paper body remained inaccessible;
3. the present result is not yet a strict improvement of Sudbury's published **convergence theorem**. It is a verified finite-window corrector and ballistic-edge result at a parameter below `0.0347`; the convergence bridge remains open.

The corrections are now stated explicitly in `meetings/003-edge-corrector-breakthrough.md` rather than silently editing the historical record.

Claim promotion: `BABP-EDGE-001` is promoted from `claimed` to `verified`, with the exact liminf/limsup wording and audit pointer in `research/claim-registry.md`.

Historical provenance decision: exact identification of Sudbury's computation with the present `k=8` LP is not load-bearing for the verified project result. No separate session will be spent solely on that attribution. Student B should continue to seek the full Sudbury proof because it is directly relevant to the current convergence bridge; if obtained, the provenance question should be resolved then.
