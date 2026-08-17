# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or equivalent forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.
- Breadth is intentional; model-specific methods are in scope.
- Opening meeting: `research/active/ergodicity-methods-toolbox/meetings/001-opening-taxonomy-source-standard-and-first-wave.md`.
- Student F: active on analytic/functional/KCSM literature Assignment 001.
- Student G: active on coupling/graphical/duality literature Assignment 001.

## Wiki publication rule

The principal's new instruction reopens the live wiki **for this toolbox section**. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

Draft method entries are staged outside `docs/` under the active workspace. After source and Professor review, accepted material will be promoted to a new top-level live-wiki section:

- `docs/ergodicity-methods.md` hub;
- one audited literature page per method under `docs/entries/`;
- `Ergodicity methods` navigation in `mkdocs.yml`.

The current live-wiki admission gate remains in force: new public entries must be source-checked and carry `audit: current` when promoted.

## Literature inclusion and source standard

Include a method if it has a rigorous criterion/theorem or reusable proof architecture, at least one IPS/spin/KCSM/Glauber-type use, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete IPS/spin application. Model-specific methods are explicitly welcome.

Every staged entry must inspect and pinpoint at least one primary source. Citation existence alone is not verification; Professor review checks that the source actually supports the claim.

## Durability and mechanical checks

Every finished method entry is committed immediately as its own durable artifact. Do not batch whole surveys. `research/active/ergodicity-methods-toolbox/validate_entries.py` checks required metadata, headings, URL/pinpoint presence, and length; it does not certify mathematical correctness or attribution.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture` under `research/active/positive-rates-conjecture/`. A concise established-results summary is `research/active/positive-rates-conjecture/programme-established-results.md` on that branch. No proof architecture or student assignment remains active there.

## Most recently completed theorem-search status

The positive-rates conjecture itself remains open. The previous loop ended with no currently credible proof architecture; that status is archival and does not constrain the present literature toolbox except as a source of search vocabulary.
