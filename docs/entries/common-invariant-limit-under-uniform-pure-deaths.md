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

A uniform pure-death component forces patch-positive spin systems started from a common high-density class to converge to the same invariant measure. The convergence rate on a polynomial-growth lattice is explicit: up to the volume-growth prefactor, it is at least one half of the pure-death rate.

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
\left(2\mathbf p^\star-\mathbf 1\right)\vee\mathbf 0,
$$

where \(\mathbf p^\star\) is the [patch critical density](patch-critical-density.md). Then there is an [invariant probability measure](invariant-measure.md) \(\pi\) such that, for every local function \(f\), there is \(K_f<\infty\) for which

$$
\left|
\nu(P_tf)-\pi(f)
\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{1}
$$

The estimate is uniform over all mixtures

$$
\nu=\int\mu_{\mathbf p}\,\Pi(d\mathbf p)
$$

whose mixing laws are supported on one-density profiles satisfying \(\mathbf p\ge\mathbf p^-\). Consequently \(\nu P_t\) converges weakly to \(\pi\) for every such mixture. In particular, every [high-density measure](high-density-measure.md) converges to \(\pi\).

The limiting measure is characterized on the monomial basis by

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

## Corollary

Under the hypotheses of the theorem, if

$$
\mathbf p^\star\le\frac12\mathbf 1,
$$

then the spin system has a unique invariant measure \(\pi\), and for every local function \(f\) there is \(K_f<\infty\) such that

$$
\sup_{\xi\in\{0,1\}^{\Lambda}}
\left|P_tf(\xi)-\pi(f)\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{3}
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

By the [duality noise lemma](duality-noise-lemma.md), \(\cL\) and \(\cL^\varepsilon\) have the same signed dual and the same full [successful-interaction](successful-interaction.md) set. Write \(P_t^\varepsilon\) and \(C^\varepsilon\) for the semigroup and patch contributions associated with \(\cL^\varepsilon\).

For every finite patch,

$$
0\le C(P)\le C^\varepsilon(P).
\tag{4}
$$

If \(P\) has terminal type \(\mathsf O\), then it is active throughout its lifetime and the noise comparison is exact:

$$
C(P)
=
e^{-\varepsilon\Delta(P)}C^\varepsilon(P).
\tag{5}
$$

Moreover, \(\mathbf p+\mathbf 1\ge2\mathbf p^\star\) for every \(\mathbf p\ge\mathbf p^-\). The reflected comparison from [monomial monotonicity for high-density measures](monomial-monotonicity-for-high-density-measures.md#domination-below-the-critical-density) therefore gives, for every end patch,

$$
\left|C(\mathbf p,P)\right|
\le
C(\mathbf 1,P)
\le
C^\varepsilon(\mathbf 1,P).
\tag{6}
$$

Put

$$
W_t^{\mathbf p}
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\mathbf p,P)
$$

and

$$
W_t^\varepsilon
=
\prod_{P\in\mathcal B_t}C^\varepsilon(P)
\prod_{P\in\mathcal E_t}C^\varepsilon(\mathbf 1,P).
$$

The Bernoulli-averaged [patch representation](patch-representation-of-spin-systems.md) gives

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[W_t^{\mathbf p}\right],
\qquad
\mathbb E_A\left[W_t^\varepsilon\right]
=
\mu_{\mathbf 1}\bigl(P_t^\varepsilon(\chi_A)\bigr)
\le1.
\tag{7}
$$

### The late-interaction term

For \(0\le T<t\), let

$$
L_{T,t}
=
\left\{
\text{no successful interaction occurs in }[T,t)
\right\},
$$

and let

$$
L_T=L_{T,\infty}.
$$

On \(L_{T,t}^c\), choose the first successful interaction after time \(T\). Tracing its source backward gives a trail of \(\mathsf{XO}\)-patches contained in \(\mathcal B_t\), and the sum of the patch lengths along the trail is at least \(T\). Applying (5) on the trail, (4) on the remaining bulk patches, and (6) on the end patches yields

$$
\left|W_t^{\mathbf p}\right|
\ind(L_{T,t}^c)
\le
e^{-\varepsilon T}W_t^\varepsilon.
$$

Consequently,

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t}^c)
\right]
\right|
\le
e^{-\varepsilon T}.
\tag{8}
$$

### Conditioning at time \(T\)

It remains to treat the contribution on \(L_{T,t}\). On this event,

$$
\mathcal B_t=\mathcal B_T,
$$

and every end patch at time \(T\) has a unique extension to an end patch at time \(t\) without an intervening successful interaction.

Fix \(Q\in\mathcal E_T\). Write

$$
i=i(Q),
\qquad
s=s(Q),
\qquad
\ell_u=u-s,
$$

and, when \(\mathsf X(Q)=\mathsf O\), write \(S=S(Q)\). Define the consistency normalizer

$$
D_Q(\ell)
=
\begin{cases}
\varphi_i(\ell),
&\mathsf X(Q)=\mathsf I,
\\[0.4em]
\delta_i(S)+\beta_i(S)\varphi_i(\ell),
&\mathsf X(Q)=\mathsf O,
\end{cases}
$$

and the weighted numerator

$$
N_Q^{\mathbf p}(\ell)
=
\begin{cases}
\psi_i(\ell,p_i),
&\mathsf X(Q)=\mathsf I,
\\[0.4em]
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\ell,p_i),
&\mathsf X(Q)=\mathsf O.
\end{cases}
$$

These are the quantities in the [patch-contribution formulas](patch-contribution.md). If \(Q_u\) is the extension of \(Q\) to time \(u\), then

$$
C(\mathbf p,Q_u)
=
\frac{N_Q^{\mathbf p}(\ell_u)}{D_Q(\ell_u)}.
\tag{9}
$$

Conditionally on consistency through time \(T\), the probability that this patch extends without a successful interaction through time \(u\) is

$$
\frac{D_Q(\ell_u)}{D_Q(\ell_T)}.
$$

Thus the local factor appearing after multiplication by \(\ind(L_{T,u})\) is

$$
K_{T,u}^{\mathbf p}(Q)
:=
\frac{D_Q(\ell_u)}{D_Q(\ell_T)}
C(\mathbf p,Q_u)
=
\frac{N_Q^{\mathbf p}(\ell_u)}{D_Q(\ell_T)}.
\tag{10}
$$

The potentially slow normalizer \(D_Q(\ell_u)\) has canceled. Conditional patch factorization at time \(T\) now gives

$$
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t})
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{Q\in\mathcal E_T}K_{T,t}^{\mathbf p}(Q).
\tag{11}
$$

### Uniform relaxation of the killed factors

Set

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
d_i=c_i^0(\vn).
$$

Then \(r_i\ge\varepsilon\), and the explicit formula for \(\psi_i\) is

$$
\psi_i(\ell,p)
=
\frac{d_i}{r_i}
+
\left(
p-\frac{d_i}{r_i}
\right)e^{-r_i\ell}.
\tag{12}
$$

In particular, its limit is independent of \(p\). Let \(N_Q^\infty\) be obtained from \(N_Q^{\mathbf p}\) by replacing \(\psi_i(\ell,p_i)\) by \(d_i/r_i\), and put

$$
K_{T,\infty}(Q)
=
\frac{N_Q^\infty}{D_Q(\ell_T)}.
$$

The same consistency-ratio calculation at infinite time gives

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{Q\in\mathcal E_T}K_{T,\infty}(Q).
\tag{13}
$$

Let \(K_{T,t}^{\varepsilon,\mathbf 1}(Q)\) denote the factor (10) for the less noisy model with terminal density \(\mathbf 1\). The successful-interaction rates, and hence the normalizers \(D_Q\), are unchanged by the pure-death perturbation. The explicit formulas, patch positivity, and

$$
p_i+1\ge2p_i^\star
$$

give the two local estimates

$$
\left|
K_{T,t}^{\mathbf p}(Q)
\right|,
\quad
K_{T,\infty}(Q)
\le
K_{T,t}^{\varepsilon,\mathbf 1}(Q),
\tag{14}
$$

and

$$
\left|
K_{T,t}^{\mathbf p}(Q)
-
K_{T,\infty}(Q)
\right|
\le
2e^{-\varepsilon(t-T)}
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
\tag{15}
$$

For an \(\mathsf{IE}\)-patch, (15) follows directly from (12): after removing \(\varepsilon\) from \(r_i\), the all-one comparison factor dominates \(e^{-(r_i-\varepsilon)\ell_t}\), while \(\ell_t\ge t-T\).

For an \(\mathsf{OE}\)-patch with \(\beta_i(S)>0\), write

$$
q_i=\frac{d_i}{r_i},
\qquad
p_{i,S}^\star
=
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}.
$$

Its numerator is a positive multiple of

$$
\psi_i(\ell,p)-p_{i,S}^\star.
$$

Patch positivity gives \(p_{i,S}^\star\le q_i\), while \(p_{i,S}^\star\le p_i^\star\) and \(p_i\ge(2p_i^\star-1)\vee0\) imply

$$
\left|p_i-q_i\right|
\le
2\left(1-p_{i,S}^\star\right).
$$

Together with (12), this proves (15). Affinity in \(p_i\) and the reflected comparison prove (14). If \(\beta_i(S)=0\), the numerator is independent of \(t\), so (15) is immediate.

Let

$$
N_T=\left|\mathcal E_T\right|.
$$

Telescoping the finite products in (11) and (13), and applying (4), (14), and (15), gives

$$
\begin{aligned}
&
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t})
\middle|\cG_T
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\middle|\cG_T
\right]
\right|
\\
&\qquad\le
2N_Te^{-\varepsilon(t-T)}
\prod_{P\in\mathcal B_T}C^\varepsilon(P)
\prod_{Q\in\mathcal E_T}
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
\end{aligned}
\tag{16}
$$

The product on the right is the conditional contribution of

$$
W_t^\varepsilon\ind(L_{T,t})
$$

given \(\cG_T\). The standard marked [interaction-cone](interaction-cone.md) estimate therefore gives

$$
\mathbb E_A\left[
N_TW_t^\varepsilon\ind(L_{T,t})
\right]
\le
K_A(1+T)^D.
\tag{17}
$$

Indeed, after marking one end-patch site, finite-range graphical path counting up to time \(T\) gives the polynomial volume factor, while the positive all-one comparison weight has total mass at most one. Integrating (16) and using (17) yields

$$
\begin{aligned}
&
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t})
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\right]
\right|
\\
&\qquad\le
2K_A(1+T)^D e^{-\varepsilon(t-T)}.
\end{aligned}
\tag{18}
$$

This estimate incorporates both the relaxation of the end-patch factors and the replacement of \(L_{T,t}\) by \(L_T\). Although \(\ind(L_{T,t})\downarrow\ind(L_T)\), estimating the indicators separately would retain the slow consistency rate. The cancellation in (10) is what removes it.

### Completion of the proof

Local finiteness gives

$$
L_\infty
:=
\bigcup_{T<\infty}L_T
=
\left\{
\left|\mathcal P\right|<\infty
\right\}.
$$

On \(L_\infty\setminus L_T\), the finite full patch family contains a successful interaction after time \(T\), and therefore contains an \(\mathsf{XO}\)-trail of total length at least \(T\). The same comparison as in (8) gives

$$
0\le
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\ind(L_\infty\setminus L_T)
\right]
\le
e^{-\varepsilon T}.
\tag{19}
$$

Combining (7), (8), (18), and (19), we obtain

$$
\begin{aligned}
&
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\\
&\qquad\le
2e^{-\varepsilon T}
+
2K_A(1+T)^D e^{-\varepsilon(t-T)}.
\end{aligned}
\tag{20}
$$

Taking \(T=t/2\) gives

$$
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\pi(\chi_A)
\right|
\le
K_A'(1+t)^D e^{-\varepsilon t/2},
\tag{21}
$$

uniformly over \(\mathbf p\ge\mathbf p^-\). Averaging over a mixing law gives the same estimate for mixtures.

Every local function has a finite expansion in [monomials](monomials.md), so (21) proves (1). Taking \(\nu=\mu_{\mathbf 1}\), compactness gives a subsequential weak limit, and convergence of all monomial moments shows that every subsequential limit is the same measure \(\pi\) characterized by (2). The finite-range spin-system semigroup is Feller, hence

$$
\pi P_s
=
\lim_{t\to\infty}\mu_{\mathbf 1}P_{t+s}
=
\pi,
$$

so \(\pi\) is invariant.

## Proof of the corollary

If \(\mathbf p^\star\le\frac12\mathbf 1\), then \(\mathbf p^-=\mathbf 0\). Every point mass \(\delta_\xi\) is the Bernoulli product measure with profile \(\mathbf p=\xi\), so the uniform estimate (1) gives (3). Any invariant measure must therefore agree with \(\pi\) on all local functions and hence equals \(\pi\). This proves uniqueness and uniform exponential ergodicity.
