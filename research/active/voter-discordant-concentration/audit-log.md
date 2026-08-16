# Audit log

## Meeting 001: source correction and reduction

`meetings/001-sharp-concentration-reduction.md`

- `state_narrowed: yes`.
- Literal source Eq. (1.9) refuted at very small times.
- Corrected target set to scale `sqrt((1+t_n)/n)`.
- Exact martingale/four-lineage reduction checked by the Professor.

## Meeting 002: genealogical variance theorem enters audit

`meetings/002-genealogical-variance-claim.md`

- `state_narrowed: yes`.
- Student D source proof: commit `e73fd25`, `students/student-d/002-four-walk-cancellation.md`.
- Professor reconstruction: `notes/professor-assignment-002-verification.md`.
- Central package registered as `VOTER-CONC-001`, status `claimed`.

## Independent correctness reviews

Review A:

- commit `add0681`;
- `audits/001-genealogy-review-a.md`;
- verdict `PASS`.

Review B:

- commit `45f960b`;
- `audits/002-genealogy-review-b.md`;
- verdict `PASS`;
- explicitly independent of Review A.

Both reconstruct the proof independently and request no mathematical repair.

## Meeting 003: correctness passed; novelty gate remains

`meetings/003-correctness-passed-novelty-audit.md`

- `state_narrowed: yes`.
- Correctness barrier passed.
- `VOTER-CONC-001` remained `claimed` pending the pre-committed novelty / closest-prior-work audit.

## Novelty audit

- commit `5ab5dce`;
- `audits/003-novelty-prior-work.md`;
- verdict: central contribution claim fails under the standing novelty standard.

Fatal closest prior work: Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Proposition 4.1 proof (4.2) plus (5.5)--(5.6). Their printed ingredients immediately imply, for Bernoulli initial data,

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
$$

and source (5.8) yields the same random-regular concentration scales as the project. The project's verified theorem improves `4` to `2` and gives a cleaner quotient-genealogy proof, but this is not a new project result under the standing novelty standard.

The literal very-small-time correction to source Eq. (1.9) is mathematically correct but its priority remains unresolved because Capannoli's 2025 thesis was inaccessible to the novelty auditor.

## Meeting 004: novelty fails and programme closes

`meetings/004-novelty-fails-and-programme-closes.md`

- `state_narrowed: yes`.
- `VOTER-CONC-001` promoted to mathematical status `verified` because correctness review is complete.
- Research-contribution status set to **not a new project result under the standing novelty standard**.
- Programme closed; Graduate Student D idle.
- No active effort will be spent resolving priority of the narrow small-time source correction.

## Wiki

Keep the live wiki frozen. No `proved here` promotion follows from this programme because its central verified theorem package is not a new project result.
