# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics and literature work live under `research/`; `CHATGPT.md` governs the workflow.

## Active scientific direction

**Ergodicity methods toolbox for spin systems and IPS, transitioning to problem-specific applicability assessment.**

- Branch: `research/ergodicity-methods-toolbox`.
- Workspace: `research/active/ergodicity-methods-toolbox/`.
- Latest meeting: `research/active/ergodicity-methods-toolbox/meetings/016-wave-six-verified-collection-sunset-assessment-phase.md`.
- Assessment protocol: `research/active/ergodicity-methods-toolbox/assessment-protocol.md`.
- Student F: active on Assignment 007.
- Student G: active on Assignment 006.

The principal has ruled that the toolbox is broad enough. **Wave seven is the final literature-collection wave.** After it is audited and integrated, breadth collection stops. The programme then assesses which frozen toolbox methods are most useful for either:

1. one-dimensional FA-1f / East out-of-equilibrium convergence; or
2. the positive-rates conjecture for simple IPS.

## Coverage and publication status

There are **67 source-audited staged entries and 67 live toolbox pages**, and the complete wave-one-through-six public layer has passed structural verification.

The principal/orchestrator reports:

```text
Checked 67 entries; 0 failed mechanical validation.
```

`mkdocs build --strict` exits 0 with no warnings and no broken internal links. The only INFO output consists of unchanged legacy conditions predating this programme.

Completeness is exact: 67 staged entries, 67 promoted pages, 67 hub links, zero unresolved links, no orphan in either direction, every promoted page carries `status:` and `audit:`, and all 164 MkDocs `.md` navigation targets resolve. `git diff origin/main..research/ergodicity-methods-toolbox -- docs/` remains additions-only with zero non-additions.

These are structural checks only. Source/claim acceptance is the Professor audit recorded in Meetings 002--005, 010, 013, and 015.

The directory question remains a principal-level wiki-curation issue and is not reopened here. No public-doc restructuring is authorized during the applicability assessment.

## Entry hygiene

Meeting 015 exposed a structural-validator blind spot: a TeX backslash in one staged entry had been consumed into a control character. The principal/orchestrator subsequently scanned 230 staged/promoted pages for control and Unicode format characters; the toolbox material is clean. A single instance outside this programme remains in frozen legacy material and has been reported separately to the principal.

Future method-entry review uses both a control/format-character scan and visual/diff inspection of TeX backslashes. Control scans cannot detect every lost backslash, for example a silently mangled `\alpha` or `\mu`.

## Final collection wave

Student F Assignment 007 is source-led: asymptotic strong Feller uniqueness; Hörmander/Malliavin propagation if distinct; Swendsen--Wang/FK spectral comparison; entropic Ricci curvature if distinct.

Student G Assignment 006 is source-led: Gray 1982 positive-rates proof architecture; Gray 1986 attractive-spin duality; Toom error/contour expansions; essential hitting times/almost-subadditive contact-process regeneration if distinct.

Returning fewer entries is acceptable. No wave eight of generic collection will be issued.

## Post-wave-seven assessment

After the wave-seven handoffs are source-audited, integrated, and structurally verified, freeze the inventory and issue:

- Student F: complete **FA-1f/East applicability audit** of every frozen toolbox method;
- Student G: complete **positive-rates applicability audit** of every frozen toolbox method;
- hostile cross-review of only the two shortlists;
- Professor synthesis with ranked method priorities and at most two recommended first proof experiments per problem.

The assessment standard is exact-interface matching, not thematic relevance. An actionable method must produce a concrete bridge lemma to a live unresolved object and survive the existing obstruction record.

For positive rates, the authoritative compact obstruction/target record is `research/active/positive-rates-conjecture/programme-established-results.md` and final `state.md` on branch `research/positive-rates-conjecture`. The sharp connected-renewal blocker is the signed two-time boundary-transmission operator on the actual connected orbit; convective disagreement escape, stationary diameter collapse, and shift/tail decay remain alternative live interfaces.

For FA-1f, the assessment uses the unresolved one-dimensional Bernoulli-quench sign/chronology reductions, the closed finite-seed programme, and East's distinguished-vacancy screening as a solved structural benchmark.

## Previous scientific direction

The direct positive-rates proof loop is stopped and archived on branch `research/positive-rates-conjecture`. Its exact obstruction record is now input to the applicability assessment, not an invitation to restart an exhausted architecture under a new name.
