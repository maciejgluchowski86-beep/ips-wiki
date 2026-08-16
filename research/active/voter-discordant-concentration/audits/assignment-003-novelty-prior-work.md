# Independent audit 003: novelty and closest prior work for `VOTER-CONC-001`

You are a fresh independent novelty / priority auditor. You did not participate in the development or correctness review of this result. Your task is not to re-referee the proof unless a literature comparison exposes a mathematical mismatch.

Repository: `maciejgluchowski86-beep/ips-wiki`, branch `research/voter-discordant-concentration`.

Read first:

- `CHATGPT.md`, especially the standing novelty standard;
- `project-state.md`;
- `research/claim-registry.md`, entry `VOTER-CONC-001`;
- `research/active/voter-discordant-concentration/meetings/003-correctness-passed-novelty-audit.md`;
- `research/active/voter-discordant-concentration/students/student-d/002-four-walk-cancellation.md`;
- `research/active/voter-discordant-concentration/audits/001-genealogy-review-a.md`;
- `research/active/voter-discordant-concentration/audits/002-genealogy-review-b.md`.

The two correctness reviews passed. Do **not** infer novelty from that fact. Do **not** infer novelty merely because Avena--Baldasso--Hazra--den Hollander--Quattropani (2024) wrote Eq. (1.9) as an open strengthening.

## Claim package whose priority must be assessed

The deterministic theorem is:

> Let `G` be a finite simple `d`-regular graph with `d>=1`, not necessarily connected. Start the rate-one continuous-time voter model from i.i.d. Bernoulli(`u`) opinions, `u in (0,1)`, and let `Dcal_t` be the discordant-edge density. If `pi` is uniform on vertices and `tau_meet` is the meeting time of two independent rate-one continuous-time simple random walks started from `pi tensor pi`, then for every `t>=0`,
> 
> $$
> \operatorname{Var}_u^G(\mathcal D_t)
> \le 2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
> $$

The proof conditions on the entire Harris genealogy at time `t`: ancestral clusters receive independent Bernoulli labels, the discordant-edge count is a weighted cut statistic on the quotient multigraph, its conditional variance is bounded by the ancestral cluster-square sum, and the variance of its conditional mean is bounded through interaction of two ancestral edge families.

Combined with the meeting estimate used in Avena et al. (2024), especially their (5.8), this gives for uniformly random simple fixed-`d>=3` regular graphs and every deterministic `t_n=o(n)`:

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n),
$$

hence concentration at scale `C_n sqrt((1+t_n)/n)` for every `C_n->infinity`. For deterministic `1<=t_n=o(n)` it gives the source scale `C_n sqrt(t_n/n)`.

The project also gives the explicit correction that literal source Eq. (1.9) is false for unrestricted very-small times, e.g. `t_n=n^{-3}`, `C_n=log n`, because initial Bernoulli fluctuations are already of order `n^{-1/2}`.

## Audit objective

Determine whether the claimed contribution is genuinely new, partly prior art, or entirely subsumed by existing literature. This is a hostile priority audit. Search broadly enough that a simple classical identity is not missed merely because terminology differs.

### A. Deterministic variance inequality

Search predecessor literature for the inequality itself or a theorem that immediately implies it. Include at least the following terminology families:

- voter model variance / covariance / concentration;
- discordant edges, disagreeing edges, interfaces, edge boundary, cut size, boundary size;
- Harris graphical representation, ancestral partition, genealogy, coalescing random walks;
- moments of voter-model polynomial observables;
- cluster or quotient-graph representations of voter configurations;
- Efron--Stein / conditional-variance arguments applied to voter genealogy;
- finite-graph voter-model concentration through meeting probabilities.

Check whether a known general covariance formula or duality theorem for voter models makes the deterministic inequality an immediate corollary, even if the inequality is not printed in the same notation.

### B. Random-regular sharp concentration

Check whether any predecessor or successor work already proves

$$
\operatorname{Var}(\mathcal D_{t_n}^n)=O((1+t_n)/n)
$$

or concentration at `sqrt(t_n/n)` throughout deterministic `1<=t_n=o(n)` for static random regular graphs, perhaps under different centering or probability language.

Read the 2024 source carefully enough to determine whether its own arguments elsewhere already imply this after a short observation. Follow the citations most likely to contain earlier variance/concentration estimates.

Search successor literature through the current date, including papers citing or extending the 2024 discordant-edge paper.

### C. Small-time correction

Determine whether the surrounding prose of source Eq. (1.9) makes an implicit lower-time intention clear enough that the `t_n->0` counterexample is merely a literal-notational correction, or whether the displayed quantifiers genuinely create a publishable correction. Search versions/corrections if any.

Do not overstate this point either way. Distinguish:

- literal falsity of the displayed statement;
- intended theorem regime;
- novelty/importance of pointing out the correction.

### D. Standing novelty standard

Apply the principal's standing rule strictly. A result does not count merely because it sharpens a constant, enlarges a routine parameter, or packages known ingredients. Conversely, a genuinely new deterministic reduction from discordance variance to two-walk meeting probability, or a proof of the authors' unresolved sharp regime by a structurally different genealogy argument, does qualify if not already implicit in prior work.

## Required source discipline

Use primary sources whenever possible. Give exact theorem/proposition/equation numbers and enough statement detail to compare hypotheses and conclusions. Search predecessor, successor, alternate terminology, and citation chains. If a potentially fatal prior result cannot be obtained in full, say so explicitly and do not declare novelty verified.

Do not rely on the project's own literature summaries as authority.

## Output

Commit the audit to

`research/active/voter-discordant-concentration/audits/003-novelty-prior-work.md`.

Your report must separately classify:

1. deterministic inequality;
2. random-regular corrected concentration theorem;
3. source-scale theorem for `1<=t_n=o(n)`;
4. small-time correction of literal Eq. (1.9).

For each, give one of:

- `novel on the audited literature`;
- `prior art / immediate corollary of prior work`;
- `priority unresolved`.

Then give an overall recommendation for `VOTER-CONC-001` under the project's standing novelty standard:

- `counts as a project result`;
- `verified mathematics but not a new project result`;
- `novelty unresolved — do not promote contribution status`.

If you find prior art, identify the earliest and closest source precisely and explain whether the project proof adds any genuinely new theorem or only a new proof/presentation.
