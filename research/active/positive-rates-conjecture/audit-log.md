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

Student G:

- commit `0ca3fd1`, `students/student-g/003-restart-count-block-bridge.md`;
- verifier commit `75b700f`, `students/student-g/003-restart-count-verifier.py`.

Student F:

- Phase-A verifier commit `0755d22`, `students/student-f/007-block-mass-disagreement-verifier.py`;
- completed write-up commit `3cb6ac9`, `students/student-f/007-block-mass-disagreement-contraction.md`.

Professor-checked conclusions:

1. **Same-parent restart bundle.** If `N` is the number of exposure entries of one fixed parent disagreement before that parent first coalesces, then
   $$
   P(N\ge n\mid\mathcal F)\le h_1^{n-1}.
   $$
   Hence `N` has the explicit exponential pgf bound
   $$
   E[s^N]\le(1-h_1)s/(1-h_1s)
   $$
   for `1<=s<h_1^{-1}`.
2. **Height algebra.** The accepted stack-clearing minorant gives an exponential height factor `phi(lambda)<1` on an explicit interval. Along the near-East path the algebraic choice `lambda=2`, `s=1+eps^2/4` gives `M(s)phi(2)->16/21<1`. This is a coupling-side restart/height stress factor, not a signed multiplier for global `J_{x,r}`.
3. **Global Foster lift not yet verified.** G's product corrector over all unresolved levels needs an explicit global phase state and transition-by-transition superharmonicity proof, including inactive/exposed/child-alive phases and later new-parent reinfections. The verifier does not check this step.
4. **F correction.** Throughout the entire residual chamber,
   $$
   cZ>1,
   $$
   and `c>b-a`. Therefore the crude condition `max{c,b-a}Z<1` has no residual solutions. The claim in Meeting 006 that it already proves a residual subregion is removed.
5. There is no contradiction between `cZ>1` and `16/21<1`: the first is a raw scalar absolute-value multiplier; the second is a restart/height coupling factor after structural decomposition. Neither decides the bounded-height signed branching kernel.
6. The remaining block theorem splits into two complementary lemmas: a rigorous global restart-corrector Foster reduction (G) and a bounded-height signed mass/disagreement kernel with block spectral radius `<1` or exact obstruction (F).

Next assignments:

- Student F: `students/student-f/assignment-008.md`;
- Student G: `students/student-g/assignment-004.md`.
