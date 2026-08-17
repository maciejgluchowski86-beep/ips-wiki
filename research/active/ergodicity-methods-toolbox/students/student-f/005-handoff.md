# Student F Assignment 005 handoff

Date: 2026-08-17

Assignment 005 is complete under the principal's six-target dispatch. Six entries were committed individually. Five directly fill assigned targets. The artificial-Nummelin target was substituted under the anti-padding rule after a second targeted search failed to locate a clean interacting-process application in which an artificially manufactured atom and the resulting renewal decomposition are themselves load-bearing.

## Entries and commits

1. `entries/bootstrap-closure-kcsm-spectral-gap.md`
   - commit `0ef9e53afed4706115cddf41d5e20b074c8b82c1`
   - deterministic bootstrap internal spanning/legal emptying -> good coarse constraint -> microscopic constrained Poincare -> positive KCSM spectral gap.

2. `entries/long-range-good-path-poincare-kcm.md`
   - commit `da03348176d6d7b5ec64b2fbbbda48a9d60dd62f`
   - likely long-range exterior/good-path constraints replace rare local droplets; constrained Poincare plus explicit droplet transport gives KCM coercivity.

3. `entries/nested-super-good-droplet-renormalisation.md`
   - commit `10f8b2b398cd38b0114a77553e1605b571119578`
   - nested super-good rectangles/mobile droplets and matched scale-by-scale inverse-gap inequalities; a Matryoshka-type relaxation recursion distinct from generic block bisection.

4. `entries/cbsep-auxiliary-process-comparison.md`
   - commit `8ecc4d1f810c992183e73bad380fdd71327e058c`
   - CBSEP/g-CBSEP is a purpose-built branching/coalescing exclusion auxiliary dynamics with its own relaxation theory; Dirichlet comparison transfers it to FA-1f and mesoscopic FA-2f droplet motion.

5. `entries/super-poincare-reaction-diffusion-particles.md`
   - commit `1e637b2dc078da69f9f5835e0b602abca0d2ad85`
   - **substitution for artificial Nummelin splitting**: super-Poincare/log-Sobolev decomposition for reaction-diffusion particle systems into particle-number and within-sector diffusion coercivity.

6. `entries/tightness-compactness-infinite-particle-dynamics.md`
   - commit `10eb2f1163e8f1af42cedfe26c7063c7e84d54fa`
   - uniform Ruelle bounds -> path-law tightness -> accumulation-point martingale problem -> compactness/identification of invariant Gibbs laws in the N/V limit.

## Source qualifications and exact pinpoints

### Bootstrap closure / legal paths

Primary: Cancrini--Martinelli--Roberto--Toninelli, *Kinetically constrained spin models*, PTRF 140 (2008), 459--504, DOI `10.1007/s00440-007-0072-3`.

- Definition 3.4: internal spanning is explicitly a legal KCSM path to the empty configuration.
- Theorem 3.3: one sufficiently probable good-block event at a finite scale implies positive infinite-volume spectral gap.
- Corollary 3.5: internal-spanning probability tending to one plus finite-block ergodicity implies positive gap.
- Theorems 6.3 and 6.7: FA-1f and FA-jf/Modified-Basic applications.

The page isolates the deterministic-bootstrap -> stochastic-coercivity transfer, not the model-specific small-q asymptotics.

### Long-range constrained Poincare / good paths

Primary: Martinelli--Toninelli, *Towards a universality picture for the relaxation to equilibrium of kinetically constrained models*, Ann. Probab. 47 (2019), 324--361, DOI `10.1214/18-AOP1262`.

- Theorem 2 and Lemma 2.5: exterior/long-range constrained Poincare inequality from a weighted failure-probability condition and martingale decomposition.
- Definition 3.1: good and super-good paths.
- Theorem 3.2 and Proposition 3.4: high-probability super-good-path constraint gives the coarse variance inequality.
- Corollary 3.9: converts path transport/congestion estimates to a robust KCM Poincare bound.

This is distinct from block bisection: the load-bearing move is to replace a rare local facilitator by a likely nonlocal path event and pay transport cost.

### Nested super-good-droplet renormalisation

Primary: Hartarsky--Martinelli--Toninelli, *Sharp threshold for the FA-2f kinetically constrained model*, PTRF 185 (2023), 993--1037, DOI `10.1007/s00440-022-01169-2`.

- Definitions 4.2--4.3: nested rectangles and recursively defined super-good events.
- Remark 4.4: irreducibility of the FA-2f dynamics restricted to a super-good rectangle.
- Proposition 4.7: inverse-gap bound propagated through the nested hierarchy.
- Lemmas 4.9--4.10: the two consecutive scale-extension inequalities whose iteration proves Proposition 4.7.

The entry uses “Matryoshka-type” only as taxonomy/expository language. The primary paper itself formulates the mechanism as recursively nested super-good rectangles and mobile droplets.

### CBSEP / generalized CBSEP

Primary: Hartarsky--Martinelli--Toninelli, *Coalescing and branching simple symmetric exclusion process*, Ann. Appl. Probab. 32 (2022), 2841--2859, DOI `10.1214/21-AAP1750`.

- equation (3): two-sided Dirichlet-form comparison between CBSEP and FA-1f.
- Corollaries 3.1--3.2: CBSEP relaxation/log-Sobolev estimates and their FA-1f transfer.
- Theorem 2: generalized-CBSEP mixing bounded by ordinary CBSEP plus random-walk cover time.
- Section 5: graphical proof of the generalized-CBSEP comparison.

Application: Hartarsky--Martinelli--Toninelli, *Sharp threshold for the FA-2f kinetically constrained model*, Proposition 5.2 and Section 5.3: generalized CBSEP on coarse super-good droplet states is the mesoscopic Poincare engine, then its edge updates are implemented by legal FA-2f paths.

### Artificial Nummelin negative result and substitution

A second targeted search again found clean Nummelin/artificial-atom theory only in general Harris-chain or statistics/diffusion settings, not a concrete interacting-particle/spin/infinite-dimensional application in which the artificial splitting and renewal cycles themselves establish the ergodic conclusion. In particular, generic Nummelin-chain constructions and continuous-time splitting used for statistical regeneration do not satisfy the assignment's interacting-process requirement. The existing live `particle-collapse-regeneration` page already covers a genuine physical recurrent atom, so relabeling that as Nummelin would duplicate rather than broaden the toolbox.

Substitution primary: Röckner--Wang, *Functional Inequalities for Particle Systems on Polish Spaces*, Potential Analysis 24 (2006), 223--243, DOI `10.1007/s11118-005-0913-6`.

- Corollary 4.4: under positive diffusion-sector gap, the full reaction-diffusion form satisfies a super-Poincare inequality iff both the one-particle diffusion form and particle-number Q-process satisfy their component super-Poincare inequalities.
- Theorem 4.2: analogous stronger functional-inequality decomposition used for logarithmic Sobolev.
- Example 5.2: finite-range Gibbs interacting diffusion on a compact manifold; component log-Sobolev estimates combine to yield the full particle-system LSI.

This is distinct from the live weak-Poincare and Liggett--Nash pages: it is a strong smoothing/tensor-decomposition interface, not a route to slow relaxation from defective coercivity.

A genuine artificial-Nummelin interacting-process application remains uncovered and should not be re-searched generically unless new primary evidence appears.

### Tightness / compactness infinite-particle limit

Primary: Conrad--Grothaus, *N/V-limit for Langevin dynamics in continuum*, Rev. Math. Phys. 23 (2011), 1--51, DOI `10.1142/S0129055X11004229`.

- Theorem 4.13: tightness of the finite-N stationary Langevin path laws on the continuous marked-configuration path space when `N_n/(2 lambda_n)^d -> rho` under the stated Ruelle-type potential assumptions.
- Theorem 4.17: every accumulation point solves the infinite-particle Langevin martingale problem.
- Theorem 5.1: finite-volume canonical Gibbs measures are relatively compact in the tame-local-observable topology and every accumulation point is a grand-canonical Gibbs measure.

This page is law-level compactness, not the already-live semigroup exhaustion argument. It constructs an infinite-particle equilibrium dynamics from subsequential weak limits. It deliberately does **not** claim uniqueness of the limiting martingale problem, convergence of the whole approximation sequence, or ergodicity from arbitrary initial conditions.

## Taxonomy decisions

- Targets 1--4 survive as four separate KCM interfaces. Although some appear in the same modern KCM proofs, their load-bearing objects differ: deterministic legal closure; likely long-range path constraints; recursively nested mobile-droplet events; and an independently analysable auxiliary particle dynamics.
- Target 5 does not currently warrant an artificial-Nummelin entry. The substitution is declared rather than treating generic splitting theory as an interacting-process application.
- Target 6 is distinct from finite-speed/coercive exhaustion because compactness of probability laws and identification of accumulation points is the main mechanism.

## Further uncovered families / negative searches worth preserving

- artificial Nummelin splitting/manufactured atom with a genuine interacting-process application remains uncovered after two targeted waves;
- a full Cheeger positive-relaxation spin application and a load-bearing spectral-profile/evolving-set IPS application remain uncovered from Assignment 004;
- nonreversible sector/hypocoercive quantitative relaxation remains uncovered after the Assignment-003 search and was not reopened here;
- projective-limit constructions based on exact consistent finite-dimensional marginals, as opposed to tightness/compactness of N/V dynamics, could still merit a separate page if a clean interacting primary source is found;
- comparison of KCSM directly with independent unconstrained refresh dynamics remains only partially covered; the live FA-1f/East constraint-domination page compares to a simpler constrained reference rather than fully unconstrained refresh.

No `docs/` or `mkdocs.yml` files were edited. Mechanical validation is left to the principal/orchestrator's normal post-commit run; this handoff does not claim a validator pass.
