# Programme state

Status: **closed at Group Meeting 002**.

## Direction

Title: 1D hard FA-1f from a finite seed

Branch: `research/fa1f-finite-seed`

Professor lineage: persistent ChatGPT Professor

Graduate-student lineage: Graduate Student A

Workspace: `research/active/fa1f-finite-seed/`

Latest group meeting: `meetings/002-unnormalized-patch-review.md`

## Target

For every `q in (0,1)`, prove local convergence of one-dimensional hard FA-1f started from the single-vacancy configuration to Bernoulli equilibrium.

The target remains open and worthwhile. The programme is closed because the concrete mechanisms developed here no longer provide a live proof edge.

## What was established

### Verified centered transform

Graduate Student A verified the exact positive finite-set dual, including nonexplosion and the infinite-volume semigroup passage. For finite nonempty `A`,

$$
P_t\chi_A^*(\eta^0)
=q^{|A|}\left(1-q^{-1}\mathbf P_A(0\in\mathcal A_t)\right).
$$

The transformed process is a useful exact identity but not a demonstrated simplification: on finite cycles it is an invertible similarity transform of FA-1f, it is not attractive or additive, and its basic front identities reproduce the physical vacancy-front identities.

Pointer: `students/student-a/001-centered-h-transform.md`.

### Verified unnormalized patch transfer

Student A derived the exact successful-skeleton expansion before normalization, all hard-FA local unnormalized amplitudes, and the first complete branching composition. Restoring consistency probabilities creates real decay in a restricted same-source routing sector, but the missing mass is exactly rerouted to child-source sectors.

At the global coefficient level, if

$$
P_t\chi_A^*=\sum_BK_t(A,B)\chi_B^*,
$$

and `Q_t` is the verified transformed Markov semigroup, then

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B).
$$

Thus the complete `h`-weighted patch transfer is stochastic and has total mass one.

Pointers:

- `students/student-a/002-unnormalized-patches.md`;
- `students/student-a/002-transfer-normalization-clarification.md`;
- `notes/professor-transfer-verification.md`.

## Why the programme is closed

The two concrete routes supplied by the principal's current patch/centered-moment machinery have converged to the same conservative positive coefficient dynamics.

1. The centered `h`-transform is exact but currently a coordinate reformulation.
2. Restoring consistency probabilities gives no full-transfer contraction; after complete branching it is exactly the same E1 semigroup in different coordinates.

The remaining conceivable route would require genuinely new one-dimensional spatial structure, such as a regeneration theorem behind the fronts. No such mechanism has emerged from the current work. Continuing now would mean searching for an unspecified third idea rather than following a narrowed proof edge.

This is an expected-value closure, not an impossibility theorem.

## Relation to closed prior FA routes

The programme did not retry the closed Bernoulli-quench sibling-cancellation route. Student A did identify exact local algebraic overlap with that route, and the boundary remains explicit: no future generation-by-generation absolute sibling contraction based on the same two-neighbour weights should be revived.

The failed unnormalized route is a different obstruction: conservation of the complete `h`-weighted coefficient transfer.

## Final proof spine

Path: `proof-spine.md`.

No active unresolved edge remains in this programme.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `students/student-a/002-unnormalized-patches.md`, Sections 9--14, plus `notes/professor-transfer-verification.md`.

Consecutive no-narrowing meetings: 0

Stagnation consultation: not applicable.

## Direction decision

`close`.

The next scientific direction is BABP convergence from a finite nonempty seed for the remaining small-parameter range. It is initialized separately on branch `research/babp-finite-seed` after this closure record.
