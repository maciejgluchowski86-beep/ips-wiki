# 003a: local typed patch Feynman--Kac weight

Date: 2026-08-17

This note executes Part A of Assignment 003. It defines the only local weight used below. No positivity notion is introduced here.

## 1. Fixed typed-dual data

Let

\[
E=\{0,1,\ldots,d-1\},\qquad E_*=E\setminus\{0\}.
\]

The signed typed dual has, for each source site `i`, active source type `r in E_*`, source outcome `s in E`, and typed target `tau`, signed branch coefficient

\[
a_{i,r}^s(\tau),
\]

jump rate

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|,
\]

and sign

\[
\epsilon_{i,r}^s(\tau)=\operatorname{sgn}_{\pm}(a_{i,r}^s(\tau)).
\]

The empty-target source-survival branch `(s,tau)=(r,emptyset)` is omitted from the jump process and inserted in the additive potential. Thus

\[
V(\xi)=\sum_{i\in\operatorname{supp}\xi}v_{i,\xi(i)}.
\]

For notational uniformity define

\[
\bar v_{i,0}=0,\qquad \bar v_{i,r}=v_{i,r}\quad(r\in E_*).
\tag{1.1}
\]

The successful nonempty-target record is

\[
(i,t,r,\tau),
\]

and hides the post-source outcome `s`.

## 2. Typed patch variables

Fix a horizon `T` and an inserted noncemetery candidate skeleton `g`. Let `P` be one induced one-site patch, with source site

\[
i=i(P),
\]

initial time `b(P)`, and terminal time `e(P)`, truncated at `T` when necessary. Write

\[
t_P=e(P)\wedge T.
\]

The local state reconstructed from the patch marks is

\[
X_u^P\in E,\qquad b(P)\le u<t_P,
\]

where `0` means dual-inactive.

The patch variable `Sigma_P` contains:

1. every ordinary local jump clock on source line `i` strictly inside `(b(P),t_P)`;
2. if `P` starts at an outgoing selected record `(i,b(P),r,\tau)`, the hidden source outcome `S_P in E` at that selected point.

At an incoming start carrying type `a`, `X_{b(P)}^P=a`. At an outgoing start, `X_{b(P)}^P=S_P`.

## 3. Selected outgoing-boundary sign

Define

\[
\epsilon_{\rm out}(P)
=
\begin{cases}
1,&P\text{ starts at an incoming boundary},\\
\epsilon_{i,r}^{S_P}(\tau),&P\text{ starts at the outgoing record }(i,b(P),r,\tau).
\end{cases}
\tag{3.1}
\]

Thus the sign of a selected nonempty-target dual jump is assigned to exactly one object: the source patch which starts immediately after that selected interaction.

Incoming target patches carry no copy of this sign.

## 4. Effective empty-target signs

The only jump clocks which can act without producing a successful-skeleton boundary are empty-target clocks

\[
(i,u,r,s,\emptyset),\qquad s\ne r.
\]

Such a mark is **effective in `P`** precisely when

\[
X_{u-}^P=r.
\]

It then updates the local state from `r` to `s` and multiplies the global dual sign by

\[
\epsilon_{i,r}^s(\emptyset).
\]

Define the local empty-target sign product

\[
\epsilon_{\emptyset}(P)
=
\prod_{\substack{(u,r,s,\emptyset)\in\Sigma_P^\circ\\ X_{u-}^P=r}}
\epsilon_{i,r}^s(\emptyset).
\tag{4.1}
\]

Marks with mismatching source type are ignored and contribute no sign. On `Con(P)`, every interior nonempty-target mark also has mismatching source type and therefore contributes no sign.

## 5. Local potential factor

Define

\[
\Phi(P)
=
\exp\left(
\int_{b(P)}^{t_P}
\bar v_{i,X_u^P}\,du
\right).
\tag{5.1}
\]

If a source is deleted, `X^P` becomes `0` and the integrand becomes zero until a later incoming boundary starts a new patch. If an empty-target or selected outgoing branch retypes the source, the integrand changes immediately to the potential of the new type. Boundary times have Lebesgue measure zero, so no convention at a single endpoint affects (5.1).

## 6. Terminal physical factor

For `a in E`, write

\[
h_0\equiv1,\qquad h_a(x)=1_{\{x=a\}}\quad(a\in E_*).
\]

If `P` is an end patch truncated at `T`, define

\[
R_T(P;\eta)=h_{X_T^P}(\eta_i).
\tag{6.1}
\]

If `P` is a bulk patch, define

\[
R_T(P;\eta)=1.
\tag{6.2}
\]

In particular, an end patch with local state `0` contributes terminal factor `1`.

## 7. Local patch weight

The local Feynman--Kac weight is

\[
\boxed{
w_P(\Sigma_P;\eta)
=
\epsilon_{\rm out}(P)\,
\epsilon_{\emptyset}(P)\,
\Phi(P)\,
R_T(P;\eta).}
\tag{7.1}
\]

This formula contains exactly four ingredients:

1. the sign of the selected outgoing branch at the initial boundary, if any;
2. signs of effective empty-target interior jumps;
3. the additive local potential integrated over the patch strip;
4. the one-site terminal tensor factor, only for end patches.

There is no factor associated with an incoming boundary itself. An incoming target merely starts the next local state at its revealed type after compatibility has been checked in the preceding patch's consistency event.

## 8. No-double-counting ledger

On a noncemetery trajectory with successful skeleton `g`:

- every selected nonempty-target jump occurs at exactly one source site and starts exactly one outgoing patch there, so its sign appears exactly once in (3.1);
- the same selected jump may create several incoming target patches, but none carries its branch sign;
- every effective empty-target jump lies strictly inside exactly one source-time patch and appears exactly once in (4.1);
- diagonal empty-target source-survival coefficients are not jump signs at all: they are already included in `v_{i,r}` and hence only in (5.1);
- the one-site patch intervals partition every site-time segment created by the skeleton, up to boundary points of zero Lebesgue measure, so the additive potential is neither omitted nor duplicated;
- at time `T`, distinct end patches lie on distinct sites, and the end states `X_T^P` reproduce the final typed configuration on those sites. Hence each factor in `H_{\xi_T}(\eta)` appears exactly once in (6.1).

These bookkeeping facts are the input for the pathwise product theorem. They do not use conditional independence or the weighted Mecke theorem.

## 9. Binary check at the level of the definition

When `d=2`, the unique active type is `1`.

- hidden selected outcome `0` is source deletion (death/split), while hidden outcome `1` is source survival (birth);
- (3.1) is the binary selected initial-boundary sign;
- the only effective empty-target jump is the binary death, whose coefficient is nonnegative in the canonical paper, so (4.1) is identically `+1` there;
- (5.1) becomes
  \[
  \exp\left(V_i\int X_u^P\,du\right);
  \]
- (6.1) becomes `eta(i)^{X_T^P}`.

Thus (7.1) is exactly the canonical binary local weight, with the extra empty-target sign factor becoming trivial in the binary specialization.