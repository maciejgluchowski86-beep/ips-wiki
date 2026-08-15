# Project state

This is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Research architecture

The group has one persistent ChatGPT Professor directing persistent graduate-student sessions. At most two sessions are in flight at once. The Professor owns scientific direction, proof spines, audits, opportunity-cost judgments, and closure decisions. Students do specified autonomous technical work and persist with their scientific direction.

The repository is canonical technical memory. Conversation links are optional only; successor sessions must rely on repository handovers and exact transcript transfer when necessary.

## Active scientific direction

**1D BABP from a finite seed.**

- Research branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Positive target: for every `lambda>0`, prove local convergence of one-dimensional biased annihilating branching process started from a finite nonempty particle set to Bernoulli equilibrium of particle density `lambda/(1+lambda)`.
- Known range: classical finite-seed convergence is known for `lambda>0.0347`.
- Main obstruction: BABP self-duality reduces local convergence to decay of a finite-test signed observable with factor `-1/lambda`; for small `lambda` this observable is badly conditioned and global particle-number growth does not control it.
- Current proof-spine bottleneck: reconstruct the exact origin of the historical `0.0347` threshold and determine whether the 2025 all-parameter DFP/linear-growth inputs remove that obstruction or expose a sharper non-dual missing lemma.
- Professor: persistent ChatGPT Professor.
- Active graduate student: Graduate Student B, to be created for this new direction.
- Concurrent bounded reconnaissance: Graduate Student A scans recent high-quality progress/open-problem literature and compares a small set of alternative targets against BABP on expected value.
- Latest group meeting: none yet in the BABP workspace.

Why this target: the canonical patch paper explicitly records finite-seed BABP convergence as unresolved for part of the parameter range. Martinelli--Shapira--Toninelli (2025) add strong all-parameter structure -- DFP exponential ergodicity, BABP linear growth from finite seeds, and product-law convergence -- while still recording the finite-seed gap. This makes the remaining obstruction more localized than in the preceding FA-1f programme.

BABP is the current working target, not an irreversible commitment and not a commitment to duality/cancellation as method. If the historical obstruction audit shows that the modern inputs do not materially change the old threshold mechanism, the Professor will compare BABP immediately against the reconnaissance pool before inventing another representation.

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

This closure is not the previously closed Bernoulli-quench sibling route. The obstruction is stronger: the complete positive coefficient transfer is conservative.

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

## Reusable negative lessons

- Wrong-norm or wrong-weight cancellation is usually fatal when the critical conversion exactly restores the lost scale.
- A strict local gain must be tested under the first nontrivial composition and in the controlling quantity.
- For FA-1f, both the centered positive transform and the full unnormalized patch coefficient transfer reduce to the same conservative dynamics; restricted routing losses are redistributed globally.
- For FA-1f sibling cancellation, the apparent two-generation gain fails at the next nontrivial composition.
- For 2D FA-1f relaxation, the reversible Dirichlet form lacks the cross-term required by the proposed local signed-move mechanism, and the nearest-vacancy capacity observable has the wrong scale.
- For SQG, scale-covariant solutions restore exactly the zero-mass-kernel gain.
- For Strong-KPP, the cancellation route has no endpoint margin.
- For stochastic cascades, improving a nodewise amplitude majorant without changing the explosion mechanism does not attack the obstruction.
- Substantial prior model-assisted effort without a route is real tractability evidence and should enter opportunity-cost judgments, even when it is not a mathematical refutation.

## Research heuristics

These are heuristics, not gates.

- Work from the actual obstruction.
- Unresolved is a research state, not a rejection criterion.
- Test scaling, weights, and first composition early.
- Preserve useful failures when they identify a reusable obstruction.
- Use independent audits after there is a central claim worth attacking, not as a substitute for sustained development.
- Close directions on expected-value grounds when the remaining route is only an unspecified hope for a new mechanism.
- Use recent serious progress/survey papers and explicit open-problem lists as a problem-first target source; do not force cancellation, duality, or patches into candidates.

## Group-meeting homeostasis

Every substantial student handoff is followed by a Professor group meeting before another substantial variant is assigned. Each meeting records exactly `state_narrowed: yes` or `state_narrowed: no` with a concrete evidence pointer. Three consecutive `no` meetings trigger an outside stagnation consultant; the Professor retains authority.

## Stable claim promotion

`research/claim-registry.md` is the status index for project-specific mathematical claims on `main`. A central theorem requires independent hostile correctness review and novelty checking before verified promotion.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required by active research. Deprecated IPS wiki material does not override the canonical patch paper.
