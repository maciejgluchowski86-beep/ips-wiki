# Independent audit assignment 002: genealogical variance theorem, review B

You are a second fresh independent correctness reviewer. Your review must be genuinely independent of Review A. Do not wait for, read, or rely on Review A's eventual report.

Read the current programme files, but treat the Professor and Student D conclusions as claims to attack:

- `CHATGPT.md`;
- `project-state.md`;
- `research/active/voter-discordant-concentration/state.md`;
- `research/active/voter-discordant-concentration/proof-spine.md`;
- `research/active/voter-discordant-concentration/meetings/002-genealogical-variance-claim.md`;
- `research/active/voter-discordant-concentration/students/student-d/002-four-walk-cancellation.md`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), especially the voter graphical construction and (5.5)--(5.8).

You may read `notes/professor-assignment-002-verification.md` only after you have independently reconstructed the main proof, and then only to identify disagreements.

## Central theorem to check

For every finite simple `d`-regular graph,

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
$$

for all `u in (0,1)` and `t>=0`.

The claimed random-regular consequences are the corrected all-sublinear concentration theorem on scale `sqrt((1+t_n)/n)` and the original `sqrt(t_n/n)` scale for every deterministic `1<=t_n=o(n)`.

## Independent attack

Your main job is to decide whether the deterministic inequality is actually true. Derive it from scratch or produce a counterexample.

Pay particular attention to issues that can be missed by a formal total-variance calculation:

- whether the ancestor map at one observation time is sufficient to condition on, or whether hidden graphical dependence remains in the cluster labels;
- whether the event that two ancestral edge families influence one another is exactly or only approximately controlled by the independent four-walk interaction event;
- whether two pair-coalescence indicators can remain dependent without a literal cross-family meeting because the same Harris environment is reused at different times;
- whether within-family coalescence can create cross-family dependence not covered by source (5.5);
- whether source (5.6) applies after averaging the covariance over **unoriented** original edges;
- whether the source's short-time meeting estimate really yields the stated `O_P((1+t)/n)` sequence-wise bound without hidden uniformity assumptions;
- whether the environment and voter expectations are centered in the same quenched sense as source Eq. (1.9).

Use small explicit regular graphs or direct finite-state calculations as hostile tests if useful. A numerical check is not a proof but may expose a flaw.

Also verify the statement that the original source scale is established for all deterministic `t_n>=1`, `t_n=o(n)`. Do not broaden that statement to arbitrary `t_n->0`.

Commit your report to:

`research/active/voter-discordant-concentration/audits/002-genealogy-review-b.md`

End with exactly one verdict:

`VERDICT: PASS`

or

`VERDICT: REPAIRABLE — ...`

or

`VERDICT: FAIL — ...`
