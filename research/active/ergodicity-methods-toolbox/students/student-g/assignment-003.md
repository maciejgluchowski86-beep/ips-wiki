# Student G Assignment 003: graphical and coupling breadth wave three

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 009, `entry-template.md`, your `handoff-002.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Fill seven currently uncovered graphical/coupling proof interfaces. Preserve the distinctions already fixed by the first three waves; do not collapse methods merely because they share a graphical construction.

## Targets

1. **Literal block/local/maximal coupling.** Find a source where several spins or updates are coupled jointly and the joint coupling is genuinely stronger than one-site/path coupling. This must be distinct from Hayes--Vigoda coupling with stationarity/local uniformity.
2. **Block construction / complete convergence via supercritical oriented percolation.** The percolation comparison should establish survival, complete convergence, phase structure, or another long-time theorem by a block construction; do not merge it with the live *subcritical disagreement domination* page.
3. **Interface or disagreement-front regeneration.** Look for a model where renewal/regeneration times of a front/interface are used to prove coupling, convergence, or long-time law.
4. **Wasserstein or weighted-metric contraction/coupling.** Prefer infinite-dimensional spin/IPS-like systems where a weighted distance or Wasserstein contraction proves uniqueness/convergence beyond ordinary finite Hamming path coupling.
5. **Finite-volume to infinite-volume graphical transfer.** Isolate a theorem/architecture where coupling/ancestor estimates uniform in finite boxes pass to an infinite-volume process and yield uniqueness or convergence. The limiting argument must be explicit enough to stand as a method page.
6. **Basic/common graphical-coupling inequality, only if distinct.** Include this only if an inspected primary source provides a reusable theorem or inequality not already covered by attractiveness, path coupling, censoring, CFTP, or disagreement percolation. If it is merely a synthesis of those pages, substitute another uncovered graphical method.
7. **Model-specific branching/annihilating/coalescing dual mechanism beyond current contact/voter pages.** The duality must reduce a relaxation/ergodicity/clustering problem through a distinct reaction mechanism, not simply restate finite-dual extinction or voter coalescence.

## Taxonomy constraints

Keep these live distinctions intact unless the primary sources themselves force a correction:

- CFTP = backward coalescence of a random map;
- clan of ancestors = finite backward dependency graph and forward reconstruction;
- information percolation = surviving histories allowed, sparse initial-information clusters controlled;
- static disagreement percolation = Gibbs boundary influence;
- dynamical disagreement percolation = space-time coupled disagreement propagation;
- voter duality = coalescing lineages, not extinction.

## Entry standard

For each successful target, create one file under `research/active/ergodicity-methods-toolbox/entries/` using the staging template. Give the criterion/theorem, mechanism, representative application, limitations, and at least one actually inspected primary source with exact theorem/proposition/lemma/section/page pinpoint and stable URL/DOI/arXiv identifier.

Model-specific methods are explicitly desired. General Markov-chain coupling results need a concrete spin/IPS/Glauber application. If a target is not genuinely distinct or lacks a clean primary application, **do not pad**; substitute a source-supported uncovered graphical method and explain the substitution.

## Durability

Mandatory: **commit every finished entry immediately as its own substantive commit.** Do not batch the seven entries and do not rely on chat as the durable record. A rendering failure should cost at most the current unfinished entry.

Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-g/handoff-003.md` with entry/commit list, source qualifications, taxonomy/substitution decisions, and further uncovered families. Mechanical validation is structural only and remains the principal/orchestrator's check.
