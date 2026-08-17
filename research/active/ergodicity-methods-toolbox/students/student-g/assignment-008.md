# Student G Assignment 008: hostile cross-review of FA-1f/East shortlist

Date: 2026-08-17

This is the hostile cross-review required by `assessment-protocol.md`. It is **not** a new primary audit, literature-collection assignment, or proof-programme restart.

## Goal

Independently attack the Professor's five A/B candidates from the completed FA-1f/East applicability audit. Review only the shortlist and the exact target/obstruction material needed to test those bridges. Do not reread or rerate the full 74-method matrix.

For each candidate return exactly one ruling:

- **PASS** — the bridge remains genuinely open after hostile attack;
- **DEMOTE** — the method may remain auxiliary/diagnostic, but its stated A/B bridge is not presently a credible target-level architecture;
- **KILL** — a precise hypothesis failure, established obstruction, exhausted equivalence, or conclusion mismatch defeats the bridge in its stated form.

A PASS requires one sentence explaining why the bridge survives the attack. A KILL requires a precise mathematical reason. DEMOTE must identify what useful content remains and why it no longer clears the A/B bar.

## Required reading

On branch `research/ergodicity-methods-toolbox`:

- `research/active/ergodicity-methods-toolbox/assessment-protocol.md`, especially Sections 3 and 5;
- `research/active/ergodicity-methods-toolbox/assessment/fa1f-east-method-audit.md`, especially its final shortlist and bridge-lemma section;
- `research/active/ergodicity-methods-toolbox/meetings/019-fa1f-east-primary-audit-complete.md`;
- the five live toolbox pages named below.

Target/obstruction material:

- branch `agent/fa1f-chronology-sign-route`, especially `docs/entries/chronology-averaged-sign-route-for-fa-1f.md`;
- branch `research/fa1f-finite-seed`, `research/active/fa1f-finite-seed/state.md` and `proof-spine.md`;
- live `docs/entries/east-distinguished-zero-screening.md`.

Repository conclusions are evidence, not authority. Recheck every load-bearing inference used to kill or pass a candidate.

## The five candidates under review

### 1. East distinguished-zero screening — rated A

Bridge to attack: construct two-sided FA stopping times and a random screened interval containing the observation set, with width `o(t)`, such that conditional on the screen variables the law inside is independent of the exterior past up to an error tending to zero uniformly enough to combine with the known positive FA finite-volume gap.

Attack points:

- whether two-sided facilitation makes the proposed screen circular rather than regenerative;
- whether the stopping variables themselves depend on the region claimed to be screened;
- whether the required `o(t)` width and error control are actually sufficient once the FA gap constant is inserted;
- whether the bridge merely restates the original convergence problem in conditional-independence language.

### 2. Refined non-diagonal discrepancy coupling — rated B

Bridge to attack: construct a genuinely new two-history coupling/permutation of update marks, allowed to pair different microscopic updates, that proves the endogenous three-site cross-product inequality

`P(100) P(010) >= P(000) P(110)`

and its reflection, or a strictly weaker chronology inequality already known to imply the quench target.

Attack points:

- whether marginal-rate preservation plus the FA constraint leaves any nontrivial freedom beyond same-mark coupling;
- whether the proposed switching rule closes under adjacent updates rather than recreating the failed isolated-insertion cone;
- whether the cross-product inequality is actually preserved by the coupled evolution or only observed numerically in small cycles;
- whether the construction silently exogenizes boundary facilitation.

The Professor's cheap exact-cycle check found no violation on sizes 5--8 in the sampled unresolved regime. Treat that as weak evidence only.

### 3. Information percolation / backward histories — rated B

Bridge to attack: build state-adaptive minimal backward supports for FA and prove that histories still carrying time-zero information are sparse enough under the Bernoulli quench to make the local law asymptotically independent of the start, without requiring total ancestor extinction.

Attack points:

- whether an FA update admits sufficiently many genuinely oblivious marks once legality itself depends on neighboring history;
- whether defining a minimal support forces the same branching/conservative transfer already exhausted in the dual programme;
- whether red-history sparsity can be controlled without taking absolute values or replacing endogenous facilitation by an external environment;
- whether the intended conclusion is strong enough for the infinite-volume Bernoulli quench rather than finite-volume mixing from warm starts.

### 4. Front regeneration / renewal — rated B

Bridge to attack: construct two-sided vacancy-front renewal times that prevent information from the exterior past from re-entering a neighborhood of the observation block, with tails strong enough that known FA equilibrium coercivity finishes the argument.

Attack points:

- whether there is a canonical front in the translation-invariant Bernoulli quench;
- whether two fronts can isolate a block without their future motion depending on the enclosed/exterior configurations in a circular way;
- whether the construction is materially different from the closed finite-seed front idea, or whether it simply assumes the missing regeneration theorem;
- whether a moving-frame or speed statement is being mistaken for actual memory erasure.

### 5. State-dependent dynamical disagreement percolation — rated B

Bridge to attack: under a coupling of the Bernoulli-quench process with equilibrium, construct a block-scale disagreement transmission process using the **actual vacancy environment** and prove subcritical connectivity from time zero to a fixed observation block, without a worst-case Dobrushin domination.

Attack points:

- whether disagreement transmission can be dominated without destroying the state dependence that is supposed to help;
- whether the law-dependent block process is stationary/decoupled enough for a valid subcritical percolation argument;
- whether conditioning on vacancy-rich blocks introduces exactly the endogenous-boundary dependence already unresolved;
- whether the route collapses into ordinary disagreement percolation, which is too strong because of the all-ones trap.

## Review standard

For each candidate explicitly test all four failure modes required by the protocol:

1. hidden theorem/source hypotheses;
2. equivalence to an exhausted route;
3. conflict with an exact obstruction in the FA chronology/finite-seed records;
4. mismatch between the actual method conclusion and the Bernoulli-quench target.

Do not promote a candidate because the bridge sounds natural. PASS only if the specific mathematical bridge is not already false, circular, or equivalent to stopped work.

## Required output

Create and commit:

`research/active/ergodicity-methods-toolbox/assessment/fa1f-east-hostile-review-g.md`

Use one subsection per candidate with exactly:

- **RULING:** PASS / DEMOTE / KILL
- **Attack**
- **Load-bearing reason**
- **If PASS:** one sentence stating why the bridge remains genuinely open
- **If DEMOTE:** the strongest remaining auxiliary use
- **If KILL:** the exact obstruction/hypothesis failure
- **Cheapest next check**, only if it would materially distinguish PASS from failure

Then write `students/student-g/008-handoff.md` containing the five rulings, the most important kill/demotion reason, and at most **two** FA candidates you believe should survive into Professor synthesis.

## Scope discipline

- No full 74-method rerating.
- No broad new literature search.
- Open a primary source only when needed to test a hidden hypothesis of one of these five methods.
- Do not edit toolbox entries, `docs/`, `mkdocs.yml`, or either primary audit.
- Do not run a proof programme. Bounded exact computations are allowed only as hostile falsification checks.
- Do not review the positive-rates shortlist; the Professor owns that cross-review.

After the handoff, stop. The next step is Professor synthesis after both hostile reviews exist.