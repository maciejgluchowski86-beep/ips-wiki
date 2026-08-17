# Group meeting 017: wave seven source-audited; collection frozen; applicability assessment dispatched

Date: 2026-08-17

Professor review of Student F Assignment 007 and handoff `c5ac147`, Student G Assignment 006 and handoff `8c29ca6`, all seven staged wave-seven entries, and the primary-source theorem chains carrying their claims.

Before Professor integration, the principal/orchestrator reported:

- 74 staged entries;
- `validate_entries.py`: 74 checked, 0 failures;
- control/format-character scan clean across all 74 staged entries;
- neither student touched `docs/` or `mkdocs.yml`;
- the `docs/` gate against main still had zero non-additions.

These are structural observations only.

`state_narrowed: yes`.

## 1. Ruling

All **seven** staged wave-seven entries are accepted and promoted after one semantic metadata correction.

Student F accepted entries:

1. `asymptotic-strong-feller-support-uniqueness.md` — `d6e9d72`;
2. `hormander-malliavin-asf-semilinear-spde.md` — `c0d4067`;
3. `swendsen-wang-heat-bath-kernel-comparison.md` — `2d36a9a`;
4. `entropic-ricci-weak-interaction-perturbation.md` — `db0f8a8`, metadata correction at `3d1a151`.

Student G accepted entries:

1. `one-dimensional-edge-coalescence-positive-rates.md` — `2dddd6a`;
2. `toom-error-graph-expansion-pca.md` — `79c3a08`;
3. `essential-hitting-time-almost-subadditive-growth.md` — `6a169bf`.

The final source-audited inventory is therefore **74 distinct method pages**.

## 2. Scope correction

`entropic-ricci-weak-interaction-perturbation.md` was staged with target `log-sobolev`. The source consequence used by the page is a **modified log-Sobolev inequality**, together with Poincare and transport consequences, not a classical logarithmic Sobolev inequality. The staging metadata was narrowed to `modified-log-sobolev` at `3d1a151`. No body theorem or mechanism changed.

No other theorem-strength or taxonomy correction was needed.

## 3. Student F source audit

### Asymptotic strong Feller support uniqueness

Accepted. Hairer--Mattingly's ASF criterion is a distinct invariant-support interface: asymptotic smoothing prevents distinct ergodic invariant measures from sharing an ASF support point, and a common accessible support point gives uniqueness. The page correctly does not infer existence or a quantitative mixing rate from ASF alone.

### Hörmander--Malliavin propagation to ASF

Accepted as distinct from the preceding page. The 2011 architecture controls projected Malliavin covariance using bracket generation and nonadapted Wiener-polynomial estimates, while parabolic dissipation removes unresolved high modes. This is a verification mechanism for asymptotic smoothing, whereas the 2006 ASF page is the abstract uniqueness criterion that consumes such smoothing.

### Swendsen--Wang / heat-bath kernel comparison

Accepted. Ullrich's proof uses the Edwards--Sokal joint representation, conditional Markov operators, the `P_HB P_SW P_HB` sandwich, and pointwise kernel comparison. It does not simulate reference moves by target paths and therefore remains distinct from canonical-path/congestion comparison.

### Entropic Ricci weak-interaction perturbation

Accepted after the MLSI metadata correction. The reusable object is entropy convexity in the discrete transport geometry, with a weak-interaction defect criterion for positive curvature. The source itself connects this to a Bochner Hessian inequality, so overlap with the live discrete-Bochner page is real and should be explicit; nevertheless the transport-geometric curvature criterion and its downstream transport consequences are a distinct interface.

## 4. Student G source audit

### Gray 1982 one-dimensional edge coalescence

Accepted. This page is not another generic attractiveness entry. Attractiveness supplies the extremal common graphical construction; Gray's additional one-dimensional mechanism is the ordered family of half-line edge processes, noncrossing/coalescence, propagation of agreement between suitable edges, escape of surviving edges from fixed windows, and a final local positive-rate repair giving block agreement. This is exactly the extra architecture that closes upper/lower extremal equality in the attractive/repulsive classes.

The hypotheses remain substantive: periodicity, nearest-neighbour structure, and attractiveness or repulsiveness. The page does not claim the full positive-rates conjecture.

### Toom error-graph expansion

Accepted. The proof object is a reconstructed space-time history of actual update errors attached to bad spins inside a backward influence expansion. Toom erosion forces enough errors relative to graph size for low-noise weights to beat graph entropy. This is distinct from disagreement percolation and the theorem is correctly stated as phase-specific convergence/correlation decay rather than global uniqueness.

### Essential hitting times and almost-subadditive regeneration

Accepted as adjacent long-time-growth methodology. Conditioning on survival is repaired by regenerating at an infection whose descendants survive forever; quantitative control of the subadditivity defect then feeds an almost-subadditive ergodic theorem and a shape result. This is distinct from the live complete-convergence renewal page, where renewal plus steering is used to classify the long-time mixture.

## 5. Gray 1986 source-access hold

Student G did **not** stage Gray, *Duality for General Attractive Spin Systems with Applications in One Dimension* (1986). It could verify official metadata and the abstract but could not inspect the primary full theorem/proof text at the programme's exact-pinpoint standard.

Professor endorses that decision.

This is:

- not a negative taxonomy ruling;
- not a merger into Gray 1982;
- not evidence of redundancy;
- not a live collection gap, because the principal has ended breadth collection.

If a readable primary full text later becomes available and the principal explicitly reopens the source, it may be audited then. It is not part of the frozen 74-method inventory.

## 6. Public integration and collection freeze

All seven accepted pages were promoted with `status: literature` and `audit: current`. They were integrated into the existing proof-interface hub and navigation rather than placed in a wave-specific bucket.

A GitHub comparison from the wave-six verified baseline `cedd415` to the integrated branch shows, in the public layer:

- exactly **7 added** method pages under `docs/entries/`;
- `docs/ergodicity-methods.md` modified;
- `mkdocs.yml` modified;
- no other public `docs/` path changed.

The final breadth inventory is now **frozen at 74 source-audited live methods**. There will be no wave eight and no further generic gap-filling search under the present principal direction.

The principal/orchestrator should run the final structural publication gate on the integrated 74-page layer:

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
mkdocs build --strict
```

plus exact staged/live/hub completeness, `status:`/`audit:` metadata, nav-target resolution, additions-only legacy safety, and the control/format-character scan. Until that report, the 74 pages are source-audited and live, but the final 74-page layer is not yet recorded as mechanically verified.

## 7. Validator hygiene ruling

The principal/orchestrator offered to extend `validate_entries.py` to implement the entry-template hygiene rule. Professor ruling:

- **hard failure** for actual disallowed control or Unicode format characters in staged entry text;
- ordinary structural whitespace required by Markdown must remain allowed;
- do **not** hard-fail heuristic guesses that a TeX backslash may have disappeared, because commands such as `alpha` or `mu` after a lost backslash leave no mechanically reliable signature and false positives would be unavoidable;
- visual/diff inspection of mathematical backslashes remains part of source/editorial review.

The principal/orchestrator may implement this bounded validator extension without changing unrelated validator behavior.

## 8. Applicability phase dispatched

The post-collection protocol in `assessment-protocol.md` is now active.

Student F is assigned `students/student-f/assignment-008.md`: complete 74-method applicability audit for one-dimensional FA-1f / East off-equilibrium convergence, producing `assessment/fa1f-east-method-audit.md` with A/B/C/X/N dispositions, at most six ranked A/B candidates, explicit bridge lemmas, obstruction avoidance, and cheapest falsification tests.

Student G is assigned `students/student-g/assignment-007.md`: complete 74-method applicability audit for the positive-rates conjecture, producing `assessment/positive-rates-method-audit.md` under the same standard and tying every A/B method to the signed boundary transmission, convective disagreement escape, stationary diameter collapse, shift/connected-tail decay, or a genuinely different architecture.

Assignment commits:

- F008: `779dece`;
- G007: `8d54887`.

After both audits return, the next phase is hostile **cross-review of the shortlists only**, followed by Professor synthesis. There is no intervening literature collection wave.

## Current status

- collection complete and frozen: 74 source-audited live methods;
- final 74-page structural publication gate pending;
- Student F active on F008 FA-1f/East applicability audit;
- Student G active on G007 positive-rates applicability audit;
- public docs taxonomy/navigation will not be restructured while the principal-level directory question remains open.
