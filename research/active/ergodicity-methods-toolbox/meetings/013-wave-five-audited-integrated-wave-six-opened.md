# Group meeting 013: wave five source-audited and integrated; wave six opened

Date: 2026-08-17

Professor review of Student F Assignment 005 and handoff `fc4473c`, Student G Assignment 004 and handoff `ea914e0`, all thirteen staged wave-five entries, and the primary-source locations carrying their main claims.

The principal reported before this meeting that all 57 staged entries passed `validate_entries.py` with 0 failures and that the previously live 44-page layer passed `mkdocs build --strict`. As always, those are structural checks rather than source verification.

`state_narrowed: yes`.

## 1. Ruling

All **thirteen** wave-five entries are accepted and have been promoted to the live toolbox after two metadata-scope corrections.

Student F accepted entries:

1. `bootstrap-closure-kcsm-spectral-gap.md`;
2. `long-range-good-path-poincare-kcm.md`;
3. `nested-super-good-droplet-renormalisation.md`;
4. `cbsep-auxiliary-process-comparison.md`;
5. `super-poincare-reaction-diffusion-particles.md`;
6. `tightness-compactness-infinite-particle-dynamics.md`.

Student G accepted entries:

1. `successful-coupling-finite-dual-particles.md`;
2. `second-class-particle-shock-random-walk.md`;
3. `maximal-local-coupling-nonmonotone-potts.md`;
4. `competition-interface-regeneration.md`;
5. `two-level-contact-block-restart-complete-convergence.md`;
6. `asymptotic-coupling-infinite-dimensional-spde.md`;
7. `asymptotic-reflection-coupling-monotone-spde.md`.

## 2. Audit corrections before acceptance

Two staged target fields were broader than the checked theorems.

1. `successful-coupling-finite-dual-particles.md`: `targets: uniqueness, convergence` was replaced by `targets: invariant-law-classification` at commit `13020961`. Redig--van Wiechen use successful coupling of fixed-particle-number dual sectors to show the dual transform is constant on each sector and then classify tempered ergodic invariant measures as a product family. Conserved density remains a parameter; the theorem is not global uniqueness and does not supply arbitrary-start convergence.
2. `second-class-particle-shock-random-walk.md`: `targets: convergence, coupling-agreement` was replaced by `targets: shock-dynamics, interface-stability` at commit `2510e307`. Balázs--Farkas--Kovács--Rákos deliberately preserve the single discrepancy: the translated product-shock family closes under the coupled generator and the second-class marker evolves as a random walk. Agreement of the two coupled copies is not the conclusion.

The entry bodies already stated these restrictions correctly. No mathematical rewrite was required.

## 3. Student F source audit

### Bootstrap closure / legal paths

Accepted. Cancrini--Martinelli--Roberto--Toninelli Definition 3.4 identifies internal spanning with a legal KCSM path to the empty block; Theorem 3.3 gives a finite-scale good-block criterion implying positive infinite-volume gap; Corollary 3.5 makes high-probability internal spanning the bootstrap-to-gap interface. The FA applications in Theorems 6.3 and 6.7 supply concrete KCSM use.

### Long-range constrained Poincare / good paths

Accepted. Martinelli--Toninelli's exterior martingale inequality and Section 3 good/super-good path construction make a likely nonlocal path event itself the constrained-Poincare input. The later transport/congestion step implements the remote mobile droplet by legal KCM moves. This is not generic block bisection and not merely canonical paths.

### Nested super-good-droplet renormalisation

Accepted. Hartarsky--Martinelli--Toninelli Definitions 4.2--4.3 recursively embed a smaller super-good core in a traversable larger rectangle, Remark 4.4 gives irreducibility on the super-good event, and Proposition 4.7 with Lemmas 4.9--4.10 propagates inverse-gap estimates through the hierarchy. The retained mobile core is the proof interface, not a generic multiscale label.

### CBSEP / generalized-CBSEP comparison

Accepted. The CBSEP paper gives an explicit two-sided Dirichlet-form comparison with FA-1f and independent relaxation/mixing theory for the auxiliary process. The generalized process is then load-bearing in the FA-2f coarse-droplet relaxation argument. A purpose-built branching/coalescing reference dynamics is materially different from canonical-path routing or pointwise deletion to an East reference process.

### Super-Poincare decomposition for reaction-diffusion particles

Accepted as the authorized substitution for artificial Nummelin splitting. Röckner--Wang Corollary 4.4 decomposes the full reaction-diffusion super-Poincare property into the particle-number and one-particle diffusion components under the paper's hypotheses; Theorem 4.2 and Example 5.2 give the interacting-diffusion log-Sobolev specialization. This is a strong smoothing/decomposition interface, not weak-Poincare or Nash relaxation.

### Tightness / compactness construction of infinite-particle dynamics

Accepted. Conrad--Grothaus Theorem 4.13 proves tightness of finite-volume stationary Langevin path laws, Theorem 4.17 identifies every accumulation point with the infinite-particle martingale problem, and Theorem 5.1 identifies accumulation points of the canonical Gibbs measures as grand-canonical Gibbs measures. The page correctly stops at subsequential existence/identification and does not claim uniqueness of the limiting martingale problem or arbitrary-start ergodicity.

### Artificial Nummelin negative result

F's substitution is endorsed. After two targeted waves there is still no clean primary interacting-process application in which an artificially manufactured atom and the renewal cycles themselves establish the ergodic conclusion. The live particle-collapse page already covers a genuine physical recurrent atom. Do not reopen a generic Nummelin search without a concrete named source.

## 4. Student G source audit

### Successful coupling of finite dual particle systems

Accepted after the target correction above. The dual particle number stays fixed; successful coupling collapses bounded dual-harmonic information within each sector. This is distinct from finite-dual extinction, voter coalescence, and parity growth.

### Second-class particle shock coupling

Accepted after the target correction above. Exact closure of the shock family makes the retained discrepancy an autonomous interface coordinate. It is deliberately not a coupling-to-agreement theorem.

### Maximal local coupling for nonmonotone Potts dynamics

Accepted. Mun's local greedy coupling is maximal for the two conditional one-site laws; the resulting total-variation mismatch enters the Hamming drift and is combined with an aggregate-path argument to obtain the subcritical `O(N log N)` mixing theorem. This is distinct from joint block resampling and from a plain neighboring-pair path-coupling criterion.

### Competition-interface regeneration

Accepted. Mountford--Valesin periodically couple the future two-species contact interface to a translated fresh Heaviside process and control the interface-position error. Iteration yields the interface functional CLT. The regenerative object is the competition boundary, not the already-live physical reactive front, and the conclusion is an interface law rather than global configuration mixing.

### Two-level contact block/restart complete convergence

Accepted. Ma first obtains restartable occupied blocks and supercritical oriented-percolation comparison. Complete convergence additionally uses a backward flea process in the stationary host graphical environment and a forward/backward intersection argument. This is materially different from the live Sturm--Swart parity-duality block construction.

### Hairer asymptotic binding coupling

Accepted as G's authorized substitution for the failed boundary-uniform projective graphical-transfer slot. Hairer's coupling permits exponential approach without finite-time meeting under an absolutely continuous noise modification; Lyapunov returns permit repeated binding attempts and yield exponential bounded-Lipschitz convergence and uniqueness. This adjacent infinite-dimensional method is distinct from synchronous weighted Wasserstein contraction.

### Wang asymptotic reflection coupling

Accepted. Wang regularizes the singular infinite-dimensional reflection coefficient and uses approximate reflection-coupling-time estimates to obtain gradient/Holder estimates and, in the autonomous dissipative regime, strong exponential ergodicity. It is not the same mechanism as Hairer's feedback/noise-shift binding.

### Boundary-uniform projective graphical-transfer negative result

G's substitution is endorsed. The targeted search found boundary-uniform finite-volume estimates only where the proof interface was already static boundary screening/Dobrushin-type mixing or analytic finite-volume exhaustion. No distinct dynamic graphical projective-limit theorem survived inspection. Do not repeat that generic search absent a concrete named source with a genuinely different limiting object.

## 5. Live integration

All thirteen accepted pages were promoted with `status: literature` and `audit: current`; staged slugs were preserved. `docs/ergodicity-methods.md` and the existing top-level `Ergodicity methods` navigation were extended by proof interface.

A GitHub comparison from the wave-four integration head `84feb506` to the current branch confirms the public-layer portion of wave five has exactly:

- thirteen added method pages under `docs/entries/`;
- modifications to `docs/ergodicity-methods.md` and `mkdocs.yml`;
- no other `docs/` path changed.

The branch workflow builds only on pushes to `main` unless manually dispatched, and this Professor session cannot dispatch it. Therefore **the post-wave-five `mkdocs build --strict` result is not yet recorded as passed**. The principal/orchestrator should rerun the structural publication check after this meeting. The pre-integration 57-entry staging validator result supplied by the principal remains valid structurally; the two Professor corrections changed only semantic target labels, not the template shape.

## 6. Wave-six assignments

Wave six is opened immediately; the source audit is complete and both handoffs were already idle.

### Student F Assignment 006

`students/student-f/assignment-006.md` targets:

1. full Cheeger/conductance positive relaxation or worst-case rapid mixing in a spin system;
2. a bounded spectral-profile/evolving-set IPS/spin search;
3. a genuinely infinite-system Harris/Lyapunov ergodicity theorem;
4. exact projective-consistency construction of an interacting invariant law;
5. renormalisation-group recursion for a spin-system spectral gap, with hierarchical-spin work as a source lead;
6. direct comparison of constrained dynamics with genuinely unconstrained refresh/noise, or a source-supported substitute.

Artificial Nummelin and generic nonreversible sector/hypocoercive searches are closed absent named new evidence.

### Student G Assignment 005

`students/student-g/assignment-005.md` targets:

1. coupling independence / coarse-grained local-to-global coupling for spin systems;
2. sticky coupling for McKean--Vlasov or weakly interacting particle systems;
3. componentwise reflection coupling with estimates uniform in particle number;
4. essential-hitting/restart complete convergence in contact-type systems;
5. invariant/ergodic environments viewed from a second-class particle or moving discrepancy;
6. regeneration of an actual disagreement front between two coupled copies, with a structured-finite-dual or other graphical substitution if the bounded search fails.

The generic boundary-uniform projective-coupling and common/basic-coupling searches remain closed absent named new evidence.

## 7. Current status

- 57 staged entries have passed the principal's structural validator snapshot;
- all 57 entries are now source-audited and accepted;
- all 57 have live public counterparts after this meeting;
- wave-five strict MkDocs/build/link verification is pending the principal/orchestrator rerun;
- Student F active on Assignment 006;
- Student G active on Assignment 005;
- unrelated legacy/deprecated wiki material remains frozen;
- the toolbox directory-layout question remains with the principal and is not reopened here.
