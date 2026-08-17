# Student G Assignment 005: structured couplings, restarts, and marked discrepancies

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 013, `entry-template.md`, your `004-handoff.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Continue breadth-first graphical/coupling coverage after wave five. This wave uses several concrete source leads rather than reopening the generic boundary-projective or basic-coupling searches that have already failed to expose separate interfaces.

Do not force six entries. Preserve model-specific proof objects when they are the reason the theorem works.

## Targets

1. **Coupling independence / coarse-grained local-to-global coupling for spin systems.** Investigate the coupling-independence framework for general spin systems, with Chen--Feng's work on unbounded-degree spin systems as a source lead. Include it only if the primary proof exposes a reusable coupling object genuinely distinct from Dobrushin influence, spectral independence, block coupling, and ordinary path coupling, rather than merely repackaging one of those live pages.

2. **Sticky coupling for McKean--Vlasov or weakly interacting particle systems.** Use Durmus--Eberle--Guillin--Schuh as a source lead. The characteristic object should be a distance process dominated by a one-dimensional dynamics with a sticky state at zero, yielding long-time convergence and/or propagation of chaos. Keep this distinct from synchronous weighted `W_1`, Hairer asymptotic binding, and reflection coupling.

3. **Componentwise reflection coupling with estimates uniform in particle number.** Investigate weakly interacting mean-field particle systems where approximate reflection is performed componentwise and a specially designed transportation cost yields exponential Wasserstein convergence uniformly in the number of particles. Liu--Wu--Zhang is a source lead. This must be separated from Wang's infinite-dimensional SPDE reflection page: the load-bearing issue here should be many-particle interaction and uniform-in-`N` control.

4. **Essential-hitting/restart complete convergence for a contact-type process.** Find a primary theorem where essential hitting times, break points, repeated restart attempts, or an equivalent survival-conditioned renewal construction drive complete convergence or local convergence on survival. It must be materially distinct from Ma's new two-level contact page, whose second load-bearing step is a forward/backward dual intersection of restartable percolation blocks.

5. **Environment seen from a second-class particle or moving discrepancy.** Find a conservative IPS theorem where the process as viewed from a second-class particle, shock marker, or finite discrepancy has an invariant/ergodic law and that moving-frame environment is the load-bearing long-time object. This must add to, rather than restate, the new exact product-shock/random-walk page.

6. **Regeneration of an actual disagreement front between two coupled copies.** Search for a coupling in which the interface of disagreements between two copies has regeneration times and those renewals prove agreement, an interface limit theorem, or a long-time coupling statement. Keep it distinct from both the physical reactive-front page and the new two-species competition-interface page. If a bounded targeted search again fails to locate a clean source, substitute either a successful-coupling theorem for a structurally different finite dual (labels/internal states/changing size, with coupling rather than extinction decisive) or another source-supported graphical interface exposed during this wave.

## Closed generic searches

Do **not** reopen these without a concrete named primary source:

- generic boundary-uniform dynamic projective coupling;
- generic common/basic graphical coupling.

The previous searches found only already-live spatial screening, finite-speed/coercive transfer, attractiveness, or disagreement mechanisms.

## Entry standard

For each successful target, create one file under `research/active/ergodicity-methods-toolbox/entries/` using the current staging template. State the theorem/criterion, mechanism, representative interacting-process application, limitations, and at least one actually inspected primary source with exact theorem/proposition/lemma/section/page pinpoint and stable DOI/arXiv URL.

Source leads in this assignment are search leads only. Verify their primary theorem chains and reject/merge the target if the proof interface does not survive inspection.

## Durability

Commit every finished entry immediately as its own substantive commit. Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-g/005-handoff.md` listing every entry/commit, source qualifications, substitutions, negative taxonomy findings, and newly uncovered graphical/coupling families. Mechanical validation remains a structural check only.
