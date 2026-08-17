# Assignment 006 final: exact three-state spectral critical-point criterion

Date: 2026-08-17

Outcome:

\[
\boxed{\texttt{CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION}.}
\]

## 1. Goal and status

Assignment 005 proved that boundary-complete `d=3` typed patch positivity cannot be characterized by zero-length and long-time endpoint inequalities alone. This block retains the unique possible interior critical point and proves an exact finite necessary-and-sufficient spectral criterion.

No applications, convergence consequences, or `d>3` extension are attempted here.

## 2. Reduction inherited from Assignment 005

Under boundary completeness:

1. the distinct-active short `IO` conditions force
   \[
   K(1,2),K(2,1)\ge0,
   \]
   so `K` is Metzler;
2. every incoming-initial `II/IO` numerator is therefore nonnegative for all time;
3. for every outgoing row
   \[
   p=(p_0,p_1,p_2),
   \]
   zero-length `OO/OI` conditions are
   \[
   p_1,p_2,p_0+p_1,p_0+p_2\ge0;
   \]
4. these make every `OO` numerator nonnegative for all time;
5. only the `OI` families remain:
   \[
   N_{p,b}(t)=p e^{tK}(e_0^T+e_b^T),
   \qquad b=1,2.
   \]

Thus the coefficient problem is finite once each `OI` time dependence is classified.

## 3. Generic distinct-spectrum formula

Let the active block have distinct eigenvalues

\[
-\mu,-\nu,
\qquad 0<\mu<\nu.
\]

The zero spectral projector is

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu}.
\]

For one `OI` row/terminal pair `u,f`, put

\[
L=uP_0f,
\qquad
n_0=uf,
\qquad
n_1=uKf.
\]

Then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t},
\]

where

\[
\boxed{
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.}
\]

No eigenvectors or numerical diagonalization are required.

The derivative has at most one positive zero. An interior minimum occurs exactly when

\[
A<0<B,
\qquad
0<R:=-\frac{\mu A}{\nu B}<1.
\]

Then

\[
t_*=\frac{-\log R}{\nu-\mu}
\]

and

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\]

Therefore `N(t)>=0` for all `t>=0` is equivalent to

- `N(0)>=0`;
- `L>=0`;
- and, only in the displayed interior-minimum regime, `N(t_*)>=0`.

This is necessary and sufficient.

Decisive note: `006a-generic-two-mode-critical-criterion.md`, commit `e79a94a5`.

## 4. Degenerate spectra

All cases are finite as well.

### One active eigenvalue zero

The full spectrum is `0,0,-nu`. Since `K` is similar to a finite-state Markov generator, zero is semisimple even for reducible chains. Hence

\[
N(t)=L+A e^{-\nu t},
\]

and endpoints suffice.

### Repeated nonzero diagonalizable active block

The active block equals `-mu I`; again every numerator is one-mode and endpoints suffice.

### Repeated nonzero Jordan block

Every numerator has form

\[
N(t)=L+(A+Bt)e^{-\mu t}.
\]

There is at most one positive critical point. It is an interior minimum exactly when

\[
B<0,
\qquad B-\mu A<0.
\]

Then

\[
t_*=rac{B-\mu A}{\mu B}>0
\]

and

\[
\boxed{
N(t_*)
=L+\frac B\mu
\exp\left(-\frac{B-\mu A}{B}\right).}
\]

Thus endpoints plus this one critical value are necessary and sufficient.

### Reducible chains

Reducibility creates no additional time-dependence class. It can increase the rank of the zero projector and make the long-time value depend on the initial active type, but the same finite spectral cases remain exhaustive.

Decisive note: `006b-degenerate-spectral-cases.md`, commit `96127a9b`.

## 5. Exact finite criterion

Combining the reductions gives a necessary-and-sufficient criterion for boundary-complete `d=3` typed bulk patch positivity:

1. `K(1,2),K(2,1)>=0`;
2. for every outgoing row `p`,
   \[
   p_1,p_2,p_0+p_1,p_0+p_2\ge0;
   \]
3. for each outgoing row and each incoming terminal type, check its long-time value and at most one interior critical value according to the spectral case above.

Every incoming and `OO` family is then automatic.

This criterion is genuinely finite. A finite local descriptor set gives finitely many `OI` pairs, and each pair requires at most one critical evaluation. There is no mesh or scan over time.

The generic critical inequality is not, in general, purely algebraic in the local coefficients because it contains

\[
R^{\mu/(\nu-\mu)}.
\]

That is a real limitation and is the spectral information whose loss caused the Assignment-005 endpoint failure. It does not turn the criterion back into the all-time semigroup definition: it is one explicitly specified local comparison per critical descriptor.

Decisive note: `006c-finite-spectral-criterion-and-usability.md`, commit `54334311`.

## 6. Mandatory exact gates

Verifier:

`006-three-state-spectral-verifier.py`, commit `419196b4`.

All checks use `Fraction` arithmetic only.

### Negative gate: Assignment-005 obstruction

The physical reference-neighbour chain has

\[
K=\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

For

\[
p=(-1/8,9/8,1/4)
\]

and incoming terminal type `1`,

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

The criterion identifies

\[
e^{-t_*}=\frac{13}{153},
\qquad
N(t_*)=-\frac1{1224}.
\]

### Positive `p_0<0` gate

Using the same reference-neighbour chain but a different physically realizable neighbour-mode coefficient row gives

\[
p=(-1/8,9/8,3/8).
\]

The two `OI` numerators are

\[
N_1(t)=\frac5{128}-\frac{15}{64}e^{-t}+\frac{153}{128}e^{-2t},
\]

\[
N_2(t)=\frac5{128}+\frac{45}{64}e^{-t}-\frac{63}{128}e^{-2t}.
\]

For the first,

\[
e^{-t_*}=\frac5{51},
\qquad
N_1(t_*)=\frac{15}{544}>0.
\]

The second is concave as a function of `e^{-t}` and has positive endpoint minimum. The verifier checks every `OI` and `OO` family for both target modes in this boundary-complete example.

Thus the criterion detects both a true interior failure and a genuinely nontrivial `p_0<0` all-time positive example.

## 7. Binary acceptance test

Suppressing type `2` leaves one active eigenvalue only. The interior critical branch disappears.

For a nonempty target `S`, the spectral criterion becomes exactly

\[
c^0(S)+c^1(S)\le0,
\]

\[
c^1(\emptyset)c^0(S)
\ge
c^0(\emptyset)c^1(S)
\]

when `c^0(emptyset)+c^1(emptyset)>0`, with the canonical degenerate clause `c\equiv0` when that sum is zero.

No stronger binary condition is introduced.

Decisive note: `006d-binary-spectral-reduction.md`, commit `93dad82b`.

## 8. Ruling

The generic and every degenerate spectral case reduce to finitely many exact endpoint/critical evaluations. The test is materially more usable than the uncountable semigroup definition and passes both mandatory physical gates and the exact binary reduction.

Therefore Assignment 006 ends

\[
\boxed{\texttt{CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION}.}
\]

The next bounded question is **not applications**. It is whether the finite spectral condition admits a natural coefficient simplification or a structural multi-state subclass in which the critical inequality becomes algebraic/monotone and therefore easier to use.
