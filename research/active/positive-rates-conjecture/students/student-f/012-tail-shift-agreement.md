# Student F 012: tail-shift agreement decision block

## Verdict

Assignment 012 asks for one bounded attempt to decide the tail-shift theorem

\[
\|\theta^M\mu-\theta^{M-1}\mu\|_{\rm TV}\longrightarrow0,
\]

where `mu=pi_infty^0` is the projective half-line zero-boundary invariant law. I do **not** prove or refute this theorem.

I obtain a new structural criterion which is materially stronger than the tail-shift restatement and which interfaces directly with Student G's completed Assignment 006.

Let `Phi_t^{n,0}` denote the common-uniform random map for the `n`-site zero-boundary chain. For one initial flip at site `i`, let `D_j(t)` be the disagreement indicator. Define the zero-boundary Hamming amplification

\[
\alpha_0(t)
:=
\sup_{n\ge1}\sup_{\eta,i}
E\sum_jD_j(t),
\tag{0.1}
\]

and its far-left damage kernel

\[
\beta_m(t)
:=
\sup_{n\ge1}\sup_{\eta,i}
E\sum_{j\le i-m}D_j(t),
\qquad m\ge1.
\tag{0.2}
\]

Then the exact zero-frequency boundary response from Assignment 010 satisfies

\[
\boxed{
\Delta_M
\le
2c\int_0^\infty \beta_{M-1}(t)\,dt.
}
\tag{0.3}
\]

This is the main new theorem of the block. It converts the stationary spatial tail problem into an **integrated single-flip damage susceptibility** for the actual zero-boundary common random map.

Finite speed gives, with `N_t~Pois(t)`,

\[
\boxed{
\beta_m(t)
\le
u_m(t)
:=
E[(N_t-m+1)_+].
}
\tag{0.4}
\]

Trivially `beta_m(t)<=alpha_0(t)`. Hence

\[
\boxed{
\int_0^\infty\alpha_0(t)dt<\infty
\quad\Longrightarrow\quad
\Delta_M\to0.
}
\tag{0.5}
\]

The implication is by dominated convergence: for each fixed `t`, `nu_m(t)->0`, while `beta_m(t)<=alpha_0(t)`.

The criterion is finite-time certifiable. The coefficient `alpha_0` is submultiplicative. If for one `T>0`

\[
\boxed{
\alpha_0(T)\le\rho<1,
}
\tag{0.6}
\]

then `alpha_0` is integrable and tail-shift agreement follows. More quantitatively, putting `m=M-1`, `S=m/4`,

\[
\boxed{
\begin{aligned}
\Delta_M
\le 2c\Bigg\{&
2^{-(m-1)}\left[\left(\frac m4-1\right)e^{m/4}+1\right]\\
&+
\frac{(T+T^2/2)\rho^{\lfloor m/(4T)\rfloor}}
{1-\rho}
\Bigg\}.
\end{aligned}
}
\tag{0.7}
\]

Both terms decay exponentially in `M` at every fixed `T,rho<1`.

Student G's Assignment 006 supplies an exact controlled-CTMC hierarchy for finite-time common-random-map damage. Its certificate

\[
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+]<1
\]

controls an infinite-volume single-flip problem by a finite HJB system plus a Poisson cone tail. For the present zero-boundary use one must also include the finitely many cases in which the fixed zero boundary lies closer than the chosen right-control cutoff `R`; this is still a finite controlled-CTMC maximization. Thus one finite strict HJB inequality can certify (0.6), and therefore `(TS)`, without any scalar Foster product or matrix-product construction.

This is real leverage but not a solution: no such strict finite-time certificate is currently proved at the hard near-East point. Conversely `alpha_0(T)>=1` for all `T` would not by itself refute tail-shift agreement, because (0.5) is sufficient rather than necessary.

The result also clarifies the interface with G. G proved that every finite common-uniform seed coalesces permanently at each fixed site, while possible survival is convective escape to the left. Equation (0.3) shows exactly the corresponding common-mass issue: tail-shift agreement follows once the **time-integrated amount of convective single-flip damage reaching arbitrarily far left is summable**. G's one-block Hamming contraction would imply this immediately. No general nonlocal norm is needed to state or certify the criterion.

If (0.6) is later certified, combining (0.7) with Assignment 011's already accepted one-next-segment estimate gives an explicit post-insertion common-mass truncation bound. It still would not close repeated signed profiles or the disagreement channel.

Supporting exact checks are in

`students/student-f/012-tail-shift-agreement-verifier.py`.

## 1. Inputs and notation

Work at a fixed strict residual point. Put

\[
B=b+c-a,
\qquad
g=b-a,
\qquad
\omega=1-c+a.
\]

The residual inequalities imply

\[
c>g>0.
\tag{1.1}
\]

For the `(N-1)`-site zero-boundary generator write

\[
L^0=L^{N-1,0}.
\]

Let `L^1` denote the same generator with boundary spin one at the rightmost site and define

\[
D=L^1-L^0.
\tag{1.2}
\]

Assignment 010 and Meeting 013 establish, for every bounded `f` on sites `1,...,N-1`,

\[
\boxed{
\delta_N(f)
:=
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND
\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].
}
\tag{1.3}
\]

Assignment 011 identifies

\[
\Delta_M
=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M\}}}
|\delta_N(f)|
\tag{1.4}
\]

with the tail-shift variation of the projective half-line invariant law.

No spectral gap, tail-shift theorem, or common-coupling extinction is assumed below.

## 2. The boundary operator is a single-flip gradient

Let `i=N-1` be the rightmost retained site. If `xi_i=0`, changing the fixed boundary from zero to one changes its flip rate from `1` to `1-c`, so the rate difference is `-c`. If `xi_i=1`, the rate changes from `b` to `a`, so the difference is `-g`.

Thus for every bounded `h`,

\[
\boxed{
Dh(\xi)
=-d(\xi_i)\,[h(\xi^i)-h(\xi)],
\qquad
d(0)=c,\ d(1)=g.
}
\tag{2.1}
\]

By (1.1),

\[
\boxed{
|Dh(\xi)|
\le
c\,|h(\xi^i)-h(\xi)|.
}
\tag{2.2}
\]

Since `D` kills constants, (1.3) gives

\[
|\delta_N(f)|
\le
c\int_0^\infty
\sup_\xi
|P_t^{N-1,0}f(\xi^i)-P_t^{N-1,0}f(\xi)|dt.
\tag{2.3}
\]

This is the point where the common random map enters.

## 3. Common-map damage kernel

For each finite zero-boundary interval use the common-uniform graphical construction. Starting from `(xi,xi^i)`, let

\[
D_j^{\xi,i}(t)
=1_{\{\Phi_t^{n,0}\xi(j)\ne
\Phi_t^{n,0}\xi^i(j)\}}.
\]

Define (0.1)--(0.2), taking the supremum only over valid sites of the finite interval. Equivalently one may take the supremum over interval size first and then over the initial single flip.

### Proposition 3.1 (Green response bounded by far-left damage)

For every `M>=2`,

\[
\boxed{
\Delta_M
\le
2c\int_0^\infty\beta_{M-1}(t)dt.
}
\tag{3.1}
\]

### Proof

Fix `N>=M+1` and an `f` in (1.4). Its support lies at least `M-1` edges to the left of the boundary site `i=N-1` of the `(N-1)`-site semigroup.

Apply the same graphical map to `xi` and `xi^i`. Then

\[
\begin{aligned}
&|P_t f(\xi^i)-P_t f(\xi)|\\
&\qquad\le
2\|f\|_\infty
P\bigl(
D_j^{\xi,i}(t)=1
\text{ for some }j\in\operatorname{supp}f
\bigr)\\
&\qquad\le
2\|f\|_\infty
E\sum_{j\le i-(M-1)}D_j^{\xi,i}(t)\\
&\qquad\le
2\|f\|_\infty\beta_{M-1}(t).
\end{aligned}
\tag{3.2}
\]

Insert this in (2.3), use `||f||_infty<=1`, and take both suprema in (1.4). `square`

This estimate is taken at each Green time `t` before integration. It therefore contains no signed-time averaging trick analogous to the forbidden trail-duration `3/5` calculation.

## 4. Finite speed gives the spatial cutoff

A single disagreement cannot be created to the right of its initial site. To reach the site `m` steps to its left by time `t`, at least `m` successive leftward update rings are needed. Student G's Assignment 006 proves the exact bound

\[
P(\sigma_m\le t)
\le
P(\operatorname{Pois}(t)\ge m).
\tag{4.1}
\]

Therefore, for every `r>=m`,

\[
P(D_{i-r}(t)=1)
\le
P(\operatorname{Pois}(t)\ge r).
\]

Summing gives

\[
\boxed{
\beta_m(t)
\le
\sum_{r=m}^\infty
P(\operatorname{Pois}(t)\ge r)
=
E[(N_t-m+1)_+]
=:\nu_m(t).
}
\tag{4.2}
\]

Also, by definition,

\[
\boxed{\beta_m(t)\le\alpha_0(t).}
\tag{4.3}
\]

For every fixed `t`, `nu_m(t)->0` as `m->infinity`.

### Corollary 4.1 (integrable susceptibility criterion)

If

\[
\boxed{
\chi_0
:=
\int_0^\infty\alpha_0(t)dt<\infty,
}
\tag{4.4}
\]

then

\[
\boxed{\Delta_M\to0.}
\tag{4.5}
\]

### Proof

By (4.2)--(4.3),

\[
0\le\beta_m(t)
\le
\min\{\alpha_0(t),\nu_m(t)\}.
\]

The second term tends to zero at every fixed `t`, and the first is integrable by assumption. Dominated convergence gives

\[
\int_0^\infty\beta_m(t)dt\to0.
\]

Use (3.1). `square`

This criterion is not another form of `(TS)`: `alpha_0(t)` is a finite-time random-map quantity defined before any stationary law is introduced.

## 5. Finite-time Hamming contraction implies the criterion

The path-coupling proof in Student G Assignment 006 applies verbatim to every finite zero-boundary interval. Taking the supremum over interval size preserves the inequalities. Hence

\[
\boxed{
\alpha_0(t+s)
\le
\alpha_0(t)\alpha_0(s).
}
\tag{5.1}
\]

The same finite-speed support argument gives

\[
\boxed{
\alpha_0(t)\le1+t.
}
\tag{5.2}
\]

Suppose now

\[
\alpha_0(T)\le\rho<1.
\tag{5.3}
\]

For `t=nT+s`, `0<=s<T`,

\[
\alpha_0(t)
\le
\rho^n(1+s).
\tag{5.4}
\]

Consequently

\[
\boxed{
\chi_0
\le
\frac{T+T^2/2}{1-\rho}<\infty.
}
\tag{5.5}
\]

Corollary 4.1 proves `(TS)`.

This already gives a new cross-interface conclusion:

> a single finite-time global Hamming contraction for the zero-boundary common random map simultaneously proves the stationary tail-shift theorem needed by F and a quantitative complete-coupling property for that zero-boundary map.

It is stronger than necessary for `(TS)`, but it is concrete and finite-time.

## 6. Explicit exponential tail-shift bound

The previous implication can be made quantitative.

For `N_t~Pois(t)`,

\[
\nu_m(t)
=E[(N_t-m+1)_+]
\le
E[N_t1_{\{N_t\ge m\}}].
\tag{6.1}
\]

Using the Poisson identity

\[
E[N_t1_{\{N_t\ge m\}}]
=tP(N_t\ge m-1)
\]

and exponential Markov with `2^{N_t}`,

\[
P(N_t\ge m-1)
\le
2^{-(m-1)}E[2^{N_t}]
=
2^{-(m-1)}e^t.
\]

Thus

\[
\boxed{
\nu_m(t)
\le
t e^t2^{-(m-1)}.
}
\tag{6.2}
\]

Put

\[
S=\frac m4,
\qquad
K=\left\lfloor\frac{m}{4T}\right\rfloor.
\]

On `[0,S]`, (6.2) gives

\[
\begin{aligned}
\int_0^S\beta_m(t)dt
&\le
2^{-(m-1)}\int_0^S te^t dt\\
&=
2^{-(m-1)}[(S-1)e^S+1].
\end{aligned}
\tag{6.3}
\]

On `[S,infinity)`, enlarge to `[KT,infinity)` and use (5.4):

\[
\begin{aligned}
\int_S^\infty\beta_m(t)dt
&\le
\int_{KT}^\infty\alpha_0(t)dt\\
&\le
\sum_{n=K}^\infty
\rho^n\int_0^T(1+s)ds\\
&=
\frac{(T+T^2/2)\rho^K}{1-\rho}.
\end{aligned}
\tag{6.4}
\]

Combining (3.1), (6.3), and (6.4) gives (0.7).

The first term has exponential rate

\[
\log2-\frac14>0,
\]

and the second rate is

\[
-\frac{\log\rho}{4T}>0.
\]

Hence the tail-shift variation decays exponentially whenever a single finite-time Hamming contraction is certified.

## 7. Exact finite controlled-CTMC interface

Student G does not prove `alpha(T)<1` at the hard near-East point, but Assignment 006 gives a finite upper-certificate hierarchy for the full common random map. The same construction gives a finite certificate for `alpha_0(T)`.

Fix left cutoff `L` and a right common-history cutoff `R`. On `[-L,0]` retain full coupled pair states; on the agreed sites `[1,R]` retain the common spins; at `R+1` allow an arbitrary predictable common boundary controller. Let

\[
A_{L,R}(T)
\]

be G's finite HJB value: maximal expected disagreements in `[-L,0]` at time `T`, optimized over finite initial states and the controller. Let

\[
\ell_L(T)=E[(\operatorname{Pois}(T)-L)_+].
\tag{7.1}
\]

For an infinite right common environment G proves

\[
\alpha(T)\le A_{L,R}(T)+\ell_L(T).
\tag{7.2}
\]

For the supremum `alpha_0(T)` over finite zero-boundary intervals there are also finitely many geometries in which the fixed zero boundary lies fewer than `R+1` sites to the right of the initial flip. Denote their analogous finite HJB values by

\[
A^0_{L,r}(T),
\qquad0\le r<R.
\]

Define

\[
\widehat A_{L,R}(T)
:=
\max\left\{
A_{L,R}(T),
A^0_{L,0}(T),\ldots,A^0_{L,R-1}(T)
\right\}.
\tag{7.3}
\]

Exactly the same truncation argument then gives

\[
\boxed{
\alpha_0(T)
\le
\widehat A_{L,R}(T)+\ell_L(T).
}
\tag{7.4}
\]

Indeed, if the fixed zero boundary is at distance at least `R+1`, its first `R` common sites plus their actual right input are an admissible history for G's controller. If it is closer, one of the finitely many `A^0_{L,r}` problems applies. Damage left of `-L` is always bounded by the same Poisson discovery tail.

Therefore the finite inequality

\[
\boxed{
\widehat A_{L,R}(T)+\ell_L(T)<1
}
\tag{7.5}
\]

for one triple `(L,R,T)` proves the tail-shift theorem with the explicit bound (0.7).

This is a finite continuous-time control calculation, not an open-ended nonlocal norm construction. It is also genuinely stronger information than fixed-window convergence: one strict inequality controls all remaining tail windows simultaneously.

At the strict near-East point

\[
(a,b,c)=\left(10^{-4},10^{-2},1-10^{-4}\right),
\]

G verifies that a worst local zero-boundary geometry has initial total-Hamming derivative

\[
c-(1-c+a)=\frac{9997}{10000}>0.
\]

Hence any successful certificate (7.5) must occur at a genuinely nonlocal time scale after initial damage expansion. I have not found such a certificate in this block.

## 8. Consequence for the one-next-segment common-mass branch

Assignment 011 already proves that for

\[
m_0=Br_0-c,
\qquad
\kappa_E=|m_0|Z<\frac23,
\]

and any `1<=d<M`,

\[
\int_0^\infty w(u)
|m_0\delta_N(P_uf)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
\tag{8.1}
\]

If (7.5) is certified, insert the explicit right side of (0.7) for `Delta_{M-d}` and choose `d=floor(M/2)`. This gives an explicit exponentially vanishing truncation error for the common-mass branch after one centered insertion, with every trail duration still inside its required absolute value.

This would not yet control:

1. the disagreement branch of the mass/disagreement identity;
2. arbitrary repeated signed-profile composition;
3. the final trail quantity `J_{x,r}`.

So even a positive certificate should feed the Professor's route-level review rather than automatically trigger a general matrix-product construction.

## 9. Likelihood/entropy route

I also tested the finite-window likelihood-ratio formulation requested in Assignment 012. For fixed `M`, the likelihood ratios

\[
R_{M,L}
=\frac{d\mu_{M,L}}{d\mu_{M-1,L}}
\]

form the usual likelihood martingale as `L` grows, and the corresponding relative entropies are nondecreasing in `L`. Finite-state positivity alone therefore points in the wrong direction for the required **uniform in `L`** estimate. I found no generator identity making those entropy increments telescope or supplying a uniform entropy budget.

This is not used as negative evidence for `(TS)`. It only explains why the new damage-susceptibility criterion is more informative than another likelihood restatement: (7.5) is a single finite inequality which would force all infinite-tail likelihood ratios to converge to one in `L^1` through the already proved variation bound.

## 10. Status and handoff

### Established in this block

1. The exact Green response obeys
   \[
   \Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
   \]
2. Finite speed gives
   \[
   \beta_m(t)\le E[(\operatorname{Pois}(t)-m+1)_+].
   \]
3. Integrable zero-boundary Hamming susceptibility
   \[
   \int_0^\infty\alpha_0(t)dt<\infty
   \]
   proves tail-shift agreement.
4. A single finite-time contraction `alpha_0(T)<1` implies that integrability and gives the explicit exponential bound (0.7).
5. G's controlled finite-time HJB construction extends to a finite certificate `(7.5)` for this zero-boundary coefficient.
6. Such a certificate would also make Assignment 011's one-next-segment common-mass truncation explicit and exponentially decaying.

### Not established

- tail-shift agreement `(TS)` unconditionally;
- a tail-shift counterexample;
- `alpha_0(T)<1` at the hard near-East point;
- G's full-line `alpha(T)<1`;
- convective survival of the common-uniform coupling.

The common-mass stationary question and G's coupling question have therefore converged onto one useful nonlocal finite-time diagnostic, but neither has been decided.

`unresolved after substantive work; exact tail-shift blocker: the zero-frequency response is bounded by the integrated far-left single-flip damage kernel Delta_M <= 2c integral beta_{M-1}(t)dt. Hence integrability of the zero-boundary Hamming susceptibility alpha_0 proves tail-shift agreement, and one finite-time contraction alpha_0(T)<1 gives an explicit exponential Delta_M bound. Moreover alpha_0(T)<1 has a finite controlled-CTMC certificate obtained from G's HJB hierarchy plus finitely many near-zero-boundary geometries and the exact Poisson cone tail. No such strict certificate, and no tail-shift counterexample, is currently proved at the hard near-East point.`