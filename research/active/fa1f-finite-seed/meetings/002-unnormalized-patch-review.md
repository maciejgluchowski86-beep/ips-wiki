# Group meeting 002: unnormalized patch transfer reviewed

Date: 2026-08-15

Professor review of Graduate Student A assignment 002 and its clarification note.

state_narrowed: yes

Evidence pointer: `research/active/fa1f-finite-seed/students/student-a/002-unnormalized-patches.md`, especially Sections 9--14, together with `research/active/fa1f-finite-seed/students/student-a/002-transfer-normalization-clarification.md` and the Professor's independent verification `research/active/fa1f-finite-seed/notes/professor-transfer-verification.md`.

## Professor verification of the load-bearing identity

The strategic conclusion turns on the claim that the complete unnormalized patch coefficient transfer is exactly the E1 Markov semigroup after the `h`-weighting. I checked this independently.

On a finite cycle, centered monomials form a basis. Define the unique coefficient matrix by

$$
P_t\chi_A^*=\sum_BK_t(A,B)\chi_B^*.
$$

The canonical patch representation computes the exact same `P_t`; for centered input one first expands it linearly into ordinary monomials, applies the exact patch formula, and then collects the centered output basis. Hence the resulting full patch coefficient matrix is exactly `K_t`.

The already verified E1 duality gives

$$
P_t\chi_A^*
=q^{|A|}\sum_BQ_t(A,B)q^{-|B|}\chi_B^*,
$$

where `Q_t=e^{t\mathcal G}` is a Markov semigroup. Uniqueness of the centered-basis expansion therefore gives

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B).
$$

Consequently

$$
\sum_Bq^{|B|-|A|}K_t(A,B)=1.
$$

There is also an independent row-sum check: evaluate the centered expansion at the all-occupied absorbing configuration, where `chi_B^*(1)=q^{|B|}`. The weighted coefficient mass must be conserved.

Student A's clarification about zero-length boundary patches is correct and important: the Section 9 kernels are `h`-normalized coefficient kernels rather than bare open-patch products. With that convention fixed, the first-composition criticality and the global identification are consistent.

I therefore accept the identification as correct for the present strategic decision.

## Mathematical result of assignment 002

The normalization-hidden-cost intuition was partially real. Restoring consistency probabilities gives explicit `e^{-Delta}` factors and strictly suppresses a fixed same-source routing sector.

But the complete first branching composition removes the apparent margin. The two child-source sectors carry exactly the missing same-source mass. This is not a numerical coincidence: globally the complete transfer is the conservative E1 Markov dynamics in another decomposition.

Thus the precommitted kill condition from Meeting 001 has occurred in its second form: the full calculation remains critical with no target-level geometric loss.

This failure is not the old Bernoulli-quench sibling-cancellation failure. No absolute-value sibling contraction is used. The stronger obstruction is conservation of the complete positive `h`-weighted coefficient transfer.

## Direction decision

**close** the 1D hard FA-1f finite-seed programme.

The open problem itself remains important. Closure is an expected-value judgment about this group's present leverage. Two genuinely distinct attempts based on the principal's patch/centered-moment machinery have now converged to the same conservative dynamics:

1. the exact centered `h`-transform;
2. the exact unnormalized successful-skeleton transfer.

A proof from here would require a new one-dimensional spatial theorem -- for example regeneration or local equilibration behind the vacancy fronts -- that is not presently encoded in either representation. We have no concrete such mechanism. Inventing a third coordinate system or another local patch decomposition would be momentum, not a narrowed proof strategy.

## Next scientific direction

The next target will be **one-dimensional BABP convergence from a finite nonempty particle set for all positive branching parameters**, i.e. removal of the remaining small-parameter gap below the classical `0.0347` threshold.

This is a genuinely new direction rather than a continuation of FA-1f. It is attractive for three reasons:

- it is explicitly identified in the canonical patch paper as an unresolved finite-seed hard-model problem;
- classical BABP has exact self-duality and quasi-duality, and the 2025 Martinelli--Shapira--Toninelli work adds all-parameter linear growth from finite seeds and exponential ergodicity for the double-flipping process;
- the remaining gap is therefore more sharply localized than for FA-1f: the task is to turn existing growth/duality structure into local convergence for small branching parameter, not first to discover the geometry of a non-attractive KCM.

A new persistent Graduate Student B is warranted because this is a new scientific direction. Graduate Student A should remain alive and idle with the FA-1f context rather than be repurposed.

The new BABP workspace will be initialized on `research/babp-finite-seed`.
