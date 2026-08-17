# Assignment 003 report: explicit typed patch representation

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

This report closes Assignment 003. It proves the exact finite-horizon patch representation for the finite-state typed dual, including the required bulk/end separation. It deliberately does **not** define generalized patch positivity.

## 1. Local weight

For a typed patch `P` on source site `i`, let

\[
A_P
=
\epsilon_{\rm out}(P)
\epsilon_{\emptyset}(P)
\exp\left(
\int_{b(P)}^{e(P)\wedge T}
\bar v_{i,X_u^P}\,du
\right),
\]

where

- `epsilon_out(P)` is `1` at an incoming start and is the hidden selected source-branch sign at an outgoing start;
- `epsilon_empty(P)` is the product of signs of all **effective** empty-target jumps in the patch interior;
- `bar v_{i,0}=0` and `bar v_{i,r}=v_{i,r}` for active type `r`.

The full patch weight is

\[
\boxed{
w_P(\Sigma_P;\eta)
=
\begin{cases}
A_P,&P\text{ bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}}
\tag{1.1}
\]

No incoming boundary carries a second copy of the selected branch sign.

Decisive note: `003a-local-typed-patch-weight.md`, commit `992552ca`.

## 2. Pathwise product theorem

On every noncemetery realization through `T`,

\[
\boxed{
\sigma_T
\exp\left(\int_0^TV(\xi_u)\,du\right)
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal P_T(G_T)}w_P(\Sigma_P;\eta).}
\tag{2.1}
\]

The proof has three independent ledgers.

### Signs

Every acting nonempty-target jump is a selected successful record on a noncemetery path. Its sign belongs to the unique outgoing-start patch at its source. Every acting empty-target jump lies strictly inside one source-time patch. These exhaust sign changes of the signed dual.

### Potential

The additive potential

\[
V(\xi)=\sum_{i\in\operatorname{supp}\xi}v_{i,\xi(i)}
\]

splits over the one-site patch intervals. Source deletion sets the local integrand to zero; source retyping switches it to the new type potential. Patch boundaries themselves have zero Lebesgue measure.

### Terminal tensor factor

End patches lie on distinct sites and their final local states reproduce the final typed configuration, with inactive state `0` contributing `h_0=1`. Thus

\[
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal E_T}h_{X_T^P}(\eta_{i(P)}).
\]

Decisive note: `003b-pathwise-typed-patch-product.md`, commit `1f58d2f3`.

## 3. Exact semigroup representation

Assignment 001 gives the Feynman--Kac duality

\[
P_TH_{\xi_0}(\eta)
=E\left[
\sigma_Te^{\int_0^TV(\xi_u)du}H_{\xi_T}(\eta)
\right].
\]

Since `H_dagger=0`, cemetery paths have exact weight zero. Combining (2.1) with Assignment 002's **weighted/killed** Mecke identity gives

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}
E_P\left[w_P(\Sigma_P;\eta)1_{Con(P)}\right]
\,m_T(dg).}
\tag{3.1}
\]

Here

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_1\cdots dt_n.
\]

Let

\[
\nu_T(dg)
=
\prod_PP_P(Con(P))m_T(dg)
=P(G_T\in dg,\tau_\dagger>T)
\]

and

\[
C_P(\eta)=E_P^{con}[w_P(\Sigma_P;\eta)].
\]

Then

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).}
\tag{3.2}
\]

Equivalently, collapse all cemetery histories to one outer skeleton atom and assign that atom contribution zero.

The false bare conditional independence from Assignment 002 is **not** used anywhere in (3.1)--(3.2).

Decisive note: `003c-exact-typed-semigroup-representation.md`, commit `6eebcaa5`.

## 4. Bulk/end separation

For a bulk patch,

\[
\boxed{C(P)=E_P^{con}[A_P].}
\tag{4.1}
\]

It depends only on:

- source site;
- interval length;
- incoming/outgoing boundary orientations;
- typed boundary labels;
- local branch rates/signs and local potentials.

It is independent of the terminal physical configuration.

For an end patch on site `i`,

\[
C_T(x,P)
=E_P^{con}[A_Ph_{X_T^P}(x)].
\]

Writing

\[
B_a(P)=E_P^{con}[A_P1_{\{X_T^P=a\}}],
\qquad a\in E,
\]

gives the explicit one-site formula

\[
\boxed{
C_T(x,P)
=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}}.}
\tag{4.2}
\]

Hence

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_T(g)}C(P)\right)
\left(\prod_{P\in\mathcal E_T(g)}C_T(\eta_{i(P)},P)\right)
\nu_T(dg).}
\tag{4.3}
\]

This proves the precise bulk/end separation pre-registered in Assignment 003. Therefore `STOP-NO-BULK-END-SEPARATION` does not occur.

Decisive note: `003d-bulk-end-separation-and-binary-reduction.md`, commit `4f9c250b`.

## 5. Mandatory exact `d=3` gate

Verifier:

`003-typed-representation-verifier.py`, commit `50f28f62`.

It uses the same two-record geometry as Assignment 002 and exact symbolic Feynman--Kac weights `c exp(q)` with rational `q`; exponentials are never numerically evaluated.

The test uses exact potentials

\[
v_{0,1}=2,\qquad v_{0,2}=5,\qquad v_{1,1}=-3,
\]

and nontrivial negative selected/empty-target signs.

The script checks:

- 32 hidden `d=3` configurations;
- 8 incoming-target-conflict configurations;
- two physical terminal configurations;
- 18 pathwise identities on the 9 noncemetery exact-two-record histories;
- 16 cemetery-by-terminal exact-zero checks;
- 64 killed/weighted representation cells;
- 128 selected outgoing sign-ledger checks;
- 16 effective empty-target retyping sign checks;
- 32 bulk terminal-data independence checks;
- 128 end one-site locality checks;
- exact rational potential segmentation under retyping and deletion;
- 8 separate `d=2` typed/binary specialization checks.

No float or Monte Carlo arithmetic is used.

## 6. Exact binary reduction

At `d=2`:

- source outcome `0` is death/split;
- source outcome `1` is birth/survival;
- `epsilon_out(P)` is exactly the canonical binary initial-boundary sign;
- the only empty-target acting jump is binary death and has positive coefficient `c_i^0(emptyset)`, so `epsilon_empty(P)=1`;
- `v_{i,1}` is exactly the paper's `V_i`;
- the end factor is `eta_i^{X_T^P}`.

Thus (1.1) is the canonical binary patch weight.

There is also no typed-target conflict in the binary case, because there is only one active type. Hence the noncemetery skeleton submeasure is the ordinary successful-skeleton law and (4.3) becomes the canonical patch representation itself.

## 7. Registered outcome

All five load-bearing requirements pass:

1. explicit local patch weight;
2. pathwise product identity;
3. exact killed-skeleton semigroup representation;
4. bulk/end separation;
5. exact binary specialization and mandatory finite gate.

Therefore Assignment 003 ends

\[
\boxed{\texttt{CONTINUE-TYPED-POSITIVITY}.}
\]

The next question is now well-posed and strictly local:

> Characterize, or find a useful coefficient-level sufficient condition for, nonnegativity of **every bulk typed patch contribution** `C(P)` for finite-state single-site replacement dynamics.

No positivity condition is asserted in Assignment 003, and no novelty claim has yet been made for the generalized representation theorem.