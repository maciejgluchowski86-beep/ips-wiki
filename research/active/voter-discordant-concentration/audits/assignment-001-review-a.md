# Independent audit assignment 001: genealogical variance theorem, review A

You are a fresh independent mathematical auditor. Do not assume the Professor or Student D is correct.

Work read-only except for committing your audit report to the path specified below. Read:

- `CHATGPT.md`;
- `project-state.md`;
- `research/active/voter-discordant-concentration/state.md`;
- `research/active/voter-discordant-concentration/proof-spine.md`;
- `research/active/voter-discordant-concentration/meetings/002-genealogical-variance-claim.md`;
- `research/active/voter-discordant-concentration/students/student-d/002-four-walk-cancellation.md`;
- `research/active/voter-discordant-concentration/notes/professor-assignment-002-verification.md`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), *Discordant edges for the voter model on regular random graphs*, especially (2.1), (5.5)--(5.8).

## Claim under audit

For every finite simple `d`-regular graph `G`, every `u in (0,1)`, and every `t>=0`, with `pi` uniform on vertices,

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

For a uniform random simple `d`-regular graph with fixed `d>=3`, this plus the source meeting estimate is claimed to imply, for every deterministic `t_n=o(n)` and every `C_n->infinity`,

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0,
$$

and the sharper source scale `C_n sqrt(t_n/n)` whenever `t_n>=1`.

## Audit requirements

Reconstruct the proof rather than checking prose locally. Try hard to falsify the earliest load-bearing step.

In particular check:

1. conditioning on the Harris genealogy and independence of ancestral cluster labels;
2. the weighted-cut conditional variance estimate, including ordered-pair counting and constants;
3. the identity between the expected ancestral cluster-square sum and stationary two-walk meeting probability, including walkers initially equal;
4. the covariance bound for `J_t`: whether two edge-family meeting indicators can genuinely be coupled to independent pair systems up to first cross-family meeting;
5. the subtle interface between within-family coalescence in the voter genealogy and the four **independent** walks in source (5.5)--(5.6);
6. uniform unoriented-edge averaging versus the oriented law `nu`;
7. the exact hypotheses and probability mode needed from source (5.7)--(5.8), especially `t<1` and deterministic sequence-wise `t_n=o(n)`;
8. Chebyshev and the quenched-in-probability conclusion;
9. edge cases: `t=0`, shared endpoints, disconnected regular graphs for the deterministic inequality, and fixed bounded times.

If a defect is repairable, state the exact repair and whether it changes the theorem. If fatal, give the smallest counterexample or broken implication you can.

Do not perform a novelty audit in place of correctness review.

Commit your report to:

`research/active/voter-discordant-concentration/audits/001-genealogy-review-a.md`

End with exactly one verdict:

`VERDICT: PASS`

or

`VERDICT: REPAIRABLE — ...`

or

`VERDICT: FAIL — ...`
