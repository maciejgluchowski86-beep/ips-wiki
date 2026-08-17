# Meeting 026: toolbox publication ruling

Date: 2026-08-17

`state_narrowed: no`.

This meeting records a publication-governance ruling only. No mathematical research claim changes.

## Question

The ergodicity-methods toolbox branch contains the source-audited and mechanically verified 74-method public layer, but the branch has not been merged to `main`. The principal's original phase instruction was to add an ergodicity-proving-methods section to the main wiki. The practical questions are:

1. whether publication to `main` is part of this phase's deliverable or requires a separate principal authorization;
2. whether publication should be a direct merge of `research/ergodicity-methods-toolbox` or a pull request;
3. whether the unresolved legacy `docs/entries/` layout/curation question must be settled first.

## Ruling

### 1. Publication to `main` is part of the original deliverable

No new substantive principal authorization is required for the scoped ergodicity-methods publication itself.

Meeting 001 records that the later principal instruction explicitly reopened the **main wiki for this new section**, while keeping unrelated deprecated IPS entries frozen. It specified that accepted material would be promoted to:

- `docs/ergodicity-methods.md`;
- individual `docs/entries/<method-slug>.md` pages;
- a top-level `Ergodicity methods` section in `mkdocs.yml`.

Meeting 018 subsequently recorded the completed 74-page structural publication gate. Therefore leaving the section indefinitely only on the research branch would leave the original wiki deliverable incomplete.

This ruling does **not** authorize unrelated wiki restructuring or legacy cleanup.

### 2. Do not directly merge the research branch to `main`

Use a **publication-only pull request based on current `main`**.

Reason: `research/ergodicity-methods-toolbox` contains far more than the stable wiki artifact: research workspaces, assessments, meetings, assignments, live state/proof-spine changes, and root research-state changes. A wholesale branch merge would conflate research history with the outward-facing wiki publication.

The publication PR should contain only the stable public artifact:

1. the 74 audited new `docs/entries/*.md` method pages;
2. `docs/ergodicity-methods.md`;
3. the additive `Ergodicity methods` navigation changes applied to the **current-main** `mkdocs.yml`.

Do not include `research/active/ergodicity-methods-toolbox/`, its assessments/meetings/assignments, the research branch's root `project-state.md`, or other research-loop state merely because they live on the source branch.

Before merge, rerun the established publication checks on the actual current-main PR candidate:

- `validate_entries.py`: 74/74;
- `mkdocs build --strict`;
- navigation/internal-link resolution;
- control/format-character scan;
- diff audit confirming the intended public change only.

The previous clean gate is strong evidence, but current `main` has advanced since the branch diverged, so the real publication candidate should be checked rather than inferred from an older comparison.

### 3. The unresolved legacy-layer/layout question is not a blocker

Do **not** wait for the principal to settle the broader `docs/entries/` legacy-layout question before publishing the new section.

Meeting 001 deliberately separated the mandates: the new ergodicity-methods section was reopened for the main wiki, while unrelated deprecated IPS material stayed frozen. Meeting 013 likewise continued integrating the new toolbox while leaving the legacy/deprecated layer and directory-layout question unresolved.

Therefore coexistence of the new audited method pages and frozen legacy pages in `docs/entries/` is an accepted interim state for this phase. The legacy-layout question remains a separate future curation decision.

## Operational record

**Decision:** the toolbox research/audit phase is complete, but its outward-facing deliverable is not complete until a scoped publication-only PR lands on `main`.

**Publication mechanism:** publication-only PR from current `main`, not a direct merge of the research branch.

**Legacy dependency:** none. Legacy cleanup/layout remains frozen and must not be bundled into the publication PR.

No files under `docs/` or `mkdocs.yml` are changed by this meeting.