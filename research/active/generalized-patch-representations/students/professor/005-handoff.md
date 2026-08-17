# Assignment 005 handoff

Date: 2026-08-17

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

## Goal

Test whether boundary-complete `d=3` typed bulk patch positivity collapses to a finite binary-style family of zero-length and long-time coefficient inequalities.

## Established

1. Boundary completeness plus typed patch positivity forces the empty-target transfer `K` to be Metzler. In `d=3`, active retyping coefficients must be nonnegative.
2. Hence `e^{tK}` is entrywise nonnegative and every incoming-initial `II/IO` numerator is automatically nonnegative.
3. For an outgoing row `p=(p0,p1,p2)`, zero-length `OO/OI` constraints are
   \[
   p_1,p_2,p_0+p_1,p_0+p_2\ge0.
   \]
   The `OO` families are then automatically nonnegative for all time.
4. The remaining `OI` numerator has the exact physical Markov interpretation
   \[
   p e^{tK}f_b^I=E_b[g(Z_t)],
   \qquad
   g=(p_0,p_0+p_1,p_0+p_2),
   \]
   where `Z` is the physical one-site chain with all neighbours in the reference state.
5. A genuine one-neighbour three-state IPS satisfies every zero-length requirement and every long-time `OI` endpoint requirement, but has an interior negative `OI` numerator.

## Exact witness

Reference-neighbour generator:

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix}.
\]

Typed empty-target transfer:

\[
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

Distinguished outgoing row:

\[
p=(-1/8,9/8,1/4),
\qquad
g=(-1/8,1,1/8).
\]

Required `OI` numerator for incoming terminal type `1`:

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+
\frac{153}{128}e^{-2t}.
\]

Endpoints:

\[
N(0)=1,
\qquad N(\infty)=1/128.
\]

Interior minimum:

\[
e^{-t_*}=13/153,
\qquad
N(t_*)=-1/1224.
\]

All physical one-neighbour rates are nonnegative. Both target labels and both active source types have positive coarse nonempty-target support. The exact verifier checks every other outgoing family in the gate.

## Binary acceptance test

Suppressing type `2` removes the active-retyping condition and returns exactly the canonical binary inequalities from Assignment 004. For the witness subsystem:

\[
u=0,
\quad w=7/4,
\quad c^0(S)=0,
\quad c^1(S)=-9/8,
\]

so

\[
c^0(S)+c^1(S)\le0,
\qquad
w c^0(S)\ge u c^1(S).
\]

No stronger binary condition was introduced.

## Decisive files

- `005a-metzler-incoming-reduction.md`, commit `f8a73319`;
- `005b-outgoing-row-markov-reduction.md`, commit `a4f36bd`;
- verifier `005-three-state-endpoint-obstruction-verifier.py`, commit `fc8c999e`;
- `005c-exact-interior-time-obstruction.md`, commit `3d8778ac`;
- `005d-binary-suppression.md`, commit `ffdb1929`;
- final report `005-three-state-positivity-criterion.md`, commit `027bcbf8`.

## What is stopped

Only the **binary-style endpoint collapse** is stopped. The exact semigroup definition of typed patch positivity remains valid.

Do not infer that no finite spectral test exists. In `d=3`, every generic remaining `OI` numerator has two decaying modes and therefore at most one interior minimum. A separate bounded block could derive an exact spectral critical-point criterion which checks that minimum explicitly.

## What remains out of scope

Applications, convergence consequences, `d>3`, and simultaneous multi-site updates were not started.
