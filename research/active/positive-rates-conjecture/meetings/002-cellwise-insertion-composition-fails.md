# Group meeting 002: one-cell insertion works; cellwise composition fails

Date: 2026-08-16

Professor review of:

- Student F, commit `d2c6e92`, `students/student-f/002-regional-insertion.md`;
- exact verifier committed at `cfbcaf5`, `students/student-f/002-regional-insertion-verifier.py`;
- Meeting 001 and the Professor-checked hidden-type insertion lemma from Student F's first report.

Student G is still working on `students/student-g/assignment-002.md`; this ruling is not being held for that return because Meeting 001 explicitly precommitted to treating failure of two-cell composition as decisive for the present cellwise route. G's independent return will be folded into the next meeting.

state_narrowed: yes

Evidence pointer: `students/student-f/002-regional-insertion.md`, especially Sections 3--9, and `students/student-f/002-regional-insertion-verifier.py`.

## Previous bottleneck

Meeting 001 asked whether the minimal scaffold cell becomes insertion-positive after regional integration and, if it does, whether that positivity composes across two consecutive hidden successful interactions.

## Professor verification

Use the complemented canonical convention and set

$$
d=b-a>0,\qquad k=1-c>0,\qquad B=d+c=b+c-a,\qquad \rho=\frac cB.
$$

For the noise-reduced process `L^-`, when the right boundary is fixed to canonical zero, the one-site source chain has rates

$$
0\to1\text{ at rate }1,
\qquad
1\to0\text{ at rate }d.
$$

Therefore its exact semigroup applied to the spin is

$$
\boxed{
K_\Delta(z)
=
\frac1{1+d}
+
\left(z-\frac1{1+d}\right)e^{-(1+d)\Delta}.
}
$$

I independently rederived this from the two-state generator. The same formula follows from the signed-dual regional weight because the active-branch potential and jump rate combine to the survival factor `e^{-(1+d)u}`; no sign-changing normalization is missing.

### One-cell result

Fix the predecessor successful interaction to be source-retaining, so the left predecessor branch is genuinely present. Integrating the left absence region gives the scalar factor

$$
K_\Delta(z)\ge0.
$$

That factor is separated from the source/right region of the current hidden interaction by the scaffold conditioning. Hence the current hidden-type contribution is of the form

$$
K_\Delta(z)\,\mathbb E^-[(B\eta_i-c)R],
$$

with `R>=0` depending only on the source/right regional randomness. After the previously verified burn-in `T_rho`, the conditional insertion lemma makes this nonnegative.

Thus the raw Duhamel left-spin dependence found in Assignment 001 is genuinely removed by the one-cell regional integration. The one-cell test passes.

### Two-cell transfer

For composition, the predecessor interaction cannot be fixed artificially to the source-retaining type. It is itself hidden. Its two types have the same target/predecessor geometry but different source continuation:

- source retained: signed coefficient `+B`, left branch present, regional factor `K_Delta(z)`;
- source removed: signed coefficient `-c`, left branch absent, regional factor `1`.

Therefore the exact signed transfer passed between consecutive cells is

$$
\boxed{
\Psi_\Delta(z)=B K_\Delta(z)-c
=B(K_\Delta(z)-\rho).
}
$$

This is the load-bearing composition formula. Any conditional normalization of the fixed scaffold geometry is positive and does not change its sign.

At lower spin `z=0`,

$$
\Psi_\Delta(0)
=
\frac{B}{1+d}(1-e^{-(1+d)\Delta})-c.
$$

Since

$$
\Psi_0(0)=-c<0
$$

and

$$
\lim_{\Delta\to\infty}\Psi_\Delta(0)
=
\frac{B-c(1+d)}{1+d}
=
\frac{d(1-c)}{1+d}>0,
$$

there is a unique positive crossing time

$$
\boxed{
\tau_*
=
\frac1{1+d}
\log\frac{B}{d(1-c)}.
}
$$

Hence, at **every** residual parameter point,

$$
\boxed{
0<\Delta<\tau_*
\quad\Longrightarrow\quad
\Psi_\Delta(0)<0.
}
$$

The scaffold geometry imposes no positive lower bound on consecutive predecessor time gaps, so these bad cells occur on positive-probability timing events. This is not a null-conditioning artifact.

The numerical verifier at

$$
(a,b,c)=(0.1,0.3,0.8)
$$

checks a strict instance: `Psi_0.1(0)<0`, while an older cell of length `20` has positive transfer, so their product is strictly negative. The arithmetic agrees with the closed formulas; the general obstruction does not depend on this numerical example.

## Ruling: what closes

The following mechanism is closed:

> reveal the last-exit scaffold geometry, keep each successful birth/jump type hidden, integrate the adjacent regional cell, obtain a nonnegative insertion-preserving transfer, and iterate those transfers cell by cell along the predecessor trail.

It fails already at two-cell composition, and the short-cell negative transfer occurs throughout the residual chamber, not only at an exceptional parameter point.

This is the negative outcome pre-specified at Meeting 001. We therefore do **not** continue by adding more cells to the same cellwise positivity argument.

The principal's older last-successful-interaction idea is not disproved in every conceivable coarse form. One could imagine summing random clusters of short signed cells before taking a sign. But that would require a new cluster-cancellation mechanism with its own quantitative estimate. It is not treated as the automatic next step, because doing so would risk exactly the reformulation loop the principal asked the programme to avoid.

## What survives

The following mathematics remains valid and reusable:

1. the corrected three-generator/scaffold boundary algebra;
2. the exact hidden-type insertion `B eta_i-c`;
3. the uniform right-conditioned `L^-` insertion estimate after `T_rho`;
4. the positive one-cell regional kernel `K_Delta`;
5. the deleted-noise trail factor `e^{-a u}`;
6. Student G's direct transient density, finite-box concentration, and adjacent-`11` suppression estimates on the original dynamics.

Items 1--5 no longer form a closing proof spine by cellwise iteration. Item 6 is now the main positive dynamical input because it concerns the actual process and does not depend on the failed composition.

## Next proof direction

The next substantial block should leave cellwise scaffold positivity behind and attack an **actual dynamic disagreement/regeneration episode**, where the exterior source is allowed to evolve and die rather than being frozen. This is materially different from both closed routes:

- unlike the old fixed-wall programme, the source is not held forever;
- unlike the just-closed scaffold route, no sign is required separately for every successful-interaction cell.

A useful first theorem would be a finite-time/slab contraction estimate under the canonical coupling, derived from the actual dynamics and, if useful, from G's transient zero-density/no-`11` estimates. A counterexample showing that those density estimates cannot control a live disagreement episode would also be genuine narrowing.

Student F is routed to this direct-dynamics problem now. Student G should finish the already-running independent Assignment 002; its result will be folded in afterward rather than discarded mid-block.

## Anti-circularity check

The previous live finite statement has been resolved: one-cell insertion is positive, but the exact two-cell transfer has the wrong sign on arbitrarily short cells. That eliminates a concrete proof mechanism. The next route changes the measurable object from signed per-cell transfer to the lifetime/propagation of an actual disagreement source; it is not a relabeling of `Psi_Delta`.
