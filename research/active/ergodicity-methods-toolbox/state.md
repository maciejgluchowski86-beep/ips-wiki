# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent interacting Markov models.

Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/015-wave-six-audited-integrated-wave-seven-opened.md`.

## Publication status

There are now **67 staged entries**, all Professor source-audited and accepted, and all 67 have live counterparts under `docs/entries/`.

The wave-one-through-five 57-page layer is mechanically verified by Meeting 014. Before the wave-six source audit, the principal/orchestrator reported:

```text
Checked 67 entries; 0 failed mechanical validation.
```

and confirmed that neither wave-six student touched `docs/` or `mkdocs.yml`.

Meeting 015 promoted all ten wave-six entries. A GitHub comparison from the verified wave-five tree `aa28743` shows exactly ten added public method pages plus modifications to `docs/ergodicity-methods.md` and `mkdocs.yml`, with no other `docs/` path changed.

The **post-wave-six structural publication check is still pending**. The principal/orchestrator should rerun `validate_entries.py`, `mkdocs build --strict`, staged/live/hub completeness, current-audit metadata, nav-target resolution, and additions-only legacy safety against the final 67-page tree.

Structural checks do not add source or mathematical authority. Source/claim acceptance is recorded in Meetings 002--005, 010, 013, and 015.

The repository-wide article layout remains unchanged: toolbox pages live in `docs/entries/`. The separate principal-level legacy-directory question is not reopened by the Professor.

## Wave-six ruling

All ten wave-six entries were accepted.

Two non-substantive corrections were made before publication:

- a control character in the hierarchical renormalisation page was repaired to the intended `\varepsilon`;
- `environment-seen-second-class-particle` was reclassified from `lyapunov-regeneration` to `coupling` because the moving-frame coupling, not a regeneration argument, is load-bearing.

Wave six added:

- infinite-dimensional Harris--Lyapunov total-variation ergodicity;
- hierarchical renormalised Brascamp--Lieb spectral-gap recursion;
- exact projective consistency of splitting Gibbs/loss-network equilibrium laws;
- relative-entropy-loss Gibbs-attractor arguments;
- stochastic localization for Ising Glauber gaps;
- coupling independence and coarse-grained Glauber comparison;
- sticky McKean--Vlasov coupling;
- particle-number-uniform componentwise reflection coupling;
- survival-conditioned renewal points for multitype contact complete convergence;
- convergence/ergodicity of the TASEP environment seen from a second-class particle.

Negative taxonomy findings are also durable. Generic full-Cheeger positive-spin, spectral-profile/evolving-set IPS, fully-unconstrained-refresh KCSM, disagreement-front regeneration, and quasi-successful-coupling searches are closed absent a concrete named source changing the evidence.

## Workers

- Student F: **active** on `students/student-f/assignment-007.md`.
- Student G: **active** on `students/student-g/assignment-006.md`.

Students stage only under the research workspace, commit each finished method separately, and do not edit `docs/` or `mkdocs.yml`.

## Wave-seven direction

Wave seven is source-led and deliberately smaller. Returning fewer than four entries is acceptable.

### Student F

Hairer--Mattingly asymptotic strong Feller uniqueness; Hairer--Mattingly Hörmander/Malliavin propagation if taxonomically separate; Ullrich Swendsen--Wang/FK cluster-dynamics comparison; Erbar--Henderson--Menz--Tetali entropic Ricci curvature if distinct from live Bochner/Wasserstein methods.

### Student G

Gray's 1982 positive-rates theorem proof architecture; Gray's 1986 general attractive-spin-system duality and edge relaxation; Toom graphical contour/error expansions for low-noise PCA; essential hitting times/almost-subadditive regeneration for contact-process growth if distinct enough from existing renewal pages.

## Next Professor action

Source-audit the next completed wave-seven handoff before promotion or further assignment on that lane. Separately, the principal/orchestrator should close the pending 67-page structural publication gate.
