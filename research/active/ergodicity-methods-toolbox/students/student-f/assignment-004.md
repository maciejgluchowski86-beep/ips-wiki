# Student F Assignment 004: analytic and recurrence breadth wave four

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 009, `entry-template.md`, your `003-handoff.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Fill seven currently uncovered analytic/recurrence proof interfaces for the ergodicity-methods toolbox. Breadth is wanted, but do not force a weak entry merely to hit the requested count.

## Targets

1. **Foster--Lyapunov + Harris recurrence/ergodicity.** Find a primary IPS-like or infinite-dimensional interacting-process theorem where a drift condition plus irreducibility/minorization/small-set input actually yields recurrence, uniqueness, or convergence.
2. **Small/petite-set regeneration or Nummelin splitting.** Keep separate from target 1 only if an inspected source makes the splitting/regeneration construction itself load-bearing and gives a concrete interacting-process application. Otherwise substitute another uncovered analytic method and explain why.
3. **Weak-Poincare or super-Poincare relaxation.** The inequality itself must drive nonexponential relaxation and be materially distinct from the existing Liggett--Nash and RFIM large-set-conductance pages.
4. **Spectral profile or evolving sets.** The profile/evolving-set object must be the main proof interface for a spin/particle/Glauber application, not merely a citation to generic finite-chain theory.
5. **Finite-volume to infinite-volume coercivity/exhaustion.** Isolate a theorem/architecture in which uniform finite-volume gap/LSI/coercive estimates are legitimately passed to an infinite-volume IPS/spin semigroup. State the limiting interface explicitly.
6. **Full Cheeger/conductance route.** Find a genuine positive-gap/rapid-mixing spin-system application using a full conductance/isoperimetric lower bound, distinct from the already-live large-set/warm-start method.
7. **KCSM comparison with a simpler refresh/reference dynamics.** The checked source should compare a constrained dynamics to an unconstrained or simpler reference chain in a way that proves relaxation; it must be distinct from the live Kob--Andersen good-block/long-range-Glauber construction.

The previously attempted nonreversible sector/hypocoercive slot is not part of this assignment. Do not repeat that generic source search unless a primary source encountered incidentally changes the evidence.

## Entry standard

For each successful target, create one file under `research/active/ergodicity-methods-toolbox/entries/` using the current staging template. Each entry must contain a self-contained criterion, mechanism, representative application, limitations, and exact primary-source pinpoint with stable URL/DOI/arXiv identifier.

General Markov-chain results qualify only when the entry has a concrete spin/IPS/KCSM/Glauber or closely adjacent interacting-particle application. Historical origin citations may be secondary to the theorem-level checked source, but say so explicitly.

If a target collapses into an already-live proof interface or has no clean primary interacting-process application, **do not pad**. Substitute a genuinely uncovered method from the coverage spine and document the substitution in the handoff.

## Durability

Mandatory: **commit every finished entry immediately as its own substantive commit.** Do not batch the wave. A session/rendering failure should lose at most the current unfinished entry.

Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-f/004-handoff.md` with entry/commit list, source qualifications, taxonomy/substitution decisions, and further uncovered families. Mechanical validation remains the principal/orchestrator's check and is not a mathematical source audit.
