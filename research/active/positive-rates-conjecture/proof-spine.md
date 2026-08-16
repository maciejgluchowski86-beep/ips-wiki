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

Stopped implementation: raw enlargement of finite random-map/HJB windows.

Abandoned as a load-bearing interface after Meeting 019: global common-uniform coalescence / zero-frequency disagreement occupation.

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

## E2. Exact signed insertion identity

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The conditional-law term is exactly a signed covariance:

$$
\boxed{
r(1-r)(\mu^1-\mu^0)(f)
=\mu[(\eta_y-r)f].}
$$

Meeting 019 returns to this signed form rather than treating the second term through positive disagreement occupation.

## E3. Norm-order obstruction

Near East, duration integration before absolute value gives the false apparent factor `3/5`, while the actual `J`-compatible depth-two factor tends to `7/5`. Therefore every trail duration remains visible until the final `L^1(w)` modulus.

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

## E5. Exact signed transfer is operator-valued

The one-segment duration-resolved transfer has the exact operator form from F009. Its entries contain the remaining left-block generators. No depth-uniform finite matrix can represent all modes.

## E6. Finite linear mode closure is impossible

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence the cyclic dimension is at least `N`.

**Status:** exact obstruction. Do not enlarge finite common-mass alphabets.

## E7. Suffix projectivity and first invariant insertion

Rightmost suffixes are autonomous, so semigroup evolution and centered insertion/drop intertwine with suffix marginalization. Consequently

$$
R_{N,M}\pi_N=\pi_M.
$$

The first invariant centered insertion is depth-uniformly finite-context approximable. A separated spatial gap gives explicit exponential localization.

## E8. Positive-frequency signed covariance localization at equilibrium

Write

$$
\phi_N=\eta_N-r_0,
\qquad
q_0=1-r_0.
$$

F010 proves the exact stationary identity

$$
\boxed{
\pi_N\left[\phi_N((1+b)-\bar L)g\right]
=q_0r_0\pi_N[Dg].
}
$$

Hence, for `f` separated by `M` sites from the right boundary,

$$
\boxed{
|\pi_N(\phi_N f)|
\le
\frac{2bc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
}
$$

This is a strict positive-frequency resolvent estimate for the **signed** covariance channel. It remains one of the main reasons to test recombination after abandoning the positive common-coupling interface.

## E9. The split mass branch has a zero-frequency response

After decomposing the first insertion into mass and conditional-law branches, the mass branch carries `bar pi_N` rather than `pi_{N-1}`. F010--F011 identify

$$
\bar\pi_N(f)-\pi_{N-1}(f)
$$

with a zero-frequency Green response and with the tail-shift variation of the projective half-line invariant law.

F012 proves the sufficient estimate

$$
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
$$

These theorems remain correct. Meeting 019 stops pursuing this Green response through global common-uniform occupation.

## E10. Common-uniform coupling: retained auxiliary facts

For every finite disagreement seed, every fixed site becomes permanently coupled almost surely; possible survival is convective escape to `-infinity`. The coupling has moving-frame contraction and submultiplicative Hamming amplification.

G007 gives a two-sided fixed-boundary finite approximation and proves

$$
\alpha(t)>1\qquad(0<t\le47)
$$

at the hard near-East point.

Meeting 018 gives a retained-spin first-discovery exploration with

$$
P(\sigma_m\le T)
\le\frac{15}{4}e^{T/20}\left(\frac58\right)^m
$$

and a finite almost-sure discovery-speed bound.

These remain valid auxiliary lemmas. They are not now required to prove global extinction or integrable susceptibility.

## E11. G008: retained two-spin state forgets post-coalescence ancestry

At the hard point, immediately after a genuine source coalescence to common zero, two reachable actual histories with the same retained `(s,t,C0)` projection can have future source-return probabilities differing by at least

$$
\boxed{\frac{b-a}{2}=\frac{99}{20000}.}
$$

Thus the Meeting-018 two-spin state is not Markov across distinct source episodes.

G003 controls repeated exposures only while the same parent episode remains alive. G006 gives qualitative eventual permanent coupling but no uniform zero-frequency tail for the number of distinct later source episodes.

## E12. G008 robust projected zero-frequency closure loses every strict factor

The least-killing one-source comparison has

$$
h_0=\frac{1000197}{1020203},
\qquad
h_1=\frac{1019997}{1020203}.
$$

If the hidden post-coalescence return capacity is robustly closed on the same retained state using only the currently proved source-lifetime information, the finite-depth Bellman envelope satisfies

$$
\boxed{
r_0=h_0,
\qquad
r_n=\frac{h_0}{1-(1-h_0)r_{n-1}}.
}
$$

Since

$$
\frac{1-h_0}{h_0}=\frac{20006}{1000197}<\frac1{49},
$$

one gets

$$
\boxed{r_n\uparrow1.}
$$

Qualified scope: this refutes strict contraction of that robust closed projected envelope, not actual `(OCC)` or every conceivable future theorem using the visible spins.

## E13. The missing all-depth episode count is itself zero-frequency occupation

Let `N_i` be the number of maximal disagreement episodes and

$$
O_i=\int_0^\infty D_i(t)dt.
$$

G008 gives

$$
\boxed{E N_i\le E O_i,}
\qquad
\boxed{E N_i\le D_i(0)+cE O_{i+1}.}
$$

Thus a theorem strong enough to close the missing return capacity would itself be a new global zero-frequency occupation mechanism. G008 does not produce one.

**Decision:** Meeting 018's stopping rule is met. Do not enlarge the exposure state, add ancestry counters, or issue a G009 occupation continuation. The common-uniform global-coalescence/occupation route is no longer the disagreement interface.

## E14. Active signed two-insertion recombination test

Define the centered insertion/drop

$$
(\mathcal J_N\mu)(f)=\mu((B\eta_N-c)f),
$$

and start from

$$
\nu_N=\mathcal J_N\pi_N.
$$

After one zero-boundary duration `u` on the remaining sites, apply the next insertion to the **full signed** measure:

$$
\boxed{
\kappa_{N,u}
=\mathcal J_{N-1}(\nu_N P_u^{N-1,0}).
}
$$

Let

$$
a_N(u)=\kappa_{N,u}(1).
$$

Student F Assignment 013 studies the remote defect

$$
\Gamma_M
=\sup_{N\ge M+2}
\int_0^\infty w(u)
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
\left|\kappa_{N,u}(f)-a_N(u)\pi_{N-2}(f)\right|du.
$$

The active question is

$$
\boxed{\Gamma_M\to0?}
$$

A positive result would show that the first nonstationary signed transfer localizes after recombination, without global common-coupling occupation. A negative result should identify an unavoidable zero-frequency signed term surviving recombination.

This is a one-next-segment test only. It does not authorize arbitrary-depth induction or a general matrix-product/nonlocal norm.

## E15. Route checkpoint after F013

If `Gamma_M->0` with a useful modulus, determine whether the exact recombination identity has a composable structure before attempting a third insertion. Do not infer all-depth control automatically.

If an unavoidable zero-frequency term survives recombination and is equivalent to the unresolved tail-shift response, then the current predecessor-trail implementation has lost both the positive-coupling and the first signed-recombination interfaces. Hold a route-level reassessment rather than generating another local architecture.

## E16. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; use `16/21` as a global Foster theorem; enlarge scalar local coupling products mechanically; revive finite common-mass mode closure; return to global common-uniform occupation or episode counting; assume an unproved uniform spectral gap / positive-rates conjecture; import the predecessor-trail reset-height drift into the actual common-uniform process; infer extinction from fixed-site coupling/front speed; infer survival from finite-time Hamming expansion; bound the two branches of Assignment 013 separately and then add absolute values; or infer arbitrary-depth control from a two-insertion result.
