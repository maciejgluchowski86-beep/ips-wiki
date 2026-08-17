# Group meeting 005: G wave two and F wave three source-audited; integration gate opens

Date: 2026-08-17

Professor review of Student G Assignment 002 and durable handoff `7d5e739`, Student F Assignment 003 and durable handoff `9c214623`, the exact staged entries cited below, the primary-source pinpoints carrying their claims, and the principal's mechanical-validation report.

`state_narrowed: yes`.

## Timing correction

The principal's handoff described F as still mid-wave-three with four entries. The branch had already advanced before this meeting: F completed the assignment with two further entries, `kclg-renormalized-glauber-comparison.md` at `850bffb0` and `large-set-conductance-warm-start.md` at `3aa52a99`, then committed `students/student-f/003-handoff.md` at `9c214623`.

Accordingly there are **30 staged method entries**, not 28, and both F and G are now idle. The reported `Checked 28 entries; 0 failed mechanical validation` remains a valid snapshot at the time it was run, but does not mechanically certify the final two F entries or the metadata correction made in this meeting.

## 1. Student G Assignment 002

All six entries expose distinct proof interfaces and are accepted for later live-wiki integration, subject to one metadata correction described below.

### Clan-of-ancestors perfect simulation

Accepted. Fernández--Ferrari--Garcia's finite-clan condition is the load-bearing criterion: a target window is reconstructed by tracing a finite dependency clan backward in a dominating Poisson process and cleaning it forward. Their branching/oriented-percolation majorant supplies a practical sufficient condition. This remains separate from CFTP and information percolation.

### Censoring inequalities

Accepted. Peres--Winkler's theorem is correctly scoped to monotone spin systems and ordered initial laws: deleting updates cannot improve total-variation distance from equilibrium from the extremal side, and the block-to-single-site use is a transfer device rather than a contraction theorem by itself.

### Coupling with stationarity and local uniformity

Accepted. Hayes--Vigoda replace worst-case contraction by contraction on a high-stationary-mass set, coupling an arbitrary chain to a stationary copy. This is not ordinary path coupling and does not fill the still-uncovered literal block/maximal-local-coupling slot.

### Coupling from the past

Accepted. Propp--Wilson's criterion is backward coalescence of a common random map, yielding an exact stationary sample. The entry correctly separates this from forward mixing and from finite ancestor-clan reconstruction.

### Coalescing-random-walk duality for voter clustering

Accepted **after correction**. Astoquillca's checked theorem classifies extremal stationary voter laws through collision properties of the dual walks. In the recurrent lattice regime the process clusters, but both consensus states remain invariant; this is not uniqueness of the stationary law. Therefore `targets: uniqueness` was too strong and is removed at commit `1761b47`. The checked targets are convergence/clustering and coupling agreement.

Holley--Liggett is retained only as historical attribution, not silently upgraded to an inspected theorem source.

### Dynamical disagreement domination by space-time percolation

Accepted. The checked Gielis--Maes--Vande Velde source explicitly converts basic-coupling discrepancies into oriented space-time connectivity, with both discrete-time PCA and continuous-time cut-and-arrow formulations. This is a dynamical method and remains separate from static van den Berg--Maes disagreement percolation for Gibbs uniqueness. The earlier 1996 Gielis--Maes paper is supporting history/application, not the primary checked pinpoint for this entry.

## 2. Student F Assignment 003

All six entries are accepted for later live-wiki integration.

### Discrete Bochner--Bakry--Emery entropy method

Accepted. Caputo--Dai Pra--Posta give a second-entropy-derivative criterion and a move-pair/Bochner identity that proves mLSI in zero-range and Bernoulli--Laplace examples. This is a method for establishing entropy coercivity, distinct from the generic LSI/mLSI criterion page.

### Two-scale coarse graining for conservative coercivity

Accepted. Menz--Otto split entropy into microscopic fibers and a coarse marginal, prove eventual convexification under renormalization, and lift the coarse LSI back through a two-scale criterion. This is materially different from Lu--Yau's filtration recursion.

### Aldous interchange/exclusion spectral-gap reduction

Accepted. Caputo--Liggett--Richthammer prove exact equality of interchange and random-walk gaps on every finite connected weighted graph, with the symmetric-exclusion gap equality as an exact consequence. This is an exact many-particle spectral reduction, not a congestion comparison.

### Liggett--Nash polynomial relaxation

Accepted. Inglis--Neklyudov--Zegarlinski provide polynomial ergodicity for a conservative infinite particle system with no spectral gap and formulate the associated Liggett--Nash coercive inequalities. The entry accurately records that the paper derives the Nash inequality after the semigroup decay, while the toolbox abstracts the reusable Nash-to-polynomial-decay mechanism.

### Renormalized long-range Glauber comparison for KCLG

Accepted as the authorized substitution for the nonreversible sector/hypocoercive slot. Cancrini--Martinelli--Roberto--Toninelli first create a high-probability renormalized good-block dynamics, prove an auxiliary constrained Glauber gap, and compare its moves back to legal Kob--Andersen motion. The substitution is preferable to forcing a sector-condition entry whose located IPS sources use the condition for fluctuation/hydrodynamic purposes rather than relaxation.

### Large-set conductance and warm-start mixing

Accepted. El Alaoui--Eldan--Gheissari--Piana use weak Poincare/large-set expansion and a Lovasz--Simonovits profile to obtain polynomial mixing from warm starts for RFIM Glauber dynamics. The entry does not claim a uniform Cheeger constant, a positive gap, or worst-case cold-start mixing.

## 3. Integration status

Meetings 002--005 have now source-audited **all 30 staged entries**. The first 18 had already been taxonomically cleared before this meeting; the twelve just reviewed are queued behind them.

No `docs/` or `mkdocs.yml` change is made in this source-audit meeting. The next Professor action is the previously promised bounded live-wiki integration pass for the first 18 entries. **Do not dispatch another F or G literature wave before that integration pass is completed and mechanically checked.** This gives the public layer a clean checkpoint and prevents an ever-growing staging inventory from outrunning curation.

After integration, further waves should preferentially fill genuinely uncovered interfaces rather than densify existing families.

## 4. Next-wave coverage reserved, not yet dispatched

G's reconnaissance identifies high-value graphical gaps: literal block/maximal local coupling; complete-convergence/block constructions via oriented percolation; interface or disagreement-front regeneration; Wasserstein/weighted-metric coupling; finite-volume-to-infinite-volume graphical transfer; a basic/common graphical-coupling synthesis; and model-specific branching/annihilating dual mechanisms beyond voter/contact.

F's reconnaissance leaves complementary analytic gaps: Foster--Lyapunov/Harris recurrence with an IPS-like application; weak or super-Poincare relaxation beyond the present Nash/RFIM examples; spectral-profile/evolving-set methods; a dedicated finite-to-infinite coercivity transfer; additional KCSM comparison with unconstrained refresh dynamics; and a genuinely relaxation-oriented nonreversible sector/hypocoercive theorem if a clean primary IPS source is eventually located.

These are coverage candidates, not assignments yet.

## 5. Required mechanical check

Before live integration, rerun

```bash
python research/active/ergodicity-methods-toolbox/validate_entries.py
```

against the current 30-entry branch. The expected count is 30. This validates structure only; the source-acceptance rulings above are separate.

Current status:

- 30 staged entries source-audited and accepted;
- Student F idle;
- Student G idle;
- no new student assignment issued in this meeting;
- first 18 entries next in the live-integration queue;
- unrelated legacy/deprecated wiki material remains frozen.
