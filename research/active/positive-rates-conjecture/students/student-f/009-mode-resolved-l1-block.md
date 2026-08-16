# Student F 009: mode-resolved `L^1(w)` block operator

## Verdict

Meeting 009 asks for the duration-resolved signed transfer, and allows an exact obstruction if the required finite mode dimension grows without bound even when disagreement/restart height is bounded. Meeting 010 subsequently refuted the scalar global Foster premise from G's Assignment 003 and replaced it on the coupling side by a 16-edge-phase feasibility problem. I do not assume the refuted Foster statement.

There are two results.

First, the mandatory mass-mode calculation is favorable. Let

\[
r_0=\frac1{1+b},\qquad \lambda_0=1+b,
\]

and write a signed mass component by its total mass `A` and centered rightmost moment

\[
C=\nu(\eta_y)-r_0\nu(1).
\]

After zero-boundary evolution for time `u`, the total signed coefficient produced by the next centered insertion is exactly

\[
(Br_0-c)A+B C e^{-\lambda_0u}.
\]

The equilibrium type has the already verified right-weighted cost

\[
\kappa_E:=|Br_0-c|Z<\frac23.
\]

The transient type also has a strict one-segment `L^1(w)` contraction:

\[
\boxed{
\kappa_T
:=B\int_0^\infty w(u)e^{-(1+b)u}\,du
<1.
}
\]

In fact, with `k=1-c`,

\[
\kappa_T
=
\frac{B(a+2b+3)}
{4ab+5a+2b^2+2bk+5b+3k+3},
\]

and the denominator minus the numerator is

\[
\boxed{
a^2+5ab+ak+7a+4bk+6k>0.}
\]

Near East,

\[
\kappa_T
=1-\frac{13}{3}\varepsilon^2+O(\varepsilon^3).
\]

Thus the transient mode is not intrinsically expansive. The old `7/5` depth-two expansion arises because the scalar normalization discarded an order-one transient mode before taking the norm.

Second, the exact finite-dimensional mode-closure target is obstructed. This obstruction is independent of disagreement and already occurs at disagreement height zero. On an `N`-site zero-boundary interval let `L_N` be the spin generator in the centered-trail convention. For the centered one-site character at the left end,

\[
h_1(\eta)=h_{p_*}(\eta_1),
\]

one has for `0<=j<=N-1`

\[
\boxed{
L_N^j h_1
=\frac{B^j}{q_*}\eta_1\eta_2\cdots\eta_{j+1}
+R_j,
\qquad
\deg R_j\le j.
}
\]

Consequently

\[
\boxed{
\dim\operatorname{span}\{h_1,L_Nh_1,\ldots,L_N^{N-1}h_1\}=N.
}
\]

Any exact linear mode space invariant under all zero-boundary semigroups and containing the trail-generated one-site centered insertion must contain this cyclic subspace. Its dimension therefore grows at least linearly with the remaining spatial depth even when the disagreement/restart height is zero. There is no depth-uniform finite-dimensional mode space `E_0`, hence no family `E_H` of the kind proposed in Assignment 009 with dimension depending only on bounded disagreement/restart height.

This does **not** refute the centered-trail route or a profile-valued/infinite-dimensional block norm. It refutes the finite exact generator-mode closure as the next theorem. The correct one-segment transfer is naturally an operator-valued `L^1(w)` map on signed left measures; I write it explicitly below. G's 16 coupling phases can be coupled to this operator, but they do not collapse its common-mass mode hierarchy.

Supporting exact symbolic checks are in

`students/student-f/009-mode-resolved-l1-verifier.py`.

## 1. Current inputs and the Meeting 010 correction

Put

\[
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\]

and

\[
w(u)=e^{-\omega u}s_1(u).
\]

For

\[
Z_\alpha
:=\int_0^\infty e^{-\alpha u}s_1(u)\,du,
\]

Meeting 006 gives

\[
\boxed{
Z_\alpha
=\frac{\alpha+1+B+a}{(\alpha+a)(\alpha+1+B)-a}.
}
\tag{1.1}
\]

Thus

\[
Z=Z_\omega.
\]

The following remain established.

1. The exact predecessor-trail decomposition is the active working reduction, still pending its final independent factorization/no-exit audit.
2. The segmentwise right factor is bounded by the product of `s_1(u)`.
3. The global nonempty-exit target is decay of
   \[
   J_{x,r}
   =Bg^{n-1}\int\left(\prod_jw(u_j)\right)
   |\pi^0_{m,r}(F_{x,u})|\,du.
   \]
4. The exact mass/disagreement identity is
   \[
   g\mu(h_{p_*}(\eta_y)f)
   =(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
   \tag{1.2}
   \]
5. The equilibrium mass multiplier obeys
   \[
   \boxed{|Br_0-c|Z<2/3},\qquad r_0=(1+b)^{-1}.
   \tag{1.3}
   \]
6. Duration integration cannot precede the relevant absolute value: near East the two orders give `3/5` and `7/5` respectively.

Meeting 010 changes only the coupling-side premise used conditionally in Assignment 008. G's exposed-only global product Foster lift is false. A reachable all-`01` stack gives positive drift growing linearly in height. What survives is G's exact 16-edge-phase/64-triple finite bulk criterion for a stronger nearest-neighbour coupling corrector. I use none of the refuted product-Foster conclusions below.

## 2. Mandatory calculation: the two scalar mass modes

Let `nu` be a finite signed measure on a zero-boundary interval whose rightmost site is `y`. Set

\[
A:=\nu(1),
\qquad
C:=\nu(\eta_y)-r_0A.
\tag{2.1}
\]

The rightmost spin is autonomous under zero boundary:

\[
0\xrightarrow{1}1,
\qquad
1\xrightarrow{b}0.
\]

Therefore, for the full zero-boundary semigroup as well,

\[
(\nu P_u)(\eta_y)
=r_0A+Ce^{-(1+b)u}.
\tag{2.2}
\]

Since

\[
gh_{p_*}(z)=Bz-c,
\tag{2.3}
\]

the total signed mass after the next centered insertion has duration profile

\[
\boxed{
M_{A,C}(u)
=(Br_0-c)A+BCe^{-(1+b)u}.
}
\tag{2.4}
\]

This is the exact equilibrium/transient decomposition required by Assignment 009. It is valid for arbitrary signed `nu`; no positivity or invariant-law assumption is used.

### 2.1 Equilibrium type

For `C=0`,

\[
\int_0^\infty w(u)|M_{A,0}(u)|du
=\kappa_E|A|,
\]

with

\[
\kappa_E=|Br_0-c|Z<\frac23.
\tag{2.5}
\]

### 2.2 Transient type

For `A=0`,

\[
\int_0^\infty w(u)|M_{0,C}(u)|du
=\kappa_T|C|,
\]

where

\[
\kappa_T
=B Z_{\omega+1+b}.
\tag{2.6}
\]

Write

\[
k=1-c>0.
\]

Then

\[
\omega=a+k,
\qquad
B=1+b-a-k,
\]

and direct substitution in (1.1) gives

\[
Z_{\omega+1+b}
=
\frac{a+2b+3}
{4ab+5a+2b^2+2bk+5b+3k+3}.
\tag{2.7}
\]

Hence

\[
\boxed{
\kappa_T
=
\frac{(1+b-a-k)(a+2b+3)}
{4ab+5a+2b^2+2bk+5b+3k+3}.
}
\tag{2.8}
\]

The denominator minus the numerator equals

\[
\boxed{
a^2+5ab+ak+7a+4bk+6k.}
\tag{2.9}
\]

Every term is strictly positive. Therefore

\[
\boxed{\kappa_T<1}
\tag{2.10}
\]

at every strict positive-rate point for which `B>0`, in particular throughout the residual chamber. Notice that no residual inequalities beyond positivity are needed for (2.10).

At

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
\]

one gets

\[
\kappa_E=\frac{48}{533},
\qquad
\boxed{\kappa_T=\frac{185}{301}}.
\tag{2.11}
\]

Along

\[
a=k=\varepsilon^2,
\qquad
b=\varepsilon,
\]

one has

\[
\boxed{
\kappa_T
=1-\frac{13}{3}\varepsilon^2
+\frac{38}{9}\varepsilon^3
+O(\varepsilon^4).
}
\tag{2.12}
\]

The transient contraction becomes weak at East but remains strict at every positive-rate point.

### 2.3 The correct profile norm

For old duration variables `v`, let `A(v)` and `C(v)` be arbitrary signed scalar profiles. Define

\[
\mathcal M(A,C)(v,u)
=(Br_0-c)A(v)+Be^{-(1+b)u}C(v).
\tag{2.13}
\]

If

\[
\|F\|_m
=\int\left(\prod_{j=1}^m w(v_j)dv_j\right)|F(v)|,
\]

then Tonelli and the triangle inequality in the **new** duration only give

\[
\boxed{
\|\mathcal M(A,C)\|_{m+1}
\le
\kappa_E\|A\|_m
+\kappa_T\|C\|_m.
}
\tag{2.14}
\]

Thus the two separated mass types have a genuine profile-level contraction. Equation (2.14) respects the norm order: old duration variables are not integrated before opposite signed profiles are combined at fixed `v`.

The near-East `7/5` expansion is not a contradiction. In that calculation the predecessor was normalized only by the small equilibrium scalar `|m_epsilon|`, while the generated transient coefficient is order one. The mode norm in (2.14) assigns that transient its own order-one size.

## 3. Exact operator-valued one-segment transfer

The two scalar functionals `(A,C)` do not determine the whole signed left measure after insertion. The exact linear object is obtained by slicing at the current rightmost spin.

Let

\[
\nu_0(f)=\nu(f\,1_{\{\eta_y=0\}}),
\qquad
\nu_1(f)=\nu(f\,1_{\{\eta_y=1\}}),
\]

for functions `f` on sites strictly left of `y`. Let `L^0` and `L^1` be the left-block generators with boundary spin at `y` fixed to `0` and `1` respectively.

During zero-boundary evolution of the full block, the rightmost site flips

\[
0\to1\text{ at rate }1,
\qquad
1\to0\text{ at rate }b.
\]

Therefore the slice measures solve the operator-valued forward system

\[
\begin{aligned}
\dot\nu_0&=\nu_0L^0-\nu_0+b\nu_1,\\
\dot\nu_1&=\nu_1L^1+\nu_0-b\nu_1.
\end{aligned}
\tag{3.1}
\]

Equivalently, for the row vector `boldnu=(nu_0,nu_1)`,

\[
\dot{\boldsymbol\nu}
=\boldsymbol\nu\,\mathbb Q_y,
\qquad
\boxed{
\mathbb Q_y
=
\begin{pmatrix}
L^0-I&I\\
bI&L^1-bI
\end{pmatrix}.
}
\tag{3.2}
\]

The centered insertion is the linear projection

\[
\boxed{
\mathcal S(\nu_0,\nu_1)
=-c\nu_0+g\nu_1.
}
\tag{3.3}
\]

Hence the exact duration-resolved signed transfer for one segment is

\[
\boxed{
(\mathfrak T_y\boldsymbol\nu)(u)
=
\mathcal S\bigl(\boldsymbol\nu e^{u\mathbb Q_y}\bigr).
}
\tag{3.4}
\]

For any norm on signed left measures, the `J`-compatible one-segment norm is

\[
\boxed{
\|\mathfrak T_y\boldsymbol\nu\|_{L^1(w)}
=
\int_0^\infty
w(u)
\left\|
\mathcal S(\boldsymbol\nu e^{u\mathbb Q_y})
\right\|du.
}
\tag{3.5}
\]

This is the mode-resolved operator requested in the assignment. It is **operator-valued**, not a scalar `2 x 2` matrix: the entries `L^0,L^1` act on the full common left measure. Applying (3.5) to the constant test function kills `L^0,L^1` and reduces exactly to the two scalar modes of Section 2.

For a block of `m` spatial transfers, one must retain all durations until the block norm:

\[
\int_{(0,\infty)^m}
\left(\prod_{j=1}^m w(u_j)du_j\right)
\left\|
\mathcal S_m e^{u_m\mathbb Q_m}
\cdots
\mathcal S_1 e^{u_1\mathbb Q_1}
\boldsymbol\nu
\right\|.
\tag{3.6}
\]

Formula (3.6), rather than a product of duration-integrated matrices, is the correct algebraic object. The `3/5` versus `7/5` obstruction is precisely the statement that the `u_j` integrations cannot in general be moved inside this norm.

## 4. Finite mode closure fails already in the pure mass sector

Assignment 009 offers as a successful outcome a finite-dimensional mode space `E_H`, at each fixed bounded disagreement/restart height `H`, invariant under zero-boundary semigroups and insertion maps. Such a theorem must in particular hold at height zero, where there is no disagreement component.

I now show that this is impossible for an exact **depth-uniform linear mode space**.

Take an interval

\[
\Lambda_N=\{1,\ldots,N\}
\]

with zero right boundary `eta_{N+1}=0`, and let `L_N` be its spin generator. Write

\[
\chi_{[1,j]}(\eta)=\eta_1\cdots\eta_j.
\]

### 4.1 Degree-raising coefficient

For a site spin `x` and right neighbour `y`, the flip-rate table is

\[
c(0,0)=1,
\quad c(0,1)=1-c,
\quad c(1,0)=b,
\quad c(1,1)=a.
\]

The factor appearing when the observable contains the spin `x` is

\[
c(x,y)(1-2x).
\]

As a multilinear polynomial on `{0,1}^2`, it is exactly

\[
\boxed{
c(x,y)(1-2x)
=1-cy-(1+b)x+Bxy.
}
\tag{4.1}
\]

The only term that increases polynomial degree is `Bxy`.

Suppose a monomial has support `S`. Updating a site `i in S` can increase its degree by at most one, and a degree increase occurs only by adjoining the right neighbour `i+1` through the `B eta_i eta_{i+1}` term.

Starting from `S={1}`, to increase degree at every one of `j` successive generator applications there is a unique possible support chain:

\[
\{1\}
\to\{1,2\}
\to\cdots
\to\{1,\ldots,j+1\}.
\]

Each step contributes a factor `B`. Therefore

\[
\boxed{
L_N^j\eta_1
=B^j\chi_{[1,j+1]}
+R'_j,
\qquad
\deg R'_j\le j,
}
\tag{4.2}
\]

for `0<=j<=N-1`.

Since

\[
h_{p_*}(\eta_1)
=\frac{\eta_1-p_*}{q_*}
\]

and `L_N1=0`, (4.2) gives

\[
\boxed{
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\chi_{[1,j+1]}
+R_j,
\qquad
\deg R_j\le j.
}
\tag{4.3}
\]

The coefficient is nonzero because `B>0` and `q_*>0` throughout the strict residual chamber.

### 4.2 Cyclic dimension

The functions

\[
h_1,L_Nh_1,\ldots,L_N^{N-1}h_1
\]

have distinct nonzero top polynomial degrees `1,2,...,N`. They are therefore linearly independent. Hence

\[
\boxed{
\dim\operatorname{span}\{L_N^j h_1:0\le j<N\}=N.
}
\tag{4.4}
\]

Now let `E_N` be any finite-dimensional linear function space that contains `h_1` and is invariant under the zero-boundary semigroup `P_t^N=e^{tL_N}`. Since the state space is finite, differentiating at `t=0` shows

\[
L_NE_N\subseteq E_N.
\]

Thus `E_N` contains every vector in (4.4), and

\[
\boxed{\dim E_N\ge N.}
\tag{4.5}
\]

This lower bound holds at every strict residual parameter point.

## 5. Consequence for Assignment 009

A trail-generated centered insertion contains the one-site character `h_{p_*}`. The proposed exact mode closure is required to be stable under the intervening zero-boundary semigroups. Therefore Section 4 is a direct obstruction to a family whose dimension depends only on bounded disagreement/restart height and not on remaining trail depth.

In particular, at disagreement height

\[
H=0,
\]

the required exact linear mode dimension is already at least `N` on an `N`-site interval. Hence

\[
\boxed{
\text{bounded disagreement/restart height does not imply bounded mass-mode dimension.}
}
\tag{5.1}
\]

This is stronger than the first- and second-order static Markov counterexamples from Assignment 008. Those showed that one- and two-spin present-state closures fail at one strict parameter point. Equation (4.5) gives a parameter-wide, all-depth obstruction to **any fixed finite linear semigroup-mode closure** of the type requested in Assignment 009.

The result also explains why a finite temporal CTMC obtained merely by adding finitely many reset-history labels cannot exactly represent the full mass profile for arbitrary depth: a `D`-phase linear Markov representation gives at most a `D`-dimensional invariant output space, whereas (4.5) requires at least `N` modes for depth `N`.

I am not claiming that every nonlinear/nonlocal representation is impossible. In particular, a matrix-product construction with depth-growing bond dimension or an infinite-dimensional Banach-space transfer is not excluded. What is excluded is the depth-uniform finite generator/mode state that Assignment 009 listed as its first finite-kernel route.

## 6. Relation to G's 16 coupling phases

Meeting 010 gives G's exact coupling-side local phase alphabet

\[
\mathcal A^2,
\qquad
\mathcal A=\{00,11,01,10\},
\]

and reduces a nearest-neighbour product/coboundary Foster ansatz to 64 local bulk inequalities plus finite boundary inequalities.

That phase state and the mass-mode obstruction solve different problems.

- G's 16 phases distinguish how **two coupled copies disagree or re-enter exposure**.
- The operator `mathbb Q_y` in (3.2) still contains `L^0,L^1` acting on the **common left mass law**.
- Even when there is no disagreement at all, the common mass semigroup has cyclic dimension at least the spatial depth by (4.5).

Therefore a successful solution of G's 16-phase feasibility problem would not, by itself, turn the signed trail transfer into a finite matrix. The correct combined object would be a 16-phase coupling cocycle whose coefficients act on the profile-valued mass space in (3.5).

## 7. What the favorable two-mode calculation still buys

The obstruction in Section 4 should not be read as evidence that the profile-valued route is expansive. The simplest two mass modes are both strictly damped:

\[
\kappa_E<\frac23,
\qquad
\kappa_T<1.
\]

The second inequality is especially relevant near East. Although

\[
\kappa_T\uparrow1,
\]

its gap is on the natural positive-rate scale

\[
1-\kappa_T
=\frac{13}{3}\varepsilon^2+O(\varepsilon^3).
\]

Thus a plausible replacement theorem is not a finite spectral-radius calculation but a **uniform weighted norm on the growing mode hierarchy**. The degree-raising formula (4.3) identifies the hierarchy explicitly: each zero-boundary generator application can add one right-neighbour variable with coefficient `B`.

A future norm would need to combine:

1. the strict regenerated equilibrium loss `kappa_E<2/3`;
2. the strict one-site transient loss `kappa_T<1`;
3. weights on higher polynomial/reset modes generated by (4.3);
4. G's phase-resolved disagreement/restart control, if its 16-phase feasibility problem is solved.

A naive coefficient `l^1` norm is not enough because the already proved `cZ>1` and `7/5` examples show expansion after premature absolute values. Cancellation must still be retained at each fixed duration profile.

## 8. Interface to `J_{x,r}` and closing proof

This assignment does not prove

\[
J_{x,r}\to0.
\]

Instead it changes the exact form of the remaining analytic target.

The finite bounded-height signed-kernel programme, interpreted as a depth-uniform finite-dimensional generator-mode space, is closed by (4.5). To control `J`, one now needs either

- an infinite-dimensional/profile-valued block norm for (3.6) with a depth-uniform contraction;
- or a genuine regeneration/truncation theorem showing that the growing mass-mode hierarchy can be cut with a quantitative tail, while preserving the `L^1(w)` norm order.

If such a theorem and G's phase-resolved coupling control both succeed, their contraction can be inserted into the existing predecessor-trail reduction to obtain decay of the nonempty-exit term. The exact Poisson--Mecke factorization and complementary no-exit term still remain separate mandatory audits before any ergodicity claim.

## Handoff

`finite mode route obstructed because: after separating the mass coefficient into equilibrium and transient types, both are individually right-weighted L1 contractive, with |Br_0-c|Z<2/3 and kappa_T=B Z_{omega+1+b}<1, where the exact transient gap is a^2+5ab+a(1-c)+7a+4b(1-c)+6(1-c)>0 and kappa_T=1-(13/3)epsilon^2+O(epsilon^3) near East. However the exact zero-boundary mass semigroup has no depth-uniform finite linear mode closure even at disagreement height zero: on an N-site interval, L_N^j h_{p_*}(eta_1) has unique top-degree term q_*^{-1}B^j eta_1...eta_{j+1}, so the cyclic mode dimension is at least N. Thus G's finite 16 disagreement phases, even if their Foster inequalities are feasible, cannot by themselves yield a finite signed trail matrix; the remaining analytic target is an infinite-dimensional/profile-valued L1(w) block norm or a quantitative regeneration/truncation of this growing mass-mode hierarchy.`
