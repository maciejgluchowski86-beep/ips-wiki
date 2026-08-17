# Assignment 010 handoff

Date: 2026-08-17

Outcome: **`STOP-SECOND-APPLICATION-POSITIVITY-FAILS`**.

## Decisive facts

The model was selected before positivity calculation: the three-state zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics.

With reference color `0`, `z=e^{-beta J}` and common proposal-rate prefactor `q`,

\[
c^{x\to y}=qz^{(n_x-n_y)_+}.
\]

For a source-type-1 successful record with one target-neighbor of type 1,

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right).
\]

Thus for every `0<z<1`, hidden outcome `2` has positive absolute rate but negative signed coefficient

\[
a_1^2=-qz^2(1-z^2)<0.
\]

A source-type-2 successful record can follow, so a realized arbitrarily short `OO` patch is negative. Hence Potts Metropolis is not typed patch positive anywhere in the interacting finite-temperature regime.

The mechanism is not Assignment 009's vacancy/birth architecture. It is a source-response contrast: the `0->1` rate has a positive singleton color-1 target increment, whereas the `2->1` Metropolis rate is already saturated and has zero increment.

General lemma:

\[
a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0
\]

plus realizable hidden outcome `s` and a follow-up source-`s` successful record implies a realized negative short `OO` patch.

## Hidden-mark honesty

The negative verdict is nondegenerate:

- at least two post-source outcomes are hidden with positive absolute rate;
- typed cemetery conflicts are realizable;
- empty-target transfer retypes active labels;
- the model is not a deterministic voter/cyclic-copy graphical dual.

## Exact gate

At `z=1/2`, `q=1`:

\[
p=(3/16,5/16,-3/16),
\]

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\]

For

\[
t_*=(8/3)\log(5/4),
\]

\[
N_{OO}(t_*)=-3884/390625<0.
\]

Verifier:

`students/professor/010-potts-metropolis-verifier.py`.

It is designed to perform 1,485 exact checks:

- 486 physical-rate positivity checks;
- 486 Möbius reconstruction checks;
- 486 typed-generator reconstruction checks;
- 9 empty-transfer checks;
- 7 decisive singleton-row checks;
- 4 realized-support checks;
- 7 finite-length gate checks.

No float literals are used.

## Programme direction

Do not automatically open a third positivity-based model search. Assignments 009 and 010 have now tested two materially different natural three-state architectures and both fail through local short-`OO` signs.

Do not insert generic `d>3` coefficient algebra.

If the generalized-patch programme continues after independent verification, the next question should be representation-only: whether the killed typed patch identity yields a useful consequence without assuming bulk patch positivity. That should be chosen only after an explicit opportunity-cost review.
