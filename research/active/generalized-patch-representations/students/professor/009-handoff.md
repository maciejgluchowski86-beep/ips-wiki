# 009 handoff

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

Selected model: Krone two-stage contact process, chosen and committed before any patch-positivity calculation.

Decisive facts:

- exact nonempty outgoing row for each adult-neighbour target:
  \[
  (\lambda,-\lambda,-\lambda);
  \]
- exact interior transfer:
  \[
  K=\begin{pmatrix}
  0&0&0\\
  0&-(1+\delta+\gamma)&0\\
  0&\gamma&-1
  \end{pmatrix};
  \]
- the consecutive-source `OO` descriptor is genuinely realizable;
- its numerator is strictly negative for every finite patch length whenever `lambda>0`;
- denominator is strictly positive;
- exact gate at `lambda=gamma=delta=1`, `exp(-t)=1/2` gives numerator `-5/16`, denominator `5/16`, contribution `-1`.

A materially different spatial SIRS model has the same obstruction.

Reusable lemma: if a positive nonempty target mode appears in `0->r` but not in any active-source transition into `r`, then `a_r^r(tau)<0`; if the source-`r` successful record can repeat, a realized short `OO` patch is negative.

Known two-stage duality/complete-convergence theory is already strong (Krone, Foxall, Sturm--Swart), so no model-level novelty is claimed from graphical duality. The killed typed representation is genuinely operative because the hidden mark is three-valued and typed cemetery conflicts are realizable, but bulk positivity fails before any new comparison/convergence theorem can follow.

Decisive files:

- `009a-literature-driven-model-selection.md`, `56ba8390`;
- `009b-two-stage-typed-specialization.md`, `232fe276`;
- `009c-two-stage-patch-positivity-obstruction.md`, `0174a59b`;
- verifier `009-two-stage-application-verifier.py`, `d2576053`;
- `009d-second-candidate-sirs-check.md`, `db0746f7`;
- `009e-two-stage-prior-work-and-application-value.md`, `423bee8e`;
- final report `009-natural-nonbinary-application.md`, `3d092827`.

Recommended next edge if the programme continues: one bounded literature-driven application search in a **structurally non-catalytic** three-state replacement family, where neighbour interactions can retype active states or otherwise avoid the proved catalytic-birth no-go. Do not tune the two-stage or SIRS models and do not return to generic `d>3` algebra by default.
