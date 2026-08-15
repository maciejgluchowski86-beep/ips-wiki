# Group meeting 005: promotion of finite-seed convergence mathematics

Date: 2026-08-15

Professor review of independent correctness reviews `abb05f6` and `1aeb5a5`.

state_narrowed: yes

Evidence pointer: `audits/002-convergence-review-a.md`, `audits/002-convergence-review-b.md`, repaired Professor proof `notes/professor-corrector-to-convergence-verification.md`, and verified prerequisite `BABP-EDGE-001`.

## Mathematical promotion decision

`BABP-CONV-001` was promoted from `claimed` to `verified` for mathematical correctness.

The verified implication is:

> If one-dimensional BABP admits a bounded finite-window right-edge corrector with uniform statewise drift `D_{k,lambda}(u,z;phi)>=v>0` for every edge state, then BABP from every finite nonempty deterministic particle set converges locally to Bernoulli equilibrium.

Both hostile reviews independently reconstructed the tagged-gap proof. Review A required two rigor repairs, both incorporated into the stable proof: localization for the unbounded exponential test and finite spatial truncation before the infinite compensator sum. Review B independently checked the generator normalization and the Jahnel--Köppl stationary-limit interface.

Combining the implication with verified `BABP-EDGE-001` gives finite-seed convergence at

$$
\lambda=\frac1{40}=0.025.
$$

That mathematical conclusion remains verified.

## Full-text novelty correction after Meeting 006

The original Meeting 005 record treated the corrector-to-convergence implication as the programme's new theorem-level contribution, with publication-level priority merely pending. The full Sudbury (1999) text shows that this was too strong.

Sudbury Section 3 already constructs the same robust finite-window edge submartingale. His Maxwell's-demon end-value is the project exterior bit, Lemma 5 is the all-state/all-end-value robustness requirement, Table 2 reports the eight-site `0.0347` computation, and Lemma 7 extends any successful window to all larger windows.

More importantly, immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used existence of a suitable submartingale in their stationary-state argument, that his Section 3 extends that condition to `lambda>0.0347`, and that their Section 5 argument then proceeds unchanged. Thus the general implication promoted here is prior art, even though the project's self-contained tagged-gap proof is mathematically correct.

The corrected novelty statement is:

> The verified project advance is the exact rational ten-site certificate at `lambda=1/40`, which extends the published finite-window/convergence range below `0.0347` inside Sudbury's established mechanism. The project also gives a self-contained modern proof of the classical implication. No novelty claim is made for the tagged-gap proof architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

The status `verified` remains appropriate because registry status records mathematical correctness, not priority.

## Stable-main correction

Meeting 005 originally promoted the claim registry, theorem note, and project state to `main`. Meeting 006 requires those same stable files to be corrected rather than withdrawn. The corrected main surface now states the prior art explicitly and reframes the `lambda=1/40` result as an exact range extension.

## E5 and direction

The all-parameter problem remains genuinely open. Student B's subsequent commits `5c357ef` and `1365840` sharpen the finite-window route to a phase-selection question for the infinite front: every singleton-selected invariant front law has positive current, so only an additional hostile invariant semi-infinite-tail phase can obstruct the method.

Meeting 006 therefore retains direction `continue` for one further substantial block, with an explicit opportunity-cost checkpoint if hostile-phase exclusion does not narrow.

## Wiki-freeze recommendation

Keep the live wiki frozen. The prior-art correction should be stabilized in the research note before any `proved here` BABP wiki update.

Meeting 006 supersedes this meeting's original novelty language while preserving its mathematical verification decision.