# Group meeting 016: wave six mechanically verified; collection sunset and applicability phase queued

Date: 2026-08-17

The principal/orchestrator supplied the post-Meeting-015 structural report and a new programme direction from the principal.

`state_narrowed: yes`.

## 1. 67-page structural gate

The integrated 67-page layer passes the complete structural publication gate:

- `validate_entries.py`: 67 checked, 0 failures;
- `mkdocs build --strict`: exit 0, no warnings, no broken internal links;
- only the unchanged pre-existing legacy INFO conditions remain;
- completeness: 67 staged, 67 promoted, 67 hub links, zero unresolved, no orphan in either direction;
- every promoted toolbox page has `status:` and `audit:`;
- all 164 MkDocs `.md` navigation targets resolve;
- `git diff origin/main..research/ergodicity-methods-toolbox -- docs/` remains additions-only with zero non-additions.

This is structural only. The mathematical/source authority of the 67 methods remains the Professor source audit recorded through Meeting 015.

Therefore the complete **67-page wave-one-through-six toolbox layer is source-audited, live, and mechanically verified**.

## 2. Entry-hygiene failure mode

The Professor's wave-six source audit found a vertical-tab control character in the hierarchical-RG staging entry where a literal TeX `\varepsilon` was intended. The previous structural validator did not test this class of corruption.

The principal/orchestrator has now scanned all 230 staged/promoted pages it checked for control and Unicode format characters. The toolbox material is clean. One control byte was found only in a frozen legacy page outside this programme and has been reported separately to the principal; this programme does not edit it.

The important durable lesson is broader than control-character scanning: TeX backslashes can be consumed as host-language escape sequences. Commands beginning with `b`, `v`, `f`, `r`, `t`, `n`, or `a` may leave a detectable control character; other commands such as `\alpha` or `\mu` may simply lose the backslash without leaving a control byte. Future entry review therefore requires both a control/format scan and visual/diff inspection of mathematical backslashes when text has passed through code or API string literals.

## 3. Principal phase change

The principal has ruled that the toolbox is sufficiently broad. **Wave seven is the final collection wave.** It has already been dispatched as F007/G006 and is allowed to finish under Meeting 015.

After wave seven lands:

1. source-audit and integrate only the entries that pass the existing standard;
2. run the final structural publication gate on that frozen inventory;
3. stop breadth collection;
4. turn the programme to assessing which toolbox methods are most useful for either:
   - one-dimensional FA-1f / East out-of-equilibrium convergence; or
   - the positive-rates conjecture for simple IPS.

No further generic gap-filling wave is authorized.

## 4. Assessment design

The Professor's protocol is recorded in `assessment-protocol.md`.

The key rule is that applicability is judged against **exact unresolved objects**, not thematic similarity. For positive rates, candidates must contact the signed boundary-transmission/connected-renewal blocker, convective disagreement escape, stationary diameter collapse, shift/tail decay, or supply a genuinely different architecture that bypasses them. Exact no-go results from the stopped programme are hard evidence against renamed versions of exhausted routes.

For FA-1f/East, the primary benchmark is the unresolved one-dimensional all-density Bernoulli quench, with the chronology/sign reductions and the closed finite-seed programme used as obstruction records and East used as a solved screening benchmark.

After wave seven, the intended first assessment dispatch is:

- Student F: complete FA-1f/East applicability audit of the frozen toolbox;
- Student G: complete positive-rates applicability audit of the frozen toolbox;
- then hostile cross-review of only the shortlists;
- then Professor synthesis with at most two recommended first proof experiments per problem.

No `docs/` restructuring is part of this phase. The separate principal-level directory question remains open and untouched.

## Current status

- 67 source-audited live methods, mechanically verified;
- F007/G006 active and explicitly the final breadth wave;
- post-wave-seven applicability protocol durable at `assessment-protocol.md`;
- next Professor action: audit wave seven when it lands, freeze the final method inventory, then issue the two problem-specific applicability assignments.
