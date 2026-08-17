# Meeting 001: open ergodicity-methods literature phase

Date: 2026-08-17

`state_narrowed: yes` — the scientific direction changes from proving the positive-rates conjecture to building a source-checked ergodicity-methods toolbox for the live wiki.

## 1. Direction change

The principal has stopped the proof loop. The new target is deliberately broad: find, document, and organize as many rigorous methods as practical for proving ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or closely related forgetting/extinction statements in spin systems, IPS, KCSM, and Glauber-type models.

Model-specific techniques are wanted. This is an inventory of mathematical tools, not a shortlist of methods likely to solve the previous conjecture.

The old positive-rates workspace remains the archive of that programme. No new proof assignment is active there.

## 2. Wiki tension resolved

The later principal instruction explicitly reopens the **main wiki for this new section**. It does not reopen unrelated deprecated IPS entries.

The live-wiki admission gate still applies. Therefore workers do **not** write drafts directly into `docs/`. Literature entries are staged and source-checked under

`research/active/ergodicity-methods-toolbox/entries/`.

After Professor source review, accepted entries will be promoted to:

- `docs/ergodicity-methods.md` as a compact hub/map;
- individual `docs/entries/<method-slug>.md` pages;
- a new top-level `Ergodicity methods` section in `mkdocs.yml`.

This gives the principal a genuinely live main-wiki section while keeping it cleanly separated from legacy/deprecated material. Existing pages are linked only when they already satisfy the current audit standard or are separately audited.

## 3. Inclusion standard

An entry belongs if it has a rigorous theorem/criterion/proof architecture, an IPS/spin/KCSM/Glauber-type use, and a primary source that can be pinpointed. The method may be extremely model-specific. General Markov-chain tools belong when a concrete spin/IPS application is documented.

Do not pad with slogans, numerical evidence, or generic analogies. Breadth means many **real methods**, not many names.

Each entry must state:

1. what conclusion it proves;
2. hypotheses/settings;
3. the core mathematical mechanism;
4. at least one representative IPS/spin use;
5. limitations/failure modes;
6. a checked primary citation with theorem/proposition/lemma/section/page pinpoint.

The staging schema is fixed in `entry-template.md`. Target length 400–900 words, maximum 1200.

## 4. Attribution standard

Accurate attribution is load-bearing in this phase. `source_status: primary-checked` means the worker opened the primary source and checked the stated pinpoint. A survey/monograph may supplement but should not silently replace the originating or representative primary theorem when available.

If priority/origin is genuinely unclear, do not guess. State the representative source and flag origin as unresolved for Professor review.

No live-wiki promotion occurs from citation existence alone. Professor review will check that the cited theorem actually supports the entry's criterion and conclusion.

## 5. Durability and mechanical verification

The Assignment-010 durability rule becomes permanent for this phase:

> Commit every finished method entry immediately. Do not wait to batch a whole survey or a whole assignment into one response.

Each commit should add one completed entry, except a small source correction may amend the immediately preceding one. This limits damage from session rendering failures and creates natural review units.

`validate_entries.py` is the mechanical checker. The principal/orchestrator should run

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
```

after each batch. A pass checks required fields, headings, URL/pinpoint presence, and length only. It does **not** certify mathematical correctness or correct attribution.

The other mechanical check is commit granularity: one finished method entry per substantive entry commit.

## 6. Worker choice

Student F and Student G are reused rather than replaced. This is a new direction, so new students would be allowed, but F and G already know the relevant vocabulary and can recognize overlaps with methods previously tested. Their project knowledge is useful for search terms and cross-links only; all literature claims must be independently sourced.

Initial division minimizes overlap:

- **F:** functional inequalities, variational/comparison methods, spatial-to-dynamical mixing, KCSM relaxation.
- **G:** coupling, graphical/disagreement methods, duality/extinction, backward-history and influence methods.

## 7. First-wave coverage

The initial twelve entries are chosen to establish the taxonomy rather than exhaust any family.

F first wave:

- Poincare/spectral-gap method;
- logarithmic Sobolev / modified log-Sobolev method;
- Dirichlet-form comparison / canonical-path comparison;
- block dynamics and martingale/bisection decomposition;
- strong spatial mixing or Dobrushin-Shlosman conditions implying dynamical relaxation;
- a genuinely model-specific KCSM relaxation mechanism, preferably East distinguished-zero or a constrained-Poincare/bisection method.

G first wave:

- attractive/monotone coupling and extremal invariant laws;
- Dobrushin influence contraction;
- path coupling in spin-system/Glauber dynamics;
- disagreement percolation or domination of disagreements by a subcritical process;
- duality plus extinction of a finite dual/ancestor process;
- backward dependency clans / coupling from the past / information-percolation history clusters (choose the cleanest first entry and flag the others as distinct future methods where appropriate).

Workers should not force these labels if the literature shows two listed items are actually the same mechanism or one label hides several genuinely distinct methods. Split or merge only with an explicit note in the handoff.

## 8. Next meeting

After the first batch, the Professor will source-audit the decisive claims, deduplicate method boundaries, update the coverage spine, and decide which entries are ready for live-wiki promotion. The next assignments should fill uncovered families rather than repeatedly deepen the first ones.
