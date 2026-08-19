# Dimer Metropolis Ising: centered-basis Metzler positivity survives

Date: 2026-08-19

This note records a correction to the pessimistic interpretation of the dimer block-end counterexample. The same interacting two-site Metropolis block-flip model whose individual terminal block patch has a negative centered coefficient nevertheless has a Metzler generator in the centered-monomial basis at the profile `p_i=1/2`. Thus the semigroup can preserve the centered-moment cone through cancellation between successful skeletons even when individual skeleton weights are not nonnegative.

## Model

Take the one-dimensional zero-field ferromagnetic Ising Hamiltonian

\[
H(\sigma)=-J\sum_i \sigma_i\sigma_{i+1},
\qquad
\sigma_i=2\eta_i-1,
\qquad J>0,
\]

with the fixed dimer partition `Q_n={2n,2n+1}`. At a clock of `Q_n`, flip both spins in the dimer and accept at Metropolis rate

\[
c_{Q_n}(\eta)=\min\{1,e^{-\beta\Delta_{Q_n}H(\eta)}\}.
\]

For one dimer `Q={1,2}` with outside neighbours `0,3`, write

\[
\rho=e^{-4\beta J}\in(0,1].
\]

The rate is `rho` exactly when both boundary bonds `(0,1)` and `(2,3)` are aligned, and is `1` otherwise.

## Center at one half

Set

\[
x_i=\eta_i-\frac12=\frac{\sigma_i}{2},
\qquad
x_A=\prod_{i\in A}x_i.
\]

The exact centered expansion of the dimer rate is

\[
\boxed{
c_Q(x)
=\frac{3+\rho}{4}
+(\rho-1)x_0x_1
+(\rho-1)x_2x_3
+4(\rho-1)x_0x_1x_2x_3.
}
\]

A simultaneous flip of sites `1,2` sends `x_1,x_2` to their negatives. Hence

\[
L_Qx_A=0
\qquad\text{if }|A\cap Q|\text{ is even},
\]

while

\[
L_Qx_A=-2c_Q(x)x_A
\qquad\text{if }|A\cap Q|\text{ is odd}.
\]

Since `x_i^2=1/4`, for any finite `E`,

\[
x_Ex_A=4^{-|A\cap E|}x_{A\triangle E}.
\]

Therefore every nonconstant centered rate coefficient `\widehat c_Q(E)` contributes the off-diagonal centered-basis coefficient

\[
\boxed{
[L_Q]_{A,A\triangle E}
=-2\widehat c_Q(E)4^{-|A\cap E|}
}
\]

when `|A cap Q|` is odd. In the dimer Metropolis rate all three nonconstant centered coefficients are nonpositive for `0<rho<1`:

\[
\widehat c_Q(\{0,1\})=\rho-1,
\qquad
\widehat c_Q(\{2,3\})=\rho-1,
\qquad
\widehat c_Q(\{0,1,2,3\})=4(\rho-1).
\]

Thus every off-diagonal centered-basis coefficient is nonnegative. The exact verifier checks the full `16 x 16` local action; there are 24 nonzero off-diagonal coefficients, each a positive rational multiple of `1-rho`.

Hence for every interacting point `beta J>0`,

\[
\boxed{L_Q\text{ is Metzler in the }p_i=1/2\text{ centered-monomial basis}.}
\]

Because the full finite-volume generator is a sum of these dimer terms, it is Metzler in the global centered-monomial basis at `p_i=1/2`. The same finite-volume matrix-exponential and finite-propagation argument used in the binary paper therefore yields

\[
\mu\preceq_*\nu
\Longrightarrow
\mu P_t\preceq_*\nu P_t,
\qquad
p_i^*=\frac12,
\]

and preservation of `M_*`, for this dimer dynamics.

## The one-half centering is forced

For `0<rho<1`, the local Metzler property on the four-site window `{0,1,2,3}` forces all four centering coordinates to equal `1/2`.

For a general profile `p=(p_0,p_1,p_2,p_3)`, the coefficient from `A={1,2}` to `B={0,3}` is exactly

\[
(\rho-1)
\left[
2\left(p_1-\frac12\right)^2
+2\left(p_2-\frac12\right)^2
\right].
\]

Since `rho-1<0`, Metzler nonnegativity forces

\[
p_1=p_2=\frac12.
\]

After this substitution, the coefficients

\[
[A=\{1\}\to B=\varnothing]
= -\frac{(2p_0-1)(\rho-1)}4,
\]

and

\[
[A=\{0,1\}\to B=\{0\}]
= \frac{(2p_0-1)(\rho-1)}4
\]

force `p_0=1/2`. Symmetrically,

\[
[A=\{2\}\to B=\varnothing]
= -\frac{(2p_3-1)(\rho-1)}4,
\]

and

\[
[A=\{2,3\}\to B=\{3\}]
= \frac{(2p_3-1)(\rho-1)}4
\]

force `p_3=1/2`.

Thus the interacting dimer has the unique local Metzler centering

\[
\boxed{p_0=p_1=p_2=p_3=\frac12.}
\]

## A small general block-flip criterion

The same algebra gives an exact criterion for a single full-block flip term centered at `1/2`. Let

\[
L_Qf(\eta)=c_Q(\eta)(f(\eta^Q)-f(\eta)),
\]

and expand its rate in the half-centered basis as

\[
c_Q(x)=\widehat c_Q(\varnothing)+\sum_{E\ne\varnothing}\widehat c_Q(E)x_E.
\]

Then, for every centered monomial `x_A` with odd `|A cap Q|`, the coefficient from `A` to `A triangle E` is

\[
-2\widehat c_Q(E)4^{-|A\cap E|}.
\]

Since `E -> A triangle E` is injective, there is no cancellation between distinct rate modes in a fixed matrix entry. Therefore the local generator is Metzler at `1/2` if and only if

\[
\boxed{
\widehat c_Q(E)\le0
\quad\text{for every nonempty }E.
}
\]

This is a genuine multi-site class with centered-order preservation. Constant-rate block flips are the degenerate case; the dimer Metropolis model is a nonconstant interacting example.

## Relation to the negative block-end result

The previous exact terminal-patch computation gave

\[
C_Q(u_1,u_2)=\frac{1-u_2}{2},
\qquad
\kappa_{\{2\}}=-\frac12.
\]

There is no contradiction. Nonnegative centered coefficients of every terminal patch are a sufficient mechanism for making each successful-skeleton weight nonnegative. The Metzler calculation proves positivity only after summing over all skeletons. The dimer therefore demonstrates the strict distinction

\[
\boxed{
\text{centered end-patch positivity can fail while centered semigroup positivity holds}.}
\]

This means centered-moment order is not generically inherited from block-patch positivity, but it can survive by an independent generator-level coefficient mechanism.

## What this does and does not restore

Established for the interacting dimer Metropolis dynamics at `p^*=1/2`:

- finite-volume centered-basis Metzler positivity;
- preservation of the centered-moment cone `M_*` and order `preceq_*` by the same matrix-exponential argument as the paper;
- the ordinary monomial comparisons and product-profile comparisons that are purely downstream of `preceq_*`.

Established more generally for a single full-block flip term centered at `1/2`:

- the exact coefficient criterion `\widehat c_Q(E)<=0` for every nonempty centered rate mode.

Not restored by this result:

- block or hyperpatch factorization/representation, which remain plausible but unproved in the multi-site extension;
- nonnegative successful-skeleton weights;
- the paper's pure-death comparison;
- the common invariant-limit theorem or its exponential rate;
- uniform unique ergodicity.

In particular, the pure-death comparison still needs componentwise monotonicity under the hidden-history tilt `exp(-epsilon int |X_u|du)`, and the convergence proof still lacks the exact outgoing-patch death factor. Metzler positivity of one semigroup does not supply either ingredient.