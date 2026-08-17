# Student F Assignment 005: analytic, KCM, recurrence, and limiting interfaces

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 012, `entry-template.md`, your `004-handoff.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Fill seven currently uncovered or only partially represented proof interfaces. This wave deliberately mixes general analytic/recurrence methods with several KCM-specific techniques that are important enough to deserve separate pages if the primary literature really uses them as distinct proof mechanisms.

Do not force seven entries. The primary source, not the assignment label, decides whether a target is genuinely distinct.

## Targets

1. **Bootstrap-percolation closure/legal-path criterion for KCM ergodicity or exponential relaxation.** Find a primary theorem where deterministic bootstrap closure/emptying is converted into KCM ergodicity, mixing, or a positive spectral gap/exponential relaxation statement. Isolate the transfer mechanism itself; do not merely restate a model-specific asymptotic theorem.

2. **Long-range constrained Poincare / good-path inequality.** Find a source where a nonlocal or long-range facilitating event with high probability yields a Poincare inequality and is then used to prove relaxation of a KCM or close interacting model. This must be distinct from ordinary block bisection and from the already-live Kob--Andersen renormalized-Glauber comparison.

3. **Matryoshka-doll / nested multiscale renormalisation.** Look for a proof in which a hierarchy of nested good/super-good events or droplets is the load-bearing device allowing one to descend from a macroscopic relaxation scale to microscopic legal dynamics. Keep separate from generic block dynamics only if the nested construction is genuinely the proof interface.

4. **CBSEP or generalized CBSEP auxiliary-process comparison.** Find a primary source where a coalescing/branching exclusion-type auxiliary process is introduced because its mixing/relaxation properties are easier to control and those properties are then transferred to a constrained spin system. The auxiliary process must be load-bearing rather than just motivational.

5. **Artificial Nummelin splitting / manufactured atom.** Include only if an inspected primary source uses Nummelin splitting or an explicitly manufactured regeneration atom in a concrete interacting-particle, interacting-diffusion, interface, or infinite-dimensional Markov application, and the renewal decomposition itself drives recurrence/ergodicity. Do not duplicate the live physical-collapse regeneration page.

6. **Projective/compactness invariant-law argument.** Find a theorem where finite-volume invariant measures, consistent marginals, tightness/compactness, or a projective limit are the main mechanism producing an infinite-volume invariant law and, preferably, uniqueness/ergodicity after an additional argument. The limiting architecture must be explicit enough to stand alone as a method page.

7. **Super-Poincare relaxation.** Find an interacting-process application where a super-Poincare inequality, not merely an ordinary/weak Poincare or Nash inequality under another name, drives quantitative semigroup relaxation. If a targeted primary-source search again yields no clean interacting-process use, substitute a genuinely infinite-lattice Harris/Lyapunov theorem or another uncovered analytic interface and document the negative search result.

Do not repeat the generic nonreversible sector/hypocoercive search from Assignment 003 unless a primary source encountered incidentally changes the evidence.

## Taxonomy constraints

- A bootstrap-percolation criterion is not the same thing as canonical paths merely because legal paths may appear in its proof.
- Long-range constrained Poincare, nested multiscale renormalisation, and CBSEP comparison may occur in the same KCM literature but should be separate only if their checked theorem chains expose separate reusable interfaces.
- Projective compactness is not finite-speed semigroup exhaustion: the former constructs/identifies limiting laws through consistency or compactness, while the latter controls dynamics in growing boxes.
- Super-Poincare must be distinguished explicitly from the live weak-Poincare, Liggett--Nash, and large-set-conductance pages.

## Entry standard

For each successful target, create one file under `research/active/ergodicity-methods-toolbox/entries/` using the current staging template. Give a self-contained criterion, mechanism, representative application, limitations, and at least one actually inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and stable URL/DOI/arXiv identifier.

General Markov-process theory qualifies only with a concrete interacting-process application. Reviews/monographs may guide the search but do not replace theorem-level checking of primary sources where those are reasonably available.

If a target collapses into an already-live proof interface or lacks a clean primary interacting-process application, **do not pad**. Substitute another uncovered source-supported method and explain the substitution in the handoff.

## Durability

Mandatory: **commit every finished entry immediately as its own substantive commit.** Do not batch the wave and do not rely on chat as durable memory.

Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-f/005-handoff.md` with the entry/commit list, source qualifications, taxonomy/substitution decisions, negative searches that should not be repeated, and further uncovered families. Mechanical validation remains the principal/orchestrator's structural check and is not a source audit.
