# FA-1f / East toolbox applicability audit

Date: 2026-08-17

Status: **in progress, Professor-owned lane after F008 became operationally unavailable**.

This audit follows `assessment-protocol.md` and `students/student-f/assignment-008.md`. The frozen inventory has 74 source-audited methods. Ratings are: A actionable; B plausible architecture; C auxiliary/diagnostic; X blocked by a specific obstruction or hypothesis failure; N no credible contact.

## Target and obstruction ledger

Main target: one-dimensional hard FA-1f started from a nontrivial Bernoulli product law, in the remaining all-density Bernoulli-quench regime. The chronology/sign record gives alternative sufficient interfaces:

1. `G_t(r) >= 0` for the positive finite-set dual;
2. shield positivity `S(t) >= 0`;
3. adjacent-vacancy repulsion `Cov(z_0(t),z_1(t)) <= 0`;
4. the endogenous-boundary three-site cross-product inequality
   `P(100)P(010) >= P(000)P(110)` and its reflection;
5. rooted punctured positivity `J_t(r) >= 0` in the last-ring Duhamel reduction.

A separate architecture may instead prove convergence directly. East's distinguished-zero lemma is the solved benchmark: a moving vacancy screens the region behind it because strict orientation makes the future of the distinguished vacancy independent of that region. The missing FA analogue must overcome the two-sided dependence of facilitation.

Hard negative evidence:

- coefficientwise positivity is stronger than needed and false;
- the isolated-insertion cone is not generator-closed because adjacent updates create cluster-extension gradients of uncontrolled sign;
- exogenizing the exterior facilitating signals removes the actual difficulty and is invalid;
- the centered positive `h`-transform and complete `h`-weighted patch transfer are conservative reformulations;
- the finite-seed patch/dual programme collapses to the same conservative coefficient dynamics;
- an equilibrium spectral gap alone does not solve the Bernoulli quench: the infinite product initial law at density `q_0 != q` is singular relative to equilibrium, and a finite-volume passage must control the volume growth of the initial density/entropy;
- any criterion that would force convergence from every initial state is incompatible with the all-ones absorbing configuration.

Pointers: `agent/fa1f-chronology-sign-route:docs/entries/chronology-averaged-sign-route-for-fa-1f.md`; `research/fa1f-finite-seed:research/active/fa1f-finite-seed/state.md` and `proof-spine.md`; live `east-distinguished-zero-screening.md`.

## Complete disposition table

The table is committed in batches while the audit proceeds. Rows already present have been read against their live method page.

| # | Method | Rating | Target interface and ruling |
|---|---|---|---|
| 1 | Attractive monotone coupling and extremal laws | X | FA-1f is not attractive in the natural occupancy order: the facilitation indicator decreases when neighboring occupancies increase, so the `0 -> 1` rate has the wrong monotonicity. The source criterion therefore does not apply. Pointer: `attractive-monotone-coupling-extremal-laws.md`, attractiveness inequalities and limitations. |
| 2 | Dobrushin influence contraction | X | Worst-case single-site influence contraction is incompatible with the hard constraint/all-ones trap in the form needed for global mixing. A screened restricted state space could change this, but constructing that screen would be the new theorem, not an application of the Dobrushin page. Pointer: `dobrushin-influence-contraction.md`, worst-case influence criterion and hard-constraint limitation. |
| 3 | Path coupling | X | The page requires a strictly contractive path metric for the finite chain and then gives worst-case mixing. Hard FA-1f with the absorbing all-ones state cannot satisfy such a criterion on the full state space. A restriction to a vacancy-containing screened region is a different architecture. Pointer: `path-coupling-glauber-dynamics.md`, criterion/limitations. |
| 4 | Coupling with stationarity and local uniformity | B | **Candidate direct-convergence interface.** The useful relaxation is that contraction need hold only when the stationary copy is in a high-probability good set. The checked theorem still couples against arbitrary second states, which FA cannot satisfy because of the trap; the possible FA adaptation is to replace worst-case second-state control by a high-probability statement under the Bernoulli-quench law on a growing screened window. This survives provisionally because it attacks the singular-start issue rather than coefficient positivity. Pointer: `coupling-with-stationarity-local-uniformity.md`, Theorem 1.2 interface; chronology target ledger. Bridge lemma to be stated in the shortlist section if retained. |
| 5 | Block coupling by joint block resampling | X | The checked theorem uses an ordered/distributive-lattice block conditional law and comparison back to local moves. FA-1f lacks the required monotone order, and an artificial unconstrained block refresh would not be a legal FA transition. Pointer: `block-coupling-joint-resampling.md`, criterion/limitations. |
| 6 | Coupling independence / coarse-grained Glauber comparison | X | The method is a Gibbs conditional-law coupling theorem for ordinary single-site Glauber relaxation. FA's obstacle is kinetic legality and a singular nonequilibrium start, not high-degree Gibbs conditional sensitivity. The pinned-law hypotheses do not furnish a bridge to any sign or screening target. Pointer: `coupling-independence-coarse-grained-comparison.md`. |
| 7 | Weighted Wasserstein contraction for infinite IPS | X | The theorem requires an order-preserving positive-cone coupling plus a uniform dissipative drift margin. FA-1f is a discrete non-attractive hard-constrained process with an absorbing trap, so the criterion cannot hold on the relevant state space. Pointer: `weighted-wasserstein-contraction-infinite-ips.md`, Theorems 1.1-1.2 interface. |
| 8 | Maximal local coupling for nonmonotone Potts dynamics | C | Maximal coupling of the two legal one-site refresh laws is available in principle, but the source's load-bearing step is an aggregate geometry controlling how local TV discrepancies accumulate. In FA the unresolved issue is exactly the two-sided endogenous constraint history; no low-dimensional aggregate parameter is supplied. Useful only as a diagnostic coupling primitive for a later screened construction. Pointer: `maximal-local-coupling-nonmonotone-potts.md`. |
| 9 | Sticky McKean-Vlasov coupling | N | The sticky scalar-distance reduction depends on nondegenerate diffusion, dissipative drift and weak mean-field interaction. No corresponding object contacts the FA sign, covariance, or spatial-screening targets. Pointer: `sticky-coupling-mckean-vlasov.md`. |
| 10 | Particle-uniform componentwise reflection | N | This is a weakly interacting mean-field diffusion argument using reflected Brownian noises and a Poisson-designed radial cost. Its hypotheses and proof object have no credible FA analogue. Pointer: `componentwise-reflection-uniform-mean-field.md`. |
| 11 | Asymptotic coupling for SPDEs | N | The architecture relies on admissible absolutely-continuous changes of driving noise, determining modes and dissipativity. FA's Harris graphical randomness does not provide an analogous continuously shiftable noise, and no bridge to the sign/screening targets emerges. Pointer: `asymptotic-coupling-infinite-dimensional-spde.md`. |
| 12 | Asymptotic reflection coupling for monotone SPDEs | N | The load-bearing mechanism is regularized reflection of additive Hilbert-space noise plus monotone-operator coercivity. This has no credible discrete hard-constraint analogue for FA. Pointer: `asymptotic-reflection-coupling-monotone-spde.md`. |
| 13 | Refined non-diagonal discrepancy coupling | B | **Candidate endogenous-boundary interface.** The exclusion theorem itself does not apply, but its reusable move is to treat paired transition rates as variables and couple *different* microscopic moves rather than insist on the same graphical arrow. The chronology record's cross-product target already identifies the precise failure of a fixed two-replica swap at two-sided updates and asks for a measure-preserving permutation of update marks. A non-diagonal two-history coupling is therefore a concrete architecture for the three-site inequality, not merely generic coupling language. Pointer: `refined-discrepancy-coupling-general-exclusion.md`; chronology equations (12e)-(12f). Bridge lemma to be stated if retained. |
| 14 | Second-class-particle shock coupling | C | Exact closure of a one-marker shock family is unavailable for FA and the process is nonconservative. The transferable idea is to retain a moving defect/interface rather than force global coupling. That is mainly diagnostic for a vacancy-front construction, especially finite seed. Pointer: `second-class-particle-shock-random-walk.md`. |
| 15 | Environment seen from a second-class particle | C | Moving to a defect frame can reveal a stationary ergodic environment even when the marker persists. FA has no known marked-frame closure or stationary law around a chosen vacancy/front. This is a useful template for a future front theorem, but not a current Bernoulli-quench bridge. It is materially more relevant to the finite-seed front problem. Pointer: `environment-seen-second-class-particle.md`; finite-seed `proof-spine.md` unresolved spatial mechanism. |
| 16 | Censoring inequalities | X | The theorem requires a monotone spin system and an ordered initial density; FA is not attractive. Censoring therefore cannot be imported to validate a convenient update schedule. Pointer: `censoring-monotone-glauber-dynamics.md`, hypotheses/limitations. |
| 17 | Dynamical disagreement percolation | B | **Candidate direct spatial-forgetting interface.** A worst-case subcritical domination cannot hold because of the absorbing trap, but the method explicitly permits multiscale/nonuniform connectivity bounds. A viable FA adaptation would bound the probability that a disagreement path from a Bernoulli-quench/stationary coupling reaches a fixed observation block after using the actual state-dependent vacancy environment, rather than a worst-case open mark. Such a bound would directly give local convergence and sits outside the conservative coefficient-transfer obstruction. Pointer: `dynamical-disagreement-space-time-percolation.md`, discrepancy-connectivity criterion and limitation that naive domination may percolate. Bridge lemma to be stated if retained. |
| 18 | Gray one-dimensional edge coalescence | X | Gray's theorem requires attractive or repulsive nearest-neighbour dynamics and strictly positive flip rates. Hard FA has zero rates on blocked sites and is neither attractive nor the repulsive transform covered there. The ordered-edge/local-positive-rate repair cannot be transplanted as stated. The edge idea remains conceptual background for front methods, but the theorem hypotheses fail. Pointer: `one-dimensional-edge-coalescence-positive-rates.md`. |

## Shortlist and bridge lemmas

Not yet frozen. Provisional B candidates after rows 1--18:

- coupling with stationarity/local uniformity;
- refined non-diagonal discrepancy coupling, aimed specifically at the endogenous three-site cross-product inequality;
- dynamical disagreement percolation, only in a state-dependent/renormalized form that does not claim worst-case subcriticality.

## Finite-seed note

The moving-marker pages (second-class shock and environment seen from a second-class particle) are materially more promising for the single-vacancy finite-seed problem than for the translation-invariant Bernoulli quench, because the finite-seed geometry supplies a genuine propagating vacancy/front marker. They remain C here because no FA marked-frame closure or regeneration law is currently known.
