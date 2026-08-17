# 011a: unnormalized killed patch-variation envelope

Date: 2026-08-17

## 1. Finite-volume signed and raw-absolute kernels

Fix a finite physical volume, so the compatible typed-dual state space `X` is finite. Cemetery is denoted `dagger` and is assigned zero duality function.

For compatible typed states `xi,zeta in X`, define the exact signed Feynman--Kac kernel

\[
Q_t(\xi,\zeta)
=E_\xi\left[
\sigma_t e^{\int_0^tV(\xi_u)du}
1_{\{\tau_\dagger>t\}}1_{\{\xi_t=\zeta\}}
\right].
\tag{1.1}
\]

Define its raw absolute-FK majorant

\[
A_t(\xi,\zeta)
=E_\xi\left[
e^{\int_0^tV(\xi_u)du}
1_{\{\tau_\dagger>t\}}1_{\{\xi_t=\zeta\}}
\right].
\tag{1.2}
\]

The exponential is positive even when `V` is negative. Thus `A_t` is a positive kernel and trivially

\[
|Q_t(\xi,\zeta)|\le A_t(\xi,\zeta).
\]

The point of this block is to insert the killed-patch grouping strictly between these two objects.

## 2. Skeleton contribution with terminal typed state fixed

Fix a candidate successful skeleton `g`. The terminal-state event `xi_t=zeta` is local over end patches: each end patch is required to end in the type prescribed by `zeta` at its site, while sites absent from `zeta` are required to be inactive.

For each bulk patch let

\[
F_P=E_P[A_P1_{Con(P)}],
\]

and for each end patch let

\[
F_{P,\zeta}
=E_P[A_P1_{Con(P)}1_{\{X_t^P=\zeta(i(P))\}}],
\]

where `zeta(i)=0` means the source line is inactive at time `t`.

Assignment 003's pathwise product identity and Assignment 002's killed weighted-Mecke theorem give

\[
Q_t(\xi,\zeta)
=\int \Phi_t(g;\xi,\zeta)m_t(dg),
\tag{2.1}
\]

with

\[
\Phi_t(g;\xi,\zeta)
=\prod_{P\in\mathcal B_t(g)}F_P
\prod_{P\in\mathcal E_t(g)}F_{P,\zeta}.
\tag{2.2}
\]

Impossible skeletons or incompatible terminal assignments have zero factor automatically.

## 3. Patch-variation kernel

Define

\[
\boxed{
R_t(\xi,\zeta)
:=\int |\Phi_t(g;\xi,\zeta)|m_t(dg)
=\int
\prod_{P\in\mathcal B_t(g)}|F_P|
\prod_{P\in\mathcal E_t(g)}|F_{P,\zeta}|
\,m_t(dg).}
\tag{3.1}
\]

This is the positive envelope obtained by delaying absolute values until **after each entire hidden patch history has been averaged**.

The first inequality is immediate:

\[
\boxed{|Q_t(\xi,\zeta)|\le R_t(\xi,\zeta).}
\tag{3.2}
\]

No normalized consistency denominator appears.

## 4. Exact comparison with raw absolute FK

For a bulk patch define

\[
G_P=E_P[|A_P|1_{Con(P)}],
\]

and for an end patch

\[
G_{P,\zeta}
=E_P[|A_P|1_{Con(P)}1_{\{X_t^P=\zeta(i(P))\}}].
\]

By the ordinary triangle inequality,

\[
|F_P|\le G_P,
\qquad
|F_{P,\zeta}|\le G_{P,\zeta}.
\tag{4.1}
\]

Hence

\[
R_t(\xi,\zeta)
\le
\int
\prod_{P\in\mathcal B_t(g)}G_P
\prod_{P\in\mathcal E_t(g)}G_{P,\zeta}
\,m_t(dg).
\tag{4.2}
\]

Now apply the same killed weighted-Mecke identity as in Assignment 002, but to the nonnegative local patch variables `|A_P|` together with the end-state indicators. On every noncemetery path,

\[
\prod_P|A_P|
=e^{\int_0^tV(\xi_u)du};
\]

all branch signs disappear and the potential remains unchanged. Therefore the right-hand side of (4.2) is exactly (1.2):

\[
\boxed{R_t(\xi,\zeta)\le A_t(\xi,\zeta).}
\tag{4.3}
\]

Combining (3.2) and (4.3),

\[
\boxed{|Q_t|\le R_t\le A_t\quad\text{entrywise}.}
\tag{4.4}
\]

This is an exact finite-volume theorem.

## 5. Cemetery is essential but causes no gap

The proof does not condition on the bare coarse record list. Both (2.1) and (4.2) use the weighted identity

\[
E\left[1_{\{\tau_\dagger>t\}}\prod_Pf_P\right]
=\int\prod_PE_P[f_P1_{Con(P)}]m_t(dg).
\]

Thus the same cemetery event that invalidates bare conditional independence is already incorporated on both sides. Cemetery histories contribute zero to `Q_t`, `R_t`, and the killed raw absolute envelope `A_t`.

## 6. Physical-semigroup norm consequence

Since

\[
P_tH_\xi(\eta)
=\sum_{\zeta\in X}Q_t(\xi,\zeta)H_\zeta(\eta),
\]

and `H_zeta(eta) in {0,1}`,

\[
|P_tH_\xi(\eta)|
\le\sum_\zeta R_t(\xi,\zeta)H_\zeta(\eta)
\le (R_t\mathbf1)(\xi).
\tag{6.1}
\]

Thus `R_t` is a genuine positive coefficient/norm majorant lying below the raw absolute FK kernel. Whether this improvement survives time concatenation and yields a useful contraction is deferred to Parts C--D; (4.4) alone is not counted as a continuation result.