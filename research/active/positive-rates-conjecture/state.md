# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/017-fixed-boundary-sandwich-and-random-map-stop.md`, `state_narrowed: yes`.

Active work:

- Students F and G: idle. No G008/F013 is authorized.
- One bounded outside consultation is authorized: `consultants/assignment-001-disagreement-front-survival-review.md`.

## Closed / stopped mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; G's exposed-only global Foster product; G's full nearest-neighbour scalar edge-product/coboundary Foster class; F's depth-uniform finite linear common-mass mode closure.

Stopped as a computational implementation after Meeting 017: raw finite-window/HJB certification of the common-uniform Hamming coefficient by simply enlarging `L,R,T` or changing the right-boundary controller.

Do not reopen these by enlarging finite scalar contexts, finite common-mass alphabets, or raw random-map windows.

## Global predecessor-trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The working reduction leaves

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

Showing `J_{x,r}->0` with depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits after `J` decay is proved.

## Common-mass side

The exact insertion decomposition is

$$
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

Professor-checked strict right-weighted losses remain

$$
|Br_0-c|Z<\frac23,
\qquad
\kappa_T=BZ_{\omega+1+b}<1.
$$

The exact common-mass semigroup has no depth-uniform finite linear mode closure. Assignments 010--011 instead give suffix projectivity, finite-context truncation of the first invariant insertion, and the tail-shift formulation of the zero-frequency response.

For the zero-boundary far-left damage kernel

$$
\beta_m(t)
=
\sup_{n,\eta,i}E\sum_{j\le i-m}D_j(t),
$$

F012 proves

$$
\boxed{
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
}
$$

If

$$
\alpha_0(t)=\sup_{n,\eta,i}E\sum_jD_j(t),
$$

then integrability of `alpha_0` implies tail-shift agreement, and one finite-time inequality `alpha_0(T)<1` is sufficient for an explicit exponential `Delta_M` bound. No such strict zero-boundary contraction is proved.

Verifier history: original F012 verifier `3750a53` fails due SymPy's symbolic convergence `Piecewise`; repair `5494008` fixes only that tooling assertion. Meeting 016's theorem ruling is from proof reconstruction.

## Actual common-uniform coupling

For every finite disagreement seed, every fixed site eventually becomes permanently coupled. Survival, if it occurs, is exactly convective escape to `-infinity`.

With

$$
q=1-c+a,
$$

one has

$$
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1},
$$

hence moving-frame exponential contraction for every `z>c/q`. This does not imply global extinction.

Define

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

It is submultiplicative; one `alpha(T)<1` would imply exponential finite-seed extinction.

### Assignment 007: convergent fixed-boundary approximation

For a fixed common boundary spin `e` at `R+1`, let `B_{L,R}^e(T)` be the finite fixed-boundary CTMC value and put

$$
r_{L,R}(T)=(L+1)P(\operatorname{Pois}(T)\ge R+1),
$$

$$
\ell_L(T)=E[(\operatorname{Pois}(T)-L)_+].
$$

Meeting 017 accepts

$$
\boxed{
B_{L,R}^e(T)-r_{L,R}(T)
\le\alpha(T)
\le
B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T).
}
$$

The old adversarial controlled value also satisfies

$$
0\le A_{L,R}(T)-B_{L,R}^e(T)\le r_{L,R}(T).
$$

Thus the right controller is not the obstruction and `alpha(T)` has a genuine two-sided finite approximation at every fixed time.

### Long initial expansion

At the strict hard point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

G007 constructs a protected-source event giving

$$
\boxed{
\alpha(t)>1\qquad(0<t\le47).
}
$$

The certified lower value at `T=47` exceeds `1.008204288867933`.

At that time, merely requiring each causal truncation error to be below `1%` needs `L>=67`, `R>=74`, with naive state count `2^210`. This is a scale diagnostic, not a universal state-size lower bound, but it rules out larger raw enumeration as a useful next block.

The G007 verifier's decimal output is display-only; assertions use exact rational interval enclosures and exact finite uniformization. It supports the finite arithmetic claims, not any unresolved global alternative.

## Current route decision after Meeting 017

The raw finite random-map certificate implementation stops here. G007 is unresolved on contraction versus survival, but the unresolved continuation is no longer a finite-certificate refinement. It requires one of two new structural theorems:

1. an **actual disagreement-front tail theorem** preserving the common-spin history before first exposure and replacing the causal Poisson cone by the true near-East front scale; or
2. a **convective-survival theorem** from a finite seed.

Even a future proof of `alpha(T)<1` would still leave arbitrary signed-profile composition and `J_{x,r}` decay unresolved. The expected value of another internal block devoted only to Hamming contraction has therefore dropped.

No G008 or F013 is issued. One bounded outside consultant now assesses whether the front or survival theorem has a credible structural route and whether it would materially advance `J_{x,r}`. After that report the Professor must either choose one sharply stated new proof-spine edge or abandon the common-uniform global-coalescence interface and return to the signed predecessor-trail problem with a different disagreement representation.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local correctors mechanically; revive finite common-mass mode closure; replace the signed disagreement channel by unrestricted total variation; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coupling or moving-frame contraction; infer survival from finite-time expansion or failure of an upper certificate; or continue the random-map route by raw larger windows alone.

## Wiki

Keep the live wiki frozen during research.
