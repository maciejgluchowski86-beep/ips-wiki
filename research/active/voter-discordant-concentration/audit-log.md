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

Claimed random-regular consequences:

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n)
$$

for every deterministic `t_n=o(n)`, yielding the corrected concentration theorem, and `O_P(t_n/n)` for deterministic `t_n>=1`, yielding the source scale in that regime.

## Independent correctness reviews

Two genuinely independent reviews are assigned and pending:

- Review A assignment: `audits/assignment-001-review-a.md`;
- Review B assignment: `audits/assignment-002-review-b.md`.

Expected outputs:

- `audits/001-genealogy-review-a.md`;
- `audits/002-genealogy-review-b.md`.

`VOTER-CONC-001` remains `claimed` until the reviews are completed and substantive objections, if any, are resolved.

## Novelty audit

A dedicated closest-prior-work / novelty audit is pending **after** correctness review. Until that audit survives, do not state publication priority or final contribution status.

## Wiki trigger

The first central theorem in this programme has entered independent audit. Under `CHATGPT.md`, this triggers principal review of the wiki freeze. Professor recommendation remains to keep the live wiki frozen until correctness and novelty review are complete.