---
title: Wiki quality and pruning
---

# Wiki quality and pruning

The live wiki is a reference and teaching layer, not a research notebook. Its purpose is to contain material that is mathematically reliable at its stated status, clearly written, nonredundant, and useful to a reader following the project. Git history, not the rendered wiki, is the default archive of discarded work.

## Two independent labels

Every live entry uses the existing `status` field to describe the mathematical role of its content and, after current review, an additional field

```yaml
audit: current
```

The two fields answer different questions.

- `status` says what kind of statement the page contains.
- `audit: current` says that a ChatGPT wiki-quality review under the current autonomous protocol has checked that the page is accurate at that status, clear, properly scoped, sourced when appropriate, and worth keeping in the live wiki.

Absence of `audit: current` means **legacy review debt**. It is not evidence that the page is false, but it is not admitted under the current live-wiki standard.

The status `proved here` is now reserved for a project-specific result whose underlying theorem is `verified` under the current research verification protocol. An old `proved here` label does not itself confer verification.

## Admission gate

Research scratch work, tentative theorem statements, worker dispatches, proof attempts, and draft expository pages do not enter `docs/`. They remain in the ChatGPT session until a Director has decided that the material belongs in the project and a designated wiki review has passed it for live use.

A new or materially edited entry may be committed to `docs/entries/` only with `audit: current`. During the legacy migration, touching an old entry therefore brings that entry up to the present standard rather than perpetuating old review debt.

A current audit checks the page at the level appropriate to its status:

- `definition`: the definition and conventions are standard or explicitly project-specific, unambiguous, and linked to prerequisites;
- `standard fact`: the statement and hypotheses are source-checked; long standard proofs may be omitted or sketched;
- `literature`: substantive claims are checked against the cited sources and are not stronger than those sources;
- `proved here`: the underlying project theorem is currently verified, and the wiki presentation matches the verified statement;
- `observation`: the observation itself has been checked and is not being passed off as a theorem or literature fact;
- `conditional`: the page names the unresolved hypothesis on which it depends and does not present the conclusion as unconditional;
- `conjecture` or `open`: the status is accurate, the question is mathematically meaningful, and known obstructions or scope restrictions needed to understand it are stated or linked;
- `heuristic`: the page is useful explanatory material and is unmistakably separated from proof;
- `obsolete`: this is a migration-only status. Once identified as obsolete, the page should be deleted from the live wiki rather than retained as an archive page.

## Pruning decisions

A Wiki Curator proposes exactly one of four actions for each page reviewed.

**Keep.** The page is correct at its stated status, clear, nonduplicative, appropriately sourced, and useful to the reading path or reference layer. Mark or retain `audit: current`.

**Rewrite.** The mathematical content is worth keeping but the exposition, scope, sourcing, dependency links, or organization is not good enough. Rewrite before granting `audit: current`.

**Demote.** The page is useful, but its mathematical status is stronger than the current evidence permits. For example, an old `proved here` entry whose theorem has not passed the current verification protocol may become `conditional`, `conjecture`, `observation`, or another accurate status if the resulting page remains useful and well written. Demotion is not a substitute for correctness: the weaker page must itself pass audit.

**Delete.** Delete pages that are false, superseded, redundant, poorly motivated remnants of terminated programmes, scaffolding, research diary material, or too low-value to justify maintaining. Deletion is preferred to an `obsolete` live page. Git history preserves the old text.

The Curator does not upgrade a project-specific theorem to `proved here`. That requires the normal mathematical verification protocol. When a pruning decision depends on disputed mathematics, the Director decides what further mathematical audit is needed; Claude never decides.

## Sweep schedule

Pruning is continuous at admission and periodic in batches.

A dedicated pruning sweep is triggered by the first of:

1. four completed integration cycles since the last sweep;
2. twelve net new live entries since the last sweep;
3. termination or major replacement of an active or reserve research programme;
4. a reader-path audit finding stale, duplicate, broken, or misleading prerequisite structure;
5. entry into `FINAL_AUDIT`;
6. unfinished legacy migration taking priority under `wiki-curation-state.json`.

A pruning sweep uses one fresh **Wiki Curator** ChatGPT session and replaces the ordinary PDE-wiki-reader slot for that cycle. It does not add a fourth concurrent worker. The Curator should normally review a coherent batch of at most about twelve entries: first legacy `proved here` pages, then entries on the current PDE reading path, then recently changed material, then obvious duplicate/obsolete/scaffolding pages.

The Curator is read-only and returns a concise action list with reasons. A Director resolves any mathematical-status issue. The single Integrator performs the approved rewrites, status changes, deletions, link repairs, and metadata changes on `main`.

## Legacy migration

Entries created before this discipline are not automatically grandfathered. Until `legacy_migration_complete` is set to `true` in `wiki-curation-state.json`, an entry without `audit: current` is legacy debt.

Migration is economical rather than exhaustive in one session. Each pruning cycle reviews a bounded batch. Existing `proved here` pages have first priority because their old labels are incompatible with the current theorem-verification protocol. The PDE reading path has second priority because it is the user's route through the subject.

When every live entry has passed the current gate and no live page has status `obsolete`, the Director may instruct the Integrator to set `legacy_migration_complete` to `true`. At that point CI treats missing audit metadata as an error for the entire live entry set.

## Reading-path discipline

`docs/pde-reading-path.md` is a curated linear route, not an inventory of everything in `docs/entries/`.

A pruning or reader-path pass checks that:

- every linked prerequisite exists and is audited;
- the path introduces concepts before using them;
- deleted or renamed entries have no stale inbound links;
- duplicate entries are merged or one is deleted;
- optional material does not interrupt the core route;
- project-specific pages enter the path only after the background needed to understand their statement and importance.

As the wiki grows, the reading path should become clearer, not longer by default. New pages belong on the core path only when they are genuine prerequisites.

## What preserves research history

The live wiki is not the archive.

- Git history preserves deleted and rewritten pages.
- `project-state.md` may retain a one-line dead end when forgetting it would cause expensive repeated work.
- A Director may exceptionally request a short non-rendered research note outside `docs/` when a failed route contains reusable technical information that cannot be recovered efficiently from Git history.

Do not create a public archive page of abandoned programmes, obsolete scaffolding, or raw research chronology merely to preserve context. The default is to prune it from the live wiki.
