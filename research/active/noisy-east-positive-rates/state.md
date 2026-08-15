# Programme state

## Direction

Title: residual positive-rates conjecture / noisy East

Branch: `research/noisy-east-positive-rates`

Professor lineage: persistent ChatGPT Professor

Graduate Student C: active persistent student for this direction

Graduate Students A and B: idle with prior lineages

Workspace: `research/active/noisy-east-positive-rates/`

Latest group meeting: `meetings/001-two-site-wall-review.md`

## Positive target

Prove ergodicity in the remaining noisy-East region for simple one-sided one-dimensional positive-rate IPS, ultimately completing the positive-rates conjecture for simple IPS.

The standing novelty standard applies: block-size calculations are diagnostic unless they produce structural mathematics about the mechanism or close the target problem.

## Assignment-001 result

Graduate Student C constructed the exact canonical two-site killed disagreement excursion and two exact verifiers. The Professor independently rebuilt the load-bearing calculations in `notes/professor-wall-test-verification.md`.

On the genuine strict residual path

$$
r_{11}=0,\qquad
r_{10}=1-\varepsilon^2,\qquad
r_{01}=\frac\varepsilon2,\qquad
r_{00}=\varepsilon,
$$

the full two-site killed kernel has

$$
\rho_2(\varepsilon)\to1,
$$

and the one-attack crossing factor from the worst agreed block satisfies

$$
F_2(\varepsilon)\to1.
$$

At the limiting East rule, an exterior disagreement creates boundary orientation `10` against an agreed `11` block; right-site updates preserve it and the next protected-site update crosses deterministically. Therefore length two has no contraction margin stable near East.

A targeted length-three diagnostic changes the structural interpretation. The full 24-state killed chain on the same path gives, after maximizing over **all eight fully agreed three-site words and both exterior disagreement orientations**,

$$
\lim_{\varepsilon\downarrow0}R_3^{\rm adv}(\varepsilon)=\frac9{10}.
$$

The maximizer is the all-one block. Thus the length-two local cycle does not automatically persist at every fixed block length.

Neither finite-state calculation is a project result. They are tractability diagnostics.

## Current bottleneck

Characterize the exact length-three adversarial one-attack factor over the **entire normalized residual noisy-East region and every asymptotic approach to the East boundary**.

Graduate Student C assignment:

`students/student-c/assignment-002.md`.

The assignment must first recover the exact residual set and East boundary from the 2025/2026 sources, then analyze the full piecewise-algebraic canonical-coupling operator rather than retaining the ordering from the single path above.

## Pre-committed finite-wall stop rule

This rule was fixed in Meeting 001 before assignment 002.

If Student C finds any genuine residual sequence approaching the East boundary with

$$
R_3^{\rm adv}(r_n)\to1,
$$

the finite-wall route is abandoned for this programme. **Do not move to length four.** This is an opportunity-cost decision, not a theorem that all longer walls fail.

If instead there is a uniform gap

$$
R_3^{\rm adv}(r)\le1-\delta
$$

throughout an East-boundary neighborhood of the full residual set, continuation still requires a concrete block-renewal/concatenation theorem that survives a dynamically changing exterior, repeated attacks, and overlap/dependence effects. If the frozen-exterior factor cannot be upgraded to a usable dynamic domination without an uncontrolled stronger quantity, the finite-wall route is also abandoned rather than enlarged.

## Research delta

Latest meeting `state_narrowed`: yes.

Evidence pointer: `students/student-c/001-two-site-wall.md`, both assignment-001 verifier scripts, `notes/professor-wall-test-verification.md`, and `meetings/001-two-site-wall-review.md`.

What narrowed:

- the two-site wall is ruled out as an East-stable mechanism;
- the proposed inference from its local cycle to every fixed finite block is refuted by the independently checked length-three diagnostic;
- the next question is a bounded regime-wide characterization, not another block-size search.

Consecutive no-narrowing meetings: 0.

## Direction

`continue for one bounded structural block`.