# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The target is fixed by the principal.

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

The working reduction leaves

$$
\boxed{
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Proving `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits.

## E2. Exact signed branching identity

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first channel is signed common mass; the second is a conditional-law disagreement channel.

## E3. Norm-order obstruction

Near East, duration integration before the absolute value gives the false apparent factor `3/5`, while the actual `J`-compatible depth-two factor tends to `7/5`. Therefore all duration variables remain visible until the final `L^1(w)` modulus.

## E4. Common-mass damping that survives

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

The one-segment duration-resolved transfer has the form

$$
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S(\boldsymbol\nu e^{u\mathbb Q_y}),
$$

where `Q_y` contains the left-block generators. No depth-uniform finite matrix can represent all common-mass modes.

## E6. Finite linear mode closure is impossible

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence the cyclic dimension is at least `N`.

**Status:** exact obstruction. Do not enlarge finite common-mass alphabets.

## E7. Suffix projectivity and first-insertion localization

Rightmost suffixes are autonomous, so semigroup evolution and centered insertion/drop intertwine with suffix marginalization. Consequently

$$
R_{N,M}\pi_N=\pi_M.
$$

The first invariant centered insertion is depth-uniformly finite-context approximable, and a separated spatial gap gives an explicit exponential defect bound. One weighted semigroup segment also has an explicit finite-speed truncation tail.

## E8. Zero-frequency response equals a tail-shift defect

Let `mu=pi_infty^0` be the projective half-line law, let `theta` drop the boundary-nearest spin, and set

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m.
$$

For the post-insertion boundary-response norm `Delta_M`, Assignment 011 proves

$$
\boxed{
\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
}
$$

and

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Thus zero-frequency locality is exactly tail-shift agreement

$$
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
$$

Conditional on `Delta_M->0`, the common-mass branch after one insertion has a valid `J`-compatible one-next-segment truncation estimate.

## E9. Assignment 012: Green response controlled by far-left damage

For finite zero-boundary chains define

$$
\beta_m(t)
=
\sup_{n,\eta,i}E\sum_{j\le i-m}D_j(t).
$$

F proves

$$
\boxed{
\Delta_M
\le
2c\int_0^\infty\beta_{M-1}(t)dt.
}
$$

The boundary generator difference is a single-flip gradient with magnitude at most `c`, and the common graphical map bounds the resulting semigroup gradient by the expected far-left disagreement occupation. The modulus is taken before Green-time integration.

Finite speed gives

$$
\beta_m(t)
\le E[(\operatorname{Pois}(t)-m+1)_+].
$$

## E10. Zero-boundary Hamming susceptibility criterion

Define

$$
\alpha_0(t)
=
\sup_{n,\eta,i}E\sum_jD_j(t)
$$

for all finite zero-boundary chains. Then

$$
\beta_m(t)\le\alpha_0(t),
$$

so dominated convergence gives

$$
\boxed{
\int_0^\infty\alpha_0(t)dt<\infty
\Longrightarrow
\Delta_M\to0.
}
$$

Moreover `alpha_0` is submultiplicative. Hence

$$
\boxed{
\alpha_0(T)<1\text{ for one }T
\Longrightarrow
\text{tail-shift agreement and exponential decay of }\Delta_M.
}
$$

This is a sufficient criterion, not an equivalence.

## E11. Zero-boundary finite certificate

G's controlled finite-window construction extends to `alpha_0`. Besides the full-line controlled problem `A_{L,R}(T)`, include finitely many cases where the fixed zero boundary is within `R` sites of the initial flip. If their maximum is `\widehat A_{L,R}(T)`, then

$$
\boxed{
\alpha_0(T)
\le
\widehat A_{L,R}(T)
+E[(\operatorname{Pois}(T)-L)_+].
}
$$

A strict right side below one proves the tail-shift theorem and explicit post-insertion mass truncation.

**Status:** no such strict certificate yet.

Verifier note: original F012 verifier commit `3750a53` fails because a symbolic geometric-series convergence condition remains in SymPy `Piecewise` form. It is not a passing certificate. Commit `5494008` repairs that tooling issue using an exact rational geometric-series check; the analytic theorem is proved in the report.

## E12. Closed scalar coupling architectures

The same-parent geometric restart theorem and separate stack-clearing minorant remain valid. The exposed-only product and the complete nearest-neighbour scalar edge-product/coboundary class are refuted. No finite local scalar Foster state remains.

## E13. Actual common coupling: local erasure and convective survival alternative

For every finite disagreement seed, every fixed site becomes permanently coupled almost surely. Survival is equivalent to unbounded leftward discovery and therefore to convective escape to `-infinity`.

The local drift satisfies

$$
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1},
\qquad q=1-c+a,
$$

which gives exponential moving-frame contraction for every `z>c/q`. This does not rule out convective survival.

## E14. Full-line finite-time Hamming criterion

Let

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

G proves

$$
\alpha(t+s)\le\alpha(t)\alpha(s).
$$

If

$$
\boxed{\alpha(T)<1}
$$

for one finite `T`, then every finite disagreement seed dies out with exponential block-time tail.

At the hard rational point the worst local geometry has initial Hamming derivative `9997/10000>0`; any contraction must emerge only after nonlocal finite-time clearing.

## E15. Full-line finite controlled-CTMC hierarchy

For the controlled value `A_{L,R}(T)`,

$$
\boxed{
\alpha(T)
\le
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+].
}
$$

One strict finite certificate proves quantitative global extinction. G007 is executing this exact diagnostic and may replace the adversarial right controller by a rigorously convergent finite approximation if necessary.

## E16. Route-level decision after F012

The profile and coupling sides have converged on the same mechanism: **finite-time contraction of complete common-random-map single-flip damage**. The relevant coefficients are different (`alpha_0` for zero-boundary profile locality, full-line `alpha` for global disagreement extinction), so success on one side does not automatically prove the other, but the finite controlled-chain machinery is common.

Direction:

1. Complete G007 unchanged.
2. F is idle; do not duplicate the HJB search while G007 is running.
3. Do not start matrix-product/nonlocal-norm engineering.
4. If G007 proves `alpha(T)<1`, next check the finitely many close-zero-boundary cases needed for `alpha_0(T)<1`, then formulate one combined block-transfer theorem.
5. If G007 proves convective survival or `alpha(T)>=1` for all `T`, close every route requiring eventual global coalescence of this synchronous coupling.
6. If G007 is unresolved and the next proposal is only larger finite windows/controllers or generic matrix-product engineering without a new approximation theorem, stop this implementation and reassess the predecessor-trail route or use a bounded outside consultation.

## E17. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; use `16/21` as a global Foster theorem; enlarge scalar local coupling products mechanically; revive a finite common-mass mode state; replace the signed structure by unrestricted total variation; assume an unproved uniform spectral gap / positive rates conjecture; infer tail-shift agreement from separate tail triviality; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coalescence or moving-frame contraction; infer survival from failure of a finite upper certificate; or treat verifier commit `3750a53` as passing.
