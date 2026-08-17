# Student G 010: connected dual-renewal tail decision

## Verdict

I do **not** prove the Assignment-010 tail theorem

\[
\sum_{k\ge8}|\lambda_k|<\delta_7
\tag{T}
\]

and I do not obtain another all-depth theorem implying `rho_J(P_*)>1` for the fixed filter.  I also do **not** refute the fixed dual-renewal witness.

The block nevertheless produces a genuine all-depth positive-frequency theorem which is substantially stronger than the one-step obstruction in 010a.  The terminal stationary insertion supplies an exact rational high-pass factor

\[
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
\]

For the actual fixed filter, `R_NQ_N` is convolution with a depth-independent signed time kernel `kappa`.  Exact algebra proves

\[
\|\kappa\|_{L^1}\le\Theta_\sharp,
\qquad
\Theta_\sharp<0.892472,
\]

and, crucially,

\[
\boxed{B\Theta_\sharp<1}
\tag{0.1}
\]

with exact value bounded by

\[
B\Theta_\sharp
\approx0.9807372831525678.
\]

Hence a complete centered insertion followed by the terminal high-pass connected resolvent is a strict, depth-uniform oscillation contraction.

The reason this does not iterate is now precise.  The high-pass multiplier is

\[
R(x)=\frac{d+gx}{1+b+x}
\]

on a mode with `L=-x`, and it has the exact positive-frequency zero

\[
\boxed{x_0=\frac{|d|}{g}=\frac1{100}.}
\tag{0.2}
\]

Thus no scalar functional-calculus inverse of `R` can convert the high-pass norm back into the unfiltered connected norm uniformly over positive frequencies.  More importantly, the actual connected coefficient can be written exactly as

\[
\boxed{
 c_{N+1}
 =\delta_N\!\left(R_NQ_Nf_N\right),
}
\tag{0.3}
\]

where

\[
\delta_N=\bar\pi_{N+1}-\pi_N,
\qquad
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1}.
\]

The remaining object is therefore a **filtered stationary boundary response evaluated on the special connected orbit**.  It is not the unrestricted tail-shift norm of F013--F014.  Proving equivalence would require a new theorem showing that the test family `R_NQ_Nf_N` norms arbitrary remote observables; no such theorem is obtained here and it does not follow from the existing algebra.

Accordingly the stopping outcome is:

> **unresolved after substantive work; connected-tail blocker:** the exact fixed-filter terminal high-pass is uniformly contractive, but the contraction is measured through `R_N`, which has a genuine positive-frequency zero, while the remaining coefficient is the special filtered boundary-response pairing `(0.3)`.  What is missing is an orbit-specific estimate for that pairing (or a complementary high-pass observable); this is strictly narrower than bare tail-shift agreement and strictly sharper than F009's growing-mode obstruction.

## 1. Exact positive core and soft perturbation

Checkpoint `010b-positive-core-soft-perturbation-checkpoint.md` rewrites the canonical `Y` coefficient dynamics after the degree transform

\[
x_A=g^{|A|}q_A.
\]

With

\[
\alpha=\frac{|d|}{g}=\frac1{100},
\]

one has exactly

\[
\widehat L=\widehat L^+-\alpha\mathsf D.
\]

The positive core is a set process with birth rate `g`, coalescence rate `c`, and Feynman--Kac killing `omega|A|`.  In particular

\[
\|e^{tL^+}f\|_g\le e^{-\omega t}\|f\|_g.
\]

Moreover, in the Bernoulli(`c/B`) product Hilbert basis,

\[
-\langle f,L^+f\rangle
\ge\omega\langle f,\mathcal Nf\rangle.
\]

This proves that the obstruction in 010a is genuinely the signed deletion channel: taking it in absolute value costs `alpha=0.01`, larger than `omega=0.0011`.

## 2. Exact last-coordinate recursion

Checkpoint `010c-last-coordinate-block-checkpoint.md` gives the exact `Y`-basis block recursion.  If `P_N` selects monomials containing the old boundary site `N`, then

\[
L_{N+1}
=
\begin{pmatrix}
L_N+cP_N & dI+gcP_N\\
P_N & L_N-(1+b)I+gP_N
\end{pmatrix}.
\tag{2.1}
\]

After product-orthogonal normalization the only asymmetric new-interface term is the scalar `d` defect.

The newest centered boundary singleton is an exact all-volume eigenfunction.  With

\[
m_0=\frac d{1+b}=-\frac9{10000},
\qquad
\psi_N=Y_N-m_0,
\]

\[
L_N\psi_N=-(1+b)\psi_N.
\]

For the fixed filter,

\[
Q_NY_N=q(1+b)(Y_N-m_0),
\]

and exactly

\[
q(1+b)
=-\frac{5240305525}{6117276447}
\approx-0.8566402991.
\]

Thus a scalar created by one centering subtraction becomes a fixed fast mode after the next insertion; it does not re-enter as an uncontrolled zero mode.

## 3. Exact stationary high-pass identity

Let

\[
A_N(f)=\pi_{N+1}(f),
\qquad
C_N(f)=\pi_{N+1}(Y_{N+1}f).
\]

Stationarity applied to the two blocks in `(2.1)` yields

\[
A_N(L_N+cP_N)+C_NP_N=0,
\]

\[
A_N(dI+gcP_N)+C_N(L_N-(1+b)I+gP_N)=0.
\]

Eliminating `A_NP_N` cancels every `P_N` term and gives

\[
\boxed{
C_N=A_NR_N,
\qquad
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
}
\tag{3.1}
\]

At `P_*`, with

\[
\varepsilon=\frac9{10000},
\qquad
g_0=g+\varepsilon=\frac{999}{10000},
\qquad r=1+b,
\]

\[
R_N=gI-g_0K_N,
\qquad
K_N=r(rI-L_N)^{-1}
=\int_0^\infty re^{-rt}P_t^Ndt.
\tag{3.2}
\]

This is an exact stationary boundary high-pass identity, not an approximation by equilibrium.

## 4. Depth-independent terminal kernel

Put

\[
h(t)=w_*(t)\sigma(t).
\]

Since `R_N` is a rational function of `L_N`, it commutes with `H_N`, `Q_N`, and `Pi_N`, and

\[
R_N\Pi_N=-\varepsilon\Pi_N.
\]

Modulo constants,

\[
R_NQ_N=R_NH_N
=\int_0^\infty\kappa(t)P_t^Ndt,
\]

where

\[
\boxed{
\kappa=gh-g_0(k_r*h),
\qquad
k_r(t)=re^{-rt}.
}
\tag{4.1}
\]

The kernel `kappa` is independent of `N`.

The exact verifier `010e-terminal-kernel-verifier.py` writes `kappa` as five algebraic exponentials.  The coefficientwise triangle bound is

\[
\|\kappa\|_1<0.982981.
\]

A signed pairing of the slow negative exponential with its `tau`-shifted positive partner on `[3,50]` gives a strictly better exact bound.  The verifier proves

\[
\frac pn>7,
\]

for the paired coefficients, while

\[
e^{8/5}<\left(\frac{25}{21}\right)^{10}<6<7.
\]

Using only `e^{-x}>=1-x` for the saved integral gives

\[
\boxed{
\|\kappa\|_1
\le\Theta_\sharp
\approx0.8924718201406568,
}
\tag{4.2}
\]

and verifies exactly

\[
\boxed{B\Theta_\sharp<1.}
\tag{4.3}
\]

No spectral gap or finite-volume asymptotic enters.

## 5. Sandwiched connected contraction

Every output of `Q_N` has zero `pi_N` mean, so its range contains zero.  If `f` has range containing zero, multiplication by the new insertion satisfies

\[
\operatorname{osc}(Y_{N+1}f)
\le(c+g)\operatorname{osc}(f)
=B\operatorname{osc}(f).
\tag{5.1}
\]

Combining `(4.2)`--`(5.1)` gives the uniform theorem

\[
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le
q_\sharp\operatorname{osc}(f),
\qquad
q_\sharp:=B\Theta_\sharp<1.
}
\tag{5.2}
\]

This is the bounded-step/sign-sensitive mechanism explicitly left open by 010a.  Cancellation occurs in the fixed positive-frequency time kernel before absolute values are taken.

The failure to finish `(T)` is therefore not failure to find any contraction.  It is failure to **iterate** `(5.2)` without losing the high-pass factor `R_N`.

## 6. Exact filtered tail-shift interface

Let

\[
\delta_N=A_N-\pi_N=\bar\pi_{N+1}-\pi_N.
\]

Since

\[
\pi_NR_NQ_N=0,
\]

`(3.1)` gives exactly

\[
\boxed{
 c_{N+1}
 =\delta_N(R_NQ_Nf_N).
}
\tag{6.1}
\]

The same stationarity identity gives a local source equation for `delta_N`:

\[
\delta_NL_N=-A_N(cI+R_N)P_N.
\]

Using

\[
cr+d=B,
\qquad c+g=B,
\]

one obtains

\[
\boxed{
 cI+R_N
 =B(I-L_N)(rI-L_N)^{-1},
}
\tag{6.2}
\]

and hence

\[
\boxed{
\delta_NL_N
=-B A_N(I-L_N)(rI-L_N)^{-1}P_N.
}
\tag{6.3}
\]

Thus the remaining coefficient is a zero-frequency spatial boundary response only after it has been tested against the special connected high-pass orbit.

This is materially different from F013/F014.  Their obstruction is the **unrestricted** remote operator norm of `delta_N` or `delta_N^(2)`, and they prove equivalence to bare tail-shift variation up to localized covariance.  Equation `(6.1)` asks only for one specific test family.  No implication from `(6.1)` to bare tail-shift, or conversely, is proved here.

## 7. Recentered newest-boundary block

Checkpoint `010h-recentered-boundary-block-checkpoint.md` further isolates the residual local defect.  Define

\[
X_i=Y_i+\varepsilon=B\eta_i-c_0,
\qquad
c_0=\frac{999}{1000},
\qquad
g_0=\frac{999}{10000}.
\]

Then `X_N` is centered for the autonomous zero-boundary spin law and

\[
Y_N=X_N-\varepsilon.
\]

The newest-coordinate block becomes

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & g_0c_0P_N\\
P_N & L_N-rI+g_0P_N
\end{pmatrix}
}
\tag{7.1}
\]

in the unnormalised `X` decomposition.  After normalizing `X` by `sqrt(c_0g_0)`, the two off-diagonal blocks are equal.  Thus the newest interface itself is symmetric; all nonreversibility is inherited through the older block.

The scalar branch `-epsilon` is already harmless.  Since

\[
|\sigma(t)|\le1+2e^{-\tau t},
\]

\[
\boxed{
\varepsilon\int_0^\infty|h(t)|dt
\le
\varepsilon(Z_\omega+2Z_{\omega+\tau})
=
\frac{4171497}{6860300}
<0.609.
}
\tag{7.2}
\]

So the remaining mechanism is specifically transmission through the boundary-containing `X` component, not the affine recentering defect.

## 8. Why I stop here

Three facts now coexist:

1. a full insertion plus terminal high-pass has the exact strict contraction `(5.2)`;
2. the high-pass factor has the exact positive-frequency zero `(0.2)`, so a one-high-pass functional-calculus norm cannot simply be inverted;
3. the coefficient itself is the special filtered boundary-response pairing `(6.1)`, not an arbitrary connected-space norm.

I tried the natural next moves suggested by these facts: direct inversion of `R`, a scalar perturbation of the positive core, and generic centered-profile total variation.  They do not close.  The first is algebraically blocked by `(0.2)`; the second loses the required cancellation (`|d|/g>omega`); the third is much too large on arbitrary zero-mass profiles and would merely return to the stopped profile problem.

The plausible remaining repair is a **complementary high-pass observable** or a theorem specific to the actual orbit in `(6.1)`.  That is a new theorem, not a minor extension of the present estimates.  Under Assignment 010's bounded-block stopping rule, I do not start another search for such a norm here.

## Durable files from this block

- `010a-canonical-y-generator-checkpoint.md` -- accepted starting checkpoint;
- `010b-positive-core-soft-perturbation-checkpoint.md` -- exact positive core and coercivity;
- `010c-last-coordinate-block-checkpoint.md` -- exact newest-coordinate block and fast singleton;
- `010d-nearby-reversible-point-checkpoint.md` -- corrected frozen-weight reversible comparison;
- `010e-terminal-connected-kernel-checkpoint.md` -- exact stationary high-pass and terminal kernel;
- `010e-terminal-kernel-verifier.py` -- exact algebraic kernel certificate, including the sharpened bound;
- `010f-sandwiched-oscillation-contraction-checkpoint.md` -- `B Theta_sharp<1` contraction;
- `010g-filtered-tail-shift-interface-checkpoint.md` -- exact identity `(6.1)` and source equation `(6.3)`;
- `010h-recentered-boundary-block-checkpoint.md` -- symmetric newest-boundary block and scalar-branch contraction;
- this file -- Assignment-010 decision.
