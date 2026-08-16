# Audit log

## Principal reset: fixed positive-rates target

Date: 2026-08-16.

The principal fixed the scientific target to the positive rates conjecture for simple IPS and instructed the Professor to prevent circular progress through equivalent reformulations.

## Inherited negative knowledge

From `research/noisy-east-positive-rates`: source-corrected residual chamber on `r11=0`; failure of the one-site long-lived-state criterion there; sharp `5/6` three-site frozen-exterior diagnostic; almost-sure eventual crossing of every fixed finite agreed block under permanently frozen exterior disagreement; closure of the fixed-finite-wall route.

## Meeting 001: exact density/sign information

Meeting: `meetings/001-density-estimates-and-regional-kernel.md`. `state_narrowed: yes`.

Student F `db49c30`: right-conditioned `L^-` insertion estimate after explicit burn-in. Student G `1f41488`: direct transient zero-density, finite-box concentration, and adjacent-`11` suppression estimates.

## Meeting 002: one-cell insertion works; two-cell composition fails

Meeting: `meetings/002-cellwise-insertion-composition-fails.md`. `state_narrowed: yes`.

Student F `d2c6e92`, verifier `cfbcaf5`: one-cell regional integration is positive, but hidden predecessor transfer is negative on sufficiently short cells. Cellwise scaffold positivity closed.

## Meeting 003: live-source contraction

Meeting: `meetings/003-live-source-contraction.md`. `state_narrowed: yes`.

Student F `d0a508c`, verifier `f379cd3`: rightmost live disagreement has childless regeneration and finite-slab regeneration; coupling drift isolates `J_i`; residual-uniform first-generation contraction fails near East.

## Meeting 004: finite-generation clearing and depth obstruction

Meeting: `meetings/004-two-generation-regeneration-and-depth-obstruction.md`. `state_narrowed: yes`.

Student F `893700c`, verifier `5e3c4bc`: every disagreement has coalescence probability at own update at least `q=1-c+a`; finite-depth ordered clearing is positive but certified depth gaps are summable. Finite-generation escalation stops.

## Meeting 005: centered predecessor-trail reduction

Meeting: `meetings/005-principal-trail-reduction-and-all-depth-transfer.md`. `state_narrowed: yes`.

Durable note: `notes/principal-centered-trail-reduction.md`. Canonical predecessor trail, positive vertical factor `e^{-(1-c+a)tau}`, right contribution after final-coin averaging, and all-depth invariant reduction established as working spine. One-generation contraction `(T)` proposed.

## Meeting 006: exact one-step obstruction; block target

Meeting: `meetings/006-one-step-transfer-refuted-block-stack-target.md`. `state_narrowed: yes`.

Principal update `notes/principal-centered-trail-update2.md`. Exact near-East `3/2` and `7/5` one-step obstructions; mass/disagreement decomposition; negative stack-height drift. Meeting 008 later corrects Meeting 006's erroneous claim that `max{c,b-a}Z<1` gives a residual subregion.

## Meeting 007: exposure resolvent and restart bottleneck

Meeting: `meetings/007-student-g-exposure-resolvent-and-restart-bottleneck.md`. `state_narrowed: yes`.

Student G `c7a33b5`, verifier `e20847a`: exact live-exposure child probability and weighted local `J_i` occupation resolvent. Crude global summation fails near East because repeated exposure re-entry is uncontrolled.

## Meeting 008: same-parent restart tail; crude residual region empty

Meeting: `meetings/008-restart-tail-and-empty-supnorm-region.md`. `state_narrowed: yes`.

Student G `0ca3fd1`, verifier `75b700f`: same-parent exposure re-entry count has geometric tail and explicit exponential pgf. Scalar restart/height diagnostic can tend to `16/21<1` near East, but is not a global Foster theorem.

Student F verifier `0755d22`, write-up `3cb6ac9`: throughout the residual chamber `cZ>1` and `c>b-a`; the crude condition `max{c,b-a}Z<1` has no residual solutions.

## Meeting 009: regenerated-mass loss and duration-mode obstruction

Meeting: `meetings/009-regenerated-mass-loss-and-duration-mode-obstruction.md`. `state_narrowed: yes`.

Student F `ac7de96`, verifier `ff3c5d5`:

- uniform regenerated mass loss `|Br_0-c|Z<2/3`;
- nontrivial mass relaxation mode;
- norm-order obstruction: signed duration average gives near-East `3/5`, actual `L^1` factor gives `7/5`;
- contracting height-one signed matrix is diagnostic only;
- first- and second-order static spatial Markov closure fail at `(1/10,3/10,4/5)`.

Meeting 009 recorded G as still in flight; G had returned only after that meeting's working snapshot.

## Meeting 010: exposed-only Foster product refuted; 16-phase reduction

Meeting: `meetings/010-exposed-product-refuted-and-16-phase-foster-reduction.md`. `state_narrowed: yes`.

Student G `4128cee`, verifier commits `bec4dda`, `4586833`:

- Assignment-003 exposed-only global product is false on reachable all-`01` stacks;
- exact tilted drift has positive bulk term linear in stack height and tends to `(H-2)/7` under the old near-East choices;
- same-parent tail survives;
- nearest-neighbour scalar edge-product class reduces exactly to 16 edge phases / 64 triple drifts and a no-positive-cycle/coboundary feasibility problem plus finite boundary inequalities.

## Meeting 011: finite common-mass mode closure refuted

Meeting: `meetings/011-finite-mode-closure-refuted-profile-truncation-target.md`. `state_narrowed: yes`.

Student F `0ca0ef3`, verifier `9c2db13`:

1. The first transient mass mode contracts:
   $$
   \kappa_T=BZ_{\omega+1+b}<1,
   $$
   with exact denominator gap
   $$
   a^2+5ab+a(1-c)+7a+4b(1-c)+6(1-c)>0.
   $$
2. Near East,
   $$
   \kappa_T=1-\frac{13}{3}\varepsilon^2+\frac{38}{9}\varepsilon^3+O(\varepsilon^4).
   $$
3. Exact common-mass transfer is operator-valued and duration-resolved.
4. On an `N`-site interval,
   $$
   L_N^j h_{p_*}(\eta_1)
   =q_*^{-1}B^j\eta_1\cdots\eta_{j+1}+R_j,
   \qquad \deg R_j\le j,
   $$
   so the cyclic mode dimension is at least `N` even at disagreement height zero. Depth-uniform finite linear mode closure is closed.

Operational overlap correction: G's Assignment 005 commits `d6f3a9d` and `3963d86` landed seconds before Meeting 011 was committed but were not seen during composition. A correction is appended to Meeting 011; its mathematical ruling on F is unchanged.

Student F moved to `students/student-f/assignment-010.md`.

## Meeting 012: balanced circulation refutes the 16-phase scalar product class

Meeting: `meetings/012-balanced-circulation-refutes-16-phase-product-class.md`. `state_narrowed: yes`.

Student G:

- write-up commit `d6f3a9d`, `students/student-g/005-16-phase-foster-feasibility.md`;
- exact verifier commit `3963d86`, `students/student-g/005-16-phase-foster-feasibility-verifier.py`.

Professor-checked conclusions:

1. At the strict residual point
   $$
   (a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
   $$
   G gives an explicit normalized rational circulation on 28 of the 64 triple phases.
2. The verifier checks exact spatial flow conservation and exact zero expected exponent change in all 16 scalar edge-weight coordinates, while the exposure-entry flux `R_mu` and changing-update mass `C_mu` are positive.
3. For every positive scalar edge matrix `Q` and every `s>1`, weighted AM--GM gives
   $$
   \sum_e\mu_eG_Q(e)
   \ge C_\mu\left(s^{R_\mu/C_\mu}-1\right)>0.
   $$
4. Any coboundary certificate would force the circulation average to be nonpositive. Therefore the entire nearest-neighbour scalar edge-product/coboundary Foster class is impossible at this strict residual point.
5. The obstruction is repeatable in the bulk, so finite boundary/height/insertion corrections cannot repair the class.
6. Same-parent renewal remains valid. Matrix-product/nonlocal correctors, every finite temporal state, `J` decay, and the conjecture are not decided.

Direction decision: do not enlarge scalar local corrector contexts mechanically. Student G moves to `students/student-g/assignment-006.md` to decide whether the common-uniform disagreement process itself survives from a finite seed near East or instead admits a genuinely nonlocal extinction/regeneration theorem. Student F continues Assignment 010 on common-mass profile truncation.
