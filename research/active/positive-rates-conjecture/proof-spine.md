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

## E0. Current route status

There is presently **no active proof architecture**.

Closed/stopped mechanisms include fixed walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Meeting 019 abandons common-uniform global coalescence / zero-frequency disagreement occupation as the load-bearing interface.

Meeting 021 records the current centered predecessor-trail/profile implementation as exhausted after recombination and finite propagation both terminate at zero-frequency spatial tail memory.

Consultation 002 proves the exact trajectory-valued spatial kernel `Q` but also

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot),
$$

so global path-space TV/KL contraction is unavailable.

Meeting 024 retains the exact stationary occupation-control hierarchy but stops its current Bellman-corrector concatenation implementation.

Meeting 025 stops the authorized internal `(J-SPEC)` route-decision branch after G009 isolates a supercritical fixed-depth singular renewal limit but no fixed-rate depth-uniform theorem.

Operative architecture assessment: consultation 002's **`no-credible-route`** status, updated by F015 and G009.

## E1. Exact predecessor-trail sufficient quantity

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The accepted predecessor-trail reduction gives

$$
\boxed{
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Decay of `J_{x,r}` is sufficient after replacing the exact right-region contribution by a uniform absolute survival bound. It is not the exact final ergodicity integral.

The present centered predecessor-trail/profile implementation for proving this decay is exhausted.

## E2. Canonical singleton normalization

For singleton depth `n`, G checkpoint `2cb0696` gives an exact reverse-transfer scalar `R_n` and proves

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n,
}
$$

where `N_n` is the principal normalization. Hence

$$
\boxed{
\limsup R_n^{1/n}
=
\limsup J_n^{1/n}
=
\limsup N_n^{1/n}.
}
$$

Define

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

The route-decision problem

$$
\rho_J>1\text{ at a strict residual point}
\quad\text{versus}\quad
\rho_J<1\text{ on a genuine residual region}
$$

remains open. No active assignment attacks it.

## E3. G009 fixed-depth singular renewal theorem

Along

$$
a=\varepsilon,
\qquad b=\frac1{10},
\qquad 1-c=\frac\varepsilon{10},
\qquad 0<\varepsilon<\frac1{10},
$$

let

$$
I_n(\varepsilon)
=\int_{(0,\infty)^{n-1}}
\left(\prod_{j=1}^{n-1}w(u_j)\right)|A_n(u)|du.
$$

G009 proves for every fixed `n`

$$
\boxed{
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1},
}
$$

and therefore

$$
\boxed{
\lim_{\varepsilon\downarrow0}J_n(\varepsilon)
=
\frac{2079}{341}
\left(\frac{499}{341}\right)^{n-1}.
}
$$

The supercritical base splits into

$$
\boxed{
\frac{499}{341}
=
\frac{10}{11}+rac{189}{341}>1.
}
$$

The first term is the short East Green channel; the second is the long regenerated-mass channel.

This is a theorem in the order of limits `epsilon->0` at fixed depth. It does **not** prove `rho_J>1` at any fixed `epsilon>0`.

## E4. All-depth East Green extraction

At the hard-East endpoint, with centered variables

$$
X_i=(1+b)\eta_i-1,
$$

G defines

$$
\ell_m(X_A)=b^{|A|}{\bf1}_{\{1\in A\}}.
$$

For rightmost multiplication/extraction `E_m`, the East generator satisfies

$$
\boxed{
\ell_{m-1}E_m(-L_m^E)^{-1}
=\frac1{1+b}\ell_m.
}
$$

At `b=1/10`, this multiplier is `10/11`.

The identity is depth-free. Thus the short renewal channel is not where G009 loses uniformity.

## E5. Uniform long-reset step equals the old spatial-memory problem

At every fixed finite depth, sufficiently long gaps relax to the current invariant projection and contribute the exact asymptotic weight

$$
\mu=\frac{189}{341}.
$$

At fixed positive `epsilon`, repeating this channel through arbitrarily large depth requires a uniform theorem replacing a long-evolved signed profile by its scalar invariant mass against every future left test.

F013--F014 identify the remote error in such a replacement. After fixed-suffix and causal errors are removed, one is left with one-/two-step shifted zero-boundary invariant-law memory, in particular

$$
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M}.
$$

Therefore G009's missing uniform long reset is the same all-depth spatial reset/tail-shift problem at which Meeting 021 stopped the predecessor-profile implementation.

The order-of-limits alternative remains genuine:

$$
\text{supercritical fixed-rate infinite-memory behavior}
\quad\text{versus}\quad
\text{late-depth crossover caused by remote spatial memory}.
$$

Neither side is proved.

## E6. Factorized finite-cylinder reproduction obstruction

For an invertible suffix-compatible factorized duration operator `K_m` preserving the natural suffix subspaces, set

$$
T_mf=Y_{m+1}K_mf.
$$

G009 proves there is no nonzero finite-cylinder `phi`, block length `p>=1`, and `lambda!=0` with

$$
T_{m+p-1}\cdots T_m\phi
=\lambda\,\phi\circ\theta^p.
$$

Ordinary Laplace-resolvent filters in G009 are invertible in the relevant half-plane, so they cannot yield an exact finite-cylinder Perron--Frobenius reproduction cycle.

This does not refute `(J+)`; it rules out that finite-memory nonsingular factorized implementation.

## E7. Recurrent zero-frequency spatial-memory bottleneck

The same all-depth spatial-memory object now arises from three distinct reductions:

1. F013: the invariant spectral projection survives in the unsplit two-insertion transfer;
2. F014: short-time light-cone screening leaves the two-step shifted invariant-law defect;
3. G009: the long regenerated channel cannot be repeated uniformly without the same spatial reset theorem.

This convergence of obstructions is target-relevant negative information. Another local representation or finite-memory reformulation is not presently justified without genuinely new input.

## E8. Exhausted common-uniform occupation interface

For finite common-uniform disagreement seeds, every fixed site eventually couples permanently and possible survival is convective escape. G008 shows the retained first-exposure state forgets post-coalescence ancestry and robust zero-frequency closure loses every strict contraction factor.

The missing all-depth return variable is itself an occupation quantity. Global common-uniform occupation remains stopped as a proof interface.

## E9. Exact trajectory-valued spatial representation

The stationary field is Markov in space on whole trajectories with kernel `Q`, but

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot).
$$

Hence global path-space Dobrushin/TV and KL contraction are unavailable. Weak ergodicity of the reachable zero-boundary orbit remains open with no independent rate-level mechanism.

## E10. Exact stationary occupation-control hierarchy

Use complemented spins so `1` is the East facilitator. Let `L_N^u` be the finite generator with right-boundary action `u in {0,1}` and define

$$
\boxed{
\mathcal K_N
=\left\{
 m(x,u)\ge0:\ \sum m=1,
 \quad \sum_{x,u}m(x,u)L_N^uF(x)=0\ \forall F
\right\}.
}
$$

Meetings 023--024 establish:

- every infinite invariant law projects into `K_N`;
- every `m in K_N` is realized by a randomized state-dependent boundary controller;
- `K_{N+1}` projects into `K_N`;
- therefore, for every local `h`,
  $$
  D_N(h)=\sup_{K_N}m(h)-\inf_{K_N}m(h)
  $$
  is nonincreasing;
- `D_N(h)->0` for every local `h` would prove uniqueness of the invariant measure.

This is retained exact mathematics, not an active proof route.

## E11. Bellman scale-extension identity and weighted mismatch

Finite LP duality gives Bellman endpoints `U_N,ell_N` with `D_N=U_N-ell_N`. If `s_N^\pm` are optimal upper/lower slacks, F015 proves

$$
\boxed{
D_M=D_N
-\inf_{K_M}m(s_N^+)
-\inf_{K_M}m(s_N^-).
}
$$

Each slack is a weighted adaptive tracking error:

$$
\boxed{
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}}.
}
$$

There is a controller-uniform unweighted mismatch bound

$$
P(X_N\ne\pi(X))
\ge
\frac{\min(a,1-c)}{N+1+\min(a,1-c)},
$$

but no theorem prevents mismatch from concentrating where the Bellman weight is small.

The missing scale theorem is therefore a genuinely weighted adaptive-feedback estimate, not supplied by the hard-East fixed-boundary relaxation results.

## E12. Additive Bellman concatenation is refuted

F015 proves that for arbitrary appended-block `G`, a corrector

$$
H(x,z)=F_N(x)+G(z)
$$

cannot strictly improve the upper or lower Bellman endpoint. Any strict scale improvement requires genuinely joint cross-block dependence.

This kills the natural concatenation mechanism tested in Assignment 015. Generic searches over larger LPs or wider joint interfaces are not active.

## E13. Current programme state

Both students are idle. No G010 or F016 is authorized.

The fixed scientific target remains the positive-rates conjecture, but no presently identified proof architecture clears the expected-value continuation bar.

A future restart requires genuinely new mathematical or literature input supplying a concrete mechanism beyond:

- bare one-/two-step tail-shift or spatial reset;
- common-uniform disagreement occupation;
- global path-space contraction of `Q`;
- generic joint Bellman corrector search;
- finite-depth or singular-order-limit `J` growth without fixed-rate uniformity;
- sampled signed resolvent cancellation without an exact right-region recursion.

## E14. Static-to-dynamic gap

Even a future proof `D_N(h)->0` would establish uniqueness, not convergence from arbitrary initial laws. A separate dynamic screening theorem would still be needed before the finite-seed local-coupling result could imply ergodicity.

## Anti-circularity checkpoint

Do not interchange the fixed-depth `epsilon->0` and fixed-rate `n->infinity` limits; infer `rho_J` from finite depths; revive tail-shift as a renamed long-reset theorem; treat shrinking controlled-LP widths as a multiscale theorem; replace weighted Bellman occupation by unweighted mismatch; invoke hard-East fixed-boundary mixing as if it controlled adaptive feedback; or revive stopped predecessor-trail/common-coupling/path-space contraction implementations.
