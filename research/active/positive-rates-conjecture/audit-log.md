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

Meeting 001 checked that the two density estimates do not compose naively and set the finite regional insertion/composition test as the next bottleneck.

## Meeting 002: one-cell insertion works, two-cell composition fails

Meeting: `meetings/002-cellwise-insertion-composition-fails.md`.

`state_narrowed: yes`.

Student F:

- commit `d2c6e92`;
- `students/student-f/002-regional-insertion.md`;
- verifier commit `cfbcaf5`.

Professor-checked conclusions: one-cell regional integration is positive, but the hidden predecessor transfer

$$
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c
$$

is negative on sufficiently short cells at every residual parameter point. The cellwise last-exit/scaffold positivity route is closed.

## Meeting 003: true rightmost-source contraction

Meeting: `meetings/003-live-source-contraction.md`.

`state_narrowed: yes`.

Student F:

- commit `d0a508c`;
- `students/student-f/003-live-disagreement-episode.md`;
- verifier commit `f379cd3`.

Professor-checked conclusions:

1. a rightmost disagreement under the true coupling dies before creating its first child with an explicit positive parameter-point probability;
2. there is an explicit finite-slab childless regeneration event;
3. the coupling drift satisfies
   $$
   \mathcal L^{\rm coup}D_i
   \le-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i;
   $$
4. marginal `11` suppression controls `J_i` only additively;
5. the first-generation contraction degenerates on the East boundary, so zero-rich/no-`11` snapshots cannot yield a residual-uniform first-generation gap.

Next assignment: exact two-generation parent-child episode including reinfection.

## Meeting 004: two-generation regeneration and all-depth obstruction

Meeting: `meetings/004-two-generation-regeneration-and-depth-obstruction.md`.

`state_narrowed: yes`.

Student F:

- commit `893700c`;
- `students/student-f/004-two-generation-episode.md`;
- verifier commit `5e3c4bc`, `students/student-f/004-two-generation-verifier.py`.

Professor-checked conclusions:

1. **Uniform local coalescence.** Every disagreement site, not only a rightmost one, has predictable coalescence intensity at least
   $$
   q=1-c+a>0.
   $$
   This holds for both disagreement orientations and all four pair states at the right neighbour.
2. **Race lemma.** A disagreeing site coalesces before the next ring immediately to its left with conditional probability at least
   $$
   p=\frac q{1+q}.
   $$
3. **Two-generation regeneration.** After a rightmost parent has created its first child, with the prospective grandchild site still agreed,
   $$
   \mathbb P(\text{parent and child clear before grandchild creation}\mid\mathcal F)
   \ge p^2
   =\left(\frac{1-c+a}{2-c+a}\right)^2.
   $$
   The full process retains all reinfections; the proof isolates a successful subevent on which the relevant reinfection clocks do not beat the coalescences.
4. **Near-East diagnostic.** The exact 24-state controlled post-birth chain shows a structured regeneration gap of order `epsilon`, substantially larger than the crude universal `O(epsilon^4)` two-stage event. This is diagnostic rather than load-bearing.
5. **Finite-depth correction.** F's ordered-clearing `p^m` bound is accepted with `m` interpreted as **active-span depth**, not merely current disagreement count. Internal agreed gaps can themselves be infected.
6. **Composition obstruction.** The certified depth-dependent gaps `p^m` are summable, so finite-depth clearing alone does not force extinction of a stack whose ancestry depth keeps increasing.

Ruling: stop finite-depth escalation. The next accepted result must control arbitrary ancestry depth structurally, through a weighted Lyapunov/drift, finite multi-type renewal/branching domination, disagreement-weighted `J_i` estimate, finite summary state, or a rigorous obstruction to such mechanisms.

Next assignment:

- `students/student-f/assignment-005.md` — all-depth disagreement-stack contraction or obstruction.

Student G remains on Assignment 002; its return will be folded into the next meeting.
