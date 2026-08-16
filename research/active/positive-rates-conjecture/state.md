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

Latest meeting: `meetings/016-route-review-converges-on-finite-time-damage-contraction.md`, `state_narrowed: yes`.

Active work:

- Student G successor: `students/student-g/assignment-007.md`, decide the finite-time full-line random-map Hamming contraction `alpha(T)<1` at the strict near-East rational point, or prove a genuine convective-survival/lower obstruction.
- Student F: Assignment 012 completed in `students/student-f/012-tail-shift-agreement.md`; no new assignment. F is idle after finishing its current response, pending G007.

## Closed mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; G's exposed-only global Foster product; G's full nearest-neighbour scalar edge-product/coboundary Foster class; F's depth-uniform finite linear common-mass mode closure.

Do not reopen these by enlarging finite scalar contexts or finite common-mass alphabets.

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
\kappa_T=BZ_{\omega+1+b}<1,
\qquad r_0=\frac1{1+b}.
$$

The exact common-mass semigroup has no depth-uniform finite linear mode closure. Assignments 010--011 instead give suffix projectivity, finite-context truncation of the first invariant insertion, and the tail-shift formulation of the zero-frequency response.

Let `mu=pi_infty^0`, let `theta` drop the boundary-nearest spin, and let

$$
\mathcal T=\bigcap_m\sigma(X_j:j\ge m).
$$

Then

$$
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T},
$$

so tail-shift agreement is equivalent to `Delta_M->0`.

### Assignment 012: damage-susceptibility criterion

For finite zero-boundary chains define the far-left single-flip damage kernel

$$
\beta_m(t)
=
\sup_{n,\eta,i}E\sum_{j\le i-m}D_j(t)
$$

and the zero-boundary Hamming amplification

$$
\alpha_0(t)
=
\sup_{n,\eta,i}E\sum_jD_j(t).
$$

Meeting 016 accepts

$$
\boxed{
\Delta_M
\le
2c\int_0^\infty\beta_{M-1}(t)dt.
}
$$

Finite speed gives

$$
\beta_m(t)
\le E[(\operatorname{Pois}(t)-m+1)_+],
\qquad
\beta_m(t)\le\alpha_0(t).
$$

Hence

$$
\boxed{
\int_0^\infty\alpha_0(t)dt<\infty
\Longrightarrow
\Delta_M\to0.
}
$$

Moreover `alpha_0` is submultiplicative, so one finite-time inequality

$$
\boxed{\alpha_0(T)<1}
$$

proves tail-shift agreement with an explicit exponential bound on `Delta_M`. The finite controlled-CTMC hierarchy from G extends to a zero-boundary certificate after finitely many close-boundary geometries are included.

No `alpha_0(T)<1` certificate is currently proved.

Verifier status: F's original verifier commit `3750a53` fails because SymPy retains the symbolic geometric-series convergence condition in `Piecewise` form. It is **not** counted as passing. F's subsequent `5494008` replaces that assertion by an exact rational geometric-series check; this is a tooling repair, not a mathematical change.

## Coupling side

For the actual common-uniform full-line coupling, every finite disagreement seed becomes permanently coupled at each fixed site. Finite-seed survival, if it occurs, is purely convective escape to `-infinity`.

With

$$
q=1-c+a,
$$

one has

$$
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1},
$$

hence moving-frame exponential contraction for every `z>c/q`.

Define

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

Meeting 015 accepts submultiplicativity and the implication

$$
\boxed{
\alpha(T)<1
\Longrightarrow
P(\tau>nT)\le\alpha(T)^n|D_0|.
}
$$

The exact finite controlled-chain hierarchy gives

$$
\alpha(T)
\le
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+].
$$

G007 is the one currently authorized execution block on this diagnostic.

## Route-level decision after Meeting 016

The common-mass and coupling sides have converged on the same **finite-time random-map damage-contraction mechanism**, although the coefficients `alpha_0` and full-line `alpha` are not automatically identical.

Continue only through G007. Do not dispatch F to a duplicate HJB search and do not begin matrix-product/nonlocal-norm engineering.

Hard stop for this implementation: if G007 returns unresolved and the only proposed continuation is larger `L,R,T` computation, a more elaborate controller, or generic matrix-product engineering without a new convergence theorem, do not issue another variant. Reassess the predecessor-trail route or use a bounded outside consultation.

If G proves full-line `alpha(T)<1`, next check the finitely many close-zero-boundary cases required to obtain `alpha_0(T)<1`; then formulate a single combined block transfer before arbitrary trail iteration. If G proves convective survival or `alpha(T)>=1` for all times, close every use of eventual global coalescence of this synchronous coupling.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local correctors mechanically; revive finite common-mass mode closure; replace the signed disagreement channel by unrestricted total variation; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coupling or moving-frame contraction; infer survival because one finite upper certificate exceeds one; or treat the failed `3750a53` verifier as a valid certificate.

## Wiki

Keep the live wiki frozen during research.
