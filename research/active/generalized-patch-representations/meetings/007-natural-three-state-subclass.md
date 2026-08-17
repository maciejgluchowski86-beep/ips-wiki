# Meeting 007: natural three-state positivity subclass

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- lumpability classification `students/professor/007a-lumpability-classification.md`, commit `6c41149d`;
- corrected symmetry theorem `007b-symmetry-and-refresh-subclass.md`, commit `52e9e7ac`;
- triangular obstruction `007c-triangular-still-spectral.md`, commit `c692967d`;
- exact verifier `007-natural-subclass-verifier.py`, commit `3a12ba34`;
- binary/honesty theorem `007d-exact-subclass-criterion-and-binary-reduction.md`, commit `06199715`;
- final report `007-natural-spectral-simplification.md`, commit `5f9b4b8b`;
- handoff `007-handoff.md`, commit `d465af1d`.

## Ruling

Assignment 007 ends

**`CONTINUE-NATURAL-THREE-STATE-SUBCLASS`.**

The programme now has a genuinely non-binary natural `d=3` subclass for which the exact typed bulk patch-positivity condition collapses from the generic Assignment-006 spectral critical test to finite algebraic endpoint inequalities, with necessity and sufficiency inside the subclass and exact binary reduction.

## 1. Lumpability is not the result

The physical reference-neighbour chain is lumpable with respect to `{0},{1,2}` exactly when

\[
q_{10}=q_{20}.
\]

A remaining `OI` value function descends to that quotient exactly when its outgoing row satisfies

\[
p_1=p_2.
\]

That route is exact but observably binary-reducible and is not counted as the multi-state result requested by the principal.

## 2. Exchange symmetry plus Metzler ordering is the result

Write

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}.
\]

The symmetric and antisymmetric decay rates are

\[
2a+b,
\qquad b+2c.
\]

Boundary completeness plus typed patch positivity forces

\[
K(1,2)=K(2,1)=c-a\ge0,
\]

so

\[
\boxed{c\ge a.}
\]

Hence the antisymmetric mode is never slower than the symmetric mode.

For every outgoing row `p=(p0,p1,p2)`, exact typed bulk patch positivity in the exchange-symmetric subclass is equivalent to

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0,}
\]

and

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

No interior spectral evaluation remains.

The proof is not a sufficient-cone argument. These inequalities are zero-length and long-time necessary conditions, and spectral ordering proves they are sufficient.

## 3. Non-binary honesty passes

The exact gate uses

\[
a=1,
\qquad b=2,
\qquad c=2
\]

and an outgoing row

\[
p=(-1/2,3/2,1),
\]

so

\[
g=(-1/2,1,1/2).
\]

Thus the two active initial states give distinct patch values at zero time. The physical chain has positive transitions between active states, both active states have positive stationary mass, and the target-type coefficient perturbations distinguish active labels. The model is not dynamically or observably equivalent to the binary quotient.

## 4. Important correction during the block

An initial symmetry checkpoint used a `c<a` example and claimed that symmetry retained an interior obstruction. That was mathematically inappropriate for the candidate positivity class because `c<a` makes the typed transfer non-Metzler and already violates short incoming-to-outgoing patch positivity.

The mistake was caught before closure and the note was replaced at commit `52e9e7ac`. Once the necessary Metzler condition is imposed, the conclusion reverses: symmetry gives an exact simplification.

This correction is part of the evidence for `state_narrowed: yes` rather than something to hide.

## 5. One-way retyping remains spectral

The Assignment-005 obstruction already has exactly one active retyping direction and still exhibits the exact negative interior minimum

\[
-1/1224.
\]

Thus triangularity is not a usable exact simplification.

## 6. Refresh subclass

The case `c=a` is a repeated-spectrum three-state refresh chain. More generally, destination-rate reference chains

\[
q_{xy}=\rho_y
\]

have one nonzero decay rate and an exact one-mode criterion. This is a genuine multi-state sibling subclass, not a binary quotient.

## 7. Binary benchmark

Suppressing type `2` removes every two-active-label symmetry/Metzler condition and recovers exactly

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause.

No stronger binary condition is introduced.

## 8. Programme ordering after Assignment 007

The programme should **not** automatically spend another block on abstract `d>3` positivity algebra.

The representation/duality/factorization theorem already covers arbitrary finite local state spaces. What remains special to `d=3` is the tractable positivity characterization.

The next block should be a bounded **literature and novelty audit** of the generalized theorem stack:

1. finite-state indicator-tensor/Feynman--Kac duality;
2. successful-record skeleton with hidden source outcome;
3. killed/noncemetery patch factorization;
4. exact local transfer characterization of bulk positivity;
5. the boundary-complete three-state spectral theorem;
6. the exchange-symmetric and refresh exact subclasses.

If the audit does not show that this mechanism is already subsumed by prior work, **applications become the next active mathematical block immediately after the audit**.

Applications are considered ready when:

- there is a genuinely non-binary exact criterion to test, which Assignment 007 now provides;
- literature review has not killed the contribution by showing the framework or criterion is already standard in equivalent language; and
- at least one concrete finite-state single-site replacement model can be written in the typed coefficients and checked against either the symmetric/refresh criterion or the exact three-state spectral criterion.

A `d>3` tractable-criterion block is deferred until one of two things happens:

- an application naturally requires more than three local states; or
- the literature audit indicates that the arbitrary-`d` criterion itself is the mathematically distinctive contribution worth pushing.

This ordering prevents the principal's application question from receding indefinitely while avoiding application work before novelty is even known.

## 9. No applications started here

Assignment 007 respected its scope. No convergence theorem, application model, `d>3` criterion, or novelty claim was started in this block.
