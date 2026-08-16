# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal.

## E0. Residual chamber

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Closed: frozen-wall route, cellwise nonnegative scaffold transfer, one-step centered `L^1` transfer, and the crude scalar condition `max{c,b-a}Z<1` on the residual chamber.

## E1. Direct coupling inputs

Every disagreement site has predictable coalescence intensity at least

$$
q=1-c+a>0.
$$

Student G's exposure resolvent controls one exposed edge exactly; repeated same-parent re-entries have a geometric tail. These are reusable inputs to the trail-generated disagreement channel.

## E2. Centered predecessor trail

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's working reduction gives a canonical predecessor trail with selected interactions all births and vertical factor

$$
e^{-\omega\tau}.
$$

The exact Poisson--Mecke factorization and no-exit complement remain to be independently audited before a closing proof.

## E3. Segmentwise right killing

The right contribution obeys

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

Define

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{a(2b+3)+(1-c)(b+2)}.
$$

Throughout `\mathcal R`, `c>b-a` and `cZ>1`, so the crude scalar absolute-value criterion is useless on the unresolved chamber.

## E4. Exact one-step obstruction

Near East,

$$
a=\varepsilon^2,\quad b=\varepsilon,\quad c=1-\varepsilon^2,
$$

the depth-two profile changes sign and the normalized absolute-value factors tend to

$$
\frac32
$$

without right killing and

$$
\frac75
$$

with right killing. Therefore pointwise positivity and one-step centered `L^1` contraction are closed.

## E5. Global right-weighted criterion

The nonempty-exit term is reduced to

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Proving `J_{x,r}->0` with depth is sufficient for the nonempty-exit term.

## E6. Exact mass/disagreement decomposition

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

This is the active signed branching identity.

## E7. Disagreement height and same-parent restarts

The accepted stack-clearing minorant gives negative drift and an exponential height factor `phi(lambda)<1` on an explicit interval. Student G proves that the number `N` of exposure re-entries of one fixed parent before its first coalescence satisfies

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1},
$$

hence

$$
E[s^N\mid\mathcal F]\le\frac{(1-h_1)s}{1-h_1s}.
$$

Near East the scalar height/restart stress factor can be chosen to tend to `16/21<1`.

**Open:** lift these scalar bounds to a rigorous global finite phase/Foster state for all parent levels. Student G Assignment 004 is in flight.

## E8. Uniform equilibrium-mass contraction

Let

$$
r_0=\frac1{1+b}
$$

be the one-site zero-boundary equilibrium density. Student F Assignment 008 proves

$$
\boxed{
|Br_0-c|Z<\frac23
}
$$

throughout the strict residual chamber.

This is a genuine all-parameter regenerative loss and is independent of the Foster premise.

## E9. Mass relaxation mode

A mass branch is not automatically at `r_0`. Its rightmost density evolves as

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u},
$$

so the mass coefficient has constant and transient pieces

$$
Br(u)-c
=(Br_0-c)+B(r-r_0)e^{-(1+b)u}.
$$

Near East the transient centered mass mode is order one while the equilibrium centered mode tends to zero. Therefore the bounded state must retain a mass-relaxation/reset-history coordinate.

## E10. Norm-order obstruction

For the exact near-East depth-two profile,

$$
\frac g{|m_\varepsilon|}
\left|\int w(u)A_{2,\varepsilon}(u)du\right|
\to\frac35<1,
$$

but the actual criterion contains

$$
\boxed{
\frac g{|m_\varepsilon|}
\int w(u)|A_{2,\varepsilon}(u)|du
\to\frac75>1.
}
$$

Hence duration integration cannot precede the block absolute-value norm. A correct proof must preserve signed duration profiles until the `L^1(w)` norm is taken.

F's exact fully-regenerated height-one signed matrix has strong local spectral contraction, including `rho->sqrt(2/5)` near East, but it is only diagnostic because its entries have already integrated duration.

## E11. Static short-word closure fails

At `(1/10,3/10,4/5)`, exact zero-boundary invariant determinants refute first- and second-order spatial Markov closure. Thus current spin or a short present-spin word is not an exact finite state.

This does not rule out finite temporal reset-history / generator-mode closure.

## E12. Current load-bearing split

Two interfaces remain.

1. **Global Foster phase (G).** Produce a rigorous finite restart/disagreement return state for arbitrary height. Its return information must be rich enough to recover the signed mass/reset mode, or explicitly state what it does not retain.
2. **Mode-resolved `L^1(w)` block operator (F).** On bounded height, retain equilibrium mass, transient mass/reset modes, disagreement phases, and unintegrated duration information until the norm. Use the uniform equilibrium loss `<2/3` as the regenerative anchor and prove a parameter-dependent block contraction, or an exact obstruction.

If both succeed, combine them to prove `J_{x,r}->0`.

## E13. Final reconstruction after `J->0`

Only after E12 closes should the group audit the exact predecessor-trail factorization and complementary no-exit term and turn the resulting convergence estimate into ergodicity.

## Anti-circularity checkpoint

Do not integrate duration before absolute value, iterate the diagnostic `K^(1)` matrix as the true kernel, use short static Markov closure, return to one-step `(T)`, or replace the disagreement channel by unrestricted total variation.
