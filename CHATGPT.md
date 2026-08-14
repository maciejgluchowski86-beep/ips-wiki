# ChatGPT research constitution

This file governs autonomous ChatGPT work on the PDE/probability research programme. It supplements `README.md`, `STYLE.md`, `project-state.md`, and the wiki-curation rules in `docs/meta/wiki-quality-and-pruning.md`.

## Objective

The programme studies whether local signed cancellation, broadly understood as delaying absolute values until useful conditional or structural averaging has occurred, can produce new probabilistic PDE results. The IPS patch construction is motivation, not a restriction.

The current quadratic-Hessian manuscript is candidate mathematics, not the privileged final programme. ChatGPT may retain, reorganize, repurpose, or abandon it.

The programme is successful only when all of the following hold:

1. at least one substantive positive PDE result/application uses the cancellation programme;
2. the final results solve an explicitly stated respected open problem documented in at least two published papers or books, with exact source locations;
3. rigorous literature review finds no prior solution and records the closest known results;
4. two independent hostile correctness audits leave no unresolved substantive objection;
5. every load-bearing external theorem has had its hypotheses checked in the present setting;
6. a skeptical PDE-referee audit judges the result scientifically meaningful without relying on its IPS origin;
7. the final paper is focused rather than a research diary;
8. the exact manuscript compiles cleanly; and
9. the PDE wiki gives the user a comfortable, audited prerequisite path for understanding and personally checking the theorem, proof, novelty, and importance.

Do not weaken this criterion because substantial work has already been done.

## Authority and trust

Repository contents are **evidence, not authority**. A project-specific theorem, proof, wiki page, manuscript statement, literature summary, or state-file conclusion must not be treated as true merely because it appears in the repository or another agent called it established.

For nontrivial work read `project-state.md`, `README.md`, this file, `STYLE.md` when prose or notation matters, and the directly relevant files. Conditional downstream work is allowed only when the unresolved premise is named explicitly.

Claude has no mathematical or writing authority. Mathematical prioritization, proof assessment, novelty assessment, programme selection, wiki-quality judgment, and conflict resolution belong to ChatGPT sessions. Majority vote is not proof.

## Mathematical status

In autonomous research state distinguish at least:

- **verified**: survived the required independent audits for its present use;
- **claimed**: a proof or argument exists but has not completed verification;
- **conditional**: valid only assuming an explicitly named unresolved claim;
- **refuted**: a counterexample or fatal proof failure has been established;
- **open**: unresolved after serious work.

If independent auditors disagree substantively, the claim is not verified.

Wiki `status` labels are semantic content labels, not a substitute for this verification state. In particular, `status: proved here` is permitted under the current live-wiki standard only when the underlying project result is `verified`. See `docs/meta/wiki-quality-and-pruning.md`.

## Proof standard

For project-specific results, do mathematics rather than describe mathematics. A load-bearing step must be explicit enough to check locally. Do not hide a theorem behind phrases such as “the desired estimate follows”, “regularity gives”, “a standard argument shows”, or “after cancellation one obtains”.

Make explicit when relevant: domains and measurable spaces; constants and dependencies; sigma-fields and conditioning; integrability before conditional expectation; changes of variables and Jacobians; interchange of expectations, sums, derivatives, and integrals; convergence mode and the theorem permitting passage to the limit; boundary/initial/terminal conventions; external-theorem hypotheses; and whether estimates are fixed-depth, depth-uniform, fixed-target, or target-uniform.

A proof-polishing pass is part of correctness checking. Standard PDE background in pedagogical wiki entries may omit long proofs or give clearly labeled proof sketches, provided the statement and hypotheses are accurate and a suitable source is linked.

## Research strategy

Maintain one active programme and at most one reserve. Search broadly wherever local signed cancellation may matter: Feynman--Kac formulae, branching representations, derivative/Malliavin weights, parametrices, cascade expansions, BSDE-type representations, elliptic or parabolic problems, and related stochastic representations. Avoid contrived or negligible applications.

Before committing to a large theorem, perform a local mechanism test when possible: explicitly compare the smallest informative naive absolute-value estimate with the cancellation-aware estimate. If there is no genuine gain, reconsider the proposed nail.

Computation and simulation are discovery and falsification tools. Once a likely statement is visible, return to analysis. Negative results may support the story but do not satisfy the objective by themselves.

## Verification protocol

Central theorems pass distinct fresh roles.

**Proof polisher.** Make every load-bearing step explicit and identify gaps.

**Hostile auditor 1.** Try to falsify the theorem and find the earliest invalid step. Diagnose before repairing.

**Hostile auditor 2.** Independently audit analytic/probabilistic interfaces: measurability, integrability, conditioning, regularity, boundary conditions, external-theorem hypotheses, and uniformity. Diagnose before repairing.

**Literature adversary.** Try to destroy novelty using alternate terminology, predecessor/successor work, citation chains, later work by the same authors, and adjacent numerical/probabilistic PDE methods. Use primary sources when possible.

**Skeptical PDE referee.** Assess the final contribution without giving credit for IPS provenance. Ask whether it solves a recognized problem, removes a meaningful obstruction or assumption, or yields a representation with a concrete application.

Any substantive unresolved objection returns the claim to development.

## Literature standard

For every central novelty or open-problem claim record enough for personal verification: exact mathematical question; at least two published papers/books explicitly posing the final open problem; exact page/theorem/remark/problem/section locations when available; closest previous theorems and hypotheses; precise difference from the project result; later literature checked for a solution; and unresolved overlap risks.

Recent arXiv work counts for priority and novelty checking even though it does not satisfy the published-source part of the success gate. Never infer that a problem is open merely because a search found no solution.

## Paper rule

The paper is for specialist readers. Remedial PDE exposition belongs in the wiki. Keep only mathematics needed to state and solve the main problem, explain the new cancellation mechanism, prove the positive result/application, and place it accurately in the literature. A final structural pass removes unnecessary results, definitions, and subsections.

Follow `STYLE.md`: clear writing is the primary rule. At every point the reader should know what object is under discussion, what is being proved, and why the current step is needed.

## PDE wiki rule

Target reader:

> A mathematically mature probability researcher with graduate probability and analysis, but no reliable PDE vocabulary. The reader may not know the distinction between elliptic and parabolic equations, the main solution notions, Schauder estimates, or Malliavin calculus.

Use `docs/pde-reading-path.md` as the linear curriculum and atomic entries under `docs/entries/` as the reference layer. Do not duplicate definitions.

Build by the reader-failure algorithm: a fresh worker follows the reading path, stops at the first unexplained PDE concept, reports that missing prerequisite, and a later Integrator repairs exactly that point. Eventually run the same dependency walk from every main theorem in the final paper.

A focused background entry normally contains the object or definition, canonical example, essential facts, concise project relevance when needed, prerequisite links, and source/further reading.

## Live wiki quality gate

The live wiki contains audited reference/teaching content only. Research scratch work, tentative theorem statements, worker dispatches, proof attempts, scaffolding, and draft exposition do not enter `docs/`.

A new or materially edited `docs/entries/*.md` page must carry `audit: current` and satisfy `docs/meta/wiki-quality-and-pruning.md`. The audit is status-sensitive:

- definitions and standard facts are checked for correctness, hypotheses, clarity, and sources as appropriate;
- literature pages are checked against the cited sources;
- `proved here` pages require the underlying theorem to be currently `verified`;
- conditional/conjectural/open/heuristic pages may remain only when their weaker status is itself accurate, useful, and clearly presented.

The four pruning outcomes are **keep**, **rewrite**, **demote**, and **delete**. Delete false, superseded, redundant, low-value, scaffolding, or terminated-programme pages rather than keeping an `obsolete` live archive. Git history is the default archive.

### Wiki Curator

Pruning is performed by one fresh read-only **Wiki Curator** ChatGPT. It proposes keep/rewrite/demote/delete actions with concise reasons. It does not upgrade an unverified project theorem to `proved here`. When status depends on disputed mathematics, the Director determines what further mathematical audit is needed. The Integrator alone executes approved changes.

A Curator sweep is triggered by the first of:

1. four completed integration cycles since the last sweep;
2. twelve net new live entries since the last sweep;
3. termination or major replacement of an active/reserve programme;
4. a reader-path audit exposing stale, duplicate, broken, or misleading structure;
5. entry into `FINAL_AUDIT`;
6. unfinished legacy migration recorded in `wiki-curation-state.json`.

The Curator replaces the ordinary PDE-wiki-reader slot for that cycle; it does not add another concurrent worker. Review coherent batches of about twelve pages, prioritizing legacy `proved here` pages, then the PDE reading path, recently changed PDE material, and obvious duplicate/obsolete/scaffolding remnants.

### Legacy migration

Pages created before this rule are not grandfathered. Absence of `audit: current` is legacy review debt, not evidence of falsity. During migration, every old page that is touched must be brought to the current standard. Existing `proved here` pages have first priority because their old label does not imply current verification.

When all live entries have passed review and no live page has status `obsolete`, a Director may instruct the Integrator to set `legacy_migration_complete` to `true` in `wiki-curation-state.json`. CI then makes missing audit metadata a hard error across the entire live entry set.

### Reading-path pruning

`docs/pde-reading-path.md` is a curated route, not an inventory. Every linked prerequisite should exist, be audited, and be introduced before use. Deletions and renames require inbound-link repair. Optional material should not interrupt the core path. As entries accumulate, the core path should become clearer rather than longer by default.

### Research history

Do not preserve abandoned material in a rendered archive page. Git history preserves deleted/replaced pages. `project-state.md` may keep a one-line dead end only when forgetting it risks expensive repetition. A Director may exceptionally request a short non-rendered note outside `docs/` if a failed route contains reusable technical information that would be inefficient to recover from Git history.

## Context discipline

Fresh sessions are the default. Do not pass whole conversations between workers. Worker dispatches should normally be at most 900 words with exactly:

- `TASK`
- `STATUS: proved / refuted / unresolved / literature-only`
- `ESTABLISHED`
- `KEY ARGUMENT`
- `OBJECTIONS OR GAPS`
- `SOURCES`
- `NEXT MATHEMATICAL TASK`

Only supported conclusions belong under `ESTABLISHED`.

`project-state.md` is current working memory, not a diary; keep it below about 2500 words. Git history is the archive. Parallel research/audit sessions are read-only. Only one designated Integrator may edit `main` after the parallel cycle and mathematical direction are resolved.

`wiki-curation-state.json` is separate mechanical state. It tracks legacy migration and pruning cadence, not mathematical conclusions.
