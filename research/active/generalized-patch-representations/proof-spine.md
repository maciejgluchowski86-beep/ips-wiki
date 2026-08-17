# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the binary patch-representation / patch-positivity mechanism to finite-state single-site replacement IPS, identify an exact multi-state positivity property, determine usable non-binary criteria, establish novelty, and then test applications.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Arbitrary finite-state tensor basis and signed local dual

**Settled in Assignment 001.**

Reference-state indicator tensors yield typed active configurations. General bounded finite-range single-site replacement rates give fixed local signed branch coefficients and an exact Feynman--Kac dual. Successful nonempty records reveal `(i,t,r,tau)` and hide post-source outcome.

## E2. Typed patch factorization

**Settled in Assignment 002 with killed-skeleton modification.**

Bare conditioning fails because typed target conflicts can enter cemetery and suppress future records globally. Since the duality function vanishes at cemetery, killed/noncemetery weighted factorization is exact and representation-sufficient.

## E3. Explicit typed patch representation

**Settled in Assignment 003.**

Bulk contributions are

\[
C(P)=E_P^{con}[A_P],
\]

end contributions are one-site indicator-basis functions, and the exact killed-skeleton semigroup representation is proved. Binary reduction is exact.

## E4. Exact finite-state bulk positivity transfer

**Settled in Assignment 004 for arbitrary finite local state space.**

The signed interior transfer is

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exactly nonnegativity of four local numerator families built from `e^{tK_i}` for every realizable descriptor and patch length.

The `d=2` specialization is exactly canonical binary patch positivity.

## E5. Boundary-complete `d=3` reduction

**Settled in Assignment 005.**

Boundary completeness forces `K` Metzler. Incoming-initial families become automatic. Zero-length outgoing conditions force

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

which makes all `OO` families automatic. Only `OI` remains, with physical Markov representation

\[
p e^{tK}f_b^I=E_b[g(Z_t)],
\qquad
 g=(p_0,p_0+p_1,p_0+p_2).
\]

## E6. Binary-style endpoint collapse

**Refuted in Assignment 005.**

The exact physically realizable witness

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

has positive zero/long endpoints but interior minimum `-1/1224`. Multi-state transients therefore contain genuine information absent from the binary theorem.

## E7. Exact finite spectral criterion in boundary-complete `d=3`

**Settled in Assignment 006.**

Every remaining `OI` function is decided by finitely many explicit evaluations. Generically

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t},
\qquad0<\mu<\nu,
\]

and there is at most one possible interior minimum. Zero-eigenvalue, repeated diagonalizable, Jordan, and reducible cases are also exact and finite.

Thus boundary-complete `d=3` positivity is no longer an all-time scan problem.

## E8. Natural exact non-binary algebraic subclass

**Settled in Assignment 007.**

Assume active-label exchange symmetry at the reference-neighbour level and in the nonempty-target coefficient family:

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}.
\]

Boundary completeness gives

\[
K(1,2)=K(2,1)=c-a,
\]

so typed positivity forces

\[
\boxed{c\ge a.}
\]

The symmetric and antisymmetric decay rates are

\[
2a+b,
\qquad b+2c.
\]

Hence the antisymmetric signed mode is never slower than the symmetric mode.

For every outgoing row `p=(p0,p1,p2)`, typed bulk patch positivity is exactly equivalent to

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0,}
\]

and

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

This is necessary and sufficient inside the subclass. It is genuinely non-binary: the exact gate allows `p_1!=p_2`, so the active labels remain observable.

### Other natural structures classified in Assignment 007

- active-block lumpability plus `p_1=p_2`: exact but observably binary-reducible;
- one-way active retyping: still genuinely two-mode; Assignment-005 obstruction already lies in this class;
- destination-rate refresh chains: repeated-spectrum sibling subclass with exact one-mode criterion.

The binary suppression remains exactly canonical.

Decisive files: `007a`--`007d`, verifier `007-natural-subclass-verifier.py`, final report, and Meeting 007.

## E9. Novelty and closest-prior-work audit

**Open and current load-bearing edge.**

The mathematical package is now stable enough to compare precisely with the literature. Before further abstraction or applications, determine whether prior work already contains any of the following in equivalent language:

1. the arbitrary-finite-state indicator-tensor signed dual for single-site replacement IPS;
2. a coarse successful-record skeleton hiding post-source outcome;
3. the killed/noncemetery patch-factorization repair for typed target conflicts;
4. the exact patch representation obtained by local averaging before taking signs/absolute values;
5. the transfer-matrix characterization of typed bulk positivity;
6. the exact boundary-complete `d=3` spectral criterion;
7. the exchange-symmetric / refresh exact subclasses.

The audit must separate standard ingredients from genuinely new assembly/theorems and must search alternate terminology.

No novelty claim is authorized before E9 is resolved.

## E10. Applications

**Next active mathematical edge if E9 does not subsume the contribution.**

Applications should begin immediately after the literature audit if the generalized mechanism remains nontrivial in novelty status.

The first application block should seek a genuinely non-binary finite-state single-site replacement IPS whose typed coefficients can be checked against either:

- the exchange-symmetric / refresh algebraic criterion; or
- the exact general boundary-complete `d=3` spectral criterion.

The application should not be a relabelled binary spin system.

## E11. `d>3` tractable positivity

**Deferred, not abandoned.**

The representation and exact transfer property already hold for arbitrary finite `d`. What is not yet generalized beyond `d=3` is a tractable coefficient/spectral characterization.

Do not activate a generic `d>3` criterion block before applications unless:

- a concrete application naturally requires more than three local states; or
- the literature audit shows that the arbitrary-`d` criterion itself is the distinctive research contribution worth developing.

This ordering prevents additional algebraic generalization from indefinitely postponing the principal's application question.

## E12. Convergence/comparison and multi-site updates

**Downstream.**

Comparison/convergence consequences and simultaneous multi-site physical updates remain outside the proved package and should be revisited only after novelty and applications clarify which extension matters.
