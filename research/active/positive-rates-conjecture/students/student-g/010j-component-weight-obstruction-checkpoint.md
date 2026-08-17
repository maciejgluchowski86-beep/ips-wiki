# Student G 010j checkpoint: component weights do not repair the one-step coefficient Lyapunov obstruction

**Status:** durable negative checkpoint for Assignment 010.  This rules out the most natural refinement of 010a: a one-step coefficient norm which weights both degree and the number of connected components.  It does **not** rule out the signed fixed-filter connected transfer itself.

## 1. Exact transformed generator

Use the `x_A=g^{|A|}q_A` coefficient variables of 010b.  At `P_*`, put

\[
\alpha:=\frac{|d|}{g}=\frac1{100},
\qquad
g=\frac{99}{1000},
\qquad
c=\frac{9999}{10000},
\qquad
\omega=\frac{11}{10000}.
\]

After combining collisions exactly, the nonconstant coefficient generator has the following transitions from a set `A`.

- At every component right edge `i<N`, birth of `i+1` has coefficient `g`.
- Removing a site whose left neighbour is occupied has the combined positive coefficient `c-alpha`.
- Removing a component left edge has coefficient `-alpha`.
- For an occupied site with empty right neighbour the diagonal contribution is `-(g+omega)`; with occupied right neighbour it is `-(c+omega)`.
- The finite-volume right boundary has extra killing, which can only help the test below, so all test sets are placed strictly away from it.

Thus the only genuinely negative removals are component-left-edge deletions, exactly as recorded in 010b.

## 2. Candidate component-weight norm

Let `kappa(A)` be the number of connected components of `A` in one dimension.  Consider the natural two-parameter refinement

\[
\boxed{
 \|f\|_{\theta,\phi}
 :=\sum_{A\ne\varnothing}
 \theta^{|A|}\phi^{\kappa(A)}|x_A|,
 \qquad \theta,\phi>0.
}
\tag{1}
\]

Suppose the nonconstant coefficient semigroup were nonexpansive in `(1)` uniformly in depth.  Taking the right derivative at time zero on three families of single monomials gives necessary inequalities.

## 3. Long blocks

Take a block of `n` consecutive occupied sites, strictly away from the finite-volume boundary, and let `n->infinity`.  All but `O(1)` of the positive removals delete an interior site and split one component into two.  Their weight ratio is `phi/theta`.  The diagonal contribution per bulk site is `-(c+omega)`.  Therefore uniform nonexpansiveness requires

\[
\boxed{
 (c-\alpha)\frac{\phi}{\theta}
 \le c+\omega.
}
\tag{L}
\]

## 4. Widely separated dimers

Take a union of many separated components, each of length two.  For each dimer the diagonal is

\[
-(c+g+2\omega).
\]

Its right edge can give a birth with weighted coefficient `g theta`.  Removing its left site has absolute coefficient `alpha/theta`; removing its right site has the combined coefficient `(c-alpha)/theta`.  The two removals leave a singleton component, so the component weight does not change.  Dividing by the number of dimers gives the necessary condition

\[
\boxed{
 g\theta+\frac c\theta
 \le c+g+2\omega.
}
\tag{D}
\]

This already forces

\[
\boxed{\theta>\frac{99}{100}.}
\tag{2}
\]

Indeed `g theta+c/theta` is decreasing for `theta<=99/100`, while at `theta=99/100`

\[
g\theta+\frac c\theta
=\frac{9801}{100000}+\frac{101}{100}
=1.10801
>1.1011
=c+g+2\omega.
\]

## 5. Widely separated singletons

Take many isolated occupied sites.  Each has diagonal `-(g+omega)`, a birth with weighted coefficient `g theta`, and a component-left-edge deletion with absolute weighted coefficient

\[
\frac{\alpha}{\theta\phi}.
\]

Hence

\[
\boxed{
 g\theta+\frac{\alpha}{\theta\phi}
 \le g+\omega.
}
\tag{I}
\]

But `(L)` gives

\[
\phi\le
\theta\frac{c+\omega}{c-\alpha},
\]

so

\[
\frac{\alpha}{\theta\phi}
\ge
\frac{\alpha(c-\alpha)}{\theta^2(c+\omega)}.
\tag{3}
\]

Set

\[
L_*:=\frac{c-\alpha}{c+\omega}
=\frac{9899}{10010}.
\]

By `(2)`, `theta>99/100`.  The function

\[
F(\theta):=g\theta+\frac{\alpha L_*}{\theta^2}
\]

is strictly increasing for `theta>=99/100`: indeed `L_*<1` and

\[
\frac{2\alpha L_*}{\theta^3}
<\frac{2}{100}\left(\frac{100}{99}\right)^3
<\frac{99}{1000}=g.
\]

Moreover `L_*>98/100`, and hence

\[
F(99/100)
>
\frac{9801}{100000}
+\frac{1}{100}\frac{98}{100}
=0.10781
>0.1001
=g+\omega.
\tag{4}
\]

Equations `(3)`--`(4)` contradict `(I)`.

Therefore

\[
\boxed{
\text{There are no }\theta,\phi>0\text{ for which `(1)` makes the actual nonconstant coefficient semigroup nonexpansive uniformly in depth.}
}
\tag{5}
\]

## 6. Consequence

This strictly extends the 010a obstruction.  Penalising or rewarding the number of spatial components cannot repair the one-step positive coefficient Lyapunov method: long blocks force a relation between `theta` and `phi`, dimers force `theta` close to or above one in the `x`-scaled variables, and isolated particles then violate the required drift inequality.

The result does **not** contradict the 010e--010f signed-filter contraction.  It says that the remaining Assignment-010 theorem cannot be obtained by first making the raw semigroup contractive in a depth-independent degree/component `ell^1` norm and only afterwards integrating the fixed time filter.  Cancellation at the resolvent/filter level remains load-bearing.
