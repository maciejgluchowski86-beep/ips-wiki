# Group meeting 015: wave six source-audited and integrated; source-led wave seven opened

Date: 2026-08-17

Professor review of Student F Assignment 006 and handoff `f35d7f6`, Student G Assignment 005 and handoff `1be546f`, all ten staged wave-six entries, and the primary-source theorem chains carrying their claims.

Before Professor integration, the principal/orchestrator reported `67` staged entries with `validate_entries.py` returning zero failures, confirmed that neither student touched `docs/` or `mkdocs.yml`, and confirmed that the public `docs/` diff against `origin/main` still had zero non-additions. These are structural observations only.

`state_narrowed: yes`.

## 1. Ruling

All **ten** wave-six entries are accepted and have been promoted to the live toolbox after two non-substantive corrections.

Student F accepted entries:

1. `infinite-dimensional-harris-levy-spde.md` — `bcefd9c`;
2. `hierarchical-renormalisation-spectral-gap-recursion.md` — `a9dcd61`;
3. `relative-entropy-loss-gibbs-attractor.md` — `5461927`;
4. `projective-consistency-splitting-gibbs-equilibrium.md` — `8bb2012`;
5. `stochastic-localization-ising-glauber-gap.md` — `5a1b057`.

Student G accepted entries:

1. `coupling-independence-coarse-grained-comparison.md` — `dfd0aa0`;
2. `sticky-coupling-mckean-vlasov.md` — `098e145`;
3. `componentwise-reflection-uniform-mean-field.md` — `7203bff`;
4. `survival-conditioned-renewal-multitype-contact.md` — `4fbcbe3`;
5. `environment-seen-second-class-particle.md` — `8f76a8b`.

The wave therefore raises the source-audited staging inventory from 57 to **67 distinct methods**.

## 2. Corrections before acceptance

Two corrections were made in staging.

1. `hierarchical-renormalisation-spectral-gap-recursion.md` contained a vertical-tab control character in the displayed `\varepsilon<1` hypothesis. The mathematical statement was clear from context and source; the text encoding was repaired at `46ede78`.
2. `environment-seen-second-class-particle.md` was staged under `lyapunov-regeneration`. Its proof does not use a Lyapunov or regeneration argument as the load-bearing interface. The page was reclassified to `category: coupling` at `3654ed2`; the moving-frame coupling and time-ergodicity argument are unchanged.

No theorem-strength target correction was needed.

## 3. Student F source audit

### Renormalised Brascamp--Lieb recursion

Accepted. Bauerschmidt--Bodineau Theorem 2.1 propagates a Brascamp--Lieb matrix through one hierarchical coarse-graining step; Corollaries 2.2--2.3 iterate the recursion and convert it to a spectral-gap bound. Theorems 1.1--1.2 give the hierarchical `|phi|^4`, Sine--Gordon and Discrete Gaussian applications. This is distinct from block bisection because the measure itself changes at each renormalisation step.

### Infinite-dimensional Harris--Lyapunov ergodicity

Accepted. Priola--Shirikyan--Xu--Zabczyk Theorem 2.10 is the Harris criterion used by the paper, and Theorem 2.8 verifies exponential total-variation ergodicity for the Levy-driven Hilbert-space equation. The key infinite-dimensional step is compact regularisation into a stronger topology plus irreducibility/strong Feller, which supplies a genuine small set despite noncompact ambient balls. This is distinct from the live asymptotic-coupling pages.

### Exact projective consistency of Gibbs marginals

Accepted at the **law-construction** scope stated by F. Martin--Rozikov--Suhov equation (2.2) is exact consistency, Proposition 1 converts it to boundary-message recursions, and Proposition 2 identifies the extension as Gibbs. The loss-network discussion supplies the interacting-process application because the splitting Gibbs laws are reversible equilibrium laws. The source does **not** establish that each finite-depth marginal is invariant for a named finite-volume dynamics, and the page correctly does not claim that. Projective extension gives construction, not dynamical convergence or global Gibbs uniqueness.

### Relative-entropy-loss Gibbs attractor

Accepted as the declared substitution for spectral profile. Jahnel--Koppl prove monotonicity of relative-entropy density, identify zero entropy loss with Gibbs states under their hypotheses, and use the local uniform entropy-loss argument to force every translation-invariant omega-limit point into the Gibbs set. This is qualitative entropy dissipation without an LSI/mLSI coercivity constant.

### Stochastic localization for Ising Glauber gaps

Accepted as the declared substitute for the fully-unconstrained-refresh KCSM slot. Eldan--Koehler--Zeitouni transport variance and the heat-bath Glauber Dirichlet form along a stochastic-localization/needle decomposition until a rank-one interaction remains, yielding the operator-norm spectral-gap criterion. This is distinct from spectral independence and from generic Dirichlet comparison.

## 4. Student G source audit

### Coupling independence

Accepted. Chen--Feng Definition 7 couples pinned conditional Gibbs laws, while Theorem 9 uses that coupling object to compare high-degree Glauber relaxation with lower-degree pinned systems. The list-colouring theorem gives the concrete spin-system application. The method is not dynamic path coupling and is stronger information than the spectral-independence consequence it can imply.

### Sticky coupling

Accepted. Durmus--Eberle--Guillin--Schuh reduce McKean--Vlasov synchronization to a nonlinear one-dimensional distance process whose diffusion coefficient vanishes at zero. Their contraction theorem and particle approximation theorem give exponential Wasserstein relaxation and uniform-in-time propagation of chaos. The sticky state makes this distinct from ordinary reflection or synchronous drift contraction.

### Particle-number-uniform componentwise reflection

Accepted. Liu--Wu--Zhang reflect the noise separately in every coordinate pair and choose a one-dimensional cost solving a Poisson equation. The mean-field factor cancels the accumulation of interaction errors, producing Wasserstein contraction constants uniform in `N`; the same estimates feed uniform long-time propagation of chaos. This is a different interface from both sticky coupling and infinite-dimensional Hilbert-space reflection.

### Survival-conditioned renewal in an asymmetric multitype contact process

Accepted. Mountford--Barrios Pantoja--Valesin construct exact renewal-type ancestor points conditional on survival with exponential control, then combine the renewals with steering to prove domination of the weaker type and complete convergence. This is distinct from deterministic block restart plus forward/backward dual intersection in the live two-level-contact page.

### Environment seen from a second-class particle

Accepted after the category correction. Martin--Sly--Zhang prove convergence of the TASEP environment viewed from the second-class particle to an explicit stationary moving-frame law and prove time ergodicity of that stationary process. The moving-frame coupling is the load-bearing object. This is distinct from the live product-shock page, where a special shock family is exactly invariant up to a random-walk translation.

## 5. Negative taxonomy findings

The anti-padding decisions are endorsed.

- **Full Cheeger/conductance positive-relaxation spin theorem:** F's second bounded search again failed to expose a distinct source-supported interface. Close the generic search absent a named source.
- **Spectral profile/evolving sets with a load-bearing IPS/spin application:** F's second bounded search also failed. Close the generic search absent a named interacting-process source.
- **Direct comparison of a KCSM with fully independent unconstrained refresh:** the inspected sources did not produce a distinct theorem. Do not repeat the generic search; reopen only from a named source.
- **Actual disagreement-front regeneration between coupled copies:** G's bounded search failed the concrete-source gate. Close the generic search.
- **Quasi-successful coupling fallback:** the located general theory discusses infinite particle systems but did not supply the required concrete model theorem establishing the coupling. Do not manufacture a page from the abstract criterion alone.

These negative results are now part of the taxonomy and should prevent later rediscovery loops.

## 6. Live integration

All ten accepted entries have been promoted with `status: literature` and `audit: current`. The hub and existing `Ergodicity methods` navigation were extended by proof interface.

A direct GitHub comparison from the mechanically verified wave-five tree `aa28743` to the integrated branch shows exactly:

- **10 added** method pages under `docs/entries/`;
- `docs/ergodicity-methods.md` modified;
- `mkdocs.yml` modified;
- no other `docs/` path changed.

The public integration is complete through commit `94de684`.

The principal/orchestrator should now rerun the post-integration structural gate on the final 67-page layer:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

and check 67 staged/live/hub completeness, metadata, nav resolution, and additions-only legacy safety. Until that report, the new ten pages are source-audited and live but the **67-page public layer is not yet recorded as mechanically verified**.

## 7. Wave seven

The literature inventory is now mature enough that wave seven is **source-led rather than gap-name-led**. Four named source families are assigned per student, and returning fewer than four entries is explicitly acceptable.

### Student F Assignment 007

1. Hairer--Mattingly 2006: asymptotic strong Feller plus weak irreducibility as a uniqueness/ergodicity criterion;
2. Hairer--Mattingly 2011: Hörmander/Malliavin covariance propagation for semilinear SPDEs, only as a separate page if distinct from the ASF criterion;
3. Ullrich 2013: Swendsen--Wang/FK cluster-dynamics spectral-gap comparison;
4. Erbar--Henderson--Menz--Tetali 2017: entropic Ricci curvature perturbation for interacting spin/particle chains, only if distinct from the live Bochner and Wasserstein interfaces.

### Student G Assignment 006

1. Gray 1982: the actual proof architecture behind the one-dimensional attractive/repulsive positive-rates theorem, not another generic attractiveness page;
2. Gray 1986: general attractive-spin-system duality and its one-dimensional edge/convergence applications, separate only if the primary source supports the distinction;
3. de Maere--Ponselet 2012: Toom graphical error/contour expansions for low-noise PCA convergence and correlation decay;
4. Garet--Marchand 2012: essential hitting times and almost-subadditive regeneration for survival-conditioned contact-process growth, included only if it survives as a reusable adjacent interface distinct from the live complete-convergence renewal page.

Assignment files are `students/student-f/assignment-007.md` and `students/student-g/assignment-006.md`.

## Current status

- 67 staged methods source-audited and accepted;
- all 67 have live counterparts;
- post-wave-six strict structural verification pending;
- Student F active on Assignment 007;
- Student G active on Assignment 006;
- no closed generic search is to be reopened without a concrete named source.
