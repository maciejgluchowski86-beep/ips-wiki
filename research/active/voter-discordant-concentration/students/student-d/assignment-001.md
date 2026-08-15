# Graduate Student D assignment 001: sharp discordance concentration reduction

Work on branch `research/voter-discordant-concentration`.

This is a genuinely new scientific direction. You are the persistent Graduate Student D for this line.

Read first:

- `project-state.md`;
- `CHATGPT.md`, especially the standing novelty standard;
- `research/active/voter-discordant-concentration/state.md`;
- `research/active/voter-discordant-concentration/proof-spine.md`;
- `research/active/voter-discordant-concentration/literature.md`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani, *Discordant edges for the voter model on regular random graphs*, especially Sections 1.3--1.4, the uniform-concentration section, and the duality/preparation used there.

Student A's previous reconnaissance is useful orientation but is not authority. Recheck every load-bearing formula from the source/model.

## Goal

Determine whether the proposed sharp concentration statement for the discordant-edge density has a credible theorem route for this group, and reduce it to the narrowest exact correlation estimate possible.

Do not spend the assignment merely extending the authors' polynomial time window by a larger exponent.

## Task A: exact source statement and current frontier

Transcribe in your own notation, without changing quantifiers:

1. the exact statement the authors expect in Eq. (1.9), including the law/probability mode, assumptions on `t_n`, `C_n`, `d`, and the initial law;
2. the strongest concentration theorem actually proved in the paper;
3. exactly where its time restriction enters the proof.

Check whether later work through 2026-08-16 resolves or materially strengthens this static random-regular-graph statement. Use primary sources for any claimed successor theorem.

## Task B: first-principles martingale decomposition

For a fixed `d`-regular graph and configuration `eta`, let `D(eta)` be the number of discordant edges and let `k_x` be the number of neighbours disagreeing with `x`.

Derive the generator action on `D` directly from the voter update rule. If the reconnaissance identity is correct, derive it rather than quoting it:

$$
LD=\sum_x\frac{k_x}{d}(d-2k_x).
$$

Introduce the minimal local observable needed to rewrite this drift and give the exact semimartingale decomposition of the normalized discordance `mathcal D_t^n`, including predictable quadratic variation with correct constants.

Decide whether the martingale part alone is uniformly of the proposed `sqrt(t/n)` size in every time regime allowed by Eq. (1.9).

## Task C: very-small-time hostile check

Do not assume the expected statement is correctly formulated at `t_n->0` or bounded `t_n`.

Test the literal Eq. (1.9) against:

- `t_n -> 0` at arbitrary rates;
- `t_n = Theta(1)`;
- `t_n -> infinity` with `t_n=o(n)`.

Include initial Bernoulli fluctuations. If an additive `n^{-1/2}` term or lower-time condition is actually necessary, state the corrected conjecture precisely and prove the obstruction to the literal version.

A genuine correction/refutation of the proposed formulation is a substantive outcome.

## Task D: isolate the integrated-drift obstruction

Center the drift observable appropriately and express

$$
\int_0^t \widetilde W_s\,ds
$$

or the exact corresponding term in the semimartingale decomposition.

Use voter/coalescing-walk duality to derive an exact representation for its second moment or covariance kernel. Determine the smallest number of dual walkers required and identify all collision/meeting events that contribute.

The desired reduction is an explicit estimate which, if proved uniformly for `t=o(n)`, would imply the sharp concentration statement. State it with exact normalizations and environmental probability mode.

Do not write "control correlations" as a placeholder: expose the actual covariance sum/integral and its required bound.

## Task E: assess the authors' weak-dependence method

Locate the load-bearing combinatorial/probabilistic estimate that limits the published concentration window. Determine whether reaching all `t=o(n)` appears to require:

- a quantitatively sharper version of the same estimate;
- a qualitatively new multi-walk coupling/decoupling statement;
- or a different martingale/corrector decomposition.

Under the standing novelty rule, simply tuning constants or increasing a window exponent is diagnostic only.

## Early-exit criterion

End the programme's first block with one of:

1. a sharp exact reduction to a plausible multi-walk estimate plus a concrete reason it may be provable;
2. a proof that the literal Eq. (1.9) needs correction, together with the corrected structural target;
3. a precise obstruction showing that the currently visible route would require an essentially new random-graph/multi-walk theorem with no concrete mechanism.

In case 3, recommend against continuing by incremental time-window improvements.

## Durable output

Commit the full report to

`research/active/voter-discordant-concentration/students/student-d/001-sharp-concentration-reduction.md`

and any exact computation/check scripts under the same student directory.

End with exactly one recommendation:

- `develop sharp multi-walk estimate`;
- `replace target by corrected concentration theorem`;
- `route not tractable — precise obstruction: ...`.

Do not edit `main`.
