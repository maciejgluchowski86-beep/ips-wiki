# Programme state

This is the Professor-owned re-entry document for the active scientific direction.

## Direction

Title: 1D hard FA-1f from a finite seed

Branch: `research/fa1f-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate-student lineage: Graduate Student A

Workspace: `research/active/fa1f-finite-seed/`

Latest group meeting: none yet

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

## Why this is not a reopened closed FA-1f route

The closed 1D FA-1f route studied a Bernoulli-quench sibling-cancellation mechanism. Its decisive failure was that a cancellation visible at two generations disappeared at the next nontrivial composition, restoring the critical scaling. That route is not being retried.

The present target has a different initial condition and a different proposed reduction. It starts from one deterministic vacancy, not a homogeneous Bernoulli quench, and uses the canonical centered-moment positivity to seek a positive Markov dual via an `h`-transform. No sibling cancellation, density-derivative expansion, or generation-by-generation contraction is assumed. If the `h`-transform reduction is correct but gives no leverage, it will be abandoned rather than reinterpreted as the closed sibling route.

The closed 2D relaxation-logarithm and nearest-vacancy capacity routes concern a different dimension, a different theorem (spectral-gap asymptotics), and a Dirichlet-form/capacity mechanism. They are irrelevant to the present proof spine except as negative lessons.

## Main obstruction

Known high-density out-of-equilibrium arguments use attractiveness/contact-process comparison, finite-volume mixing, or related devices that are not available uniformly for all `q`. Hard FA-1f is non-attractive.

The patch paper's Theorem C does not apply: its convergence mechanism requires a uniform environment-independent creation of facilitating states, which becomes a uniform pure-death component in the dual. Hard FA-1f has no such component. Section 8.2 of the canonical paper states that the proof would need model-specific replacements for both late-interaction suppression and end-factor relaxation. Moreover, finite-seed point masses are not usefully bracketed by nondegenerate product laws in the centered-moment order.

## Present approach

Exploit the especially simple centered generator of FA-1f. Put

$$
\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p),
\qquad h(A)=q^{|A|}.
$$

The Professor's initial calculation in `notes/professor-initial-reduction.md` claims that after conjugation by `h`, the centered-monomial semigroup is dual to a genuine finite-set Markov process: every active site `i` rings at rate one and refreshes membership of its two neighbours independently to Bernoulli(`q`), leaving all other memberships unchanged. If this is correct, then

$$
P_t\chi_A^*(\eta^{0})
=q^{|A|}\left(1-q^{-1}\mathbf P_A(0\in\mathcal A_t)\right).
$$

Thus the target reduces to the local-density statement

$$
\mathbf P_A(0\in\mathcal A_t)\longrightarrow q
$$

for every finite nonempty initial active set `A` of this transformed process.

This reduction is currently `claimed`, not verified. Graduate Student A's first task is to check it from first principles and determine whether the transformed process has genuinely more tractable structure or is merely an equivalent reformulation.

## Proof spine

Path: `proof-spine.md`

Current bottleneck: establish and assess the centered `h`-transform reduction, then identify a target-relevant mechanism for local convergence of the transformed finite-set process.

## Mathematical state

### Verified

- The canonical patch paper proves patch factorization and the exact patch representation.
- For FA-1f, the canonical paper proves patch positivity and patch threshold `p^*=p`.
- The canonical paper proves positivity of the semigroup in the centered-monomial basis.
- Martinelli--Shapira--Toninelli's Conjecture 1 contains the active target as a special case.

### Claimed

- The exact `h`-transform/finite-set dual reduction in `notes/professor-initial-reduction.md`.

### Conditional

- Any downstream use of the transformed finite-set process is conditional on the claimed duality until Student A checks it.

### Refuted or eliminated

- The previously closed Bernoulli-quench sibling-cancellation route is not part of this programme.
- The previously closed 2D signed-move and nearest-vacancy-capacity routes are not part of this programme.

### Open

- Whether the transformed finite-set process has a useful recurrence, regeneration, front, invariant-measure, or coupling structure that yields one-site density convergence from finite nonempty sets.
- Whether the transformed process or the exact duality is already known under another name.
- If this reduction gives no leverage, whether the unnormalized patch/successful-skeleton representation yields a more informative model-specific late-interaction estimate.

## Current bottleneck

The first bottleneck is not yet the full convergence theorem. It is to validate the exact transformed process and decide whether the target has genuinely been reduced to a more tractable positive finite-set problem.

## Strongest positive evidence

The centered basis is unusually rigid for FA-1f: the patch threshold equals the equilibrium density and the coefficient signs are exact. The proposed `h`-transform uses the absorbing all-one configuration to produce a natural harmonic weight `q^{|A|}`, suggesting a genuine Markov representation rather than another signed majorant. The resulting local update rule, if correct, is explicit enough for direct probabilistic analysis.

## Strongest negative evidence

A change of dual representation can simply move the original difficulty. The transformed process is not obviously attractive, and finite-seed local convergence may be equivalent in hardness to the original conjecture. Earlier local-cancellation attempts in FA-1f failed after composition, so any apparent simplification must be tested on multi-particle configurations immediately.

## Current assignment

Graduate Student A: independently derive or refute the claimed `h`-transform duality, identify the transformed process precisely, analyze its first nontrivial multi-particle transitions, and assess whether it offers a mathematically distinct route to the single-vacancy convergence theorem. Exact assignment: `students/student-a/assignment-001.md`.

## Research delta

Latest meeting `state_narrowed`: not applicable; no student group meeting yet.

Evidence pointer: `notes/professor-initial-reduction.md`

Consecutive no-narrowing meetings: 0

Stagnation consultation pending or completed: none

## Files

- `proof-spine.md`
- `notes/professor-initial-reduction.md`
- `literature.md`
- `audit-log.md`
- `students/student-a/assignment-001.md`

## Principal-facing brief

### Active target

Single-vacancy convergence to equilibrium for 1D hard FA-1f for every `q in (0,1)`.

### What changed mathematically

Programme initialized. The Professor identified a candidate centered `h`-transform reduction to an explicit finite-set neighbour-refresh process; this is currently a claimed calculation awaiting Student A's check.

### What the Professor directly inspected

`CHATGPT.md`, `project-state.md`, `README.md`, the canonical patch paper supplied by the principal, and the 2025 Martinelli--Shapira--Toninelli open-problems paper at the target/conjecture level.

### Current proof-spine bottleneck

Validate and assess the finite-set dual reduction.

### Strongest reason to continue

The target is explicitly open and the canonical patch/centered-moment machinery gives an unusually concrete possible reduction.

### Strongest reason to doubt the direction

The transformed finite-set process may encode the same hard non-attractive dynamics without adding leverage.

### State narrowed since last group meeting

Not applicable before the first student meeting.

### Direction

`continue`: this is the best current target and the first calculation is cheap and decisive enough to justify immediate work.

### What happens next

Graduate Student A checks the reduction and probes the transformed process. No second student is needed yet.

### Pending audit or stagnation consultation

None.

### Question for the principal

None.