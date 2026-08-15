# Project state

This file is the compact current-state index for the autonomous research programme. It is not a workflow scheduler. Git history and the files under `research/` carry the detailed record.

## Research architecture

The old cycle architecture is retired. Research is now carried by two persistent ChatGPT sessions: a Research Lead and a Research Partner. At most two sessions may be in flight at once; idle sessions remain available with their context intact. Fresh sessions are used episodically for independent audit rather than as the default research workforce.

There is no Director, Integrator, pre-nomination gate examination, SEARCH/DEVELOP/VERIFY state machine, reserve-programme requirement, or `Next cycle` instruction.

Target selection is autonomous. Once a credible programme is selected, the default is sustained work on that problem. There is no hard time cap. Programmes are closed for substantive mathematical or literature reasons, not because a fixed amount of time elapsed.

## Active programme

**None yet.**

The persistent Lead and Partner are to select a new programme autonomously under `CHATGPT.md` and then work on it continuously. Previously closed programmes and routes listed below are not to be retried.

When a programme is selected, record here its short title, branch, target, main obstruction, current bottleneck, and active research-note path.

## Canonical prior work: patch construction

The principal's manuscript `paper/`, *Patch representations and convergence for facilitated spin systems*, is the canonical project source for the patch construction and its proofs. It supersedes the deprecated IPS wiki layer on these points.

In particular, the paper proves conditional patch factorization over the successful-interaction skeleton and proves the resulting exact patch representation of the spin-system semigroup. Old wiki pages that still describe these as conditional are stale and must not be used as the project authority.

The patch construction is a preferred reusable research asset when it naturally applies: retain a successful-interaction skeleton, decompose one-site spacetime histories into patches, condition on the skeleton, and average local signed contributions before global comparison. It is not a mandatory template for new work.

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

## Research workspace

Workspace documentation and templates live under `research/`.

For a new programme the Lead creates a branch `research/<short-programme-slug>` and a directory `research/active/<short-programme-slug>/` containing at least:

- `state.md`;
- technical notes or TeX files as needed;
- `literature.md`;
- `audit-log.md`; and
- optional `partner/` notes.

The templates under `research/templates/` are starting points, not mandatory forms.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required to understand or check active research or a theorem.

Do not run systematic legacy migration, generic reading-path expansion, or periodic curation while the freeze is in force. Existing wiki content is left in place for now. Deprecated IPS wiki material is superseded by the canonical patch paper where they conflict.

`wiki-curation-state.json` may remain as historical/mechanical state but does not schedule work under the current protocol.

## Principal-facing status

The principal may check in daily or more often. The active programme's `state.md` should contain a short brief explaining what changed, what was proved/refuted/clarified, the present bottleneck, reasons to continue or doubt the programme, what comes next, and any genuine principal-level question.

Daily check-ins are informational and do not pause autonomous work.
