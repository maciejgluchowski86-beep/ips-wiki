# 003c: exact typed patch semigroup representation

Date: 2026-08-17

This note executes Part C of Assignment 003. It combines the pathwise identity of 003b with the **killed/noncemetery** weighted factorization of Assignment 002. It does not use the false bare conditional factorization given only the coarse record list.

## 1. Feynman--Kac variable

For finite typed initial state `xi_0`, define

\[
W_T(\eta)
=
\sigma_T
\exp\left(\int_0^T V(\xi_u)\,du\right)
H_{\xi_T}(\eta).
\tag{1.1}
\]

Assignment 001 gives, under the stated Feynman--Kac integrability hypothesis,

\[
P_TH_{\xi_0}(\eta)=E_{\xi_0}[W_T(\eta)].
\tag{1.2}
\]

Since `H_dagger=0`,

\[
W_T(\eta)
=
1_{\{\tau_\dagger>T\}}W_T(\eta).
\tag{1.3}
\]

Thus cemetery histories are exactly zero, not an approximation or discarded error term.

## 2. Insert the pathwise patch product

On `{tau_dagger>T}`, Theorem 1.1 of 003b gives

\[
W_T(\eta)
=
\prod_{P\in\mathcal P_T(G_T)}w_P(\Sigma_P;\eta).
\tag{2.1}
\]

Combining (1.2)--(2.1),

\[
P_TH_{\xi_0}(\eta)
=
E_{\xi_0}\left[
1_{\{\tau_\dagger>T\}}
\prod_{P\in\mathcal P_T(G_T)}w_P(\Sigma_P;\eta)
\right].
\tag{2.2}
\]

The signed product in (2.2) is integrable because its absolute value equals the absolute value of the Feynman--Kac variable on noncemetery paths and vanishes on cemetery paths. This is exactly the signed-integrable regime allowed by Theorem 2.1 of `002c-weighted-typed-patch-factorization.md`.

## 3. Reference record measure

For a chronological typed candidate record list

\[
g=((i_k,t_k,r_k,\tau_k))_{k=1}^n,
\qquad 0<t_1<\cdots<t_n\le T,
\]

with nonempty targets, recall

\[
\Lambda_{i,r}(\tau)
=
\sum_{s\in E}|a_{i,r}^s(\tau)|
\]

and the inserted-record measure

\[
m_T(dg)
=
\prod_{k=1}^n\Lambda_{i_k,r_k}(\tau_k)
\,dt_1\cdots dt_n,
\tag{3.1}
\]

summed over the discrete record labels. Lists incompatible with any noncemetery typed history simply acquire zero local consistency mass.

## 4. Unnormalized exact representation

Apply the weighted Mecke identity of Assignment 002 to (2.2), with `h=1` and `f_P=w_P`. This yields the first exact typed patch representation.

### Theorem 4.1 (unnormalized typed patch representation)

For every finite typed initial state, horizon `T`, and terminal physical configuration `eta`,

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}
E_P\left[
 w_P(\Sigma_P;\eta)
 1_{\operatorname{Con}(P)}
\right]
\,m_T(dg).}
\tag{4.1}
\]

This is an equality of the physical semigroup with a product of **one-patch unnormalized expectations** integrated over typed successful-record lists.

The cemetery coupling discovered in Assignment 002 is absent from (4.1) only because its exact zero factor `1_{tau_dagger>T}` has been included before Mecke factorization.

## 5. Normalized consistent contributions

For a patch with positive consistency probability define

\[
P_P^{\mathrm{con}}(\cdot)
=P_P(\cdot\mid\operatorname{Con}(P))
\]

and

\[
\boxed{
C_P(\eta)
=E_P^{\mathrm{con}}[w_P(\Sigma_P;\eta)].}
\tag{5.1}
\]

Assignment 002 gives the noncemetery skeleton submeasure

\[
\nu_T(dg)
=P(G_T\in dg,\tau_\dagger>T)
=
\prod_{P\in\mathcal P_T(g)}P_P(\operatorname{Con}(P))
\,m_T(dg).
\tag{5.2}
\]

On a `nu_T`-null skeleton there is no need to define normalized contributions. On its support every patch consistency probability is positive.

Since

\[
E_P[w_P1_{Con(P)}]
=P_P(Con(P))C_P(\eta),
\]

formula (4.1) becomes:

### Theorem 5.1 (normalized killed-skeleton representation)

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}C_P(\eta)
\,\nu_T(dg).}
\tag{5.3}
\]

This is the direct finite-state analogue of replacing every hidden patch variable by its consistent patch expectation, except that the outer skeleton law is the **noncemetery submeasure** rather than the bare successful-skeleton law.

## 6. Cemetery-atom formulation

It is sometimes cleaner to work with a genuine probability-valued outer variable. Define

\[
\widehat G_T
=
\begin{cases}
G_T,&\tau_\dagger>T,\\
\dagger,&\tau_\dagger\le T.
\end{cases}
\]

Its law consists of `nu_T` on ordinary record lists plus one cemetery atom of mass

\[
P(\tau_\dagger\le T).
\]

Define the outer patch functional to be zero at that atom:

\[
\mathcal C_T(\dagger;\eta)=0,
\]

and for ordinary `g`,

\[
\mathcal C_T(g;\eta)
=
\prod_{P\in\mathcal P_T(g)}C_P(\eta).
\]

Then (5.3) is equivalently

\[
\boxed{
P_TH_{\xi_0}(\eta)
=E[\mathcal C_T(\widehat G_T;\eta)].}
\tag{6.1}
\]

This formulation preserves the intuitive statement that the semigroup is an expectation over a coarse skeleton, while making the cemetery branch explicit instead of pretending that ordinary bare-skeleton conditional independence holds there.

## 7. Integrability and locality comments

For a fixed finite patch interval, the local type potential `bar v_{i,a}` is bounded over the finite state set and the sign/terminal factors have absolute value at most one. Hence every individual `w_P` is integrable under its reference patch law.

The global integrability needed to pass from the signed dual to (1.2) is exactly the Assignment-001 Feynman--Kac hypothesis; no stronger moment assumption is introduced by the patch representation.

All randomness inside the expectation in (4.1) is local to one source-time strip, plus the selected hidden source outcome when the patch starts outgoing. Cross-patch dependence survives only in the outer record list `g` and in the cemetery atom, as intended.

## 8. What remains before positivity

The representation theorem itself is now exact. Assignment 003 still requires a separate structural proof that:

1. every bulk contribution is independent of terminal physical data and is determined by finite typed boundary data, interval length, site, and local dual coefficients;
2. every end contribution depends on `eta` only through the one-site terminal basis factor;
3. the `d=2` specialization is mathematically the canonical binary patch weight.

Only if all three hold does the registered outcome permit moving to a later characterization of nonnegative **bulk** typed patch contributions.