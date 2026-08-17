# Student G 010d checkpoint: exact nearby reversible generator and frozen-weight comparison

**Status:** intermediate durable checkpoint for Assignment 010. This does **not** yet prove `(T)`.  A correction made immediately after the first version is incorporated here: preserving `B` and `omega` does **not** preserve the canonical duration weight, because the one-particle survival factor depends on `a` separately.  The reversible point below is therefore a reference for the finite-volume generator and insertion algebra, while the actual `P_*` duration weight must be kept frozen externally.

## 1. A nearby point preserving `B` and `omega`, but not `w`

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

However the canonical survival transform is

\[
Z_\alpha(a)
=\frac{\alpha+1+B+a}{(\alpha+a)(\alpha+1+B)-a},
\tag{4}
\]

so changing `a` changes `s_1(u)` and hence changes the canonical weight

\[
w(u)=e^{-\omega u}s_1(u).
\]

Thus the canonical `P_0` duration weight and `z_sigma` are **not** the ones used in Assignment 010.  No argument below identifies them.

For comparison with the actual connected operator, keep instead the actual weight

\[
w_*(u):=w_{P_*}(u)
\]

fixed and define the auxiliary reversible-semigroup operator

\[
\widetilde H_{0,N}^\sigma
:=\int_0^\infty w_*(u)\sigma(u)e^{uL_{0,N}}\,du,
\tag{5}
\]

\[
\widetilde Q_{0,N}^\sigma
:=\widetilde H_{0,N}^\sigma-z_*\Pi_{0,N},
\qquad
z_*:=\int_0^\infty w_*(u)\sigma(u)\,du.
\tag{6}
\]

This is not the canonical dual operator of the model `P_0`; it is an auxiliary comparison operator using the **actual Assignment-010 weight** and the reversible reference semigroup.  With this convention, the difference between `H_*` and `\widetilde H_0` comes only from the finite-volume semigroups.

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
\tag{7}
\]

The flip-rate ratio is independent of the right neighbour:

\[
\frac{r_{0y}}{r_{1y}}=10,
\qquad y\in\{0,1\}.
\]

Thus the Bernoulli product measure of density

\[
\boxed{p_0=\frac1{1+b}=\frac{10}{11}}
\tag{8}
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
\tag{9}
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
\tag{10}
\]

This is exactly the recentering hidden in 010c: there `m_0=d/(1+b)=-9/10000=-\varepsilon`, so `X=Y-m_0=Y+\varepsilon`.

In particular, the insertion at `P_*` splits into

\[
\boxed{M_Y=M_X-\varepsilon I.}
\tag{11}
\]

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
\boxed{
L_*=L_0+\varepsilon\sum_{i<N}\mathcal A_i,
}
\tag{12}
\]

with no perturbation at the right boundary and

\[
\boxed{
(\mathcal A_i f)(\eta)
={\bf1}_{\{\eta_{i+1}=1\}}(2\eta_i-1)
\bigl[f(\eta^i)-f(\eta)\bigr].
}
\tag{13}
\]

The perturbation is signed: at right-neighbour state `1`, it decreases the `0->1` rate by `epsilon` and increases the `1->0` rate by `epsilon`.

On the single centered coordinate, `(13)` is equivalently

\[
\boxed{
(L_*-L_0)X_i
=-\varepsilon X_{i+1}-\varepsilon c_0,
\qquad i<N.
}
\tag{14}
\]

The rightmost coordinate is untouched by the perturbation, and therefore

\[
L_*X_N=-(1+b)X_N
\tag{15}
\]

exactly in every volume.

## 5. Relation to the 010b/010c constants

The recentered constants in 010c are precisely the reversible parameters:

\[
c+m_0=c-\varepsilon=c_0=\frac{999}{1000},
\]

\[
g-m_0=g+\varepsilon=g_0=\frac{999}{10000}.
\tag{16}
\]

Moreover

\[
(c+m_0)(g-m_0)=c_0g_0
=B^2\frac{b}{(1+b)^2},
\tag{17}
\]

so normalizing `X_i` by `sqrt(c_0g_0)` is exactly normalization in `L^2(mu_0)`, not an artificial coefficient scaling.

At `P_0` the generator can be written as a product-reversible constrained refresh generator.  If `E_{p_0,i}` refreshes site `i` from Bernoulli(`p_0`), then

\[
L_0
=\sum_i R(\eta_{i+1})\bigl(E_{p_0,i}-I\bigr),
\tag{18}
\]

with

\[
R(0)=1+b=\frac{11}{10},
\qquad
R(1)=\omega=\frac{11}{10000}.
\tag{19}
\]

Hence `L_0` is self-adjoint in `L^2(mu_0)` and its Dirichlet form dominates `omega` times the independent-refresh Dirichlet form.  This recovers the number-operator coercivity of 010b from a genuine reversible Markov generator.

Because the auxiliary operator `(5)` is a real scalar function of the self-adjoint `L_0`, `\widetilde H_{0,N}^sigma` and `\widetilde Q_{0,N}^sigma` are also self-adjoint in `L^2(mu_0)`; the scalar function is determined by the **actual** weight `w_*`, not by the canonical weight of `P_0`.

## 6. Consequence for the connected-tail problem

The exact comparison now has the following valid form.

- The finite-volume dynamics at `P_*` is the reversible product dynamics `L_0` plus the local signed defect `(13)`.
- The actual insertion is the product-centered `X` insertion plus the scalar defect `-epsilon`.
- The actual Assignment-010 duration weight `w_*` and fixed filter `sigma` are held fixed throughout; they are **not** replaced by the canonical `P_0` duration law.
- With this frozen weight, the reference propagation `(5)` remains self-adjoint because only the semigroup is replaced by the reversible `P_0` semigroup.
- The fresh right-boundary mode is unperturbed by `(12)`.

Thus a Duhamel/cluster expansion of the actual fixed-filter connected operator around `(5)` is legitimate and tags every dynamical loss of reversibility by an explicit local factor `epsilon`, without changing the witness weight.  What is not legitimate is to import the canonical `P_0` survival transform or its `z_sigma` as though it were equal to the one at `P_*`.

A crude global perturbation bound is still insufficient, since `epsilon/omega=9/11`; locality and the fresh-boundary high-frequency channel must be retained.
