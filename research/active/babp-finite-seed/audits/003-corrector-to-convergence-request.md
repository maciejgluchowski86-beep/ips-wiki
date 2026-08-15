# Independent audit request 003: BABP convergence theorem and external-input audit

You are the second fresh independent auditor of a candidate new BABP theorem. Work independently of audit 002. Do not read audit 002 before completing your own mathematical judgment.

Branch: `research/babp-finite-seed`.

Read first:

- `research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`;
- `research/claim-registry.md`, entry `BABP-CONV-001`;
- the verified edge hypothesis in `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`;
- the primary sources needed for the stationary-limit and stationary-classification inputs.

After forming your own view, read `research/active/babp-finite-seed/notes/professor-corrector-to-convergence-verification.md` and report whether it changes anything.

The candidate theorem is:

> For fixed `lambda>0`, existence of a bounded finite-window edge corrector with uniform statewise positive drift implies local convergence of one-dimensional BABP from every finite nonempty deterministic initial set to Bernoulli equilibrium. In particular the verified `k=10`, `lambda=1/40` corrector would imply finite-seed convergence at `lambda=1/40`.

This audit has two equal priorities: an independent proof-level attack and an exact audit of the external theorem interface.

## A. Independent proof attack

Try to break the proposed gap argument. In particular:

- derive the generator of the corrected width of an internal gap directly from BABP, including width one and side populations of size one;
- test the claim that positive gaps never merge and never split;
- test the exponential killed-supermartingale construction;
- test the Poisson displacement domination;
- test the infinite-space compensator sum over gap nucleations;
- test whether the final empty-window bound is uniform in late time rather than a per-genealogy statement;
- test whether any event type creates a long empty interval not represented by a tagged gap genealogy.

If there is a shorter independent proof of the bridge, give it. If there is a counterexample to any stated intermediate assertion, determine whether it actually kills the theorem or can be repaired.

## B. External theorem interface

Independently verify from primary sources that the following inputs apply to BABP at arbitrary fixed `lambda>0` in the convention of the project:

1. every weak limit point of the one-dimensional BABP measure-valued trajectory is stationary;
2. every stationary law of one-dimensional BABP is a convex combination of the empty configuration and Bernoulli equilibrium.

The Professor currently proposes Jahnel--Köppl (2026), Theorem 2.5, for item 1 and Martinelli--Shapira--Toninelli (2025), Corollary 2.9, for item 2. Check the actual hypotheses, not just abstracts or theorem labels. Translate the BABP generator into the cited framework and verify each required boundedness/range/influence assumption. Flag any mismatch of variables, state conventions, translation invariance, irreducibility, or positivity assumptions.

Also independently verify that the 2025 progress paper records finite-seed convergence only down to `lambda>0.0347` (or its exact endpoint convention), so that `lambda=1/40` would indeed lie outside the published range identified there. Do not make a global novelty claim from one survey alone; report the scope of what you have checked.

## C. Exact theorem boundary

Determine whether the candidate theorem really requires the full statewise corrector condition or can be weakened. For audit purposes, do not strengthen the registered claim unless you prove the strengthening.

Confirm the initial-condition scope. The registered claim is only for finite nonempty deterministic sets and asserts no quantitative convergence rate.

## Output

Commit to

`research/active/babp-finite-seed/audits/003-corrector-to-convergence-audit.md`.

End with one of:

- `VERIFIED`;
- `VERIFIED WITH CORRECTIONS`;
- `NOT VERIFIED`.

Give exact primary-source citations for every external input you accept. Do not rely on audit 002 or the Professor's verdict as authority.