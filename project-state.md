# Project state

This file is the compact current-state index for the autonomous research programme. It is not a workflow scheduler. Git history and the files under `research/` carry the detailed record.

## Research architecture

The group is organized as a persistent ChatGPT Professor directing persistent graduate-student sessions.

At adoption of this revision:

- the former Research Lead becomes the **Professor**;
- the former Research Partner becomes the first **Graduate Student**.

The Professor directs and audits the big picture. Graduate students do specified autonomous hands-on research. The Professor may do mathematics directly when useful, but that is not its default function.

Professor and student sessions are kept alive as long as the platform permits. If a session reaches a platform length limit, the successor continues the same role lineage. Conversation links are optional pointers only; the protocol does not assume a successor can read an authenticated predecessor conversation. Repository handover plus exact transcript transfer is the fallback.

Many sessions may remain alive and idle. At most two sessions may be in flight at once.

There is no Director, Integrator, seven-gate examination, SEARCH/DEVELOP/VERIFY state machine, reserve-programme requirement, fixed worker taxonomy, fresh-session default, 900-word dispatch, or `Next cycle` instruction.

## Active scientific direction

**1D hard FA-1f from a finite seed.**

- Research branch: `research/fa1f-finite-seed`
- Positive target: for every `q in (0,1)`, prove local convergence of one-dimensional hard FA-1f started from a single vacancy to its Bernoulli product equilibrium law; finite nonempty vacancy sets are the natural later extension.
- Main obstruction: the hard model is non-attractive and lacks the uniform pure-death component used twice in the canonical patch-paper convergence theorem; finite-seed point masses are not usefully bracketed by nondegenerate product laws in centered-moment order.
- Current proof-spine bottleneck: verify and assess a claimed centered `h`-transform reduction to a positive finite-set process in which every active site refreshes membership of its two neighbours independently to Bernoulli(`q`).
- Professor: persistent ChatGPT Professor.
- Active graduate student: Graduate Student A.
- Active workspace: `research/active/fa1f-finite-seed/`
- Latest group meeting: none yet.

This is not a reopening of the closed 1D Bernoulli-quench sibling-cancellation route. The active target has deterministic finite-seed initial data and the current route is an exact positive dual/`h`-transform calculation rather than a generation-by-generation signed sibling contraction. Graduate Student A's first assignment explicitly checks whether the transformed simultaneous-neighbour refresh is secretly equivalent to the closed mechanism; if so, that subroute will be stopped rather than renamed.

A new graduate student is not being spawned at initialization. One persistent student is enough to settle the first exact bottleneck calculation.

## Professor review and homeostasis

After each substantial student handoff, before sending the same thread into another substantial variant, the Professor reads the decisive raw technical material and holds an asynchronous group meeting.

Each meeting records `state_narrowed: yes | no` with a pointer to the evidence.

A new speculative variant does not by itself count as narrowing. Narrowing means target-relevant uncertainty was actually reduced by a proof, counterexample, route elimination, sharper reduction or obstruction, improved controlling estimate, necessary-hypothesis change, material literature resolution, or comparable mathematical information.

The Professor may close or redirect a direction on expected-value and opportunity-cost grounds. It does not need an impossibility theorem or proof that all imaginable methods fail.

After three consecutive no-narrowing meetings, Claude mechanically launches a fresh outside Stagnation Consultant. The consultant advises; the Professor retains authority and must respond explicitly. Three further no-narrowing meetings trigger another fresh consultation.

## Canonical prior work: patch construction

The principal's manuscript `paper/`, *Patch representations and convergence for facilitated spin systems*, is the canonical project source for the patch construction and its proofs. It supersedes the deprecated IPS wiki layer on these points.

In particular, the paper proves conditional patch factorization over the successful-interaction skeleton and the resulting exact patch representation of the spin-system semigroup. Old wiki pages that still describe these as conditional are stale and must not be used as project authority.

The patch construction is a preferred reusable research asset when it naturally applies: retain a successful-interaction skeleton, decompose local spacetime histories into patches, condition on the skeleton, and average signed local contributions before global comparison. It is not a mandatory template for new work.

The canonical patch claims are indexed in `research/claim-registry.md`.

## Reusable observations from closed work

Two observations from the terminated quadratic-Hessian programme survived hostile audit without becoming the target theorem of a successful programme:

- the time-integrated first-moment norm of one centered heat-Hessian edge from $C^\alpha$ to $C^\beta$ has sharp cost $\asymp(\alpha-\beta)^{-1}$ on compact exponent ranges;
- the ordered-time derivative-cluster norm satisfies $\mathfrak P_m(\alpha,T)\leq 2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}$.

Classical local heat/Hermite cancellation remains reusable background mechanism evidence, not project novelty by itself. As a calibration, two first-derivative Gaussian marks admit the exact conditional-coarsening $L^1$ ratio

$$
\kappa=\frac{\pi}{2e},
$$

and independent clusters tensorize as $\kappa^n$.

## Closed programmes and routes

The following programmes are permanently closed and are not to be retried:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching; and
- Gaussian bridge coarsening.

The following screened routes are also closed and are not to be revived by renaming them:

- 1D FA-1f Bernoulli-quench sibling cancellation;
- strongly non-harmonic Wigner--Fokker--Planck via unweighted Moyal/skew cancellation;
- 2D FA-1f relaxation logarithm via local signed-move cancellation;
- the nearest-vacancy annular/electrical-capacity observable for that 2D FA-1f route; and
- the general bootstrap-percolation sharpness route based only on bare inclusion--exclusion/Bonferroni overlap subtraction.

The broader mathematical problems may remain open. What is closed is the recorded programme or route.

## Expensive dead ends worth remembering

- Quadratic-Hessian did not lead to a sufficiently worthwhile positive target despite producing reusable estimates.
- Fresnel integrability collapsed to classical/low-payoff mathematics for the project.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged.
- For Strong-KPP, the proposed cancellation route has zero margin at critical ends, while connected-limit detuning produces a linear error that dominates the hoped-for quadratic gain at sufficiently small amplitude.
- For supercritical SQG, smooth scale-covariant solutions can restore exactly the critical-scale loss that the zero-mass-kernel cancellation was meant to remove; no equation-generated exclusion of the saturating family was found.
- Deterministic restarting of the marked branching representation gives no strict first-moment maturity gain: value-only positive majorants spend the same blow-up budget and restarted gradient kernels are not better.
- Gaussian bridge coarsening gives an exact strict contraction, but it is an instance of classical conditional-expectation contraction rather than a new obstruction-level mechanism.
- In the 1D FA-1f sibling route, cancellation visible at two generations is lost at the next nontrivial composition, restoring the critical scaling.
- For strongly non-harmonic Wigner--Fokker--Planck, the weighted coercive norm introduces a translated-bump loss that destroys the unweighted Moyal/skew gain at the relevant level.
- For the 2D FA-1f local signed-move route, the relevant reversible Dirichlet form is a sum of squared individual increments without the needed sign cross-term.
- The nearest-vacancy annular/electrical-capacity observable gives the wrong scale after the pivotal-shell calculation; concentrating variation near the typical radius also fails to produce the desired logarithmic improvement.
- Bare inclusion--exclusion/Bonferroni overlap subtraction did not provide a sufficiently distinctive obstruction-level route to general bootstrap-percolation sharpness.

## Research heuristics

These are heuristics, not gates.

- Work from the actual obstruction. A cancellation that exists only in a weaker or unweighted quantity is not useful unless it survives in the norm or quantity controlling the theorem.
- Test the first nontrivial composition and natural critical scaling early when a proposed local gain is central.
- Stress a mechanism on examples selected from the obstruction, not examples selected to flatter the mechanism.
- Do cheap decisive mathematics before exhaustive literature work, while still checking novelty before making a strong claim.
- A classical technique may support new mathematics. Novelty should be located in the theorem or obstruction-level consequence, not in the mere existence of cancellation or conditional averaging.
- Repeated failed variants with no genuine narrowing are evidence against tractability even when no impossibility theorem is available.

## Research workspace

Workspace documentation and templates live under `research/`.

For a new direction the Professor creates a branch `research/<short-programme-slug>` and a directory `research/active/<short-programme-slug>/` containing at least:

- `state.md`;
- `proof-spine.md`;
- technical notes as needed;
- `literature.md`;
- `audit-log.md`;
- `meetings/`;
- `students/`; and
- `handover.md` when a session succession is pending or completed.

The repository is canonical technical memory. Persistent conversations are working memory.

## Stable claim promotion

`research/claim-registry.md` is the mechanical status index for project-specific mathematical claims on `main`.

A manuscript being present on `main` does not make its theorems verified. Verified claims point to durable independent audit records. Principal-designated canonical claims are recorded explicitly.

The Professor owns scientific promotion; Claude verifies registry and repository metadata mechanically.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required to understand or check active research or a theorem.

Do not run systematic legacy migration, generic reading-path expansion, or periodic curation while the freeze is in force.

When the first central theorem of a new programme enters independent audit, the Professor raises the freeze for principal review. Nothing automatically unfreezes it.

Deprecated IPS wiki material is superseded by the canonical patch paper where they conflict.

## Principal-facing status

The principal may check in daily or more often.

The Professor's brief should state the active target, what changed mathematically, what raw material the Professor inspected, the current proof-spine bottleneck, strongest positive and negative evidence, whether the state narrowed, the continue/pivot/close decision, next assignment, and any pending outside consultation or genuine principal-level question.

Daily check-ins are informational and do not pause autonomous work.
