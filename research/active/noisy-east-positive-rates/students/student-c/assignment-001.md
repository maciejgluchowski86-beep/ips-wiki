# Graduate Student C assignment 001: two-site agreed-block wall test

Work on branch `research/noisy-east-positive-rates`.

This is a genuinely new scientific direction. You are the persistent Graduate Student C for this line.

Read first:

- `project-state.md`;
- `CHATGPT.md`, especially the standing novelty standard;
- `research/active/noisy-east-positive-rates/state.md`;
- `research/active/noisy-east-positive-rates/proof-spine.md`;
- `research/active/noisy-east-positive-rates/literature.md`;
- Student A's prior opportunity-cost reconnaissance on branch `research/babp-finite-seed`, file `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`;
- Głuchowski--Menz (2025), *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*;
- Głuchowski--Menz (2026), *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*.

Before using any exact theorem convention, rederive it from the papers. The reconnaissance is a guide, not authority.

## Main task

Test the smallest genuinely stronger version of the existing one-site wall mechanism.

Under the canonical coupling, take a block of two adjacent sites on which the two coupled processes currently agree. Treat the influencing exterior state adversarially. Construct the exact finite-state process describing agreement/disagreement evolution relevant to whether a disagreement crosses the two-site block before the block regenerates to full agreement.

Define a killed process/operator in which killing is the first successful disagreement crossing from the influencing side through the block before regeneration. Make the state space, transition rates, and regeneration event explicit.

Compute the exact crossing-versus-regeneration next-generation quantity. Depending on the natural formulation this may be a Perron root, a killed-chain return kernel, or an equivalent finite-state reproduction factor. Prove the equivalence between your finite-state quantity and the probabilistic crossing event used by the coupling argument.

## Questions to settle

1. Reproduce the one-site theorem/obstruction as a calibration from the exact paper convention.
2. Determine whether the two-site factor is `<1` on any open subset of the region not covered by the one-site criterion.
3. Determine its behavior approaching the East boundary with strictly positive noise.
4. Decide whether a uniform subcritical bound can hold throughout the residual noisy-East region.
5. If the two-site mechanism fails, identify the exact local cycle or bottleneck responsible.
6. Test whether that obstruction obviously persists for every fixed block length. Do not claim this without proof.

## Novelty rule

A better numerical region at block length two is **not by itself a project result**. This assignment is a falsification/tractability probe.

If the calculation is favorable, formulate the structural theorem that would turn finite-block subcriticality into ergodicity across the residual region. If it is unfavorable, formulate the strongest structural obstruction actually supported by the calculation.

Do not respond to failure at length two by automatically moving to length three. A larger-block follow-up requires a mathematical reason to expect a qualitatively different mechanism.

## Exactness and computation

Use symbolic/rational computation when useful, but expose the exact finite-state generator/operator and the inequalities carrying the conclusion. A numerical eigenvalue alone is insufficient.

Stress-test any claimed uniform inequality on parameter paths approaching the East boundary and on the one-site criterion boundary.

## Durable output

Commit the complete report to:

`research/active/noisy-east-positive-rates/students/student-c/001-two-site-wall.md`

Include any verifier/source code under the same student directory.

End the report with one recommendation:

- `develop block-renewal theorem`;
- `finite-wall route structurally obstructed`; or
- `unresolved — precise next falsification test: ...`.

Do not edit `main`.