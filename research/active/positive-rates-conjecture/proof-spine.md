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

Closed: frozen-wall route, cellwise nonnegative scaffold transfer, one-step centered `L^1` transfer, the crude scalar condition `max{c,b-a}Z<1`, and G Assignment 003's exposed-only independent-level Foster product.

## E1. Direct coupling inputs

Every disagreement site has predictable coalescence intensity at least

$$
q=1-c+a>0.
$$

Student G's exposure resolvent controls one exposed edge exactly. Repeated re-entries of one fixed parent before its first coalescence have a geometric tail. These remain reusable.

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

the depth-two profile changes sign and the normalized absolute-value factors tend to `3/2` without right killing and `7/5` with right killing. Therefore pointwise positivity and one-step centered `L^1` contraction are closed.

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

## E7. Same-parent restart bundle survives

Let `N` count exposure entries of one fixed parent disagreement before that same parent first coalesces. Student G proves

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1},
$$

hence for `1<=s<h_1^{-1}`,

$$
E[s^N\mid\mathcal F]\le\frac{(1-h_1)s}{1-h_1s}.
$$

The accepted stack-clearing minorant separately gives an exponential height factor `phi(lambda)<1` on an explicit interval.

Near East the scalar product of these two separate estimates can tend to `16/21<1`.

**Status:** both scalar estimates are valid; `16/21` is diagnostic only and is not a global Foster multiplier.

## E8. Exposed-only global product Foster lift is false

Assignment 003 assigned factor `e_x>=1` to exposed parent edges and factor one to every nonexposed unresolved level, then multiplied by `lambda^H`.

Student G Assignment 004 gives a reachable stack

$$
\sigma_i=(X_i,Y_i)=01,
\qquad 0\le i\le H-1,
$$

between coupled zero bookkeeping boundaries. For

$$
V=\lambda^H C_{\rm old},
$$

the exact tilted drift is

$$
\boxed{
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
}
$$

For `s>1`, `lambda>1`, `e_0>=1`, the interior coefficient is strictly positive and grows linearly in `H`, whereas the height boundary gain is fixed. Thus the old product cannot be superharmonic uniformly in height.

With the old near-East choices,

$$
\frac{\mathscr L_sV}{V}\to\frac{H-2}{7}.
$$

**Status:** exact refutation of the Assignment-003 global product rule. Same-parent renewal remains intact.

## E9. Exact 16-phase coupling product/coboundary reduction

Let

$$
\mathcal A=\{00,11,01,10\}
$$

be the coupled pair states and choose positive nearest-neighbour edge weights

$$
q_{\alpha\beta}>0.
$$

For

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i},
$$

the common-uniform update of the middle pair in a triple `(alpha,beta,gamma)` gives the exact exposure-tilted bulk drift

$$
G_Q(\alpha,\beta,\gamma)
=
\sum_{\beta'\ne\beta}
\Pi_{\beta,\gamma}(\beta')
\left[
 s^{\rho(\alpha,\beta,\gamma;\beta')}
 \frac{q_{\alpha\beta'}q_{\beta'\gamma}}
 {q_{\alpha\beta}q_{\beta\gamma}}
 -1
\right].
$$

There are 16 edge phases and 64 triples.

For this nearest-neighbour product class, uniform all-height control of the interior bulk is equivalent to a no-positive-cycle condition on the 16-vertex de Bruijn graph. Equivalently, there must exist a phase potential `psi` with

$$
\boxed{
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
}
$$

for every triple. Full Foster contraction additionally requires finitely many boundary inequalities for rightmost coalescence/height, trail insertion, left boundary, terminal phases, and suffix trimming.

**Status:** exact finite reduction for the nearest-neighbour product/coboundary corrector class. Existence of feasible `Q,psi,s,lambda` throughout the residual chamber is open. Student G Assignment 005 attacks it.

## E10. Uniform equilibrium-mass contraction

Let

$$
r_0=\frac1{1+b}
$$

be the one-site zero-boundary equilibrium density. Student F Assignment 008 proves

$$
\boxed{|Br_0-c|Z<\frac23}
$$

throughout the strict residual chamber.

This is a genuine all-parameter regenerative loss and is independent of the coupling Foster issue.

## E11. Mass relaxation mode

A mass branch is not automatically at `r_0`. Its rightmost density evolves as

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u},
$$

so the mass coefficient has constant and transient pieces

$$
Br(u)-c
=(Br_0-c)+B(r-r_0)e^{-(1+b)u}.
$$

Near East the transient centered mass mode is order one while the equilibrium centered mode tends to zero. Therefore the bounded signed state must retain a mass-relaxation/reset-history coordinate.

## E12. Norm-order obstruction

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

## E13. Static short-word closure fails

At `(1/10,3/10,4/5)`, exact zero-boundary invariant determinants refute first- and second-order spatial Markov closure. Thus current spin or a short present-spin word is not an exact finite signed state.

This does not rule out finite temporal reset-history / generator-mode closure.

## E14. Current load-bearing split

Two interfaces remain.

1. **16-phase coupling Foster feasibility (G).** Solve or refute the nearest-neighbour product/coboundary inequalities E9, including boundary/height transitions. A success gives a valid all-height coupling return mechanism; a positive unavoidable cycle would close this corrector class.
2. **Mode-resolved `L^1(w)` signed operator (F).** On bounded coupling height/phase, retain equilibrium mass, transient mass/reset modes, disagreement phases, and unintegrated duration information until the norm. Use the uniform equilibrium loss `<2/3` as the regenerative anchor and prove a parameter-dependent block contraction, or an exact obstruction.

G's 16 coupling phases and F's temporal mass modes solve distinct closure problems. If both interfaces succeed, combine them to prove `J_{x,r}->0`.

## E15. Final reconstruction after `J->0`

Only after E14 closes should the group audit the exact predecessor-trail factorization and complementary no-exit term and turn the resulting convergence estimate into ergodicity.

## Anti-circularity checkpoint

Do not use `16/21` as a global Foster theorem, repair a single stack without checking all phase cycles, integrate duration before absolute value, iterate the diagnostic `K^(1)` matrix as the true kernel, use short static Markov closure, return to one-step `(T)`, or replace the disagreement channel by unrestricted total variation.
