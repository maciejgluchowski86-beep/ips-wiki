# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

The breadth-compilation phase is ending. The principal has ruled that **wave seven is the final collection wave**. After it is audited and integrated, the programme turns to assessing which toolbox methods are most useful for either one-dimensional FA-1f/East out-of-equilibrium convergence or the positive-rates conjecture for simple IPS.

Latest meeting: `meetings/016-wave-six-verified-collection-sunset-assessment-phase.md`.

Assessment protocol: `assessment-protocol.md`.

## Publication status

There are **67 staged entries**, all Professor source-audited and accepted, and all 67 have live counterparts under `docs/entries/`.

The complete 67-page wave-one-through-six layer is now mechanically verified. The principal/orchestrator reports:

```text
Checked 67 entries; 0 failed mechanical validation.
```

and `mkdocs build --strict` exits 0 with no warnings and no broken internal links. The only INFO output is unchanged legacy material predating this programme.

Completeness is exact: 67 staged entries, 67 promoted pages, 67 hub links, zero unresolved, no orphan in either direction, every promoted page carries `status:` and `audit:`, and all 164 MkDocs `.md` navigation targets resolve. `git diff origin/main..research/ergodicity-methods-toolbox -- docs/` remains additions-only with zero non-additions.

These checks are structural only. Source/claim authority is the Professor audit recorded in Meetings 002--005, 010, 013, and 015.

The repository-wide article layout remains unchanged: toolbox pages live in `docs/entries/`. The separate principal-level legacy-directory question remains open and is not a Professor task.

## Entry hygiene

Meeting 015 exposed a validator blind spot: a TeX backslash had been consumed into a vertical-tab control character in one staging entry. The principal/orchestrator subsequently scanned 230 staged/promoted pages for control and Unicode format characters; the toolbox material is clean. One instance exists only in frozen legacy material and has been reported separately to the principal.

Future entry review must use both a control/format scan and visual/diff inspection of TeX backslashes. A scan can catch escape collapses such as `\b` or `\v`, but a lost backslash in commands such as `\alpha` or `\mu` may leave no control byte. The research `entry-template.md` now records this rule.

## Wave-six ruling

All ten wave-six entries were accepted and promoted. Two non-substantive corrections were made before publication:

- a control character in the hierarchical-renormalisation page was repaired to the intended `\varepsilon`;
- `environment-seen-second-class-particle` was reclassified from `lyapunov-regeneration` to `coupling` because the moving-frame coupling is load-bearing.

Repeated generic searches closed by Meeting 015 remain closed absent named new evidence: full-Cheeger positive-spin relaxation, spectral-profile/evolving-set IPS use, fully-unconstrained-refresh KCSM comparison, disagreement-front regeneration, quasi-successful coupling, artificial Nummelin splitting, nonreversible sector/hypocoercive IPS relaxation, boundary-uniform projective graphical coupling, and generic common/basic graphical coupling.

## Workers and final collection wave

- Student F: **active** on `students/student-f/assignment-007.md`.
- Student G: **active** on `students/student-g/assignment-006.md`.

Wave seven is source-led, deliberately small, and explicitly the final breadth wave. Students may return fewer entries rather than pad.

### Student F

Hairer--Mattingly asymptotic strong Feller uniqueness; Hairer--Mattingly Hörmander/Malliavin propagation if taxonomically separate; Ullrich Swendsen--Wang/FK cluster-dynamics comparison; Erbar--Henderson--Menz--Tetali entropic Ricci curvature if distinct from existing Bochner/Wasserstein methods.

### Student G

Gray's 1982 positive-rates proof architecture; Gray's 1986 attractive-spin-system duality and edge relaxation; Toom graphical contour/error expansions for low-noise PCA; essential hitting times/almost-subadditive contact-process regeneration if sufficiently distinct from existing renewal pages.

No wave eight of generic collection is authorized.

## Post-wave-seven phase

After wave seven lands:

1. Professor source-audits and integrates only passing entries.
2. The principal/orchestrator runs the final structural publication gate on the frozen inventory.
3. Breadth collection stops.
4. Student F receives the **FA-1f/East applicability audit** described in `assessment-protocol.md`.
5. Student G receives the **positive-rates applicability audit** described there.
6. The students then hostile-review only each other's shortlists.
7. The Professor synthesizes ranked method priorities and at most two recommended first proof experiments per problem.

Applicability is judged against exact unresolved objects and exact obstruction records, not thematic similarity. The positive-rates authoritative compact record is `programme-established-results.md` plus final `state.md` on branch `research/positive-rates-conjecture`. The FA-1f assessment uses the one-dimensional chronology/sign reductions, the closed finite-seed programme, and East as a solved screening benchmark.

## Next Professor action

Source-audit wave seven when it lands. Do not issue another collection assignment. After integration, freeze the method inventory and issue the two problem-specific applicability audits.
