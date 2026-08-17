# Assignment 006 handoff

Date: 2026-08-17

Outcome:

**`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`.**

## What is proved

For boundary-complete `d=3`, typed bulk patch positivity has an exact finite necessary-and-sufficient spectral criterion.

Assignment 005 already reduced the problem to outgoing-initial/incoming-terminal (`OI`) numerators after proving:

- `K` is Metzler;
- incoming-initial families are automatic;
- zero-length outgoing conditions are
  \[
  p_1,p_2,p_0+p_1,p_0+p_2\ge0;
  \]
- these make all `OO` families automatic.

For every remaining `OI` descriptor:

### Distinct negative active eigenvalues

If the active spectrum is `-mu,-nu`, `0<mu<nu`, then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}
\]

with

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu},
\quad L=uP_0f,
\quad n_0=uf,
\quad n_1=uKf,
\]

\[
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.
\]

There is at most one interior minimum. It occurs exactly when

\[
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1.
\]

Then

\[
N(t_*)
=L+\frac{\nu-\mu}{\nu}A R^{\mu/(\nu-\mu)}.
\]

All-time nonnegativity is equivalent to zero-length, long-time, and this one critical value when applicable.

### Degenerate cases

- one active zero eigenvalue: one decaying mode, endpoints suffice;
- repeated nonzero diagonalizable active block: one decaying mode, endpoints suffice;
- repeated nonzero Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  with at most one interior minimum and an explicit critical value;
- reducible reference-neighbour chains introduce no new time-dependence class because `K` is similar to a finite-state Markov generator and zero is semisimple.

## Mandatory gates

Verifier: `006-three-state-spectral-verifier.py`, commit `419196b4`.

Negative gate reproduces the Assignment-005 witness:

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224.
\]

Positive gate uses a physically realizable boundary-complete row

\[
p=(-1/8,9/8,3/8)
\]

with `p_0<0`; all its relevant `OI` families are nonnegative for every time. The nontrivial one has

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

## Binary acceptance test

Suppressing type `2` removes the interior-critical branch completely and gives exactly

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical zero-rate clause. No stronger binary condition appears.

## Tractability judgment

The criterion is genuinely finite, not a time scan: each finite local `OI` descriptor requires at most one interior critical evaluation.

It is not generally a polynomial/rational coefficient cone. With algebraic input the generic critical value contains one algebraic power

\[
R^{\mu/(\nu-\mu)}.
\]

That limitation should be retained explicitly; it is the transient information whose removal caused the endpoint failure in Assignment 005.

## Decisive commits

- generic criterion: `e79a94a5`;
- degenerate cases: `96127a9b`;
- exact verifier: `419196b4`;
- finite-usability theorem: `54334311`;
- binary reduction: `93dad82b`;
- final report: `5957a9cf`.

## Next mathematical question

Do **not** start applications yet.

The next bounded question is whether the finite spectral criterion admits a natural coefficient simplification or a structural multi-state subclass in which the critical inequality becomes algebraic or monotone. Assignment 005 already rules out suppressing the interior mode in general.
