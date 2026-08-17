# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Problem-specific applicability assessment of the completed ergodicity-methods toolbox.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/018-final-74-verified-professor-takes-fa-lane.md`.
- Assessment protocol: `research/active/ergodicity-methods-toolbox/assessment-protocol.md`.
- Student G: active on Assignment 007, positive-rates applicability audit.
- Student F: unavailable because its conversation reached the maximum-length/session limit; Assignment 008 is durable but not running.
- Professor: owns the FA-1f/East applicability audit directly.

Breadth collection is finished. The final frozen inventory contains **74 source-audited method pages**. No wave eight or generic gap-filling search is authorized.

The programme now asks which frozen methods are most useful for either:

1. one-dimensional FA-1f / East out-of-equilibrium convergence; or
2. the positive-rates conjecture for simple IPS.

## Coverage and publication status

All **74 staged method entries are Professor source-audited and accepted**, and all 74 have live counterparts under `docs/entries/`.

Meeting 018 records the final post-integration structural gate:

```text
Checked 74 entries; 0 failed mechanical validation.
```

`mkdocs build --strict` exits 0 with no warnings and no broken internal links. Completeness is exact: 74 staged entries, 74 promoted pages, 74 hub links, zero unresolved, no orphan in either direction, every promoted page carries `status:` and `audit:`, and all 171 MkDocs `.md` navigation targets resolve. The `docs/` diff against `origin/main` remains additions-only with zero non-additions, and the control/format-character scan is clean across all 74 staged entries.

These checks are structural only. Source/claim acceptance is the Professor audit recorded through Meeting 017.

Therefore the final **74-method toolbox is source-audited, live, and mechanically verified**. No collection-phase publication gate remains open.

The principal-level directory question remains open. No public-doc restructuring is part of the applicability phase.

## Entry hygiene

A TeX-escape corruption found during wave-six source audit showed that required-field validation alone is insufficient. The entry template requires a control/format-character scan plus visual/diff inspection of mathematical backslashes.

Professor ruling for the offered validator extension: hard-fail actual disallowed control or Unicode format characters in staged entries, preserve ordinary Markdown whitespace, and do not add unreliable heuristics for silently lost TeX backslashes such as `alpha` or `mu`. Frozen legacy corruption remains outside this programme.

## Active applicability phase

Student G is running the positive-rates audit under `students/student-g/assignment-007.md`.

Student F cannot receive the FA-1f/East assignment because its conversation is no longer accepting turns. Attempts to use dormant earlier F conversations also fail. The Professor therefore takes the FA-1f/East audit directly rather than serializing both primary audits through G or waiting for a replacement worker.

Both primary audits use the same `assessment-protocol.md` standard: classify all 74 methods A/B/C/X/N, return at most six ranked A/B candidates, state explicit bridge lemmas, identify exact obstruction avoidance, and give cheap falsification tests.

After both audits are available, hostile cross-review is performed on the shortlists only, followed by Professor synthesis with at most two recommended first proof experiments per problem. A new worker session, if the principal opens one, should be used first to restore independent cross-review capacity rather than to restart breadth collection.

## Previous scientific direction

The direct positive-rates proof loop is stopped and archived on branch `research/positive-rates-conjecture`. Its exact obstruction record is input to the present assessment, not an invitation to restart an exhausted architecture under a new name.
