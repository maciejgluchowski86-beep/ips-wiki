---
title: Audit of routes to Bernoulli convergence for one-dimensional FA-1f
status: heuristic
tags:
  - FA-1f
  - out of equilibrium
  - convergence
  - chronology
  - coarse graining
---

# Audit of routes to Bernoulli convergence for one-dimensional FA-1f

This entry records the current proof architecture for the unresolved convergence problem for one-dimensional two-sided FA-1f. It separates terminal reductions, proved tools, viable global routes, and approaches that should no longer be treated as proof strategies.

Throughout, \(q\in(0,1)\) is the equilibrium vacancy density and \(q_0>0\) is the initial Bernoulli vacancy density.

## Terminal reductions

Two reductions should be regarded as fixed.

First, the positive centered dual already proves convergence in the range

$$
q_0<2q.
$$

Thus the unresolved range satisfies \(q_0\ge2q\), in particular \(q_0\ge q\).

Second, the stationary-measure classification reduces the remaining problem to excluding the fully occupied trap from subsequential stationary limits. If a subsequential stationary limit is

$$
\lambda\mu_q+(1-\lambda)\delta_{\mathbf1},
$$

then either of the following is sufficient to force \(\lambda=1\):

1. the sharp one-site bound
   $$
   \mathbb P_{\mu_{q_0}}(\eta_t(0)=0)\ge q
   $$
   for all large \(t\), or
2. vacancy-gap tightness
   $$
   \lim_{L\to\infty}\limsup_{t\to\infty}
   \mathbb P_{\mu_{q_0}}
   \bigl(\eta_t\equiv1\text{ on }[-L,L]\bigr)=0.
   $$

The second target is geometrically weaker and should be used by primal arguments. The first target is the natural endpoint of the signed-discrepancy route.

## Proved tools

The following statements are established and useful, but none is a global proof by itself.

### Moving-edge chronology average

The [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md) gives an exact stopped FA chronology on a nonempty edge whose output is the one-edge CBSEP heat-bath law. In the moving version the desired branch occurs after an exact \({\rm Exp}(q)\) time, and the number of shifts before branching has an exponential tail. This is a genuine averaging over update counts and order.

The [iterated splitting](iterated-moving-edge-splitting-for-fa-1f.md) and [separated reproduction](separated-vacancy-reproduction-for-fa-1f.md) lemmas amplify this into robust random-time reproduction of tagged physical vacancies, uniformly over the exterior history.

### Local discrepancy zipper identities

For the single marked discrepancy

$$
D_iF(A)=pF(A)-F(A\cup\{i\}),
$$

the center and neighboring update identities have nonnegative coefficients. The signed one-ring obstruction occurs only for updates separated from the marked zipper. See [discrepancy zipper route](discrepancy-zipper-route-for-fa-1f.md).

### Regional undoing of duality

The [confined-duality identity](undoing-duality-under-confined-interactions.md) converts a signed dual whose successful interactions are confined to a region during a time interval into an ordinary modified FA semigroup. This is the correct way to treat a fully averaged unmarked region: once it is genuinely isolated, its value is obtained from a positive Markov operator rather than from a new coefficientwise positivity claim.

### Front mobility

The all-density finite-seed theorem gives linear growth of the span of finitely many vacancies. It does not control vacancy gaps behind the extremes. See [front growth and vacancy density](front-growth-and-vacancy-density-for-fa-1f.md).

### BABP plus interface stirring

The exact identity

$$
L_{\rm FA}=\frac12L_{\rm BABP}+L_{\rm xor}
$$

separates a BABP reaction layer from a reversible domain-wall stirring layer. It is structural information, not a convergence argument: the BABP quasi-duality transform does not preserve positivity of the residual layer.

## Primary route: terminal-singleton discrepancy zipper

The primary route is now the one-site discrepancy inequality

$$
D_0(\varnothing,t)
=
p-\mathbb E_{\mu_{q_0}}[\eta_0(t)]
\ge0,
\qquad q_0\ge q.
\tag{1}
$$

Equation (1) is equivalent to the vacancy-density lower bound \(\rho_t\ge q\), which immediately excludes the trap component.

The reason to prefer this route over a general discrepancy cone is its terminal geometry. The backward exploration starts from one marked terminal discrepancy and **no unmarked terminal background**. Background sites are created only when updates meet the zipper. Consequently, if predecessor closure is chosen correctly, a component that separates from the marked path should either

1. close as a bulk component, or
2. reach time \(0\).

It should not create an arbitrary hard-range terminal end factor at time \(t\).

The proposed regional calculation is therefore:

* reveal only the zipper, the predecessors needed to make it a true spacetime separator, and the certifying absence intervals;
* apply the positive local zipper identities at every revealed interaction touching the mark;
* leave the complete order of all interactions inside each detached region hidden;
* integrate a bounded detached component as an ordinary nonnegative bulk patch contribution;
* integrate a component reaching time \(0\) by undoing its full signed chronology to a time-dependent confined FA semigroup acting on the nonnegative Bernoulli initial monomial.

The missing theorem is a **two-sided zipper factorization**: the revealed zipper/scaffold must be defined so that, conditional on it, the unrevealed Poisson marks factorize over the detached regions with precisely the boundary data required by the regional semigroup identities.

This is a genuine chronology-averaging target. It does not ask for positivity of arbitrary fixed update words, arbitrary regional coefficients, or a new global correlation cone.

### Relation to the existing barrier--scaffold construction

The earlier barrier--scaffold construction is a template for the required Poisson disintegration, but it is not directly reusable. Its barrier is built from one-sided rightward successful interactions. Two-sided FA interactions and the moving discrepancy can generate predecessor branches on both sides. The new theorem must therefore be proved for the actual zipper geometry rather than quoted from the one-sided scaffold.

This is the point at which the primary route should either succeed or be abandoned. If a detached component can touch the terminal boundary independently of the zipper, or if the conditioning necessarily reveals internal chronology in a way that prevents regional semigroup averaging, the route fails structurally.

## Secondary route: primal regeneration to a zeros lemma

The [vacancy-gap route](gap-process-route-for-fa-1f.md) remains a valid global architecture. It aims only at vacancy-gap tightness.

The local part is strong: moving-edge regeneration, iterated splitting, and separated tagged-vacancy reproduction all hold for every \(q>0\). The unresolved step is not local branching. It is deterministic-time spatial bookkeeping.

A standard block argument would need a statement of the following form. For suitable fixed spacetime blocks, a vacancy in an input block should produce vacancies in prescribed output blocks at the deterministic top time with probability close to one, using only graphical marks in a bounded enlargement. The existing reproduction lemmas instead give daughters at random stopping times. The daughters are physical vacancies and their tags are immortal, but distinct tags may later merge onto one physical vacancy. Therefore random-time reproduction is not yet a supercritical oriented-percolation comparison.

The all-density front theorem does not repair this: it controls the span of a finite-seed process, while the lack of attractiveness prevents deleting the exterior vacancies and comparing the resulting evolution with the full Bernoulli process.

This route remains viable, but it requires a new coarse process or stopping-line theorem that controls persistence and collision of descendants at deterministic observation times. It is substantially heavier than the local regeneration lemmas.

## Supporting constructions, not proof routes

### Vacancy lens

The [vacancy-lens factorization](vacancy-lens-factorization-for-fa-1f.md) correctly factors a prescribed tagged-vacancy lens after bridge-time expansion. The global tessellation obstruction is real. For a single lens around one observation site, inward-priority tagging is consistent, so the construction may still be useful inside either primary route. By itself it gives no contraction of the lens width; the weighted moving-boundary transfer operator remains uncontrolled.

### BABP comparison

The BABP relation explains the reaction geometry and motivates CBSEP-type coarse updates. There is no direct stochastic comparison, and the exact similarity transform for the additive-rate FA convention applies to BABP rather than to OR-rate FA-1f. The BABP/XOR split should therefore be used only as structural guidance unless a new positive comparison is proved.

## Routes to retire

The following should no longer be pursued as independent proof strategies.

1. **Fixed-count or deterministic-word positivity.** Relevant strengthenings are false. The sign cancellation occurs only after averaging update counts and order.
2. **Coefficientwise positivity of shuffle or punctured polynomials.** Numerical positivity without a chronology mechanism is not a proof architecture.
3. **General multi-discrepancy or negative-association cones.** Strong versions fail, and adjacent-covariance inequalities merely replace the original problem by another unproved correlation inequality.
4. **Direct attractiveness or stochastic domination.** FA-1f is not attractive in the required order; hard-core and height variants tested so far do not repair this.
5. **Microscopic contact-process domination for all \(q\).** The elementary embedded contact process is useful only in a high-vacancy regime. At small \(q\), any all-density contact-process comparison must first perform chronology averaging and is therefore part of the regeneration route, not a separate argument.
6. **Exact FA--reaction-diffusion similarity transform.** The known exact transform uses the additive facilitation convention and therefore treats BABP, not the OR-rate FA-1f model considered here.
7. **Front motion implies gap tightness.** Linear motion of extreme vacancies does not control the density behind them.
8. **Uniform finite-volume mixing of the nonempty occupied-boundary component.** This is not available uniformly in the interval length; a single vacancy must diffuse across the interval. Finite-volume mixing estimates remain useful only with their correct length dependence.

## Work order

The proof search should now be sequential rather than branching.

1. Prove or disprove the terminal-singleton two-sided zipper factorization.
2. If it holds, identify every detached regional integral with a nonnegative bulk factor or an ordinary confined FA semigroup and conclude (1).
3. If the factorization fails for a structural reason, stop the signed route and return to the primal regeneration route.
4. On the primal route, formulate a deterministic-time block kernel before doing further local constructions. The existing random-time reproduction lemmas should be used only insofar as they prove that kernel.

No additional positivity cone, front theorem, or local reproduction lemma is presently needed before these global steps are settled.
