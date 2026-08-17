# 002c: weighted typed patch factorization

Date: 2026-08-17

The finite gate in `002b-finite-cemetery-factorization-gate.md` shows that conditional independence given only the coarse typed record list is false. This note proves the representation-sufficient replacement allowed by Assignment 002.

## 1. Reference record measure

For each nonempty typed target `tau`, superpose the signed-dual branch clocks over source outcome `s` at fixed `(i,r,tau)`. The coarse rate is

\[
\Lambda_{i,r}(\tau)=\sum_{s\in E}|a_{i,r}^s(\tau)|,
\]

and a selected coarse point carries an independent hidden outcome with law

\[
q_{i,r,\tau}(s)=\frac{|a_{i,r}^s(\tau)|}{\Lambda_{i,r}(\tau)}.
\]

Let `G_T` be the typed successful record list through time `T`, and let `tau_dagger` be the cemetery hitting time.

For a chronological candidate list

\[
g=((i_k,t_k,r_k,\tau_k))_{k=1}^n,
\qquad0<t_1<\cdots<t_n\le T,
\]

define, on each fixed discrete-label component,

\[
m_T(dg)=\prod_{k=1}^n\Lambda_{i_k,r_k}(\tau_k)\,dt_1\cdots dt_n,
\tag{1.1}
\]

and sum over all finite lists. Impossible lists will simply have zero consistency factor.

For every induced patch `P`, `Sigma_P` contains all ordinary local clocks in its open source-time strip and, when the patch starts at an outgoing selected record, that record's hidden source outcome. These variables are independent under the inserted-record reference law: patch interiors are disjoint source-time strips and selected hidden outcomes are independent marks.

Let `Con(P)` be the local event from 002a: no interior unrecorded successful nonempty-target clock, the correct type at an outgoing terminal, and compatibility `X_{e-} in {0,a}` at an incoming terminal.

## 2. Weighted Mecke identity

### Theorem 2.1

For every finite horizon `T`, nonnegative measurable skeleton function `h`, and nonnegative measurable patch functions `f_P`,

\[
\boxed{\begin{aligned}
&E\left[h(G_T)1_{\{\tau_\dagger>T\}}
\prod_{P\in\mathcal P_T(G_T)}f_P(\Sigma_P)\right]\\
&\qquad=
\int h(g)\prod_{P\in\mathcal P_T(g)}
E_P\left[f_P(\Sigma_P)1_{\operatorname{Con}(P)}\right]m_T(dg).
\end{aligned}}
\tag{2.1}
\]

The same identity holds for an integrable signed product.

### Proof

Apply the multivariate Mecke formula to ordered tuples of nonempty-target coarse Poisson points. Fixing the inserted list `g` leaves independent hidden outcome marks at the selected points and independent Poisson restrictions on the disjoint patch strips, hence the product reference laws `P_P`.

On this inserted-record space, 002a proved the exact event identity

\[
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_{P\in\mathcal P_T(g)}\operatorname{Con}(P).
\tag{2.2}
\]

The interior conditions exclude every omitted successful nonempty-target point; outgoing terminal conditions make every inserted source record successful with its revealed pre-type; incoming terminal conditions make every target merge compatible. Conversely, a noncemetery trajectory with exactly those records must satisfy all three kinds of local condition.

After substituting (2.2), every factor depends on one independent patch variable, so the reference expectation splits into the product in (2.1). The signed integrable case follows by positive/negative parts. `square`

## 3. Conditional factorization under the noncemetery skeleton

Setting all `f_P=1` gives the subprobability skeleton law

\[
\nu_T(dg):=P(G_T\in dg,\tau_\dagger>T)
\]

with exact density

\[
\boxed{
\nu_T(dg)=
\prod_{P\in\mathcal P_T(g)}P_P(\operatorname{Con}(P))\,m_T(dg).}
\tag{3.1}
\]

For `nu_T`-almost every `g`, define the normalized consistent patch law

\[
P_P^{\mathrm{con}}(\cdot)
=P_P(\cdot\mid\operatorname{Con}(P)).
\]

Taking the Radon--Nikodym derivative of (2.1) with respect to (3.1) yields

\[
\boxed{
E\left[\prod_Pf_P(\Sigma_P)\mid G_T=g,\tau_\dagger>T\right]
=
\prod_PE_P^{\mathrm{con}}[f_P].}
\tag{3.2}
\]

Thus the hidden patch variables are genuinely conditionally independent given the successful record list and noncemetery survival.

Equivalently, collapse every cemetery history to one outer atom by defining

\[
\widehat G_T=G_T\quad\text{on }\{\tau_\dagger>T\},
\qquad
\widehat G_T=\dagger\quad\text{otherwise}.
\]

Conditional factorization holds at every ordinary value of this killed skeleton. The cemetery atom needs no patch law in the semigroup representation.

## 4. Bare conditioning really fails

The survival condition in (2.1)--(3.2) cannot generally be removed. In the exact `d=3` gate, if `K` is the incoming-target conflict at the second selected record and `B` is a future mark in the next patch,

\[
P(K,B\mid G)=\frac4{17}
\ne
\frac{32}{289}
=P(K\mid G)P(B\mid G).
\]

The reason is structural: after a selected incoming target conflicts, the global dual is in cemetery and all future no-record constraints disappear simultaneously.

## 5. Why the weaker theorem is sufficient

The Feynman--Kac variable from Assignment 001 is

\[
W_T(\eta)=\sigma_T
\exp\left(\int_0^TV(\xi_u)\,du\right)H_{\xi_T}(\eta),
\]

with `H_dagger=0` and `V(dagger)=0`. Hence identically

\[
\boxed{W_T(\eta)=1_{\{\tau_\dagger>T\}}W_T(\eta).}
\tag{5.1}
\]

Cemetery histories therefore have exactly zero semigroup weight. The weighted factorization (2.1) loses no contribution and is sufficient for an exact generalized patch representation.

The next block should factor `W_T` itself into explicit one-patch multiplicative weights, define normalized bulk/end typed patch contributions under `P_P^{con}`, and state the semigroup representation over `nu_T` or the killed skeleton `widehat G_T`. Patch positivity is still downstream.

## 6. Registered stop-rule consequence

`STOP-NO-LOCAL-CONSISTENCY` does not occur: on noncemetery histories exact skeleton consistency is a product of local events.

`STOP-TYPED-CONFLICT-COUPLING` also does not occur: conflict creates bare conditional dependence, but the dependence is supported entirely on cemetery histories and vanishes identically after the exact Feynman--Kac zero weight is inserted.

Together with the mandatory finite gate, Theorem 2.1 reaches the positive side of the Assignment-002 rule, subject only to final report/audit packaging.
