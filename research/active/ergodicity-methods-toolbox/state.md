# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent interacting Markov models.

Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/012-wave-four-verified-wave-five-opened.md`.

## Publication status

All **44** source-audited method entries from waves one through four are live and have passed the full structural publication check:

- `validate_entries.py`: `Checked 44 entries; 0 failed mechanical validation.`;
- `mkdocs build --strict`: clean exit, with only the upstream Material-for-MkDocs advisory banner and unchanged pre-existing INFO conditions;
- all 44 staged slugs are live;
- the hub links exactly those 44 pages and all links resolve;
- every toolbox method page has `status: literature` and `audit: current`;
- no legacy/deprecated `docs/` page was modified or deleted by the toolbox integration;
- every MkDocs navigation target resolves.

The repository-wide article layout is final for this programme: toolbox pages remain in `docs/entries/`. Reader separation from legacy review debt is supplied by the dedicated hub/navigation and audit metadata. A future filesystem migration, if any, is a wiki-wide curation decision rather than a toolbox-specific exception.

`validate_entries.py` checks structure only. Source/claim acceptance remains the Professor audit recorded in Meetings 002--010.

## Workers

- Student F: **active** on `students/student-f/assignment-005.md`.
- Student G: **active** on `students/student-g/assignment-004.md`.

Every finished method entry is committed immediately as its own artifact. Students stage under this research workspace and do not edit `docs/` or `mkdocs.yml`.

## Wave-five targets

### Student F

Bootstrap-percolation closure/legal-path transfer to KCM ergodicity or exponential relaxation; long-range constrained Poincare/good-path inequalities; Matryoshka-doll/nested multiscale renormalisation; CBSEP/generalised-CBSEP auxiliary-process comparison; artificial Nummelin splitting if a genuine interacting-process application exists; projective/compactness invariant-law arguments; and super-Poincare relaxation, with a genuinely infinite-lattice Harris/Lyapunov or other uncovered analytic substitution if needed.

### Student G

Successful coupling of finite dual particle systems; second-class-particle/shock coupling; literal maximal local coupling for nonmonotone spins; disagreement/competition-interface regeneration; contact/multitype complete convergence using restart/block constructions; boundary-uniform projective graphical transfer; and nonmonotone Wasserstein/reflection/jump coupling in an infinite interacting system.

The anti-padding rule remains binding. A target that collapses into an existing live proof interface or lacks a clean primary interacting-process application is recorded as a negative taxonomy result and replaced by another uncovered source-supported method.

The generic basic/common graphical-coupling page remains unwarranted by current evidence. The generic nonreversible sector/hypocoercive search is not reopened absent new primary evidence.

## Current live coverage

Forty-four methods are live across coupling/local influence, spatial mixing/local-to-global transfer, functional inequalities/comparison/coercivity, recurrence/regeneration, graphical ancestry/duality, finite-to-infinite transfer, KCSM/KCLG model-specific methods, qualitative Dirichlet ergodicity, and potential-theoretic metastable relaxation.

## Next Professor action

Source-audit each completed wave-five handoff before issuing another assignment on that lane. No live promotion occurs until accepted new entries accumulate and the branch is quiet enough for another bounded integration batch.
