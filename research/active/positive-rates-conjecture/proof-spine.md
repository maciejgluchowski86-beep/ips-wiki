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

Finite speed gives

$$
\beta_m(t)\le E[(\operatorname{Pois}(t)-m+1)_+].
$$

## E10. Zero-boundary Hamming susceptibility criterion

Define

$$
\alpha_0(t)=\sup_{n,\eta,i}E\sum_jD_j(t).
$$

Then `beta_m(t)<=alpha_0(t)`, so

$$
\boxed{
\int_0^\infty\alpha_0(t)dt<\infty
\Longrightarrow
\Delta_M\to0.
}
$$

Moreover `alpha_0` is submultiplicative, hence

$$
\boxed{
\alpha_0(T)<1\text{ for one }T
\Longrightarrow
\text{tail-shift agreement and exponential }\Delta_M\text{ decay}.}
$$

This is sufficient, not equivalent.

## E11. Closed scalar coupling architectures

The same-parent restart theorem and separate stack-clearing minorant remain valid. The exposed-only product and complete nearest-neighbour scalar edge-product/coboundary class are refuted. No finite local scalar Foster state remains.

## E12. Actual common coupling: local erasure and convective alternative

For every finite disagreement seed, every fixed site becomes permanently coupled almost surely. Survival is equivalent to unbounded leftward discovery and hence convective escape to `-infinity`.

The local drift satisfies

$$
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1},
\qquad q=1-c+a,
$$

which gives exponential moving-frame contraction for every `z>c/q`. This does not rule out convective survival.

## E13. Full-line finite-time Hamming criterion

Let

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

G proves submultiplicativity. If

$$
\alpha(T)<1
$$

for one finite `T`, every finite disagreement seed dies out with an exponential block-time tail.

## E14. G007 fixed-boundary convergence theorem

For the ordinary finite fixed-boundary CTMC on `[-L,R]`, let `B_{L,R}^e(T)` be the maximal expected disagreement count in `[-L,0]` and put

$$
r_{L,R}(T)
=(L+1)P(\operatorname{Pois}(T)\ge R+1),
$$

$$
\ell_L(T)
=E[(\operatorname{Pois}(T)-L)_+].
$$

Meeting 017 accepts

$$
\boxed{
B_{L,R}^e(T)-r_{L,R}(T)
\le\alpha(T)
\le B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T).
}
$$

Also the old adversarial controlled value satisfies

$$
0\le A_{L,R}(T)-B_{L,R}^e(T)\le r_{L,R}(T).
$$

Thus the right controller is quantitatively harmless and `alpha(T)` has a genuine two-sided finite approximation for every fixed `T`.

## E15. G007 long initial-expansion theorem

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

The certified lower bound at `T=47` exceeds `1.008204288867933`.

Therefore any Hamming contraction, if it exists, occurs only after a long initial amplification regime.

## E16. Raw finite random-map enumeration is stopped

At `T=47`, even the diagnostic requirement of less than `1%` error on each causal side forces `L>=67`, `R>=74`, with naive state count `2^210`. This is not a universal lower bound on proof complexity, but it shows that the now-rigorous causal sandwich does not make direct full-state enumeration a plausible next proof block.

**Status:** no larger-`L,R,T` G008 variant; no new boundary-controller variant.

## E17. Current structural fork

The only coupling-side continuations that change the proof spine are:

1. **actual-front tail:** prove a tail/front estimate for the true disagreement process which is substantially sharper than the causal Poisson cone and retains pre-exposure common-spin history;
2. **convective survival:** prove finite-seed survival by a valid block/regeneration comparison preserving the same common-state history.

The predecessor-trail reset-height drift cannot be imported into this actual coupling without circularity.

Even a positive `alpha(T)<1` theorem would still leave arbitrary signed-profile composition and `J_{x,r}` decay. Consequently another internal Hamming-certificate block has low expected payoff.

## E18. Bounded outside consultation

No G008/F013 is issued. The active task is the bounded consultant brief

`consultants/assignment-001-disagreement-front-survival-review.md`.

The consultant must recommend exactly one of:

- `continue-front`;
- `continue-survival`;
- `abandon-common-coupling-interface`.

After that consultation the Professor chooses one sharply stated proof-spine edge or abandons global coalescence of this synchronous coupling as the disagreement interface.

## E19. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; use `16/21` as a global Foster theorem; enlarge scalar local coupling products mechanically; revive a finite common-mass mode state; replace the signed structure by unrestricted total variation; assume an unproved uniform spectral gap / positive rates conjecture; infer tail-shift agreement from separate tail triviality; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coalescence or moving-frame contraction; infer survival from finite-time Hamming expansion; or continue the random-map route by raw larger finite windows alone.
