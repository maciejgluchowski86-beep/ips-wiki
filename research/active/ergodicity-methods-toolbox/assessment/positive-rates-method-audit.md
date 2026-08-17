# Positive-rates applicability audit

Date: 2026-08-17

## Scope and rating standard

This audit assesses the frozen 74-method ergodicity toolbox against the positive-rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS. It is an applicability assessment, not a literature-collection wave and not a restart of the stopped proof programme.

Ratings follow `assessment-protocol.md`:

- **A**: actionable; a concrete bridge lemma, not known false and not equivalent to an exhausted route, would materially advance the target.
- **B**: plausible architecture; a coherent architecture survives the obstruction ledger, but several substantial bridges are still missing.
- **C**: auxiliary/diagnostic; useful for a sublemma, comparison, or falsification test, but not a target-level architecture.
- **X**: blocked by a specific hypothesis failure, exact obstruction, or exhausted equivalent route.
- **N**: no mathematically credible contact with the live target interfaces.

An `A` or `B` rating is invalid without an explicit bridge lemma. For every `A/B/C/X` disposition below, the matrix names a target interface and a repository/source pointer.

## Positive-rates target interfaces

### PR1: signed boundary transmission / connected renewal

The sharp residual object at the stopped hard point is the signed two-time boundary-transmission operator `V_N` isolated in positive-rates Meeting 030. Both scalar time kernels change sign and the input is the actual connected orbit. A bridge on this route must preserve that two-time cancellation strongly enough to make connected renewal coefficients summable or geometric. Taking absolute values before the two integrations does not qualify.

### PR2: common-coupling convective escape

For a finite initial disagreement set under the common-uniform coupling, the rightmost disagreement is nonincreasing and every fixed site couples permanently almost surely. Survival can therefore occur only by convective escape to minus infinity. A useful coupling/front method must decide extinction versus such escape, not merely reprove fixed-site coupling. See positive-rates `programme-established-results.md`, Section 1.

### PR3: stationary boundary-control diameter

For local `h`, the stationary occupation-control hierarchy gives decreasing diameters `D_N(h)`. Proving `D_N(h) -> 0` for every local `h` yields invariant-law uniqueness. Additive Bellman correctors without cross-block dependence cannot improve the endpoints; any useful new bridge must exploit genuinely cross-block information. See `programme-established-results.md`, Sections 1 and 3.

### PR4: shift / connected-tail decay

One-/two-step zero-boundary shift agreement, `Gamma_M -> 0`, general `J_{x,r} -> 0`, `(J-SPEC)`, and connected-tail summability remain open. A bare tail-shift reformulation does not clear the restart bar. See positive-rates Meetings 025--030 and the final `state.md`.

A method may also qualify through **PR5: a materially different target-level architecture** that bypasses PR1--PR4, but the implication chain must make the bypass explicit.

## Hard obstruction ledger used in the audit

The following are treated as established negative evidence rather than targets for another renamed attempt:

1. nearest-neighbour scalar edge-product/coboundary Foster certificates are ruled out at a hard residual point by exact balanced circulation;
2. no depth-uniform finite linear generator-mode closure contains the common-mass transfer;
3. the natural positive raw coefficient norms, including the component-count refinement, cannot be uniformly nonexpansive in depth;
4. the exact trajectory-valued spatial kernel has Dobrushin total-variation coefficient one;
5. additive Bellman correctors without cross-block dependence cannot improve the stationary endpoints;
6. another generic norm, reversible comparison, filter optimization, larger coefficient table, bare tail-shift argument, common-coupling occupation variant, or generic Bellman-corrector search does not restart the stopped programme;
7. finite-time Hamming contraction is not available at the hard near-East calibration point on the tested interval, while fixed-site common-coupling agreement is already known and is insufficient because convective escape remains possible.

Pointers: `research/active/positive-rates-conjecture/programme-established-results.md`; final positive-rates `state.md`; Meetings 025--030 on branch `research/positive-rates-conjecture`.

## Complete disposition table

Counts after inspecting all 74 live method pages: **A 1, B 4, C 25, X 10, N 34**.

| Method | Rating | Interface | Disposition |
|---|---:|---|---|
| Attractive monotone coupling and extremal invariant laws | **X** | PR2 | Residual chamber includes genuinely non-attractive/non-repulsive rates; attractiveness only reduces to extremal laws and cannot treat the hard residual point. Pointer: `docs/entries/attractive-monotone-coupling-extremal-laws.md`; positive-rates established-results §1. |
| Dobrushin influence contraction | **X** | PR4 | The stopped programme already computed Dobrushin TV coefficient 1 for the exact trajectory-valued spatial kernel, so the relevant worst-case influence contraction has no deficit. Pointer: `docs/entries/dobrushin-influence-contraction.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Path coupling | **X** | PR2 | At the hard near-East point the tested finite-time Hamming contraction satisfies `alpha(t)>1` on `0<t<=47`, and another generic metric/norm search is explicitly stopped. Pointer: `docs/entries/path-coupling-glauber-dynamics.md`; positive-rates established-results §1. |
| Coupling with stationarity / local uniformity | **C** | PR3 | Stationary typicality could diagnose which occupation controls matter, but the invariant law is the unknown object; without an independent high-mass good set this is circular. Pointer: `docs/entries/coupling-with-stationarity-local-uniformity.md`; positive-rates established-results §3. |
| Block coupling by joint block resampling | **B** | PR3 | Joint blocks can use cross-block dependence that the additive Bellman obstruction leaves open; a two-block contraction of occupation-control diameter would close the stationary hierarchy. Pointer: `docs/entries/block-coupling-joint-resampling.md`; positive-rates established-results §3. |
| Coupling independence / pinned-law coarse comparison | **X** | PR4 | Applied to right-boundary pinnings, the required uniform conditional-law coupling is essentially the unresolved shift/boundary-agreement estimate; the source also assumes Gibbs conditional laws. Pointer: `docs/entries/coupling-independence-coarse-grained-comparison.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Weighted synchronous Wasserstein contraction | **X** | PR2 | Requires an order-compatible dissipative weighted distance; the residual model is nonmonotone and positive raw coefficient/weighted norm contractions have exact obstructions. Pointer: `docs/entries/weighted-wasserstein-contraction-infinite-ips.md`; positive-rates established-results §1. |
| Maximal local coupling for nonmonotone Potts | **X** | PR2 | For binary same-site updates the common-uniform/maximal local coupling already realizes the optimal one-site mismatch; local Hamming contraction still fails at the hard point. Pointer: `docs/entries/maximal-local-coupling-nonmonotone-potts.md`; positive-rates established-results §1. |
| Sticky McKean--Vlasov coupling | **N** | — | The sticky scalar diffusion mechanism uses continuous radial noise and mean-field law dependence absent from the binary Poisson spin system. Pointer: `docs/entries/sticky-coupling-mckean-vlasov.md`. |
| Componentwise reflection coupling | **N** | — | Reflection of Brownian coordinates and mean-field `1/N` error cancellation have no natural analogue in this local binary jump system. Pointer: `docs/entries/componentwise-reflection-uniform-mean-field.md`. |
| Asymptotic binding coupling | **C** | PR5 | A localized absolutely-continuous change of graphical noise could in principle bypass common-coupling extinction, but no finite-cost Poisson intervention adapted to an escaping disagreement is presently identified. Pointer: `docs/entries/asymptotic-coupling-infinite-dimensional-spde.md`; positive-rates final state / Meetings 025--030. |
| Asymptotic reflection coupling for SPDEs | **N** | — | Its load-bearing Hilbert-space reflection regularization is specific to additive continuous noise. Pointer: `docs/entries/asymptotic-reflection-coupling-monotone-spde.md`. |
| Refined non-diagonal discrepancy coupling | **B** | PR2 | It shows how to abandon the basic coupling and pair different microscopic moves while controlling discrepancies; a local coupled-rate construction could directly attack convective escape. Pointer: `docs/entries/refined-discrepancy-coupling-general-exclusion.md`; positive-rates established-results §1. |
| Second-class-particle shock coupling | **C** | PR2 | Treating the rightmost disagreement as a retained marker is a useful diagnostic, but exact autonomous shock closure is model-specific and would not itself rule out escape. Pointer: `docs/entries/second-class-particle-shock-random-walk.md`; positive-rates established-results §1. |
| Environment seen from a second-class particle | **C** | PR2 | The moving-frame environment is a natural way to analyze disagreement survival/escape, but existence of a stationary front law is compatible with persistent escape and gives no contradiction by itself. Pointer: `docs/entries/environment-seen-second-class-particle.md`; positive-rates established-results §1. |
| Censoring inequalities | **X** | PR2 | The theorem requires monotone dynamics and ordered initial laws, precisely unavailable in the residual nonmonotone chamber. Pointer: `docs/entries/censoring-monotone-glauber-dynamics.md`; positive-rates established-results §1. |
| Dynamical disagreement percolation | **C** | PR2 | A coarse subcritical disagreement-path estimate would rule out escape, but naive domination loses state-dependent cancellation and fixed-site agreement is already known. Pointer: `docs/entries/dynamical-disagreement-space-time-percolation.md`; positive-rates established-results §1. |
| Gray one-dimensional edge coalescence | **A** | PR2 | This is the closest theorem: if Gray's protected hybrid edges/noncrossing/coalescence can be realized by a nonbasic coupling in the residual chamber, the positive-rate local repair closes ergodicity. Pointer: `docs/entries/one-dimensional-edge-coalescence-positive-rates.md`; positive-rates established-results §1. |
| Static disagreement percolation | **N** | — | It is a Gibbs-boundary uniqueness criterion; the positive-rates invariant law is not given by a static Gibbs specification. Pointer: `docs/entries/disagreement-percolation-gibbs-uniqueness.md`. |
| Dobrushin--Shlosman spatial-to-dynamical mixing | **N** | — | Requires a reversible Gibbs specification with uniform spatial mixing, neither available nor naturally defined for the target IPS. Pointer: `docs/entries/dobrushin-shlosman-spatial-to-dynamical.md`. |
| Spectral independence | **N** | — | Conditional Gibbs influence matrices and down-up Glauber geometry are not available for the unknown nonreversible invariant law. Pointer: `docs/entries/spectral-independence-local-to-global.md`. |
| Finite-size strong-mixing criterion | **C** | PR3 | The finite-scale-to-large-scale idea is relevant, but the checked theorem is reversible Gibbs/LSI; a nonreversible boundary-control analogue would itself be new. Pointer: `docs/entries/finite-size-strong-mixing-criterion.md`; positive-rates established-results §3. |
| Poincare / spectral gap | **C** | PR5 | A uniform coercive estimate could provide relaxation once an invariant reference is fixed, but it neither identifies nor uniquely selects the unknown invariant law in the present nonreversible problem. Pointer: `docs/entries/poincare-spectral-gap.md`; positive-rates final state / Meetings 025--030. |
| LSI / mLSI | **N** | — | Requires a known invariant law and usually reversibility/entropy production structure; it is strictly farther from the current uniqueness bottleneck than Poincare. Pointer: `docs/entries/log-sobolev-modified-log-sobolev.md`. |
| Discrete Bochner--Bakry--Emery | **N** | — | The reversible commuting-move entropy Hessian criterion has no identified reference law or move algebra for the residual IPS. Pointer: `docs/entries/bochner-bakry-emery-discrete-entropy.md`. |
| Entropic Ricci weak-interaction perturbation | **N** | — | Finite reversible weak-interaction curvature geometry does not attach to the unknown nonreversible invariant measure. Pointer: `docs/entries/entropic-ricci-weak-interaction-perturbation.md`. |
| Stochastic localization for Ising Glauber gaps | **N** | — | Uses a quadratic Ising Hamiltonian and reversible heat-bath Dirichlet form absent from the target. Pointer: `docs/entries/stochastic-localization-ising-glauber-gap.md`. |
| Dirichlet-form / canonical-path comparison | **C** | PR5 | A comparison to a tractable reference would be useful only with a common stationary law; no such reference is known, and generic reversible comparison was already a stopped direction. Pointer: `docs/entries/dirichlet-form-canonical-path-comparison.md`; positive-rates final state / Meetings 025--030. |
| Swendsen--Wang/FK kernel comparison | **N** | — | Depends on the Edwards--Sokal representation and reversible Potts/FK kernels, with no analogue for the target generator. Pointer: `docs/entries/swendsen-wang-heat-bath-kernel-comparison.md`. |
| Block dynamics and bisection variance | **C** | PR3 | The recursive scale-loss idea could inform a diameter recursion, but the checked argument is a reversible variance decomposition and does not supply the required cross-block stationary control. Pointer: `docs/entries/block-dynamics-bisection-variance.md`; positive-rates established-results §3. |
| Lu--Yau martingale recursion | **N** | — | Built around canonical conserved ensembles and equivalence of ensembles, absent here. Pointer: `docs/entries/lu-yau-martingale-conditional-variance.md`. |
| Two-scale conservative coarse graining | **N** | — | Requires conservative canonical measures, conditional LSIs and convexification; none match the target. Pointer: `docs/entries/two-scale-coarse-graining-conservative-lsi.md`. |
| Hierarchical renormalised gap recursion | **C** | PR3 | The idea of propagating a quantitative defect through changing effective measures is suggestive for `D_N`, but no compatible renormalisation of the occupation-control sets is known. Pointer: `docs/entries/hierarchical-renormalisation-spectral-gap-recursion.md`; positive-rates established-results §3. |
| Block/approximate entropy factorization | **N** | — | Needs a Gibbs law, conditional entropies and heat-bath entropy production. Pointer: `docs/entries/block-factorization-entropy.md`. |
| Holley--Stroock perturbation | **X** | PR1 | The stopped programme already found frozen reversible comparison insufficient; moreover a full-volume bounded perturbation would lose exponentially with volume. Pointer: `docs/entries/holley-stroock-bounded-perturbation.md`; positive-rates Meeting 030. |
| Moving-particle exclusion comparison | **N** | — | Uses conservative exchange algebra/effective resistance with no analogue for spin flips. Pointer: `docs/entries/moving-particle-long-jump-exclusion.md`. |
| Aldous interchange/exclusion gap | **N** | — | Exact interchange/exclusion spectral algebra is unrelated to the nonconservative binary spin generator. Pointer: `docs/entries/aldous-interchange-exclusion-gap.md`. |
| Liggett--Nash polynomial relaxation | **C** | PR4 | A nonlinear coercive inequality could turn a controlled signed/connected seminorm into slow decay, but the programme's natural positive raw seminorms fail and no stable replacement is known. Pointer: `docs/entries/liggett-nash-polynomial-relaxation.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Weak Poincare from Glauber influence | **C** | PR4 | It converts integrated single-spin coupling tails into relaxation, but the positive-rates programme has already reduced exactly such susceptibility/tail control to the unresolved escape/shift interfaces. Pointer: `docs/entries/weak-poincare-glauber-relaxation.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Super-Poincare reaction/diffusion decomposition | **N** | — | Particle-number/diffusion sector decomposition and reversible Dirichlet forms do not match the target. Pointer: `docs/entries/super-poincare-reaction-diffusion-particles.md`. |
| Large-set conductance / warm starts | **N** | — | Requires a finite reversible stationary flow and warm-start control; neither addresses uniqueness of the unknown infinite-volume invariant law. Pointer: `docs/entries/large-set-conductance-warm-start.md`. |
| KCLG renormalized Glauber comparison | **C** | PR5 | Its useful lesson is to manufacture a tractable auxiliary coarse process before comparison, but the actual theorem is reversible/conservative and gives no candidate auxiliary dynamics here. Pointer: `docs/entries/kclg-renormalized-glauber-comparison.md`; positive-rates final state / Meetings 025--030. |
| KCSM constraint domination | **N** | — | Pointwise Dirichlet-form domination needs a common reversible measure and constraint ordering, absent from the target rates. Pointer: `docs/entries/kcsm-constraint-domination-reference-process.md`. |
| Bootstrap closure to KCSM gap | **N** | — | Deterministic legal emptying/product equilibrium structure is specific to KCSM constraints. Pointer: `docs/entries/bootstrap-closure-kcsm-spectral-gap.md`. |
| Long-range good-path Poincare | **N** | — | Relies on product equilibrium, rare facilitating droplets and legal constrained moves, none present in the target. Pointer: `docs/entries/long-range-good-path-poincare-kcm.md`. |
| Nested super-good droplet renormalisation | **N** | — | The nested mobile-droplet geometry is KCM-specific and has no identified positive-rates proof object. Pointer: `docs/entries/nested-super-good-droplet-renormalisation.md`. |
| CBSEP auxiliary-process comparison | **C** | PR2 | A purpose-built auxiliary disagreement process could be useful if one can dominate the true disagreement cloud in the correct direction, but no such generator/comparison is presently known. Pointer: `docs/entries/cbsep-auxiliary-process-comparison.md`; positive-rates established-results §1. |
| Foster--Lyapunov plus Harris recurrence | **X** | PR2 | The live theorem needs a recurrent small set; infinite translation-invariant spin space supplies no obvious small set, and the programme already refuted the natural local scalar Foster class at a hard point. Pointer: `docs/entries/foster-lyapunov-harris-geometric-ergodicity.md`; positive-rates established-results §1. |
| Infinite-dimensional Harris--Lyapunov | **N** | — | Its compact regularisation/strong-Feller small set comes from smoothing Levy noise, unavailable for the lattice jump system. Pointer: `docs/entries/infinite-dimensional-harris-levy-spde.md`. |
| Particle-collapse regeneration | **N** | — | There is no finite-dimensional collapse atom for the infinite spin system. Pointer: `docs/entries/particle-collapse-regeneration.md`. |
| Physical-front regeneration | **B** | PR2 | The surviving disagreement can only be a moving leftward front; a genuine renewal decomposition with a uniform chance of terminal coupling per cycle would rule out convective survival. Pointer: `docs/entries/front-regeneration-renewal-times.md`; positive-rates established-results §1. |
| Competition-interface regeneration | **C** | PR2 | Approximate translated-interface restart is conceptually relevant, but it gives an interface limit law rather than extinction and the target disagreement front lacks a known localized two-phase structure. Pointer: `docs/entries/competition-interface-regeneration.md`; positive-rates established-results §1. |
| Survival-conditioned ancestor renewal | **C** | PR2 | Renewal under survival can organize the escaping front, but by itself it is compatible with survival; an additional contradiction/kill mechanism would still be needed. Pointer: `docs/entries/survival-conditioned-renewal-multitype-contact.md`; positive-rates established-results §1. |
| Essential hitting times / almost subadditivity | **C** | PR2 | Could quantify speed of disagreement escape under survival, but a deterministic negative speed is compatible with convective survival and does not prove extinction. Pointer: `docs/entries/essential-hitting-time-almost-subadditive-growth.md`; positive-rates established-results §1. |
| Finite-volume coercivity + exhaustion | **C** | PR4 | Time-coupled exhaustion is useful only after a boundary-uniform finite-volume relaxation estimate; obtaining that screening is essentially the unresolved shift/boundary problem. Pointer: `docs/entries/finite-volume-coercivity-exhaustion-uniqueness.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Graphical finite-speed transfer | **C** | PR4 | Finite propagation is already available in the programme and localizes the error, but the remaining growing-box relaxation/boundary term is exactly what is unresolved. Pointer: `docs/entries/finite-speed-finite-volume-transfer.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Tightness/compactness infinite dynamics | **N** | — | Constructs subsequential invariant/dynamical limits but does not prove uniqueness; existence is not the positive-rates bottleneck. Pointer: `docs/entries/tightness-compactness-infinite-particle-dynamics.md`. |
| Projective consistency of Gibbs marginals | **N** | — | Exact tree Gibbs consistency constructs laws but offers no uniqueness/convergence mechanism for this lattice IPS. Pointer: `docs/entries/projective-consistency-splitting-gibbs-equilibrium.md`. |
| Number rigidity + tail Dirichlet ergodicity | **N** | — | Requires a symmetric Dirichlet form, rigidity and a specified invariant point field, none available here. Pointer: `docs/entries/number-rigidity-tail-dirichlet-ergodicity.md`. |
| Relative-entropy-loss Gibbs attractor | **N** | — | Needs a known stationary Gibbs reference/specification and only attracts to its Gibbs simplex; the target invariant laws are not known to be Gibbs. Pointer: `docs/entries/relative-entropy-loss-gibbs-attractor.md`. |
| Asymptotic strong Feller support uniqueness | **N** | — | The product-space jump dynamics has no identified asymptotic smoothing/common-support mechanism analogous to degenerate SPDEs. Pointer: `docs/entries/asymptotic-strong-feller-support-uniqueness.md`. |
| Hörmander/Malliavin propagation | **N** | — | Malliavin covariance and parabolic dissipation are specific to continuous-noise SPDEs. Pointer: `docs/entries/hormander-malliavin-asf-semilinear-spde.md`. |
| Finite-ancestor duality + extinction | **C** | PR5 | The target has a finite signed graphical dual, so extinction-type estimates are relevant, but the programme's difficulty is signed branching/weights rather than an ordinary absorbing finite ancestor set. Pointer: `docs/entries/duality-extinction-finite-ancestor-process.md`; positive-rates final state / Meetings 025--030. |
| Successful coupling of finite dual particles | **C** | PR5 | Could suggest coupling signed dual states instead of bounding their size, but the live theorem uses fixed particle number and bounded positive harmonic transforms; the target dual changes size and carries signs. Pointer: `docs/entries/successful-coupling-finite-dual-particles.md`; positive-rates final state / Meetings 025--030. |
| Voter coalescing-walk duality | **N** | — | Single-parent coalescing ancestry is absent from general positive-rates spin updates. Pointer: `docs/entries/voter-coalescing-random-walk-duality.md`. |
| Parity branching-annihilating duality | **N** | — | Requires cancellative parity structure not present for arbitrary rate triples. Pointer: `docs/entries/parity-duality-branching-annihilating.md`. |
| Supercritical block construction | **N** | — | Its purpose is to prove and control survival of an active phase, whereas the target needs to eliminate surviving disagreement; the parity-dual setting is absent. Pointer: `docs/entries/supercritical-block-construction-complete-convergence.md`. |
| Two-level contact block/restart complete convergence | **C** | PR2 | Restartable blocks plus forward/backward intersection suggest a coarse coupling test, but the target lacks a monotone contact dual and survival blocks would not by themselves imply disagreement extinction. Pointer: `docs/entries/two-level-contact-block-restart-complete-convergence.md`; positive-rates established-results §1. |
| Toom error-graph expansion | **X** | PR2 | The method needs an eroding deterministic rule plus genuinely rare errors; at the hard near-East calibration leftward disagreement propagation is not a rare-error event, and absolute error weights discard the signed cancellation of PR1. Pointer: `docs/entries/toom-error-graph-expansion-pca.md`; positive-rates established-results §1. |
| Coupling from the past | **C** | PR5 | Positive rates give random maps, but global backward coalescence on the infinite lattice is stronger than needed and convective escape prevents the obvious grand-coupling certificate; local CFTP could still be a diagnostic. Pointer: `docs/entries/coupling-from-the-past.md`; positive-rates final state / Meetings 025--030. |
| Clan-of-ancestors perfect simulation | **C** | PR5 | Positive rates supply oblivious-noise components, so backward dependency clans are a concrete object; simple branching subcriticality is likely too strong near the hard point, but a finite-depth reproduction test is cheap. Pointer: `docs/entries/clan-of-ancestors-perfect-simulation.md`; positive-rates final state / Meetings 025--030. |
| Information percolation | **B** | PR5 | Unlike CFTP/clan extinction it allows histories to survive and only requires sparse initial-information clusters, potentially bypassing both common-coupling escape and signed connected-tail control. Pointer: `docs/entries/information-percolation-backward-histories.md`; positive-rates final state / Meetings 025--030. |
| East distinguished-zero screening | **C** | PR4 | One-sided orientation suggests distinguished reset paths that screen a left region, but without a product equilibrium the remaining conditional law is essentially the zero-boundary/shift object already unresolved. Pointer: `docs/entries/east-distinguished-zero-screening.md`; positive-rates established-results §§2,4 / Meetings 025--030. |
| Potential-theoretic capacity | **N** | — | Metastable reversible capacity estimates do not address global uniqueness/ergodicity of the nonreversible positive-rates system. Pointer: `docs/entries/potential-theoretic-capacity-metastability.md`. |

## Ranked A/B shortlist

_To be filled after the complete disposition table is fixed._

## Repackaging warnings and cheapest-first tests

_To be filled with the shortlist._
