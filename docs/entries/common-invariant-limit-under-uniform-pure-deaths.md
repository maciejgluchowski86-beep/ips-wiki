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

Here \(\mathcal P\) is the full [patch](patch.md) family of the signed dual started from \(A\), and the integrand is defined to be zero when \(\left|\mathcal P\right|=\infty\).

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

In particular, suppose that a configuration \(\xi\) has zeroes only in \(F\Subset\Lambda\). The uniform pure-death assumption gives

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

For every finite patch,

$$
0\le C(P)\le C^\varepsilon(P).
\tag{5}
$$

If \(P\) has terminal type \(\mathsf O\), then it is active throughout its lifetime and the noise comparison is exact:

$$
C(P)
=
e^{-\varepsilon\Delta(P)}C^\varepsilon(P).
\tag{6}
$$

For an end patch \(P\) based at \(i=i(P)\), write

$$
\begin{aligned}
C(z,P)
&=
a(P)+b(P)(z-p_i^\star),
\\
C^\varepsilon(z,P)
&=
a^\varepsilon(P)+b^\varepsilon(P)(z-p_i^\star).
\end{aligned}
$$

The centered end-patch comparison gives

$$
0\le a(P)\le a^\varepsilon(P),
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

Define \(W_t^{\varepsilon,\nu}\) by replacing every contribution by its less noisy counterpart. Distinct end patches are based at distinct sites, so expansion around \(\mathbf p^\star\) gives

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
\prod_{P\in\mathcal E_t\setminus\mathcal Q}a(P).
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

### The late-interaction term

For \(0\le T<t\), let

$$
L_{T,t}
=
\left\{
\text{no successful interaction occurs in }[T,t)
\right\},
\qquad
L_T=L_{T,\infty}.
$$

On \(L_{T,t}^c\), take the first successful-interaction time \(u\in[T,t)\). The backward trail of \(\mathsf{XO}\)-patches leading from its source to time zero consists of bulk patches and has total lifetime at least \(u\ge T\). Applying the exact comparison (6) along this trail, (5) to the remaining bulk patches, and (7) term by term in (8), gives

$$
0
\le
W_t^\nu\ind(L_{T,t}^c)
\le
e^{-\varepsilon T}
W_t^{\varepsilon,\nu}\ind(L_{T,t}^c).
$$

Using (9),

$$
0
\le
\mathbb E_A\left[
W_t^\nu\ind(L_{T,t}^c)
\right]
\le
e^{-\varepsilon T}.
\tag{10}
$$

### The no-late-interaction term

On \(L_{T,t}\), every \(Q\in\mathcal E_T\) has a unique extension \(Q_t\in\mathcal E_t\) with no intervening successful interaction. Let

$$
i=i(Q),
\qquad
s=s(Q),
\qquad
\Delta_u=u-s.
$$

Multiplying the end contribution of \(Q_t\) by its conditional probability of extending from \(T\) to \(t\) without a successful interaction gives the affine factor

$$
K_{T,t}(z,Q)
=
\begin{cases}
\dfrac{\psi_i(\Delta_t,z)}{\varphi_i(\Delta_T)},
&\mathsf X(Q)=\mathsf I,
\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta_t,z)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta_T)
},
&\mathsf X(Q)=\mathsf O,
\end{cases}
\tag{11}
$$

where \(S=S(Q)\). The consistency normalizer at time \(t\) cancels in (11). Conditional on \(\cG_T\), independence of the post-\(T\) patch data and averaging over \(\nu\) yield

$$
\mathbb E_A\left[
W_t^\nu\ind(L_{T,t})
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)\,
\nu\left[
\prod_{Q\in\mathcal E_T}
K_{T,t}(\eta(i(Q)),Q)
\right].
\tag{12}
$$

For a patch based at \(i\), put

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
d_i=c_i^0(\vn),
\qquad
q_i=\frac{d_i}{r_i}.
$$

The uniform death bound gives \(r_i\ge\varepsilon\), and

$$
\psi_i(\Delta,z)
=
q_i+(z-q_i)e^{-r_i\Delta}.
\tag{13}
$$

Define \(K_{T,\infty}(Q)\) by replacing \(\psi_i(\Delta_t,z)\) in (11) by \(q_i\). The result is independent of \(z\). On \(L_T\), the end patches extend to the infinite patches of the full family, and

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{Q\in\mathcal E_T}K_{T,\infty}(Q).
\tag{14}
$$

### One-patch estimates

Write

$$
\begin{aligned}
K_{T,t}(z,Q)
&=
a_{T,t}(Q)+b_{T,t}(Q)(z-p_i^\star),
\\
K_{T,t}^\varepsilon(z,Q)
&=
a_{T,t}^\varepsilon(Q)
+b_{T,t}^\varepsilon(Q)(z-p_i^\star),
\end{aligned}
$$

and set

$$
M_{T,t}^\varepsilon(Q)
=
K_{T,t}^\varepsilon(1,Q).
$$

The following estimates hold:

$$
\begin{aligned}
0
&\le
a_{T,t}(Q)
\le
a_{T,t}^\varepsilon(Q)
\le
M_{T,t}^\varepsilon(Q),
\\
0
&\le
K_{T,\infty}(Q)
\le
M_{T,t}^\varepsilon(Q),
\\
0
&\le
b_{T,t}(Q)
\le
e^{-\varepsilon(t-T)}
b_{T,t}^\varepsilon(Q),
\\
\left|
a_{T,t}(Q)-K_{T,\infty}(Q)
\right|
&\le
e^{-\varepsilon(t-T)}
M_{T,t}^\varepsilon(Q).
\end{aligned}
\tag{15}
$$

To verify them, reducing the death rate by \(\varepsilon\) replaces \(r_i\) by

$$
r_i^\varepsilon=r_i-\varepsilon
$$

and leaves the successful-interaction rates and consistency normalizers unchanged. If \(r_i^\varepsilon>0\), set \(q_i^\varepsilon=d_i/r_i^\varepsilon\). Then

$$
\psi_i^\varepsilon(\Delta,1)
=
q_i^\varepsilon
+
\left(1-q_i^\varepsilon\right)e^{-r_i^\varepsilon\Delta}
\ge
e^{-r_i^\varepsilon\Delta}.
\tag{16}
$$

If \(r_i^\varepsilon=0\), then \(d_i=0\) and \(\psi_i^\varepsilon(\Delta,1)=1\), so the same estimates follow directly.

For an \(\mathsf{IE}\)-patch, the slope ratio is exactly

$$
\frac{b_{T,t}(Q)}{b_{T,t}^\varepsilon(Q)}
=
e^{-\varepsilon\Delta_t}
\le
e^{-\varepsilon(t-T)}.
$$

Moreover,

$$
\left|
a_{T,t}(Q)-K_{T,\infty}(Q)
\right|
=
\frac{
\left|p_i^\star-q_i\right|e^{-r_i\Delta_t}
}{
\varphi_i(\Delta_T)
},
$$

which is bounded as in (15) by (16). The remaining inequalities follow from \(0\le q_i\le q_i^\varepsilon\), terminal monotonicity, and pure-death comparison.

For an \(\mathsf{OE}\)-patch with \(\beta_i(S)>0\), put

$$
p_{i,S}^\star
=
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}.
$$

Patch positivity gives

$$
p_{i,S}^\star
\le
p_i^\star,
\qquad
p_{i,S}^\star
\le
q_i
\le
q_i^\varepsilon.
$$

The numerator in (11) is

$$
\beta_i(S)
\left(
\psi_i(\Delta_t,z)-p_{i,S}^\star
\right).
$$

Since \(p_i^\star,q_i\in[p_{i,S}^\star,1]\),

$$
\left|p_i^\star-q_i\right|
\le
1-p_{i,S}^\star.
$$

On the other hand,

$$
\psi_i^\varepsilon(\Delta,1)-p_{i,S}^\star
\ge
\left(1-p_{i,S}^\star\right)
e^{-r_i^\varepsilon\Delta}.
$$

These two inequalities give the last line of (15), and the slope ratio is again \(e^{-\varepsilon\Delta_t}\). The other comparisons follow from monotonicity in \(z\), pure-death comparison, and \(q_i\le q_i^\varepsilon\). If \(\beta_i(S)=0\), the factor is independent of \(t\) and the assertions are immediate. This proves (15).

### Centered product comparison

Expanding the \(\nu\)-average in (12) around \(\mathbf p^\star\), the sum of all terms containing at least one slope is

$$
R_{T,t}^\nu
=
\sum_{\vn\ne\mathcal Q\subseteq\mathcal E_T}
\nu\left(
\chi_{\{i(Q):Q\in\mathcal Q\}}^\star
\right)
\prod_{Q\in\mathcal Q}b_{T,t}(Q)
\prod_{Q\in\mathcal E_T\setminus\mathcal Q}
a_{T,t}(Q).
$$

By (15), every term is nonnegative and contains at least one factor supplying \(e^{-\varepsilon(t-T)}\). Hence

$$
0
\le
R_{T,t}^\nu
\le
e^{-\varepsilon(t-T)}
\nu\left[
\prod_{Q\in\mathcal E_T}
K_{T,t}^\varepsilon(\eta(i(Q)),Q)
\right].
\tag{17}
$$

For the constant terms, the telescoping product inequality and (15) give, with \(N_T=|\mathcal E_T|\),

$$
\left|
\prod_{Q\in\mathcal E_T}a_{T,t}(Q)
-
\prod_{Q\in\mathcal E_T}K_{T,\infty}(Q)
\right|
\le
N_Te^{-\varepsilon(t-T)}
\prod_{Q\in\mathcal E_T}M_{T,t}^\varepsilon(Q).
\tag{18}
$$

Combining (17) and (18), multiplying by the bulk contributions, and using (5), we obtain

$$
\begin{aligned}
&
\left|
\mathbb E_A\left[
W_t^\nu\ind(L_{T,t})
\middle|\cG_T
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\middle|\cG_T
\right]
\right|
\\
&\quad\le
e^{-\varepsilon(t-T)}
\prod_{P\in\mathcal B_T}C^\varepsilon(P)
\Bigg\{
\nu\left[
\prod_{Q\in\mathcal E_T}
K_{T,t}^\varepsilon(\eta(i(Q)),Q)
\right]
\\
&\hspace{15em}
+
N_T
\prod_{Q\in\mathcal E_T}
M_{T,t}^\varepsilon(Q)
\Bigg\}.
\end{aligned}
\tag{19}
$$

The first expression in braces is the conditional no-late-interaction weight for the less noisy process started from \(\nu\); the second is the corresponding all-one weight with one marked end patch.

> **Finite-speed note.** Temporarily restrict the graphical construction to a ball of radius \(vt\) around \(A\), with \(v\) large enough that the truncation error is \(O(e^{-\varepsilon t})\). Finite range, bounded rates, and polynomial volume growth then give, on \(L_{T,t}\),
>
> $$
> N_T=N_t
> \le
> |B(A,vt)|
> \le
> C_A(1+t)^D.
> $$
>
> Both positive comparison weights have total mass at most one by (9), once with initial law \(\nu\) and once with \(\mu_{\mathbf1}\). Therefore the expectation of the right-hand side of (19), without its exponential factor, is at most \(K_A(1+t)^D\). The finite-speed error is absorbed by increasing \(K_A\).

Integrating (19) gives

$$
\left|
\mathbb E_A\left[
W_t^\nu\ind(L_{T,t})
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\right]
\right|
\le
K_A(1+t)^D e^{-\varepsilon(t-T)}.
\tag{20}
$$

### Completion for \(\mathcal M_\star\)

Local finiteness gives

$$
\bigcup_{T<\infty}L_T
=
\left\{
\left|\mathcal P\right|<\infty
\right\}.
$$

On the event that the patch family is finite but there is an interaction after \(T\), the first such interaction again has an \(\mathsf{XO}\)-trail of total lifetime at least \(T\). The exact noise comparison along this trail gives

$$
0
\le
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\ind\left(
\left|\mathcal P\right|<\infty
\right)
\ind(L_T^c)
\right]
\le
e^{-\varepsilon T}.
\tag{21}
$$

For the last inequality, dominate by the full less noisy product. Its total mass is at most one: on the event of finitely many interactions, the nonnegative finite-horizon all-one weights converge to that product, so Fatou's lemma and (9) apply.

Combining (10), (20), and (21) yields

$$
\left|
\nu(P_t\chi_A)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\le
2e^{-\varepsilon T}
+
K_A(1+t)^D e^{-\varepsilon(t-T)}.
\tag{22}
$$

Taking \(T=t/2\) proves

$$
\left|
\nu(P_t\chi_A)-\pi(\chi_A)
\right|
\le
K_A'(1+t)^D e^{-\varepsilon t/2},
\tag{23}
$$

uniformly over \(\nu\in\mathcal M_\star\).

Every local function has a finite expansion in monomials, so (23) gives the same estimate for local \(f\). Taking \(\nu=\mu_{\mathbf1}\), compactness gives a subsequential weak limit, and convergence of all monomial moments shows that every subsequential limit is the same measure \(\pi\) characterized by (2). The finite-range spin-system semigroup is Feller, hence

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
