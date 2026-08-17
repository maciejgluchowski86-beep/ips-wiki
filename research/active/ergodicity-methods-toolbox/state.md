# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

**Breadth collection is complete.** Wave seven was the final collection wave. The programme is now in the problem-specific applicability phase governed by `assessment-protocol.md`.

Latest meeting: `meetings/017-wave-seven-audited-collection-frozen-assessment-dispatched.md`.

## Frozen inventory and publication status

There are **74 staged method entries**, all Professor source-audited and accepted, and all 74 have live counterparts under `docs/entries/`.

The first 67 pages, through wave six, are mechanically verified by Meeting 016. Before wave-seven Professor integration, the principal/orchestrator reported:

```text
Checked 74 entries; 0 failed mechanical validation.
```

and a clean control/format-character scan across all 74 staged entries. Neither wave-seven student touched `docs/` or `mkdocs.yml`.

Meeting 017 source-audited and promoted all seven wave-seven entries. A GitHub comparison from the verified wave-six baseline `cedd415` shows exactly seven added public method pages plus modifications to `docs/ergodicity-methods.md` and `mkdocs.yml`, with no other public `docs/` path changed.

The **final post-wave-seven 74-page structural publication gate is pending**. The principal/orchestrator should rerun `validate_entries.py`, `mkdocs build --strict`, 74 staged/live/hub completeness, current-audit metadata, nav-target resolution, additions-only legacy safety, and the control/format-character scan on the integrated tree.

Structural checks do not add mathematical or source authority. Source/claim acceptance is recorded through Meeting 017.

The repository-wide article layout remains unchanged: toolbox pages live in `docs/entries/`. The separate principal-level legacy-directory question remains open and is not a Professor task.

## Wave-seven ruling

All seven staged entries were accepted and promoted:

- asymptotic strong Feller support separation and uniqueness;
- Hörmander--Malliavin propagation of degenerate noise to asymptotic smoothing;
- Swendsen--Wang / heat-bath Edwards--Sokal kernel comparison;
- entropic Ricci curvature from weak-interaction perturbation;
- Gray's one-dimensional positive-rates edge-coalescence architecture;
- Toom error-graph expansion for low-noise PCA;
- essential hitting times plus almost-subadditive regeneration for contact-process growth.

One semantic metadata correction was made: the entropic-Ricci entry now targets `modified-log-sobolev`, not classical `log-sobolev`.

Gray 1986 was not staged because Student G could not inspect the primary full theorem/proof text. This is a **source-access hold**, not a negative taxonomy ruling or merger. It is outside the frozen 74-method inventory unless the principal explicitly reopens it later.

## Entry hygiene

Meeting 015 exposed a validator blind spot in which a TeX escape became a control character. Entry review now requires both a control/format-character scan and visual/diff inspection of mathematical backslashes.

Professor ruling on the proposed validator extension:

- hard-fail actual disallowed control or Unicode format characters in staged entries;
- preserve ordinary structural whitespace required by Markdown;
- do not hard-fail heuristic guesses about silently lost TeX backslashes such as `alpha` or `mu`, because they have no reliable mechanical signature.

The frozen legacy control-byte issue reported by the principal/orchestrator is outside this programme and remains untouched.

## Active applicability assignments

- Student F: **active** on `students/student-f/assignment-008.md`, the complete FA-1f/East applicability audit.
- Student G: **active** on `students/student-g/assignment-007.md`, the complete positive-rates applicability audit.

Each student must classify all 74 frozen methods as A/B/C/X/N, return at most six ranked A/B candidates, formulate explicit bridge lemmas, identify the exact obstruction each route avoids, and give cheapest-first falsification tests. No broad new literature search and no public-doc edits are authorized.

After both audits return, the next step is hostile cross-review of the **shortlists only**, followed by Professor synthesis with at most two recommended first proof experiments per problem.

## Closed collection phase

There is no wave eight and no further generic gap-filling search under the current principal direction. Earlier negative taxonomy findings remain useful as anti-loop evidence, but the programme no longer maintains an uncovered-method agenda.

## Next Professor action

Receive F008/G007 applicability audits, audit their bridge statements against the exact FA-1f and positive-rates obstruction records, then dispatch hostile cross-review of only the surviving shortlists.
