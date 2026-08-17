# Typed successful-skeleton factorization

> **Current research.** This page records the theorem established on `research/generalized-patch-representations`. It has not yet completed independent external audit.

The finite-state typed dual has a one-site patch decomposition analogous to the binary patch construction, but target-type conflicts force one modification: the exact factorization is attached to the **noncemetery/killed successful skeleton**, not to the bare successful-record list.

## Typed boundaries

A successful nonempty-target record is

\[
(i,t,r,\tau),
\]

where `r` is the pre-interaction source type and `tau` is the typed target. The hidden source outcome `s` is not recorded.

A patch on site `i` carries a local state

\[
X_u^P\in E,
\]

with `0` meaning inactive and `a\neq0` meaning active with type `a`.

At an incoming start carrying type `a`, set `X_s^P=a`. At an outgoing start, sample the hidden source outcome with probability proportional to the absolute typed branch coefficient and set the post-boundary local state to that outcome.

## Local consistency

For a patch `P`, consistency requires:

1. no interior nonempty-target clock has source-type label equal to the current local type;
2. an outgoing terminal with revealed source type `r` has `X_{e-}^P=r`;
3. an incoming terminal carrying type `a` has
   \[
   X_{e-}^P\in\{0,a\};
   \]
4. an end patch has no additional terminal condition.

The incoming condition is new. If a target type `a` arrives while the local state is a different nonzero type, the typed merge conflicts and the global dual enters cemetery.

For any inserted candidate record list `g`,

\[
\boxed{
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_{P\in\mathcal P_T(g)}\operatorname{Con}(P).}
\]

Thus exact skeleton consistency is patch-local once cemetery histories are excluded.

## Why bare conditioning fails

A conflicting incoming target is applied only after its source record has already been selected. Therefore the conflicting record remains in the successful list, but after the conflict all later successful records are suppressed automatically because the global dual is in cemetery.

An exact `d=3` two-record calculation gives events `K` (incoming conflict) and `B` (a future mark in the next patch) such that

\[
P(K\mid G)=\frac8{17},
\qquad
P(B\mid G)=\frac4{17},
\]

but

\[
P(K,B\mid G)=\frac4{17}
\ne
\frac{32}{289}.
\]

Hence the hidden patch variables are not independent conditional only on the bare typed record list.

## Weighted factorization

For a candidate record list

\[
g=((i_k,t_k,r_k,\tau_k))_{k=1}^n,
\]

write

\[
m_T(dg)
=
\prod_k\Lambda_{i_k,r_k}(\tau_k)
\,dt_1\cdots dt_n,
\]

where

\[
\Lambda_{i,r}(\tau)=\sum_s|a_{i,r}^s(\tau)|.
\]

Then for nonnegative measurable skeleton function `h` and patch functions `f_P`,

\[
\boxed{\begin{aligned}
&E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P(\Sigma_P)\right]\\
&\qquad=
\int h(g)\prod_P
E_P\left[f_P(\Sigma_P)1_{\operatorname{Con}(P)}\right]m_T(dg).
\end{aligned}}
\]

This is the typed analogue of patch factorization needed for the semigroup representation.

Equivalently, the noncemetery successful-skeleton submeasure satisfies

\[
\nu_T(dg)
=P(G_T\in dg,\tau_\dagger>T)
=
\prod_PP_P(\operatorname{Con}(P))m_T(dg),
\]

and conditional on `G_T=g` together with noncemetery survival, the patch variables are independent with their normalized consistent patch laws.

## Why cemetery histories may be removed exactly

The signed typed dual has

\[
H_\dagger=0.
\]

Therefore its Feynman--Kac random variable vanishes identically on every cemetery history. The survival indicator in the weighted factorization removes no nonzero semigroup contribution.

One can equivalently collapse all cemetery histories to a single killed-skeleton atom whose patch contribution is zero.

## Next step

The next theorem is the explicit typed patch representation. The global Feynman--Kac weight must be factored into local patch weights containing:

- the hidden outgoing-branch sign;
- signs of effective empty-target marks;
- the local additive-potential integral;
- the terminal one-site basis factor on end patches.

Only after that exact representation is established will it be meaningful to define generalized patch positivity.
