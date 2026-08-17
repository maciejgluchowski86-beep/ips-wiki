# Group meeting 010: wave four source audit; fourteen-entry integration gate opens

Date: 2026-08-17

Professor review of Student F Assignment 004 and handoff `55d5e44`, Student G Assignment 003 and handoff `753f4eb`, all fourteen staged entries, and the primary-source locations carrying their main claims. The principal reports `Checked 44 entries; 0 failed mechanical validation`; as always this is structural only.

`state_narrowed: yes`.

## 1. Audit corrections before acceptance

Four scope/pinpoint corrections were made before the wave was accepted.

1. `weak-poincare-glauber-relaxation.md`: Völlering's checked numbering is Theorem 3.2 for the attractive autocorrelation reduction, Corollary 3.3 for the low-temperature Ising application, and Proposition 4.7 for the weak-Poincare inequality. The staged entry and handoff had these as Theorem 3.3, Corollary 3.4, and Proposition 4.8. Corrected at `fa48b2c`. The mathematical mechanism was unchanged.
2. `refined-discrepancy-coupling-general-exclusion.md`: `targets: uniqueness` was too coarse for a theorem classifying extremal translation-invariant invariant laws across conserved densities. The target is now `invariant-law-classification`, at `44e36ac`. The body already had the correct restriction.
3. `number-rigidity-tail-dirichlet-ergodicity.md`: moved from the generic `functional-inequality` staging category to `other` at `d7865e0`. Its proof interface is zero-energy/Dirichlet-form irreducibility plus tail structure, not a quantitative functional inequality.
4. `potential-theoretic-capacity-metastability.md`: likewise moved to `other` at `6ce981f`. Capacity/potential theory is variational but is not itself a Poincare/LSI-type functional-inequality method. The page remains explicitly scoped to metastable crossover, not global mixing.

A fifth metadata tightening was made at `1f9f115`: parity duality now targets `invariant-law-classification` and `convergence`, rather than a bare `uniqueness` label. Sturm--Swart prove uniqueness within the homogeneous coexisting class; the absorbing constant laws remain invariant.

These corrections are exactly why `validate_entries.py` is not a mathematical/source validator.

## 2. Student F Assignment 004

All seven entries are accepted after the corrections above.

### Foster--Lyapunov plus Harris geometric ergodicity

Accepted. Mattingly--McKinley--Pillai's Harris theorem combines a Lyapunov drift with a small-set/minorization condition to give weighted-total-variation contraction, a unique invariant law, and geometric convergence. Their interacting bead--spring/Stokes system supplies a genuine interacting-process application. This remains distinct from exact renewal regeneration.

### Regeneration at a recurrent particle-collapse atom

Accepted. Baryshnikov--Stolyar explicitly identify the centered finite-particle process as regenerative when all particles collapse to one location; a uniform positive collapse probability on each fixed time interval gives finite mean cycles, positive recurrence, and a unique stationary centered law. No artificial splitting is inserted, so a genuine Nummelin-splitting IPS application remains uncovered.

### Weak Poincare from nonuniform Glauber influence

Accepted after the pinpoint correction. Völlering converts time tails of a one-spin discrepancy into scale-dependent variance inequalities and then a weak-Poincare estimate; for attractive systems the input reduces to a one-spin autocorrelation and yields low-temperature Ising phase relaxation. This is distinct from Liggett--Nash interpolation and from large-set conductance.

### Number rigidity plus tail triviality and Dirichlet irreducibility

Accepted as F's substitution for spectral profile/evolving sets. Suzuki proves that, under the paper's local conditional irreducibility/closability and quasi-regularity hypotheses, number rigidity plus tail triviality yields global Dirichlet-form irreducibility and hence L2 semigroup ergodicity. The determinantal point-process examples make this a genuine infinite interacting-particle method. A true spectral-profile/evolving-set IPS entry remains uncovered.

### Finite-volume coercivity plus exhaustion

Accepted. Zitt's Theorem 2.2 allows either finite-volume log-Sobolev constants growing at the controlled `n/log n` rate or uniform generalized Beckner inequalities above the stated exponent threshold. The proof explicitly couples box size to time and decomposes the infinite semigroup into finite/infinite approximation, finite-box relaxation, and Gibbs-limit terms. It therefore deserves a dedicated finite-to-infinite analytic-transfer entry, separate from G's graphical finite-speed transfer below.

### Potential-theoretic capacity for metastable spin relaxation

Accepted as an adjacent relaxation tool, with a scope warning. Bovier--den Hollander--Marello use Dirichlet and flow variational principles for capacity to obtain sharp metastable crossover times and an exponential exit law for disordered Curie--Weiss Glauber dynamics. This belongs in the toolbox because the programme explicitly includes closely related spin-system relaxation architectures, but it must sit in a metastability/potential-theory subsection and must not be presented as proving global ergodicity, rapid mixing, or a positive gap. A clean full-Cheeger positive-relaxation spin application remains uncovered.

### KCSM constraint domination by a slower reference process

Accepted. Cancrini--Martinelli--Roberto--Toninelli delete legal FA-1f moves until a tractable oriented East process on a rooted spanning tree remains. Pointwise constraint domination orders the Dirichlet forms, and Theorems 6.1 and 6.3 transfer the one-dimensional East gap to finite rooted graphs and then arbitrary infinite connected bounded-degree graphs. This is strictly simpler than canonical-path routing and distinct from the live Kob--Andersen renormalized auxiliary-process construction.

## 3. Student G Assignment 003

All seven entries are accepted after the target-scope tightening above.

### Block coupling by joint block resampling

Accepted. Felsner--Heldt--Roch--Winkler introduce a genuine whole-block conditional resampling chain and control a block-divergence quantity under a monotone coupling before using path coupling and comparison to return to the local chain. The load-bearing estimate is at block-law level, so this is not a duplicate of ordinary one-site path coupling or Hayes--Vigoda equilibrium-typicality.

### Supercritical block construction and complete convergence

Accepted. Sturm--Swart coarse-grain the branching-annihilating interface process into good space-time blocks and dominate from below by supercritical oriented percolation. Together with duality/growth information this yields complete convergence for the rebellious voter model. The direction of percolation comparison is opposite to the live subcritical disagreement-percolation method.

### Front regeneration and renewal times

Accepted. Jara--Moreno--Ramírez construct regeneration times at a moving reactive front, prove the conditional restart statement for every regeneration and iid post-first increments, and use renewal theory to prove convergence of the process seen from the front to its unique nontrivial invariant law. This is distinct from East's distinguished vacancy and from F's literal collapse atom.

### Weighted Wasserstein contraction for an infinite particle system

Accepted. Bezborodov--Di Persio--Friesen--Kuchling use a weighted l1 state space, common-noise monotone coupling, and a dissipative effective-drift inequality to get exponential W1 contraction and a unique invariant law for countable-site continuous-spin systems. This supplies the infinite-dimensional transportation-metric interface missing from finite Hamming/path coupling.

### Finite-speed transfer from finite-volume relaxation

Accepted. Cancrini--Martinelli--Roberto--Toninelli couple a local infinite-volume observable to a growing finite-volume Kob--Andersen process, bound the restriction error by finite speed, and balance it against finite-volume coercivity with box size proportional to time. This is the graphical/causal version of finite-to-infinite transfer; it remains separate from Zitt's analytic LSI/Beckner exhaustion architecture.

### Refined discrepancy coupling beyond basic exclusion coupling

Accepted after the target metadata correction. Gobron--Saada prove that basic coupling is not the right attractive coupling for general configuration-dependent exclusion rates. They explicitly design non-diagonal coupled transitions, obtain a discrepancy-nonincreasing attractive coupling, and under connectivity/no-blocking hypotheses classify extremal translation-invariant invariant measures. This is a legitimate substitution for the conditional generic-basic-coupling slot because it identifies a new coupling design interface exactly where ordinary basic coupling fails.

G's decision **not** to create a generic common-clock/basic-coupling page is endorsed. The searched material did not separate such a page from existing attractiveness, path coupling, and dynamical disagreement propagation; forcing it would have been padding.

### Parity duality with branching-annihilating particles

Accepted with the restricted target metadata. Sturm--Swart's finite dual survives, branches and annihilates while preserving parity; loss of primal information comes from unbounded spatially distributed dual growth and asymptotic parity randomization, not extinction or mere coalescence. The resulting theorem classifies the homogeneous coexisting invariant law and proves convergence under the stated survival/nonstability hypotheses.

## 4. Wave-four taxonomy and remaining gaps

The fourteen accepted entries open four areas that were thin in the first thirty: recurrence/regeneration, qualitative Dirichlet-form ergodicity, finite-to-infinite transfer, and metastable/potential-theoretic relaxation. They also broaden coupling/duality beyond one-site contraction.

Still-uncovered interfaces include genuine spectral-profile/evolving-set IPS use; a full-Cheeger positive-gap/rapid-mixing spin theorem distinct from canonical paths and large-set conductance; artificial Nummelin splitting in a concrete interacting process; super-Poincare beyond the present weak-Poincare/Nash examples; projective/compactness invariant-law arguments; additional infinite-lattice Harris/Lyapunov methods; and genuinely distinct model-specific mechanisms as later source searches expose them.

## 5. Integration gate

There are now **44 staged entries**, all source-audited and accepted after the corrections above. The first thirty are already live; the newest fourteen remain staged.

Both students are idle and the branch is quiet. Open a single bounded live-integration pass for these fourteen entries. Preserve their staged slugs, add `status: literature` and `audit: current`, remove staging-only front matter, integrate them into the existing hub by proof interface, and update the existing top-level MkDocs section. Do not touch unrelated legacy pages.

After that batch closes, require the same structural checks used for the previous integrations: staging validator, strict MkDocs build, staged-versus-promoted completeness, hub link resolution and coverage, current-audit metadata, legacy safety, and nav-target resolution.

Current status:

- 44 staged entries source-audited and accepted;
- 30 currently live;
- 14 cleared for immediate live integration;
- Student F idle;
- Student G idle;
- no new literature assignment until the 14-page integration is mechanically checked.
