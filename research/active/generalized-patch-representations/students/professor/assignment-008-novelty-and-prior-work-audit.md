# Assignment 008: novelty and closest-prior-work audit for generalized patch representations

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 007 ended `CONTINUE-NATURAL-THREE-STATE-SUBCLASS`. The mathematical package is now stable enough for the literature audit repeatedly deferred in Meetings 004--007.

This is a literature/novelty block, not a new proof block. Applications, `d>3` coefficient algebra, convergence, and multi-site updates remain out of scope until the audit ruling.

## Goal

Determine which parts of the generalized finite-state patch programme are standard, which are already present in equivalent language, and which remain plausibly new.

The audit must be willing to return a negative novelty finding. Correct mathematics is not automatically a research contribution.

## Fixed mathematical package to compare

### A. Arbitrary finite-state representation

For finite local state space `E={0,...,d-1}` and bounded finite-range single-site replacement dynamics:

1. reference-state indicator tensor basis;
2. exact signed local Feynman--Kac dual with typed active configurations;
3. nonempty successful record `(i,t,r,tau)` revealing pre-source type and typed target while hiding post-source outcome;
4. one-site typed spacetime patches;
5. target conflicts producing cemetery;
6. exact killed/noncemetery weighted patch factorization;
7. explicit patch representation with bulk/end separation.

### B. Exact bulk transfer positivity

The signed interior transfer is

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset),
\]

and typed bulk patch positivity is exact nonnegativity of the four local semigroup numerator families on realizable descriptors.

### C. Boundary-complete `d=3` theorem

Boundary completeness forces `K` Metzler and reduces positivity to `OI` Markov-semigroup expectations. Every remaining numerator has an exact finite spectral test: endpoints plus at most one explicit interior critical value, including degenerate spectra.

### D. Natural exact subclass

For exchange-symmetric reference-neighbour dynamics

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\]

with exchange-symmetric nonempty-target coefficients, boundary-complete typed positivity is equivalent to

\[
c\ge a,
\]

and, for every outgoing row `p=(p0,p1,p2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

The criterion is genuinely non-binary; it does not require `p_1=p_2`.

Destination-rate refresh chains form a repeated-spectrum sibling subclass.

## Part A. Search vocabulary and predecessor map

Search literature under multiple terminologies, including at least:

- finite-state interacting particle systems / spin systems / multitype particle systems;
- monomial, indicator, tensor-product, polynomial, or moment duality;
- signed duality and Feynman--Kac duality;
- graphical duals with branching/retyping particles;
- hidden marks / partial revelation / conditional graphical constructions;
- Poisson skeleton conditioning / cluster or block factorization;
- transfer matrices for local Feynman--Kac weights;
- positivity-preserving semigroups / eventual positivity / cone invariance;
- lumpable Markov chains, symmetric Markov chains, refresh chains;
- multistate extensions of binary spin-system duality.

Search both classical IPS sources and adjacent probability/positive-systems literature when the same mathematics may use different language.

## Part B. Separate novelty statuses

Do not collapse the package into one yes/no verdict. Classify at least:

1. finite-state typed signed duality;
2. killed typed patch factorization/representation;
3. transfer-matrix bulk positivity formulation;
4. exact `d=3` finite spectral criterion;
5. exchange-symmetric exact algebraic criterion;
6. the combined framework as a method.

For each item use one of:

- `known / directly subsumed`;
- `known ingredients, assembly plausibly new`;
- `plausibly new theorem/mechanism`;
- `unresolved from literature found`.

## Part C. Closest source reconstruction

For every source that appears close, reconstruct enough mathematics to compare actual hypotheses and conclusions. Do not rely on abstracts or terminology resemblance.

In particular determine whether any source already:

- conditions on a coarser graphical skeleton while averaging hidden local update types before taking absolute values;
- handles typed target conflicts by killing/cemetery in a factorized representation;
- identifies the empty-target coefficient matrix as the exact signed interior transfer after Feynman--Kac cancellation;
- states positivity of all bulk patches through finite local semigroup inequalities;
- obtains the same three-state spectral or symmetric endpoint criterion.

## Part D. Literature chronology

Check predecessor and successor literature. If a modern paper independently contains the same theorem, record that even if the older classical sources do not.

The audit should distinguish:

- method already known before the principal's binary patch paper;
- finite-state generalization already known after/beside it;
- genuinely new consequence of combining standard pieces.

## Part E. Ruling on next programme block

The literature result controls sequencing.

### If the framework/theorem remains plausibly new

Queue **applications as the next active mathematical block**. Do not insert another generic `d>3` criterion block first.

The application block should seek a genuinely non-binary finite-state single-site replacement IPS whose typed coefficients satisfy either:

- the exchange-symmetric / refresh exact criterion; or
- the exact general boundary-complete `d=3` spectral criterion.

### If the core framework is directly subsumed

Do not proceed to applications merely to decorate a known mechanism. Reassess whether there is a narrower theorem/application with independent value.

### `d>3` ordering

A generic `d>3` tractable-criterion block remains deferred unless:

- an application naturally requires more than three states; or
- the literature audit identifies the arbitrary-`d` criterion as the part with the strongest novelty/importance.

## Mandatory sources

At minimum inspect:

- the canonical binary patch paper under `paper/` as the project benchmark;
- standard IPS duality references already cited there;
- classical multitype/finite-state IPS duality literature;
- relevant Feynman--Kac / branching duality literature;
- relevant Markov-chain lumpability and positive-semigroup literature for the criterion-level claims.

Use web/literature search. Cite exact sources and theorem/proposition numbers where possible.

## Pre-registered outcomes

Return exactly one programme-level ruling, while preserving per-component novelty statuses.

### `CONTINUE-TO-APPLICATIONS`

The core generalized patch mechanism or at least one load-bearing theorem remains plausibly new and substantive after closest-prior-work comparison. Queue a concrete application-search block next. Do not insert generic `d>3` algebra first.

### `STOP-GENERALIZATION-SUBSUMED`

The generalized representation/positivity mechanism is already directly present in prior work in equivalent mathematical form, and the `d=3`/symmetric criteria do not provide a sufficiently independent contribution. Record exact sources and stop this programme before applications.

### `NARROW-TO-SPECIFIC-NEW-THEOREM`

The general mechanism is largely known, but one specific theorem (for example killed typed factorization, exact spectral criterion, or symmetric endpoint criterion) remains plausibly new and independently worthwhile. Narrow the project to that theorem before applications.

### `UNRESOLVED-NOVELTY-AUDIT`

The closest sources leave one precise novelty comparison unresolved. Record the exact missing source/theorem comparison; do not proceed to applications until resolved.

## Anti-loop rules

Do not:

- infer novelty from unfamiliar terminology;
- count the finite-state tensor expansion itself as new without evidence;
- treat a correct but standard Markov spectral calculation as a project contribution merely because it is exact;
- search only literature using the word `patch`;
- start applications before the audit ruling;
- enlarge to `d>3` during this audit;
- modify `docs/entries/`, `docs/meta/`, or `mkdocs.yml`.

## Durability

Commit source-by-source comparison notes when they materially change the novelty picture.

Final report:

`students/professor/008-novelty-and-prior-work-audit.md`.

Final handoff:

`students/professor/008-handoff.md`.

No writes to `main`.
