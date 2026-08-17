# Student G 010i checkpoint: reversible fresh insertion gains one half derivative

**Status:** intermediate durable checkpoint for Assignment 010.  This gives a dimension-free positive-frequency estimate for the fixed filter at the nearby reversible reference point `P_0`, with the **actual** Assignment-010 duration weight held frozen.  It does not yet control the full `P_*` connected orbit; the remaining issue is stability of this fresh-insertion estimate under the actual nonreversible spatial defect.

## 1. Reference operator and fixed scalar multiplier

Use the corrected reversible reference point from 010d,

\[
P_0=(a_0,b,c_0)
=\left(\frac1{10000},\frac1{10},\frac{999}{1000}\right),
\]

with product reversible law

\[
\mu_0={\rm Bernoulli}(10/11)^{\otimes N}.
\]

Keep the **actual** `P_*` duration weight and fixed filter.  Put

\[
A_{0,N}:=-L_{0,N}\ge0
\]

on `L^2(mu_0)`.  Since `L_{0,N}` is self-adjoint, the frozen filtered operator is the scalar functional calculus

\[
\widetilde H_{0,N}^\sigma=q(A_{0,N}),
\]

where

\[
\boxed{
q(x)=Z_{\omega+x}-2Z_{\omega+\tau+x},
\qquad x\ge0,
}
\tag{1}
\]

and `Z`, `omega`, `tau` are the actual `P_*` scalar data.

The exact rational function is

\[
q(x)=
-100\,
\frac{
2500000000x^3+10507750000x^2+10879253250x-340242903
}{
(100000x^2+210210x+341)
(2500000x^2+5415250x+179253)
}.
\tag{2}
\]

Let `num/den` denote the reduced numerator and denominator in `(2)`.  Direct expansion gives

\[
\begin{aligned}
den-x\num
={}&500000000000x^4
+2117825000000x^3\\
&+2245042827500x^2
+5503083080x
+61125273,
\end{aligned}
\tag{3}
\]

and

\[
\den+x\num
=16275000000x^3
+69192177500x^2
+73551663680x
+61125273.
\tag{4}
\]

Every coefficient in `(3)`--`(4)` is strictly positive.  Since `den>0` on `[0,infty)`,

\[
\boxed{|xq(x)|<1\quad\text{for every }x>0.}
\tag{5}
\]

The companion verifier `010i-fresh-insertion-sobolev-verifier.py` checks `(2)`--`(5)` exactly.

## 2. Exact variational estimate for a fresh centered insertion

Recall the product-centered coordinate

\[
X_i=B\eta_i-c_0,
\qquad
\mu_0(X_i)=0,
\qquad
\mu_0(X_i^2)=c_0g_0,
\]

with

\[
g_0=\frac{999}{10000},
\qquad
c_0g_0=\frac{998001}{10000000}.
\]

Let `M_X` append the fresh rightmost coordinate:

\[
M_Xf=X_Nf,
\]

for `f` on the first `N-1` sites.  At the zero right boundary the new site is refreshed at the fixed rate

\[
r=1+b=\frac{11}{10}.
\]

For arbitrary `h` on `N` sites, write `E_Nh` for conditional expectation over the fresh coordinate under `mu_0`.  Product centering gives

\[
\langle M_Xf,h\rangle_{\mu_0}
=
\langle M_Xf,h-E_Nh\rangle_{\mu_0},
\]

hence

\[
|\langle M_Xf,h\rangle|
\le
\sqrt{c_0g_0}\,\|f\|_2\,\|h-E_Nh\|_2.
\tag{6}
\]

The site-`N` contribution to the Dirichlet form is exactly

\[
\langle h,A_{0,N}h\rangle
\ge
r\|h-E_Nh\|_2^2.
\tag{7}
\]

Using the variational formula for the inverse of a positive self-adjoint operator on the centered subspace,

\[
\langle g,A_{0,N}^{-1}g\rangle
=
\sup_h\left\{2\langle g,h\rangle-\langle h,A_{0,N}h\rangle\right\},
\]

`(6)`--`(7)` give

\[
\boxed{
M_X^*A_{0,N}^{-1}M_X
\le
\frac{c_0g_0}{r}I
=rac{998001}{11000000}I.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\|A_{0,N}^{-1/2}M_Xf\|_2
\le
\sqrt{\frac{998001}{11000000}}\,\|f\|_2.
}
\tag{9}
\]

No spectral gap estimate enters `(8)`.

## 3. The fixed filter turns the half-derivative gain into an `H^1` bound

Because `M_Xf` has zero `mu_0`-mean, the invariant subtraction in the connected operator vanishes on this input:

\[
\widetilde Q_{0,N}^\sigma M_Xf
=q(A_{0,N})M_Xf.
\]

By `(5)`, spectral calculus gives

\[
\|A_{0,N}q(A_{0,N})\|_{2\to2}\le1.
\]

Combining with `(9)`,

\[
\begin{aligned}
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma M_Xf\|_2
&=
\|A_{0,N}q(A_{0,N})A_{0,N}^{-1/2}M_Xf\|_2\\
&\le
\sqrt{\frac{998001}{11000000}}\,\|f\|_2.
\end{aligned}
\]

Thus

\[
\boxed{
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma M_Xf\|_2
\le0.30121\,\|f\|_2
}
\tag{10}
\]

uniformly in depth.

This is a genuine fresh-insertion positive-frequency theorem: the enormous zero-frequency value `q(0)=z_sigma` never appears.  The insertion supplies an exact negative Sobolev gain, while the filter supplies the compensating factor `xq(x)`.

## 4. The actual insertion `Y=X+m_0` still has a strict reference margin

At `P_*`, and hence in the frozen comparison,

\[
Y_i=X_i+m_0,
\qquad
m_0=-\frac9{10000}.
\]

For the scalar part, the corrected 010h checkpoint gives the exact bound

\[
\|h\|_1<\frac{881295044}{1453125}<625.
\tag{11}
\]

Together with `(5)`,

\[
x|q(x)|^2
=|xq(x)|\,|q(x)|
<625,
\]

so

\[
\boxed{
\sup_{x\ge0}\sqrt{x}|q(x)|<25.
}
\tag{12}
\]

The invariant subtraction is invisible after applying `A_{0,N}^{1/2}`.  Therefore, for arbitrary `f`,

\[
\boxed{
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le
\left(
\sqrt{\frac{998001}{11000000}}
+rac9{400}
\right)\|f\|_2.
}
\tag{13}
\]

The parenthesis is approximately `0.32371` and is strictly below one.  The verifier checks this margin exactly by squaring the rational inequality

\[
\frac{998001}{11000000}<\left(1-\frac9{400}\right)^2.
\]

## 5. What remains at `P_*`

Estimate `(13)` is not yet an iterable norm for the actual connected orbit.  It maps an `L^2(mu_0)` input to one derivative measured by the reversible reference generator.  A naive use of the reference spectral gap to return from this `H^1` norm to `L^2` loses the margin and is not acceptable.

The next target is therefore sharply defined: exploit the **local** form of

\[
L_*-L_0
\]

and the fresh-coordinate structure to propagate the reference `H^1` gain through the actual connected transfer without paying a depth-dependent perturbation norm.  The exact recentered boundary tilt from corrected 010h is the natural local bookkeeping variable for this step.

This route is different from bare tail shift and from a generic mode closure: `(8)` is an all-depth variational inequality tied specifically to the fresh inserted coordinate, and `(5)` uses the fixed Assignment-010 rational filter exactly.
