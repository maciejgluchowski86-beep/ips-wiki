# Student F Assignment 001: analytic and KCSM ergodicity methods

## Objective

Build the first source-checked analytic/functional half of the ergodicity-methods toolbox. This is literature work, not a proof attempt for the positive-rates conjecture.

Read first:

- root `CHATGPT.md`;
- `research/active/ergodicity-methods-toolbox/state.md`;
- `proof-spine.md`;
- `entry-template.md`;
- `meetings/001-opening-taxonomy-source-standard-and-first-wave.md`.

The old positive-rates files may suggest terminology but are not sources.

## Durability rule — mandatory

**Commit each finished method entry immediately.** One completed method entry per substantive entry commit. Do not wait to finish the assignment or batch several entries into one response. If the session freezes, only the current unfinished entry should be lost.

Stage entries under:

`research/active/ergodicity-methods-toolbox/entries/`

using `entry-template.md` exactly enough to pass `validate_entries.py`.

## Source rule

For every entry:

- inspect at least one primary source;
- give an exact theorem/proposition/lemma/section/page pinpoint;
- include a stable URL/DOI/arXiv link;
- if the canonical theorem is a general Markov-chain result, also give a concrete spin-system/IPS/KCSM/Glauber application source;
- do not claim priority when you have not checked it;
- distinguish uniqueness, convergence, spectral gap, log-Sobolev, and mixing-time conclusions precisely.

## First-wave entries

Produce six entries, unless source structure clearly requires a split/merge. If you change the list, explain why in the handoff.

1. **Poincare inequality / spectral-gap method.** State the semigroup/variance criterion and the conclusion it gives; include a representative spin-system or KCSM application.
2. **Logarithmic Sobolev and/or modified logarithmic Sobolev method.** Separate classical LSI from mLSI if the mechanisms/conclusions differ enough to deserve distinct entries.
3. **Dirichlet-form comparison / canonical-path comparison.** Explain how comparison transfers a gap or mixing estimate and give an IPS/Glauber application.
4. **Block dynamics + martingale/variance decomposition/bisection.** Focus on the recursive mechanism used to obtain uniform spectral gaps or relaxation bounds in spin systems/KCSM.
5. **Spatial mixing implies dynamical mixing.** Source a rigorous bridge such as Dobrushin-Shlosman/strong spatial mixing to spectral gap, LSI, or rapid Glauber mixing. State exactly which spatial condition implies which dynamical conclusion.
6. **One model-specific KCSM relaxation mechanism.** Prefer a method that is not merely another name for item 4: e.g. distinguished-zero/oriented-vacancy arguments for East, legal-path/canonical-path coercivity, or bootstrap-percolation-assisted relaxation. Pick the clearest source-supported mechanism.

## Breadth reconnaissance

While sourcing these, keep a short list in your final handoff of additional distinct analytic/model-specific methods that should be assigned later. Do not write speculative entries merely to enlarge the count.

## Completion

Run the mechanical validator if available in your environment. Your final handoff should be short: list committed entry filenames and SHAs, any source/attribution uncertainty, and the next uncovered method families you found. Do not edit `docs/` in this assignment.
