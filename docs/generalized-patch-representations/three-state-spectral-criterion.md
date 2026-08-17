# Exact three-state spectral positivity criterion

> **Research-branch page.** This page exists only on `research/generalized-patch-representations`. It is not published on `main`.

For boundary-complete three-state single-site replacement systems, typed bulk patch positivity admits a finite exact spectral test.

The result follows the exact transfer representation

\[
K(0,\cdot)=0,
\qquad
K(r,s)=a_r^s(\emptyset),
\]

and the Assignment-005 structural reduction.

## Boundary-complete reduction

Boundary completeness forces the active retyping entries of `K` to be nonnegative. Thus `K` is Metzler and `e^{tK}` is entrywise nonnegative.

For every outgoing row

\[
p=(p_0,p_1,p_2),
\]

the zero-length conditions are

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0.
\]

After these conditions:

- every incoming-initial bulk numerator is nonnegative;
- every outgoing-to-outgoing bulk numerator is nonnegative;
- only outgoing-to-incoming (`OI`) numerators remain.

For incoming terminal type `b`, write

\[
N_{p,b}(t)=p e^{tK}(e_0^T+e_b^T).
\]

## Generic distinct spectrum

Suppose the active `2 x 2` block has eigenvalues

\[
-\mu,-\nu,
\qquad0<\mu<\nu.
\]

Then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

No eigenvectors are needed. Put

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu},
\quad L=uP_0f,
\quad n_0=uf,
\quad n_1=uKf.
\]

Then

\[
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.
\]

The derivative has at most one positive zero. The only possible interior minimum occurs when

\[
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1.
\]

In that case

\[
t_*=rac{-\log R}{\nu-\mu}
\]

and

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\]

Thus

\[
N(t)\ge0\quad\forall t\ge0
\]

is equivalent to nonnegativity at `t=0`, at `t=infinity`, and at this one interior point when it exists.

## Degenerate spectra

No irreducibility assumption is required.

Because `K` is similar to the physical finite-state Markov generator with the neighbours frozen in the reference state, zero eigenvalues are semisimple even for reducible chains.

The remaining possibilities are:

- one zero and one negative active eigenvalue: one decaying mode, so endpoints suffice;
- repeated negative diagonalizable active block: one decaying mode;
- repeated negative Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  again with at most one interior minimum;
- all-zero active spectrum: constant numerator.

Hence every boundary-complete three-state descriptor is decided by finitely many local evaluations.

## Why the critical value is necessary

The endpoint-only criterion fails. A physically realizable example has

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

but

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224.
\]

The spectral criterion detects this exact negative minimum.

A separate physically realizable boundary-complete row

\[
p=(-1/8,9/8,3/8)
\]

has `p_0<0` but remains positive for every patch length. Its nontrivial `OI` minimum is

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

Thus the criterion distinguishes genuine positivity from the interior-time obstruction.

## Binary reduction

Suppressing type `2` leaves only one active decay mode. The interior-critical branch disappears and the criterion reduces exactly to

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical zero-rate clause.

No stronger binary condition is introduced.

## Limitation

The criterion is finite but not generally a purely algebraic coefficient cone. In the generic case the exact critical inequality contains

\[
R^{\mu/(\nu-\mu)}.
\]

This spectral factor is the transient information that the three-state endpoint counterexample shows cannot be discarded in general.
