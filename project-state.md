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
- New project datum: at `lambda=1/40=0.025`, a ten-site right-edge corrector has exact uniformly positive generator drift `1033/40000000`; claim `BABP-EDGE-001` is `claimed` pending fresh independent audit.
- Current proof-spine bottleneck: prove or refute that positive two-sided edge speed, together with the known invariant-law/global-growth inputs, yields finite-seed local convergence; first test `lambda=1/40`.
- Downstream analytic problem: construct positive finite-window edge correctors for every `lambda>0`, equivalently show the finite-window threshold tends to zero if the bridge is sufficient.
- Professor: persistent ChatGPT Professor.
- Active development student: Graduate Student B.
- Concurrent second session: fresh independent auditor for `BABP-EDGE-001`.
- Graduate Student A: idle after bounded opportunity-cost reconnaissance.
- Latest group meeting: `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`.

The programme graduated from provisional to committed at Meeting 003. Student B localized the historical numerical obstruction to a finite-state right-edge submartingale/corrector problem, analytically reproduced the old `1/3` cutoff at window size one, numerically reproduced `0.0346195435...` at window size eight, and supplied an exact rational positive-drift certificate below `0.0347` at window size ten. The Professor independently checked the generator formula, positive-drift-to-edge-speed implication, the `k=1` algebra, and a separately implemented `k=8`/`k=10` LP.

Graduate Student A's reconnaissance had favored the residual simple-IPS positive-rates/noisy-East problem over **provisional** BABP unless BABP produced a genuinely new small-parameter handle. The edge certificate satisfies that condition. Noisy East remains the strongest identified reserve candidate if the BABP bridge fails or the finite-window threshold problem proves sterile.

The programme is not committed to cancellation, duality, or patches as its main method. The active mechanism is a finite-state Markov-additive edge corrector. DFP quasi-duality has been demoted as a black-box route because the finite-test cylinder has no probability-law DFP representation and its finite-window signed representation has exponentially growing coefficient norm.

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
- The BABP edge calculation is a positive example of obstruction-first work: reconstructing the historical proof barrier exposed a finite-state optimization problem that could be improved immediately before any attempt at the full theorem.
- A computational certificate becomes strategically meaningful only when its generator encoding and theorem consequence are checked separately; the BABP claim therefore remains `claimed` until fresh audit.

## Group-meeting homeostasis

Every substantial student handoff is followed by a Professor group meeting before another substantial variant is assigned. Each meeting records exactly `state_narrowed: yes` or `state_narrowed: no` with a concrete evidence pointer. Three consecutive `no` meetings trigger an outside stagnation consultant; the Professor retains authority.

Meeting 003 records `state_narrowed: yes` because the group localized the historical BABP threshold, found a claimed exact edge certificate below it, demoted the DFP black-box route, and reduced the next theorem question to a precise bridge.

## Stable claim promotion

`research/claim-registry.md` is the status index for project-specific mathematical claims on `main`. `BABP-EDGE-001` is currently `claimed`; the fresh audit request is `research/active/babp-finite-seed/audits/001-edge-corrector-request.md`. It must not be promoted to `verified` until a durable independent audit supports the exact generator/certificate/speed claim.

No project claim currently states finite-seed convergence at `lambda=1/40`.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required by active research. Deprecated IPS wiki material does not override the canonical patch paper.
