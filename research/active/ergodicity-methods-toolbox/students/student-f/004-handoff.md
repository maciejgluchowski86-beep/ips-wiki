# Student F Assignment 004 handoff

Date: 2026-08-17

Assignment 004 is complete. Seven entries were committed individually. Five directly fill the assigned targets. Two targets were substituted under the assignment's explicit anti-padding rule after targeted searches failed to locate a clean primary interacting-process application in which the requested interface itself was load-bearing.

## Entries and commits

1. `entries/foster-lyapunov-harris-geometric-ergodicity.md`
   - commit `21c0339a984c64109527b50de3ee340fda3a7c64`
   - Foster--Lyapunov drift plus Harris small-set minorization; weighted-TV geometric ergodicity for an interacting stochastic bead-spring system.

2. `entries/particle-collapse-regeneration.md`
   - commit `3fbb61078dc37ca8759078321f296e7fb8dbb0db`
   - load-bearing regeneration at a literal recurrent atom in a synchronization particle system after centering; finite-mean cycles give positive recurrence and a unique stationary shape law.

3. `entries/weak-poincare-glauber-relaxation.md`
   - commit `6b85159677e2dbf35fa00462804815e0c6b65a69`
   - weak-Poincare/nonuniform coercivity obtained from single-spin disturbance tails for infinite-volume Glauber dynamics; includes low-temperature Ising phase relaxation.

4. `entries/number-rigidity-tail-dirichlet-ergodicity.md`
   - commit `e3f6bca1b3dc6b206bfa34ba0e012cc2824c57a8`
   - **substitution for spectral profile/evolving sets**: number rigidity + tail triviality + conditional local Dirichlet irreducibility imply global Dirichlet-form irreducibility and L2 semigroup ergodicity for infinite interacting point-process diffusions.

5. `entries/finite-volume-coercivity-exhaustion-uniqueness.md`
   - commit `af794b748a29b6faafb64e044306d49bd885acf5`
   - finite-volume LSI/Beckner coercivity plus finite-speed semigroup exhaustion; explicit time-volume coupling yields uniqueness of the infinite-volume tempered Gibbs law.

6. `entries/potential-theoretic-capacity-metastability.md`
   - commit `9a11bd677ab990c9ffc16a70c57177c13673ed6f`
   - **substitution for full Cheeger/conductance**: Dirichlet/flow variational capacity estimates as the main analytic interface for sharp metastable Glauber crossover times and exponential exit laws.

7. `entries/kcsm-constraint-domination-reference-process.md`
   - commit `8f20ccb78c09b2310a2a0e3c74ffc2bb7e168dbc`
   - KCSM constraint deletion/Dirichlet-form domination: FA-1f on a rooted graph dominates an oriented East reference process, giving a positive gap on finite and infinite bounded-degree connected graphs.

## Taxonomy and substitution decisions

### Target 2: regeneration versus Harris

No substitution was needed, but I did **not** create a generic Nummelin-splitting page. The inspected Baryshnikov--Stolyar source has an actual regeneration atom: when synchronization collapses all particles to one location, the centered state is deterministic; a uniform positive collapse probability on each fixed time interval gives finite-mean regeneration cycles. The renewal structure itself is used to prove positive recurrence, uniqueness of the centered stationary law, and steady-state speed. This is genuinely different from the Harris entry, where a small-set minorization is only one ingredient of a weighted contraction and no renewal-cycle decomposition is constructed.

A genuinely interacting-process application of *artificial* Nummelin splitting remains an uncovered literature item.

### Target 4 substitution: spectral profile/evolving sets

Targeted searches located clean spectral-profile/evolving-set theorems for general finite random walks, but the particle/exclusion sources found did not use that profile as their load-bearing IPS proof interface. I therefore did not manufacture an application by attaching generic finite-chain theory to an IPS example.

Replacement: Suzuki's number-rigidity/tail-triviality criterion is a distinct uncovered analytic architecture for infinite interacting diffusions. Theorem 4.3(ii) and Corollary 4.4 turn spatial rigidity and tail triviality, together with conditional local Dirichlet irreducibility, into global Dirichlet-form irreducibility and explicit L2 semigroup convergence. Section 6 verifies the hypotheses for sine_2, Airy_2, Bessel and Ginibre point fields, including the unlabelled infinite Dyson Brownian motion.

A genuine spectral-profile/evolving-set IPS application remains uncovered.

### Target 6 substitution: full Cheeger/conductance positive relaxation

The positive spin-system sources found during this search either implement canonical-path/flow congestion, which is already live, or use conductance to prove **slow-mixing lower bounds**. The existing live RFIM page already covers the distinct large-set-conductance/warm-start route. I did not find a clean primary spin-system theorem where a uniform full Cheeger lower bound itself is the distinct positive-gap/rapid-mixing engine.

Replacement: potential-theoretic capacity is a genuinely different variational interface for spin relaxation. In Bovier--den Hollander--Marello, Section 5.1 makes capacity and its Dirichlet/Berman--Konsowa variational representations the key analytic objects; sharp capacity and valley-mass estimates feed Theorems 1.1--1.2, which give sharp mean metastable crossover times and asymptotically exponential crossover laws for disordered Curie--Weiss Glauber dynamics. The entry deliberately targets `metastable-relaxation`, not global mixing or spectral gap.

A clean full-Cheeger positive-relaxation spin application remains uncovered.

## Source qualifications

- **Harris:** Mattingly--McKinley--Pillai Theorem 2.2 is the weighted-TV Harris criterion; Lemma 2.3 and Proposition 2.4 verify drift and minorization for the bead-spring process; Theorem 2.1 is the model conclusion.
- **Regeneration:** Baryshnikov--Stolyar Section 3 proves the centered process regenerative at full-particle collapse and establishes a uniform positive collapse probability on each fixed interval, hence finite-mean cycles and unique stationary law. No origin claim for regeneration/Nummelin is made.
- **Weak Poincare:** Völlering Theorem 3.1 is the single-spin-disturbance variance estimate; Proposition 4.8 gives the weak-Poincare form and nonexponential relaxation; Theorem 3.3 and Corollary 3.4 provide the attractive/low-temperature Ising application.
- **Number rigidity:** Suzuki Theorem 4.3(ii) and Corollary 4.4 are the global irreducibility/L2-ergodicity statements. The entry does not claim a positive gap or uniqueness beyond the selected symmetric Dirichlet-form invariant law.
- **Finite-to-infinite:** Zitt Theorem 2.2 is the uniqueness theorem. Decomposition (12) is the limiting interface: finite-volume approximation + finite-volume relaxation + Gibbs-limit term, with box size chosen proportional to time. The entry states the tempered/finite-range continuous-spin scope.
- **Capacity:** Bovier--den Hollander--Marello Theorems 1.1--1.2 are crossover-time conclusions; Section 5.1 equations (5.1), (5.3) and Sections 4--5 are the capacity/Dirichlet-form proof interface. The entry does not relabel metastability as rapid mixing.
- **KCSM domination:** Cancrini--Martinelli--Roberto--Toninelli Definition 3/Remark 7 give constraint domination; Theorem 6.1 and Lemma 6.2 implement the rooted-tree East comparison; Theorem 6.3 gives the infinite bounded-degree graph consequence.

## Further uncovered families

- a genuine spectral-profile or evolving-set theorem whose profile is load-bearing in an interacting-particle/spin application;
- a genuine full-Cheeger positive-gap/rapid-mixing spin application distinct from canonical paths and large-set conductance;
- Nummelin splitting/artificial-atom regeneration with a concrete interacting-process application;
- super-Poincare inequalities with an interacting-process application distinct from the weak-Poincare and Nash pages;
- Harris/Lyapunov criteria for genuinely infinite lattice IPS rather than finite-particle/interacting-diffusion systems;
- potential-theoretic capacity methods for infinite-volume IPS, beyond finite-volume metastable Glauber examples;
- coercive comparison with independent refresh dynamics for additional KCSM beyond the FA-1f/East constraint-domination entry.

No `docs/` or `mkdocs.yml` files were edited. Mechanical validation is left to the principal/orchestrator's normal post-commit run; this handoff does not claim a validator pass.
