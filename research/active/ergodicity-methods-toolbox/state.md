# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction, not a continuation of the positive-rates proof loop. Breadth is intentional: model-specific methods are in scope.

## Publication target and wiki status

The principal's new instruction explicitly reopens the live wiki **for this toolbox section only**. The previous freeze remains in force for unrelated legacy/deprecated IPS pages unless a separate current audit is requested.

Research drafts do not go directly into `docs/`. Entries are first staged under this workspace, source-checked, and Professor-reviewed. Accepted entries will later be promoted to the live wiki as ordinary audited literature entries under a new top-level MkDocs section `Ergodicity methods`, with one hub page and one concept page per method.

Planned live structure:

- `docs/ergodicity-methods.md` — compact map of the toolbox;
- `docs/entries/<method-slug>.md` — individual method pages;
- `mkdocs.yml` — new top-level `Ergodicity methods` navigation section.

This keeps the new section cleanly separate from deprecated material while respecting the repository's article-first wiki architecture and current admission gate.

## Workers

Student F and Student G are reused for the first literature wave. Their prior mathematical context is useful for recognizing method families and avoiding accidental rediscovery, but repository/project claims are not literature authority. Every entry must be grounded in actual external sources.

- Student F: analytic, functional-inequality, variational, block-dynamics, and KCSM relaxation methods.
- Student G: coupling, graphical, disagreement, influence, duality, and backward-history methods.

At most two sessions remain in flight.

## Durability rule

Every finished method entry is committed immediately as its own durable artifact. Do not batch a survey into one final response. A session freeze should cost at most the current unfinished entry.

## Inclusion standard

Include a method when all of the following hold:

1. there is a rigorous theorem, criterion, or reusable proof architecture in the literature;
2. it proves or is explicitly used to prove at least one target property: ergodicity/uniqueness, convergence to equilibrium, coupling agreement/coalescence, spectral gap/Poincare, log-Sobolev or modified log-Sobolev, quantitative mixing, or extinction/forgetting that implies one of these;
3. there is at least one spin-system/IPS/KCSM/Glauber-type application or the method is itself formulated for such models;
4. the entry can state its hypotheses, mechanism, conclusion, and limitations self-containedly;
5. at least one primary source has been inspected and pinpointed.

Model-specific techniques are explicitly included. General Markov-chain methods are included when an IPS/spin-system application is documented. Mere heuristics, numerical diagnostics, or analogies with no rigorous IPS use are excluded.

## Source standard

Every staged entry must cite at least one inspected primary source with a precise theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. If the method's canonical origin is a general Markov-chain source, also cite a concrete IPS/spin-system application. Secondary surveys and books may be added, but do not substitute for primary attribution when the primary source is available.

Only entries marked `source_status: primary-checked` are eligible for later live-wiki promotion.

## Entry size and format

Staged entries use `entry-template.md`. Target length is 400–900 words; hard ceiling 1200 words excluding front matter and references. Each entry must contain a mathematical criterion/theorem-level statement rather than only prose description.

## Mechanical checking

`validate_entries.py` checks required metadata, headings, source pinpoints/URLs, and length. Passing it certifies only structure, not mathematical correctness or attribution. The Professor remains responsible for source audit before promotion.

## Current work

Opening assignments:

- `students/student-f/assignment-001.md`
- `students/student-g/assignment-001.md`

Latest meeting: `meetings/001-opening-taxonomy-source-standard-and-first-wave.md`.
