# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a coarse successful-interaction skeleton;
4. killed/weighted patch factorization;
5. explicit patch contributions;
6. exact typed bulk nonnegativity;
7. a tractable multi-state positivity criterion retaining genuinely necessary transient information;
8. only then consequences and applications.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Finite-state tensor basis and signed local dual

**Settled in Assignment 001.**

Reference-state indicator tensors yield typed active configurations. General bounded finite-range single-site replacement rates give fixed local signed branch coefficients and a local Feynman--Kac dual. Successful nonempty records reveal `(i,t,r,tau)` and hide the post-source outcome.

## E2. Typed patch factorization

**Settled in Assignment 002 with killed-skeleton modification.**

Bare conditioning fails because typed target conflicts can enter cemetery and suppress future records globally. Since `H_dagger=0`, killed/noncemetery weighted factorization is exact.

## E3. Explicit typed patch representation

**Settled in Assignment 003.**

Bulk contributions are

\[
C(P)=E_P^{con}[A_P],
\]

end contributions are one-site indicator-basis functions, and the exact killed-skeleton semigroup representation is proved. Binary reduction is exact.

## E4. Exact typed bulk positivity transfer

**Settled in Assignment 004.**

The signed interior transfer is

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exactly the nonnegativity of the four local numerator families built from `e^{tK_i}` for every realizable descriptor and `t>0`.

The `d=2` specialization is exactly the canonical patch-positivity coefficient criterion.

## E5. Boundary-complete `d=3` structural reduction

**Settled in Assignment 005.**

Boundary completeness forces `K` Metzler. Hence incoming-initial families are automatic. For every outgoing row

\[
p=(p_0,p_1,p_2),
\]

zero-length conditions force

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

which makes all `OO` families automatic. Only `OI` remains, with the physical Markov representation

\[
p e^{tK}f_b^I=E_b[g(Z_t)],
\qquad
 g=(p_0,p_0+p_1,p_0+p_2).
\]

## E6. Binary-style endpoint criterion

**Refuted in Assignment 005.**

The exact witness

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

has

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

but

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224.
\]

Thus zero-length plus long-time inequalities do not characterize boundary-complete `d=3` positivity. This does not affect the exact semigroup property or binary theory.

## E7. Exact finite spectral criterion in boundary-complete `d=3`

**Settled in Assignment 006.**

For each remaining `OI` descriptor, the active `2 x 2` spectrum is real because `K` is Metzler.

### Generic distinct negative active eigenvalues

If

\[
-\mu,-\nu,
\qquad0<\mu<\nu,
\]

then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

Use

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
0<R=-\frac{\mu A}{\nu B}<1,
\]

and then

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\]

Hence zero-length, long-time, and at most one critical-value check are necessary and sufficient.

### Degenerate spectra

Also settled exactly:

- one zero active eigenvalue: one decaying mode;
- repeated negative diagonalizable active block: one decaying mode;
- repeated negative Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  again with at most one interior minimum;
- reducible reference-neighbour chains: no new time-dependence class; zero remains semisimple because `K` is similar to a finite-state Markov generator.

Thus every boundary-complete `d=3` descriptor is decided by finitely many explicit local evaluations.

### Mandatory gates

The criterion reproduces the Assignment-005 negative minimum and verifies a separate physically realizable `p_0<0` positive example with

\[
p=(-1/8,9/8,3/8),
\]

whose nontrivial minimum is

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

The binary suppression again gives exactly the canonical coefficient inequalities.

Decisive files: `006a`--`006d`, verifier `006-three-state-spectral-verifier.py`, and Meeting 006.

## E8. Natural simplification / structural subclass

**Open and current load-bearing edge.**

The exact `d=3` criterion is finite but not generally a purely algebraic coefficient cone. Its generic critical inequality contains

\[
R^{\mu/(\nu-\mu)}.
\]

Assignment 005 proves that the interior transient cannot simply be deleted.

The next bounded problem is:

> identify a mathematically natural non-binary structural subclass for which the exact critical condition simplifies to algebraic/monotone local inequalities, and prove necessity and sufficiency within that subclass while preserving the exact binary reduction.

Possible structure must arise from the IPS/transfer algebra rather than be imposed solely to force positivity. A merely sufficient cone is not a replacement for the exact property unless the subclass itself is independently natural.

## E9. Consequences, applications, and broader updates

**Blocked on E8.**

Do not start applications, convergence, arbitrary `d`, or simultaneous multi-site updates before the simplification/subclass question is materially resolved.

## Novelty status

No literature novelty claim has yet been made. A targeted literature audit remains necessary once the theorem package is stable enough to compare precisely.
