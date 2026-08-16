# Student F 007: Phase-A audit of the block mass/disagreement correction

## Verdict

Assignment 007 says to audit the new Meeting 006 correction in order and, if any Phase-A item fails, identify the first false statement and stop before building the block norm.

Items 1--4 pass independently:

1. the segmentwise right-survival chain and product bound have the stated form;
2. its Laplace resolvent is the stated `Z`;
3. the near-East one- and two-site invariant quantities `m_epsilon`, `M_{2,epsilon}`, and `A_{2,epsilon}` are correct;
4. `A_{2,epsilon}` changes sign and the absolute-value ratios tend to `3/2` and `7/5`.

The first failure is Phase-A item 5. The inequality

\[
\max\{c,b-a\}Z<1
\]

is a valid sufficient condition for the crude right-weighted sup-norm estimate, but the principal update's statement that it gives a genuine **residual** subregion is false. In fact, throughout the entire residual chamber,

\[
\boxed{cZ>1.}
\]

Since `c>b-a`, the sufficient condition is never satisfied on `mathcal R`.

Thus I stop before Phase B, as instructed. This correction does **not** refute the predecessor-trail decomposition, the mass/disagreement identity, the stack-drift mechanism, or the possibility of a block contraction. It removes only the claimed already-proved easy residual subregion. The block theorem remains unresolved and should be reconsidered after this correction is entered into the spine.

Supporting exact checks are in

`students/student-f/007-block-mass-disagreement-verifier.py`.

## 1. Notation

Put

\[
B=b+c-a,
\qquad
g=b-a,
\qquad
\omega=1-c+a.
\]

The residual chamber is

\[
0<a<b,
\qquad
\frac12\le c<1,
\qquad
c\ge a+b,
\qquad
b\ge\sqrt2(1-c).
\tag{1.1}
\]

I use the predecessor-trail factorization itself only as the working lemma adopted by the Professor. The present audit begins with the new Meeting 006 right-region correction. Nothing below upgrades the Poisson--Mecke trail factorization to an independently audited closing theorem.

## 2. Segmentwise right killing

The comparison chain in the principal update has transient states `(1,0)`. Starting from `1`, it jumps

\[
1\xrightarrow{a}0,
\qquad
0\xrightarrow{1}1,
\]

and is killed from state `0` at rate `B`. Its transient generator is therefore

\[
K=
\begin{pmatrix}
-a&a\\
1&-(1+B)
\end{pmatrix}.
\tag{2.1}
\]

Let `s_1(u)` be survival through time `u` starting from state `1`. The eigenvalues of `-K` are

\[
\rho_\pm
=
\frac{a+1+B\pm\sqrt{(a+1+B)^2-4aB}}2,
\]

so solving the two-state system gives

\[
\boxed{
s_1(u)
=
\frac{\rho_+e^{-\rho_-u}-\rho_-e^{-\rho_+u}}
{\rho_+-\rho_-}.
}
\tag{2.2}
\]

At every selected trail interaction the relevant right boundary is refreshed to state `1`. Conditional on the decorated trail, the successive right-region strips use disjoint graphical randomness. Applying the same killed comparison independently on each strip therefore gives the claimed multiplicative estimate

\[
\boxed{
|R_{\gamma,t}(\eta)|
\le C_A\prod_{k=1}^n s_1(u_k).
}
\tag{2.3}
\]

This calculation is conditional on the working trail factorization, but the killed-chain part itself checks.

## 3. Resolvent `Z`

For any `alpha>0`, the survival resolvent is

\[
\int_0^\infty e^{-\alpha u}s_1(u)\,du
=e_1^T(\alpha I-K)^{-1}{\bf1}.
\]

Direct inversion of the `2 x 2` matrix gives

\[
\boxed{
Z_\alpha
=
\frac{\alpha+1+B+a}
{(\alpha+a)(\alpha+1+B)-a}.
}
\tag{3.1}
\]

Putting `alpha=omega`,

\[
\boxed{
Z
=
\frac{\omega+1+B+a}
{(\omega+a)(\omega+1+B)-a}.
}
\tag{3.2}
\]

Using `B=b+c-a` and `omega=1-c+a`, this simplifies to

\[
\boxed{
Z
=
\frac{a+b+2}
{2ab+3a-bc+b-2c+2}.
}
\tag{3.3}
\]

The denominator is positive because (3.2) is the resolvent of a sub-Markov chain at positive Laplace parameter.

## 4. Independent reconstruction of the near-East two-site scalar

Take

\[
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2.
\tag{4.1}
\]

Then

\[
p_*=\frac{1+\varepsilon}{1+2\varepsilon},
\qquad
q_*=\frac{\varepsilon}{1+2\varepsilon}.
\tag{4.2}
\]

In the centered-trail spin convention the flip-rate table is

\[
c_{00}=1,
\qquad
c_{01}=\varepsilon^2,
\qquad
c_{10}=\varepsilon,
\qquad
c_{11}=\varepsilon^2.
\tag{4.3}
\]

### 4.1 One site

With zero right boundary, one site has rates

\[
0\xrightarrow{1}1,
\qquad
1\xrightarrow{\varepsilon}0.
\]

Hence its invariant calm density is `1/(1+epsilon)`. For

\[
h_{p_*}(z)=\frac{z-p_*}{q_*},
\]

this gives

\[
\boxed{
m_\varepsilon
=\pi_1^0(h_{p_*})
=-\frac{\varepsilon}{1+\varepsilon}.
}
\tag{4.4}
\]

### 4.2 Two sites

I solved the four-state zero-boundary chain directly. For states `(00,01,10,11)`, its generator is obtained from (4.3), with a zero boundary to the right of the second site. Solving `pi Q=0` and then evaluating `h_{p_*}(eta_1)h_{p_*}(eta_2)` gives

\[
\boxed{
M_{2,\varepsilon}
=\pi_2^0\bigl(h_{p_*}(\eta_1)h_{p_*}(\eta_2)\bigr)
=
\frac{(1+\varepsilon)(2\varepsilon-1)}
{2\varepsilon^2+5\varepsilon+1}.
}
\tag{4.5}
\]

The relevant one-site zero-boundary semigroup relaxes its centered mode at rate `1+epsilon`, so the two-level invariant scalar is

\[
\boxed{
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}
\bigl(M_{2,\varepsilon}-m_\varepsilon^2\bigr).
}
\tag{4.6}
\]

Thus the principal's formulas are reproduced independently.

## 5. Sign change and the `3/2`, `7/5` limits

For `0<epsilon<1/2`, (4.5) is strictly negative, whereas

\[
\lim_{u\to\infty}A_{2,\varepsilon}(u)=m_\varepsilon^2>0.
\]

Hence `A_{2,epsilon}` has exactly one zero. Write

\[
\lambda=1+\varepsilon,
\qquad
C_\varepsilon=m_\varepsilon^2-M_{2,\varepsilon}>0.
\]

Then

\[
A_{2,\varepsilon}(u)
=m_\varepsilon^2-C_\varepsilon e^{-\lambda u},
\]

and its zero is

\[
u_*
=\frac1\lambda
\log\frac{C_\varepsilon}{m_\varepsilon^2}.
\tag{5.1}
\]

As `epsilon->0`,

\[
C_\varepsilon\to1,
\qquad
u_*\to\infty,
\qquad
\omega u_*=2\varepsilon^2u_*\to0.
\tag{5.2}
\]

### 5.1 Without right killing

The signed Laplace integral is

\[
S_\varepsilon
:=\int_0^\infty e^{-\omega u}A_{2,\varepsilon}(u)\,du
=
\frac{m_\varepsilon^2}{\omega}
-
\frac{C_\varepsilon}{\omega+\lambda}.
\]

Since

\[
\frac{m_\varepsilon^2}{\omega}\to\frac12,
\qquad
\frac{C_\varepsilon}{\omega+\lambda}\to1,
\]

we have

\[
S_\varepsilon\to-\frac12.
\tag{5.3}
\]

Let `N_epsilon` be the magnitude of the negative lobe, namely minus the integral over `[0,u_*]`. Explicitly,

\[
N_\varepsilon
=
\frac{C_\varepsilon}{\omega+\lambda}
\bigl(1-e^{-(\omega+\lambda)u_*}\bigr)
-
\frac{m_\varepsilon^2}{\omega}
\bigl(1-e^{-\omega u_*}\bigr).
\]

By (5.2), `N_epsilon->1`. Therefore

\[
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du
=S_\varepsilon+2N_\varepsilon
\longrightarrow\frac32.
\]

Finally

\[
\frac g{|m_\varepsilon|}
=(1-\varepsilon)(1+\varepsilon)\to1,
\]

so

\[
\boxed{
\frac g{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du
\longrightarrow\frac32.
}
\tag{5.4}
\]

### 5.2 With segmentwise right killing

For the right-survival kernel define

\[
Z_\alpha
=\int_0^\infty e^{-\alpha u}s_1(u)\,du.
\]

The signed integral is now

\[
S_\varepsilon^{R}
=m_\varepsilon^2Z_\omega
-C_\varepsilon Z_{\omega+\lambda}.
\]

On the near-East path, (3.2) gives

\[
Z_\omega
=
\frac{\varepsilon^2+\varepsilon+2}
{\varepsilon^2(3\varepsilon+5)},
\tag{5.5}
\]

so

\[
m_\varepsilon^2Z_\omega\to\frac25.
\]

Also `Z_{omega+lambda}->1`, while `C_epsilon->1`. Thus

\[
S_\varepsilon^R\to-\frac35.
\tag{5.6}
\]

For the negative lobe,

\[
N_\varepsilon^R
=C_\varepsilon\int_0^{u_*}
 e^{-(\omega+\lambda)u}s_1(u)\,du
-
m_\varepsilon^2\int_0^{u_*}
 e^{-\omega u}s_1(u)\,du.
\]

The first term tends to `1`, because `u_*->infinity` and the corresponding full resolvent tends to `1`. The second term is bounded by `m_epsilon^2 u_*`, which tends to zero. Hence

\[
N_\varepsilon^R\to1.
\]

Consequently

\[
\boxed{
\frac g{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}s_1(u)
|A_{2,\varepsilon}(u)|\,du
\longrightarrow
-\frac35+2
=
\frac75.
}
\tag{5.7}
\]

This independently confirms the exact obstruction that superseded Assignment 006. One-step positivity and one-step `L^1` contraction remain closed.

## 6. Phase-A item 5 fails: the purported easy residual subregion is empty

Meeting 006 / the principal update states that the direct sup-norm estimate proves a genuine residual subregion whenever

\[
\max\{c,g\}Z<1.
\tag{6.1}
\]

The implication from (6.1) to decay is fine. The problem is that (6.1) cannot occur in `mathcal R`.

First, from `c>=a+b` and `a>0`,

\[
c>b>b-a=g.
\]

Therefore

\[
\max\{c,g\}=c.
\tag{6.2}
\]

It remains to prove `cZ>1` throughout (1.1).

Using (3.3), `cZ<1` would be equivalent to

\[
F(a,b,c)
:=
2ab-ac+3a-2bc+b-4c+2
>0.
\tag{6.3}
\]

Set

\[
x=1-c.
\]

The residual constraints imply

\[
0<x\le\frac12,
\qquad
a<b,
\qquad
a+b+x\le1,
\qquad
x\le\frac b{\sqrt2}.
\tag{6.4}
\]

Moreover

\[
F
=a(2b+x+2)+x(2b+4)-b-2.
\tag{6.5}
\]

This is increasing in `a`. Put

\[
b_0
:=
\frac1{2+1/\sqrt2}.
\tag{6.6}
\]

We split according to which upper bound on `a` is active.

### Case 1: `2b+x<=1`

Then `b<=1-b-x`, so `a<b` and (6.5) give

\[
F
<
G_1(b,x)
:=2b^2+b+3bx+4x-2.
\tag{6.7}
\]

Here

\[
x\le\min\left\{\frac b{\sqrt2},1-2b\right\}.
\]

If `b<=b_0`, then `x<=b/sqrt2`. Since `G_1` is increasing in `x`,

\[
G_1(b,x)
\le
2b^2+b+\frac{3b^2+4b}{\sqrt2}-2.
\]

The right-hand side is increasing in `b`, and at `b=b_0` equals

\[
\frac{2(-43+30\sqrt2)}{49}<0,
\]

because `30sqrt2<43`.

If `b>=b_0`, then `x<=1-2b`, so

\[
G_1(b,x)
\le
-2(2b^2+2b-1).
\]

The polynomial in parentheses is increasing in `b`, and at `b_0` it equals

\[
\frac{43-30\sqrt2}{49}>0.
\]

Thus `F<0` throughout Case 1.

### Case 2: `2b+x>=1`

Now `1-b-x<=b`, hence from (6.4),

\[
a\le1-b-x.
\]

Using this in (6.5),

\[
F
\le
G_2(b,x)
:=-2b^2-bx-b-x^2+3x.
\tag{6.8}
\]

On `0<x<=1/2` and `b<1`,

\[
\partial_xG_2=3-b-2x>0.
\]

Also Case 2 together with `x<=b/sqrt2` forces `b>=b_0`.

If `b<=1/sqrt2`, then

\[
G_2(b,x)
\le
G_2\left(b,\frac b{\sqrt2}\right)
=-\frac b2
\left[(\sqrt2+5)b-3\sqrt2+2\right].
\]

The bracket is increasing in `b`, and at `b=b_0` it equals

\[
\frac{32-22\sqrt2}{7}>0.
\]

Thus `G_2<0`.

If `b>=1/sqrt2`, then `x<=1/2`, and

\[
G_2(b,x)
\le G_2\left(b,\frac12\right)
=-\frac{(2b-1)(4b+5)}4<0.
\]

Thus `F<0` throughout Case 2 as well.

Combining the cases,

\[
\boxed{
F(a,b,c)<0
\quad\text{for every }(a,b,c)\in\mathcal R.
}
\tag{6.9}
\]

Equivalently,

\[
\boxed{
cZ>1
\quad\text{throughout }\mathcal R.}
\tag{6.10}
\]

By (6.2),

\[
\boxed{
\max\{c,g\}Z<1
\quad\text{has no solutions in }\mathcal R.}
\tag{6.11}
\]

This is the first false statement encountered in the ordered Assignment 007 audit.

## 7. Consequence for the active programme

What fails is specifically the sentence that the direct sup-norm criterion already proves a nonempty residual subregion. The conditional theorem

\[
\max\{c,g\}Z<1
\Longrightarrow
\text{direct trail-depth decay}
\]

remains algebraically valid; its intersection with the current unresolved residual chamber is empty.

The following Meeting 006 objects are not refuted by this audit:

- the predecessor-trail decomposition;
- segmentwise right killing;
- the global quantity `J_{x,r}`;
- the mass/disagreement decomposition;
- negative drift of the unresolved disagreement stack;
- a possible multi-step/block contraction.

Assignment 007 explicitly instructs that if any Phase-A item fails, the first failure should be recorded and the block construction stopped there. I therefore did not promote any candidate block norm after finding (6.11).

Likewise, the complementary no-exit contribution has not disappeared: any later closing reconstruction must still control it explicitly, as required by Meetings 005--006. This report does not claim a full convergence implication.

principal update fails at: the claimed direct-sup easy residual subregion is empty; throughout the residual chamber `g<c` and `c Z>1`, so `max{c,g} Z<1` never holds.
