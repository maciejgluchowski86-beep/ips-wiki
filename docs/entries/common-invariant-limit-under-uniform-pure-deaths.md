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

For a patch-positive spin system with a uniform pure-death component, mixtures of Bernoulli product measures above a threshold extending below the patch critical density converge to a common invariant measure. On a polynomial-growth lattice the convergence is exponential on local functions, up to a polynomial prefactor. The limiting factors are the contributions of the complete full patches.

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

Then there are an [invariant probability measure](invariant-measure.md) \(\pi\) and \(\gamma>0\) such that, for every local function \(f\), there is \(K_f<\infty\) for which

$$
\left|
\nu(P_tf)-\pi(f)
\right|
\le
K_f(1+t)^D e^{-\gamma t}.
$$

The estimate is uniform over all mixtures \(\nu\) of Bernoulli product measures whose mixing laws are supported on one-density profiles satisfying \(\mathbf p\ge\mathbf p^-\). Consequently \(\nu P_t\) converges weakly to \(\pi\) for every such mixture. In particular, every [high-density measure](high-density-measure.md) converges to \(\pi\).

Under the extension of the full-patch contribution defined below, the limiting measure is characterized on the monomial basis by

$$
\pi(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(|\mathcal P|<\infty\right)
\right],
\qquad A\Subset\Lambda.
\tag{1}
$$

Here \(\mathcal P\) is the full [patch](patch.md) family of the signed dual started from \(A\), and the integrand is defined to be zero when \(|\mathcal P|=\infty\).

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

## Infinite full-patch contribution

Put

$$
r_i=c_i^0(\vn)+c_i^1(\vn),
\qquad
d_i=c_i^0(\vn).
$$

These are nonnegative spin-system rates, and the pure-death assumption gives

$$
r_i\ge c_i^1(\vn)\ge\varepsilon.
\tag{2}
$$

Write

$$
\varphi_i^\infty
=
\lim_{\Delta\to\infty}\varphi_i(\Delta)
=
\begin{cases}
\dfrac{d_i}{\alpha_i}, & \alpha_i>0,\\[0.8em]
1, & \alpha_i=0,
\end{cases}
\qquad
\psi_i^\infty
=
\frac{d_i}{r_i}.
$$

Let \(P\) be an infinite full patch based at \(i\). For \(t\ge s(P)\), put \(\Delta=t-s(P)\). Since \(e(P)=\infty\), the two-duration function in the full-cut contribution satisfies

$$
\begin{aligned}
\psi_i(\Delta,\infty,z)
&=
d_i\int_0^\Delta e^{-r_i w}\,dw
+
z e^{-r_i\Delta}\varphi_i^\infty
\\
&=
\psi_i^\infty
+
\left(z\varphi_i^\infty-\psi_i^\infty\right)e^{-r_i\Delta}.
\end{aligned}
\tag{3}
$$

Thus the limit of \(C_t(z,P)\) exists and is independent of \(z\). Extend the notation \(C(P)\) to infinite full patches by

$$
C(P)
=
\lim_{t\to\infty}C_t(z,P)
=
\begin{cases}
\dfrac{\psi_i^\infty}{\varphi_i^\infty},
& \mathsf X(P)=\mathsf I,
\\[1.2em]
\dfrac{
c_i^0(S(P))
-
\left(c_i^0(S(P))+c_i^1(S(P))\right)\psi_i^\infty
}{
|c_i^0(S(P))|
+
|c_i^0(S(P))+c_i^1(S(P))|\varphi_i^\infty
},
& \mathsf X(P)=\mathsf O.
\end{cases}
\tag{4}
$$

As usual, only labels with positive consistency probability occur; their denominators in (4) are positive. Patch positivity makes both rows nonnegative. For the outgoing row this follows explicitly from

$$
\begin{aligned}
c_i^0(S)
-
\left(c_i^0(S)+c_i^1(S)\right)\psi_i^\infty
&=
\frac{
c_i^1(\vn)c_i^0(S)-c_i^0(\vn)c_i^1(S)
}{r_i}
\ge0.
\end{aligned}
\tag{5}
$$

Equation (3) also gives a uniform exponential approach to (4), with rate controlled by \(r_i\ge\varepsilon\).

## Proof of the theorem

Fix a deterministic one-density profile \(\mathbf p\ge\mathbf p^-\). Conditioning the duality formula on \(\cG_\infty\) and then using the full-skeleton form of the [patch representation](patch-representation-of-spin-systems.md) gives

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[W_t^{\mathbf p}\right],
\tag{6}
$$

where

$$
W_t^{\mathbf p}
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal C_t}C_t(\mathbf p,P).
\tag{7}
$$

The first product contains the full patches completed by time \(t\); the second contains the full patches cut by time \(t\).

For \(T<\infty\), let

$$
L_T
=
\left\{
\text{no successful interaction occurs after time }T
\right\},
$$

and set

$$
L_\infty
=
\bigcup_{T<\infty}L_T.
$$

Local finiteness and the patch construction give

$$
L_\infty
=
\{|\mathcal I|<\infty\}
=
\{|\mathcal P|<\infty\}.
\tag{8}
$$

We use a positive comparison that retains a uniform pure-death component. Set

$$
\lambda=\frac\varepsilon2,
\qquad
\cL^\circ=\cL-\lambda\mathcal N^0,
$$

where

$$
\mathcal N^0f(\xi)
=
\sum_{i\in\Lambda}
\left(f(\xi^{i,0})-f(\xi)\right).
$$

The lower bound on \(c_i^1\) makes \(\cL^\circ\) a spin-system generator, still with pure-death rate at least \(\lambda\). By the [duality noise lemma](duality-noise-lemma.md), \(\cL\) and \(\cL^\circ\) have the same signed dual and the same full successful-interaction skeleton. Their local Feynman--Kac factors satisfy

$$
F_t(z,P)
=
\exp\left(
-\lambda\int_{s(P)}^tX_u^P\,du
\right)
F_t^\circ(z,P).
\tag{9}
$$

In particular, if \(P\) has terminal label \(\mathsf O\), consistency forces \(X_u^P=1\) throughout the relevant part of the patch. Hence

$$
C(P)
=
e^{-\lambda(e(P)-s(P))}C^\circ(P)
\tag{10}
$$

for a completed \(\mathsf{IO}\)- or \(\mathsf{OO}\)-patch, and

$$
C_t(z,P)
=
e^{-\lambda(t-s(P))}C_t^\circ(z,P)
\tag{11}
$$

when such a full patch is cut at time \(t\).

Removing \(\lambda\mathcal N^0\) leaves all nonempty-target coefficients unchanged and increases the positive parts of the patch formulas. Together with the reflected comparison at \(\mathbf p^-\), this gives

$$
0\le C(P)\le C^\circ(P),
\qquad
|C(\mathbf p,P)|
\le
C(\mathbf1,P)
\le
C^\circ(\mathbf1,P).
$$

The first comparison applies to completed finite patches and, using (4) for both generators, to infinite full patches. The second applies to finite-horizon end patches.

For the finite-horizon comparison family, put

$$
H_t
=
\prod_{P\in\mathcal B_t}C^\circ(P)
\prod_{P\in\mathcal E_t}C^\circ(\mathbf 1,P).
\tag{12}
$$

The patch formulas, patch positivity, and the reflected end-patch comparison imply that every factor in (12) is nonnegative and that it dominates the corresponding absolute factor for \(\cL\) with terminal profile \(\mathbf p\). Moreover,

$$
\mathbb E_A[H_t]
=
\mu_{\mathbf1}\bigl(P_t^\circ(\chi_A)\bigr)
\le1.
\tag{13}
$$

The end-patch sites are the sites in the interaction cone. Finite-speed graphical path counting on a polynomial-growth lattice therefore gives the marked bound

$$
\mathbb E_A\left[
\left(1+|\mathcal E_t|\right)H_t
\right]
\le
K_A(1+t)^D.
\tag{14}
$$

The same argument, stopped at \(T\), gives

$$
\mathbb E_A\left[
\left(1+|\mathcal E_T|\right)H_t
\ind(L_T)
\right]
\le
K_A(1+T)^D,
\qquad t>T.
\tag{15}
$$

We next establish two estimates. First, suppose \(L_T^c\) occurs and let \(u>T\) be the first successful-interaction time after \(T\). Trace its source backward through the full patch family. Before time zero is reached, this gives a trail of \(\mathsf{OO}\)-patches ending in an \(\mathsf{IO}\)-patch that starts at the initial interaction. If \(u\le t\), the trail consists of bulk patches up to time \(u\). If \(u>t\), it consists of bulk patches followed by one full cut patch with terminal label \(\mathsf O\). In either case, the portion visible by time \(t\) has total duration at least \(\min\{u,t\}>T\). Equations (10)--(11) therefore extract the factor

$$
e^{-\lambda\min\{u,t\}}
\le
e^{-\lambda T}.
\tag{16}
$$

Average the remaining full-skeleton information back to \(\cG_t\). The bulk and terminal factors are then bounded by (12); marking the possible trail costs at most \(1+|\mathcal E_t|\). From (14),

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T^c)
\right]
\right|
\le
e^{-\lambda T}
\mathbb E_A\left[
\left(1+|\mathcal E_t|\right)H_t
\right]
\le
K_A(1+t)^D e^{-\lambda T}.
\tag{17}
$$

Second, on \(L_T\) every finite full patch is completed by time \(T\), and the remaining full patches are infinite and start no later than \(T\). Thus for \(t>T\),

$$
W_t^{\mathbf p}
=
\prod_{\substack{P\in\mathcal P\\e(P)<\infty}}C(P)
\prod_{\substack{P\in\mathcal P\\e(P)=\infty}}C_t(\mathbf p,P).
\tag{18}
$$

Define

$$
W_\infty
=
\prod_{P\in\mathcal P}C(P)
\ind(L_\infty).
\tag{19}
$$

By (3), every moving factor in (18) differs from its limit in (4) by a multiple of

$$
e^{-r_i(t-s(P))}
\le
e^{-\varepsilon(t-T)}.
$$

Apply the finite-product telescoping identity to the infinite-patch product in (18), and use (12) as the positive comparison after averaging the local patch data. Since the infinite full patches on \(L_T\) are in bijection with \(\mathcal E_T\), (15) gives

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T)
\right]
-
\mathbb E_A\left[
W_\infty\ind(L_T)
\right]
\right|
\le
K_A(1+T)^D e^{-\varepsilon(t-T)}.
\tag{20}
$$

It remains to control the tail of the limiting product. All factors in (19) are nonnegative. Let \(W_\infty^\circ\) be its analogue for \(\cL^\circ\). On each \(L_T\), the nonnegative finite-horizon weights (12) converge to \(W_\infty^\circ\). Hence Fatou's lemma and (13) give

$$
\mathbb E_A\left[
W_\infty^\circ\ind(L_\infty)
\right]
\le1.
\tag{21}
$$

On \(L_\infty\setminus L_T\), the first successful interaction after \(T\) has a complete \(\mathsf{OO}\)-to-\(\mathsf{IO}\) trail of total duration greater than \(T\). Using (10) on that trail and the positive comparison on every other full patch gives

$$
0
\le
W_\infty
\ind(L_\infty\setminus L_T)
\le
e^{-\lambda T}
W_\infty^\circ
\ind(L_\infty\setminus L_T).
$$

Consequently,

$$
\mathbb E_A\left[
W_\infty\ind(L_\infty\setminus L_T)
\right]
\le
e^{-\lambda T}.
\tag{22}
$$

Combining (6), (17), (20), and (22), for \(t>T\), gives

$$
\begin{aligned}
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A[W_\infty]
\right|
&\le
K_A(1+t)^D e^{-\lambda T}
+
K_A(1+T)^D e^{-\varepsilon(t-T)}
+
e^{-\lambda T}.
\end{aligned}
\tag{23}
$$

Take \(T=t/2\). Since \(\lambda=\varepsilon/2\), increasing \(K_A\) to cover bounded \(t\) yields

$$
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A[W_\infty]
\right|
\le
K_A(1+t)^D e^{-\varepsilon t/4}.
\tag{24}
$$

The estimate is uniform in \(\mathbf p\ge\mathbf p^-\), so it remains valid after averaging over any mixing law supported on such profiles.

Every local function depending on a finite set \(S\) has a finite [monomial](monomials.md) expansion

$$
f
=
\sum_{A\subseteq S}\widehat f(A)\chi_A.
$$

Summing (24) proves the asserted local-function estimate once the limiting moments are identified with a probability measure. Take the initial law \(\mu_{\mathbf1}\). Compactness of \(\{0,1\}^{\Lambda}\) gives a subsequential weak limit of \(\mu_{\mathbf1}P_t\), while convergence of every monomial moment shows that all subsequential limits agree. Denote the resulting probability measure by \(\pi\). Equations (19) and (24) give (1), and local functions determine weak convergence.

Finally, the finite-range spin-system semigroup is Feller. Hence, for every \(s\ge0\),

$$
\pi P_s
=
\lim_{t\to\infty}(\mu_{\mathbf1}P_t)P_s
=
\lim_{t\to\infty}\mu_{\mathbf1}P_{t+s}
=
\pi.
$$

Thus \(\pi\) is invariant. Since \(\mathbf p^-\le\mathbf p^\star\), the class covered by the theorem contains all high-density measures.

## Proof of the corollary

The assumption \(\mathbf p^\star\le\frac12\mathbf1\) gives \(\mathbf p^-=\mathbf0\). Every deterministic law is a product measure because

$$
\delta_\xi=\mu_{\mathbf\xi}.
$$

Thus the theorem's estimate holds uniformly over all deterministic initial configurations and hence over all initial laws. If \(\widetilde\pi\) is invariant, then for every local function \(f\),

$$
\left|\widetilde\pi(f)-\pi(f)\right|
=
\left|\widetilde\pi(P_tf)-\pi(f)\right|
\longrightarrow0,
$$

so \(\widetilde\pi=\pi\). Absorbing the polynomial factor into a slightly smaller exponential rate proves uniform exponential ergodicity on local functions.
