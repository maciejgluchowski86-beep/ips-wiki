# Student G Assignment 002: second coupling and graphical literature wave

## Objective

Fill six distinct coupling/graphical gaps in the ergodicity-methods toolbox. This is literature compilation, not a proof attempt for the positive-rates conjecture.

Read first:

- root `CHATGPT.md`;
- `research/active/ergodicity-methods-toolbox/state.md`;
- `proof-spine.md`;
- `entry-template.md`;
- `meetings/003-g-wave-one-source-audit-and-joint-taxonomy.md`.

Your first-wave entries are accepted. Reuse their terminology where appropriate, but do not duplicate them.

## Durability rule — mandatory

**Commit each finished method entry immediately.** One completed method entry per substantive entry commit. Do not batch several entries into a final response. If the session freezes, only the current unfinished entry should be at risk.

Stage entries under:

`research/active/ergodicity-methods-toolbox/entries/`

and keep them compatible with `validate_entries.py`.

## Source rule

For every entry:

- inspect at least one primary source;
- give exact theorem/proposition/lemma/section/page pinpoints;
- include a stable DOI/arXiv/publisher URL;
- if the canonical theorem is general Markov-chain theory, include a concrete spin-system/IPS/Glauber application;
- do not claim priority unless checked;
- distinguish static Gibbs uniqueness, finite-volume mixing, infinite-volume convergence, clustering, perfect sampling, and spectral-gap conclusions precisely.

## Second-wave entries

Produce six entries, unless source structure forces a split or merge. Explain any change in the handoff.

1. **Dynamical disagreement domination.** Find a rigorous space-time coupling in which disagreements between two spin-system trajectories are dominated by a subcritical contact process, branching process, or oriented-percolation process, yielding coupling agreement or dynamical mixing. Keep this separate from the already accepted static van den Berg--Maes disagreement-percolation entry.

2. **Coupling from the past (CFTP).** State the backward random-map coalescence criterion and a genuine spin/Glauber application. Keep exact stationary sampling conceptually separate from merely proving forward mixing.

3. **Clan of ancestors / perfect simulation.** Prefer the Fernandez--Ferrari--Garcia style criterion where almost-sure finiteness of a backward dependency clan is proved by a branching or percolation majorant. Give a spin/Gibbs/IPS application. Do not merge this with CFTP or information percolation.

4. **Censoring inequalities.** Source a Peres--Winkler-type result for monotone Glauber/spin dynamics: deleting updates cannot accelerate mixing in the relevant stochastic/order sense. State the exact monotonicity and initial-law hypotheses and one application.

5. **Block/local/maximal coupling beyond one-site path coupling.** Find a genuinely different coupling architecture: e.g. couple blocks, use maximal local couplings, or couple after multiple updates so that a one-site Hamming contraction is unnecessary. The entry must have a concrete spin-system/Glauber application and should explain what extra freedom the block/local coupling buys.

6. **Coalescing-random-walk duality for voter-type systems.** Give the graphical duality from voter spins to coalescing walks and state how recurrence/transience or coalescence yields clustering, convergence to agreement, or classification of invariant laws. This is a model-specific graphical method and should be distinct from the already accepted finite-ancestor extinction entry.

## Breadth reconnaissance

In the final handoff, list additional distinct coupling/graphical methods that remain uncovered, but do not create speculative entries merely to increase count. Useful possibilities include complete-convergence/block-construction arguments, disagreement fronts/regeneration, coupling in weighted Wasserstein metrics, and finite-volume-to-infinite-volume graphical transfer.

## Completion

Run `validate_entries.py` if available. The final handoff should list entry filenames and SHAs, note any source/attribution qualifications, and identify any proposed split/merge. Do not edit `docs/` in this assignment.
