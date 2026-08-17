# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent Glauber-type models.

Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/009-second-integration-verified-wave-four-opened.md`.

## Publication status

All **30** source-audited entries from the first three waves are live:

- `docs/ergodicity-methods.md` is the proof-interface hub;
- all thirty pages are ordinary articles under `docs/entries/`;
- `mkdocs.yml` has the dedicated top-level `Ergodicity methods` section;
- every toolbox page carries `status: literature` and `audit: current`.

The principal mechanically verified the completed second integration: all 30 staged slugs are live, all hub links resolve, hub coverage equals the staged inventory, current-audit metadata is complete, no legacy/deprecated page was modified or deleted, and every MkDocs entry target resolves. This is structural publication checking only; source and claim-scope acceptance remain the Professor audits in Meetings 002--005.

The directory question is closed for this programme. Toolbox pages remain in the repository-wide `docs/entries/` article namespace. Reader separation is supplied by the dedicated hub/navigation and audit metadata. A future repository-wide namespace migration may move them, but no toolbox-specific restructuring is planned.

## Workers

- Student F: **active** on `students/student-f/assignment-004.md`, analytic/recurrence breadth wave four.
- Student G: **active** on `students/student-g/assignment-003.md`, graphical/coupling breadth wave three.

Every finished method entry must be committed immediately as its own substantive commit. Students stage under this research workspace and do not edit `docs/` or `mkdocs.yml`.

## Inclusion and source standard

Include a method when it has a rigorous theorem/criterion/reusable proof architecture, a spin-system/IPS/KCSM/Glauber application or formulation, and a self-contained statement of hypotheses, mechanism, conclusion, and limitations. General Markov-chain methods require a concrete interacting-process application. Mere heuristics and numerical diagnostics are excluded.

Every staged entry must cite at least one actually inspected primary source with an exact theorem/proposition/lemma/section/page pinpoint and a stable URL/DOI/arXiv identifier. Historical attribution may be separate from the theorem-level checked source. Only `source_status: primary-checked` entries accepted in a Professor source-audit meeting are eligible for live promotion.

`validate_entries.py` checks structure only. The voter-duality correction at `1761b47` remains the standing example that validator success does not certify truth or attribution.

## Wave-four targets

### Student G

Literal block/maximal coupling; supercritical oriented-percolation block/complete-convergence constructions; interface/front regeneration; Wasserstein/weighted-metric coupling; graphical finite-volume-to-infinite-volume transfer; a genuinely distinct common graphical-coupling theorem if one exists; and a model-specific branching/annihilating/coalescing dual beyond the current contact/voter examples.

### Student F

Foster--Lyapunov plus Harris recurrence; small/petite-set or Nummelin regeneration if genuinely distinct; weak/super-Poincare relaxation; spectral-profile/evolving-set methods; finite-volume-to-infinite-volume coercivity transfer; full Cheeger/conductance gap or rapid-mixing methods; and KCSM comparison with a simpler/unconstrained reference dynamics distinct from the live Kob--Andersen renormalized route.

The previously attempted nonreversible sector/hypocoercive slot is not reassigned: one serious search found no clean relaxation-oriented IPS primary source, so repeating it generically would encourage padding.

If an assigned family collapses into an existing proof interface or lacks a clean primary application, the student should substitute another uncovered method and document the reason rather than manufacture an entry.

## Current live coverage

Thirty methods are live across coupling/local influence, spatial mixing/local-to-global transfer, functional inequalities/comparison/coercivity, and graphical ancestry/duality/regeneration. CFTP, ancestor clans, and information percolation remain distinct; static and dynamical disagreement percolation remain distinct; voter coalescence is not uniqueness.

## Next Professor action

Source-audit the first completed wave-four handoff before issuing any further assignment on that student lane. After enough accepted entries accumulate, integrate them in another bounded quiet batch and repeat the structural publication checks.
