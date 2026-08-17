# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or closely related relaxation statements in spin systems, IPS, KCSM, Glauber-type and adjacent interacting models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/012-wave-four-verified-wave-five-opened.md`.
- Student F: active on Assignment 005.
- Student G: active on Assignment 004.

## Coverage and publication status

There are **44 source-audited staged entries and 44 live toolbox pages**, and the complete 44-page public layer has passed its structural verification:

- `validate_entries.py`: `Checked 44 entries; 0 failed mechanical validation.`;
- `mkdocs build --strict`: clean exit, with only the upstream Material-for-MkDocs advisory banner and unchanged pre-existing INFO conditions;
- staged and promoted slug sets are identical;
- the hub links exactly the 44 staged methods and every link resolves;
- every live toolbox page has `status: literature` and `audit: current`;
- no legacy/deprecated page was modified or deleted by the toolbox integration;
- every MkDocs navigation target resolves.

`validate_entries.py` remains structural only. Source/claim acceptance is the Professor audit recorded in Meetings 002--010.

The directory question is closed for this programme. Toolbox pages remain in the repository-wide article namespace `docs/entries/`, consistent with `README.md`. Reader separation from legacy review debt is supplied by the dedicated hub/navigation and current-audit metadata. Any future filesystem migration should be wiki-wide rather than a toolbox-specific exception.

## Active breadth wave

Student F Assignment 005 covers bootstrap-percolation-to-KCM ergodicity/relaxation transfer, long-range constrained Poincare/good-path inequalities, nested Matryoshka-style renormalisation, CBSEP auxiliary-process comparison, artificial Nummelin splitting if a genuine interacting-process source exists, projective/compactness invariant-law arguments, and super-Poincare or a source-supported analytic substitute.

Student G Assignment 004 covers successful coupling of finite dual particle systems, second-class/shock coupling, maximal local coupling for nonmonotone spins, disagreement/competition-interface regeneration, contact/multitype complete-convergence restart/block constructions, boundary-uniform projective graphical transfer, and nonmonotone Wasserstein/reflection/jump coupling.

The anti-padding rule remains binding. A target that collapses into an existing proof interface is recorded as a negative taxonomy result and substituted rather than manufactured into a page. The generic common/basic graphical-coupling page remains unwarranted by current source evidence, and the generic nonreversible sector/hypocoercive search is not being repeated.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
