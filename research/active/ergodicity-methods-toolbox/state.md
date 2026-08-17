# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

This is a literature-compilation direction. Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/008-second-live-integration-batch.md`.

## Publication status

The live wiki is reopened for this toolbox section only. Unrelated legacy/deprecated IPS pages remain frozen unless separately audited.

All **30** source-audited method entries are now represented in the live wiki:

- `docs/ergodicity-methods.md` is the hub;
- all thirty method pages are under the ordinary article namespace `docs/entries/`;
- `mkdocs.yml` has a top-level `Ergodicity methods` section organized by proof interface;
- every toolbox method page carries `status: literature` and `audit: current`.

The first eighteen passed their post-integration mechanical check. The second batch added the remaining twelve pages and modified only the toolbox hub and navigation relative to pre-batch head `3e99b211`.

The filesystem layout is deliberate: toolbox pages remain in the repository-wide `docs/entries/` namespace. Separation from unaudited legacy material is via the dedicated hub/navigation and audit metadata, not a toolbox-specific directory. A physical reorganization would be a global wiki-curation decision, not a local toolbox exception.

## Workers

- Student F: idle after Assignment 003 and handoff `students/student-f/003-handoff.md` (`9c214623`).
- Student G: idle after Assignment 002 and handoff `students/student-g/handoff-002.md` (`7d5e739`).
- No new assignment is issued until the second live-integration check is reported.

Every finished method entry in future literature waves must still be committed immediately as its own artifact.

## Inclusion and source standard

Include a method when it has a rigorous theorem/criterion/reusable proof architecture, a spin-system/IPS/KCSM/Glauber application or formulation, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete IPS/spin application. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Only `source_status: primary-checked` entries accepted in a Professor source-audit meeting are eligible for live promotion.

`validate_entries.py` checks metadata, headings, source-pinpoint/URL presence, and length only; it does not certify attribution or mathematical correctness. The voter-duality overclaim corrected at `1761b47` remains the explicit reminder that validator success is structural only.

## Current live coverage

### Coupling and local influence

Attractiveness; Dobrushin influence contraction; path coupling; coupling with stationarity/local uniformity; censoring inequalities; dynamical disagreement domination by space-time percolation.

### Spatial mixing and local-to-global transfer

Static disagreement percolation; Dobrushin--Shlosman; spectral independence; finite-size strong-mixing bootstrap.

### Functional inequalities, comparison, and multiscale coercivity

Poincare/spectral gap; LSI/mLSI; discrete Bochner entropy; canonical-path/Dirichlet comparison; block bisection; Lu--Yau recursion; two-scale conservative coarse graining; entropy factorization; Holley--Stroock perturbation; moving-particle comparison; Aldous interchange/exclusion gap reduction; Liggett--Nash relaxation; large-set conductance; KCLG renormalized Glauber comparison.

### Graphical ancestry, duality, and exact sampling

Finite-dual extinction; voter coalescing-walk duality; coupling from the past; clan-of-ancestors perfect simulation; information percolation; East distinguished-zero screening.

The voter page has no uniqueness claim. CFTP, ancestor clans, and information percolation remain distinct proof interfaces. Static and dynamical disagreement percolation remain distinct.

## Required second-batch mechanical check

Run:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

and confirm all thirty live slugs and current-audit metadata, all hub/nav links, the exact second-batch diff against `3e99b211`, and absence of modifications/deletions to non-toolbox `docs/` pages.

## Next uncovered families

After that check, priority gaps include literal block/maximal local coupling, complete-convergence/oriented-percolation block constructions, interface/front regeneration, weighted/Wasserstein coupling, Foster--Lyapunov/Harris recurrence, small-set/Nummelin regeneration with an IPS-like application, weak/super-Poincare and spectral-profile methods, finite-to-infinite graphical/coercive transfer, further KCSM comparison mechanisms, full Cheeger/conductance gap methods with a spin application, and model-specific branching/annihilating duals.
