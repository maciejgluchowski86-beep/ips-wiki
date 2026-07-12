---
title: Common invariant limit under uniform pure deaths
status: proved here
tags:
  - patch positivity
  - pure deaths
  - local functions
  - convergence
  - invariant measures
---

# Common invariant limit under uniform pure deaths

For a patch-positive spin system with a uniform pure-death component, mixtures of Bernoulli product measures above a threshold extending below the patch critical density converge to a common invariant measure. On a polynomial-growth lattice the convergence is exponential on local functions, up to a polynomial prefactor. The monomial moments of the limit are the contributions of the finite complete patch families.

**References.** None yet.

## Theorem

Let \(\Lambda\) be a [polynomial-growth lattice](polynomial-growth-lattice.md) with exponent \(D\), and let \(\cL\) be the generator of a uniformly bounded finite-range spin system with the [patch positivity property](patch-positivity-property.md). Suppose that there is \(\varepsilon>0\) such that

$$
c_i^1(\xi)\ge\varepsilon
\qquad
\text{for every }i\in\Lambda
\text{ and }\xi\in\{0,1\}^{\Lambda}.
$$

Set

$$
\mathbf p^-
=
\left(2\mathbf p^\star-\mathbf 1\right)\vee\mathbf 0.
$$

Then there is an [invariant probability measure](invariant-measure.md) \(\pi\) such that, for every local function \(f\), there is \(K_f<\infty\) for which

$$
\left|
\nu(P_tf)-\pi(f)
\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
$$

The estimate is uniform over all mixtures \(\nu\) of Bernoulli product measures whose mixing laws are supported on one-density profiles satisfying \(\mathbf p\ge\mathbf p^-\). Consequently \(\nu P_t\) converges weakly to \(\pi\) for every such mixture. In particular, every [high-density measure](high-density-measure.md) converges to \(\pi\).

The limiting measure is characterized on the monomial basis by

$$
\pi(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right],
\qquad A\Subset\Lambda.
$$

Here \(\mathcal P\) is the full [patch](patch.md) family of the signed dual started from \(A\), and the integrand is defined to be zero when \(\left|\mathcal P\right|=\infty\).

## Corollary

Under the hypotheses of the theorem, if

$$
\mathbf p^\star\le\frac12\mathbf 1,
$$

then the spin system has a unique invariant measure \(\pi\) and is uniformly exponentially [ergodic](ergodicity.md) on local functions: there is \(\gamma>0\) such that, for every local function \(f\), some \(K_f<\infty\) satisfies

$$
\sup_{\xi\in\{0,1\}^{\Lambda}}
\left|P_tf(\xi)-\pi(f)\right|
\le
K_f e^{-\gamma t}.
$$

## Proof of the theorem

Define \(\cL^\varepsilon\) by reducing every \(1\)-to-\(0\) flip rate by \(\varepsilon\). The lower bound on \(c_i^1\) makes this another spin-system generator, and

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

By the [duality noise lemma](duality-noise-lemma.md), \(\cL\) and \(\cL^\varepsilon\) have the same signed dual process and the same full [successful-interaction](successful-interaction.md) set \(\mathcal I\). Write \(P_t^\varepsilon\) and \(C^\varepsilon\) for the semigroup and patch contributions associated with \(\cL^\varepsilon\).

The patch formulas give

$$
0\le C(P)\le C^\varepsilon(P)
$$

for every finite patch. If \(P\) has terminal type \(\mathsf O\), so that its type is \(\mathsf{XO}\) with \(\mathsf X\in\{\mathsf S,\mathsf I,\mathsf O\}\), then the patch is active throughout and the comparison is exact:

$$
C(P)
=
e^{-\varepsilon\Delta(P)}C^\varepsilon(P).
\tag{1}
$$

The patch critical density is unchanged because the pure-death perturbation changes only the empty coefficient \(c_i^1(\vn)\). Since

$$
\mathbf p+\mathbf 1\ge2\mathbf p^\star,
$$

the reflected comparison from [monomial monotonicity for high-density measures](monomial-monotonicity-for-high-density-measures.md#domination-below-the-critical-density) gives, for every end patch,

$$
\left|C^{\mathbf p}(P)\right|
\le
C^{\mathbf 1}(P)
\le
C^{\varepsilon,\mathbf 1}(P).
\tag{2}
$$

Set

$$
W_t^{\mathbf p}
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P).
$$

The positive comparison weight is

$$
W_t^\varepsilon
=
\prod_{P\in\mathcal B_t}C^\varepsilon(P)
\prod_{P\in\mathcal E_t}C^{\varepsilon,\mathbf 1}(P).
$$

Its total mass satisfies

$$
\mathbb E_A\left[W_t^\varepsilon\right]
=
\mu_{\mathbf 1}\bigl(P_t^\varepsilon(\chi_A)\bigr)
\le1.
$$

The Bernoulli-averaged [patch representation](patch-representation-of-spin-systems.md) reads

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[W_t^{\mathbf p}\right].
\tag{3}
$$

For \(T<\infty\), let

$$
L_T
=
\left\{
\text{no successful interactions occur after time }T
\right\}.
$$

For \(t>T\), let

$$
L_{T,t}
=
\left\{
\text{no successful interactions occur between times }T\text{ and }t
\right\}.
$$

We first prove

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T^c)
\right]
\right|
\le
e^{-\varepsilon T}
+
K_A(1+T)^D e^{-\varepsilon(t-T)},
\qquad t>T.
\tag{4}
$$

Every successful interaction \((i,u,S)\) has a trail of \(\mathsf{XO}\)-type patches leading to its source. This is because every successful interaction ends a patch with an outgoing interaction and every patch begins with a successful interaction. Hence one can trace backward in time a sequence of \(\mathsf{OO}\) and \(\mathsf{IO}\) patches, ending with an \(\mathsf{SO}\) patch. The trail spans time up to \(u\), so

$$
\sum_{P\text{ in the trail}}\Delta(P)\ge u.
\tag{5}
$$

First consider \(L_T^c\cap L_{T,t}^c\). Choose the first successful interaction after time \(T\), let \(u\le t\) be its time, and denote its trail by \(\Gamma_u\). Every patch in \(\Gamma_u\) is a bulk patch, so (1) and (5) give

$$
\begin{aligned}
\prod_{P\in\Gamma_u}C(P)
&=
\exp\left(
-\varepsilon
\sum_{P\in\Gamma_u}\Delta(P)
\right)
\prod_{P\in\Gamma_u}C^\varepsilon(P)
\\
&\le
e^{-\varepsilon u}
\prod_{P\in\Gamma_u}C^\varepsilon(P)
\\
&\le
e^{-\varepsilon T}
\prod_{P\in\Gamma_u}C^\varepsilon(P).
\end{aligned}
$$

Apply \(C(P)\le C^\varepsilon(P)\) to the other bulk patches and (2) to the end patches. Pointwise on \(L_T^c\cap L_{T,t}^c\),

$$
\left|W_t^{\mathbf p}\right|
\le
e^{-\varepsilon T}W_t^\varepsilon.
$$

Therefore

$$
\begin{aligned}
\left|
\mathbb E_A\left[
W_t^{\mathbf p}
\ind\left(L_T^c\cap L_{T,t}^c\right)
\right]
\right|
&\le
\mathbb E_A\left[
\left|W_t^{\mathbf p}\right|
\ind\left(L_T^c\cap L_{T,t}^c\right)
\right]
\\
&\le
e^{-\varepsilon T}
\mathbb E_A\left[W_t^\varepsilon\right]
\\
&\le
e^{-\varepsilon T}.
\end{aligned}
$$

It remains to consider \(L_T^c\cap L_{T,t}\).

Although a successful interaction occurs after \(t\), there need not be an \(\mathsf{XO}\)-trail reaching time \(T\) within the horizon-\(t\) patch family. Instead, at least one end-patch site must remain active throughout the interval from \(T\) to \(t\). Indeed, without a successful interaction during that interval, a site that becomes inactive cannot be reactivated, and extinction of all end-patch sites would make every later successful interaction impossible.

For this estimate, temporarily undo the patch-internal averaging in \(W_t^{\mathbf p}\) and use the pre-averaged factors from the patch representation. Then

$$
\begin{aligned}
&\ind\left(
L_T^c\cap L_{T,t}
\right)
\\
&\qquad\le
\sum_{P\in\mathcal E_t}
\ind\left(
L_T^c\cap L_{T,t}
\cap
\left\{
X_u^P=1
\text{ for every }u\in[T,t]
\right\}
\right).
\end{aligned}
\tag{6}
$$

Condition on \(\cG_t\). This fixes the end patches and leaves their internal data independent. If the marked end patch \(P\) is active throughout \([T,t]\), then the noise identity gives

$$
\exp\left(
-\varepsilon\int_{s_-(P)}^tX_u^P\,du
\right)
\le
e^{-\varepsilon(t-T)}.
$$

Removing this noise, replacing the terminal density by \(\mathbf 1\), and then applying the bulk and end-patch comparisons gives

$$
\begin{aligned}
&\left|
\mathbb E_A\left[
W_t^{\mathbf p}
\ind\left(L_T^c\cap L_{T,t}\right)
\right]
\right|
\\
&\quad\le
\mathbb E_A\left[
\ind(L_{T,t})
\sum_{P\in\mathcal E_t}
e^{-\varepsilon(t-T)}
\prod_{Q\in\mathcal B_t}C^\varepsilon(Q)
\prod_{Q\in\mathcal E_t}C^{\varepsilon,\mathbf 1}(Q)
\right]
\\
&\quad=
e^{-\varepsilon(t-T)}
\mathbb E_A\left[
\left|\mathcal E_t\right|
W_t^\varepsilon
\ind(L_{T,t})
\right].
\end{aligned}
$$

On \(L_{T,t}\), the end-patch sites at time \(t\) are the end-patch sites at time \(T\). Finite spread of information on a polynomial-growth lattice gives the marked comparison estimate

$$
\mathbb E_A\left[
\left|\mathcal E_T\right|W_t^\varepsilon
\right]
\le
K_A(1+T)^D.
\tag{7}
$$

Consequently,

$$
\begin{aligned}
&\left|
\mathbb E_A\left[
W_t^{\mathbf p}
\ind\left(L_T^c\cap L_{T,t}\right)
\right]
\right|
\\
&\quad\le
e^{-\varepsilon(t-T)}
\mathbb E_A\left[
\left|\mathcal E_T\right|
W_t^\varepsilon
\right]
\\
&\quad\le
K_A(1+T)^D e^{-\varepsilon(t-T)}.
\end{aligned}
$$

Together with the preceding estimate for \(L_T^c\cap L_{T,t}^c\), this proves (4).

We now prove that, for each fixed \(T<\infty\),

$$
\lim_{t\to\infty}
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T)
\right]
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_T)
\right].
$$

Showing only that a possible limit does not depend on the terminal configuration \(\xi\) is easier. The following estimate gives the additional control needed to prove that the limit exists and to identify it with the full-patch formula.

Define

$$
L_\infty
=
\bigcup_{T<\infty}L_T.
$$

Local finiteness gives

$$
L_\infty
=
\left\{
\left|\mathcal I\right|<\infty
\right\}
=
\left\{
\left|\mathcal P\right|<\infty
\right\}.
\tag{8}
$$

Fix \(T<\infty\). On \(L_T\), the set \(\mathcal B_t\) is independent of \(t\) once \(t>T\). The sites carrying end patches are also independent of \(t\), because starting or ending a patch requires a successful interaction. Denote the corresponding infinite patches by \(\mathcal E_\infty\).

For \(P\in\mathcal E_\infty\), let \(P^{(t)}\in\mathcal E_t\) be its truncation and set

$$
C_t^\varepsilon(P)
=
C^{\varepsilon,\mathbf 1}(P^{(t)}),
\qquad
\Delta_t(P)
=
\left|
C^{\mathbf p}(P^{(t)})-C(P)
\right|.
$$

Let \(P\) be based at \(i\), put \(\ell=t-s_-(P)\), and write

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
d_i=\delta_i(\vn).
$$

Thus \(r_i\ge\varepsilon\). Write \(\varphi_i^\infty\) and \(\psi_i^\infty\) for the limits of \(\varphi_i(\ell)\) and \(\psi_i(\ell,p)\) as \(\ell\to\infty\). The latter is independent of \(p\). From the explicit formulas,

$$
\begin{aligned}
\psi_i(\ell,p)-\psi_i^\infty
&=
\left(
p-\frac{d_i}{r_i}
\right)e^{-r_i\ell},
\\
\varphi_i(\ell)-\varphi_i^\infty
&=
\left(
1-\frac{d_i}{\alpha_i}
\right)e^{-\alpha_i\ell}
\qquad
\text{when }\alpha_i>0.
\end{aligned}
$$

When \(\alpha_i=0\), one has \(d_i=0\) and \(\varphi_i(\ell)=1\), so the second difference vanishes. Write \(\psi_i^\varepsilon\) for the function \(\psi_i\) associated with \(\cL^\varepsilon\). After decreasing \(\varepsilon\) if necessary, the exponential remainders in these formulas are bounded by \(e^{-\varepsilon\ell}\). On the positive-weight skeletons under consideration, the limiting denominators below are positive. Since \(\ell\ge t-T\), the two common end-patch types satisfy

$$
\begin{aligned}
\Delta_t(P)
&=
\left|
\frac{\psi_i(\ell,p_i)}{\varphi_i(\ell)}
-
\frac{\psi_i^\infty}{\varphi_i^\infty}
\right|
\\
&=
\frac{
\left|
\left(
\psi_i(\ell,p_i)-\psi_i^\infty
\right)\varphi_i^\infty
+
\psi_i^\infty
\left(
\varphi_i^\infty-\varphi_i(\ell)
\right)
\right|
}{
\varphi_i(\ell)\varphi_i^\infty
}
\\
&\le
\kappa e^{-\varepsilon(t-T)}
\frac{\psi_i^\varepsilon(\ell,1)}{\varphi_i(\ell)}
\\
&=
\kappa e^{-\varepsilon(t-T)}C_t^\varepsilon(P),
\qquad
\operatorname{type}(P^{(t)})\in\{\mathsf{SE},\mathsf{IE}\}.
\end{aligned}
$$

For an \(\mathsf{OE}\) patch with initial target \(S\), put

$$
\begin{aligned}
N_i^p(\ell)
&=
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\ell,p),
\\
D_i(\ell)
&=
\delta_i(S)+\beta_i(S)\varphi_i(\ell),
\end{aligned}
$$

and denote their limits by \(N_i^\infty\) and \(D_i^\infty\). Let \(N_i^{\varepsilon,1}(\ell)\) be the same numerator with \(\psi_i(\ell,p)\) replaced by \(\psi_i^\varepsilon(\ell,1)\). The third end-patch formula gives

$$
\begin{aligned}
\Delta_t(P)
&=
\left|
\frac{N_i^{p_i}(\ell)}{D_i(\ell)}
-
\frac{N_i^\infty}{D_i^\infty}
\right|
\\
&=
\frac{
\left|
\left(
N_i^{p_i}(\ell)-N_i^\infty
\right)D_i^\infty
+
N_i^\infty
\left(
D_i^\infty-D_i(\ell)
\right)
\right|
}{
D_i(\ell)D_i^\infty
}
\\
&\le
\kappa e^{-\varepsilon(t-T)}
\frac{
N_i^{\varepsilon,1}(\ell)
}{
D_i(\ell)
}
\\
&=
\kappa e^{-\varepsilon(t-T)}C_t^\varepsilon(P).
\end{aligned}
$$

The same \(\kappa<\infty\) may be used in the three cases. Together with the positive comparison for the limiting factor, this gives

$$
0\le C(P)\le C_t^\varepsilon(P),
\qquad
\Delta_t(P)
\le
\kappa e^{-\varepsilon(t-T)}C_t^\varepsilon(P).
\tag{9}
$$

Expanding each finite contribution as its limit plus an error and applying (9) gives

$$
\left|
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P)
-
\prod_{P\in\mathcal E_\infty}C(P)
\right|
\le
\prod_{P\in\mathcal E_\infty}C_t^\varepsilon(P)
\left[
\left(
1+\kappa e^{-\varepsilon(t-T)}
\right)^{|\mathcal E_\infty|}
-1
\right].
\tag{10}
$$

We now use finite spread in the stronger factorial-moment form required by (10). Put \(N_T=|\mathcal E_T|\). For every \(k\ge1\), graphical path counting gives

$$
\mathbb E_A\left[
W_t^\varepsilon
\binom{N_T}{k}
\ind(L_T)
\right]
\le
\frac{\left(K_A(1+T)^D\right)^k}{k!}.
\tag{11}
$$

Indeed, every end-patch site is either in \(A\) or is reached by a graphical path of successful interactions before time \(T\). For \(k\) distinct sites, sum over the corresponding \(k\)-tuples of graphical paths. Uniformly bounded finite-range interaction rates give the usual finite-speed path bound, and polynomial volume growth leaves at most order \((1+T)^{Dk}\) choices. Division by \(k!\) removes the ordering of the selected sites. The positive all-one comparison weight has total mass at most one, so the same counting applies with the factor \(W_t^\varepsilon\).

Multiplying (10) by the bulk factors, using their comparison with \(C^\varepsilon\), expanding the power, and applying (11) gives the explicit sequence

$$
\begin{aligned}
&\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T)
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_T)
\right]
\right|
\\
&\quad\le
\sum_{k\ge1}
\left(
\kappa e^{-\varepsilon(t-T)}
\right)^k
\mathbb E_A\left[
W_t^\varepsilon
\binom{N_T}{k}
\ind(L_T)
\right]
\\
&\quad\le
\sum_{k\ge1}
\frac{
\left(
K_A(1+T)^D\kappa e^{-\varepsilon(t-T)}
\right)^k
}{k!}
\\
&\quad=
\exp\left(
K_A(1+T)^D\kappa e^{-\varepsilon(t-T)}
\right)-1.
\end{aligned}
\tag{12}
$$

All full-patch contributions are nonnegative. On \(L_\infty\setminus L_T\), the finite complete patch family contains a successful interaction after time \(T\), hence an \(\mathsf{XO}\)-trail of total length greater than \(T\). The same comparison used for the first part of (4) gives

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_\infty\setminus L_T)
\right]
\le
e^{-\varepsilon T}.
\tag{13}
$$

Combining (3), (4), (12), and (13) gives

$$
\begin{aligned}
&\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\\
&\qquad\le
2e^{-\varepsilon T}
+
K_A(1+T)^D e^{-\varepsilon(t-T)}
\\
&\qquad\quad+
\exp\left(
K_A(1+T)^D\kappa e^{-\varepsilon(t-T)}
\right)-1.
\end{aligned}
\tag{14}
$$

Take \(T=t/2\). For all sufficiently large \(t\), the exponent in the last line is at most one, so \(e^x-1\le2x\) shows that the right-hand side is bounded by

$$
K_A'(1+t)^D e^{-\varepsilon t/2}.
$$

Increasing \(K_A'\) handles bounded \(t\), proving the estimate for each monomial. The estimates are uniform in \(\mathbf p\ge\mathbf p^-\), so averaging over a mixing law gives the same result for mixtures.

Every local function depending on a finite set \(S\) has a finite [monomial](monomials.md) expansion

$$
f
=
\sum_{A\subseteq S}\widehat f(A)\chi_A.
$$

Summing the monomial estimates proves the asserted local-function bound once the limiting moments are identified with a probability measure. Take \(\nu=\mu_{\mathbf 1}\). Compactness of \(\{0,1\}^{\Lambda}\) gives a subsequential weak limit of \(\mu_{\mathbf 1}P_t\), while convergence of every monomial moment shows that all subsequential limits agree. Denote the resulting probability measure by \(\pi\). Local functions determine weak convergence, so the same argument and the uniform estimate give \(\nu P_t\Rightarrow\pi\) for every mixture in the theorem.

Finally, the finite-range spin-system semigroup is Feller. Hence, for every \(s\ge0\),

$$
\pi P_s
=
\lim_{t\to\infty}(\mu_{\mathbf 1}P_t)P_s
=
\lim_{t\to\infty}\mu_{\mathbf 1}P_{t+s}
=
\pi.
$$

Thus \(\pi\) is invariant. Since \(\mathbf p^-\le\mathbf p^\star\), the class covered by the theorem contains all high-density measures.

## Proof of the corollary

The assumption \(\mathbf p^\star\le\frac12\mathbf 1\) gives \(\mathbf p^-=\mathbf 0\). Every deterministic law is a product measure because

$$
\delta_\xi=\mu_{\mathbf \xi}.
$$

Thus the theorem's estimate holds uniformly over all deterministic initial configurations and hence over all initial laws. If \(\rho\) is invariant, then for every local function \(f\),

$$
\left|\rho(f)-\pi(f)\right|
=
\left|\rho(P_tf)-\pi(f)\right|
\longrightarrow0,
$$

so \(\rho=\pi\). Absorbing the polynomial factor into a slightly smaller exponential rate proves uniform exponential ergodicity on local functions.
