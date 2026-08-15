# Proof spine

This file is maintained by the Professor.

## Main target

For one-dimensional hard FA-1f with vacancy density `q in (0,1)`, started from the configuration `eta^{0}` with exactly one vacancy at the origin, prove

$$
P_t f(\eta^{0})\longrightarrow \mu_p(f),\qquad p=1-q,
$$

for every local function `f`.

Equivalently, it is enough to prove convergence of all centered monomials

$$
P_t\chi_A^*(\eta^{0})\longrightarrow 0,
\qquad
\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p),
$$

for every nonempty finite `A`.

## Obstruction map

### E0. Centered-moment reduction

**Statement.** Since centered monomials form a basis for local functions and `mu_p(chi_A^*)=0` for nonempty `A`, the main target follows from decay of every nonempty centered monomial.

**Status:** verified/standard.

**Owner:** Professor.

**Decisive pointer:** `state.md` and the centered basis in the canonical patch paper, Section 5.4.

### E1. Exact positive finite-set dual after the harmonic transform

**Claim.** Define

$$
H(A,\eta)=q^{-|A|}\chi_A^*(\eta),
$$

for finite nonempty `A`. There is a Markov process `(\mathcal A_t)` on finite nonempty subsets of `Z` whose generator is

$$
\mathcal G g(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq\{i-1,i+1\}}
q^{|R|}p^{2-|R|}
\,g\bigl((A\setminus\{i-1,i+1\})\cup R\bigr)
-g(A)
\right].
$$

In words: every active site `i` rings at rate one and refreshes membership of its two neighbours independently to Bernoulli(`q`); site `i` itself is retained.

The claimed duality is

$$
P_t\chi_A^*(\eta)
=
q^{|A|}\mathbf E_A\left[
q^{-|\mathcal A_t|}\chi_{\mathcal A_t}^*(\eta)
\right].
$$

For the one-vacancy configuration `eta^{0}` this becomes

$$
P_t\chi_A^*(\eta^{0})
=
q^{|A|}
\left(
1-q^{-1}\mathbf P_A(0\in\mathcal A_t)
\right).
$$

**Status:** claimed by Professor; first student check pending.

**Owner:** Graduate Student A.

**Decisive pointer:** `notes/professor-initial-reduction.md`; forthcoming Student A note.

**If false:** revise the programme immediately; do not build downstream work on this representation.

### E2. Local-density convergence for the transformed finite-set process

**Desired statement.** For every finite nonempty initial set `A`,

$$
\mathbf P_A(0\in\mathcal A_t)\longrightarrow q.
$$

By E1 this is equivalent to the active target at the centered-monomial level.

**Status:** open.

**Owner:** unassigned beyond Student A's reconnaissance of structure.

**What is currently unknown:** whether `\mathcal A_t` has an exploitable invariant-law, recurrence, regeneration, front, or comparison structure from finite initial sets; whether this process is already known under another name; whether the transformation genuinely reduces difficulty.

### E3. A model-specific mechanism implying E2

This is the real theorem-level missing edge. Candidate mechanisms are not yet part of the spine until they survive Student A's structural analysis.

Potential forms that would count:

- a regeneration/coupling theorem for the transformed process;
- control of its left/right fronts plus mixing behind the front;
- a duality or comparison with a better understood branching-coalescing system;
- an exact relation to an existing finite-seed convergence theorem strong enough to imply E2.

**Status:** open, not yet formulated sharply enough to assign as a theorem.

## Current first unresolved edge

**E1 is the immediate bottleneck.** It is a cheap exact calculation and must be settled before investing in E2/E3.

If E1 is correct, Student A must also test the first nontrivial multi-particle transitions and identify whether the transformed process is structurally simpler or merely a restatement. That assessment determines the next spine revision.

## Mathematically distinct alternative route

If the centered `h`-transform proves sterile, return to the canonical patch representation before normalization and retain the consistency probabilities in the skeleton measure. This would seek direct model-specific substitutes for the two uses of uniform pure deaths in Theorem C: suppression of late successful interactions and relaxation of terminal dependence. This is distinct from the closed Bernoulli sibling-cancellation route, but it is not the current bottleneck.

## Routes eliminated

- 1D Bernoulli-quench sibling cancellation: closed project route; do not retry.
- 2D FA-1f local signed-move cancellation for the relaxation logarithm: different target and closed route.
- 2D nearest-vacancy/electrical-capacity observable: different target and closed route.

## Revision note

Initial spine. The central new candidate reduction is the Professor's `h`-transform calculation. No claim is made yet that E2 is easier than the original problem.