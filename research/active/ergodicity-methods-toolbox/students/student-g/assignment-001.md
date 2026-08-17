# Student G Assignment 001: coupling, graphical, and dual ergodicity methods

## Objective

Build the first source-checked probabilistic/graphical half of the ergodicity-methods toolbox. This is literature work, not a continuation of Assignment 010 or another attack on the positive-rates conjecture.

Read first:

- root `CHATGPT.md`;
- `research/active/ergodicity-methods-toolbox/state.md`;
- `proof-spine.md`;
- `entry-template.md`;
- `meetings/001-opening-taxonomy-source-standard-and-first-wave.md`.

The old positive-rates files may suggest terminology but are not sources.

## Durability rule — mandatory

**Commit each finished method entry immediately.** One completed method entry per substantive entry commit. Do not batch the assignment into a single late commit. This rule is specifically intended to survive rendering/session failures.

Stage entries under:

`research/active/ergodicity-methods-toolbox/entries/`

using `entry-template.md` closely enough to pass `validate_entries.py`.

## Source rule

For every entry:

- inspect at least one primary source;
- give an exact theorem/proposition/lemma/section/page pinpoint;
- include a stable URL/DOI/arXiv link;
- if the method originates in general Markov-chain theory, cite a concrete spin-system/IPS/Glauber application as well;
- do not infer priority from familiarity;
- distinguish uniqueness, coupling/coalescence, convergence, spectral gap, and mixing-time conclusions exactly.

## First-wave entries

Produce six entries, unless the primary literature shows that a listed label should clearly split or merge. Explain any change in the handoff.

1. **Attractive/monotone coupling and extremal invariant laws.** Give the order-preserving graphical coupling criterion and explain how upper/lower processes reduce uniqueness/ergodicity questions.
2. **Dobrushin influence contraction.** State an influence-matrix/contraction criterion and a precise spin-system consequence.
3. **Path coupling for Glauber/spin dynamics.** Give the local-distance criterion and a representative spin application; keep it distinct from Dobrushin if the sources support a real distinction.
4. **Disagreement percolation / domination of disagreement by a subcritical process.** State the domination mechanism and what extinction gives.
5. **Duality plus extinction.** Use a clean additive/contact/voter-type example in which extinction or coalescence of a finite dual yields uniqueness or convergence of the primal.
6. **Backward-history methods.** Choose the cleanest first entry among coupling from the past, clan-of-ancestors/backward dependency clusters, and information-percolation/history-cluster methods. State in the handoff which neighboring methods are genuinely distinct and should receive later entries.

## Breadth reconnaissance

Record, in the final handoff only, additional distinct coupling/graphical methods found during source search: block coupling, maximal coupling, oriented-percolation comparisons, regeneration/front methods, information percolation, perfect simulation, complete-convergence arguments, etc. Do not create low-information entries just to increase count.

## Completion

Run the mechanical validator if available. Final handoff should list committed entry filenames and SHAs, any attribution uncertainty, and uncovered method families. Do not edit `docs/` in this assignment.
