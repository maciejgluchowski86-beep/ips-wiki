# Assignment 007 final report: natural three-state positivity subclass

Date: 2026-08-17

Outcome: **`CONTINUE-NATURAL-THREE-STATE-SUBCLASS`**.

## 1. Goal

Test whether natural `d=3` structural subclasses simplify the exact Assignment-006 spectral criterion without replacing typed patch positivity by a sufficient cone or by an observable binary quotient.

The tested classes were:

- active-block lumpability;
- active-type exchange symmetry;
- one-way active retyping.

## 2. Lumpability

For the physical reference-neighbour chain, strong lumpability with respect to

\[
\{0\},\qquad\{1,2\}
\]

is exactly

\[
q_{10}=q_{20}.
\]

For an outgoing row

\[
p=(p_0,p_1,p_2),
\]

the remaining `OI` value function

\[
g=(p_0,p_0+p_1,p_0+p_2)
\]

descends to the quotient exactly when

\[
p_1=p_2.
\]

When both the dynamics and every tested value function lump, the numerator is one-mode and endpoint conditions are exact. This is **binary-reducible**, because the tested observable itself cannot distinguish active types. It is not counted as the desired result.

Decisive note: `007a-lumpability-classification.md`, commit `6c41149d`.

## 3. Exchange symmetry gives a genuine non-binary exact subclass

Assume the reference-neighbour chain is exchange-symmetric:

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\qquad a,b,c\ge0,
\]

and the nonempty-target coefficient family is invariant under `1<->2`.

The two nonzero decay rates are

\[
\lambda_s=2a+b,
\qquad
\lambda_a=b+2c,
\]

for the symmetric and antisymmetric modes.

Boundary completeness plus typed patch positivity forces the active retyping entries of `K` to be nonnegative. Here

\[
K(1,2)=K(2,1)=c-a,
\]

so the necessary Metzler condition is

\[
\boxed{c\ge a.}
\]

Consequently

\[
\lambda_a\ge\lambda_s.
\]

For an outgoing row define

\[
g=(p_0,p_0+p_1,p_0+p_2),
\qquad
m=(g_1+g_2)/2,
\qquad
d=(g_1-g_2)/2.
\]

Then

\[
N_1(t)=L+(m-L)e^{-\lambda_s t}+d e^{-\lambda_a t},
\]

\[
N_2(t)=L+(m-L)e^{-\lambda_s t}-d e^{-\lambda_a t},
\]

with

\[
L=\frac{b g_0+2a m}{b+2a}.
\]

If `p_0<0`, the zero-length conditions imply `m>=0` and

\[
m-L=\frac{b}{b+2a}(m-p_0)\ge0.
\]

For whichever numerator carries a negative antisymmetric coefficient, the faster decay gives the exact lower bound

\[
N_b(t)
\ge
L+(g_b-L)e^{-\lambda_s t},
\]

which is nonnegative whenever the zero-length value `g_b` and the long-time value `L` are nonnegative. If the antisymmetric coefficient is positive, every modal term is nonnegative.

Therefore the exact boundary-complete criterion in this subclass is:

\[
\boxed{c\ge a,}
\]

and for every outgoing row,

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0,}
\]

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

These conditions are necessary and sufficient. No critical-time evaluation remains.

A first draft of the symmetry analysis used a `c<a` example and was corrected before closure: such an example violates the already-necessary Metzler condition and is not a valid test inside the candidate positivity class.

Decisive corrected note: `007b-symmetry-and-refresh-subclass.md`, commit `52e9e7ac`.

## 4. Non-binary honesty gate

Take

\[
a=1,
\qquad b=2,
\qquad c=2.
\]

Then

\[
Q=
\begin{pmatrix}
-2&1&1\\
2&-4&2\\
2&2&-4
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
0&0&0\\
1&-5&1\\
1&1&-5
\end{pmatrix}.
\]

For one target mode choose outgoing rows

\[
p^{1,1}=(0,1/4,1/4),
\qquad
p^{2,1}=(-1/2,3/2,1),
\]

and take the second target mode by exchanging active labels. The corresponding physical rates are all nonnegative; the target-type-1 rates are

\[
(1,1/2,3/4,3,5/4,9/4)
\]

in transition order `01,02,10,12,20,21`, and target type `2` gives the swapped list.

For the distinguished row,

\[
g=(-1/2,1,1/2),
\qquad L=1/8,
\]

and

\[
N_1(t)=1/8+(5/8)e^{-4t}+(1/4)e^{-6t},
\]

\[
N_2(t)=1/8+(5/8)e^{-4t}-(1/4)e^{-6t}.
\]

Both are nonnegative for all time. Since

\[
N_1(0)=1\ne1/2=N_2(0),
\]

the observable does not factor through the binary active block. Both active physical states have positive stationary mass, the physical chain has positive `1<->2` transitions, and the target perturbations distinguish active labels. The subclass is genuinely three-state.

A physically realizable row in the same class with

\[
p=(-1/2,1,1/2)
\]

has all zero-length signs nonnegative but long-time value `L=-1/8`, showing the final inequality is nonvacuous.

## 5. Refresh boundary case

When `c=a`, the symmetric and antisymmetric decay rates coincide. This is exactly a three-state refresh chain with destination rates `(b,a,a)`.

More generally, any reference chain with

\[
q_{xy}=\rho_y\quad(x\ne y)
\]

has

\[
e^{tQ}g=\pi(g)\mathbf1+e^{-Rt}(g-\pi(g)\mathbf1),
\qquad R=\rho_0+\rho_1+\rho_2.
\]

Thus all `OI` numerators are one-mode, even when `p_1!=p_2`, and the exact long-time condition is

\[
R p_0+\rho_1p_1+\rho_2p_2\ge0.
\]

This is a broader repeated-spectrum exact subclass.

## 6. One-way active retyping does not simplify

The Assignment-005 obstruction already has

\[
K(1,2)=1/2,
\qquad
K(2,1)=0,
\]

and the exact numerator

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with negative interior minimum

\[
N(t_*)=-1/1224.
\]

Hence triangular active transfer remains genuinely spectral.

Decisive note: `007c-triangular-still-spectral.md`, commit `c692967d`.

## 7. Exact verifier

`007-natural-subclass-verifier.py`, commit `3a12ba34`.

The verifier uses `Fraction` arithmetic only and checks:

- lumpability and value-lump conditions;
- a physically realizable exchange-symmetric positive gate with `c>a` and `p_1!=p_2`;
- a physically realizable negative long-time row in the same class;
- the refresh identity `Q^2=-RQ`;
- the exact triangular obstruction;
- the binary reduction.

The expected assertion count is 90. No floating-point sign decision or time mesh is used.

## 8. Exact binary reduction

Suppress type `2`. All conditions involving exchange of two active labels disappear. Every binary reference-neighbour generator is automatically a two-state refresh chain.

For

\[
u=c^0(\emptyset),
\qquad
w=c^1(\emptyset),
\]

and outgoing row

\[
p=(c^0(S),-c^0(S)-c^1(S)),
\]

the zero-length `OO` condition is exactly

\[
c^0(S)+c^1(S)\le0.
\]

The long-time inequality becomes

\[
w c^0(S)-u c^1(S)\ge0,
\]

i.e.

\[
c^1(\emptyset)c^0(S)
\ge
c^0(\emptyset)c^1(S).
\]

The zero-length `OI` sign `-c^1(S)>=0` follows from these two inequalities when `u+w>0`, exactly as in Assignment 004. The degenerate case `u+w=0` is the canonical `c\equiv0` clause.

No stronger binary condition survives.

Decisive note: `007d-exact-subclass-criterion-and-binary-reduction.md`, commit `06199715`.

## 9. Ruling

The lumpable-observable route is binary-reducible, and one-way retyping remains spectral. But exchange symmetry plus the already-necessary Metzler ordering produces a genuinely non-binary exact coefficient/endpoint criterion materially simpler than Assignment 006.

Therefore Assignment 007 ends

\[
\boxed{\texttt{CONTINUE-NATURAL-THREE-STATE-SUBCLASS}.}
\]

Applications, convergence, and `d>3` were not started in this block.
