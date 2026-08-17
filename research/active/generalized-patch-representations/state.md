# Programme state

Date: 2026-08-17

## Active direction

Generalize the canonical patch-representation / patch-positivity framework beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/005-three-state-endpoint-criterion-obstructed.md`.

## Assignment 001

Status: **`CONTINUE-TYPED-PATCH`**.

The reference-state indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for finite-state bounded finite-range single-site replacement IPS. Nonempty successful records reveal source/time/pre-source type/typed target and hide post-source outcome.

## Assignment 002

Status: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditional factorization fails because incoming typed conflicts can hit cemetery and remove all future no-record constraints. Since `H_dagger=0`, the exact representation uses killed/noncemetery weighted factorization.

## Assignment 003

Status: **`CONTINUE-TYPED-POSITIVITY`**.

The exact typed patch representation is proved. Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data; end contributions are one-site indicator-basis functions.

## Assignment 004

Status: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

For active local type `r`, the exact weighted interior transfer is

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset).
\]

The unsigned consistency transfer is the killed Markov matrix built from absolute empty-target coefficients and the nonempty-target hazard.

For

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

and outgoing row

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\]

typed bulk patch positivity is exactly nonnegativity for all realizable descriptors and `t>0` of

\[
e_a e^{tK_i}f_b^I,
\qquad
e_a e^{tK_i}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O.
\]

The `d=2` specialization is exactly the canonical binary patch-positivity criterion.

## Assignment 005

Status: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

The stop is specific to a binary-style endpoint collapse in boundary-complete `d=3`. The exact semigroup positivity property above remains valid.

### Boundary completeness forces Metzler `K`

For reference-neighbour physical rates `q_xy`,

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix}.
\]

Short incoming-to-outgoing patches between distinct active types force

\[
q_{21}\ge q_{01},
\qquad
q_{12}\ge q_{02}.
\]

Thus `K` is Metzler and `e^{tK}` is entrywise nonnegative. Every incoming-initial `II/IO` family is automatic.

### Outgoing rows

For outgoing row `p=(p0,p1,p2)`, zero-length boundary completeness forces

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0.
\]

Then every `OO` family is automatic. The remaining `OI` family has the exact physical Markov interpretation

\[
p e^{tK}f_b^I=E_b[g(Z_t)],
\qquad
 g=(p_0,p_0+p_1,p_0+p_2),
\]

where `Z` is the physical local chain with all neighbours in the reference state.

### Exact interior-time obstruction

A genuine one-neighbour physical IPS has

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

One boundary-complete outgoing row is

\[
p=(-1/8,9/8,1/4),
\qquad
 g=(-1/8,1,1/8).
\]

For incoming terminal type `1`,

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

Although

\[
N(0)=1,
\qquad
N(\infty)=1/128,
\]

at

\[
e^{-t_*}=13/153
\]

one has

\[
N(t_*)=-1/1224.
\]

All physical one-neighbour rates are nonnegative. The exact gate checks all other outgoing families in the constructed test and the binary suppression.

### Binary suppression

Suppressing type `2` removes the distinct-active retyping condition and recovers exactly

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause. No stronger binary condition is introduced.

Decisive files:

- `students/professor/005a-metzler-incoming-reduction.md`, commit `f8a73319`;
- `005b-outgoing-row-markov-reduction.md`, commit `a4f36bd`;
- exact verifier `005-three-state-endpoint-obstruction-verifier.py`, commit `fc8c999e`;
- `005c-exact-interior-time-obstruction.md`, commit `3d8778ac`;
- `005d-binary-suppression.md`, commit `ffdb1929`;
- final report `005-three-state-positivity-criterion.md`, commit `027bcbf8`;
- handoff `005-handoff.md`, commit `4710ddf9`;
- Meeting 005, commit `ee43807e`.

## Current proof-spine edge

**Exact finite spectral criterion retaining interior-time information.**

Assignment 005 refutes endpoint-only coefficient tests in boundary-complete `d=3`, but it also reduces every generic remaining `OI` numerator to two real decaying modes. A materially different bounded continuation is to derive the exact critical-point condition for

\[
L+A e^{-\mu t}+B e^{-\nu t}
\]

and decide whether that finite spectral test is useful enough to count as a tractable typed positivity criterion.

Do not move to applications or convergence yet.

## Scope, novelty and publication boundary

Current proved scope: finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis.

Simultaneous multi-site physical updates remain outside scope.

No novelty claim has yet been made for the generalized theorem. Literature audit remains downstream of a stable criterion-level theorem.

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are not to be modified by this programme. Stable current research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge any programme content to `main`.**

All previously stopped programmes remain closed.
