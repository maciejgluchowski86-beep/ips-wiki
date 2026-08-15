# Project state

This file is the compact current-state index for the autonomous research programme. It is not a workflow scheduler. Git history and the files under `research/` carry the detailed record.

## Research architecture

The project now uses a professor-and-graduate-students model.

- **Professor:** the former Research Lead, the persistent mathematician session holding the current mathematical thread.
- **Graduate Student A:** the former Research Partner, the persistent session that audited and redesigned the architecture.
- **Graduate Student B:** a separate persistent mathematical session to be created or resumed by Claude under `CLAUDE.md`.

The Professor is a ChatGPT session, not the human principal. The principal is the PI: they inspect progress and set scientific priorities but are not asked to referee proofs or manage technical work.

All regular group members work on the same active programme. Many sessions may remain alive and idle, but at most two sessions may be in flight at once. Fresh sessions are used episodically as outside experts, stagnation consultants, and independent auditors.

There is no Director, Integrator, pre-nomination gate examination, SEARCH/DEVELOP/VERIFY state machine, reserve-programme requirement, fixed worker dispatch, or `Next cycle` instruction.

The Professor owns target choice, proof-spine decomposition, assignments, recombination, opportunity-cost judgment, and programme closure. Students own technical attacks and have broad freedom in method.

Every active programme is periodically synthesized through Professor group meetings. After three consecutive completed meetings with no recorded mathematical information gain, Claude mechanically launches a fresh stagnation consultation. The consultation does not kill the programme automatically; it forces an outside expected-value review and an explicit Professor decision to continue, pivot, or close.

## Active programme

**None yet.**

The Professor is to choose a new programme autonomously with input from the graduate students. Previously closed programmes and routes listed below are not to be retried.

Reconnaissance is not intended to become a permanent mode. If no programme is active at two consecutive principal check-ins, `CLAUDE.md` requires an explicit Professor target-selection meeting.

When a programme is selected, record here its short title, branch, target, main obstruction, current bottleneck, proof-spine path, latest information gain, and active research-note path.

## Canonical prior work: patch construction

The principal's manuscript `paper/`, *Patch representations and convergence for facilitated spin systems*, is the canonical project source for the patch construction and its proofs. It supersedes the deprecated IPS wiki layer on these points.

In particular, the paper proves conditional patch factorization over the successful-interaction skeleton and proves the resulting exact patch representation of the spin-system semigroup. Old wiki pages that still describe these as conditional are stale and must not be used as the project authority.

The patch construction is a preferred reusable research asset when it naturally applies: retain a successful-interaction skeleton, decompose one-site spacetime histories into patches, condition on the skeleton, and average local signed contributions before global comparison. It is not a mandatory template for new work.

These canonical claims are indexed in `research/claim-registry.md`.

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

- Work from the actual obstruction. A cancellation that exists only in a weaker or unweighted quantity is not useful unless it survives in the norm or quantity that controls the theorem.
- Test the first nontrivial composition and natural critical scaling early when a proposed local gain is central.
- Stress a mechanism on examples selected from the obstruction, not examples selected to flatter the mechanism.
- Do cheap decisive mathematics before exhaustive literature work, while still checking novelty before making a strong claim.
- A classical technique may support new mathematics. Novelty should be located in the theorem or obstruction-level consequence, not in the mere existence of cancellation or conditional averaging.
- Repeated failure can be information even without an impossibility theorem. The Professor may close a programme on opportunity-cost grounds when the proof spine is not narrowing and better targets have higher expected value.

## Research workspace

Workspace documentation and templates live under `research/`.

For a new programme the Professor creates a branch `research/<short-programme-slug>` and a directory `research/active/<short-programme-slug>/` containing at least:

- `state.md`;
- `proof-spine.md`;
- technical notes or TeX files as needed;
- `literature.md`;
- `audit-log.md`;
- `meetings/`; and
- `students/`.

The Professor owns the state, proof spine, group-meeting synthesis, and principal-facing brief. Students keep substantial independent calculations under their own subdirectories when useful.

The repository is canonical long-term memory. Persistent sessions should regularly re-ground from the current state, proof spine, latest meeting note, and relevant technical files rather than relying on conversational memory alone.

## Stable claim promotion

`research/claim-registry.md` records the status of project-specific mathematical claims promoted to `main`.

A manuscript on `main` is a draft artifact by default and does not establish its own theorem claims. New or materially strengthened project-specific theorem claims promoted to `main` must be registered as `claimed`, `verified`, or principal-designated `canonical`, with audit references for `verified` claims.

Claude checks the presence of this metadata mechanically; mathematical correctness remains a ChatGPT responsibility.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required to understand or check active research or a theorem.

Do not run systematic legacy migration, generic reading-path expansion, or periodic curation while the freeze is in force. Existing wiki content is left in place for now. Deprecated IPS wiki material is superseded by the canonical patch paper where they conflict.

When the first central theorem of a new programme reaches independent audit, the Professor should ask in the principal-facing brief whether theorem-driven wiki work should expand. The freeze remains until the principal changes it.

`wiki-curation-state.json` may remain as historical/mechanical state but does not schedule work under the current protocol.

## Principal-facing status

The principal may check in daily or more often. The Professor's active `state.md` brief should report the active problem, mathematical change since the previous brief, proof-spine movement, present bottleneck, current direction decision, assignments, no-information-gain meeting count, pending audits or stagnation consultations, and any genuine principal-level question.

Daily check-ins are informational and do not pause autonomous work.
