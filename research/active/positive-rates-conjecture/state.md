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

Latest meeting: `meetings/019-two-spin-occupation-obstruction-and-common-coupling-stop.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-013.md`, one signed two-insertion recombination test on the predecessor-trail/profile side.
- Student G successor: idle. No G009 common-coupling continuation is authorized.

## Closed / stopped mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; exposed-only global Foster product; full nearest-neighbour scalar edge-product/coboundary Foster class; depth-uniform finite linear common-mass mode closure.

Stopped: raw finite-window/HJB certification by enlarging `L,R,T` or changing the right-boundary controller.

**Abandoned as a load-bearing proof interface after Meeting 019:** common-uniform global coalescence / zero-frequency occupation. Do not continue by enlarging the retained exposure state, adding ancestry counters, proving an all-depth episode-count theorem as a default continuation, or restarting raw random-map enumeration.

Previously proved common-coupling facts remain valid auxiliary lemmas.

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

All trail durations must remain visible until the final modulus. The Meeting-009 norm-order obstruction remains binding.

## Signed insertion structure retained

For a law `mu` with rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

The second term is intrinsically a signed covariance:

$$
\boxed{
r(1-r)(\mu^1-\mu^0)(f)
=\mu[(\eta_y-r)f].
}
$$

Professor-checked common-mass damping remains

$$
|Br_0-c|Z<\frac23,
\qquad
BZ_{\omega+1+b}<1,
\qquad r_0=\frac1{1+b}.
$$

At the invariant zero-boundary law, F010 already gives the positive-frequency covariance resolvent

$$
\pi_N\left[\phi_N((1+b)-\bar L)g\right]
=q_0r_0\pi_N[Dg],
\qquad
\phi_N=\eta_N-r_0,
$$

and the explicit separated-gap bound

$$
|\pi_N(\phi_N f)|
\le
\frac{2bc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
$$

This signed structure is now the active alternative to the stopped positive-coupling disagreement bound.

## What remains from F010--F012

F010 proves exact suffix/projective intertwining and finite-context truncation of the first invariant insertion. F011 identifies the post-split mass defect with tail-shift variation. F012 proves the sufficient common-coupling bound

$$
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
$$

These results remain mathematically valid, but Meeting 019 no longer pursues the right side through global common-uniform occupation. Tail-shift agreement itself remains open.

The exact common-mass semigroup has no depth-uniform finite linear mode closure, so the signed route may not be replaced by a fixed finite generator alphabet.

## Common-uniform coupling: retained auxiliary results

For finite disagreement seeds:

- every fixed site eventually becomes permanently coupled;
- possible survival is convective escape to `-infinity`;
- moving-frame weighted disagreement contracts;
- the Hamming coefficient is submultiplicative;
- G007 proves a two-sided fixed-boundary approximation and `alpha(t)>1` for `0<t<=47` at the hard point;
- Meeting 018 proves the retained-spin first-discovery tail
  $$
  P(\sigma_m\le T)
  \le\frac{15}{4}e^{T/20}\left(\frac58\right)^m
  $$
  and an almost-sure finite discovery-speed bound.

These remain available as auxiliary finite-time statements. They are no longer the required route to `J`.

## Meeting 019: G008 occupation obstruction

G008 does not prove or refute the actual occupation estimate `(OCC)`. It proves a state-sufficiency obstruction for the retained two-spin exploration.

At the hard point the least-killing one-source comparison gives

$$
h_0=\frac{1000197}{1020203},
\qquad
h_1=\frac{1019997}{1020203}.
$$

After a genuine source coalescence to common zero, two reachable histories with the same retained `(s,t,C0)` state can have source-return laws differing by at least

$$
\boxed{\frac{b-a}{2}=\frac{99}{20000}.}
$$

Thus the retained state forgets residual right-ancestry capacity. G003 controls re-entry only during one live parent episode; G006 gives only qualitative eventual permanent coupling.

If the missing post-coalescence return capacity is robustly closed on the same projected state using only the currently proved source-lifetime information, the finite-depth Bellman envelope satisfies

$$
r_0=h_0,
\qquad
r_n=\frac{h_0}{1-(1-h_0)r_{n-1}},
$$

with

$$
\frac{1-h_0}{h_0}=\frac{20006}{1000197}<\frac1{49},
\qquad
\boxed{r_n\uparrow1.}
$$

Hence that robust zero-frequency projected closure has contraction-factor supremum one. This does not refute actual `(OCC)` or every conceivable theorem using the visible spins; it proves that a new quantitative all-depth return mechanism would be required.

The missing episode count is itself a zero-frequency observable:

$$
E N_i\le E O_i,
\qquad
E N_i\le D_i(0)+cE O_{i+1},
\qquad
O_i=\int_0^\infty D_i(t)dt.
$$

No such new mechanism was produced. Meeting 018's stopping rule is therefore met.

## Active signed recombination test

Define

$$
(\mathcal J_N\mu)(f)=\mu((B\eta_N-c)f),
\qquad
\nu_N=\mathcal J_N\pi_N.
$$

Student F Assignment 013 evolves the **full signed** measure `nu_N` for one zero-boundary trail duration and applies the next insertion without first estimating the mass and conditional-law-difference pieces separately:

$$
\kappa_{N,u}
=\mathcal J_{N-1}(\nu_N P_u^{N-1,0}).
$$

With total mass `a_N(u)=kappa_{N,u}(1)`, define the remote defect

$$
\Gamma_M
=\sup_{N\ge M+2}
\int_0^\infty w(u)
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
\left|\kappa_{N,u}(f)-a_N(u)\pi_{N-2}(f)\right|du.
$$

The active question is whether

$$
\boxed{\Gamma_M\to0}
$$

with a useful depth-uniform modulus, or whether an unavoidable zero-frequency term survives even after full signed recombination.

This is one bounded test, not an all-depth theorem and not permission for matrix-product/nonlocal-norm engineering.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local correctors mechanically; revive finite common-mass mode closure; return to global common-uniform occupation or episode counting; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coupling/front speed; infer survival from finite-time Hamming expansion; split the signed insertion into positive branches and bound them independently when Assignment 013 requires recombination; or infer arbitrary-depth control from a two-insertion calculation.

## Wiki

Keep the live wiki frozen during research.
