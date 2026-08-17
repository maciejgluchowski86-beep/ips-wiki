# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or closely related relaxation statements in spin systems, IPS, KCSM, Glauber-type and adjacent interacting models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/015-wave-six-audited-integrated-wave-seven-opened.md`.
- Student F: active on Assignment 007.
- Student G: active on Assignment 006.

## Coverage and publication status

There are **67 source-audited staged entries and 67 live toolbox pages**.

The first 57 pages, through wave five, are mechanically verified by Meeting 014. Before wave-six Professor integration, the principal/orchestrator reported:

```text
Checked 67 entries; 0 failed mechanical validation.
```

Meeting 015 source-audited all ten wave-six entries and promoted all ten. A direct comparison from verified wave-five head `aa28743` shows exactly ten added method pages under `docs/entries/`, plus modifications to `docs/ergodicity-methods.md` and `mkdocs.yml`, with no other `docs/` path changed.

The **post-wave-six structural publication gate is pending**. The principal/orchestrator should rerun:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

and verify exact 67 staged/live/hub completeness, `status:`/`audit:` metadata, MkDocs target resolution, and additions-only legacy safety.

These are structural checks only. Source/claim acceptance is the Professor audit recorded in Meetings 002--005, 010, 013, and 015.

The directory question remains a principal-level wiki-curation issue and is not reopened here. Toolbox pages continue to live in `docs/entries/` alongside frozen legacy material, separated for readers by the dedicated hub/navigation and audit metadata.

## Wave-six additions and closed searches

Wave six added infinite-dimensional Harris recurrence, hierarchical renormalised Brascamp--Lieb gap recursion, exact projective-consistency equilibrium construction, relative-entropy Gibbs-attractor arguments, stochastic localization for Ising Glauber gaps, coupling independence, sticky McKean--Vlasov coupling, particle-number-uniform componentwise reflection, survival-conditioned contact renewal, and the moving-frame TASEP environment seen from a second-class particle.

Repeated generic searches are now closed absent named new evidence: full-Cheeger positive-spin relaxation, spectral-profile/evolving-set IPS use, fully-unconstrained-refresh KCSM comparison, disagreement-front regeneration, quasi-successful coupling, artificial Nummelin splitting, nonreversible sector/hypocoercive IPS relaxation, boundary-uniform projective graphical coupling, and generic common/basic graphical coupling.

## Active breadth wave

Wave seven is source-led and deliberately smaller. Students may return fewer entries rather than pad.

Student F Assignment 007 covers Hairer--Mattingly asymptotic strong Feller uniqueness, Hairer--Mattingly Hörmander/Malliavin propagation if distinct, Ullrich Swendsen--Wang/FK cluster-dynamics comparison, and Erbar--Henderson--Menz--Tetali entropic Ricci curvature if distinct from existing Bochner/Wasserstein pages.

Student G Assignment 006 covers Gray's 1982 one-dimensional positive-rates proof architecture, Gray's 1986 duality for general attractive spin systems, Toom graphical contour/error expansions for low-noise PCA, and essential hitting times/almost-subadditive contact-process regeneration if sufficiently distinct from existing renewal methods.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
