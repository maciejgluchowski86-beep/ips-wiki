# Student F 011: zero-frequency boundary-response locality

## Verdict

Assignment 011 asks whether

\[
\Delta_M
=\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
|\bar\pi_N(f)-\pi_{N-1}(f)|
\]

converges to zero. I do not prove or refute that statement.

I do obtain an exact necessary-and-sufficient reformulation which removes the finite-volume Green-kernel notation completely. Let `pi_infty^0` be the projective half-line zero-boundary invariant law from Assignment 010, indexed from the boundary into the left half-line as

\[
X_j=\eta_{-j},\qquad j\ge0,
\]

and let

\[
\theta(x_0,x_1,x_2,\ldots)=(x_1,x_2,x_3,\ldots)
\]

be the spatial shift which moves one site away from the zero boundary. If

\[
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_{m\ge0}\mathcal F_m,
\]

then

\[
\boxed{
\Delta_M
=\|\theta\pi_\infty^0-\pi_\infty^0\|_{\mathcal F_{M-1}}.
}
\]

Consequently `Delta_M` is nonincreasing and

\[
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\pi_\infty^0-\pi_\infty^0\|_{\mathcal T}.
}
\]

In particular,

\[
\boxed{
\Delta_M\to0
\iff
\theta\pi_\infty^0\text{ and }\pi_\infty^0
\text{ agree on the remote-left tail sigma-field }\mathcal T.
}
\]

This is the precise half-line spatial-mixing theorem which decides Assignment 011. Failure is equally concrete: there must exist a left-tail event whose probability changes under one spatial shift.

This reformulation also shows why the positive results of Assignment 010 do not by themselves settle the zero-frequency problem. Finite-context approximation of the boundary conditional `K_M` concerns one conditional observable near the zero boundary; the new statement concerns total variation of the **entire infinite spatial tail** under a shift. Even perfect local conditional truncation does not imply tail-shift agreement in general.

I also prove the requested one-step lift conditional on `Delta_M->0`. Let

\[
m_0=Br_0-c,
\qquad r_0=\frac1{1+b}.
\]

After the first centered insertion, the common-mass branch is `m_0 bar pi_N`. For `1<=d<M` and every `f` supported in `{1,...,N-M}`,

\[
\boxed{
\int_0^\infty w(u)
\left|
 m_0(\bar\pi_N-\pi_{N-1})(P_u^{N-1,0}f)
\right|du
\le
|m_0|
\left[
 Z\Delta_{M-d}
+\frac{4}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
\]

Equivalently, using `kappa_E=|m_0|Z<2/3`,

\[
\le
\left[
\kappa_E\Delta_{M-d}
+\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
\]

Thus if the tail-shift theorem is true, choosing `d=floor(M/2)` gives a genuine duration-resolved truncation of the mass branch after one centered insertion. The absolute value remains inside the `u`-integral throughout, so this does not violate the Meeting 009 norm-order restriction.

The remaining obstacle before arbitrary iteration would still be the disagreement channel and repeated signed profile composition. Student G's common-coupling survival/extinction test is independent and is not used here.

Supporting exact finite-volume indexing checks are committed as

`students/student-f/011-zero-frequency-boundary-response-verifier.py`.

## 1. Accepted input

Work in the strict residual chamber and put

\[
B=b+c-a,
\qquad g=b-a,
\qquad\omega=1-c+a,
\qquad r_0=\frac1{1+b},
\]

with

\[
w(u)=e^{-\omega u}s_1(u),
\qquad Z=\int_0^\infty w(u)du.
\]

From Assignment 010 and Meeting 013 we use:

1. right-suffix projectivity
   \[
   R_{N,M}\pi_N=\pi_M;
   \]
2. the exact zero-frequency response
   \[
   \bar\pi_N(f)-\pi_{N-1}(f)
   =\pi_N\left[
   \eta_ND\int_0^\infty
   P_t^{N-1,0}(f-\pi_{N-1}(f))dt
   \right];
   \]
3. one-segment finite propagation
   \[
   \int_0^\infty
   w(u)\|P_uf-P_u^{(d)}f\|_\infty du
   \le\frac{2}{\omega(1+\omega)^d}\|f\|_\infty;
   \]
4. the equilibrium mass loss
   \[
   \kappa_E=|Br_0-c|Z<\frac23.
   \]

No spectral gap, common-coupling extinction, or finite scalar Foster theorem is assumed.

## 2. Half-line coordinates

By suffix projectivity, the finite laws `(pi_N)` define a unique probability law

\[
\mu:=\pi_\infty^0
\]

on

\[
\Omega=\{0,1\}^{\mathbb N_0},
\]

where `X_0` is the spin adjacent to the fixed zero boundary and `X_j` is the spin `j` sites farther left.

Thus the original left-to-right finite vector under `pi_N` is distributed as

\[
(X_{N-1},X_{N-2},\ldots,X_0).
\tag{2.1}
\]

Let

\[
\theta:\Omega\to\Omega,
\qquad
(\theta x)_j=x_{j+1}.
\tag{2.2}
\]

For a sigma-field `G`, use the variation seminorm

\[
\|\nu-\rho\|_{\mathcal G}
:=\sup_{\substack{|F|\le1\\F\ \mathcal G\text{-measurable}}}
|\nu(F)-\rho(F)|.
\tag{2.3}
\]

This is the same normalization as the supremum in the definition of `Delta_M`; for probability measures it is twice the event-normalized total-variation distance.

## 3. Exact identification of `Delta_M`

For `m>=0`, set

\[
\mathcal F_m=\sigma(X_j:j\ge m).
\tag{3.1}
\]

### Proposition 3.1

For every `M>=2`,

\[
\boxed{
\Delta_M
=\|\theta\mu-\mu\|_{\mathcal F_{M-1}}.
}
\tag{3.2}
\]

Equivalently,

\[
\Delta_M
=\|\theta^M\mu-\theta^{M-1}\mu\|_{\rm TV}
\tag{3.3}
\]

on the full reindexed half-line.

### Proof

Fix `N>=M+1` and put `L=N-M`. A function occurring in the definition of `Delta_M` depends on the finite block of original sites

\[
1,\ldots,L.
\]

Under `bar pi_N`, this block has the law of

\[
(X_{N-1},X_{N-2},\ldots,X_M).
\]

Under `pi_{N-1}`, the same labelled function has the law of

\[
(X_{N-2},X_{N-3},\ldots,X_{M-1}).
\]

After reversing the order inside the finite block, these are respectively the first `L` coordinates of `theta^M mu` and `theta^{M-1} mu`. Equivalently, they are the restrictions of `theta mu` and `mu` to finite cylinder functions in `F_{M-1}`.

Taking the supremum over `N`, hence over all finite cylinder lengths `L`, gives (3.2). Finite cylinder functions generate `F_{M-1}`, and the variation norm of two finite measures on a countable product space is the supremum over cylinder-measurable bounded functions. Equation (3.3) is the same statement after reindexing the tail. `square`

### Corollary 3.2

The sequence `Delta_M` is nonincreasing.

### Proof

The sigma-fields decrease:

\[
\mathcal F_M\subset\mathcal F_{M-1}.
\]

Restriction to a smaller sigma-field cannot increase variation. `square`

This monotonicity is not visible from the zero-frequency Green formula itself.

## 4. Exact tail limit

Define the remote-left spatial tail sigma-field

\[
\mathcal T
:=\bigcap_{m\ge0}\mathcal F_m.
\tag{4.1}
\]

### Theorem 4.1

One has

\[
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
\tag{4.2}
\]

Consequently

\[
\boxed{
\Delta_M\to0
\iff
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
\tag{4.3}
\]

### Proof

Let

\[
\lambda=\frac12(\mu+\theta\mu)
\]

and let

\[
H=\frac{d(\theta\mu-\mu)}{d\lambda}.
\]

Then `H` is bounded. For every sub-sigma-field `G`, the restriction of the signed measure `theta mu-mu` to `G` has density

\[
E_\lambda[H\mid\mathcal G]
\]

with respect to `lambda|_G`. Hence

\[
\|\theta\mu-\mu\|_{\mathcal G}
=\int
\left|E_\lambda[H\mid\mathcal G]\right|d\lambda.
\tag{4.4}
\]

Apply this to the decreasing sigma-fields `F_m`. The reverse martingale theorem gives

\[
E_\lambda[H\mid\mathcal F_m]
\longrightarrow
E_\lambda[H\mid\mathcal T]
\]

in `L^1(lambda)`. Taking the integrals of the absolute values in (4.4) proves (4.2). Equation (4.3) follows because the variation norm on `T` vanishes exactly when the two restricted measures agree. `square`

### Corollary 4.2: exact failure certificate

If `(2)` in Assignment 011 is false, then there is a tail event

\[
A\in\mathcal T
\]

such that

\[
\boxed{
\mu(A)\ne\mu(\theta^{-1}A).
}
\tag{4.5}
\]

Thus failure is not merely slow finite-volume mixing: the fixed zero boundary selects a spatial tail law which changes under one translation even arbitrarily far to the left.

Conversely, absence of such a tail-shift defect is exactly the desired zero-frequency locality theorem.

## 5. Why Assignment 010 does not already prove Theorem 4.1 has zero right side

Assignment 010 proves that

\[
K_M=E[BX_0-c\mid X_1,\ldots,X_M]
\]

converges in `L^1`. That is a martingale approximation of one bounded boundary observable. It does not control the variation distance between the entire infinite tails in (4.2).

This logical gap is real even outside the IPS setting. Consider an independent nonstationary product law on `(X_j)_{j>=0}` with

\[
P(X_j=1)=
\begin{cases}
p+\delta,&j\text{ even},\\
p-\delta,&j\text{ odd},
\end{cases}
\]

for `0<delta<min(p,1-p)`. Then every conditional expectation of the boundary variable `X_0` given the left coordinates is already constant, so the analogue of `K_M` truncates exactly at `M=0`. Boundary/far-left correlations also vanish identically. Nevertheless the law and its one-step shift are mutually singular on the tail: the empirical densities on the even and odd subsequences distinguish them almost surely. In our variation normalization their tail-shift defect is `2` for every `M`.

This example is **not** claimed to arise from the IPS. It only shows that the accepted martingale and separated-correlation estimates cannot imply (4.3) without an additional dynamical theorem.

## 6. Conditional lift to one post-insertion mass branch

The tail-shift theorem would immediately do more than the static statement in Assignment 011.

Let

\[
\delta_N:=\bar\pi_N-\pi_{N-1}
\tag{6.1}
\]

on the `(N-1)`-site zero-boundary state space. Let `f` satisfy

\[
\|f\|_\infty\le1,
\qquad
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}.
\]

Fix `1<=d<M` and set

\[
R=N-M+d.
\]

Let `\widehat P_u f` be the semigroup obtained by evolving only the sites `1,...,R` with a fixed zero boundary at `R+1`, viewed as a function on the full `(N-1)`-site space. It is supported in `{1,...,R}`. Hence, by the definition of `Delta`,

\[
|\delta_N(\widehat P_u f)|
\le
\Delta_{M-d}\|f\|_\infty.
\tag{6.2}
\]

Finite propagation across the `d`-site buffer gives the conservative pointwise estimate

\[
\|P_u^{N-1,0}f-\widehat P_u f\|_\infty
\le
2\|f\|_\infty
P(\operatorname{Pois}(u)\ge d).
\tag{6.3}
\]

Since `delta_N` is a difference of two probability measures,

\[
|\delta_N(g)|\le2\|g\|_\infty.
\]

Combining (6.2)--(6.3), retaining the absolute value at each duration `u`, and using `s_1(u)<=1`,

\[
\begin{aligned}
\int_0^\infty w(u)
|\delta_N(P_u^{N-1,0}f)|du
&\le
Z\Delta_{M-d}\|f\|_\infty\\
&\quad+4\|f\|_\infty
\int_0^\infty e^{-\omega u}
P(\operatorname{Pois}(u)\ge d)du.
\end{aligned}
\]

The accepted Laplace--Poisson identity gives

\[
\boxed{
\int_0^\infty w(u)
|\delta_N(P_u^{N-1,0}f)|du
\le
\left[
Z\Delta_{M-d}
+\frac{4}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
\tag{6.4}
\]

At the first invariant centered insertion, the common-mass coefficient is

\[
m_0=Br_0-c.
\]

Therefore the duration-resolved mass-branch truncation error is

\[
\boxed{
\int_0^\infty w(u)
\left|
 m_0\delta_N(P_u^{N-1,0}f)
\right|du
\le
\left[
\kappa_E\Delta_{M-d}
+\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
\tag{6.5}
\]

If `Delta_M->0`, choose for example

\[
d=\lfloor M/2\rfloor.
\]

Both terms in (6.5) then tend to zero uniformly in `N`. Thus **the truth of the stationary tail-shift theorem would already prove a `J`-compatible, one-next-segment truncation for the mass branch after one centered insertion.**

This is stronger than simply replacing `bar pi_N` by `pi_{N-1}` at time zero.

## 7. What would still remain

Even if (4.3) is proved, arbitrary trail iteration is not automatic.

1. The disagreement branch in
   \[
   g\mu(h_{p_*}(\eta_y)f)
   =(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f)
   \]
   remains outside the common-mass estimate.
2. After further signed transfers the input is no longer one of the two stationary measures appearing in `Delta_M`; one needs a block argument showing that accumulated truncation errors remain subordinate to the genuine mass losses `kappa_E<2/3` and `kappa_T<1`.
3. Student G's Assignment 006 may rule the common-uniform global-coalescence route in or out, but no conclusion from it is used here.

So a positive answer to Assignment 011 would be a real missing first post-insertion estimate, not the final `J` theorem.

## 8. Current blocker

I tested the obvious routes against the anti-circularity requirement.

- Finite speed alone cannot decide the tail norm because the zero-frequency Green integral has no long-time damping.
- A depth-uniform sup-norm mixing estimate would decide it, but proving such an estimate is at least as strong as the nonlocal regeneration issue under investigation and cannot be assumed.
- The accepted `K_M` martingale truncation and separated-gap covariance estimate do not imply tail-shift agreement, as Section 5 shows.
- Both scalar coupling Foster architectures are already refuted and are not used.

The exact remaining theorem is therefore (4.3): **tail-shift agreement for the projective half-line zero-boundary invariant law.** This is a static spatial statement, but it contains precisely the long-time cancellation hidden in the zero-frequency Green response.

A proof could come from a genuinely dynamical theorem establishing tail equivalence/triviality for `mu` and `theta mu`, or from a direct signed Green-kernel argument. A counterexample would be a tail event satisfying (4.5).

## Handoff

`unresolved after substantive work; exact Green-kernel blocker: the Assignment-011 quantity is exactly the remote-tail shift defect of the projective half-line invariant law. If mu=pi_infty^0, theta drops the boundary-nearest spin, F_m=sigma(X_j:j>=m), and T=intersection_m F_m, then Delta_M=||theta mu-mu||_{F_{M-1}} is nonincreasing and reverse-martingale convergence gives lim_M Delta_M=||theta mu-mu||_T. Hence zero-frequency boundary locality holds iff mu and theta mu agree on the left spatial tail sigma-field; failure is equivalent to a tail event whose probability changes under one shift. The accepted first-insertion martingale truncation does not imply this stronger tail statement. Conditional on Delta_M->0, the mass branch after one centered insertion already has the J-compatible one-next-segment truncation bound kappa_E Delta_{M-d}+4|Br_0-c|/[omega(1+omega)^d], so d~M/2 makes that error vanish. The remaining unknown is therefore the tail-shift theorem itself, not another finite-volume profile bookkeeping step.`