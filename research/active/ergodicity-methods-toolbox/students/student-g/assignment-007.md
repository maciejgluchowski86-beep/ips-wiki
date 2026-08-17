# Student G Assignment 007: positive-rates applicability audit

Date: 2026-08-17

This is **not a literature-collection assignment**. Wave seven ended collection. The final toolbox inventory is frozen for this assessment except for Professor source-audit corrections and the pending final structural gate.

## Goal

Assess every source-audited toolbox method for usefulness toward the positive-rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS.

The stopped positive-rates programme contains exact reductions and exact obstruction theorems. High ratings require contact with a live residual object or a materially different architecture that bypasses those objects. Renaming an exhausted route is not new input.

## Required reading

On branch `research/ergodicity-methods-toolbox`:

- `research/active/ergodicity-methods-toolbox/assessment-protocol.md`;
- `research/active/ergodicity-methods-toolbox/meetings/017-wave-seven-audited-collection-frozen-assessment-dispatched.md` once present;
- `docs/ergodicity-methods.md` and every live method page linked from that hub;
- especially `docs/entries/one-dimensional-edge-coalescence-positive-rates.md`, while treating Gray's attractive/repulsive hypotheses as substantive rather than generic positive-rates coverage.

On branch `research/positive-rates-conjecture`:

- `research/active/positive-rates-conjecture/programme-established-results.md`;
- `research/active/positive-rates-conjecture/state.md`;
- Meetings 025 through 030.

Repository conclusions are evidence to be independently checked before they carry a new inference.

## Exact target interfaces

A candidate `A/B` method must attach explicitly to at least one of the following, or supply a materially different target-level architecture that bypasses all of them.

### 1. Signed boundary transmission / connected renewal

The sharpest residual object of the fixed-filter route is

\[
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
 \bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt,
\]

on the **actual connected orbit**. Both scalar kernels change sign. A bridge for this route must preserve the two-time cancellation strongly enough to produce summable/geometric connected coefficients. Taking absolute values before the integrations does not qualify.

### 2. Common-coupling convective escape

Finite disagreements locally erase, the rightmost disagreement is nonincreasing, and every fixed site couples permanently; unresolved survival can occur only by convective escape to `-infinity`. A useful coupling/front method must decide extinction versus such escape rather than merely reproving fixed-site coupling.

### 3. Stationary boundary-control diameter

The exact occupation-control hierarchy gives decreasing diameters `D_N(h)`. Proving `D_N(h) -> 0` for every local `h` would yield invariant-law uniqueness. Additive correctors without cross-block dependence are already known not to improve the Bellman endpoints.

### 4. Shift / connected-tail decay

One-/two-step zero-boundary shift agreement, `Gamma_M -> 0`, general `J_{x,r} -> 0`, `(J-SPEC)`, and connected-tail summability remain unresolved. Bare tail-shift reformulations alone do not clear the restart bar.

## Hard obstruction ledger

Treat the following as hard evidence against equivalent proposals:

- nearest-neighbour scalar edge-product/coboundary Foster certificates are ruled out at a hard residual point by exact balanced circulation;
- no depth-uniform finite linear generator-mode closure contains the common-mass transfer;
- the natural positive raw coefficient norms, including the component-count refinement, cannot be uniformly nonexpansive in depth;
- the exact trajectory-valued spatial kernel has Dobrushin total-variation coefficient one;
- additive Bellman correctors without cross-block dependence cannot improve the endpoints;
- another generic norm, reversible comparison, filter optimization, larger coefficient table, bare tail-shift argument, common-coupling occupation variant, or generic Bellman-corrector search does not restart the stopped programme.

Gray 1982 is now in the toolbox. Its edge process should be assessed seriously, but its success under attractiveness/repulsiveness does not by itself address the residual nonmonotone chamber. The assessment task is to identify whether any part of its ordered-edge/local-repair architecture has a mathematically credible replacement there.

## Required output

Create and commit:

`research/active/ergodicity-methods-toolbox/assessment/positive-rates-method-audit.md`

It must contain:

1. **Complete disposition table.** Every final toolbox method receives exactly one rating:
   - `A` actionable;
   - `B` plausible architecture;
   - `C` auxiliary/diagnostic;
   - `X` blocked by a specific obstruction or hypothesis failure;
   - `N` no credible contact.
2. **Shortlist of at most six A/B methods**, ranked by expected research value.
3. For every shortlisted method, an explicit **bridge lemma** stated mathematically and attached to one of the four live interfaces above or to a genuinely different target-level theorem chain.
4. The implication chain from the bridge to a target-level advance.
5. The exact established obstruction it avoids.
6. A **cheapest-first falsification test**: exact finite-state calculation, small-depth operator computation, coupling sanity check, or sharply bounded source inspection that could kill the route quickly.
7. A separate warning whenever a candidate is merely a repackaging of an architecture stopped in Meetings 025--030.

For every `A/B/C/X` row, name the target interface and cite the relevant repository/source pointer. `A` or `B` without a bridge statement is invalid.

## Scope discipline

- No broad new literature search.
- Open primary sources only when a toolbox page is insufficient to formulate or falsify an adaptation precisely.
- Do not create or edit toolbox entries, `docs/`, or `mkdocs.yml`.
- Do not restart the positive-rates proof programme inside this assignment. Perform only the minimum calculations needed to classify or falsify candidate architectures.
- Do not pad the shortlist. A conclusion that no method clears `B` is acceptable if supported method by method.
- Gray 1986 remains a source-access hold from wave seven. Do not turn it into an un-audited method page or use abstract-only details as a load-bearing theorem.

## Handoff

After committing the audit, write `students/student-g/007-handoff.md` with:

- audit commit;
- count of A/B/C/X/N dispositions;
- ranked A/B shortlist;
- the single cheapest falsification experiment you recommend running first;
- any apparently promising method killed by an exact obstruction.

Then stop. The next step is hostile cross-review, not another collection or proof assignment.
