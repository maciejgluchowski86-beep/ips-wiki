# 004a: exact signed interior transfer

Date: 2026-08-17

This note executes Part A of Assignment 004. It derives the unnormalized signed transfer directly from the local Poisson construction used in Assignments 001--003.

## 1. Local data

Fix a source site `i`. Write

\[
E=\{0,1,\ldots,d-1\},\qquad E_*=E\setminus\{0\}.
\]

For active source type `r in E_*`, source outcome `s in E`, and typed target `tau`, the signed dual branch coefficient is

\[
a_{i,r}^s(\tau).
\]

The empty-target source-survival branch `(s,tau)=(r,emptyset)` is diagonal and is not a Poisson jump. Every other branch has rate

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|
\]

and sign

\[
\epsilon_{i,r}^s(\tau)=\operatorname{sgn}_{\pm}a_{i,r}^s(\tau).
\]

For the source-line interior define

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
\tag{1.1}
\]

and the matching nonempty-target hazard

\[
\kappa_{i,r}
=\sum_{\tau\ne\emptyset}\sum_{s\in E}|a_{i,r}^s(\tau)|.
\tag{1.2}
\]

By Assignment 001 the local Feynman--Kac potential is

\[
v_{i,r}
=\rho_{i,r}+\kappa_{i,r}+a_{i,r}^r(\emptyset).
\tag{1.3}
\]

For the inactive local state put `v_{i,0}=0`.

## 2. Weighted killed source-line process

Inside a patch, consistency forbids every nonempty-target clock whose revealed source type matches the current local type. Hence, while the source-line state is `r in E_*`:

- each empty-target branch `r -> s`, `s != r`, rings at rate `|a_{i,r}^s(emptyset)|`, changes the local state to `s`, and multiplies the intrinsic weight by its sign;
- the path is killed at rate `kappa_{i,r}` by a matching nonempty-target clock;
- between marks, it receives potential `v_{i,r}`.

State `0` is inactive: no source-typed clock can act there and its potential is zero, so it is absorbing for the local interior dynamics.

For a terminal test function `F:E -> R`, define

\[
(T_tF)(x)
=
E_x\left[
\epsilon_{\emptyset}(0,t)
\exp\left(\int_0^t v_{i,X_u}\,du\right)
1_{\{\zeta>t\}}F(X_t)
\right],
\tag{2.1}
\]

where `zeta` is the first matching nonempty-target clock and `epsilon_emptyset(0,t)` is the product of signs of effective empty-target jumps.

## 3. Infinitesimal derivation

Fix `r in E_*`. In an interval of length `h`, up to `o(h)`:

- no empty-target jump and no killing occurs with probability
  \[
  1-(\rho_{i,r}+\kappa_{i,r})h;
  \]
- the empty-target branch `r -> s`, `s != r`, occurs with probability
  \[
  |a_{i,r}^s(\emptyset)|h;
  \]
- a matching nonempty-target mark kills the path and contributes zero.

Multiplication by the potential contributes `1+v_{i,r}h+o(h)`. Therefore

\[
\begin{aligned}
T_hF(r)
={}&F(r)
+h\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
\bigl(\epsilon_{i,r}^s(\emptyset)F(s)-F(r)\bigr)\\
&-h\kappa_{i,r}F(r)
+h v_{i,r}F(r)+o(h).
\end{aligned}
\tag{3.1}
\]

Since

\[
|a_{i,r}^s(\emptyset)|\epsilon_{i,r}^s(\emptyset)
=a_{i,r}^s(\emptyset)
\]

and (1.3) gives

\[
-\rho_{i,r}-\kappa_{i,r}+v_{i,r}
=a_{i,r}^r(\emptyset),
\]

we obtain the exact cancellation

\[
\boxed{
(K_iF)(r)=\sum_{s\in E}a_{i,r}^s(\emptyset)F(s),
\qquad r\in E_*.
}
\tag{3.2}
\]

For the inactive state,

\[
\boxed{(K_iF)(0)=0.}
\tag{3.3}
\]

Thus the signed killed Feynman--Kac transfer is a fixed finite-dimensional semigroup

\[
\boxed{T_t=e^{tK_i},}
\tag{3.4}
\]

where the row of `K_i` indexed by `0` is zero and every active row is exactly the vector of empty-target signed coefficients.

This proves the candidate identity in Assignment 004 Part A. It is not heuristic generator bookkeeping: (3.1) comes directly from the competing local Poisson clocks, killing event, and potential.

## 4. Structural consequences

1. **Nonempty-target coefficients disappear from the numerator interior generator.** They still determine selected-boundary vectors and the consistency denominator, but their interior no-success hazards cancel against the corresponding term in the potential.

2. **Retyping remains visible.** For `r,s in E_*`, `s != r`, the off-diagonal entry
   \[
   K_i(r,s)=a_{i,r}^s(\emptyset)
   \]
   can have either sign.

3. **Deletion remains visible.** The entry
   \[
   K_i(r,0)=a_{i,r}^0(\emptyset)
   \]
   transfers weighted mass to the inactive state.

4. **The inactive row is not the coefficient row of a physical source type.** There is no dual source type `0`; state `0` simply records local inactivity and is absorbing between incoming boundaries.

The denominator transfer is different because it contains neither signs nor the Feynman--Kac potential. It is derived separately in 004b.
