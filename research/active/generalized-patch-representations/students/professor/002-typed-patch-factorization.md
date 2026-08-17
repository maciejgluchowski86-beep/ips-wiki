# Assignment 002 report: typed successful-skeleton factorization

Date: 2026-08-17

## Verdict

**`CONTINUE-TYPED-REPRESENTATION`.**

The one-site typed patch geometry survives for general finite-state single-site replacement dynamics, but with one precise modification relative to the binary paper.

Bare conditional independence given only the coarse typed successful-record list is false: a selected incoming target can conflict with a different active type, send the global dual to cemetery, and thereby remove all future no-record constraints at once.

However this dependence is supported entirely on cemetery histories. Since the typed duality function satisfies `H_dagger=0`, every such history has exactly zero Feynman--Kac weight. After multiplying by the noncemetery indicator, exact skeleton consistency is a product of one local event per one-site patch, and the Mecke/Radon--Nikodym proof goes through.

Thus the correct generalized object is the **noncemetery/killed successful skeleton** rather than the bare record list.

## 1. Typed patch state and boundaries

For a patch `P` on site `i`, the local state is

\[
X_u^P\in E,
\]

with `0` inactive and `a in E_*` active with type `a`.

An incoming boundary carries a typed target label `a`; the next patch begins at type `a`.

An outgoing boundary carries the revealed pre-source type `r` and typed target `tau`. At an outgoing start, the hidden source outcome `s in E` is sampled with law

\[
P(s=u\mid i,r,\tau)
=\frac{|a_{i,r}^u(\tau)|}{\Lambda_{i,r}(\tau)},
\qquad
\Lambda_{i,r}(\tau)=\sum_v|a_{i,r}^v(\tau)|.
\]

The hidden outcome sets the post-boundary local source type.

Interior empty-target clocks update the local type when their source-type label matches. An interior nonempty-target clock with matching source type would be an omitted successful record and is forbidden by consistency.

## 2. Exact local consistency event

For each patch `P`, `Con(P)` consists of:

1. every interior nonempty-target point `(r,s,tau)` has `X_{u-}^P != r`;
2. an outgoing terminal with source type `r_e` satisfies
   \[
   X_{e-}^P=r_e;
   \]
3. an incoming terminal carrying type `a_e` satisfies
   \[
   X_{e-}^P\in\{0,a_e\};
   \]
4. an end terminal has no additional condition.

The incoming condition is the only genuinely new boundary condition. A different active type is a target conflict and sends the global typed dual to cemetery.

The deterministic stitching lemma is:

\[
\boxed{
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_{P\in\mathcal P_T(g)}\operatorname{Con}(P).}
\]

The proof is by chronological induction over the selected records. Empty-target marks evolve only their source line; the interior condition excludes omitted selected points; outgoing terminal conditions make inserted source records successful; incoming terminal conditions make every target merge compatible.

Decisive file: `002a-typed-patch-local-consistency.md`, commit `08108e32`.

## 3. Mandatory d=3 conflict gate

The exact finite gate uses two sites and two selected records

\[
R_1=(0,t_1,1,\tau_1),\qquad \tau_1(1)=1,
\]

\[
R_2=(1,t_2,1,\tau_2),\qquad \tau_2(0)=1.
\]

The first hidden source outcome is `s_1 in {1,2}`. Between records an empty-target `2 -> 1` dual retyping clock may occur on site `0`. Therefore the incoming target of `R_2` conflicts exactly when

\[
(s_1,e)=(2,0).
\]

After `R_2`, two future nonempty-target clock indicators test the no-extra-record conditions on the two end patches. The second hidden source outcome is `s_2 in {0,1}`.

Taking all five hidden variables independent and fair gives `32` exact configurations, including `8` incoming-target conflicts.

The bare two-record skeleton has mass

\[
\frac{17}{32},
\]

while its noncemetery part has mass

\[
\frac9{32}
=
\frac34\cdot\frac12\cdot\frac34.
\]

If `K` is the incoming conflict and `B` a future mark in the next site-0 patch, then under bare skeleton conditioning

\[
P(K\mid G)=\frac8{17},
\qquad
P(B\mid G)=\frac4{17},
\]

but

\[
\boxed{
P(K,B\mid G)=\frac4{17}
\ne
\frac{32}{289}.}
\]

So full conditional-law factorization given `G` is genuinely false.

After multiplying by the noncemetery indicator, the exact weight is the product of the three local consistency indicators. The verifier checks all `32` cells of the normalized weighted joint law against the product of its patch marginals.

Decisive files:

- `002-typed-factorization-verifier.py`, commit `b9e75b42`;
- `002b-finite-cemetery-factorization-gate.md`, commit `d8eca517`.

## 4. Weighted Mecke factorization

For a chronological candidate record list

\[
g=((i_k,t_k,r_k,\tau_k))_{k=1}^n,
\]

define the reference record measure

\[
m_T(dg)
=
\prod_{k=1}^n\Lambda_{i_k,r_k}(\tau_k)
\,dt_1\cdots dt_n,
\]

summed over the discrete record labels.

The inserted selected points carry independent hidden source-outcome marks. The remaining Poisson marks split over disjoint source--time patch strips. Hence before consistency conditioning the patch variables are independent.

The weighted Mecke identity is

\[
\boxed{\begin{aligned}
&E\left[h(G_T)1_{\{\tau_\dagger>T\}}
\prod_Pf_P(\Sigma_P)\right]\\
&\qquad=
\int h(g)
\prod_{P\in\mathcal P_T(g)}
E_P\left[f_P(\Sigma_P)1_{\operatorname{Con}(P)}\right]
\,m_T(dg).
\end{aligned}}
\]

This follows by multivariate Mecke plus the exact local-consistency identity above.

Setting `f_P=1` gives the noncemetery skeleton submeasure

\[
\nu_T(dg)
:=P(G_T\in dg,\tau_\dagger>T)
\]

with density

\[
\boxed{
\nu_T(dg)
=
\prod_P P_P(\operatorname{Con}(P))\,m_T(dg).}
\]

Consequently, for `nu_T`-almost every `g`,

\[
\boxed{
E\left[\prod_Pf_P(\Sigma_P)\mid G_T=g,\tau_\dagger>T\right]
=
\prod_PE_P^{\mathrm{con}}[f_P].}
\]

Equivalently collapse all cemetery histories to one outer atom and condition on the resulting killed skeleton.

Decisive theorem: `002c-weighted-typed-patch-factorization.md`, commit `925c8330`.

## 5. Why this is representation-sufficient

The typed Feynman--Kac variable is

\[
W_T(\eta)
=
\sigma_T
\exp\left(\int_0^TV(\xi_u)\,du\right)
H_{\xi_T}(\eta),
\]

with `H_dagger=0`. Therefore

\[
W_T=1_{\{\tau_\dagger>T\}}W_T
\]

identically.

Thus the factorization theorem deletes no nonzero contribution. Cemetery paths are not approximated or bounded; their exact duality weight is zero.

This is sufficient to continue to an exact typed patch representation.

## 6. Exact next theorem

The next block should prove the following, still without positivity.

For every noncemetery typed patch `P`, define a local Feynman--Kac weight from:

1. the sign of the hidden source outcome at an outgoing start;
2. the signs of effective empty-target interior marks;
3. the local potential integral
   \[
   \exp\left(\int_{s(P)}^{e(P)\wedge T}
   1_{\{X_u^P\ne0\}}v_{i(P),X_u^P}\,du\right);
   \]
4. for end patches at horizon `T`, the terminal one-site factor
   \[
   h_{X_T^P}(\eta_{i(P)}),
   \qquad h_0\equiv1.
   \]

On noncemetery paths, patch strips partition all active source-time and every effective sign mark belongs to one source patch, so the global Feynman--Kac integrand should be the product of these local weights.

The desired theorem is then

\[
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}
E_P\left[w_P(\Sigma_P;\eta)1_{\operatorname{Con}(P)}\right]
\,m_T(dg),
\]

or equivalently

\[
P_TH_{\xi_0}(\eta)
=
\int
\prod_P C_P(\eta)\,\nu_T(dg),
\qquad
C_P(\eta)=E_P^{\mathrm{con}}[w_P].
\]

Bulk contributions should be independent of `eta`; only end contributions retain the terminal physical spin.

This theorem should be established before asking what typed patch positivity means.

## 7. Scope

Assignment 002 proves factorization for finite-state **single-site replacement** dynamics in the canonical indicator tensor basis.

It does not yet:

- define typed patch positivity;
- handle simultaneous multi-site physical updates;
- prove any moment-order or convergence theorem;
- make a literature novelty claim.

The incoming-conflict phenomenon is a real difference from the binary paper, but it is resolved exactly at the representation level by the killed/noncemetery skeleton.
