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

## Shortlist and bridge lemmas

Not yet frozen. Provisional survivor from rows 1--10: coupling with stationarity/local uniformity. It will remain B only if a mathematically precise Bernoulli-start finite-window bridge can be stated without assuming away the all-ones trap.

## Finite-seed note

No row in this first batch is yet promoted specifically for the finite-seed problem. Any coupling method that requires a positive-density typical initial environment is, if anything, less adapted to the single-vacancy start.
