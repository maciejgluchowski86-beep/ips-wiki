# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/015-local-coalescence-convective-escape-and-random-map-test.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-012.md`, decide tail-shift agreement of the projective half-line invariant law;
- Student G successor: `students/student-g/assignment-007.md`, decide the finite-time random-map Hamming contraction `alpha(T)<1` at the strict near-East rational point, or prove a genuine survival/lower obstruction.

Operational note: the original G session failed before committing Assignment 006. The successor repeated Assignment 006 and committed `78470a1` plus verifier `43f4bb1`. Those commits landed shortly before Meeting 014 and were not seen during its composition; Meeting 015 contains the G ruling. No uncommitted predecessor mathematics is used.

## Closed mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1` contraction; crude scalar `max{c,b-a}Z<1`; G's exposed-only global Foster product; G's full nearest-neighbour scalar edge-product/coboundary Foster class; F's depth-uniform finite linear common-mass mode closure.

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

The exact common-mass semigroup has no depth-uniform finite linear mode closure.

Assignments 010--011 establish exact suffix projectivity, finite-context truncation of the first invariant insertion, explicit one-segment localization, and the exact tail-shift formulation of the zero-frequency boundary response. Let

$$
\mu=\pi_\infty^0,
\qquad
\theta(x_0,x_1,\ldots)=(x_1,x_2,\ldots),
$$

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m.
$$

Then

$$
\Delta_M
=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
$$

and

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Thus zero-frequency boundary locality is equivalent to the tail-shift theorem

$$
\boxed{
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
$$

Conditional on this theorem, the mass branch after one centered insertion already has a `J`-compatible one-next-segment truncation bound. Student F Assignment 012 is the final bounded decision block on this theorem before route-level review.

## Coupling side: Meeting 015

For the actual common-uniform coupling, every finite disagreement seed becomes permanently coupled at each fixed site. If `R_t=max D_t`, then each current rightmost disagreement coalesces permanently with hazard at least

$$
q=1-c+a.
$$

Consequently finite-seed survival is equivalent to **convective escape to `-infinity`**; no disagreement can persist in a fixed spatial window.

The exact local drift obeys

$$
\boxed{
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1}.
}
$$

Hence for every `z>c/q`,

$$
\boxed{
E\sum_i z^iD_i(t)
\le e^{-(q-c/z)t}\sum_i z^iD_i(0).
}
$$

This is exponential moving-frame/local contraction, not global extinction.

Define the finite-time single-flip Hamming amplification

$$
\alpha(t)
=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

Meeting 015 accepts

$$
\alpha(t+s)\le\alpha(t)\alpha(s).
$$

If `alpha(T)<1` for one finite `T`, then every finite seed dies out with exponential block-time tail.

G also gives the exact finite controlled-CTMC upper hierarchy

$$
\boxed{
\alpha(T)
\le
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+].
}
$$

At the hard rational point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

short-time Hamming damage is expansive:

$$
\left.\frac d{dt}E|D_t|\right|_{t=0}
=c-q=\frac{9997}{10000}>0.
$$

Thus any `alpha(T)<1` theorem must bundle genuinely nonlocal clearing after initial expansion. Assignment 007 executes this finite diagnostic; it is not a new scalar local Foster architecture.

## Route-level checkpoint

Both sides have now been reduced to concrete nonlocal decision theorems:

1. F012: tail-shift agreement of the projective half-line invariant law;
2. G007: finite-time random-map Hamming contraction versus genuine convective-survival obstruction.

Do not launch open-ended matrix-product/nonlocal norm engineering. The promised route-level expected-value review is due when F012 returns; G007 is allowed in parallel only because it executes the exact finite diagnostic already exposed by G006.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local correctors mechanically; revive finite common-mass mode closure; replace the signed disagreement channel by unrestricted total variation; import the predecessor-trail reset-height drift into the actual common-uniform disagreement process; infer extinction from fixed-site coupling or `V_z`; or infer survival merely because a finite upper certificate stays above one.

## Wiki

Keep the live wiki frozen during research.
