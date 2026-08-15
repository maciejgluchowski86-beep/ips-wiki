# Group meeting 001: centered transform reviewed

Date: 2026-08-15

Professor review of Graduate Student A assignment 001.

state_narrowed: yes

Evidence pointer: `research/active/fa1f-finite-seed/students/student-a/001-centered-h-transform.md`, especially Sections 1--4 (exact E1 verification), Sections 7--12 (front identities, reversibility, failure of attractiveness/additivity, BABP comparison, finite-volume similarity), and Section 13 (exact overlap with the closed sibling algebra).

## Professor judgment

E1 is correct and is promoted to **verified for current research use**. Student A independently derived the generator identity, supplied nonexplosion/exponential-moment control, justified the infinite-volume semigroup passage, and checked the single-vacancy specialization. I have read the derivation itself, not only the handoff.

The more important result is negative for strategy. I do not regard the centered `h`-transform as the main line any longer. On a finite cycle it is an exact invertible similarity transform of the transpose FA-1f generator; the transformed chain has the same basic vacancy-front identities, is neither attractive nor additive, and its reversible Dirichlet form is only comparable to BABP, whose finite-seed convergence is itself unresolved in part of the parameter range. There is no concrete theorem-level simplification here.

The local algebra also intersects the permanently closed Bernoulli-quench sibling route exactly: the same normalized centered parameter and the same two-neighbour factorization appear in the simultaneous-neighbour term. This does not make E1 itself a retry, because the post-transform target is a bounded one-site occupation event. It does mean that any attempt to obtain progress by taking absolute values of the two refreshed sibling weights and seeking a generation-by-generation contraction is forbidden mathematically as well as procedurally: it is the already failed mechanism.

Therefore the programme continues on the same **finite-seed FA-1f target** but pivots its proof strategy. E1 is retained as an exact identity and diagnostic tool, not as the active mechanism.

## New main line

The next line is the unnormalized successful-skeleton / patch representation already recorded as the distinct alternative in the initial spine.

The canonical patch proof conditions on the successful skeleton and divides local weighted expectations by patch consistency probabilities. For the hard model, that normalization may hide the probability cost of maintaining a long successful skeleton. The next calculation will recombine these factors and work with

$$
\widehat C(P)
=
\mathbf E_P\left[F(P)\mathbf 1_{\operatorname{Con}(P)}\right]
=
\mathbf P_P(\operatorname{Con}(P))C(P),
$$

with the analogous end-patch amplitude.

This line is not yet accepted as promising beyond one more decisive calculation. A chain-only heuristic is insufficient: every successful FA-1f record has the two-neighbour target and creates source/target descendant patches, so the first test must include the complete first branching composition and the skeleton intensity factors. If that full calculation merely reproduces the closed sibling algebra or remains critical with no geometric loss, expected value drops sharply.

## Proof-spine decision

- E0 unchanged.
- E1: `claimed -> verified`, then demoted from active mechanism to retained identity.
- E2 is now the exact unnormalized hard-FA patch/skeleton expansion and full first-composition calculation.
- E3 is split into the two model-specific estimates that would have to replace the uses of uniform pure deaths in the canonical convergence theorem: late-interaction control and terminal-dependence relaxation.
- E4 is recombination into centered-moment decay.

Updated pointer: `research/active/fa1f-finite-seed/proof-spine.md`.

## Direction decision

**continue, with a proof-strategy pivot inside the same target.**

The target itself has not lost value. What has been eliminated is the idea that the positive `h`-transform already makes the hard problem materially easier. One more obstruction-level patch calculation is justified because the canonical paper gives exact local formulas and because this route addresses precisely the place where its convergence theorem stops.

## Next assignment

Graduate Student A will derive the unnormalized hard-FA patch expansion from the canonical factorization, compute all local amplitudes and skeleton-intensity factors, and test the first complete branching composition. The assignment is in `students/student-a/assignment-002.md`.

No second graduate student is requested. The current protocol keeps the existing student attached to this scientific direction, and E2 is sufficiently local that parallel work would add coordination cost before the route is known to survive its first composition test.
