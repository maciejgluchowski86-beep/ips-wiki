# Probabilistic representations for nonlinear PDEs

This part of the wiki studies probabilistic representations of nonlinear parabolic PDEs, with particular attention to the absolute-moment problems created by derivative weights. The basic distinction is between two statements which are easy to conflate:

> a branching construction may be an exact **signed** Duhamel identity while failing to define an \(L^1\) random variable.

For linear equations, Feynman--Kac and backward-Kolmogorov formulas provide the model. For nonlinear equations, Duhamel's formula produces products of unknown solution values, and branching turns those products into products over descendants. If the nonlinearity contains spatial derivatives, Gaussian integration by parts, Malliavin/Bismut weights, or a differential coding system transfers derivatives to the sampled motion. These derivative weights are singular on short edges. Where cancellation is allowed to occur before the first absolute value therefore becomes part of the representation itself.

The project has two acts. The first uses existing branching constructions to show that absolute integrability depends on the representation architecture, not only on the PDE. The second studies a quadratic Hessian equation and develops a hierarchy of coarsenings of its raw marked Duhamel measures. The resulting picture is now sharper than the original raw-versus-averaged fork: raw-faithful sampling is impossible for one fixed smooth datum, complete interior averaging is integrable, and an intermediate construction which retains genuine branch-time randomness is also integrable on a stronger small-data regime.

## Coding trees: exactness does not imply \(L^1\)

The broad Nguwi--Penent--Privault setting is the terminal equation

$$
\partial_tu(t,x)
+
\frac12\partial_x^2u(t,x)
+
f(J_nu(t,x))
=0,
\qquad
u(T,x)=\phi(x),
$$

where

$$
J_nu=(u,u_x,\ldots,u_{x^n}).
$$

The [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md) propagates differential codes. Repeated spatial differentiation generates arbitrarily high derivatives of the jet nonlinearity. Their [Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md) is conditional on absolute integrability of every code-rooted functional required by the recursion.

The first project-level negative theorem is the [repeated-Hessian obstruction](entries/repeated-hessian-obstruction-for-coding-trees.md). Fix an active direction \(j\), so \(\phi^{(j+1)}\not\equiv0\), and an allowed composite code \(g^*\). For a bounded measurable set \(B\), define

$$
D_m(B;g,j)
=
\int_B
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|\,dy.
$$

If

$$
\limsup_{m\to\infty}
\left(
\frac{D_m(B;g,j)}{m!}
\right)^{1/m}
=
\infty,
$$

then the \(g^*\)-rooted raw coding-tree functional has infinite absolute expectation at every positive remaining horizon. The proof isolates a repeated Hessian genealogy. Lifetime, mechanism-selection, and survival probabilities cancel their reciprocal compensators, while the ordered branch-time simplex contributes \(1/m!\). The terminal jet growth is therefore visible in the absolute expectation.

The same estimate gives a necessity theorem in the other direction. If the trees rooted at both \(f^*\) and \((\partial_{z_j}f)^*\) are integrable, then for almost every terminal point

$$
|\partial_{z_j}^r f(J_n\phi(y))|
\leq
C_yA_y^r\Gamma(r/2+1).
$$

This is the [Gevrey-\(1/2\) necessity theorem](entries/gevrey-half-necessity-for-coding-trees.md). The formal directional Taylor series must be entire with at most Gaussian growth. Under only \(C^\infty\) hypotheses this is a statement about the formal jet; identifying that series with the original directional germ requires analyticity.

The [finite directional radius theorem](entries/finite-directional-radius-obstruction.md) gives a convenient special case, while the [integrable-regime note](entries/integrable-regime-of-coding-tree.md) records that the NPP theorem is not vacuous.

## The representation-level dichotomy

The coding-tree obstruction does not by itself distinguish a difficult PDE from a difficult representation. The proved [representation-level dichotomy](entries/representation-level-dichotomy.md) does.

For

$$
\partial_tu+
\frac12u_{xx}
+
\eta\left(e^{(u_x)^4}-1\right)=0,
\qquad
u(T,x)=a\cos x,
$$

with

$$
0<a\leq
\frac{\operatorname{erfc}(1/\sqrt2)}{\sqrt3},
$$

the raw NPP functional rooted at both \(f^*\) and the identity code is non-\(L^1\) at every positive horizon. By contrast, an explicit [HLOTW marked branching](entries/marked-branching-diffusion-for-gradient-nonlinearities.md) construction has finite second moment for

$$
0<T<
\frac1{2\pi e(e-1)^2\eta^2},
$$

and its expectation is identified with a continuous viscosity solution. The comparison is deliberately representation-level: two exact branching architectures attached to the same PDE have different absolute-moment behavior.

This benchmark is Act I of the project, not its final theme. Its role is to establish that signed exactness does not determine integrability.

## Quadratic Hessian equation and finite patches

The main representation programme concerns

$$
\partial_tv
=
\frac12v_{xx}
+
\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

on

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Writing \(z=v_{xx}\) gives

$$
z(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{1}
$$

Finite Picard expansion produces rooted planar binary Duhamel trees. A **patch** is a maximal chain obtained by repeatedly following the left child. The [finite-depth patch theorem](entries/finite-depth-duhamel-patch-regrouping.md) proves that replacing every such chain by its complete iterated Duhamel integral is an exact finite reindexing. The [finite conditional-factorization theorem](entries/conditional-factorization-for-finite-pde-patches.md) gives the corresponding finite probabilistic statement when the appropriate interior marks remain unexposed.

The regrouping changes the unit at which an absolute value may be taken. A centered Hessian edge has the exact form

$$
\partial_x^2P_rf(x)
=
\frac1r
\mathbb E\left[
He_2(Z)
\bigl(f(x+\sqrt rZ)-f(x)\bigr)
\right].
$$

Mean-zero Hermite cancellation gives

$$
\|\partial_x^2P_rf\|_\infty
\lesssim
r^{-1+\alpha/2}[f]_{C^\alpha}.
$$

The [Hölder-cancellation entry](entries/holder-cancellation-for-heat-semigroup-derivatives.md) develops the corresponding higher-order and commutator estimates.

## An auxiliary deterministic theorem

The [self-consistent deterministic iteration](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md) is useful but is the weakest major result in the quadratic-Hessian chain. Under a uniform Schauder smallness condition, the semi-implicit iteration

$$
\partial_tz_{n+1}
=
\partial_x^2
\left[
\left(\frac12+\lambda z_n\right)z_{n+1}
\right]
$$

stays in a fixed ellipticity window and contracts in \(H^{-1}\). It gives a unique small uniformly parabolic solution and an implicit self-consistent diffusion representation. The theorem supplies an overlapping deterministic solution theory; it is not the main probabilistic result.

## C-prime: complete interior averaging

Let

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
$$

and define

$$
(\mathcal Df)(t)
=
\int_0^t
\partial_x^2P_{t-s}f(s)\,ds.
$$

The [parabolic Hölder bound](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md) gives

$$
\|\mathcal D(fg)\|_X
\leq
C_{\mathcal D}(\alpha,T)
\|f\|_X\|g\|_X.
$$

Put

$$
M=\|P_\cdot\phi''\|_X,
\qquad
 a=|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

For every finite planar binary tree \(	au\), integrate all continuous branch-time, Brownian, Gaussian/Hermite, and descendant variables inside the decorated skeleton and denote the deterministic profile by \(F_\tau\). Then

$$
\|F_\tau\|_X
\leq
Ma^{|\tau|}.
$$

Since the number of trees with \(n\) internal vertices is the Catalan number \(C_n\), the condition

$$
\boxed{4a<1}
\tag{2}
$$

gives

$$
\sum_\tau\|F_\tau\|_X<\infty.
$$

The resulting sum solves (1), and sampling one discrete skeleton with any full-support probability mass function gives an unbiased \(L^1\) estimator. This is [Theorem C-prime](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md).

C-prime is defined directly through the deterministic Duhamel profiles. It is not written as a conditional expectation of an unresolved infinite raw functional, because ordinary conditional expectation would already require the desired \(L^1\) property.

## Why direct raw estimates fail

Several routes were audited before the fixed-datum theorem was found. They remain useful because each identifies a different obstruction.

1. **Fixed pathwise Hölder or same-regularity Besov control.** A single centered edge has the desired expected sup-norm gain but does not preserve the same pathwise regularity.
2. **Decreasing Banach scale.** The [Banach-scale obstruction](entries/banach-scale-obstruction-for-raw-pde-patches.md) proves a sharp one-edge cost \(1/\delta\). Any stepwise first-moment proof with total regularity budget \(\Delta\) pays at least
   $$
   c^n\left(\frac n\Delta\right)^n.
   $$
   This is a barrier to that proof architecture, not by itself a fixed-datum divergence theorem.
3. **Joint centered marks.** The [joint centered-mark theorem](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md) genuinely escapes the stepwise hypothesis. Two marks give a finite joint estimate with no intermediate regularity loss. At length \(m\), however, the canonical retained-mark block has sharp uniform growth \(C^m m!\). Signed averaging of internal Gaussian bridge coordinates collapses a bare derivative chain to one higher Hermite score and restores geometric growth.

The last point suggested Gaussian-bridge coarsening as an intermediate representation. The global result below shows why the naive patchwise version is not enough.

## Fixed-datum raw-faithful obstruction

The [raw-barycenter obstruction](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) removes the generation-dependent-frequency caveat of the earlier operator-norm barriers.

Choose

$$
N_m=K^m,
\qquad
b_m=(m!)^{-1/2},
$$

and put every frequency into one smooth Hessian datum

$$
g_\varepsilon(x)
=
\varepsilon
\left[
\cos x+
\sum_{m\ge m_0}b_m\cos(N_mx)
\right].
$$

For every fixed derivative order \(k\),

$$
\sum_m b_mN_m^k<\infty,
$$

so \(g_\varepsilon\in C^\infty(\mathbb T)\). The obstruction may be realized on **right-oriented combs**. On the length-\(m\) right comb, terminal Fourier projections isolate frequency \(1\) on each side leaf and \(N_m\) on the final distinguished leaf. Restricting each Hessian duration to

$$
N_m^{-2}
\leq r_j\leq
\frac h{4m}
$$

gives one logarithmic factor per retained centered edge and

$$
\|\mu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}}.
\tag{3}
$$

The sum over the disjoint comb cylinders diverges.

The theorem applies to **raw-faithful** estimators: after the canonical raw marked state is exposed, the raw signed marked contribution must remain the conditional barycenter. Conditional Jensen then transfers (3) to every positive proposal dominating the same intrinsic signed measure. Lifetime, genealogy, and Gaussian proposal changes, arbitrary dependence among proposal variables, and auxiliary conditionally unbiased randomness cannot improve the first moment.

The amplitude \(arepsilon\) can be made small enough that the same datum lies inside the C-prime regime (2). Thus the paper has a clean representation-level contrast for the same small smooth datum:

> complete interior averaging gives an unbiased \(L^1\) representation, while every raw-faithful representation has infinite first moment.

This is not an impossibility theorem for randomness. Decorative marks can always be appended to C-prime, and antithetic or other signed couplings may change the raw conditional barycenter. The correct obstruction is raw-faithfulness.

## Coarsenings of the intrinsic signed measures

For a fixed finite skeleton \(	au\), let \(\mu_\tau\) be its intrinsic signed measure on the raw interior-mark space \(\mathcal M_\tau\). A measurable coarsening

$$
\mathcal C_\tau:
\mathcal M_\tau\to\overline{\mathcal M}_\tau
$$

produces

$$
\overline\mu_\tau
=
(\mathcal C_\tau)_\#\mu_\tau.
$$

A canonical coarsened importance sampler has first moment

$$
\sum_\tau
\|\overline\mu_\tau\|_{\mathrm{TV}}.
\tag{4}
$$

For every coarsening,

$$
|F_\tau(t,x)|
\leq
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
\leq
\|\mu_\tau\|_{\mathrm{TV}}.
$$

The constant map attains the lower bound and is exactly C-prime. It is therefore total-variation optimal skeleton by skeleton, although it need not be the only coarsening with a summable global total variation.

## Naive Gaussian-bridge coarsening fails

The failure is exact. Patches are maximal **left-child** chains. The fixed-datum obstruction can be realized on right combs, where every left child is terminal and every continuing internal child is right. Hence every maximal-left patch on the obstruction genealogy has length one.

A one-edge Gaussian bridge map has no bridge coordinate to remove: the normalized endpoint Gaussian equals the original Gaussian mark. If one retains the unnormalised endpoint displacement instead, the map is invertible once the edge duration is retained. Total variation is unchanged in either case. Therefore naive patchwise Gaussian-bridge coarsening leaves the divergent subseries (3) unchanged.

This result is part of the [time-spine coarsening theorem](entries/time-spine-coarsening-for-quadratic-hessian-patches.md). It does not contradict the local bridge identity: genuine multi-edge patches still benefit from bridge averaging. The obstruction genealogies simply never supply such a patch.

## A genuine intermediate \(L^1\) representation

The same entry proves that the coarsening hierarchy does not collapse to raw versus fully averaged.

For every non-leaf finite tree, take its **root maximal-left patch**. Retain the actual ordered branch times on that patch, but integrate out all Gaussian/Hermite and Brownian marks there and every continuous variable inside its side subtrees. The pushforward signed measure on the retained time simplex has density equal to the deterministic root-patch Duhamel integrand.

Let \(K_{\mathrm{time}}(\alpha,T)<\infty\) be the optimal geometric base for the absolute time integral of one deterministic maximal-left patch. Its finiteness follows from the derivative-cluster/commutator estimate. Put

$$
b
=
|\lambda|K_{\mathrm{time}}(\alpha,T)M,
$$

and

$$
C(a)
=
\sum_{n\ge0}C_na^n
=
\frac{1-\sqrt{1-4a}}{2a},
\qquad C(0)=1.
$$

If

$$
\boxed{
4a<1,
\qquad
bC(a)<1,
}
\tag{5}
$$

then

$$
\sum_\tau
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau\|_{\mathrm{TV}}
\leq
\frac{M}{1-bC(a)}
<\infty.
\tag{6}
$$

Thus the canonical coarsened importance sampler is unbiased and \(L^1\), while a nontrivial continuous branch-time vector remains random.

If

$$
\theta
=
\frac{K_{\mathrm{time}}(\alpha,T)}
{C_{\mathcal D}(\alpha,T)},
$$

then the additional condition in (5) is exactly

$$
\frac\theta2
\left(1-\sqrt{1-4a}\right)<1.
$$

For \(	heta\leq2\) it is automatic under \(4a<1\); for \(	heta>2\) it is equivalent to

$$
a<\frac{\theta-1}{\theta^2}.
$$

No universal numerical strengthening is asserted, because the ratio depends on the chosen valid operator constants.

## The proved hierarchy and the remaining question

The quadratic-Hessian programme now has three proved levels:

1. **Raw-faithful / identity:** non-\(L^1\) for one fixed arbitrarily small smooth datum.
2. **Time-spine coarsening:** \(L^1\) under (5), with genuine continuous branch-time randomness retained.
3. **Complete interior averaging / C-prime:** \(L^1\) under the full Catalan condition \(4a<1\).

Thus complete interior averaging is **not necessary** for \(L^1\). What the fixed-datum theorem proves is that some departure from the canonical raw conditional barycenter is necessary.

The [random-patch conjecture](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md) remains open because it is formulated on the whole C-prime regime \(4a<1\). The time-spine theorem proves it on the stronger subregime (5). The remaining problem is quantitative: can a nonconstant coarsening retaining genuine continuous interior randomness be made integrable throughout the entire C-prime interval?

## Reading map

A newcomer can read the PDE section in four layers.

### Foundations

- [Heat-reference fully nonlinear terminal PDE](entries/heat-reference-fully-nonlinear-pde.md)
- [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md)
- [Feynman--Kac formula for linear parabolic equations](entries/feynman-kac-formula-for-linear-parabolic-equations.md)
- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md)
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md)
- [Importance-sampling compensators](entries/importance-sampling-compensators.md)
- [Disjoint-event lower bounds for compensated branching estimators](entries/disjoint-event-lower-bounds-for-compensated-branching-estimators.md)
- [Uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md)
- [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md)
- [Malliavin and Bismut automatic differentiation](entries/malliavin-and-bismut-automatic-differentiation.md)
- [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md)
- [Brownian confinement and heat-kernel positivity](entries/brownian-confinement-and-heat-kernel-positivity.md)
- [Lacunary and Hadamard-gap trigonometric series](entries/lacunary-and-hadamard-gap-trigonometric-series.md)
- [Total variation, bounded variation, and derivative singularities](entries/total-variation-bounded-variation-and-derivative-singularities.md)
- [Tonelli, Markov, and Borel--Cantelli](entries/tonelli-markov-and-borel-cantelli.md)

### Parabolic regularity and function spaces

- [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md)
- [Parabolic Hölder spaces](entries/parabolic-holder-spaces.md)
- [Parabolic Hölder bound for the Hessian Duhamel operator](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md)
- [Random fields in function spaces](entries/random-fields-in-function-spaces.md)
- [Conditional expectation and fluctuations of random fields](entries/conditional-expectation-and-fluctuations-of-random-fields.md)
- [Besov spaces on the torus](entries/besov-spaces-on-the-torus.md)
- [Parabolic maximum principle and Schauder estimates](entries/parabolic-maximum-principle-and-schauder-estimates.md)
- [Interior Hölder estimates for parabolic equations](entries/interior-holder-estimates-for-parabolic-equations.md)
- [Aronson and Nash Gaussian bounds](entries/aronson-nash-gaussian-bounds.md)
- [\(H^{-1}\) energy method](entries/h-minus-one-energy-method.md)
- [Weak parabolic solutions on the torus](entries/weak-parabolic-solutions-on-the-torus.md)
- [Itô diffusions and backward Kolmogorov representation](entries/ito-diffusions-and-backward-kolmogorov-representation.md)

### Branching constructions and coding-tree results

- [Marked branching diffusion for gradient nonlinearities](entries/marked-branching-diffusion-for-gradient-nonlinearities.md)
- [Antithetic and ghost branching schemes](entries/antithetic-and-ghost-branching-schemes.md)
- [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md)
- [Nguwi--Penent--Privault coding-tree Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md)
- [Directional jet radius](entries/directional-jet-radius.md)
- [Repeated-Hessian obstruction for coding trees](entries/repeated-hessian-obstruction-for-coding-trees.md)
- [Finite directional radius obstruction](entries/finite-directional-radius-obstruction.md)
- [Gevrey-1/2 necessity for coding trees](entries/gevrey-half-necessity-for-coding-trees.md)
- [Integrable regime of the coding tree](entries/integrable-regime-of-coding-tree.md)
- [Dichotomy benchmark](entries/dichotomy-benchmark.md)
- [Representation-level dichotomy](entries/representation-level-dichotomy.md)

### Quadratic-Hessian patch route

- [Finite-depth Duhamel patch regrouping](entries/finite-depth-duhamel-patch-regrouping.md)
- [Conditional factorization for finite PDE patches](entries/conditional-factorization-for-finite-pde-patches.md)
- [Self-consistent patch iteration for the quadratic Hessian PDE](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md)
- [Skeleton-averaged \(L^1\) representation for the quadratic Hessian PDE](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md)
- [Banach-scale obstruction for raw PDE patches](entries/banach-scale-obstruction-for-raw-pde-patches.md)
- [Joint centered-mark dichotomy for raw PDE patches](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md)
- [Raw-barycenter \(L^1\) obstruction for the quadratic Hessian PDE](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md)
- [Time-spine coarsening for quadratic Hessian patches](entries/time-spine-coarsening-for-quadratic-hessian-patches.md)
- [\(L^1\) random-patch conjecture for the quadratic Hessian PDE](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md)

The [reference list](meta/references.md) collects the literature cited throughout these pages.
