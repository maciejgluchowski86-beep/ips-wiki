# Audit log

## Meeting 001: source correction and reduction

`meetings/001-sharp-concentration-reduction.md`

- `state_narrowed: yes`.
- Literal source Eq. (1.9) refuted at very small times.
- Corrected target set to scale `sqrt((1+t_n)/n)`.
- Exact martingale/four-lineage reduction checked by the Professor.
- No project theorem registered at that meeting.

## Meeting 002: genealogical variance theorem enters audit

`meetings/002-genealogical-variance-claim.md`

- `state_narrowed: yes`.
- Student D source proof: commit `e73fd25`, `students/student-d/002-four-walk-cancellation.md`.
- Professor reconstruction: `notes/professor-assignment-002-verification.md`.
- Central package registered as `VOTER-CONC-001`, status `claimed`.

Claimed deterministic inequality:

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

## Independent correctness reviews completed

Review A:

- commit `add0681`;
- `audits/001-genealogy-review-a.md`;
- verdict `PASS`.

Review B:

- commit `45f960b`;
- `audits/002-genealogy-review-b.md`;
- verdict `PASS`;
- explicitly did not read Review A.

Both reconstruct the proof independently and request no mathematical repair. Both verify the conditional genealogy argument, ordered-pair count, cluster-square/meeting identity, four-family coupling including within-family coalescence, edge orientation normalization, random-walk clock convention, random-regular source interface, quenched probability mode, and the very-small-time counterexample.

Editorial clarifications adopted into the project statement:

- deterministic theorem: finite simple `d`-regular graphs with `d>=1`; connectedness not required;
- random-regular consequence: fixed `d>=3`;
- use source (5.8), not the bare (5.7) wording, for the all-small-time meeting estimate; monotonicity handles `t<1`;
- phrase the source-(1.9) defect at theorem level rather than claiming a complete classification of every subunit sequence.

## Meeting 003: correctness passed; novelty gate remains

`meetings/003-correctness-passed-novelty-audit.md`

- `state_narrowed: yes`.
- Correctness barrier passed with two independent hostile reviews.
- `VOTER-CONC-001` deliberately remains `claimed` because Meeting 002 pre-committed to a closest-prior-work / novelty audit before `verified` promotion or manuscript contribution language.

## Novelty audit in flight

Assignment:

`audits/assignment-003-novelty-prior-work.md`.

Expected output:

`audits/003-novelty-prior-work.md`.

The audit must classify separately the deterministic inequality, corrected all-sublinear random-regular theorem, source-scale theorem for deterministic `1<=t_n=o(n)`, and small-time correction of literal Eq. (1.9). It must search predecessor/successor literature and alternate terminology rather than relying on the 2024 source's open-problem statement.

Until this audit is resolved, `VOTER-CONC-001` remains `claimed` despite having passed correctness review.

## Wiki

Keep the live wiki frozen until novelty/contribution status is settled.
