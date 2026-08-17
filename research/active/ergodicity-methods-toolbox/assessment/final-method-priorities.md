# Final method priorities after hostile cross-review

Date: 2026-08-17

Status: **Professor synthesis completing the applicability assessment governed by `assessment-protocol.md`.**

This synthesis uses the frozen 74-method inventory, both complete primary audits, Student G's independent hostile review of the Professor-owned FA-1f/East shortlist, and the Professor's hostile review of Student G's positive-rates shortlist. It does not add or revise toolbox entries and does not modify `docs/` or `mkdocs.yml`.

## 1. Decision summary

The hostile reviews materially narrowed both primary shortlists.

### FA-1f / East Bernoulli quench

Primary shortlist: 1 A + 4 B.

Hostile result:

- East distinguished-zero screening — **PASS**;
- refined non-diagonal discrepancy coupling — **DEMOTE**;
- information percolation / adaptive backward histories — **PASS**;
- front regeneration / renewal — **DEMOTE**;
- state-dependent dynamical disagreement percolation — **KILL**.

**Final recommendation:** reopen the FA-1f Bernoulli-quench programme for one bounded proof block on a two-sided causal-screen theorem. Keep adaptive information histories as the independent reserve architecture. Do not reopen a separate front-regeneration, disagreement-percolation, or chronology-switch programme unless one first produces the specific missing local object recorded below.

### Positive-rates conjecture

Primary shortlist: 1 A + 4 B.

Hostile result:

- Gray one-dimensional edge coalescence — **PASS**;
- refined non-diagonal discrepancy coupling — **PASS**;
- information percolation — **PASS**;
- block coupling / joint-block stationary control — **DEMOTE**;
- disagreement-front regeneration — **DEMOTE**.

The three PASS rulings reduce to **two research families**: nonbasic one-dimensional coupling (refined coupled rates as the concrete first mechanism, Gray edge geometry as the structural target) and information percolation.

**Final recommendation:** do **not** reopen the positive-rates proof programme yet. First run the two bounded structural falsification experiments in Section 4. A positive exact signal from either can justify a new narrowly stated proof block. Until then Meeting 030's `no-credible-route` / signed-boundary-transmission restart bar remains operative.

## 2. FA-1f / East final ranking

### FA-1. Two-sided causal screening — REOPEN, first priority

Source method: East distinguished-zero screening.

Why it survives: the literal East theorem is oriented and does not transfer, but the adapted bridge asks for a genuinely new two-sided graphical sigma-field rather than assuming orientation. The independent review found no chronology/dual obstruction ruling out such an approximate causal screen. Once the screen exists, the downstream relaxation is already available from the positive finite-volume FA spectral gap.

#### Strongest bridge lemma: FA-SCREEN

Fix equilibrium vacancy density `q>0`, Bernoulli initial vacancy density `q0>0`, and a finite observation interval `A`. Prove that there exist deterministic `s_t -> infinity`, events `E_t`, random times `tau_t <= t-s_t`, random finite intervals `I_t` containing `A`, and screen data `S_t` such that:

1. `P_{mu_{q0}}(E_t^c) -> 0`;
2. on `E_t`, `|I_t| = o(s_t)`;
3. `S_t` and the event `E_t` can be determined without revealing the Poisson/coin marks in the protected interior `I_t x (tau_t,t]` that will subsequently drive relaxation;
4. conditional on the past and on `S_t`, the protected interior marks on `(tau_t,t]` are fresh and the evolution of the spins in `A` up to time `t` is unaffected by the exterior configuration except through boundary data for which the finite-volume FA relaxation estimate applies;
5. the conditional law at time `tau_t` inside `I_t` is absolutely continuous with respect to the Bernoulli-`q` equilibrium law with an `L^2` cost at most `exp(C_q |I_t|)` (the trivial finite-state bound is enough).

If the finite-volume FA gap is `gamma(q)>0`, then on `E_t` the local relaxation error is bounded schematically by

`exp(C_q |I_t| - gamma(q) s_t)`,

which tends to zero by item 2. Together with `P(E_t^c)->0`, this yields convergence on `A` from `mu_{q0}` to `mu_q`.

This is stronger than the desired conclusion but is not a restatement of it: items 3--4 are explicit causal-measurability/freshness statements that can be falsified locally.

#### Exact obstruction avoided

- It does not use coefficientwise positivity or the conservative `h`-weighted dual/patch transfer.
- It does not exogenize the two-sided boundary facilitation signal.
- It does not require worst-case convergence and therefore does not conflict with the all-ones trap.
- It uses the known FA gap only after memory has been screened, so it does not confuse equilibrium coercivity with the singular-start problem.

#### First proof experiment

**Finite graphical leakage test.** Specify the simplest proposed left/right marker or corridor rule on a 5--7-site window. Exhaustively compare exterior continuations that agree on all declared screen data. Reject the rule if an exterior continuation can change any interior ring's legality, change future screen variables, or if conditioning on screen success reveals any interior mark that is supposed to remain fresh. This is the first gate before tail estimates.

### FA-2. Quench-specific adaptive information histories — PASS, reserve architecture

Source method: information percolation / backward update histories.

Why it survives: hard FA has no state-independent oblivious mark that can be used exactly as in high-temperature Glauber dynamics, so the Lubetzky--Sly construction does not transfer literally. But a Bernoulli-quench-specific **adaptive** reveal process can short-circuit the OR facilitation constraint after discovering an actual vacancy, merge histories, and delete logically irrelevant branches. The independent review found no theorem identifying this minimal causal information with the conservative transformed dual.

#### Strongest bridge lemma: FA-INFO

Construct, for each finite observation set `A` and time `t`, an adaptive decision/reveal procedure on the common graphical construction with a random time-zero information object `R_t(A)` and an exact second-moment comparison of the form

`chi^2( Law_{mu_{q0}}(eta_t|_A), Law_{mu_q}(eta_t|_A) )`

`<= E[ W_q,q0(R_t,R_t') | revealed non-red history ] - 1`,

where `R_t,R_t'` are conditionally independent copies of the residual time-zero information and `W_q,q0` is the product-likelihood intersection weight generated by the two Bernoulli initial laws. Prove that the right-hand side tends to zero for every fixed `A`.

The construction must be state-adaptive: at a legal FA ring, discovering one vacant neighbour may terminate the other branch; histories may merge; and illegal rings may require both neighbours plus the old-site history. The second-moment bound must be proved for this actual reveal process rather than quoted from the mark-only Ising history theorem.

This gives local total-variation convergence of the Bernoulli quench to equilibrium without requiring all histories to die and without requiring convergence from the trapped all-ones state.

#### Exact obstruction avoided

The target is causal information, not the positive mass of the exact finite-set dual. Therefore stochastic conservation of the `h`-weighted dual transfer does not imply conservation of `R_t`. The method also avoids exogenous boundary facilitation and worst-case disagreement domination.

#### Second proof experiment

**Exact adaptive-decision-tree test.** On a small space-time slab, compute the exact minimal decision tree for one terminal site under product initial vacancies and actual graphical marks, including short-circuit evaluation of the FA OR constraint. Compare one- and two-block distributions of residual time-zero information with the naive branching majorant. If adaptive pruning/merging shows no quantitative improvement in low-`q` stress tests under any natural reveal statistic, demote before multiscale work. A first-moment dual-particle count is not an admissible kill statistic.

### FA methods not to reopen separately

- **Refined non-diagonal chronology coupling — DEMOTE.** The source theorem is conservative/monotone exclusion. An unrestricted measure-preserving endpoint-history injection is essentially the target cross-product inequality itself. Retain only a bounded local switch-state feasibility test; no proof programme until a predictable finite switch state closes under every adjacent FA update.
- **Front regeneration — DEMOTE.** In the Bernoulli sea there is no independent canonical fresh front. Once the proposed two-front object has enough no-reentry/freshness to work, it is an implementation of FA-SCREEN, not a distinct architecture. It remains more natural for the separate finite-seed problem.
- **State-dependent disagreement percolation — KILL as an independent architecture.** Product-background transmission probabilities are not iterable along a path conditioned on disagreement survival. Uniform domination returns to the all-ones worst-case obstruction; law-dependent domination first requires screening/adaptive-history control.
- **Equilibrium coercivity families — auxiliary only.** Positive FA gap is already known for every `q>0`; these methods belong downstream of FA-SCREEN rather than upstream of the quench problem.
- **Relative-entropy Gibbs-attractor shortcut — X.** The checked theorem requires irreducibility R6, which hard FA violates at the all-ones trap.

## 3. Positive-rates final ranking

### PR-1. Nonbasic one-dimensional coupling / Gray edge geometry — PASS family, first priority after feasibility

This combines two primary candidates rather than funding them independently.

The checked Gray theorem uses attractiveness/repulsiveness to create protected hybrid regions and ordered noncrossing edges. Those hypotheses fail in the residual chamber. The checked refined-discrepancy theorem is conservative exclusion-specific. What survives is a concrete design question: can one build a genuinely different finite-range coupled generator by pairing different microscopic moves?

#### Strongest first bridge: PR-COUPLE

For every residual rate triple, construct a translation-covariant finite-range Markovian coupling of two copies of the spin system, allowed to pair a flip at site `i` in one marginal with a flip or null/different-site flip in the other, such that for every pair with finite disagreement set `D`,

`bar L |D| <= -kappa |D|`

for some `kappa>0` depending on the rates but not on the configuration.

Then

`E|D_t| <= exp(-kappa t)|D_0|`.

Finite propagation reduces arbitrary initial configurations on a fixed observation interval to `O(t)` initial discrepancies, and `O(t)e^{-kappa t}->0`, yielding local mixing and uniqueness.

This is deliberately stronger than necessary. Its value is that it is exactly and cheaply falsifiable.

#### Gray structural upgrade if PR-COUPLE is locally feasible

On the same coupled-rate variables, test whether one can define scalar splice-edge variables satisfying local no-crossing, permanent coalescence, and protected-region identities. If such identities exist without a hidden spin order, Gray's density/coalescence architecture becomes a credible nonmonotone one-dimensional target. If the stronger Hamming drift fails but the edge identities remain feasible, Gray may still survive as a weaker route.

#### Exact obstruction avoided

- The common-uniform certificate `alpha(t)>1` applies to the old coupling, not to a new joint generator.
- The balanced-circulation theorem rules out scalar Foster/coboundary corrections, not arbitrary coupled transition rates.
- No positive coefficient norm or signed PR1 estimate is used.

### PR-2. Information percolation / sparse red histories — PASS, independent bypass

This is the genuinely different positive-rates family.

Strict positivity permits a random-map decomposition with state-independent reset-to-zero/reset-to-one marks plus residual local maps. Backward histories can therefore contain genuine oblivious deaths, but near the hard near-East point a naive first-moment branching bound is expected to be too crude.

#### Strongest bridge lemma: PR-INFO

For a finite observation set `A`, choose an admissible random-map decomposition and let `R_t(A)` denote the top sites whose minimal backward histories still carry time-zero information after conditioning on the non-red history. Prove a volume-uniform pair-intersection estimate strong enough for a Miller--Peres-type `L^2` bound, for example

`E[ 2^{|R_t intersect R_t'|} | green/non-red history ] - 1 <= C_A e^{-gamma t}`,

or an explicitly derived analogue for the optimized random maps.

Then the law on `A` becomes independent of the initial configuration even though some histories may survive. This bypasses common-coupling extinction, CFTP/clan extinction, the stationary diameter hierarchy, and the signed boundary-transmission operator.

#### Exact obstruction avoided

The trajectory-valued spatial Dobrushin coefficient one concerns full conditional path laws and does not imply nondecay of minimal backward information after averaging over reset maps. Likewise `alpha(t)>1` is specific to common-uniform coupling. The method must not be reduced to an expected-offspring `<1` test.

### Positive-rates methods not to reopen now

- **Joint-block Bellman control — DEMOTE.** The proposed bridge inequality is, by the exact scale-extension identity, equivalent to the desired fixed-fraction diameter contraction unless an independent cross-block theorem is supplied. Meeting 024 already stopped the search for such a theorem through additive/fixed-block correctors.
- **Disagreement-front regeneration — DEMOTE.** Meeting 019 identified hidden right-ancestry capacity not retained by the local front state and explicitly stopped the common-uniform global-coalescence/occupation interface. Naming the missing fresh state `regeneration` does not create it.
- **Dobrushin/path/basic-coupling contraction, scalar Foster families, reversible comparison, larger coefficient/norm searches, and bare tail-shift variants** remain blocked exactly as recorded in the positive-rates programme. Do not recycle them under new terminology.
- **Signed PR1 connected-renewal route** remains at Meeting 030's boundary-transmission blocker; no method in the frozen toolbox supplied a credible new cancellation-preserving estimate for it.

## 4. At most two first experiments per problem

### FA-1f

1. **FA-SCREEN leakage/measurability test** on the smallest concrete two-sided marker rule. This is the gate for the recommended reopened proof block.
2. **FA-INFO adaptive decision-tree test** on one/two temporal blocks, measuring actual residual causal information rather than transformed-dual particle count.

### Positive rates

1. **Exact rational non-diagonal coupled-rate LP at the hard point** `P_h=(1/10000,1/100,9999/10000)`. Maximize `kappa` under exact marginal constraints for every unavoidable local pair pattern. On the same variables, add Gray no-crossing/protection/coalescence constraints. A certified `kappa<=0` kills PR-COUPLE in its stated form; local infeasibility of the edge constraints kills the direct Gray extension.
2. **Finite-depth optimized pair-support calculation for PR-INFO.** Enumerate admissible deterministic local random maps, optimize the reset/residual decomposition for backward-support sparsity, and compute the exact pair-support/intersection transfer. A meaningful negative certificate must concern nondecay of the pair-intersection quantity uniformly over admissible decompositions; a supercritical first-moment branching number is insufficient.

## 5. Programme decisions

### FA-1f / East

**Recommend reopening.** The reopening should be narrow: one proof block whose sole theorem target is FA-SCREEN, beginning with the finite leakage/measurability gate. Success on the causal screen has a verified short downstream chain to Bernoulli-quench convergence through the known positive FA gap. Failure of the simplest screen constructions should trigger reassessment before enlarging marker state spaces indefinitely.

Adaptive information histories are the reserve architecture. Do not run both as full proof programmes simultaneously unless the principal explicitly chooses parallelism after the first screen gate.

### Positive rates

**Recommend no reopening yet.** The stopped programme's restart bar remains justified. The two surviving families are credible enough for bounded exact experiments but not yet for an infinite-volume proof block. Reopen only if:

- the non-diagonal LP/Gray test returns a concrete feasible joint generator or edge identity that survives all local patterns; or
- the optimized information-history calculation shows a genuine pair-intersection contraction mechanism not reducible to ancestor extinction or a known norm obstruction.

Absent such a signal, retain `no-credible-route` rather than spending another block on generic coupling engineering.

## 6. Assessment phase close

The frozen toolbox remains at 74 methods. The applicability assessment has now completed:

- complete primary audit for both targets;
- independent hostile attack of each primary shortlist by the party that did not produce it;
- final problem-specific ranking and restart recommendation.

No public taxonomy/navigation change follows automatically from these rankings. The next action is a principal decision on the recommended FA reopening and on whether to authorize the bounded positive-rates feasibility experiments.