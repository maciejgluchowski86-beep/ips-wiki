# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal.

## E0. Residual chamber

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Closed mechanisms: frozen finite walls; cellwise nonnegative scaffold transfer; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; exposed-only global Foster product; complete nearest-neighbour scalar edge-product/coboundary Foster class; depth-uniform finite linear common-mass mode closure.

## E1. Centered predecessor trail and global criterion

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The working predecessor-trail reduction leaves

$$
\boxed{
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Proving `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits after `J` decay is proved.

## E2. Exact signed branching identity

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first channel is signed common mass; the second is a conditional-law disagreement channel.

## E3. Norm-order obstruction

Near East, duration integration before the absolute value gives a false apparent contraction `3/5`, whereas the actual `J`-compatible depth-two factor tends to `7/5`:

$$
\frac g{|m_\varepsilon|}\left|\int wA_{2,\varepsilon}\right|\to\frac35,
\qquad
\frac g{|m_\varepsilon|}\int w|A_{2,\varepsilon}|\to\frac75.
$$

Therefore all duration variables must remain visible until the final `L^1(w)` norm.

## E4. Common-mass scalar damping

Let

$$
r_0=\frac1{1+b}.
$$

The equilibrium and first transient mass modes satisfy

$$
\boxed{|Br_0-c|Z<\frac23,}
\qquad
\boxed{\kappa_T=BZ_{\omega+1+b}<1.}
$$

These are genuine damping inputs, not an all-depth theorem.

## E5. Exact common-mass transfer is operator-valued

Slice a signed law by the current rightmost spin. The duration-resolved one-segment transfer has the operator form

$$
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S(\boldsymbol\nu e^{u\mathbb Q_y}),
$$

where the entries of `Q_y` contain the left-block generators. No depth-uniform finite matrix replaces this exact object.

## E6. Depth-uniform finite linear common-mass mode closure is impossible

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence the cyclic subspace has dimension at least `N`.

**Status:** exact obstruction. Do not enlarge finite common-mass alphabets.

## E7. Exact suffix projectivity and first-insertion truncation

Rightmost suffixes are autonomous, so semigroup evolution and centered insertion/drop intertwine with suffix marginalization. Consequently

$$
R_{N,M}\pi_N=\pi_M.
$$

For the projective half-line law, the first invariant centered insertion has conditional coefficient

$$
K_M=E[B\eta_0-c\mid\eta_{-M},\ldots,\eta_{-1}],
$$

with

$$
\sup_{n\ge M}\|K_n-K_M\|_1\to0.
$$

This is a genuine depth-uniform finite-context approximation, not finite Markov order.

## E8. Explicit equilibrium localization and one-segment tail

For a bounded test function separated by `M` sites from the boundary,

$$
\left|\pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
$$

One weighted semigroup segment also satisfies

$$
\int_0^\infty w(u)\|P_uf-P_u^{(M)}f\|_\infty du
\le\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.
$$

Scalar iteration is unavailable because it reintroduces `cZ>1`.

## E9. Zero-frequency boundary response

After one insertion the mass branch is `bar pi_N`, not `pi_{N-1}`. Its exact discrepancy is

$$
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].
$$

Finite speed alone is nonintegrable at zero frequency.

## E10. Assignment 011: exact tail-shift reduction

Let `mu=pi_infty^0` be the projective half-line invariant law with boundary-nearest coordinate `X_0`, let

$$
\theta(x_0,x_1,\ldots)=(x_1,x_2,\ldots),
$$

and define

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m.
$$

For

$$
\Delta_M
=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
|\bar\pi_N(f)-\pi_{N-1}(f)|,
$$

F proves

$$
\boxed{
\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}}.
}
$$

Hence `Delta_M` is nonincreasing. Using the density of `theta mu-mu` relative to `(mu+theta mu)/2` and the reverse martingale theorem,

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Therefore the stationary zero-frequency locality question is exactly

$$
\boxed{
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
\tag{TS}
$$

Separate tail 0--1 laws do not imply `(TS)`; the same tail events must receive the same probabilities.

**Status:** exact reduction, unresolved. Student F Assignment 012 must prove or refute `(TS)` or produce a genuinely stronger structural criterion, preferably via finite-window likelihood ratios / relative entropy / boundary influence.

## E11. Conditional one-next-segment lift

Let `m_0=Br_0-c` and `kappa_E=|m_0|Z`. If `Delta_M->0`, then for any `1<=d<M`,

$$
\boxed{
\int_0^\infty w(u)
|m_0(\bar\pi_N-\pi_{N-1})(P_u f)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
$$

Choosing `d~M/2` makes this first post-insertion mass-branch truncation error vanish. Arbitrary signed-profile iteration still remains open.

## E12. Coupling facts and closed local Foster classes

The same-parent geometric restart theorem and separate stack-clearing minorant remain valid. The exposed-only product fails on long all-`01` stacks. The entire nearest-neighbour scalar edge-product/coboundary class is refuted at a strict near-East point by the balanced-circulation AM--GM certificate.

No finite local scalar Foster state remains.

## E13. Current coupling viability test

A successor Student G session is redoing Assignment 006 after the predecessor session failed before committing its work. The task is unchanged: decide whether the common-uniform disagreement process survives forever with positive probability from a finite seed at a strict near-East point.

- Survival closes every proof requiring global coalescence of this synchronous coupling.
- Extinction must be accompanied by a genuinely nonlocal quantitative regeneration theorem.

No uncommitted predecessor reasoning is treated as evidence.

## E14. Route-level checkpoint

Both remaining interfaces are now concrete decision theorems rather than generic requests for a nonlocal norm.

1. F012: prove or refute tail-shift agreement `(TS)`.
2. G006: decide finite-seed survival/extinction of the common-uniform coupling near East.

After both return, hold a route-level expected-value review before authorizing broader matrix-product/nonlocal construction.

## E15. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value, use `16/21` as a global Foster theorem, enlarge scalar local coupling products mechanically, revive a finite common-mass mode state, replace the signed structure by unrestricted total variation, assume an unproved uniform spectral gap / positive rates conjecture, infer tail-shift agreement from separate tail triviality, or infer infinite-tail total-variation decay from fixed finite-window convergence without uniformity in window size.
