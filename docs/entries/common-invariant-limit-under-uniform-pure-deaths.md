---
title: Common invariant limit under uniform pure deaths
status: proved here
tags:
  - spin systems
  - invariant measures
  - local functions
  - patch positivity
  - pure death
---

# Common invariant limit under uniform pure deaths

A uniform pure-death component forces a patch-positive spin system started from any measure in the [centered lower class](high-density-measure.md) \(\mathcal M_-\) to converge to the same invariant measure. On a polynomial-growth lattice, the convergence rate is explicit: up to the volume-growth prefactor, it is at least one half of the pure-death rate.

## Theorem

Let \(\Lambda\) be a [polynomial-growth lattice](polynomial-growth-lattice.md) with exponent \(D\), and let \(\cL\) be the generator of a uniformly bounded finite-range spin system with the [patch positivity property](patch-positivity-property.md). Suppose that there is \(\varepsilon>0\) such that

$$
c_i^1(\xi)\ge\varepsilon
\qquad
\text{for every }i\in\Lambda
\text{ and }\xi\in\{0,1\}^{\Lambda}.
$$

Then there is an [invariant probability measure](invariant-measure.md) \(\pi\) such that, for every local function \(f\), there is \(K_f<\infty\) for which

$$
\sup_{\nu\in\mathcal M_-}
\left|
\nu(P_tf)-\pi(f)
\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{1}
$$

Consequently \(\nu P_t\) converges weakly to \(\pi\) for every \(\nu\in\mathcal M_-\). In particular, the conclusion holds for every [high-density measure](high-density-measure.md), since

$$
\mathcal M_\star\subseteq\mathcal M_-.
$$

The limiting measure is characterized on the [monomial](monomials.md) basis by

$$
\pi(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right],
\qquad A\Subset\Lambda.
\tag{2}
$$

Here \(\mathcal P\) is the full [patch](patch.md) family of the signed dual started from \(A\), and the [full-patch contribution](patch-contribution.md) \(C(P)\) is defined uniformly for every \(P\in\mathcal P\). The integrand is defined to be zero when \(\left|\mathcal P\right|=\infty\).

The profile condition used for product initial laws is contained in this formulation. Indeed, the [product-measure characterization](high-density-measure.md#bernoulli-product-measures) of \(\mathcal M_-\) gives

$$
\mu_{\mathbf p}\in\mathcal M_-
\quad\Longleftrightarrow\quad
p_i\ge\left(2p_i^\star-1\right)\vee0
\quad\text{for every }i\in\Lambda.
$$

Convexity then gives the theorem for every mixture supported on such profiles, while \(\mathcal M_-\) also contains non-product and non-mixture initial laws.

## Finite centered perturbations

**Remark.** The same limit and rate hold under the more general assumption that, for some \(0\le K<\infty\),

$$
\nu\left(\chi_A^\star\right)
\ge
-K\chi_A^\star(\mathbf1)
\qquad
\text{for every }A\Subset\Lambda.
\tag{3}
$$

Indeed,

$$
\frac{\nu+K\mu_{\mathbf1}}{1+K}\in\mathcal M_\star,
$$

and the identity

$$
\nu
=
(1+K)\frac{\nu+K\mu_{\mathbf1}}{1+K}
-K\mu_{\mathbf1}
$$

increases the constant in (1) by at most a factor \(1+2K\). The class \(\mathcal M_-\) is the case \(K=1\).

In particular, suppose that a configuration \(\xi\) has zeroes only in \(F\Subset\Lambda\). The [empty-neighbour bound](patch-critical-density.md#empty-neighbour-bound) and the uniform pure-death assumption give

$$
p_i^\star
\le
\frac{c_i^0(\vn)}
{c_i^0(\vn)+c_i^1(\vn)}
<1.
$$

Hence (3) holds for \(\nu=\delta_\xi\) with

$$
K
=
\prod_{i\in F}
\max\left\{
1,
\frac{p_i^\star}{1-p_i^\star}
\right\}.
$$

Thus every configuration with only finitely many zeroes converges to the same measure \(\pi\) at the rate in (1), with a constant depending on the finite zero set.

## Corollary

Under the hypotheses of the theorem, if

$$
\mathbf p^\star\le\frac12\mathbf1,
$$

then every probability measure belongs to \(\mathcal M_-\). Consequently the spin system has a unique invariant measure \(\pi\), and for every local function \(f\) there is \(K_f<\infty\) such that

$$
\sup_{\xi\in\{0,1\}^{\Lambda}}
\left|P_tf(\xi)-\pi(f)\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{4}
$$

In particular, the system is uniformly exponentially [ergodic](ergodicity.md).

## Proof of the theorem

Define \(\cL^\varepsilon\) by reducing every \(1\)-to-\(0\) flip rate by \(\varepsilon\). The assumed lower bound makes this another spin-system generator, and

$$
\cL
=
\cL^\varepsilon+\varepsilon\mathcal N^0,
\qquad
\mathcal N^0f(\xi)
=
\sum_{i\in\Lambda}
\left(f(\xi^{i,0})-f(\xi)\right).
$$

By the [duality noise lemma](duality-noise-lemma.md), \(\cL\) and \(\cL^\varepsilon\) have the same signed dual and the same full [successful-interaction](successful-interaction.md) set. Write \(P_t^\varepsilon\) and \(C^\varepsilon\) for the semigroup and patch contributions associated with \(\cL^\varepsilon\). The [pure-death comparison](pure-death-comparison-under-patch-positivity.md) shows that \(\cL^\varepsilon\) has patch positivity and the same critical profile \(\mathbf p^\star\).

The same coefficientwise comparison in the unified full-patch formula gives, for every \(P\in\mathcal P\),

$$
0\le C(P)\le C^\varepsilon(P).
\tag{5}
$$

Every patch with terminal type \(\mathsf O\) is finite. It is active throughout its lifetime, and the noise comparison is exact:

$$
C(P)
=
e^{-\varepsilon\Delta(P)}C^\varepsilon(P).
\tag{6}
$$

For an end patch \(P\) based at \(i=i(P)\), write

$$
\begin{aligned}
C(z,P)&=C(p_i^\star,P)+b(P)(z-p_i^\star),\\
C^\varepsilon(z,P)&=C^\varepsilon(p_i^\star,P)+b^\varepsilon(P)(z-p_i^\star).
\end{aligned}
$$

The centered end-patch comparison gives

$$
0\le C(p_i^\star,P)\le C^\varepsilon(p_i^\star,P),
\qquad
0\le b(P)\le b^\varepsilon(P).
\tag{7}
$$

### Positive skeleton weights

Fix \(\nu\in\mathcal M_\star\), and put

$$
W_t^\nu
=
\prod_{P\in\mathcal B_t}C(P)\,
\nu\left[
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right].
$$

Define \(W_t^{\varepsilon,\nu}\) by replacing every contribution by its less noisy counterpart. The [general-law end-factor expansion](patch-representation-of-spin-systems.md#averaging-over-a-general-initial-law) gives

$$
\nu\left[
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right]
=
\sum_{\mathcal Q\subseteq\mathcal E_t}
\nu\left(
\chi_{\{i(P):P\in\mathcal Q\}}^\star
\right)
\prod_{P\in\mathcal Q}b(P)
\prod_{P\in\mathcal E_t\setminus\mathcal Q}C(p_{i(P)}^\star,P).
\tag{8}
$$

Every term is nonnegative, and (5) and (7) compare it coefficientwise with the less noisy term. Therefore

$$
0\le W_t^\nu\le W_t^{\varepsilon,\nu}.
$$

The averaged [patch representation](patch-representation-of-spin-systems.md) gives

$$
\mathbb E_A[W_t^\nu]
=
\nu(P_t\chi_A),
\qquad
\mathbb E_A[W_t^{\varepsilon,\nu}]
=
\nu(P_t^\varepsilon\chi_A)
\le1.
\tag{9}
$$

### Spatial confinement

Fix \(0\le T<t\) and \(R\Subset\Lambda\) with \(A\subseteq R\). Let

$$
E_T^R=\{\mathbf{Cone}_T\subseteq R\}
$$

and define the ordinary zero-boundary error

$$
\rho_A(T,R)=\left\|(P_T-P_T^{R,0})\chi_A\right\|_\infty.
$$

By [undoing duality under confined interactions](undoing-duality-under-confined-interactions.md), followed by integration over \(\nu\),

$$
\mathbb E_A\left[W_t^\nu\ind(E_T^R)\right]=\nu\left(P_{t-T}P_T^{R,0}\chi_A\right).
$$

Since \(W_t^\nu\ge0\), equation (9) and contraction of \(P_{t-T}\) in the supremum norm give

$$
0\le\mathbb E_A\left[W_t^\nu\ind((E_T^R)^c)\right]=\nu\left(P_{t-T}(P_T-P_T^{R,0})\chi_A\right)\le\rho_A(T,R).
\tag{10}
$$

For later use, write

$$
G_A=\prod_{P\in\mathcal P}C(P)\ind\left(|\mathcal P|<\infty\right).
$$

The same bound with initial law \(\mu_{\mathbf1}\) holds for every finite-horizon weight \(W_u^{\mu_{\mathbf1}}\), \(u\ge T\). On \(\{|\mathcal P|<\infty\}\), these weights converge to \(\prod_{P\in\mathcal P}C(P)\), while \(G_A=0\) on the complementary event. Positivity and Fatou's lemma therefore give

$$
0\le\mathbb E_A\left[G_A\ind((E_T^R)^c)\right]\le\rho_A(T,R).
\tag{11}
$$

### Late-interaction terms

Let

$$
L_{T,t}=\{\text{no successful interaction occurs in }(T,t]\},
\qquad
L_T=L_{T,\infty}.
$$

On \(L_{T,t}^c\), take the first successful-interaction time \(u\in(T,t]\). The backward trail of \(\mathsf{XO}\)-patches leading from its source to time zero consists of bulk patches and has total lifetime at least \(u\ge T\). Applying the exact comparison (6) along this trail, (5) to the remaining bulk patches, and (7) term by term in (8), then using (9), gives

$$
0\le\mathbb E_A\left[W_t^\nu\ind(E_T^R\cap L_{T,t}^c)\right]\le e^{-\varepsilon T}.
\tag{12}
$$

Local finiteness gives

$$
\bigcup_{T<\infty}L_T=\{|\mathcal P|<\infty\}.
$$

On \(\{|\mathcal P|<\infty\}\cap L_T^c\), the first interaction after \(T\) has the same kind of \(\mathsf{XO}\)-trail. Comparing along this trail and dominating by the full less noisy product gives

$$
0\le\mathbb E_A\left[G_A\ind(E_T^R\cap L_T^c)\right]\le e^{-\varepsilon T}.
\tag{13}
$$

The full less noisy product has mass at most one: on \(\{|\mathcal P|<\infty\}\), the nonnegative finite-horizon all-one weights converge to that product, so Fatou's lemma and (9) apply.

### No-late-interaction terms

Set \(\tau=t-T\). On \(L_{T,t}\), every \(Q\in\mathcal E_T\) has a unique extension through time \(t\) with no intervening successful interaction. The [empty-neighbour relaxation identity](patch-contribution.md#empty-neighbour-relaxation) shows that its end contribution, multiplied by the conditional probability of this extension, is \(C(\psi_{i(Q)}(\tau,z),Q)\). Therefore

$$
\mathbb E_A\left[W_t^\nu\ind(L_{T,t})\mid\cG_T\right]=\prod_{P\in\mathcal B_T}C(P)\,\nu\left[\prod_{Q\in\mathcal E_T}C\left(\psi_{i(Q)}(\tau,\eta(i(Q))),Q\right)\right].
\tag{14}
$$

Put

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
q_i=\frac{c_i^0(\vn)}{r_i}.
$$

The uniform death bound gives \(r_i\ge\varepsilon\), and \(\psi_i(\tau,z)\to q_i\) as \(\tau\to\infty\). On \(L_T\), every \(Q\in\mathcal E_T\) extends to an infinite full patch. Hence

$$
\mathbb E_A\left[G_A\ind(L_T)\mid\cG_T\right]=\prod_{P\in\mathcal B_T}C(P)\prod_{Q\in\mathcal E_T}C(q_{i(Q)},Q).
\tag{15}
$$

Let \(\psi_i^\varepsilon\) be the empty-neighbour relaxation for the less noisy process. The [empty-neighbour bound](patch-critical-density.md#empty-neighbour-bound) gives \(p_i^\star\le q_i\). The monotone coupling of the two empty-neighbour chains gives \(\psi_i(\tau,z)\le\psi_i^\varepsilon(\tau,z)\), while removal of the pure deaths changes \(r_i\) to \(r_i-\varepsilon\). For \(Q\in\mathcal E_T\) based at \(i=i(Q)\), equation (7) and the affine dependence on \(z\) now give

$$
\begin{aligned}
0&\le C\left(\psi_i(\tau,p_i^\star),Q\right)\le C^\varepsilon\left(\psi_i^\varepsilon(\tau,p_i^\star),Q\right),\\
0&\le\partial_z\!\left[C\left(\psi_i(\tau,z),Q\right)\right]\le e^{-\varepsilon\tau}\partial_z\!\left[C^\varepsilon\left(\psi_i^\varepsilon(\tau,z),Q\right)\right],\\
0&\le C(q_i,Q)-C\left(\psi_i(\tau,p_i^\star),Q\right)\le e^{-\varepsilon\tau}C(q_i,Q).
\end{aligned}
\tag{16}
$$

Indeed, the last line follows directly from

$$
C(q_i,Q)-C\left(\psi_i(\tau,p_i^\star),Q\right)=b(Q)(q_i-p_i^\star)e^{-r_i\tau}.
$$

Here \(r_i\ge\varepsilon\) and \(b(Q)(q_i-p_i^\star)\le C(q_i,Q)\).

Expanding the \(\nu\)-average in (14) around \(\mathbf p^\star\), every nonconstant term contains at least one slope. The first two lines of (16) therefore give

$$
0\le\nu\left[\prod_{Q\in\mathcal E_T}C\left(\psi_{i(Q)}(\tau,\eta(i(Q))),Q\right)\right]-\prod_{Q\in\mathcal E_T}C\left(\psi_{i(Q)}(\tau,p_{i(Q)}^\star),Q\right)\le e^{-\varepsilon\tau}\nu\left[\prod_{Q\in\mathcal E_T}C^\varepsilon\left(\psi_{i(Q)}^\varepsilon(\tau,\eta(i(Q))),Q\right)\right].
\tag{17}
$$

The last line of (16) and the telescoping product inequality give

$$
0\le\prod_{Q\in\mathcal E_T}C(q_{i(Q)},Q)-\prod_{Q\in\mathcal E_T}C\left(\psi_{i(Q)}(\tau,p_{i(Q)}^\star),Q\right)\le|\mathcal E_T|e^{-\varepsilon\tau}\prod_{Q\in\mathcal E_T}C(q_{i(Q)},Q).
\tag{18}
$$

On \(E_T^R\), the [interaction-cone identity](interaction-cone.md) gives \(|\mathcal E_T|=|\mathbf{Cone}_T|\le|R|\). After multiplication by the bulk contributions, the right-hand side of (17) is \(e^{-\varepsilon\tau}\) times the conditional no-late-interaction weight for the less noisy process, whose expectation is at most one by (9). The right-hand side of (18) is at most \(|R|e^{-\varepsilon\tau}\) times the conditional limiting no-late-interaction weight, which is dominated by the full less noisy product controlled after (13). Multiplying by \(\ind(E_T^R)\) and integrating gives

$$
\left|\mathbb E_A\left[W_t^\nu\ind(E_T^R\cap L_{T,t})\right]-\mathbb E_A\left[G_A\ind(E_T^R\cap L_T)\right]\right|\le(1+|R|)e^{-\varepsilon(t-T)}.
\tag{19}
$$

### Completion for \(\mathcal M_\star\)

The events \((E_T^R)^c\), \(E_T^R\cap L_{T,t}^c\), and \(E_T^R\cap L_{T,t}\) partition the finite-horizon weight. The analogous decomposition of \(G_A\) uses \(L_T^c\) and \(L_T\). Combining (10)--(13) and (19) yields

$$
\left|\nu(P_t\chi_A)-\mathbb E_A[G_A]\right|
\le
2\rho_A(T,R)+2e^{-\varepsilon T}+(1+|R|)e^{-\varepsilon(t-T)}.
\tag{20}
$$

Apply [finite propagation for zero-boundary restrictions](finite-propagation-for-zero-boundary-restrictions.md) with \(a=\varepsilon\). There is \(v<\infty\) such that, for

$$
R_T=B(A,vT),
$$

one has

$$
\rho_A(T,R_T)\le C_Ae^{-\varepsilon T},
\qquad
|R_T|\le C_A(1+T)^D.
$$

Taking \(T=t/2\) in (20), with \(R=R_T\), proves

$$
\left|\nu(P_t\chi_A)-\pi(\chi_A)\right|
\le
K_A(1+t)^D e^{-\varepsilon t/2},
\tag{21}
$$

uniformly over \(\nu\in\mathcal M_\star\).

Every local function has a finite expansion in monomials, so (21) gives the same estimate for local \(f\). Taking \(\nu=\mu_{\mathbf1}\), compactness gives a subsequential weak limit, and convergence of all monomial moments shows that every subsequential limit is the same measure \(\pi\) characterized by (2). The finite-range spin-system semigroup is Feller, hence

$$
\pi P_s
=
\lim_{t\to\infty}\mu_{\mathbf1}P_{t+s}
=
\pi,
$$

so \(\pi\) is invariant.

### Extension to \(\mathcal M_-\)

Let \(\nu\in\mathcal M_-\). By definition,

$$
\overline\nu
=
\frac{\nu+\mu_{\mathbf1}}2
\in
\mathcal M_\star.
$$

Since

$$
\nu=2\overline\nu-\mu_{\mathbf1},
$$

the triangle inequality and the uniform \(\mathcal M_\star\) estimate give

$$
\left|
\nu(P_tf)-\pi(f)
\right|
\le
2\left|
\overline\nu(P_tf)-\pi(f)
\right|
+
\left|
\mu_{\mathbf1}(P_tf)-\pi(f)
\right|.
$$

Absorbing the factor three into \(K_f\) proves (1).

## Proof of the corollary

If \(\mathbf p^\star\le\frac12\mathbf1\), then, pointwise for every configuration \(\xi\),

$$
\frac{\chi_A^\star(\xi)}
{\chi_A^\star(\mathbf1)}
=
\prod_{i\in A}
\frac{\xi(i)-p_i^\star}{1-p_i^\star}
\ge
-1.
$$

Thus every probability measure belongs to \(\mathcal M_-\), and (1) gives (4). If \(\rho\) is invariant, then for every local function \(f\),

$$
\left|\rho(f)-\pi(f)\right|
=
\left|\rho(P_tf)-\pi(f)\right|
\le
\sup_\xi\left|P_tf(\xi)-\pi(f)\right|
\underset{t\to\infty}{\longrightarrow}0.
$$

Therefore \(\rho=\pi\), proving uniqueness and uniform exponential ergodicity.
