# Student G Assignment 004 handoff

## Status

Assignment 004 is complete. The repository assignment contains seven target slots. Seven source-checked entries were staged under `research/active/ergodicity-methods-toolbox/entries/`, one substantive entry per commit. Six retain the assigned proof interface. The boundary-uniform projective graphical-transfer target did not survive source inspection as a distinct method and was replaced by asymptotic coupling for infinite-dimensional stochastic dynamics.

No file under `docs/` and no `mkdocs.yml` file was edited.

## Entries and commits

1. `successful-coupling-finite-dual-particles.md` — `8d7c05de70d0662c84e1607c4b2e38a47710bc84`.
2. `second-class-particle-shock-random-walk.md` — `18fd31eb1346cf2877a95a83e9bad06d7d999b13`.
3. `maximal-local-coupling-nonmonotone-potts.md` — `6e573aae573780a50a6d68ce3caf49e1905225bf`.
4. `competition-interface-regeneration.md` — `49929e1277d0de4cffe4910b5d1c804cfeac7fce`.
5. `two-level-contact-block-restart-complete-convergence.md` — `9b355734b2ea378a9e0f746694cdcc0715e086a2`.
6. `asymptotic-coupling-infinite-dimensional-spde.md` — `7d2609fda66fa44087a5453f34ef2036087c20e4` — substitution for the boundary-uniform projective graphical-transfer slot.
7. `asymptotic-reflection-coupling-monotone-spde.md` — `722229bce8037336a4f8cccd65da62eec626e28d`.

## Taxonomy decisions

### Successful coupling of finite duals is not extinction, voter coalescence, or parity growth

Redig--van Wiechen couple two dual systems with the **same fixed particle number** until their full configurations agree. Invariance makes the dual transform harmonic; successful coupling then forces that transform to be constant on each finite-particle sector. Primal ergodicity supplies multiplicativity and hence product-measure classification. No dual particles need disappear, no ancestral lineages merge, and no parity observable is used.

### A second-class particle can be the retained discrepancy rather than an error to eliminate

Balázs--Farkas--Kovács--Rákos exhibit product shock measures for which the coupled pair differs by one second-class particle and the translated shock family closes under the generator. The marker itself becomes an autonomous nearest-neighbour random walk. Its drift is the microscopic shock velocity. This is distinct from the live discrepancy-nonincreasing coupling page: here the discrepancy is deliberately preserved because its stochastic motion is the load-bearing interface variable.

### Maximal local Potts coupling is distinct from path coupling and block resampling

For the multi-component Curie--Weiss--Potts Glauber chain, scalar monotone Ising coupling is unavailable. Mun couples the two conditional one-site Gibbs laws maximally, so the local mismatch probability is exactly their total-variation distance. Direct worst-case adjacent-pair contraction is still insufficient; an aggregate-path argument controls the accumulated local discrepancies and yields `O(N log N)` mixing. No block is jointly resampled and the decisive local coupling is optimized probabilistically rather than order-preserving.

### Competition-interface regeneration is not physical-front regeneration

Mountford--Valesin regenerate the **boundary between two competing contact-process types**. At restart times, a fresh translated Heaviside process is coupled to the original future interface, with a controlled interface-position error. Iteration gives approximately fresh increments and a functional CLT. Neither competing phase is erased, so this is not the exact fresh-wake mechanism of the live reactive physical-front page.

### Contact-type complete convergence uses block restart plus forward/dual intersection

Ma's two-level contact process first obtains restartable occupied blocks that dominate supercritical oriented percolation. For complete convergence the argument then constructs a backward flea dual in the stationary host graphical environment; conditional on forward and backward survival, their coarse paths meet around the midpoint. This is distinct from the live Sturm--Swart ADBARW page, where the coarse survival construction is combined with parity-preserving branching-annihilating duality.

### Boundary-uniform projective graphical transfer: negative taxonomy result and substitution

I did **not** create a `boundary-uniform-projective-graphical-transfer` entry. The primary sources found with finite-volume estimates uniform over boundary conditions fell into proof interfaces already live:

- static disagreement or Dobrushin-type boundary screening, where the boundary-uniform coupling is itself the already represented spatial-uniqueness mechanism; or
- analytic finite-volume coercivity/semigroup exhaustion, where the limiting step is not a new graphical coupling interface.

I did not find a clean primary theorem in which a genuinely new, boundary-uniform **dynamic graphical coupling** is the load-bearing projective limit from finite boxes to infinite-volume uniqueness/convergence. Repeating this generic search without a new named source is unlikely to add coverage.

The replacement is `asymptotic-coupling-infinite-dimensional-spde.md`. Hairer's method is a distinct coupling interface: exact finite-time meeting is abandoned. A feedback modification of the noise makes determining modes approach exponentially while an absolute-continuity estimate controls the changed noise law; Lyapunov returns allow repeated binding attempts. Theorem 4.1 and Corollary 4.3 yield exponential bounded-Lipschitz/Wasserstein mixing and uniqueness for infinite-dimensional stochastic dynamics.

### Reflection coupling remains separate from Hairer asymptotic binding

Wang's nonlinear monotone-SPDE construction addresses a different obstruction. The formal infinite-dimensional reflection coefficient involving `Q^{-1}(X-Y)` is not well posed for Hilbert--Schmidt noise. Section 3 regularizes the inverse covariance and cuts off the reflection near the diagonal, producing a sequence of approximate reflection couplings. Coupling-time estimates give gradient/Hölder bounds and Theorem 2.2 gives exponential convergence/strong ergodicity in autonomous dissipative regimes.

The two new infinite-dimensional pages should not be merged merely because both use the phrase “asymptotic coupling.” Hairer uses **feedback/noise-shift binding plus absolute continuity** and does not require finite-time coalescence. Wang uses **regularized reflection of an additive noise component** and derives semigroup bounds from approximate reflection coupling times.

## Source qualifications

### Successful finite-dual coupling

Primary checked source: Frank Redig and Hidde van Wiechen, *Ergodic Theory of Multi-layer Interacting Particle Systems*, Journal of Statistical Physics 190 (2023), Article 88, DOI `10.1007/s10955-023-03099-2`. Checked pinpoints: Section 3.2, Theorems 3.1--3.2, Section 4 and Theorem 4.1. The classification is for the paper's tempered/ergodic class and respects conserved particle-density parameters; it is not a claim of one global invariant law across densities.

### Second-class shock coupling

Primary checked source: Márton Balázs, György Farkas, Péter Kovács and Attila Rákos, *Random walk of second class particles in product shock measures*, Journal of Statistical Physics 139 (2010), 252--279, DOI `10.1007/s10955-010-9933-8`, arXiv `0909.3071`. Checked pinpoints: Section 3.1, Theorem 3.1 and Remark 3.2. The entry states exact shock-family closure and shock motion; it does not promote this to global ergodicity of the conservative IPS.

### Maximal local Potts coupling

Primary checked source: Kyunghoo Mun, *Dynamical Phase Transition for the homogeneous multi-component Curie-Weiss-Potts model*, Journal of Statistical Physics 193 (2026), Article 16, DOI `10.1007/s10955-026-03571-9`. Checked pinpoints: Theorem 1; Section 3.1, Lemmas 3.2--3.3; Section 3.2, Lemmas 3.6, 3.7 and 3.10. The application is finite-volume mean-field Potts dynamics; the entry does not claim that maximal local coupling automatically beats Dobrushin bounds in spatial models.

### Competition-interface regeneration

Primary checked source: Thomas Mountford and Daniel Valesin, *Functional Central Limit Theorem for the Interface of the Symmetric Multitype Contact Process*, ALEA 13 (2016), 481--519, DOI `10.30757/ALEA.v13-20`, arXiv `1509.04339`. Checked pinpoints: Theorem 1.2; Sections 2.3--2.4, especially Theorem 2.11; Section 3. The conclusion is a long-time law for the interface, not mixing of the whole infinite configuration.

### Two-level contact block/restart complete convergence

Primary checked source: Ruibo Ma, *Complete convergence theorem for a two-level contact process*, ALEA 19 (2022), 943--976, DOI `10.30757/ALEA.v19-37`, arXiv `1904.08401`. Checked pinpoints: Theorem 2; Theorem 3.5 and Proposition 3.6; Section 4, especially Section 4.1. A supercritical block comparison alone is not presented as complete convergence; the forward/backward meeting argument is retained as a separate load-bearing step.

### Asymptotic binding coupling

Primary checked source: Martin Hairer, *Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling*, Probability Theory and Related Fields 124 (2002), 345--380, DOI `10.1007/s004400200216`, arXiv `math/0109115`. Checked pinpoints: Section 2.3; assumptions A1--A5 in Section 3; Theorem 4.1 and Corollary 4.3; Sections 5--6. The entry labels this as an adjacent infinite-dimensional interacting Markov/SPDE method rather than a lattice spin-system theorem.

### Asymptotic reflection coupling

Primary checked source: Feng-Yu Wang, *Asymptotic Couplings by Reflection and Applications for Non-Linear Monotone SPDEs*, Nonlinear Analysis 117 (2015), 55--66, DOI `10.1016/j.na.2015.01.012`, arXiv `1407.3522`. Checked pinpoints: Theorems 2.1--2.3; Section 3, especially equation (3.2) and Proposition 3.1; Section 6. “Monotone” here is the variational monotone-operator hypothesis for the SPDE, not attractiveness/order-preserving coupling.

## Negative searches that should not be repeated generically

- **Generic boundary-uniform projective graphical transfer:** current search did not expose a distinct dynamic graphical limiting theorem. Boundary-uniform sources located were already Dobrushin/disagreement screening or analytic coercivity/exhaustion. Reopen only with a concrete named source or a clearly different limiting object.
- **Generic common/basic graphical coupling:** the prior G003 negative result remains unchanged; nothing in this wave produced a separate proof interface.
- **Treating every reflection/Wasserstein paper as one method:** Hairer binding, Wang asymptotic reflection, and the live synchronous weighted-`W_1` contraction have different coupling objects and should remain separate.

## Further uncovered graphical/coupling families

The search suggests several possible later interfaces, subject to the same source gate:

- **sticky coupling** for interacting McKean--Vlasov or kinetic systems, where the distance process has a sticky state at zero and yields perturbation-stable Wasserstein/TV estimates;
- **successful coupling for finite duals with internal labels or nonconserved dual size**, if the coupling step rather than extinction/parity remains decisive;
- **shock/second-class-particle coupling beyond exact product shocks**, for example invariant laws of the environment viewed from the second-class particle or shock measures with several discrepancies;
- **restart/essential-hitting complete convergence** for multitype contact processes where no backward self-duality is available and the restart architecture itself replaces dual intersection;
- **interface regeneration for disagreement fronts** arising directly from a coupling of two copies, rather than a physical or species-competition interface;
- **reflection-plus-synchronous or sticky Wasserstein coupling** for weakly interacting particle systems with estimates uniform in particle number, distinct from both infinite-dimensional SPDE reflection and purely synchronous drift contraction;
- a genuinely **boundary-uniform dynamic projective coupling** remains uncovered if a source can be found whose finite-box-to-infinite-volume passage is not merely an instance of the live spatial-screening or coercivity-transfer pages.

## Mechanical validation

All seven entries were written against the current staging template and committed separately. `validate_entries.py` remains the principal/orchestrator's structural check; this handoff does not treat validator success as mathematical or source verification.
