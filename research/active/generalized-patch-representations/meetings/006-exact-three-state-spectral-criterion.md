# Meeting 006: exact three-state spectral criterion

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- generic two-mode criterion `students/professor/006a-generic-two-mode-critical-criterion.md`, commit `e79a94a5`;
- degenerate spectral cases `006b-degenerate-spectral-cases.md`, commit `96127a9b`;
- exact verifier `006-three-state-spectral-verifier.py`, commit `419196b4`;
- finite-usability theorem `006c-finite-spectral-criterion-and-usability.md`, commit `54334311`;
- binary reduction `006d-binary-spectral-reduction.md`, commit `93dad82b`;
- final report `006-three-state-spectral-criterion.md`, commit `5957a9cf`;
- handoff `006-handoff.md`, commit `23488674`.

## Ruling

Assignment 006 ends

**`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`.**

The endpoint-only criterion refuted in Assignment 005 remains refuted. What is now proved is a different statement: retaining the unique possible interior critical point gives a finite necessary-and-sufficient criterion for boundary-complete `d=3` typed bulk patch positivity.

## 1. Generic case

If the active eigenvalues are

\[
-\mu,-\nu,
\qquad0<\mu<\nu,
\]

then every remaining `OI` numerator is

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

The coefficients are obtained without eigenvectors from

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu},
\]

\[
L=uP_0f,
\qquad n_0=uf,
\qquad n_1=uKf,
\]

\[
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.
\]

The only interior-minimum regime is

\[
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1.
\]

Then the unique interior minimum is

\[
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.
\]

Thus zero-length, long-time, and at most one critical value are necessary and sufficient.

## 2. Degenerate cases are also finite

No irreducibility assumption is needed.

Because `K` is similar to a finite-state physical Markov generator, zero eigenvalues are semisimple even for reducible chains.

- one zero and one negative active eigenvalue: one decaying mode;
- repeated negative diagonalizable active block: one decaying mode;
- repeated negative Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  again with at most one interior minimum;
- all-zero active spectrum: constant numerator.

No spectral case requires a continuum of time checks.

## 3. Full finite criterion

Under boundary completeness, typed bulk patch positivity is equivalent to:

1. Metzler retyping conditions
   \[
   K(1,2),K(2,1)\ge0;
   \]
2. for every outgoing row `p`,
   \[
   p_1,p_2,p_0+p_1,p_0+p_2\ge0;
   \]
3. for each remaining `OI` row/terminal pair, its long-time value and at most one explicit interior critical value according to the spectral case.

Incoming-initial and `OO` families are automatic after the first two steps.

## 4. Mandatory gates

The exact verifier uses physical one-neighbour `d=3` rates and Fraction arithmetic only.

It reproduces the negative Assignment-005 witness

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224,
\]

and separately verifies a boundary-complete physically realizable row

\[
p=(-1/8,9/8,3/8)
\]

with `p_0<0` for which every required `OI` numerator is nonnegative for all time. Its nontrivial minimum is

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

Thus the criterion distinguishes failure from genuine nontrivial positivity.

## 5. Tractability judgment

The criterion is finite and materially more usable than the semigroup definition: each local descriptor requires at most one critical evaluation, not a mesh or scan over `t`.

It is **not** generally a purely algebraic coefficient cone. The generic critical value retains the spectral factor

\[
R^{\mu/(\nu-\mu)}.
\]

That limitation is substantive and should not be hidden. Assignment 005 proves that deleting this transient information is invalid in general.

This is nevertheless not `STOP-SPECTRAL-CRITERION-NOT-TRACTABLE`: the exact time optimization has been eliminated and replaced by a finite local calculation.

## 6. Binary acceptance test

Suppressing type `2` leaves one decaying mode, so the interior critical branch disappears. The criterion reduces exactly to the canonical binary patch-positivity inequalities

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause. No stronger binary condition is introduced.

## 7. Direction after this meeting

Applications and convergence remain blocked.

The next mathematical question is narrower than the general semigroup problem:

> Is there a natural non-binary structural subclass or coefficient condition for which the finite three-state critical inequality becomes algebraic, monotone, or otherwise transparent, while retaining exact binary equivalence?

Do not revive endpoint-only criteria and do not replace the exact property by a sufficient cone unless the subclass itself is mathematically natural and the equivalence within that subclass is proved.

No novelty claim is made yet. Literature audit remains downstream of a stable theorem package.
