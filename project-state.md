# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Principal target: compile a broad, concise, self-contained, source-checked toolbox of rigorous methods used to prove ergodicity/uniqueness, convergence to equilibrium, coupling agreement, positive spectral gap, log-Sobolev inequalities, quantitative mixing, or closely related relaxation statements in spin systems, IPS, KCSM, Glauber-type and adjacent interacting models.
- Breadth is intentional; model-specific methods are in scope.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/014-wave-five-structural-verification.md`.
- Student F: active on Assignment 006.
- Student G: active on Assignment 005.

## Coverage and publication status

There are **57 source-audited staged entries and 57 live toolbox pages**, and the complete wave-one-through-five public layer has passed structural verification.

On the integrated tree at `aa28743`, the principal/orchestrator reports:

```text
Checked 57 entries; 0 failed mechanical validation.
```

`mkdocs build --strict` exits 0 with no warnings and no broken internal links. The only INFO output consists of seven pre-existing legacy pages absent from navigation and one pre-existing legacy absolute-link note on the coarsened-patches page.

Completeness is exact: 57 staged entries, 57 promoted pages, 57 hub links, zero unresolved links, no promoted page missing from the hub, and no hub link without a page. Every promoted toolbox page contains `status:` and `audit:` metadata. All 154 MkDocs `.md` navigation targets resolve to real files.

Legacy safety passes: `git diff origin/main..research/ergodicity-methods-toolbox -- docs/` is additions-only with zero non-additions. The wave-five public layer consists of thirteen added method pages plus modifications confined to `docs/ergodicity-methods.md` and `mkdocs.yml`.

These are structural publication checks only. Source/claim acceptance is the Professor audit recorded in Meetings 002--005, 010, and 013.

The directory question remains a principal-level wiki-curation issue and is not reopened here. Toolbox pages continue to live in `docs/entries/` alongside frozen legacy material, with reader separation supplied by the dedicated hub/navigation and audit metadata.

## Active breadth wave

Student F Assignment 006 covers a full Cheeger/conductance positive-relaxation spin theorem, one bounded spectral-profile/evolving-set search, infinite-system Harris/Lyapunov ergodicity, exact projective-consistency invariant-law construction, hierarchical renormalisation-group spectral-gap recursion, and constrained-to-unconstrained refresh comparison or a source-supported substitute.

Student G Assignment 005 covers coupling independence, sticky coupling, particle-number-uniform componentwise reflection coupling, essential-hitting/restart complete convergence, moving-frame invariant laws seen from second-class particles, and actual disagreement-front regeneration, with a structured-finite-dual or other source-supported graphical substitution if needed.

Closed generic searches are not repeated absent named new evidence: artificial Nummelin splitting in interacting systems, generic nonreversible sector/hypocoercive IPS relaxation, generic boundary-uniform dynamic projective coupling, and generic common/basic graphical coupling.

## Previous scientific direction

The positive-rates conjecture proof loop has been stopped by the principal. Its archive remains on branch `research/positive-rates-conjecture`; `research/active/positive-rates-conjecture/programme-established-results.md` is the concise established-results summary there. The conjecture itself remains open.
