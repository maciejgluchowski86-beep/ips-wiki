# Student F assignment 012: decide tail-shift agreement of the half-line invariant law

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/014-zero-frequency-response-equals-tail-shift-defect.md`;
- your `011-zero-frequency-boundary-response.md` and verifier;
- `meetings/013-equilibrium-profile-truncates-zero-frequency-response-remains.md`;
- current `state.md` and `proof-spine.md`;
- Student G `assignment-006.md` only for interface awareness.

The scientific target remains the positive rates conjecture for simple IPS.

## What is now accepted

Let `mu=pi_infty^0` be the projective half-line zero-boundary invariant law, with `X_0` nearest the fixed zero boundary and shift

$$
\theta(x_0,x_1,x_2,\ldots)=(x_1,x_2,x_3,\ldots).
$$

For

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m,
$$

you proved and the Professor checked

$$
\boxed{
\Delta_M
=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
}
$$

and

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Hence

$$
\boxed{
\Delta_M\to0
\iff
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
\tag{TS}
$$

You also proved that `(TS)` implies the one-next-segment common-mass truncation bound

$$
\int_0^\infty w(u)
|m_0(\bar\pi_N-\pi_{N-1})(P_u f)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
\]

Thus `(TS)` is now a genuine decision theorem, not merely a reformulation of notation.

A warning: tail triviality of `mu` and `theta mu` separately is **not sufficient**. Two measures may each have a 0--1 tail and still assign different probabilities to the same tail event. The target is tail-shift agreement/asymptotic stationarity itself.

## Objective

Decide `(TS)` at every strict residual point, or refute it at one strict residual point.

This is a bounded viability block. Do **not** move on to a general matrix-product/nonlocal trail norm.

The preferred positive theorem is

$$
\boxed{
\|\theta^M\mu-\theta^{M-1}\mu\|_{\rm TV}\to0,
}
\tag{A}
$$

on the full reindexed half-line, equivalently `(TS)`.

A negative theorem is an explicit strict residual point and tail event `A in T` such that

$$
\mu(A)\ne\mu(\theta^{-1}A).
\tag{B}
$$

If neither direction closes, the assignment must produce a new structural criterion that is materially stronger than restating `(TS)`.

## Preferred finite-window likelihood / entropy route

The most useful next object is the finite-window likelihood ratio between two adjacent far-left windows.

For `M,L>=1`, let

$$
\mu_{M,L}
=\operatorname{Law}_\mu(X_M,\ldots,X_{M+L-1}),
$$

and compare it with

$$
\mu_{M-1,L}
=\operatorname{Law}_\mu(X_{M-1},\ldots,X_{M+L-2}).
$$

All finite-state probabilities are strictly positive. Define the exact likelihood ratio

$$
R_{M,L}
=\frac{d\mu_{M,L}}{d\mu_{M-1,L}}
$$

after identifying the two copies of `{0,1}^L`.

Investigate whether the invariant generator/projective structure yields a recursion, entropy inequality, or martingale for `R_{M,L}` which is uniform in `L` and forces

$$
\sup_L\|\mu_{M,L}-\mu_{M-1,L}\|_{\rm TV}\to0.
$$

A sufficient entropy route would be a bound

$$
\sup_L H(\mu_{M,L}\mid\mu_{M-1,L})\to0,
$$

or the reverse entropy, followed by Pinsker. Do not assume such a bound; derive it from the IPS structure if it is true.

Equally useful is an exact recursion showing that a non-unit likelihood-ratio mode persists at infinity, which would lead to `(B)`.

You are not required to use entropy if another exact route is better. The purpose of this formulation is to force the tail question into finite positive probabilities rather than another vague appeal to mixing.

## Other admissible routes

You may instead prove `(TS)` through one of the following, provided the argument is non-circular:

1. an explicit boundary-influence coupling for **stationary half-line laws** whose disagreement probability on the entire tail tends to zero;
2. a spatial regeneration theorem which directly couples `mu` and `theta mu` beyond a random finite location with probability tending to one;
3. a direct signed Green-kernel cancellation that implies the tail variation vanishes;
4. a proof that every subsequential limit of `theta^M mu` is the same shift-invariant law together with a quantitative argument excluding persistent period/phase oscillation between successive shifts.

Merely proving tightness or existence of subsequential shift-invariant limits is not enough: `(TS)` concerns successive shifts in total variation on the whole remaining tail.

## Anti-circularity

Do not assume:

- the positive rates conjecture;
- a depth-uniform spectral gap or uniform sup-norm mixing theorem;
- extinction of the common-uniform coupling from Student G Assignment 006;
- a scalar local Foster product already refuted in Meetings 010--012;
- that separate tail 0--1 laws imply tail-shift agreement;
- that decay of every fixed finite-window difference implies total-variation decay on the infinite tail without a uniform-in-window estimate.

Do not infer `(TS)` from the decreasing rational diagnostics in your verifier. They are finite-window evidence only.

## Interface with G and route stop condition

The replacement Student G session is redoing Assignment 006 unchanged after the prior session failed before committing its work. Do not depend on any uncommitted G reasoning.

After this assignment and G006 return, the Professor will hold a route-level expected-value review. Therefore do not continue automatically from `(TS)` into a general nonlocal norm construction.

If `(TS)` is proved, state exactly what new input it supplies beyond the one-next-segment estimate already accepted and what remains for repeated signed profiles.

If `(TS)` is refuted, state precisely which common-mass profile-truncation mechanism is thereby closed.

If still unresolved, identify one exact theorem or finite optimization/inequality that would decide it and explain why it is not merely equivalent notation.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/012-tail-shift-agreement.md`

with verifier/certificate code if computation is used.

End with one of:

- `tail-shift agreement proved: ...`;
- `tail-shift agreement refuted at: ...`;
- `unresolved after substantive work; exact tail-shift blocker: ...`.
