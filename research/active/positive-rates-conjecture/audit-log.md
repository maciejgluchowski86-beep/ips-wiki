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

Meeting:

`meetings/001-density-estimates-and-regional-kernel.md`

`state_narrowed: yes`.

Student F, commit `db49c30`, reconstructed the hidden-type algebra and proved the right-conditioned `L^-` insertion estimate after explicit burn-in. Student G, commit `1f41488`, proved direct transient zero-density, finite-box concentration, and adjacent-`11` suppression estimates for the original dynamics.

Meeting 001 checked that the two density estimates do not compose naively and set the finite regional insertion/composition test as the next bottleneck.

## Meeting 002: one-cell insertion works, two-cell composition fails

Meeting:

`meetings/002-cellwise-insertion-composition-fails.md`

`state_narrowed: yes`.

Student F:

- commit `d2c6e92`;
- `students/student-f/002-regional-insertion.md`;
- verifier commit `cfbcaf5`, `students/student-f/002-regional-insertion-verifier.py`.

Professor-checked conclusions:

1. With the predecessor successful interaction fixed source-retaining, the left regional factor is the positive zero-boundary `L^-` kernel
   $$
   K_\Delta(z)=\frac1{1+b-a}+\left(z-\frac1{1+b-a}\right)e^{-(1+b-a)\Delta},
   $$
   so one-cell regional integration really removes the raw Duhamel left-dependence and the current hidden insertion is nonnegative after the previously proved burn-in.
2. Under two-cell composition the predecessor is itself hidden, giving exact signed transfer
   $$
   \Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c.
   $$
3. For `z=0`, every residual parameter point has a positive threshold
   $$
   \tau_*=(1+b-a)^{-1}\log\frac{b+c-a}{(b-a)(1-c)}
   $$
   such that `Psi_Delta(0)<0` for every `0<Delta<tau_*`.
4. Scaffold predecessor gaps have no positive lower bound, so cellwise nonnegative insertion cannot be iterated.

Ruling: the cellwise last-exit/scaffold positivity route is closed. A hypothetical coarser random-cluster cancellation would be a new mechanism and is not the automatic next step.

Student F next assignment:

`students/student-f/assignment-003.md` — direct live-disagreement/regeneration episode under the true dynamics.

Student G was still mid-block on Assignment 002 when Meeting 002 was held. Its return will be folded into the next meeting rather than delaying this pre-specified route ruling.
