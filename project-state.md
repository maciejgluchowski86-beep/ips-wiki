# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Research architecture

The group has one persistent ChatGPT Professor directing persistent graduate-student sessions. At most two sessions are in flight at once. The Professor owns scientific direction, proof spines, audits, opportunity-cost judgments, and closure decisions. Students do specified autonomous technical work and persist with their scientific direction.

The repository is canonical technical memory. Conversation links are optional only; successor sessions must rely on repository handovers and exact transcript transfer when necessary.

## Active scientific direction

**1D BABP from a finite seed — committed programme.**

- Research branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Positive target: for every `lambda>0`, prove local convergence of one-dimensional biased annihilating branching process started from a finite nonempty particle set to Bernoulli equilibrium of particle density `lambda/(1+lambda)`.
- Historical known range: the published finite-seed convergence theorem reaches the `0.0347` parameter threshold.
- Verified project datum: at `lambda=1/40=0.025`, a ten-site right-edge corrector has exact uniformly positive generator drift `1033/40000000`; claim `BABP-EDGE-001` is `verified` by independent audit `d1ef2ca`.
- Exact consequence: for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

- This does not by itself establish existence of limiting edge speeds or finite-seed convergence at `lambda=1/40`.
- Current proof-spine bottleneck: prove or refute that these ballistic edge bounds, together with the known invariant-law/global-growth inputs, yield finite-seed local convergence; first test `lambda=1/40`.
- Downstream analytic problem: construct positive finite-window edge correctors for every `lambda>0`, equivalently show the finite-window threshold tends to zero if the bridge is sufficient.
- Professor: persistent ChatGPT Professor.
- Active development student: Graduate Student B.
- Independent auditor: completed audit 001.
- Graduate Student A: idle after bounded opportunity-cost reconnaissance.
- Latest group meeting: `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`.

The programme graduated from provisional to committed at Meeting 003. Student B found the finite-window right-edge corrector hierarchy, analytically reproduced the old `1/3` numerical boundary at window size one, numerically reproduced `0.0346195435...` at window size eight, and supplied an exact rational positive-drift certificate at window size ten and `lambda=1/40`. The Professor independently checked the mathematics, and a fresh hostile audit independently rederived the generator and verified the certificate.

Meeting 003 originally overstated three points. Audit 001 corrected them explicitly: the corrector proves liminf/limsup ballistic bounds rather than existence of speed limits; literal identity of the present `k=8` LP with Sudbury's internal 1999 computation is unverified; and the current result is not yet an improvement of Sudbury's published convergence theorem. The meeting note and claim registry now record these narrower statements.

Graduate Student A's reconnaissance had favored the residual simple-IPS positive-rates/noisy-East problem over **provisional** BABP unless BABP produced a genuinely new small-parameter handle. The audited edge certificate satisfies that condition. Noisy East remains the strongest identified reserve candidate if the BABP bridge fails or the finite-window threshold problem proves sterile.

The programme is not committed to cancellation, duality, or patches as its main method. The active mechanism is a finite-state Markov-additive edge corrector. DFP quasi-duality has been demoted as a black-box route because the finite-test cylinder has no probability-law DFP representation and its finite-window signed representation has exponentially growing coefficient norm.

## Historical provenance status

The accessible Sudbury (1999) record confirms the `0.0347` finite-seed convergence threshold, hunted-submartingale method, and edge-speed bounds. Its full body was not accessible to Student B or the independent auditor. Therefore the exact claim that Sudbury used literally the same `k=8` LP, normalization, or eight-site encoding remains unverified.

That provenance question is not load-bearing for `BABP-EDGE-001`, which now stands on an independent proof and hostile audit. Obtaining the full paper remains useful because Student B is reconstructing the edge-bound-to-convergence bridge. No separate session will be spent solely on historical identity.

## Most recently closed programme

**1D hard FA-1f from a finite seed** was closed at Group Meeting 002 on expected-value grounds. The open problem itself remains worthwhile.

Two distinct project mechanisms were settled:

1. the exact centered `h`-transform to a positive finite-set process is correct but is an invertible finite-volume similarity with no demonstrated simplification;
2. the exact unnormalized successful-skeleton transfer restores real consistency-probability losses on restricted routing sectors, but after complete branching its centered coefficient matrix satisfies

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B),
$$

where `Q_t` is the same E1 Markov semigroup. Thus the full `h`-weighted transfer is conservative.

After the first version of Meeting 002, the principal supplied additional tractability evidence: extensive prior ChatGPT work on one-dimensional FA-1f off-equilibrium convergence had already failed to produce a result. This is not an impossibility theorem, but together with the two present-project negatives it materially lowers expected value for reopening that target. The principal also clarified that cancellation/duality is not a preferred or required organizing mechanism and recommended recent serious progress/survey papers with explicit open problems as target-selection sources.

Decisive records:

- `research/active/fa1f-finite-seed/meetings/002-unnormalized-patch-review.md`;
- `research/active/fa1f-finite-seed/notes/professor-transfer-verification.md`;
- `research/active/fa1f-finite-seed/students/student-a/002-unnormalized-patches.md`.

## Canonical prior work: patch construction

The principal's manuscript `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for the patch construction and its proofs and supersedes the deprecated IPS wiki layer on those points.

It proves conditional patch factorization over the successful-interaction skeleton and the exact patch representation. The construction is a preferred reusable asset when it naturally addresses the obstruction, not a mandatory research template.

## Closed programmes and routes

Closed programmes not to be retried by renaming:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on the centered transform / unnormalized patch-transfer routes.

Closed screened routes:

- 1D FA-1f Bernoulli-quench sibling cancellation;
- strongly non-harmonic Wigner--Fokker--Planck via unweighted Moyal/skew cancellation;
- 2D FA-1f relaxation logarithm via local signed-move cancellation;
- 2D FA-1f nearest-vacancy annular/electrical-capacity observable;
- general bootstrap-percolation sharpness from bare inclusion--exclusion/Bonferroni overlap subtraction.

Broader mathematical problems may remain open. What is closed is the recorded programme or mechanism.

## Reusable negative and positive lessons

- Wrong-norm or wrong-weight cancellation is usually fatal when the critical conversion exactly restores the lost scale.
- A strict local gain must be tested under the first nontrivial composition and in the controlling quantity.
- For FA-1f, both the centered positive transform and the full unnormalized patch coefficient transfer reduce to the same conservative dynamics; restricted routing losses are redistributed globally.
- Substantial prior model-assisted effort without a route is real tractability evidence and should enter opportunity-cost judgments.
- Recent serious progress/survey papers and explicit open-problem lists are useful target sources; the group should not force cancellation, duality, or patches into candidates.
- The BABP edge calculation is a positive example of obstruction-first work: reconstructing the historical proof barrier exposed a finite-state optimization problem that could be improved before any attempt at the full theorem.
- A computational certificate becomes strategically meaningful only when its generator encoding and theorem consequence are checked independently. `BABP-EDGE-001` has now completed that audit, but its theorem boundary remains narrow.

## Group-meeting homeostasis

Every substantial student handoff is followed by a Professor group meeting before another substantial variant is assigned. Each meeting records exactly `state_narrowed: yes` or `state_narrowed: no` with a concrete evidence pointer. Three consecutive `no` meetings trigger an outside stagnation consultant; the Professor retains authority.

Meeting 003 records `state_narrowed: yes` because the group localized the BABP edge-corrector problem, found an exact certificate below `0.0347`, demoted the DFP black-box route, and reduced the next theorem question to a precise bridge. The later hostile audit corrected the scope but strengthened the mathematical status of the core certificate.

## Stable claim promotion

`research/claim-registry.md` is the status index for project-specific mathematical claims on `main`.

`BABP-EDGE-001` is `verified`. Audit record:

- commit `d1ef2ca`;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

No project claim currently states finite-seed convergence at `lambda=1/40` or existence of limiting edge speeds.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required by active research. Deprecated IPS wiki material does not override the canonical patch paper.
