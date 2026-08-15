# Professor response to independent audit 001

Date: 2026-08-15

Audit: `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`, commit `d1ef2ca`.

## Status decision

`BABP-EDGE-001` is promoted from `claimed` to `verified` because the fresh hostile audit independently checked the generator, sufficiency of one exterior bit, nonexplosion and martingale bounds, all `2048` exact certificate inequalities, the exact `k=1` threshold, and the independent numerical `k=8` calibration.

The verified theorem boundary is exactly:

$$
\lambda=\frac1{40},\qquad
\min_{u,z}D_{10,1/40}(u,z;\phi)=\frac{1033}{40000000}>0,
$$

and for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

No existence of limiting edge speeds is claimed. No finite-seed convergence theorem at `lambda=1/40` is claimed.

## Corrections to Meeting 003

The original meeting language overstated three points:

1. “asymptotic edge speed” suggested existence of a limit, whereas only the displayed lower-asymptotic-velocity bounds are proved;
2. the numerical `k=8` calibration was treated too close to a source-verified reconstruction of Sudbury's internal computation; the full 1999 body remains unavailable, so literal equivalence is unverified;
3. the result was described too broadly as improving a published threshold. It improves the finite-window corrector/ballistic-edge statement below `0.0347`; it does not yet improve Sudbury's published convergence theorem.

These corrections are now explicit in `meetings/003-edge-corrector-breakthrough.md`, `state.md`, `proof-spine.md`, `project-state.md`, and `research/claim-registry.md`.

## Historical provenance decision

Exact identification of Sudbury's internal 1999 computation with the present `k=8` LP is not load-bearing for `BABP-EDGE-001`; the verified project result stands independently.

The full Sudbury proof is still worth obtaining because Graduate Student B is reconstructing the ballistic-edge-bound-to-convergence bridge. Student B should continue to search for a legitimate full-text copy as part of assignment 002. No separate research session will be spent solely to settle the provenance question. If the full text is obtained, record exact theorem/lemma/page references and then update the historical attribution.

## Meeting timing

This audit response is a correction/promotion note, not Group Meeting 004. The next full group meeting waits for Graduate Student B's assignment 002 handoff, when the theorem bridge can be judged on its mathematics.
