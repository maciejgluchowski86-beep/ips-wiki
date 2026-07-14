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
\qquad
L_T=L_{T,\infty}.
$$

On \(L_{T,t}^c\), let \(u\in[T,t)\) be the first successful-interaction time after \(T\), and let \(\Gamma_u\) be the trail of \(\mathsf{XO}\)-patches leading to its source. Every patch in \(\Gamma_u\) belongs to \(\mathcal B_t\), and

$$
\sum_{P\in\Gamma_u}\Delta(P)\ge u\ge T.
$$

Using the exact comparison (5) along this trail gives

$$
\begin{aligned}
\prod_{P\in\Gamma_u}C(P)
&=
\exp\left(
-\varepsilon\sum_{P\in\Gamma_u}\Delta(P)
\right)
\prod_{P\in\Gamma_u}C^\varepsilon(P)
\\
&\le
e^{-\varepsilon T}
\prod_{P\in\Gamma_u}C^\varepsilon(P).
\end{aligned}
$$

Apply (4) to the other bulk patches and (6) to the end patches. Pointwise on \(L_{T,t}^c\),

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
W_t^{\mathbf p}\ind(L_{T,t}^c)
\right]
\right|
&\le
\mathbb E_A\left[
\left|W_t^{\mathbf p}\right|\ind(L_{T,t}^c)
\right]
\\
&\le
e^{-\varepsilon T}
\mathbb E_A\left[
W_t^\varepsilon\ind(L_{T,t}^c)
\right]
\\
&\le
e^{-\varepsilon T}
\mathbb E_A\left[W_t^\varepsilon\right]
\\
&\le
e^{-\varepsilon T}.
\end{aligned}
\tag{8}
$$

### Conditioning at time \(T\)

On \(L_{T,t}\), no patch begins or ends between \(T\) and \(t\). Hence, up to the null event of an interaction exactly at \(T\),

$$
\mathcal B_t=\mathcal B_T,
$$

and every \(Q\in\mathcal E_T\) has a unique extension \(Q_u\in\mathcal E_u\) for \(T\le u\le t\). Fix such a \(Q\), write

$$
i=i(Q),
\qquad
s=s(Q),
\qquad
\ell_u=u-s,
$$

and write \(S=S(Q)\) when \(\mathsf X(Q)=\mathsf O\).

Suppose first that \(Q\) has type \(\mathsf{IE}\). Given that it is consistent through time \(T\), its probability of extending without a successful interaction through time \(u\) is

$$
\frac{\varphi_i(\ell_u)}{\varphi_i(\ell_T)}.
$$

Multiplying this probability by its end contribution gives

$$
\frac{\varphi_i(\ell_u)}{\varphi_i(\ell_T)}
\frac{\psi_i(\ell_u,p_i)}{\varphi_i(\ell_u)}
=
\frac{\psi_i(\ell_u,p_i)}{\varphi_i(\ell_T)}.
$$

For an \(\mathsf{OE}\)-patch, the same calculation is

$$
\begin{aligned}
&
\frac{
\delta_i(S)+\beta_i(S)\varphi_i(\ell_u)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\ell_T)
}
\\
&\qquad\quad\times
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\ell_u,p_i)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\ell_u)
}
\\
&\qquad=
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\ell_u,p_i)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\ell_T)
}.
\end{aligned}
$$

Denote the last expression in the appropriate one of these two displays by \(K_{T,u}^{\mathbf p}(Q)\). The normalizer at time \(u\), whose convergence may be slow, has canceled.

Conditional on \(\cG_T\), the post-\(T\) interaction data of the distinct end patches are independent. Multiplying their extension probabilities and their end contributions therefore gives

$$
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t})
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{Q\in\mathcal E_T}K_{T,t}^{\mathbf p}(Q).
\tag{9}
$$

### Relaxation of the killed factors

For a patch based at \(i\), put

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
d_i=c_i^0(\vn),
\qquad
q_i=\frac{d_i}{r_i}.
$$

Since \(r_i\ge\varepsilon\), the patch-contribution formula reads

$$
\psi_i(\ell,p)
=
q_i+(p-q_i)e^{-r_i\ell}.
\tag{10}
$$

Define \(K_{T,\infty}(Q)\) by replacing \(\psi_i(\ell_u,p_i)\) in the displayed formula for \(K_{T,u}^{\mathbf p}(Q)\) by \(q_i\). Equivalently, it is the limit of the joint factor “no successful interaction through \(u\)” times “end contribution at \(u\).” Thus this definition also covers the case in which the limiting consistency probability vanishes. Conditional factorization gives

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\ind(L_T)
\middle|\cG_T
\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{Q\in\mathcal E_T}K_{T,\infty}(Q).
\tag{11}
$$

Let \(K_{T,t}^{\varepsilon,\mathbf 1}(Q)\) be the same killed factor for the less noisy model with terminal density \(\mathbf 1\). The successful-interaction rates and all consistency normalizers are unchanged by the perturbation. Put \(r_i^\varepsilon=r_i-\varepsilon\). When \(r_i^\varepsilon>0\), set \(q_i^\varepsilon=d_i/r_i^\varepsilon\); then

$$
\psi_i^\varepsilon(\ell,1)
=
q_i^\varepsilon+
\left(1-q_i^\varepsilon\right)e^{-r_i^\varepsilon\ell}
\ge
e^{-r_i^\varepsilon\ell}.
\tag{12}
$$

If \(r_i^\varepsilon=0\), then \(d_i=0\) and \(\psi_i^\varepsilon(\ell,1)=1\), so the estimates below follow directly.

For an \(\mathsf{IE}\)-patch, (10), (12), and \(\ell_t\ge t-T\) give

$$
\begin{aligned}
\left|
K_{T,t}^{\mathbf p}(Q)-K_{T,\infty}(Q)
\right|
&=
\frac{
\left|p_i-q_i\right|e^{-r_i\ell_t}
}{
\varphi_i(\ell_T)
}
\\
&\le
e^{-\varepsilon\ell_t}
\frac{
e^{-r_i^\varepsilon\ell_t}
}{
\varphi_i(\ell_T)
}
\\
&\le
e^{-\varepsilon(t-T)}
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
\end{aligned}
\tag{13}
$$

Now let \(Q\) have type \(\mathsf{OE}\). If \(\beta_i(S)=0\), its killed factor is independent of \(t\), and there is nothing to prove. Otherwise patch positivity gives

$$
\beta_i(S)\sigma_i^\beta(S)
=
-c_i^0(S)-c_i^1(S)
=
\beta_i(S)>0.
$$

Writing

$$
p_{i,S}^\star
=
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)},
$$

the numerator of the killed factor is

$$
\beta_i(S)
\left(
\psi_i(\ell,p)-p_{i,S}^\star
\right).
$$

Patch positivity gives

$$
p_{i,S}^\star\le q_i\le q_i^\varepsilon.
\tag{14}
$$

Moreover,

$$
\left|p_i-q_i\right|
\le
2\left(1-p_{i,S}^\star\right).
\tag{15}
$$

Indeed, if \(p_i\ge q_i\), the left-hand side is at most \(1-q_i\le1-p_{i,S}^\star\). If \(p_i<q_i\) and \(p_i^\star<1/2\), it is at most \(1\le2(1-p_{i,S}^\star)\). If \(p_i<q_i\) and \(p_i^\star\ge1/2\), then

$$
q_i-p_i
\le
1-p_i
\le
2(1-p_i^\star)
\le
2(1-p_{i,S}^\star).
$$

By (12) and (14),

$$
\begin{aligned}
\psi_i^\varepsilon(\ell,1)-p_{i,S}^\star
&=
q_i^\varepsilon-p_{i,S}^\star
+
\left(1-q_i^\varepsilon\right)e^{-r_i^\varepsilon\ell}
\\
&\ge
\left(1-p_{i,S}^\star\right)e^{-r_i^\varepsilon\ell}.
\end{aligned}
\tag{16}
$$

The denominators of the original and less noisy killed factors are the same. Equations (10), (15), and (16) therefore yield

$$
\begin{aligned}
\left|
K_{T,t}^{\mathbf p}(Q)-K_{T,\infty}(Q)
\right|
&=
\frac{
\beta_i(S)\left|p_i-q_i\right|e^{-r_i\ell_t}
}{
\delta_i(S)+\beta_i(S)\varphi_i(\ell_T)
}
\\
&\le
2e^{-\varepsilon(t-T)}
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
\end{aligned}
\tag{17}
$$

The same comparison factors dominate the killed factors themselves:

$$
\left|K_{T,t}^{\mathbf p}(Q)\right|,
\quad
K_{T,\infty}(Q)
\le
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
\tag{18}
$$

For an \(\mathsf{IE}\)-patch,

$$
0\le
\psi_i(\ell,p_i)
\le
\psi_i(\ell,1)
\le
\psi_i^\varepsilon(\ell,1),
\qquad
0\le q_i\le q_i^\varepsilon\le\psi_i^\varepsilon(\ell,1).
$$

Dividing by the common positive denominator \(\varphi_i(\ell_T)\) proves (18). For an \(\mathsf{OE}\)-patch, the killed factor is affine and nondecreasing in \(p_i\), and

$$
K_{T,t}^{\mathbf p}(Q)
+
K_{T,t}^{\mathbf 1}(Q)
=
2K_{T,t}^{(\mathbf p+\mathbf 1)/2}(Q)
\ge0
$$

because \((p_i+1)/2\ge p_i^\star\). Hence

$$
\left|K_{T,t}^{\mathbf p}(Q)\right|
\le
K_{T,t}^{\mathbf 1}(Q)
\le
K_{T,t}^{\varepsilon,\mathbf 1}(Q).
$$

Also \(K_{T,\infty}(Q)\ge0\) by patch positivity, and (12), (14) show that it is no larger than the less noisy factor.

Let \(N_T=|\mathcal E_T|\), and fix a deterministic ordering of \(\mathcal E_T\). The elementary telescoping inequality

$$
\left|
\prod_Q a_Q-\prod_Q b_Q
\right|
\le
\sum_Q
\left|a_Q-b_Q\right|
\prod_{R<Q}|a_R|
\prod_{R>Q}|b_R|
$$

together with (4), (13), (17), and (18) gives

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
\tag{19}
$$

The product on the right is

$$
\mathbb E_A\left[
W_t^\varepsilon\ind(L_{T,t})
\middle|\cG_T
\right].
$$

> **Finite-speed note.** The resulting marked expectation is most cleanly bounded by temporarily restricting the graphical construction to a finite ball. Choose \(v\) so large that, up to time \(t\), replacing the infinite lattice by the ball of radius \(vt\) around \(A\) changes the semigroup—and the same graphical expansion with one marked terminal site—by at most \(C_Ae^{-\varepsilon t}\). Such a choice is possible from the Poisson path bound for a uniformly bounded finite-range system. Perform the duality and patch factorization inside this ball. On \(L_{T,t}\), \(N_T=N_t\), and deterministically
>
> $$
> N_t=|\mathcal E_t|
> \le
> \left|B(A,vt)\right|
> \le
> C_A(1+t)^D.
> $$
>
> Since the positive comparison weight has total mass at most one,
>
> $$
> \mathbb E_A\left[
> N_TW_t^\varepsilon\ind(L_{T,t})
> \right]
> \le
> K_A(1+t)^D.
> \tag{20}
> $$
>
> The finite-speed error is absorbed by increasing \(K_A\). This finite-volume restriction is needed only for this bound, so no finite-volume notation is carried through the rest of the argument.

Integrating (19) and using (20) yields

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
2K_A(1+t)^D e^{-\varepsilon(t-T)}.
\end{aligned}
\tag{21}
$$

This estimate treats the relaxation of the end-patch factors and the replacement of \(L_{T,t}\) by \(L_T\) simultaneously. Estimating the indicators separately would reintroduce the slow consistency rate that canceled above.

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

On \(L_\infty\setminus L_T\), choose the first successful interaction after \(T\) and its \(\mathsf{XO}\)-trail. The same calculation as in the proof of (8) gives the pointwise bound

$$
\prod_{P\in\mathcal P}C(P)
\ind(L_\infty\setminus L_T)
\le
e^{-\varepsilon T}
\prod_{P\in\mathcal P}C^\varepsilon(P)
\ind(L_\infty\setminus L_T).
$$

The full less noisy product has total mass at most one. Indeed, on \(L_\infty\) the nonnegative finite-horizon weights \(W_u^\varepsilon\) converge to that product, and Fatou's lemma and (7) give

$$
\begin{aligned}
\mathbb E_A\left[
\prod_{P\in\mathcal P}C^\varepsilon(P)\ind(L_\infty)
\right]
&\le
\liminf_{u\to\infty}
\mathbb E_A\left[W_u^\varepsilon\right]
\\
&\le1.
\end{aligned}
$$

Consequently,

$$
\begin{aligned}
0
&\le
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)
\ind(L_\infty\setminus L_T)
\right]
\\
&\le
e^{-\varepsilon T}
\mathbb E_A\left[
\prod_{P\in\mathcal P}C^\varepsilon(P)
\ind(L_\infty\setminus L_T)
\right]
\\
&\le
e^{-\varepsilon T}.
\end{aligned}
\tag{22}
$$

Combining (7), (8), (21), and (22), we obtain

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
2K_A(1+t)^D e^{-\varepsilon(t-T)}.
\end{aligned}
\tag{23}
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
\tag{24}
$$

uniformly over \(\mathbf p\ge\mathbf p^-\). Averaging over a mixing law gives the same estimate for mixtures.

Every local function has a finite expansion in [monomials](monomials.md), so (24) proves (1). Taking \(\nu=\mu_{\mathbf 1}\), compactness gives a subsequential weak limit, and convergence of all monomial moments shows that every subsequential limit is the same measure \(\pi\) characterized by (2). The finite-range spin-system semigroup is Feller, hence

$$
\pi P_s
=
\lim_{t\to\infty}\mu_{\mathbf 1}P_{t+s}
=
\pi,
$$

so \(\pi\) is invariant.

## Proof of the corollary

If \(\mathbf p^\star\le\frac12\mathbf 1\), then \(\mathbf p^-=\mathbf 0\). Every point mass \(\delta_\xi\) is the Bernoulli product measure with profile \(\mathbf p=\xi\), so the uniform estimate (1) gives (3). If \(\rho\) is invariant, then for every local function \(f\),

$$
\left|\rho(f)-\pi(f)\right|
=
\left|\rho(P_tf)-\pi(f)\right|
\le
\sup_\xi\left|P_tf(\xi)-\pi(f)\right|
\underset{t\to\infty}{\longrightarrow}0.
$$

Thus \(\rho=\pi\), proving uniqueness and uniform exponential ergodicity.
