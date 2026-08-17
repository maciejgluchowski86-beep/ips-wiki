# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

## E0. Route status

Closed/stopped mechanisms include fixed walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Meeting 019 abandons common-uniform global coalescence / zero-frequency disagreement occupation as the load-bearing interface.

Meeting 021 records the current centered predecessor-trail/profile implementation as exhausted after recombination and finite propagation both terminate at zero-frequency spatial tail memory.

Consultation 002 proves the exact trajectory-valued spatial kernel `Q` but also

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot),
$$

so global path-space TV/KL contraction is unavailable.

Meeting 023 adds a genuinely different architecture: a finite-dimensional stationary occupation-control hierarchy on one-time marginals.

## E1. Predecessor-trail route-decision object retained

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The accepted predecessor-trail reduction gives the sufficient absolute-duration quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

For singleton depth `n`, write

$$
J_n=\frac gB N_n,
$$

and

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

Student G Assignment 009 decides the route-level alternative

$$
\boxed{
\rho_J>1\text{ at a strict residual point}
\quad\text{or}\quad
\rho_J<1\text{ on a genuine residual region.}
}
\tag{J-SPEC}
$$

Finite-depth growth alone is not decisive.

A proof `rho_J>1` refutes the **absolute-duration domination** at that point, not the exact predecessor-trail identity or ergodicity.

## E2. Exhausted signed-profile interface

The old profile implementation established strict one-segment damping, exact operator-valued transfer, suffix projectivity, fixed-suffix positive-frequency localization, and exact two-insertion formulas.

F013 proves that the unsplit two-insertion transfer retains a genuine zero temporal-frequency projection. F014 proves that fixed-suffix mixing and finite propagation leave the two-step tail-shift law

$$
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M},
$$

with

$$
\Gamma_M
\le
c^2Z\Delta_{\lceil M/2\rceil}^{(2)}+Ce^{-\gamma M}.
$$

No independent theorem controls this law. Further local profile composition is stopped.

## E3. Exhausted common-uniform occupation interface

For finite common-uniform disagreement seeds, every fixed site eventually couples permanently and possible survival is convective escape. The retained first-exposure exploration has an explicit front tail, but G008 proves that the projected state forgets post-coalescence ancestry and robust zero-frequency closure loses every strict contraction factor.

The missing all-depth return variable is itself a disagreement occupation quantity. Global common-uniform occupation is stopped as the proof interface.

## E4. Trajectory-valued spatial kernel is exact but not contractive globally

The one-sided stationary trajectory field is Markov in space on

$$
D(\mathbb R,\{0,1\})
$$

with kernel `Q` defined by the local graphical construction.

However constant-zero and constant-one inputs produce mutually singular stationary output path laws. Hence the full path-space Dobrushin coefficient is one and TV/KL may be transmitted isometrically.

Weak ergodicity of the reachable zero-boundary orbit remains open, but no independent rate-level mechanism is currently known.

## E5. New exact stationary occupation-control hierarchy

Use the complemented spin `xi=1-eta`, so `1` is the East facilitator. Let `L_N^u` be the generator on `N` sites with right-boundary control `u in {0,1}`.

Define

$$
\boxed{
\mathcal K_N
=
\left\{
 m(x,u)\ge0:
 \sum_{x,u}m(x,u)=1,
 \quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0
 \ \forall F
\right\}.
}
\tag{K}
$$

Meeting 023 proves:

1. every infinite-volume invariant law projects into `K_N`;
2. every `m in K_N` is realized by a finite chain with a randomized state-dependent boundary controller;
3. the projection of `K_{N+1}` using the old boundary spin as the new control lies in `K_N`.

For local `h`, define

$$
D_N(h)
=
\sup_{m\in\mathcal K_N}m(h)
-
\inf_{m\in\mathcal K_N}m(h).
$$

Then

$$
\boxed{D_{N+1}(h)\le D_N(h).}
$$

If

$$
D_N(h)\to0
$$

for every local `h`, the infinite IPS has a unique invariant measure.

## E6. Exact Bellman/Poisson dual

Finite LP duality gives

$$
\boxed{
U_N(h)
=
\inf_F\max_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
}
$$

$$
\boxed{
\ell_N(h)
=
\sup_F\min_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
}
$$

and

$$
\boxed{D_N(h)=U_N(h)-\ell_N(h).}
$$

Thus static screening can be proved by correctors valid simultaneously for both boundary controls at every state.

This is structurally different from trajectory-kernel contraction: it controls one-time stationary local marginals under an adversarial boundary-control relaxation.

## E7. Active static multiscale target

The principal proposes

$$
\boxed{
D_{2N}(h)
\le
(1-\rho)D_N(h)+Ce^{-\gamma N}
}
\tag{R}
$$

for fixed residual rates and all large `N`, or another scale-recursive theorem forcing `D_N(h)->0`.

Student F Assignment 015 must decide whether finite Bellman/Poisson correctors **concatenate** into such a repeatable theorem.

Larger finite LPs, smaller numerical diameters, or exact single-scale certificates without a repeatability theorem do not establish `(R)`.

## E8. Hard-East ingredient and missing robustness

In the complemented convention,

$$
0\to1\text{ at rate }a+(b-a)\xi_{i+1},
\qquad
1\to0\text{ at rate }(1-c)+c\xi_{i+1}.
$$

The principal's intended mechanism is that neighbour-independent soft resets create facilitators, after which hard-East relaxation screens a macroscopic subblock.

The KCM-book inputs checked by the Professor are:

- East Theorem 7.6: exponential convergence of local observables once a facilitator is present in the oriented future;
- East Theorem 7.8: linear finite-volume mixing time with empty or ergodic boundary.

These pure-East theorems do not directly imply `(R)` in the controlled noisy chain. The load-bearing missing statement is a robustness/censoring or Bellman concatenation theorem which survives all soft reset marks and every state-dependent boundary controller.

Conditioning on the absence of soft noise over an `O(N)` spacetime block cannot provide the fixed screening probability required by `(R)`.

## E9. Static-to-dynamic gap

Even if `(R)` proves

$$
D_N(h)\to0,
$$

this yields uniqueness of the invariant measure, not yet convergence from every initial law.

A later target would be uniform distributional screening of far-right perturbations, schematically

$$
S_N(h)
\le
C_h\left(D_{\lfloor N/2\rfloor}(h)+e^{-\gamma N}\right).
\tag{ZF}
$$

Together with the already proved local disappearance of finite disagreement seeds, `(ZF)` would imply convergence by a splice argument.

`(ZF)` is not active until the static screening mechanism is established.

## E10. Current decision tree

Two tasks are active and logically independent:

1. **G009 / `(J-SPEC)`**: determine whether the old absolute-duration predecessor-trail norm is asymptotically supercritical. If unresolved without a new asymptotic mechanism, stop that branch.
2. **F015 / stationary screening**: determine whether the controlled stationary LP correctors admit a repeatable multiscale contraction. If unresolved with only finite-box shrinkage, stop that route rather than enlarge `N`.

No third route is authorized.

If F015 succeeds on a genuine residual region, continue the static stationary-law route and only then address the dynamic upgrade.

If both tasks fail to produce a structural theorem, return to the `no-credible-route` state.

## Anti-circularity checkpoint

Do not infer asymptotic `J` growth from finite depths; infer multiscale screening from shrinking finite LP widths; invoke pure-East mixing as if it already controlled the noisy state-dependent boundary process; treat uniqueness as convergence; revive stopped predecessor-trail/common-coupling architectures; or use path-space `Q` contraction, which is exactly false globally.
