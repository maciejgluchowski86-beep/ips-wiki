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

The historical numerical threshold was localized to a finite-window right-edge corrector/submartingale problem. Student B derived the exact edge-generator drift, analytically recovered the `lambda>1/3` threshold at `k=1`, numerically obtained a `k=8` zero-drift threshold `0.0346195435...`, and supplied an exact rational certificate at `k=10`, `lambda=1/40` with minimum drift `1033/40000000>0`.

The human principal independently executed the exact standard-library certificate and reproduced the asserted minimum and argmin. This was a mechanical arithmetic check only.

The Professor independently checked the mathematical encoding and consequence in `notes/professor-edge-corrector-verification.md`:

- rederived the finite-window generator drift from the BABP event rates;
- checked that one exterior bit suffices for the instantaneous generator;
- proved the bounded-corrector positive-drift implication to positive asymptotic edge speed;
- rederived the `k=1` threshold exactly;
- separately implemented the LP and reproduced the `k=8` zero crossing near `0.0346195435` and strict feasibility at `k=10, lambda=0.025`.

Historical-source qualification: the accessible Sudbury (1999) publisher record explicitly states the `0.0347` finite-seed improvement and edge-speed bounds, and the title explicitly concerns hunting submartingales. The exact full proof text was not available during this Professor check, so line-by-line identity between Sudbury's internal construction and the present `k=8` encoding is not yet certified.

Scientific status after Meeting 003:

- `BABP-EDGE-001` entered `research/claim-registry.md` with status `claimed`;
- its claim is the exact positive-drift ten-site corrector at `lambda=1/40` and consequent positive outward edge speeds;
- no claim is made yet that finite-seed convergence holds at `lambda=1/40`;
- the current first unresolved edge is the edge-speed-to-local-convergence bridge;
- DFP quasi-duality was demoted as a black-box route after Student B showed the finite-test cylinder has no probability-law DFP representation and the exact finite-window signed representation has exponentially growing coefficient norm.

Opportunity-cost review: Student A's reconnaissance had favored the residual simple-IPS positive-rates/noisy-East problem over provisional BABP unless Student B found a genuinely new small-parameter handle. The exact certificate supplies such a handle, so the Professor committed to BABP for the next substantial block while retaining noisy East as the strongest current reserve candidate.

Group Meeting 003:

- path: `meetings/003-edge-corrector-breakthrough.md`;
- `state_narrowed: yes`;
- direction: `continue`;
- BABP status: committed active programme.

Because one finite-state calculation currently carries the strategy, the Professor requested a fresh independent hostile audit at `audits/001-edge-corrector-request.md`. The project claim remains `claimed` until that audit returns.

Graduate Student B's next assignment is `students/student-b/assignment-002.md`: reconstruct or reprove the bridge from positive two-sided edge speed to finite-seed local convergence, first at `lambda=1/40`, and isolate any second parameter-dependent hypothesis before work begins on proving the finite-window threshold tends to zero.
