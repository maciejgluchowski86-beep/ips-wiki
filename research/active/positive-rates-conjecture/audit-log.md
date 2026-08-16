# Audit log

## Principal reset: fixed positive-rates target

Date: 2026-08-16

The principal fixed the scientific target to the positive rates conjecture for simple IPS and instructed the Professor to prevent circular progress through equivalent reformulations.

Initial durable files:

- `principal-starting-note.md` — verbatim principal note;
- `state.md` — fixed-target and anti-circularity rules;
- `proof-spine.md` — current source reductions and active proof edges;
- `literature.md` — primary sources and inherited project work;
- `meetings/000-principal-reset.md` — setup meeting.

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
- verifier commit `cfbcaf5`, `students/student-f/002-regional-insertion-verifier.py`.

Professor-checked conclusions:

1. one-cell regional integration gives a positive zero-boundary `L^-` kernel and removes the raw Duhamel left dependence;
2. two-cell composition gives signed transfer `Psi_Delta(z)=(b+c-a)K_Delta(z)-c`;
3. for `z=0`, every residual parameter point has negative transfer on sufficiently short positive cells;
4. scaffold gaps have no positive lower bound.

Ruling: the cellwise last-exit/scaffold positivity route is closed. Student F moved to the true live-disagreement dynamics. Student G remained mid-block on Assignment 002.

## Meeting 003: true rightmost-source contraction

Meeting: `meetings/003-live-source-contraction.md`.

`state_narrowed: yes`.

Student F:

- commit `d0a508c`;
- `students/student-f/003-live-disagreement-episode.md`;
- verifier commit `f379cd3`, `students/student-f/003-live-disagreement-verifier.py`.

Professor-checked conclusions:

1. For a rightmost disagreement `j` with `j-1` agreed, under the true common-uniform coupling, put
   $$
   d=b-a,\qquad q=1-c+a,
   $$
   and
   $$
   D=(b+q)(1+q)-a(1-c).
   $$
   Conditional on every evolving common right-hand history,
   $$
   \mathbb P(\text{first child before source death}\mid\mathcal F)
   \le1-\delta,
   \qquad
   \delta=\frac{q(d+2q)}D>0.
   $$
2. A finite-slab childless regeneration event has probability at least
   $$
   \delta_T=\frac{1-c+a}{1+a}(1-e^{-(1+a)T})>0.
   $$
3. The local coupling generator satisfies
   $$
   \mathcal L^{\rm coup}D_i
   \le-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i,
   $$
   where `J_i` is the high-risk state `D_i=0,D_{i+1}=1,X_i=Y_i=1`.
4. Marginal `11` suppression bounds `E J_i` only additively, so it does not close the disagreement drift.
5. Along `a=eps^2,b=eps,c=1-eps^2`, the childless gap tends to zero and an all-zero/no-`11` local state still transmits a first child with probability tending to one. Thus zero-rich/no-`11` snapshots cannot yield a residual-uniform first-generation contraction.

Ruling: this East degeneration is not route-closing by itself because the target is pointwise on strict positive-rate parameters and the post-first-child dynamics contains additional killing/reinfection effects. The live-disagreement route remains active.

Next assignment:

- `students/student-f/assignment-004.md` — exact two-generation parent-child episode including all child-death and reinfection cycles, with immediate restart/composition test if contraction survives.

Student G remains on Assignment 002; its return will be folded into the next meeting.
