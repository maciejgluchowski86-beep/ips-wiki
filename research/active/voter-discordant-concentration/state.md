# Programme state

## Direction

Title: sharp concentration of voter-model discordant edges on random regular graphs

Branch: `research/voter-discordant-concentration`

Professor lineage: persistent ChatGPT Professor

Graduate Student D: new persistent student for this direction

Graduate Students A, B, C: idle with prior lineages

Workspace: `research/active/voter-discordant-concentration/`

Latest group meeting: none yet

## Target

Study the explicit concentration strengthening posed in Avena--Baldasso--Hazra--den Hollander--Quattropani, *Discordant edges for the voter model on regular random graphs* (ALEA 2024).

For a random `d`-regular graph on `n` vertices and voter model started from i.i.d. Bernoulli(`u`) opinions, let

$$
\mathcal D_t^n
$$

be the fraction of discordant edges. The source proposes sharp concentration on the intrinsic fluctuation scale throughout sublinear times: for `t_n/n -> 0` and `C_n -> infinity`, establish the source's Eq. (1.9), whose scale is

$$
C_n\sqrt{t_n/n}.
$$

The exact probability mode, quantifiers, and any required lower-time qualification must be copied from the primary source before proof work. Student A's earlier reconnaissance is guidance, not authority.

## Why this direction

The noisy-East finite-wall programme closed after its one-attack statistic was shown not to concatenate under repeated attacks. The next opportunity-cost candidate has three attractive features:

- the target is explicitly proposed by the authors of the 2024 paper;
- the expected fluctuation scale has a direct martingale interpretation;
- there is a concrete load-bearing obstruction: control of the integrated centered drift / local two-edge correlation observable at the same scale.

The programme must not become a sequence of modestly longer time-window improvements. Under the standing novelty standard, a qualifying outcome is the full structural concentration theorem, a genuine obstruction/counterexample to the proposed formulation, or a new theorem identifying the correct sharp regime.

## First mathematical task

Graduate Student D assignment 001 is a source-grounded reduction/falsification task.

It must:

1. state Eq. (1.9) exactly from the published/arXiv source, including probability mode and time assumptions;
2. inspect the proof of the existing uniform-concentration theorem and identify exactly where its time window stops;
3. rederive the generator/martingale decomposition of `D_t^n` from first principles;
4. isolate the centered drift term and rewrite its covariance/variance in a form suitable for dual coalescing-walk analysis;
5. test the literal conjectured scale in the very-small-time regimes rather than assuming it is correctly formulated there; and
6. identify a single necessary correlation estimate whose proof would close the target, or a precise obstruction showing why the published weak-dependence method cannot reach it.

## Novelty discipline

A theorem extending the published concentration window by a larger exponent but not reaching a structurally new regime does not count as a project result by itself.

The first assignment is diagnostic. Its output should either expose a credible sharp route or lower the expected value quickly.

## Research delta

No group meeting yet.

## Direction

`continue`.
