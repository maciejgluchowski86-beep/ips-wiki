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

Latest meeting: `meetings/022-no-credible-proof-architecture-but-j-route-decision-reopened.md`, `state_narrowed: yes`.

Active work:

- Student G: `students/student-g/assignment-009.md`, one bounded asymptotic route-decision block on `(J-SPEC)`.
- Student F: idle.
- No other proof architecture is active.

## Route status

Closed/stopped mechanisms include fixed finite walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Abandoned as a load-bearing interface after Meeting 019:

- common-uniform global coalescence / zero-frequency disagreement occupation.

Recorded as exhausted after Meeting 021:

- the current centered predecessor-trail/profile implementation based on composing the present signed insertion through successive zero-boundary segments.

Outside consultation 002 returns `no-credible-route`: no presently identified direct-spatial, alternative-coupling, or alternative-transform architecture clears the continuation bar as a proof programme.

Meeting 022 does **not** reverse those stops. It authorizes only a route-decision theorem testing whether the absolute-duration `J` criterion itself is false.

## Exact trajectory-valued spatial transfer from consultation 002

Let

$$
\mathscr X=D(\mathbb R,\{0,1\}).
$$

Given a complete right-neighbour trajectory `y`, define the left-site trajectory from independent graphical marks:

- rate `1-c`: set to `1`;
- rate `a`: set to `0`;
- rate `B=b+c-a`: if `y=0`, refresh to Bernoulli `c/B`; if `y=1`, do nothing.

Because

$$
\omega=a+1-c>0,
$$

there is almost surely a last neighbour-independent reset before every finite time. This defines a bi-infinite trajectory kernel

$$
Q(y,dx).
$$

Finite zero-boundary stationary trajectory fields are exactly Markov in space with transition `Q`, started from the constant-zero boundary trajectory; their time-zero projections are the invariant laws `pi_N`.

The natural full path-space contractions are exactly unavailable. For constant input trajectories `bold0,bold1`,

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot).
$$

The singularity follows from different asymptotic occupation fractions except on `a=b(1-c)`, and from different jump frequencies on that surface. Hence the Dobrushin coefficient of `Q` is one. For

$$
\lambda_p=p\delta_{\mathbf0}+(1-p)\delta_{\mathbf1},
$$

one has exact TV and KL isometry:

$$
\|\lambda_pQ-\lambda_qQ\|_{TV}=|p-q|,
$$

and

$$
D(\lambda_pQ\|\lambda_qQ)
=D(\lambda_p\|\lambda_q).
$$

This does not refute weak ergodicity of the reachable zero-boundary orbit, but no independent rate-level mechanism for that restricted theorem is currently known. Do not launch generic `Q`-exactness, `g`-measure variation, `bar d`, Hellinger, or block-maximal-coupling searches by default.

## Canonical predecessor-trail quantity

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

Previously the programme tried to prove `J->0`. Meeting 021 stopped the available implementation for doing so.

The principal's independent target study now raises a stronger possibility: `J->0` itself may fail at strict residual points.

## Principal finite-box evidence and the new route-decision target

Durable note:

`notes/principal-target-hierarchy-and-j-norm-evidence.md`.

The principal's separate computation used singleton depth-`n` absolute-duration values `N_n` with

$$
J_n=\frac gB N_n.
$$

Define

$$
\boxed{
\rho_J(a,b,c)
:=
\limsup_{n\to\infty}J_n^{1/n}
=
\limsup_{n\to\infty}N_n^{1/n}.
}
$$

The immediate route-decision problem is

$$
\boxed{
\text{either prove }\rho_J<1\text{ throughout the residual chamber,
 or prove }\rho_J>1\text{ at one strict residual point.}
}
\tag{J-SPEC}
$$

The principal's finite-box evidence, not yet independently verified asymptotically, reports apparent growth at

$$
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
$$

with

$$
N_{10}\approx2.3975,
\qquad
\left(\frac{N_{10}}{N_7}\right)^{1/3}\approx1.153.
$$

A second strict point `(1/500,1/10,9999/10000)` has reported three-depth ratio about `1.070`.

Finite-depth growth alone is not a proof of `rho_J>1`. Student G Assignment 009 must produce an asymptotic block/minorization/Perron--Frobenius or comparable certificate, or an opposite theorem `rho_J<1` on a genuine region.

Do not continue by simply computing larger depths.

## Signed cancellation evidence is recorded but not active

The same principal study reports very strong cancellation in signed multivariate duration-resolvent pairings. At the strong-growth point, the reported depth-ten comparison is roughly

$$
N_{10}=2.3975
\qquad\text{versus}\qquad
|L_{10}(0)|=0.00325.
$$

This suggests that replacing the exact right-region factor by its absolute survival bound may destroy decisive cancellation.

Possible later targets are:

- scalar signed resolvent decay `(ML)`;
- the actual full right-region signed target `(JT)`;
- a matrix-resolvent formulation `(MR)` if the exact right-region recursion closes appropriately.

These are **not active assignments**. `(ML)` is only a proxy until the exact duration-dependent right-region class is reconstructed and linked to the ergodicity integral.

## Current decision

Only `(J-SPEC)` is active.

If G proves `rho_J>1` at one strict residual point, record the absolute-duration `J` strategy as refuted there. The exact predecessor-trail identity remains valid, but any future use must retain additional right-region/duration cancellation rather than dominate it away.

If G proves `rho_J<1` on a genuine residual region, the absolute-duration target survives there, though the exhausted proof implementation still needs replacement.

If G returns unresolved with only deeper finite-depth evidence and no asymptotic mechanism, return to consultation 002's `no-credible-route` state and keep both students idle until genuinely new input arrives.

## Unresolved target-level facts

Open:

- `(J-SPEC)`;
- one- and two-step tail-shift agreement off the product surface;
- `Gamma_M->0`;
- `J_{x,r}->0` in general;
- common-uniform extinction versus convective survival;
- weak ergodicity of the reachable trajectory kernel `Q`;
- the positive rates conjecture.

On the exact surface `a=b(1-c)`, the zero-boundary invariant law is Bernoulli product and the signed insertion obstruction vanishes.

## Anti-circularity

Do not integrate duration before the required modulus; infer asymptotic `J` growth from finite depths alone; revive closed scalar/coupling architectures; turn `Q`-exactness into a renamed tail theorem; infer ergodicity from sampled signed resolvents; or start `(ML)/(JT)/(MR)` before `(J-SPEC)` and the exact right-region recursion justify them.

## Wiki

Keep the live wiki frozen during research.
