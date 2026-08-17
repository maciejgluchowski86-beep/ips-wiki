# Student F Assignment 008: FA-1f / East applicability audit

Date: 2026-08-17

This is **not a literature-collection assignment**. Wave seven ended collection. The final toolbox inventory is frozen for this assessment except for Professor source-audit corrections and the pending final structural gate.

## Goal

Assess every source-audited toolbox method for usefulness toward one-dimensional FA-1f / East out-of-equilibrium convergence, with the unresolved all-density one-dimensional hard FA-1f Bernoulli-quench problem as the main target and East as the closest solved structural benchmark.

The question is not which methods are generally powerful or thematically close. A high rating requires a mathematically explicit bridge to an exact unresolved object.

## Required reading

On branch `research/ergodicity-methods-toolbox`:

- `research/active/ergodicity-methods-toolbox/assessment-protocol.md`;
- `research/active/ergodicity-methods-toolbox/meetings/017-wave-seven-audited-collection-frozen-assessment-dispatched.md` once present;
- `docs/ergodicity-methods.md` and every live method page linked from that hub;
- `docs/entries/fa-1f-out-of-equilibrium.md`;
- `docs/entries/east-out-of-equilibrium.md`;
- `docs/entries/east-distinguished-zero-screening.md`.

On branch `agent/fa1f-chronology-sign-route`:

- `docs/entries/chronology-averaged-sign-route-for-fa-1f.md`.

On branch `research/fa1f-finite-seed`:

- `research/active/fa1f-finite-seed/state.md`;
- `research/active/fa1f-finite-seed/proof-spine.md`.

Repository conclusions are evidence to be checked, not authority. Do not silently strengthen a source theorem or reopen an exact route already shown to collapse to the conservative centered/patch transfer.

## Exact target interfaces

The chronology/sign record supplies several sufficient targets in the unresolved Bernoulli-quench regime. They are alternatives, not mandatory architecture choices:

1. finite-time sign preservation `G_t(r) >= 0`;
2. shield positivity `S(t) >= 0`;
3. adjacent-vacancy repulsion `Cov(z_0(t),z_1(t)) <= 0`;
4. the endogenous-boundary three-site conditional cross-product inequality;
5. rooted punctured positivity `J_t(r) >= 0` in the last-ring Duhamel reduction.

A method may instead propose a genuinely different route to convergence, but then the bridge statement must identify the precise target-level theorem it would prove.

Hard negative evidence includes:

- coefficientwise positivity is stronger than necessary and false;
- the isolated-insertion cone is not manifestly generator-invariant because adjacent updates create cluster-extension gradients of uncontrolled sign;
- replacing endogenous exterior facilitation by independent or deterministic signals removes the actual difficulty and is not a valid closure;
- the centered positive `h`-transform and complete `h`-weighted patch transfer are exact but conservative/stochastic reformulations;
- the closed finite-seed programme reached the same conservative coefficient dynamics through its two exact patch/dual routes;
- a new route based on one-dimensional spatial screening/regeneration is still admissible, but it must explain the two-sided obstruction absent in East.

## Required output

Create and commit:

`research/active/ergodicity-methods-toolbox/assessment/fa1f-east-method-audit.md`

It must contain:

1. **Complete disposition table.** Every final toolbox method receives exactly one rating:
   - `A` actionable;
   - `B` plausible architecture;
   - `C` auxiliary/diagnostic;
   - `X` blocked by a specific obstruction or hypothesis failure;
   - `N` no credible contact.
2. **Shortlist of at most six A/B methods**, ranked by expected research value.
3. For every shortlisted method, an explicit **bridge lemma** stated mathematically. “Use coupling”, “use regeneration”, or “prove spatial mixing” is not a bridge lemma.
4. The implication chain from that bridge to a live FA-1f target or to convergence itself.
5. The exact established obstruction the route avoids, or an explanation why it is genuinely outside the closed architectures.
6. A **cheapest-first falsification test**: finite-volume computation, exact generator calculation, coupling sanity check, or sharply bounded primary-source inspection that could kill the route before a major proof investment.
7. A separate note when a method is materially more promising for the finite-seed problem than for the Bernoulli quench.

For every `A/B/C/X` row, name the target interface and cite the relevant repository/source pointer. `A` or `B` without a written bridge statement is invalid.

## Scope discipline

- No broad new literature search.
- Open primary sources only when a toolbox page is insufficient to formulate or falsify an adaptation precisely.
- Do not create or edit toolbox entries, `docs/`, or `mkdocs.yml`.
- Do not begin proving the shortlisted lemmas beyond the minimum calculations needed to classify/falsify them; this assignment is comparative architecture assessment.
- Do not pad the shortlist. Zero, one, or two credible A/B methods is an acceptable outcome.

## Handoff

After committing the audit, write `students/student-f/008-handoff.md` with:

- audit commit;
- count of A/B/C/X/N dispositions;
- ranked A/B shortlist;
- the single cheapest falsification experiment you recommend running first;
- any method that initially looked promising but was killed by an exact existing obstruction.

Then stop. The next step is hostile cross-review, not another collection or proof assignment.
