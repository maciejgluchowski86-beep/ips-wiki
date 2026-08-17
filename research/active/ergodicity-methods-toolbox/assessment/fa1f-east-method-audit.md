# FA-1f / East toolbox applicability audit

Date: 2026-08-17

Status: **complete primary audit, Professor-owned lane after F008 became operationally unavailable**.

This audit follows `assessment-protocol.md` and `students/student-f/assignment-008.md`. All 74 frozen source-audited method pages were read. Ratings are: **A** actionable; **B** plausible architecture; **C** auxiliary/diagnostic; **X** blocked by a specific obstruction or hypothesis failure; **N** no credible contact.

Disposition count: **1 A, 4 B, 24 C, 21 X, 24 N**.

## Target and obstruction ledger

Main target: one-dimensional hard FA-1f started from a nontrivial Bernoulli product law, in the remaining all-density Bernoulli-quench regime. The chronology/sign record gives alternative sufficient interfaces:

1. `G_t(r) >= 0` for the positive finite-set dual;
2. shield positivity `S(t) >= 0`;
3. adjacent-vacancy repulsion `Cov(z_0(t),z_1(t)) <= 0`;
4. the endogenous-boundary three-site cross-product inequality
   `P(100)P(010) >= P(000)P(110)` and its reflection;
5. rooted punctured positivity `J_t(r) >= 0` in the last-ring Duhamel reduction.

A different architecture may prove local convergence directly. East is the solved benchmark: a distinguished vacancy screens the region behind it, after which the positive East gap gives relaxation. For FA the missing issue is the two-sided dependence of facilitation.

Hard negative evidence used throughout:

- coefficientwise positivity is stronger than needed and false;
- the isolated-insertion cone is not generator closed because adjacent updates create cluster-extension gradients of uncontrolled sign;
- replacing endogenous exterior facilitation by independent/deterministic signals removes the actual difficulty;
- the centered positive `h`-transform and complete `h`-weighted patch transfer are conservative reformulations;
- the finite-seed patch/dual programme collapses to the same conservative coefficient dynamics;
- FA-1f already has positive equilibrium spectral gap for every `q>0`; proving that gap again is not a quench solution;
- an equilibrium gap or entropy inequality alone does not control the globally singular product start `mu_{q0}` versus `mu_q` in infinite volume;
- any criterion forcing convergence from every initial state is incompatible with the all-ones absorbing configuration.

Primary obstruction pointers: `agent/fa1f-chronology-sign-route:docs/entries/chronology-averaged-sign-route-for-fa-1f.md`; `research/fa1f-finite-seed:research/active/fa1f-finite-seed/state.md` and `proof-spine.md`; live `east-distinguished-zero-screening.md`.

## Complete disposition table

| # | Method | Rating | Target interface and ruling |
|---|---|---|---|
| 1 | Attractive monotone coupling | X | FA is not attractive in the natural occupancy order. Pointer: `attractive-monotone-coupling-extremal-laws.md`. |
| 2 | Dobrushin influence contraction | X | Worst-case contraction is incompatible with the hard trap; a screened state space would first have to be built. Pointer: `dobrushin-influence-contraction.md`. |
| 3 | Path coupling | X | Strict full-state-space contraction would imply worst-case mixing despite the absorbing trap. Pointer: `path-coupling-glauber-dynamics.md`. |
| 4 | Coupling with stationarity/local uniformity | C | Useful endpoint principle once one has a high-probability screened coupling, but the checked theorem still controls arbitrary second states. Removing that requirement leaves the screen itself as the real theorem. Pointer: `coupling-with-stationarity-local-uniformity.md`. |
| 5 | Joint block resampling coupling | X | Requires ordered/distributive block conditionals and legal block resampling; neither is available for hard FA. Pointer: `block-coupling-joint-resampling.md`. |
| 6 | Coupling independence | X | Gibbs conditional-law sensitivity does not control kinetic legality; FA equilibrium conditionals are already product. Pointer: `coupling-independence-coarse-grained-comparison.md`. |
| 7 | Weighted Wasserstein contraction | X | Requires order/dissipativity absent in non-attractive hard FA and would conflict with the trap. Pointer: `weighted-wasserstein-contraction-infinite-ips.md`. |
| 8 | Maximal local nonmonotone coupling | C | A useful local coupling primitive, but no FA aggregate geometry controls accumulated discrepancies. Pointer: `maximal-local-coupling-nonmonotone-potts.md`. |
| 9 | Sticky McKean--Vlasov coupling | N | Diffusive mean-field distance process has no FA analogue. Pointer: `sticky-coupling-mckean-vlasov.md`. |
| 10 | Componentwise reflection mean-field coupling | N | Reflection Brownian coupling and mean-field averaging do not contact FA. Pointer: `componentwise-reflection-uniform-mean-field.md`. |
| 11 | Asymptotic coupling for SPDEs | N | Absolutely continuous noise shifts/determining modes have no discrete hard-constraint analogue. Pointer: `asymptotic-coupling-infinite-dimensional-spde.md`. |
| 12 | Asymptotic reflection coupling | N | Hilbert-space reflection plus monotone coercivity has no FA interface. Pointer: `asymptotic-reflection-coupling-monotone-spde.md`. |
| 13 | Refined non-diagonal discrepancy coupling | **B** | Treating paired transition rates as variables suggests coupling *different* microscopic updates, precisely the freedom needed for the chronology-switching cross-product target where a fixed replica swap fails. Pointer: `refined-discrepancy-coupling-general-exclusion.md`; chronology (12e)--(12f). |
| 14 | Second-class-particle shock coupling | C | Moving-marker idea is relevant mainly to finite-seed fronts; no exact FA shock family closes. Pointer: `second-class-particle-shock-random-walk.md`. |
| 15 | Environment seen from a second-class particle | C | Moving-frame stationarity is a useful front template, especially finite seed, but no FA marked-frame closure is known. Pointer: `environment-seen-second-class-particle.md`. |
| 16 | Censoring inequalities | X | Requires monotonicity absent in FA. Pointer: `censoring-monotone-glauber-dynamics.md`. |
| 17 | Dynamical disagreement percolation | **B** | A law-dependent/renormalized disagreement-connectivity bound could prove local forgetting without worst-case contraction. Pointer: `dynamical-disagreement-space-time-percolation.md`. |
| 18 | Gray one-dimensional edge coalescence | X | Requires attractive/repulsive dynamics and strictly positive rates; hard FA has blocked zero rates and neither order structure. Pointer: `one-dimensional-edge-coalescence-positive-rates.md`. |
| 19 | Static disagreement percolation | N | Product Gibbs uniqueness solves the wrong object; kinetic memory remains. Pointer: `disagreement-percolation-gibbs-uniqueness.md`. |
| 20 | Dobrushin--Shlosman spatial-to-dynamical | X | Ordinary Gibbs Glauber theorem explicitly does not supply hard-KCSM coercivity. Pointer: `dobrushin-shlosman-spatial-to-dynamical.md`. |
| 21 | Spectral independence | X | Product equilibrium has trivial static influences while the kinetic constraint remains untouched. Pointer: `spectral-independence-local-to-global.md`. |
| 22 | Finite-size strong-mixing bootstrap | X | Source requires unconstrained Glauber-type coercivity; hard constraints need new inputs. Pointer: `finite-size-strong-mixing-criterion.md`. |
| 23 | Poincare/spectral gap | C | Already known positive for FA at every `q>0`; useful only after a spatial screen is obtained. Pointer: `poincare-spectral-gap.md`. |
| 24 | LSI/mLSI | C | Could accelerate finite-window relaxation, but does not by itself handle an infinite-volume singular start. Pointer: `log-sobolev-modified-log-sobolev.md`. |
| 25 | Discrete Bochner entropy method | C | Potential finite-volume mLSI engine; zero kinetic rates are difficult and no screen is supplied. Pointer: `bochner-bakry-emery-discrete-entropy.md`. |
| 26 | Entropic Ricci perturbation | X | Positive weak-interaction rate criterion is incompatible with genuine zero FA rates; finite-volume entropy would still leave the singular start. Pointer: `entropic-ricci-weak-interaction-perturbation.md`. |
| 27 | Stochastic localization | N | Ising interaction-matrix localization does not address a kinetic constraint with product equilibrium. Pointer: `stochastic-localization-ising-glauber-gap.md`. |
| 28 | Canonical-path/Dirichlet comparison | C | Can prove constrained finite-volume coercivity, already available more directly for FA; no quench bridge. Pointer: `dirichlet-form-canonical-path-comparison.md`. |
| 29 | Swendsen--Wang/FK kernel comparison | N | No Edwards--Sokal auxiliary representation is available for FA kinetics. Pointer: `swendsen-wang-heat-bath-kernel-comparison.md`. |
| 30 | Block dynamics/bisection | C | Source already proves positive FA gap for every `q>0`; downstream of screening only. Pointer: `block-dynamics-bisection-variance.md`, Theorem 6.3 application. |
| 31 | Lu--Yau martingale recursion | N | Canonical conserved-sector recursion has no FA conserved variable. Pointer: `lu-yau-martingale-conditional-variance.md`. |
| 32 | Two-scale conservative coarse graining | N | Conservative continuous-spin architecture has no FA target object. Pointer: `two-scale-coarse-graining-conservative-lsi.md`. |
| 33 | Hierarchical Brascamp--Lieb recursion | N | Effective Gibbs-potential flow addresses equilibrium gap, not kinetic access from a singular start. Pointer: `hierarchical-renormalisation-spectral-gap-recursion.md`. |
| 34 | Block entropy factorization | X | Checked reduction uses ordinary heat-bath entropy production; constrained IPS require redesign, which is the missing kinetic content. Pointer: `block-factorization-entropy.md`. |
| 35 | Holley--Stroock perturbation | X | FA changes legal transitions, not the invariant product density; hard constraints are outside bounded-density perturbation transfer. Pointer: `holley-stroock-bounded-perturbation.md`. |
| 36 | Moving-particle/effective resistance | N | Exclusion exchange algebra has no FA analogue. Pointer: `moving-particle-long-jump-exclusion.md`. |
| 37 | Aldous interchange gap | N | Fixed-particle symmetric exclusion structure absent. Pointer: `aldous-interchange-exclusion-gap.md`. |
| 38 | Liggett--Nash inequality | N | FA already has positive equilibrium gap; no conserved diffusive slow mode needs Nash replacement. Pointer: `liggett-nash-polynomial-relaxation.md`. |
| 39 | Weak Poincare from influence tails | C | Single-spin disturbance tail is a useful memory diagnostic, but conclusion is equilibrium relaxation weaker than the known FA gap. Pointer: `weak-poincare-glauber-relaxation.md`. |
| 40 | Super-Poincare reaction/diffusion | N | Particle-number/spatial-diffusion decomposition does not match FA. Pointer: `super-poincare-reaction-diffusion-particles.md`. |
| 41 | Large-set conductance/warm starts | C | Bernoulli `q0` on a length-`L` box has warmness exponential in `L`; with `L~t` from finite speed, polynomial warm-start relaxation cannot close the quench. Pointer: `large-set-conductance-warm-start.md`. |
| 42 | KCLG renormalized Glauber comparison | C | Good-block auxiliary dynamics is useful coercive design, but 1D FA already has mobile single vacancies; missing issue is memory erasure. Pointer: `kclg-renormalized-glauber-comparison.md`. |
| 43 | KCSM constraint domination by East | C | Directly proves FA gap from East but explicitly not East's nonequilibrium screening. Pointer: `kcsm-constraint-domination-reference-process.md`. |
| 44 | Bootstrap closure to KCSM gap | C | FA internal spanning already proves positive gap; legal paths do not imply exterior-memory erasure. Pointer: `bootstrap-closure-kcsm-spectral-gap.md`. |
| 45 | Long-range good-path Poincare | C | Locates/transports mobile defects for equilibrium coercivity; in FA a single vacancy is already mobile. Pointer: `long-range-good-path-poincare-kcm.md`. |
| 46 | Nested super-good droplets | C | Preserving one mobile core across scales is useful front intuition, mainly finite seed, but output is restricted-chain gap. Pointer: `nested-super-good-droplet-renormalisation.md`. |
| 47 | CBSEP/g-CBSEP comparison | C | Strong finite-volume FA-specific comparison, but finite-volume relaxation on an `O(t)` box does not by itself control the singular quench. Pointer: `cbsep-auxiliary-process-comparison.md`. |
| 48 | Foster--Lyapunov/Harris | X | Uniform small-set recurrence is incompatible with the hard trap absent a prior screened reduction. Pointer: `foster-lyapunov-harris-geometric-ergodicity.md`. |
| 49 | Infinite-dimensional Harris | N | Compact regularization/strong-Feller mechanism absent. Pointer: `infinite-dimensional-harris-levy-spde.md`. |
| 50 | Particle-collapse atom | N | Literal infinite-system renewal atom is unavailable; generic 'find an atom' gives no FA bridge. Pointer: `particle-collapse-regeneration.md`. |
| 51 | Front regeneration/renewal | **B** | Fresh-start times that prevent old information from re-entering a moving front match the spatial mechanism explicitly missing from the closed FA finite-seed programme; a two-sided local version can screen a quench observation window. Pointer: `front-regeneration-renewal-times.md`; finite-seed `proof-spine.md`. |
| 52 | Competition-interface regeneration | C | Approximate restart of a localized interface is relevant supporting machinery but FA quench has no canonical single interface. Pointer: `competition-interface-regeneration.md`. |
| 53 | Survival-conditioned renewal | C | Fresh graphical future is instructive, but FA has no survival-conditioned ancestor process furnishing such renewal points. Pointer: `survival-conditioned-renewal-multitype-contact.md`. |
| 54 | Essential hitting times | C | Could quantify front growth after a persistent vacancy-front object is built; does not itself erase memory. Pointer: `essential-hitting-time-almost-subadditive-growth.md`. |
| 55 | Finite-volume coercivity + exhaustion | C | Correct limiting decomposition, but a box `n~t` incurs exponential product-density cost that a black-box low-q gap cannot uniformly beat. Pointer: `finite-volume-coercivity-exhaustion-uniqueness.md`. |
| 56 | Finite-speed finite-volume transfer | C | Essential downstream localization infrastructure; checked theorem is equilibrium relaxation and does not solve the singular start. Pointer: `finite-speed-finite-volume-transfer.md`. |
| 57 | Tightness/compactness path limits | N | Infinite FA dynamics/equilibrium already exist; subsequential construction does not select the quench limit. Pointer: `tightness-compactness-infinite-particle-dynamics.md`. |
| 58 | Projective consistency | N | Constructs an equilibrium law rather than attraction; FA product equilibrium is already explicit. Pointer: `projective-consistency-splitting-gibbs-equilibrium.md`. |
| 59 | Number rigidity/tail Dirichlet ergodicity | N | Number-rigid configuration-space diffusion structure absent, and `L2(mu_q)` ergodicity is weaker than the target. Pointer: `number-rigidity-tail-dirichlet-ergodicity.md`. |
| 60 | Relative-entropy-loss Gibbs attractor | X | Theorem 2.6 requires irreducibility R6. Hard FA violates R6 at all ones, which cannot create a first vacancy. Pointer: `relative-entropy-loss-gibbs-attractor.md`; Jahnel--Koppl assumptions R1--R6 and Remark 2.7. |
| 61 | Asymptotic strong Feller uniqueness | X | `mu_q` has full support while `delta_1` is another invariant law, so the needed support-separation property cannot hold on full FA state space. Pointer: `asymptotic-strong-feller-support-uniqueness.md`. |
| 62 | Hörmander--Malliavin ASF verification | N | No differentiable/Malliavin/bracket structure. Pointer: `hormander-malliavin-asf-semilinear-spde.md`. |
| 63 | Finite-ancestor duality + extinction | X | Actual FA centered dual/weighted transfer from the closed programme does not supply an empty absorbing dual and is conservative. Pointer: `duality-extinction-finite-ancestor-process.md`; finite-seed obstruction record. |
| 64 | Successful coupling of fixed-size duals | X | Actual FA dual changes set size; fixed-particle-sector hypothesis fails and the weighted transfer is already conservative. Pointer: `successful-coupling-finite-dual-particles.md`. |
| 65 | Voter coalescing-walk duality | N | FA histories are not single-parent coalescing walks. Pointer: `voter-coalescing-random-walk-duality.md`. |
| 66 | Parity duality | N | FA is not cancellative/parity dual. Pointer: `parity-duality-branching-annihilating.md`. |
| 67 | Supercritical block construction | C | Propagating vacancy-rich blocks proves activity, not local forgetting; restart/screening must be added. Pointer: `supercritical-block-construction-complete-convergence.md`. |
| 68 | Two-level block-and-restart | C | Complete convergence uses monotone contact survival plus compatible dual intersection, absent for FA's known dual. Pointer: `two-level-contact-block-restart-complete-convergence.md`. |
| 69 | Toom error graphs | N | Low-noise eroding PCA structure and small error parameter absent. Pointer: `toom-error-graph-expansion-pca.md`. |
| 70 | Coupling from the past | X | Global backward coalescence is impossible in the presence of the all-ones closed class; monotone simplification also fails. Pointer: `coupling-from-the-past.md`. |
| 71 | Clan-of-ancestors perfect simulation | X | Full-state-space finite dependency clans would select a unique past-independent local law, incompatible with the blocked stationary history. Pointer: `clan-of-ancestors-perfect-simulation.md`. |
| 72 | Information percolation/backward histories | **B** | Law-dependent adaptive histories may carry initial information only on rare clusters; unlike CFTP, not every history must die. This can be formulated under the Bernoulli quench and need not contradict the trap. Pointer: `information-percolation-backward-histories.md`. |
| 73 | East distinguished-zero screening | **A** | Closest solved architecture. FA already has the downstream positive gap; a two-sided approximate regeneration screen is the single missing bridge. Pointer: `east-distinguished-zero-screening.md`; row 43; chronology (12d)--(12f). |
| 74 | Potential-theoretic capacity | N | Quench is not metastable escape; all ones is absorbing rather than a rare valley with positive escape capacity. Pointer: `potential-theoretic-capacity-metastability.md`. |

## Ranked A/B shortlist

### 1. East distinguished-zero screening — A

**Bridge lemma: two-sided sublinear-width regeneration screen.** Fix `q,q0 in (0,1)` and a finite observation interval `Lambda`. There should exist random times `tau_t <= t-s_t`, random intervals `I_t=[L_t,R_t]` containing `Lambda`, and screen events `E_t` such that

- `s_t -> infinity` and `|I_t|=o(s_t)` on `E_t`;
- `P_{mu_{q0}}(E_t^c)->0`;
- on `E_t`, during `[tau_t,t]` the evolution relevant to `Lambda` is causally insulated from the exterior of `I_t` by genuine FA vacancy histories, so conditional on the screen data it can be represented by an FA process on `I_t` with legal vacancy boundary conditions using fresh interior marks.

No exact conditional equilibrium at time `tau_t` is required. Any law on `I_t` has an `L2(mu_q^{I_t})` density cost at most `exp(C_q|I_t|)`. The uniform positive finite-volume FA gap `gamma(q)>0` therefore gives schematically

`|mu_{q0} P_t f - mu_q(f)| <= 2||f||_infty P(E_t^c) + C_f exp(C_q|I_t|-gamma(q)s_t)`, 

which tends to zero.

**Implication chain.** Screen lemma -> finite screened interval with long remaining time -> known FA gap/constraint-domination -> local convergence for every Bernoulli `q0>0`.

**Exact obstruction avoided.** It does not require coefficient contraction, exact East one-sided independence, or worst-case mixing. The screen is built from the actual endogenous two-sided FA graphical history.

**Cheapest falsification test.** Any proposed marker rule should first be enumerated on 5--7 sites. Check whether changing the exterior while keeping the proposed screen data fixed can alter a legal interior update or the future marker law. The naive one-vacancy East transplant fails this test because the marker's future can depend on both sides. Only a paired/renewal/corridor rule with leakage probability tending to zero should receive further work.

**Finite-seed note.** Even more promising there: a genuine left/right vacancy front exists, so the same regeneration construction need not be manufactured from a translation-invariant sea of vacancies.

### 2. Refined non-diagonal discrepancy coupling — B

**Bridge lemma: measure-preserving chronology switch.** For every `t`, construct an injective measure-preserving transformation on pairs of independent FA initial configurations and graphical histories which maps

`{replica 1 ends with 000, replica 2 ends with 110}`

into

`{replica 1 ends with 100, replica 2 ends with 010}`,

for the three sites `(-1,0,1)`, and construct the reflected transformation as well. The map may pair different microscopic updates in the two replicas; it must preserve each marginal graphical law and legality of every reconstructed update.

Then

`P(100)P(010) >= P(000)P(110)`

and its reflection. By the chronology record, these are exactly the endogenous-boundary inequalities needed on the first-exit face of the two-site cone `u,v>=q`, `Delta<=0`. Hence adjacent vacancy covariance stays nonpositive, the vacancy density cannot cross below `q`, and every stationary limit-point mixture `lambda mu_q+(1-lambda)delta_1` must have `lambda=1`.

**Implication chain.** Chronology switch -> cross-product inequalities -> adjacent repulsion -> `rho_t>=q` -> exclusion of trap weight -> Bernoulli equilibrium convergence.

**Exact obstruction avoided.** It targets the weakest known three-site inequality, not false coefficientwise positivity or full negative association. It directly addresses the known failure of a fixed vertical replica swap at two-sided updates.

**Cheapest falsification test.** Two tests. First, for any proposed switch rule, enumerate the first two-sided update encountered by the swap interface and verify legality/marginal preservation exactly. Second, finite-cycle numerical CTMC tests can search for a counterexample to the target inequality before constructing the map. The Professor ran the latter on periodic cycles of sizes 5--8 for 80 random parameter choices with `q in (0.01,0.49)`, `q0 in [2q,0.999]` when nonempty, and 14 times from `0.005` to `20`; no violation was found. The smallest observed cross-product margin was about `4.86e-10`, with adjacent covariance still negative. This is numerical evidence only.

**Finite-seed note.** This route is specific to translation-invariant Bernoulli marginals and is less naturally adapted to a single-vacancy start.

### 3. Information percolation/backward histories — B

**Bridge lemma: law-dependent extinction of initial-information histories.** Build an adaptive backward reveal of the minimal information needed to determine `eta_t|Lambda` from the FA graphical marks. Legal refresh randomness may terminate a branch once enough neighboring vacancy information has been revealed; blocked updates retain the earlier spin and continue the branch. For every Bernoulli `q0>0`, prove that the conditional influence of the time-zero red history tends to zero, for example

`E[ || Law(eta_t|Lambda | marks above time 0) - Law(eta_t|Lambda | same marks, time-zero spins resampled from mu_q) ||_TV ] -> 0`.

A stronger sufficient form is that the minimal determining support at time zero is empty with probability tending to one under the Bernoulli-quench graphical law.

**Implication chain.** Vanishing red-history influence -> local law independent of quench time-zero spins -> compare with stationary Bernoulli start under the same graphical construction -> local convergence.

**Exact obstruction avoided.** The history is state-adaptive and law-dependent, unlike the positive finite-set transformed dual whose complete weighted transfer is conservative. It need not work for the all-ones initial state.

**Cheapest falsification test.** The naive independent-branching bound is already too weak: revealing one neighbor first gives expected dependency count of order `1+p+p^2>1` at a ring under a product background (`p=1-q`). Thus a simple subcritical Galton--Watson domination is dead in the hard regime. Any serious attempt must exploit adaptive short-circuiting, mergers, repeated refreshes, or block-scale history geometry. A small-block exact history enumeration should test whether those effects can push the effective reproduction below one.

**Finite-seed note.** Less natural than front regeneration for a single seed, because the initial information is highly concentrated rather than a product field.

### 4. Front regeneration/renewal — B

**Bridge lemma: two-sided vacancy-front renewal.** Starting from a Bernoulli quench and a fixed observation interval, construct left and right vacancy-front candidate times and failure times analogous to the front-regeneration source. With probability tending to one, before time `t-s_t` obtain successful renewal fronts bracketing the observation interval such that old graphical information outside the two fronts cannot re-enter the bracket during the remaining interval of length `s_t->infinity`; the bracket width should be `o(s_t)` or otherwise admit a compatible finite-volume mixing estimate.

**Implication chain.** Successful two-front renewal -> fresh screened local future -> finite-volume FA gap -> convergence.

**Exact obstruction avoided.** The construction explicitly allows failed attempts and conditions on a successful separation event; it does not demand the exact one-sided conditional independence that fails for a single FA vacancy.

**Cheapest falsification test.** Specify the simplest candidate vacancy-front rule and enumerate whether an old exterior dependency can cross behind it through a two-sided legal update. If re-entry occurs with probability one or the failure time has no plausible tail, discard the rule before proving renewal estimates. The finite-seed geometry is the natural first testbed.

**Finite-seed note.** This is probably the most promising toolbox architecture for the finite-seed problem itself, because the physical vacancy front is already distinguished.

### 5. State-dependent dynamical disagreement percolation — B

**Bridge lemma: subcritical good-block disagreement transmission.** Couple an FA process from `mu_{q0}` to a stationary `mu_q` process using a coupling allowed to depend on the local joint state. Find finite block scales `L,T` and a good-block event generated by the actual vacancy environment such that, conditional on a disagreement entering a good block, the probability that it exits through any future neighboring block is small enough for the coarse disagreement process to be dominated by a subcritical finite-range oriented percolation; bad-block probability under the two product laws must be absorbed in the same subcritical comparison.

Then the probability of a disagreement path from time zero to `Lambda x {t}` tends to zero.

**Implication chain.** Block transmission estimate -> subcritical disagreement connectivity -> coupling agreement on every fixed local set -> Bernoulli-quench convergence.

**Exact obstruction avoided.** This is not worst-case disagreement domination, which the trap rules out. Subcriticality is required only in the state-dependent product-law environment, and the coupling can use non-diagonal local moves.

**Cheapest falsification test.** On small blocks, solve or simulate the exact coupled generator from a single incoming disagreement under product backgrounds and estimate the expected number/probability of outgoing disagreements. If no `L,T` window shows a subcritical trend as `q` decreases, the route should be demoted before a renormalization proof is attempted.

**Finite-seed note.** Potentially useful, but front regeneration has a more natural geometric object for a single vacancy.

## Methods deliberately not shortlisted

The most important negative synthesis is that **equilibrium coercivity is not the missing mathematics**. Rows 23--47 include several strong FA/KCSM spectral-gap, block, bootstrap, East-comparison and CBSEP results, and the FA gap is already positive for every vacancy density. These methods become useful immediately *after* a screen/regeneration lemma but do not create one.

Likewise, global uniqueness/minorization tools (Harris, CFTP, ASF, entropy-attractor with R6) fail for structural reasons tied to the all-ones closed class. The relative-entropy attractor theorem is especially worth recording as an anti-loop result: its irreducibility hypothesis R6 fails exactly at the hard FA trap.

The closed positive-dual/patch programme is also respected: no duality page is shortlisted unless it changes the proof object. The only shortlisted algebraic route, row 13, acts directly on pairs of *physical graphical histories* to target the three-site cross-product inequality.

## Finite-seed ranking note

For the separate single-vacancy finite-seed problem, the ordering changes. Front regeneration (row 51) and East-style screening (row 73) become the dominant pair, with moving-frame defect methods (rows 14--15), essential hitting times (54), and nested mobile-core geometry (46) as useful supporting templates. The chronology-switching cross-product route is substantially less natural there because it exploits translation-invariant Bernoulli marginals.

## Primary-audit conclusion

The toolbox does not expose an existing theorem that already solves the all-density FA-1f Bernoulli quench. It does, however, narrow the plausible new mathematics sharply. The best routes all concern **local loss of exterior/initial information**, not stronger equilibrium relaxation:

1. build a two-sided FA replacement for East's distinguished-vacancy screen;
2. prove the exact three-site chronology inequality by a non-diagonal measure-preserving switch;
3. control state-adaptive backward information histories;
4. construct two-sided vacancy-front renewal times;
5. renormalize actual disagreement transmission under the product-law environment.

These five candidates should be the only FA-1f/East methods sent to hostile cross-review. No sixth candidate is added to fill the quota.
