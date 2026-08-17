# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a graphical process with a coarser successful-interaction skeleton;
4. conditional/weighted factorization into spacetime patches;
5. explicit patch contributions;
6. an exact local bulk nonnegativity property;
7. a tractable criterion retaining whatever multi-state transient information is genuinely necessary;
8. only then consequences and applications.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Canonical finite-state tensor basis

**Settled in Assignment 001.**

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives typed active configurations; conflicts give cemetery `dagger` with zero duality function.

## E2. Exact signed local dual

**Settled in Assignment 001.**

General bounded finite-range single-site replacement rates yield fixed local signed branch coefficients `a_{i,r}^s(tau)`. Absolute values are Poisson rates and source outcome deletes/preserves/retypes the source. Target conflicts affect only the deterministic merge.

## E3. Typed successful record

**Settled in Assignment 001.**

For nonempty target, record

\[
(i,t,r,\tau)
\]

and hide post-source outcome `s`.

## E4. Typed patch factorization

**Settled in Assignment 002 with a necessary killed-skeleton modification.**

Bare conditioning on the coarse record list fails because an incoming typed conflict can send the dual to cemetery and remove future no-record constraints. Since `H_dagger=0`, the exact representation uses killed/noncemetery weighted factorization.

## E5. Explicit typed patch representation

**Settled in Assignment 003.**

Bulk contributions are

\[
C(P)=E_P^{con}[A_P],
\]

end contributions are one-site indicator-basis functions, and the exact killed-skeleton semigroup representation is proved. The binary specialization is exact.

## E6. Exact typed bulk patch positivity

**Settled in Assignment 004 at transfer-matrix level.**

For active local type `r`, the weighted interior transfer has generator

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset).
\]

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

typed bulk patch positivity is exactly nonnegativity of

\[
e_a e^{tK_i}f_b^I,
\qquad e_a e^{tK_i}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O
\]

for every realizable descriptor and every `t>0`.

The binary specialization recovers exactly the canonical patch-positivity coefficient criterion.

## E7. Boundary-complete three-state reduction

**Settled in Assignment 005.**

For `d=3`, boundary completeness forces the empty-target transfer to be Metzler. Writing reference-neighbour physical rates `q_xy`,

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix},
\]

short incoming-to-outgoing descriptors imply

\[
q_{21}\ge q_{01},
\qquad
q_{12}\ge q_{02}.
\]

Hence `e^{tK}` is entrywise nonnegative.

Consequences:

- every incoming-initial `II/IO` numerator is automatic;
- for outgoing row `p=(p0,p1,p2)`, zero-length conditions force
  \[
  p_1,p_2,p_0+p_1,p_0+p_2\ge0;
  \]
- all `OO` families are then automatic;
- only outgoing-initial/incoming-terminal (`OI`) families remain.

For

\[
g=(p_0,p_0+p_1,p_0+p_2),
\]

and the physical reference-neighbour generator `Q`, the exact intertwining gives

\[
\boxed{p e^{tK}f_b^I=E_b[g(Z_t)].}
\]

Thus the multi-state sign issue is a local Markov-semigroup transient problem.

## E8. Binary-style endpoint criterion

**Refuted in Assignment 005.**

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

For one boundary-complete outgoing row

\[
p=(-1/8,9/8,1/4),
\qquad
 g=(-1/8,1,1/8),
\]

the required `OI` numerator is

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

Both endpoint values are strictly positive:

\[
N(0)=1,
\qquad
N(\infty)=1/128,
\]

but at

\[
e^{-t_*}=13/153
\]

one has

\[
N(t_*)=-1/1224.
\]

All physical one-neighbour rates are nonnegative and all other endpoint conditions in the gate hold.

Therefore the direct binary-style collapse to zero-length and long-time coefficient inequalities is stopped:

**`STOP-NO-FINITE-ENDPOINT-CRITERION`.**

Suppressing type `2` recovers exactly the canonical binary coefficient inequalities and removes the obstruction.

Decisive files: `005a`--`005d`, verifier `005-three-state-endpoint-obstruction-verifier.py`, and Meeting 005.

## E9. Exact spectral critical-point criterion

**Open and current load-bearing edge.**

The endpoint collapse is false, but the `d=3` reduction is still unusually rigid. Under the Metzler/physical conditions, the two nonzero eigenvalues are real. Generically every remaining `OI` numerator is

\[
L+A e^{-\mu t}+B e^{-\nu t},
\qquad 0<\mu<\nu.
\]

Such a function has at most one interior critical point capable of being a negative minimum. Therefore a materially distinct next question is:

> derive a necessary-and-sufficient **finite spectral test** consisting of endpoint conditions plus the exact interior critical-value inequality when that minimum exists, including repeated/degenerate eigenvalue cases and exact binary reduction.

This retains the transient information shown necessary by Assignment 005 rather than reviving the refuted endpoint-only criterion.

## E10. Consequences, applications, and broader updates

**Blocked on E9.**

Do not start applications, convergence, `d>3`, or simultaneous multi-site updates until the spectral criterion is either proved useful or rejected on mathematical grounds.

## Novelty status

No literature novelty claim has yet been made for the generalized representation/positivity theorem. A targeted literature audit remains necessary once the criterion-level theorem is stable enough to compare precisely.
