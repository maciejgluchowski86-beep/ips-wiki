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

Stopped computational implementation: raw enlargement of finite random-map/HJB windows after G007.

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
\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
$$

and

$$
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
$$

Thus zero-frequency locality is exactly tail-shift agreement. Conditional on `Delta_M->0`, the common-mass branch after one insertion has a valid `J`-compatible one-next-segment truncation estimate.

## E9. Green response controlled by far-left damage

For finite zero-boundary chains define

$$
\beta_m(t)
=
\sup_{n,\eta,i}E\sum_{j\le i-m}D_j(t).
$$

F012 proves

$$
\boxed{
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
}
$$

This is the load-bearing interface for any coupling-side front theorem.

## E10. Zero-boundary Hamming susceptibility criterion

Define

$$
\alpha_0(t)=\sup_{n,\eta,i}E\sum_jD_j(t).
$$

Then `beta_m(t)<=alpha_0(t)`, so integrability of `alpha_0` implies `Delta_M->0`. Submultiplicativity further gives

$$
\alpha_0(T)<1\text{ for one }T
\Longrightarrow
\text{tail-shift agreement and exponential }\Delta_M\text{ decay}.
$$

This is sufficient, not equivalent.

## E11. Closed scalar coupling architectures

The same-parent restart theorem and separate stack-clearing minorant remain valid. The exposed-only product and complete nearest-neighbour scalar edge-product/coboundary class are refuted. No finite local scalar Foster state remains.

## E12. Actual common coupling: local erasure and convective alternative

For every finite disagreement seed, every fixed site becomes permanently coupled almost surely. Survival is equivalent to unbounded leftward discovery and hence convective escape to `-infinity`.

The local drift gives moving-frame exponential contraction, but this does not rule out convective survival.

## E13. Full-line finite-time Hamming criterion

Let

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

G proves submultiplicativity. One `alpha(T)<1` would imply exponential extinction of every finite disagreement seed.

## E14. G007 fixed-boundary convergence theorem

For the ordinary finite fixed-boundary CTMC, Meeting 017 accepts

$$
B_{L,R}^e(T)-r_{L,R}(T)
\le\alpha(T)
\le B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T),
$$

with explicit causal Poisson errors. Thus the adversarial right controller is not the obstruction and finite fixed-boundary values converge to `alpha(T)` for every fixed `T`.

## E15. G007 long initial expansion

At

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

an explicit protected-source event yields

$$
\boxed{
\alpha(t)>1\qquad(0<t\le47).
}
$$

Therefore any Hamming contraction, if it exists, occurs only after a long initial amplification regime.

## E16. Raw finite random-map enumeration is stopped

At the first times not excluded by E15, the causal sandwich already requires enormous raw windows. Larger `L,R,T` enumeration and another right-boundary controller are stopped as a proof implementation.

## E17. Meeting 018: retained two-spin pre-exposure exploration

Outside consultation 001 produced, and the Professor checked, a four-state killed exploration retaining

$$
Z=(s,t),
$$

where `s` is the common spin of the current fresh target and `t` the common spin one site farther left. The right neighbour enters through mode `D`, `C0`, or `C1`. The transition rates are exact and the next-left spin `t` is propagated without freshening when the current target first becomes disagreeing.

At the hard point a strict rational superharmonic certificate with

$$
\lambda=\frac1{20},\qquad \rho=\frac58
$$

gives, for first-discovery times `sigma_m`,

$$
\boxed{
P(\sigma_m\le T)
\le\frac{15}{4}e^{T/20}\left(\frac58\right)^m.
}
\tag{AF}
$$

Hence

$$
\boxed{
E\sum_{j<-L}D_j(T)
\le10e^{T/20}\left(\frac58\right)^{L+1}.
}
\tag{AF-tail}
$$

This is a true disagreement-front estimate which preserves the pre-exposure common-spin history and is strictly sharper than the causal Poisson cone.

A second exact certificate gives

$$
\boxed{
\limsup_{t\to\infty}\frac{N_t}{t}
\le\frac{1/100}{\log(100/81)}\approx0.0474561
}
$$

almost surely for the number of newly discovered left sites.

The G007 fixed-boundary sandwich can replace its causal errors by the corresponding `(AF)` errors. This improves truncation structurally but does not restart raw enumeration.

## E18. First-discovery control is not zero-frequency occupation control

The front estimate `(AF)` behaves as `e^{lambda t}rho^m`; at fixed `m` it is not integrable over time. It therefore does not prove the F012 condition.

Define

$$
G_m
:=
\sup_{\text{finite zero-boundary systems},\eta,i}
\int_0^\infty
E\sum_{j\le i-m}D_j(t)\,dt.
$$

The active load-bearing question is

$$
\boxed{
G_m\le C\theta^m
\quad\text{for some }C<\infty,\ \theta<1.
}
\tag{OCC}
$$

If `(OCC)` holds, then immediately

$$
\Delta_M\le2cC\theta^{M-1}.
$$

Unlike first discovery, occupation must control repeated disagreement episodes after exposure. The arbitrary predictable-mode domination used for `(AF)` cannot simply make mode `D` immortal: fixed-site permanent coupling rules that out for the actual process.

## E19. One final common-uniform occupation block

Student G Assignment 008 is the only active block. It must either:

1. prove `(OCC)` by combining the retained two-spin state with actual source-lifetime/re-entry information; or
2. prove a precise structural obstruction showing that this two-spin state cannot control zero-frequency occupation after the already established actual source-lifetime facts are incorporated.

Failure of an immortal adversarial `D` controller alone is too crude and does not count as the obstruction.

If G008 proves `(OCC)`, the stationary tail-shift / first post-insertion mass interface is solved, but arbitrary duration-resolved signed-profile iteration and `J_{x,r}` remain open. If G008 refutes the two-spin occupation exploration or returns unresolved without a genuinely new occupation mechanism, abandon the common-uniform global-coalescence interface; do not enlarge the exposure state or return to raw finite windows by default.

## E20. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; use `16/21` as a global Foster theorem; enlarge scalar local coupling products mechanically; revive a finite common-mass mode state; replace the signed structure by unrestricted total variation; assume an unproved uniform spectral gap / positive rates conjecture; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coupling/front speed; infer survival from finite-time Hamming expansion; turn `(AF)` into an occupation theorem without controlling repeated episodes; or continue by raw larger finite windows alone.
