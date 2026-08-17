# Student G 010d checkpoint: `P_*` as an exact perturbation of a nearby reversible product point

**Status:** intermediate durable checkpoint for Assignment 010. This does **not** yet prove `(T)`, but it replaces the informal phrase “soft East perturbation” by an exact fixed-filter comparison with a genuine reversible spin system.

## 1. A nearby point preserving all duration data

At the primary point

\[
P_*=(a,b,c)
=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
\]

put

\[
\varepsilon:=\frac9{10000}.
\]

Define

\[
\boxed{
P_0=(a_0,b,c_0)
:=\left(a-\varepsilon,b,c-\varepsilon\right)
=\left(\frac1{10000},\frac1{10},\frac{999}{1000}\right).
}
\tag{1}
\]

Then, exactly,

\[
B_0=b+c_0-a_0=b+c-a=B,
\tag{2}
\]

and

\[
\omega_0=1-c_0+a_0=1-c+a=\omega.
\tag{3}
\]

Therefore the scalar right-survival weight `w(u)`, the functions `Z_alpha`, the fixed filter

\[
\sigma(u)=1-2e^{-(4/125)u},
\]

and the scalar `z_sigma` are **identical** at `P_0` and `P_*`.

The difference is entirely in the finite-volume spin semigroup and in the centered insertion.

## 2. `P_0` is exactly on the product-reversible surface

At `P_0`,

\[
1-c_0=\frac1{1000},
\qquad
b(1-c_0)=\frac1{10000}=a_0.
\]

Hence

\[
\boxed{b(1-c_0)-a_0=0.}
\tag{4}
\]

The flip-rate ratio is independent of the right neighbour:

\[
\frac{r_{0y}}{r_{1y}}=10,
\qquad y\in\{0,1\}.
\]

Thus the Bernoulli product measure of density

\[
\boxed{p_0=\frac1{1+b}=\frac{10}{11}}
\tag{5}
\]

is reversible for every zero-boundary finite volume at `P_0`.

Equivalently, if

\[
X_i:=B\eta_i-c_0,
\]

then

\[
\mu_0(X_i)=0,
\qquad
\mu_0(X_i^2)=c_0g_0,
\]

where

\[
g_0:=b-a_0=\frac{999}{10000}.
\]

Indeed

\[
c_0g_0=\frac{998001}{10000000}.
\tag{6}
\]

The `X_A` are therefore the product-orthogonal monomials for the genuine invariant law of `P_0`.

## 3. The actual insertion is a small affine perturbation

Because `B` is unchanged,

\[
Y_i=B\eta_i-c
=X_i-\varepsilon.
\]

Thus

\[
\boxed{Y_i=X_i-\varepsilon.}
\tag{7}
\]

This is exactly the recentering hidden in 010c: there `m_0=d/(1+b)=-9/10000=-\varepsilon`, so `X=Y-m_0=Y+\varepsilon`.

In particular, the insertion at `P_*` splits into

\[
\boxed{
M_Y=M_X-\varepsilon I,
}
\tag{8}
\]

where `M_X` is multiplication by the normalized product-centered character of the reversible point.

## 4. The actual generator is a single signed local defect of size `epsilon`

The two models have identical rates when the right neighbour equals `0`:

\[
r_{00}=1,
\qquad
r_{10}=b=\frac1{10}.
\]

When the right neighbour equals `1`,

\[
P_0:\quad r_{01}=\frac1{1000},\quad r_{11}=\frac1{10000},
\]

whereas

\[
P_*:\quad r_{01}=\frac1{10000},\quad r_{11}=\frac1{1000}.
\]

Consequently

\[
L_*=L_0+\varepsilon\sum_{i<N}\mathcal A_i,
\tag{9}
\]

with no perturbation at the right boundary and

\[
\boxed{
(\mathcal A_i f)(\eta)
={\bf1}_{\{\eta_{i+1}=1\}}(2\eta_i-1)
\bigl[f(\eta^i)-f(\eta)\bigr].
}
\tag{10}
\]

The perturbation is signed: at right-neighbour state `1`, it decreases the `0->1` rate by `epsilon` and increases the `1->0` rate by `epsilon`.

On the single centered coordinate, `(10)` is equivalently

\[
\boxed{
(L_*-L_0)X_i
=-\varepsilon X_{i+1}-\varepsilon c_0,
\qquad i<N.
}
\tag{11}
\]

The rightmost coordinate is untouched by the perturbation, and therefore

\[
L_*X_N=-(1+b)X_N
\tag{12}
\]

exactly in every volume.

## 5. Relation to the 010b/010c constants

The recentered constants in 010c are precisely the reversible parameters:

\[
c+m_0=c-\varepsilon=c_0=\frac{999}{1000},
\]

\[
g-m_0=g+\varepsilon=g_0=\frac{999}{10000}.
\tag{13}
\]

Moreover

\[
(c+m_0)(g-m_0)=c_0g_0
=B^2\frac{b}{(1+b)^2},
\tag{14}
\]

so normalizing `X_i` by `sqrt(c_0g_0)` is exactly normalization in `L^2(mu_0)`, not an artificial coefficient scaling.

Finally, at `P_0` the generator can be written as a product-reversible constrained refresh generator.  If `E_{p_0,i}` refreshes site `i` from Bernoulli(`p_0`), then

\[
L_0
=\sum_i R(\eta_{i+1})\bigl(E_{p_0,i}-I\bigr),
\tag{15}
\]

with

\[
R(0)=1+b=\frac{11}{10},
\qquad
R(1)=\omega=\frac{11}{10000}.
\tag{16}
\]

Hence `L_0` is self-adjoint in `L^2(mu_0)` and its Dirichlet form dominates `omega` times the independent-refresh Dirichlet form.  This recovers the number-operator coercivity of 010b from a genuine reversible Markov generator.

## 6. Consequence for the connected-tail problem

The fixed-filter connected problem may now be expanded around a reference model with all of the following properties simultaneously:

1. the duration weight and filter are exactly the same as at `P_*`;
2. the invariant law is an explicit product law;
3. the reference generator is reversible;
4. the reference insertion `X` is exactly centered;
5. the actual insertion differs by the scalar `-epsilon`;
6. the actual dynamics differs by the local signed defect `(10)`, also of size `epsilon`;
7. the fresh right-boundary mode is completely unperturbed.

This is stronger than treating `dD` by absolute operator norm.  In particular, every loss of reversibility is now tagged by an explicit local `epsilon` defect, while the reference propagation can be handled before absolute values are taken.

The next viable target is therefore a connected/cluster estimate for the fixed filter in which the `P_0` propagation is summed exactly and only the defect insertions `(8)` and `(10)` are counted.  A crude global perturbation bound is not sufficient, since `epsilon/omega=9/11`; locality and the fresh-boundary high-frequency channel must be retained.
