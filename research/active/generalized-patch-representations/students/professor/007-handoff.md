# Assignment 007 handoff

Date: 2026-08-17

Outcome: **`CONTINUE-NATURAL-THREE-STATE-SUBCLASS`**.

## Decisive result

For boundary-complete `d=3`, suppose the physical reference-neighbour chain and nonempty-target coefficient family are invariant under active-label exchange `1<->2`, so

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}.
\]

Then typed bulk patch positivity is equivalent to:

\[
c\ge a,
\]

and, for every outgoing row `p=(p0,p1,p2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

The criterion is necessary and sufficient inside the subclass. It is genuinely non-binary: admissible rows may have `p1 != p2`, and the exact physical gate has distinct `OI` values from initial active states 1 and 2.

## Mechanism

Exchange symmetry splits the remaining `OI` numerator into symmetric and antisymmetric modes. The already-necessary Metzler condition is `c>=a`, which makes the antisymmetric mode decay at least as fast as the symmetric mode. For `p0<0`, the symmetric modal coefficient is nonnegative. Therefore the signed faster mode can be bounded by the slower one, reducing the all-time sign problem exactly to zero-length and long-time endpoints.

This is not the binary quotient mechanism. Observable lumpability requires `p1=p2` and was classified separately as binary-reducible.

## Other candidates

- Lumpable dynamics plus lumped value functions gives an exact one-mode criterion but is observably binary-reducible.
- One-way active retyping remains genuinely spectral. The Assignment-005 triangular witness already has an interior negative minimum `-1/1224`.
- The refresh subclass `q_xy=rho_y` is a repeated-spectrum boundary/sibling case with exact one-mode criterion.

## Binary gate

Suppressing type 2 removes every two-active-label structural condition. The exact criterion reduces to

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause. No stronger condition survives.

## Files

- `007a-lumpability-classification.md`, commit `6c41149d`;
- corrected `007b-symmetry-and-refresh-subclass.md`, commit `52e9e7ac`;
- `007c-triangular-still-spectral.md`, commit `c692967d`;
- verifier `007-natural-subclass-verifier.py`, commit `3a12ba34`;
- `007d-exact-subclass-criterion-and-binary-reduction.md`, commit `06199715`;
- final report `007-natural-spectral-simplification.md`, commit `5f9b4b8b`.

## Important correction

An initial version of `007b` tried to use an exchange-symmetric example with `c<a` as an interior-time obstruction. This was caught before closure: it violates the already-necessary Metzler condition `c>=a`. The file was replaced at `52e9e7ac`. The corrected theorem goes in the opposite direction and is the main result of the assignment.

## Next direction recommendation

Do **not** continue automatically to `d>3` coefficient algebra.

The finite-state representation itself already covers arbitrary finite `d`; what remains `d>3`-specific is tractable positivity characterization. The programme now has both an exact generic `d=3` spectral criterion and a genuine non-binary algebraic subclass.

The next bounded block should be a targeted literature/novelty audit of the generalized finite-state representation, killed-skeleton factorization, transfer criterion, and symmetric/refresh subclass. If that audit does not subsume the mechanism, applications should become the active mathematical block immediately after it.

A `d>3` tractable-criterion block should be activated only if an application naturally requires more than three states, or if the literature audit shows that the genuinely new part lies specifically in the arbitrary-`d` extension.
