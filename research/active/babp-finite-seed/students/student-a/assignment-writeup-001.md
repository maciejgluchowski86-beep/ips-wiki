# Graduate Student A assignment: BABP theorem writeup and closest-prior-work audit

Work on branch `research/babp-finite-seed`.

This is a bounded writeup/literature assignment inside the existing BABP programme, not a new scientific direction.

Read first:

- `project-state.md`;
- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/babp-finite-seed/meetings/005-convergence-promotion.md`;
- `research/results/babp-finite-seed-convergence.md`;
- `research/claim-registry.md`, entries `BABP-EDGE-001` and `BABP-CONV-001`;
- independent audits `001-edge-corrector-audit.md`, `002-convergence-review-a.md`, and `002-convergence-review-b.md`;
- `STYLE.md` if you draft LaTeX.

The mathematics of `BABP-CONV-001` is now verified. Publication-level novelty/priority is not yet verified.

## 1. Closest-prior-work audit

Perform a source-specific search through 2026-08-15 for anything that may already imply or contain either of these results:

1. the general criterion “uniformly positive statewise finite-window edge corrector implies finite-seed local convergence”;
2. finite-seed BABP convergence at `lambda=1/40`, or at any parameter below the classical `0.0347` range.

Search under alternate terminology, including biased annihilating branching process, annihilating branching process, branching-annihilating process, jumping voter model, edge submartingale, interface/front process, finite particle system, and relevant dual formulations.

At minimum inspect and distinguish what is actually proved in:

- Neuhauser--Sudbury (1993), *The biased annihilating branching process*;
- Mountford (1993), *A coupling of finite particle systems*;
- Sudbury (1997) and related qualitative BABP convergence work;
- Lloyd--Sudbury (1997) on duality/quasi-duality;
- Sudbury (1998), finite-boundary computational/submartingale method;
- Sudbury (1999), *Hunting submartingales...*;
- Martinelli--Shapira--Toninelli (2025), especially Section 5 and Remark 5.4;
- papers citing Sudbury (1999) or the 2025 progress paper through 2026-08-15.

Try harder than the earlier targeted successor search. Search citation chains, author pages/repositories, alternate titles/terminology, and recent preprints. If the full Sudbury (1999) text becomes legitimately accessible, inspect its exact convergence bridge and finite-window construction and record page/theorem references.

For every potentially overlapping result, state exactly whether it contains:

- a statewise corrector hypothesis;
- only an outer-edge speed statement;
- a local no-escape/gap argument;
- the same numerical parameter range;
- a theorem applicable after a simple rescaling;
- or merely a related mechanism.

Do not infer novelty from absence in one survey. If the priority claim remains uncertain, say so.

## 2. Prepare the focused research-note structure

Recommend a compact paper structure for the verified result. The natural core is:

- model and prior finite-seed range;
- theorem: statewise edge corrector implies finite-seed convergence;
- exact `lambda=1/40`, `k=10` certificate/corollary;
- finite-window edge generator and certificate verification format;
- internal-gap genealogy and corrected-gap contraction;
- localized exponential lifetime/width estimate;
- Poisson displacement and finite-truncation compensator sum;
- nonescape and stationary-limit argument;
- external theorem convention/rescaling;
- discussion of the all-parameter front problem.

Keep the main theorem statement at its verified scope: finite nonempty deterministic initial sets, no convergence rate, no claim that bare ballistic speed suffices.

The generator convention must be explicit:

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

When citing Martinelli--Shapira--Toninelli, state explicitly

$$
\lambda=q/p,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

The writeup must contain the two repairs required by Review A:

- localization before using `exp(theta Z)` in Dynkin/optional stopping;
- finite spatial truncation in the nucleation compensator before monotone convergence.

## 3. Decide packaging and novelty language

Recommend whether this should presently be:

- a short standalone note centered on the `lambda=1/40` improvement and general corrector criterion;
- a broader BABP paper that waits for the all-parameter front-gap problem;
- or a staged approach, with a complete short note now and later strengthening if E5 succeeds.

Give exact safe novelty language. Distinguish:

- mathematically verified project theorem;
- current evidence that it improves the range recorded in 2025;
- publication-level priority claim, which requires your closest-prior-work audit.

Do not write “first” or “best known” unless the search supports it strongly enough.

## 4. Drafting

If useful, create a manuscript skeleton under

`research/active/babp-finite-seed/drafts/`

using the repository's paper style only where natural. Do not modify the canonical patch manuscript and do not edit the live wiki.

At minimum commit a durable report to

`research/active/babp-finite-seed/students/student-a/writeup-001-literature-and-manuscript-plan.md`.

End with:

- closest prior theorem found;
- novelty status: verified / strongly supported / unresolved;
- recommended paper scope;
- any exact literature issue requiring a fresh specialist audit before submission-level confidence.