# Student F Assignment 002: analytic toolbox second wave

## Objective

Continue the source-checked analytic/functional half of the ergodicity-methods toolbox. Wave one has been accepted at Meeting 002. This assignment should **fill distinct gaps**, not produce variants of the six accepted entries.

Read first:

- root `CHATGPT.md`;
- `research/active/ergodicity-methods-toolbox/state.md`;
- `proof-spine.md`;
- `entry-template.md`;
- `meetings/001-opening-taxonomy-source-standard-and-first-wave.md`;
- `meetings/002-f-wave-one-source-audit-and-second-wave.md`.

## Durability rule — mandatory

**Commit each finished method entry immediately. One completed method entry per substantive entry commit.** Do not batch the wave into a final response. If the session freezes, only the current unfinished entry should be at risk.

Stage under

`research/active/ergodicity-methods-toolbox/entries/`

and run `validate_entries.py` when practical.

## Source and scope rules

For every entry:

- inspect at least one primary source and give an exact theorem/proposition/lemma/section/page pinpoint;
- give a stable DOI/arXiv/source URL;
- if the main criterion is general Markov-chain machinery, cite a concrete spin/IPS/KCSM/Glauber application;
- distinguish uniqueness, $L^2$ convergence, total-variation mixing, entropy decay, spectral gap, and LSI precisely;
- do not claim priority unless checked;
- explain overlap with an already accepted toolbox entry rather than repeating its derivation.

Breadth remains the goal. A highly model-specific method is acceptable if rigorous and reusable.

## Second-wave entries

Produce six entries, unless source structure forces a well-justified split/merge.

1. **Lu--Yau martingale / conditional-variance recursion.** Focus on recursive conditioning or martingale decomposition used to prove spectral-gap or log-Sobolev estimates for Glauber/Kawasaki-type systems. Separate this from the already accepted overlapping-block bisection method.

2. **Spectral independence / local-to-global influence method.** State the influence-matrix criterion actually used in the source and the resulting Glauber spectral-gap/mixing/functional-inequality conclusion. Explain how this differs from classical one-site Dobrushin contraction and Dobrushin--Shlosman spatial mixing.

3. **Block factorization or approximate factorization of entropy.** Treat factorization itself as the proof architecture: a block/conditional entropy inequality is iterated or fed into mLSI/LSI to obtain rapid relaxation. Do not merely restate the wave-one LSI page. Prefer a source where spatial mixing is converted quantitatively into block factorization and then dynamics.

4. **Bounded-perturbation / Holley--Stroock transfer.** Give the precise comparison hypothesis and constant loss under which Poincare/LSI-type coercivity transfers from a reference Gibbs law or generator to a perturbed one, plus a spin-system application. State prominently when the oscillation loss grows with volume and therefore fails to give a uniform infinite-volume estimate.

5. **Moving-particle / long-jump comparison for conservative IPS.** Source a genuine exclusion/Kawasaki argument in which a long exchange is decomposed into local exchanges or a moving-particle lemma transfers a reference coercive estimate. Explain its relation to, but distinction from, generic canonical-path comparison.

6. **Finite-size / finite-volume criterion for uniform relaxation.** Source a theorem where checking mixing/coercivity on boxes up to a controlled scale or uniformly over boundary conditions yields a volume-uniform spectral gap, LSI, or exponential Glauber relaxation. The criterion itself, not merely a particular high-temperature conclusion, should be the focus.

If one item cannot be supported cleanly by a primary spin/IPS source, replace it with another genuinely distinct analytic method from the coverage spine and explain the substitution in the handoff. Do not pad with a weakly supported entry.

## Completion

Final handoff: filenames and SHAs, any source ambiguity, any substitution, and a short list of still-uncovered analytic families. Do not edit `docs/`.
