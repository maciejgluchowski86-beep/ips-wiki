# Meeting 005: three-state endpoint criterion is obstructed by an interior-time dip

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- `students/professor/005a-metzler-incoming-reduction.md`, commit `f8a73319`;
- `005b-outgoing-row-markov-reduction.md`, commit `a4f36bd`;
- exact verifier `005-three-state-endpoint-obstruction-verifier.py`, commit `fc8c999e`;
- `005c-exact-interior-time-obstruction.md`, commit `3d8778ac`;
- `005d-binary-suppression.md`, commit `ffdb1929`;
- final report `005-three-state-positivity-criterion.md`, commit `027bcbf8`;
- handoff `005-handoff.md`, commit `4710ddf9`.

## Ruling

Assignment 005 ends

**`STOP-NO-FINITE-ENDPOINT-CRITERION`.**

The stop is deliberately narrow. The exact semigroup definition of typed bulk patch positivity from Assignment 004 remains valid. What is refuted is a direct three-state analogue of the binary theorem in which zero-length and long-time coefficient inequalities alone control every patch length.

## 1. Boundary completeness makes the interior transfer Metzler

For the physical reference-neighbour rates `q_xy`,

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix}.
\]

Short `IO` patches between distinct active types force

\[
q_{21}\ge q_{01},
\qquad
q_{12}\ge q_{02}.
\]

Together with physical deletion coefficients, every off-diagonal entry of `K` is nonnegative. Hence `K` is Metzler and `e^{tK}` is entrywise nonnegative.

Therefore all incoming-initial `II/IO` families are automatic.

## 2. Outgoing rows reduce to one Markov sign problem

For an outgoing row

\[
p=(p_0,p_1,p_2),
\]

zero-length boundary completeness forces

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0.
\]

The `OO` families then remain nonnegative for all time by Metzler positivity.

Define

\[
g=(p_0,p_0+p_1,p_0+p_2).
\]

If `Q` is the physical one-site generator with neighbours fixed in the reference state, the indicator-basis evaluation matrix gives

\[
R K^T=Q R,
\]

and hence

\[
p e^{tK}f_b^I=E_b[g(Z_t)].
\]

Thus only `OI` can still fail.

## 3. Exact interior-time counterexample

The decisive physical reference generator is

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix},
\]

with typed transfer

\[
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

The one-neighbour rate table in `005c` is physically nonnegative at all three neighbour states and supplies both typed target modes with positive coarse hazards from both active source types.

For one outgoing row,

\[
p=(-1/8,9/8,1/4),
\qquad
g=(-1/8,1,1/8).
\]

For incoming terminal type `1`,

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

The endpoints are strictly positive,

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

but

\[
e^{-t_*}=13/153
\]

gives

\[
N(t_*)=-1/1224.
\]

The verifier checks all remaining outgoing `OI/OO` families in the gate and finds no hidden endpoint failure.

Hence the second transient mode creates a genuine interior sign obstruction invisible to the binary-style endpoint conditions.

## 4. Binary benchmark remains exact

Suppressing type `2` removes the distinct-active retyping constraints. The remaining `OI` numerator has only one decaying exponential, so endpoint positivity is equivalent to the canonical binary conditions

\[
c^0(S)+c^1(S)\le0,
\]

\[
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause when the empty-neighbour total rate vanishes.

The concrete witness suppresses to

\[
u=0,
\quad w=7/4,
\quad c^0(S)=0,
\quad c^1(S)=-9/8,
\]

which satisfies the binary criterion.

Thus there is no `STOP-BINARY-POSITIVITY-MISMATCH`.

## 5. Direction after the stop

Do not start applications or convergence.

The exact `d=3` sign structure now suggests a materially different possible continuation: derive a **spectral critical-point criterion** which explicitly checks the at-most-one interior minimum of

\[
L+A e^{-\mu t}+B e^{-\nu t}.
\]

That would not revive the stopped endpoint criterion; it would be an exact finite spectral test retaining the interior-time information exposed here.

Whether that test is useful enough to justify later applications should be decided only after it is proved and compared with the original coefficient-level goal.
