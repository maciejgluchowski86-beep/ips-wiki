# Graduate Student C assignment 002: uniform three-site wall characterization

Work on branch `research/noisy-east-positive-rates`.

Read first:

- `project-state.md`;
- `CHATGPT.md`, especially the standing novelty standard;
- `research/active/noisy-east-positive-rates/state.md`;
- `research/active/noisy-east-positive-rates/proof-spine.md`;
- `research/active/noisy-east-positive-rates/meetings/001-two-site-wall-review.md`;
- `research/active/noisy-east-positive-rates/notes/professor-wall-test-verification.md`;
- your assignment-001 report and both verifier scripts;
- the exact residual-region reductions in Głuchowski--Menz (2025, 2026).

Do not move to block length four in this assignment.

## Goal

Decide whether the **length-three** agreed-block crossing/regeneration mechanism has a uniform contraction gap over the entire residual noisy-East approach to the East boundary.

The previous `9/10` limit on one path is diagnostic only. The question now is the complete asymptotic regime, not another block-size instance.

## Step 1: define the exact residual set from source

State the normalized residual parameter set `R` that remains after the time-scaling/state-symmetry reductions actually proved in the 2025/2026 papers. Define its East boundary `partial_E R` precisely.

Do not silently replace the true residual by the particular path from assignment 001.

If the residual on the normalized face `r11=0` is most naturally written with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

identify all inequalities that are genuinely part of the unresolved set and all inequalities that are merely a convenient ordering chamber for the canonical coupling.

## Step 2: define the adversarial length-three factor globally

For every `r in R`, construct the exact length-three killed embedded chain under the canonical coupling, with:

- all eight fully agreed three-site initial words;
- both exterior disagreement orientations `01` and `10`;
- the designated right-boundary attack;
- crossing when disagreement reaches the protected left site before regeneration;
- regeneration when the full three-site block is again agreed.

Define

$$
R_3^{\rm adv}(r)
$$

as the maximum unconditional one-attack crossing factor over those sixteen initial/exterior choices.

The canonical coupling is piecewise algebraic because the ordering of the four `r_xy` changes. Partition the relevant residual region into the necessary ordering chambers rather than assuming the ordering from the path used in assignment 001.

## Step 3: characterize every East-boundary asymptotic

Determine

$$
\sup_{\bar r\in\partial_E R}
\limsup_{\substack{r\to\bar r\\r\in R}}
R_3^{\rm adv}(r).
$$

The desired output is an exact theorem or exact counterexample, not sampling.

Where useful, introduce scale-free ratios for the small parameters approaching East and compactify the asymptotic problem. For example, if source-verified residual inequalities imply a normalization in which `1-r10`, `r00`, and `r01` all vanish, determine whether the limit depends only on ratios such as

$$
\frac{r_{01}}{r_{00}},
\qquad
\frac{1-r_{10}}{r_{00}},
$$

including their boundary cases. This is only a suggested coordinate system; derive the correct one from the actual residual geometry.

Prove one of the following:

1. **uniform gap:** there is an explicit `delta>0` and an East-boundary neighborhood in the full residual set such that
   $$
   R_3^{\rm adv}(r)\le1-\delta;
   $$
2. **loss of uniformity:** exhibit a genuine residual sequence approaching the East boundary for which
   $$
   R_3^{\rm adv}(r_n)\to1.
   $$

A numerical supremum is insufficient. Use exact rational/algebraic elimination, monotonicity, compactness plus exact boundary analysis, or another rigorous method.

## Pre-committed route decision

Meeting 001 fixed the following rule.

If you obtain **loss of uniformity**, the finite-wall route is closed for this programme. Do not compute length four. Record the asymptotic path and the structural reason the length-three margin fails.

If you obtain a **uniform gap**, do not call that a project result by itself. The next scientific object is the missing infinite-volume theorem:

> a block-renewal/concatenation theorem showing that a uniform adversarial local crossing factor below one implies extinction of disagreements, hence ergodicity, in the residual simple IPS.

In the uniform-gap case, end this assignment by formulating that theorem precisely and listing every additional hypothesis needed to pass from the frozen-exterior one-attack operator to the actual dynamically evolving coupled IPS. In particular identify whether repeated attacks, exterior changes during an excursion, overlapping blocks, or dependence between successive regenerations require a stronger local quantity than `R_3^{adv}`.

If the factor is uniformly below one but cannot plausibly dominate the actual dynamic exterior without an uncontrolled stronger quantity, say so explicitly. The Professor has pre-committed not to respond by increasing block length.

## Novelty standard

A better numerical region for a three-site block is not a project result. A qualifying outcome would be structural, for example:

- a regime-wide theorem that the finite-wall mechanism has a uniform East-boundary contraction gap together with a valid renewal theorem yielding ergodicity;
- a regime-wide theorem that the mechanism necessarily loses uniformity and therefore cannot close the residual by this architecture; or
- another genuinely qualitative mechanism exposed by the exact characterization.

Do not claim novelty for the 24-state computation itself.

## Durable output

Commit the report to:

`research/active/noisy-east-positive-rates/students/student-c/002-uniform-three-site-wall.md`

Put exact verifier/algebra scripts under the same student directory.

End with exactly one recommendation:

- `uniform three-site gap; formulate block-renewal theorem`;
- `finite-wall route loses uniformity; close it`;
- `unresolved — exact remaining obstruction: ...`.