# Positive-rates applicability audit

Date: 2026-08-17

## Scope and rating standard

This audit assesses the frozen 74-method ergodicity toolbox against the positive-rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS. It is an applicability assessment, not a literature-collection wave and not a restart of the stopped proof programme.

Ratings follow `assessment-protocol.md`:

- **A**: actionable; a concrete bridge lemma, not known false and not equivalent to an exhausted route, would materially advance the target.
- **B**: plausible architecture; a coherent architecture survives the obstruction ledger, but several substantial bridges are still missing.
- **C**: auxiliary/diagnostic; useful for a sublemma, comparison, or falsification test, but not a target-level architecture.
- **X**: blocked by a specific hypothesis failure, exact obstruction, or exhausted equivalent route.
- **N**: no mathematically credible contact with the live target interfaces.

An `A` or `B` rating is invalid without an explicit bridge lemma. For every `A/B/C/X` disposition below, the final matrix names a target interface and a repository or source pointer.

## Positive-rates target interfaces

### PR1: signed boundary transmission / connected renewal

At the strict residual point used in the stopped programme, the sharp connected-renewal residual object is the signed two-time boundary-transmission operator

\[
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
 \bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
\]

Both scalar kernels change sign and the input is the actual connected orbit. A bridge on this route must retain the two-time cancellation strongly enough to make the connected renewal coefficients summable or geometric. Taking absolute values before the integrations does not qualify. See positive-rates Meetings 026--030 and `programme-established-results.md`, Sections 2 and 4.

### PR2: common-coupling convective escape

For a finite initial disagreement set under the common-uniform coupling, the rightmost disagreement is nonincreasing and every fixed site couples permanently almost surely. Survival can therefore occur only by convective escape to minus infinity. A useful coupling/front method must decide extinction versus such escape, not merely reprove fixed-site coupling. See `programme-established-results.md`, Section 1, and the final positive-rates `state.md`.

### PR3: stationary boundary-control diameter

For local `h`, the stationary occupation-control hierarchy gives decreasing diameters

\[
D_N(h)=\sup_{m\in\mathcal K_N}m(h)-\inf_{m\in\mathcal K_N}m(h).
\]

Proving `D_N(h) -> 0` for every local `h` yields invariant-law uniqueness. Additive Bellman correctors without cross-block dependence cannot improve the endpoints; any useful new bridge must exploit genuinely cross-block information. See `programme-established-results.md`, Sections 1 and 3.

### PR4: shift / connected-tail decay

One-/two-step zero-boundary shift agreement, `Gamma_M -> 0`, general `J_{x,r} -> 0`, `(J-SPEC)`, and connected-tail summability remain open. A bare tail-shift reformulation does not clear the restart bar. See positive-rates Meetings 025--030 and the final `state.md`.

A method may also qualify through **PR5: a materially different target-level architecture** that bypasses PR1--PR4, but the implication chain must make the bypass explicit.

## Hard obstruction ledger used in the audit

The following are treated as established negative evidence rather than targets for another renamed attempt:

1. nearest-neighbour scalar edge-product/coboundary Foster certificates are ruled out at a hard residual point by exact balanced circulation;
2. no depth-uniform finite linear generator-mode closure contains the common-mass transfer;
3. the natural positive raw coefficient norms, including the component-count refinement, cannot be uniformly nonexpansive in depth;
4. the exact trajectory-valued spatial kernel has Dobrushin total-variation coefficient one;
5. additive Bellman correctors without cross-block dependence cannot improve the stationary endpoints;
6. another generic norm, reversible comparison, filter optimization, larger coefficient table, bare tail-shift argument, common-coupling occupation variant, or generic Bellman-corrector search does not restart the stopped programme;
7. finite-time Hamming contraction is not available at the hard near-East calibration point on the tested interval, while fixed-site common-coupling agreement is already known and is insufficient because convective escape remains possible.

Pointers: `research/active/positive-rates-conjecture/programme-established-results.md`; final `state.md`; Meetings 025--030 on branch `research/positive-rates-conjecture`.

## Complete disposition table

_To be filled after every frozen live method page has been inspected._

## Ranked A/B shortlist

_To be filled after the complete disposition table is fixed._

## Repackaging warnings and cheapest-first tests

_To be filled with the shortlist._
