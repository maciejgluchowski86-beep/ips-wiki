# Audit log

## Principal reset: fixed positive-rates target

Date: 2026-08-16

The principal fixed the scientific target to the positive rates conjecture for simple IPS and instructed the Professor to prevent circular progress through equivalent reformulations.

## Inherited negative knowledge

From branch `research/noisy-east-positive-rates`:

- source-corrected residual chamber on `r11=0`;
- failure of the one-site long-lived-state criterion there;
- sharp `5/6` three-site frozen-exterior one-attack diagnostic;
- almost-sure eventual crossing of every fixed finite agreed block under a permanently frozen exterior disagreement;
- closure of the fixed-finite-wall route.

## Meeting 001: exact density/sign information

Meeting: `meetings/001-density-estimates-and-regional-kernel.md`.

`state_narrowed: yes`.

Student F, commit `db49c30`, reconstructed the hidden-type algebra and proved the right-conditioned `L^-` insertion estimate after explicit burn-in. Student G, commit `1f41488`, proved direct transient zero-density, finite-box concentration, and adjacent-`11` suppression estimates for the original dynamics.

## Meeting 002: one-cell insertion works, two-cell composition fails

Meeting: `meetings/002-cellwise-insertion-composition-fails.md`.

`state_narrowed: yes`.

Student F, commit `d2c6e92`, plus verifier `cfbcaf5`: one-cell regional integration is positive, but the hidden predecessor transfer is negative on sufficiently short cells. Cellwise last-exit/scaffold positivity is closed.

## Meeting 003: true rightmost-source contraction

Meeting: `meetings/003-live-source-contraction.md`.

`state_narrowed: yes`.

Student F, commit `d0a508c`, verifier `f379cd3`: a rightmost live disagreement has explicit childless regeneration; a finite-slab regeneration event exists; the coupling drift isolates `J_i`; residual-uniform first-generation contraction from zero-rich/no-`11` snapshots fails near East.

## Meeting 004: two-generation regeneration and all-depth obstruction

Meeting: `meetings/004-two-generation-regeneration-and-depth-obstruction.md`.

`state_narrowed: yes`.

Student F, commit `893700c`, verifier `5e3c4bc`: every disagreement site has coalescence intensity at least `q=1-c+a`; the parent-child episode clears before grandchild creation with positive environment-uniform probability; finite-depth ordered clearing is positive but the certified depth gaps are summable. Finite-generation escalation stops.

## Meeting 005: principal centered predecessor-trail reduction

Meeting: `meetings/005-principal-trail-reduction-and-all-depth-transfer.md`.

`state_narrowed: yes`.

Durable note: `notes/principal-centered-trail-reduction.md`.

Working conclusions: the residual centered dual has a canonical predecessor trail with positive factor `e^{-(1-c+a)tau}`; the right contribution is uniformly bounded after final-coin averaging; finite zero-boundary mixing reduces the nonempty-exit term to an all-depth invariant expectation; exact East cancellation holds. Meeting 005 proposed a one-generation centered signed-measure contraction `(T)`.

## Meeting 006: exact depth-two obstruction to `(T)`; block mass/disagreement target

Meeting: `meetings/006-one-step-transfer-refuted-block-stack-target.md`.

`state_narrowed: yes`.

Durable principal update: `notes/principal-centered-trail-update2.md`.

Professor checks confirmed the segmentwise right-killing formula, the exact near-East `3/2` and `7/5` one-step obstructions, the mass/disagreement decomposition, and negative stack-height drift. Meeting 006 also stated that the crude condition `max{c,b-a}Z<1` gives a residual subregion; Meeting 008 later corrects that statement.

## Meeting 007: Student G exposure resolvent and restart bottleneck

Meeting: `meetings/007-student-g-exposure-resolvent-and-restart-bottleneck.md`.

`state_narrowed: yes`.

Student G, commit `c7a33b5`, verifier `e20847a`: every live exposure edge, including non-rightmost disagreements, has an exact killed-chain child probability and weighted `J_i` occupation resolvent. Crude global summation fails near East because repeated exposure re-entry/restart count is uncontrolled. G's local `J_i` is distinct from the global trail quantity `J_{x,r}`.

## Meeting 008: same-parent restart tail and empty crude residual region

Meeting: `meetings/008-restart-tail-and-empty-supnorm-region.md`.

`state_narrowed: yes`.

Student G, commit `0ca3fd1`, verifier `75b700f`: same-parent exposure re-entry count has geometric tail and explicit exponential pgf. The scalar height/restart stress factor can be chosen to tend to `16/21<1` near East, but the global product/phase Foster lift remains unverified.

Student F, verifier `0755d22`, write-up commit `3cb6ac9`: throughout the residual chamber `cZ>1` and `c>b-a`, so the crude condition `max{c,b-a}Z<1` has no residual solutions. The purported easy residual subregion from Meeting 006 is removed.

The remaining block theorem splits into a global restart/Foster phase lemma (G) and a bounded-height signed mass/disagreement kernel (F).

## Meeting 009: uniform regenerated-mass loss and duration-mode obstruction

Meeting: `meetings/009-regenerated-mass-loss-and-duration-mode-obstruction.md`.

`state_narrowed: yes`.

Student F:

- commit `ac7de96`, `students/student-f/008-bounded-signed-kernel.md`;
- verifier commit `ff3c5d5`, `students/student-f/008-bounded-signed-kernel-verifier.py`.

Professor-checked conclusions:

1. **Uniform regenerated mass loss.** With `r_0=1/(1+b)`,
   $$
   |Br_0-c|Z<\frac23
   $$
   at every strict residual parameter point. This is independent of G's Foster premise and upgrades the near-East `2/5` limit to the full chamber.
2. **Mass relaxation is a state variable.** A mass branch has rightmost density
   $$
   r(u)=r_0+(r-r_0)e^{-(1+b)u},
   $$
   so a nontrivial transient mass/reset mode survives between insertions; near East it is order one while the equilibrium centered mode vanishes.
3. **Norm-order obstruction.** Near East,
   $$
   \frac g{|m_\varepsilon|}\left|\int w(u)A_{2,\varepsilon}(u)du\right|\to\frac35,
   $$
   but the actual `J`-compatible quantity is
   $$
   \frac g{|m_\varepsilon|}\int w(u)|A_{2,\varepsilon}(u)|du\to\frac75.
   $$
   Hence duration integration cannot precede the block absolute-value norm.
4. **Height-one signed cancellation is real but diagnostic only.** F's exact fully-regenerated matrix has spectral radius about `0.10325` at `(1/10,3/10,4/5)` and tends to `sqrt(2/5)` near East, but it cannot be iterated as the proof kernel because its duration coordinate has already been integrated.
5. **Static short-word closure fails.** Exact invariant-law determinants refute first- and second-order spatial Markov closure at `(1/10,3/10,4/5)`. This rules out current-spin / two-spin static closure but not a finite temporal reset-history state.
6. **Revised bounded target.** The bounded kernel must be a mode-resolved `L^1(w)` operator retaining mass relaxation/reset-history information until the norm is taken. A scalar Foster return statement alone does not determine this signed kernel.

Student G continues Assignment 004 unchanged. Student F moves to `students/student-f/assignment-009.md`.
