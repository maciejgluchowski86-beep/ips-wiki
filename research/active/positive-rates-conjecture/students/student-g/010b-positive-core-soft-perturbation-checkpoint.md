# Student G 010b checkpoint: exact positive core and soft perturbation

**Status:** intermediate durable checkpoint for Assignment 010. This does **not** decide `(J-SPEC)` or the connected-tail target `(T)`.

This checkpoint sharpens 010a.  The canonical `Y` generator is not merely "close to East".  After removing the single coefficient `d`, the remaining operator has an exact positive set-process representation and an exact coercive Hilbert-space structure.  At `P_*` the entire sign-indefinite perturbation has one explicit dimensionless strength, `1/100`.

## 1. Algebraic identities at the primary point

Recall

\[
k=1-c,
\qquad B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a=k+a,
\qquad d=bk-a<0,
\]

and

\[
Y_i=B\eta_i-c.
\]

The identities

\[
 b+k=g+\omega,
\qquad
 1+a=c+\omega,
\qquad
 1+b=g+c+\omega
\tag{1}
\]

are exact.

Write

\[
e=-d>0,
\qquad
\alpha:=\frac e g.
\]

At

\[
P_*=(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
\]

we have

\[
 g=\frac{99}{1000},
\qquad
 \omega=\frac{11}{10000},
\qquad
 e=\frac{99}{100000},
\qquad
\boxed{\alpha=\frac1{100}.}
\tag{2}
\]

## 2. Exact coefficient transform

For

\[
f=\sum_A q_A Y_A,
\]

put

\[
x_A:=g^{|A|}q_A.
\tag{3}
\]

Let `\widehat L` denote the coefficient generator in the `x_A` variables.  Combining the collisions in 010a equation `(4)`, or equivalently transforming before combining, gives the following exact description.

For every occupied `i<N`:

- if `i+1\notin A`, the positive birth
  \[
  A\longrightarrow A\cup\{i+1\}
  \]
  has coefficient `g`;
- if `i+1\in A`, the positive coalescence
  \[
  A\longrightarrow A\setminus\{i+1\}
  \]
  has coefficient `c`;
- every occupied `i` has the signed deletion
  \[
  A\longrightarrow A\setminus\{i\}
  \]
  with coefficient
  \[
  \frac d g=-\alpha.
  \]

The diagonal contribution of an occupied interior site is respectively

\[
-(g+\omega)
\quad\hbox{or}\quad
-(c+\omega),
\tag{4}
\]

while an occupied right-boundary site contributes

\[
-(g+c+\omega).
\tag{5}
\]

Thus

\[
\boxed{
\widehat L=\widehat L^+-\alpha\mathsf D,
}
\tag{6}
\]

where `\mathsf D` deletes one occupied site with positive coefficient one, and `\widehat L^+` contains only the birth/coalescence terms and the diagonals `(4)`--`(5)`.

This is the exact soft perturbation.  No comparison of the original rates with a different East generator is being made.

## 3. Positive-core set-process representation

On nonempty subsets of `{1,...,N}`, define a sub-Markov set process as follows.

For each occupied `i<N`:

- if `i+1\notin A`, add `i+1` at rate `g`;
- if `i+1\in A`, remove `i+1` at rate `c`.

If `N\in A`, send the process to a cemetery state at rate `g+c`.  In addition, impose Feynman--Kac killing at rate

\[
\omega |A|.
\]

Its Feynman--Kac generator on the nonempty-set coordinates is exactly `\widehat L^+`.  Hence `\widehat L^+` is Metzler and

\[
\boxed{
\left\|e^{tL^+}f\right\|_g
\le e^{-\omega t}\|f\|_g,
\qquad
\|f\|_g:=\sum_{A\ne\varnothing}g^{|A|}|q_A|,
}
\tag{7}
\]

whenever the constant coefficient is ignored.  In fact the path representation retains the stronger factor

\[
\exp\left\{-\omega\int_0^t |A_s|\,ds\right\}.
\tag{8}
\]

The obstruction in 010a is now transparent: taking absolute values of the perturbation in `(6)` adds deletion mass at rate `\alpha|A|`, while the positive core only guarantees killing `\omega|A|`; at `P_*`,

\[
\alpha=\frac1{100}>\frac{11}{10000}=\omega.
\tag{9}
\]

Therefore a Duhamel argument that replaces every signed deletion by its absolute value destroys the available depth-uniform killing before any connected structure is used.  Cancellation of the soft deletion is load-bearing.

## 4. Exact Hilbert-space structure

Let

\[
p_*:=\frac cB
\]

and let `\mu_*` be Bernoulli(`p_*`) product measure.  Since

\[
\mu_*(Y_i)=0,
\qquad
Y_i^2=(g-c)Y_i+cg,
\]

we have

\[
\mu_*(Y_A Y_{A'})=0\quad(A\ne A'),
\qquad
\|Y_A\|_{L^2(\mu_*)}^2=(cg)^{|A|}.
\tag{10}
\]

The positive core `L^+` is self-adjoint in this orthogonal basis.  Indeed a birth pair

\[
A\longleftrightarrow A\cup\{i+1\}
\]

has coefficients `1` and `cg` in the unscaled `Y` basis, while the squared basis norms differ by exactly the factor `cg`.

More precisely, decompose the quadratic form source-site by source-site.  For an interior occupied `i`, the two local states `i+1\notin A` and `i+1\in A`, after orthonormalization, give the `2\times2` block

\[
\begin{pmatrix}
-(g+\omega) & \sqrt{cg}\\
\sqrt{cg} & -(c+\omega)
\end{pmatrix}
=
-\omega I+
\begin{pmatrix}
-g & \sqrt{cg}\\
\sqrt{cg} & -c
\end{pmatrix}.
\tag{11}
\]

The second matrix is negative semidefinite because its determinant is zero and its trace is `-(g+c)`.  The right boundary contributes only the negative diagonal `-(g+c+\omega)`.

Consequently, if

\[
\mathcal N Y_A=|A|Y_A,
\]

then

\[
\boxed{
-\langle f,L^+f\rangle_{\mu_*}
\ge
\omega\,\langle f,\mathcal N f\rangle_{\mu_*}
}
\tag{12}
\]

for every finite `Y`-polynomial with zero constant coefficient.  In particular the nonconstant spectrum of `L^+` lies in `(-\infty,-\omega]`.

## 5. Consequence for the connected-tail attack

Equations `(6)`--`(12)` identify the remaining issue much more sharply than a generic growing-mode statement.

- The `d=0` core has a positive Feynman--Kac representation and exact number-operator coercivity.
- The actual perturbation is a single signed deletion operator with strength `\alpha=1/100` after the canonical `g` transform.
- Since `\alpha>\omega`, an estimate that takes absolute values at each deletion cannot close uniformly in depth.
- Any successful multi-step estimate must exploit the fact already visible in 010a: when the deleted site has an occupied left neighbour, the signed deletion lands on the same monomial as a positive coalescence and combines as `c-\alpha` in the transformed variables.  The only genuinely negative removal is at a component left edge.

This leaves a concrete next target: retain component geometry long enough to pair the `-\alpha` deletion with the positive birth/coalescence core before absolute values are taken, rather than perturbing the positive core in operator norm.
