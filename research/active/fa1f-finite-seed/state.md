# Programme state

This is the Professor-owned re-entry document for the active scientific direction.

## Direction

Title: 1D hard FA-1f from a finite seed

Branch: `research/fa1f-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate-student lineage: Graduate Student A

Workspace: `research/active/fa1f-finite-seed/`

Latest group meeting: `meetings/001-h-transform-review.md`

## Target

Fix vacancy density `q in (0,1)` and `p=1-q`. Consider one-dimensional hard FA-1f on `Z`, with state `0` vacant/facilitating and state `1` occupied/calm. Let `eta^{0}` be the configuration with a single vacancy at the origin and all other sites occupied.

Prove that for every local function `f`,

$$
P_t f(\eta^{0}) \longrightarrow \mu_p(f) \qquad (t\to\infty),
$$

where `mu_p` is the Bernoulli product equilibrium law with calm-state density `p`.

The natural later extension is every deterministic finite nonempty vacancy set, but the active target is the single-vacancy case.

## Why this target

This is a canonical unresolved out-of-equilibrium problem for FA-1f, not a theorem manufactured around the patch method. Martinelli--Shapira--Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems* (arXiv:2510.20461, 2025), Conjecture 1, conjecture convergence to equilibrium from every initial law which almost surely contains at least one infection and explicitly single out the single-infection initial condition as natural. Their Section 6 gives preliminary finite-vacancy results rather than the conjectured convergence theorem.

The canonical patch paper `paper/`, *Patch representations and convergence for facilitated spin systems*, Section 8.2 independently identifies convergence from finitely many facilitating states without uniform deaths, including hard FA-1f from finitely many vacancies, as an unresolved problem requiring model-specific control.

The target builds directly on the principal's prior mathematics: for FA-1f the patch threshold is exactly `p`, and the centered-monomial basis from Theorem B has nonnegative semigroup coefficients.

## Relation to closed FA-1f routes

This programme is not the closed 1D Bernoulli-quench sibling-cancellation route. The target starts from one deterministic vacancy and the current proof line works with the canonical successful-skeleton/patch representation rather than a generation-by-generation signed sibling majorant.

Graduate Student A did find an exact overlap between the local algebra of the verified centered `h`-transform and the old sibling route: the same parameter `a=-p/q`, the same two-neighbour factorization, and the same maximal two-sibling event appear. Therefore any future attempt to extract progress by taking absolute values of those two refreshed sibling weights and seeking a contraction is explicitly closed. This overlap is recorded in `students/student-a/001-centered-h-transform.md`, Section 13.

The closed 2D relaxation-logarithm and nearest-vacancy capacity routes concern a different dimension, theorem, and mechanism.

## Main obstruction

Hard FA-1f is non-attractive, and the canonical patch-paper convergence theorem does not apply because it requires a uniform environment-independent creation of facilitating states, which becomes a uniform pure-death component in the dual. Hard FA-1f has no such component.

Theorem C uses uniform pure deaths twice: to suppress successful interactions after a cut time by a backward-chain survival factor, and to control terminal end-factor dependence when there are no late interactions. Section 8.2 states that a hard-model extension requires model-specific replacements for both bounds. Finite-seed point masses are also not usefully bracketed by nondegenerate product laws in the centered-moment order.

## Present approach

The first approach, an exact centered `h`-transform to a positive finite-set process, has been verified but demoted as a proof strategy. Student A showed that on finite cycles it is an invertible similarity transform of the transpose FA-1f generator; the transformed process has no current monotone/additive/front simplification sufficient for finite-seed convergence.

The active approach now returns to the canonical successful-skeleton proof **before normalization by patch consistency probabilities**. Define

$$
\widehat C(P)
=
\mathbf E_P\left[F(P)\mathbf 1_{\operatorname{Con}(P)}\right]
=
\mathbf P_P(\operatorname{Con}(P))C(P),
$$

with the analogous end-patch amplitude. The aim is to expose the actual probability cost of a hard-FA successful skeleton and test whether full branching geometry creates a useful loss which the normalized patch contributions hide.

This is currently only a candidate mechanism. A single backward-chain heuristic is not enough because every successful FA-1f record has both neighbours as target and creates a full family of source/target patches. Assignment 002 tests the complete first composition in the actual singleton equilibrium deviation.

## Proof spine

Path: `proof-spine.md`

Current bottleneck: E2, the exact unnormalized hard-FA patch/skeleton expansion and its first full branching-composition test.

If E2 survives, the next theorem-level edges are E3a late-interaction control and E3b terminal-dependence relaxation without uniform pure deaths.

## Mathematical state

### Verified

- The canonical patch paper proves patch factorization and the exact patch representation.
- For FA-1f, the canonical paper proves patch positivity and patch threshold `p^*=p`.
- The canonical paper proves positivity of the semigroup in the centered-monomial basis.
- Martinelli--Shapira--Toninelli's Conjecture 1 contains the active target as a special case.
- The centered `h`-transform / finite-set dual reduction from the initial Professor calculation is correct for every finite initial dual set, including nonexplosion and the infinite-volume semigroup passage. Decisive check: `students/student-a/001-centered-h-transform.md` Sections 1--4.

### Claimed

- No new theorem-level claim from the unnormalized patch route yet. The local `widehat C` formulas and full skeleton bookkeeping are assignment 002 rather than established facts in the active workspace.

### Conditional

- Any future E3 estimate based on unnormalized patch amplitudes is conditional on E2 being derived exactly and showing a target-level handle beyond the verified `h`-transform.

### Refuted or eliminated

- The previously closed Bernoulli-quench sibling-cancellation route remains closed.
- The centered `h`-transform as a standalone proof strategy is demoted: it is an exact positive reformulation but no current simplification. Evidence: `students/student-a/001-centered-h-transform.md` Sections 7--15 and `meetings/001-h-transform-review.md`.
- The previously closed 2D signed-move and nearest-vacancy-capacity routes are not part of this programme.

### Open

- Exact unnormalized hard-FA patch amplitudes and full successful-skeleton measure bookkeeping.
- Whether the apparent criticality of one backward outgoing chain survives the first full branching composition.
- Whether consistency probabilities plus one-dimensional overlap/coalescence/recurrence yield a late-interaction estimate unavailable in the normalized representation.
- Whether the unnormalized patch expansion is merely another resummation of the verified `h`-transform and therefore adds no leverage.
- If E2 survives, model-specific replacements for late-interaction suppression and terminal-dependence relaxation.

## Current bottleneck

Determine whether the unnormalized successful-skeleton expansion creates any real target-level gain after all patches generated by the first two successful records are included. The first-composition calculation is deliberately chosen to kill the route early if it only reproduces the old sibling algebra or a critical positive transform with no additional geometry.

## Strongest positive evidence

The patch construction is canonical and exact, and the hard-model failure of Theorem C is sharply localized. Restoring consistency probabilities changes the object being estimated: instead of normalized local contributions alone, one sees the probability cost of the successful skeleton. This directly addresses the missing pure-death majorant rather than changing coordinates abstractly.

## Strongest negative evidence

Student A's assignment 001 showed that a very clean positive reformulation can still be only an invertible change of coordinates. The same local two-neighbour algebra also overlaps exactly with the permanently closed sibling route. The patch alternative therefore has to survive a full branching-composition test in the actual centered target quantity; a chain-only `e^{-Delta}` factor is not evidence of progress.

## Current assignment

Graduate Student A: derive the unnormalized hard-FA patch representation exactly from Theorem 4.4, compute all local amplitudes and skeleton intensities, write the singleton equilibrium deviation in that expansion, and evaluate skeletons with zero, one, and two successful records including the full patch family. Determine whether the first composition gives a real gain or only reproduces E1 / the closed sibling mechanism.

Exact assignment: `students/student-a/assignment-002.md`.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `students/student-a/001-centered-h-transform.md`, Sections 1--4 and 7--15; meeting judgment in `meetings/001-h-transform-review.md`.

Consecutive no-narrowing meetings: 0

Stagnation consultation pending or completed: none

## Files

- `proof-spine.md`
- `notes/professor-initial-reduction.md`
- `literature.md`
- `audit-log.md`
- `meetings/001-h-transform-review.md`
- `students/student-a/001-centered-h-transform.md`
- `students/student-a/assignment-002.md`

## Principal-facing brief

### Active target

Single-vacancy convergence to equilibrium for 1D hard FA-1f for every `q in (0,1)`.

### What changed mathematically

E1 was verified exactly, but the transformed process was shown to be an invertible finite-volume coordinate transform with no present front/monotonicity/BABP simplification. The active proof strategy therefore pivots to the unnormalized successful-skeleton/patch expansion.

### What the Professor directly inspected

`students/student-a/001-centered-h-transform.md` in full, the current state and proof spine, and the original Professor reduction. The decisive structural evidence is the finite-volume similarity, exact front identities, non-attractiveness/non-additivity, BABP form comparison, and closed-route algebra overlap in Student A's Sections 7--15.

### Current proof-spine bottleneck

E2: exact unnormalized hard-FA patch amplitudes plus the first full branching-composition calculation in the singleton equilibrium deviation.

### Strongest reason to continue

The target remains strong and the patch route attacks the precise point where the canonical convergence proof fails.

### Strongest reason to doubt the direction

The first clean reduction was sterile, and the local patch algebra may again collapse to an exact critical reformulation or the already closed sibling mechanism.

### State narrowed since last group meeting

`yes`: E1 was verified and simultaneously eliminated as the main proof mechanism; the exact closed-route overlap was identified.

### Direction

`continue`, with a proof-strategy pivot inside the same target.

### What happens next

Graduate Student A performs assignment 002. No second student is needed before this decisive composition test.

### Pending audit or stagnation consultation

None.

### Question for the principal

None.