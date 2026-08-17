# 003b: pathwise typed patch product identity

Date: 2026-08-17

This note executes Part B of Assignment 003, using the local weight from `003a-local-typed-patch-weight.md`. The identity is pathwise and precedes every conditional-expectation or Mecke argument.

## 1. Statement

Fix a finite horizon `T` and a realization of the signed typed dual which does not hit cemetery through `T`. Let

\[
G_T=g
\]

be its realized successful typed record list and let `P_T(g)` be the corresponding finite patch family. For every patch `P`, let `w_P` be (7.1) of 003a.

### Theorem 1.1 (pathwise typed patch product)

On every such noncemetery realization,

\[
\boxed{
\sigma_T
\exp\left(\int_0^T V(\xi_u)\,du\right)
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal P_T(g)}
w_P(\Sigma_P;\eta).}
\tag{1.1}
\]

No conditional independence is used in this identity.

## 2. Sign factorization

The signed typed dual changes sign only when an actual non-diagonal graphical jump acts.

There are exactly two possibilities.

### 2.1 Nonempty target

A nonempty-target clock acts precisely when its source type matches the current active source type. On a noncemetery path, every such acting clock is a successful interaction and therefore appears in `g`.

For a selected record

\[
(i,t,r,\tau),
\]

its hidden source outcome is `s`, and the global sign is multiplied by

\[
\epsilon_{i,r}^s(\tau).
\]

The interaction creates exactly one outgoing boundary on source line `i`. The patch starting at that outgoing boundary contains the hidden source outcome and, by definition (3.1) of 003a, contains exactly this sign as `epsilon_out(P)`.

The same interaction may create several incoming target boundaries, but none of those target patches contains a copy of the sign.

Thus every selected nonempty-target jump sign appears exactly once among the outgoing-start patch factors.

### 2.2 Empty target

An empty-target jump clock has index

\[
(i,u,r,s,\emptyset),\qquad s\ne r.
\]

It acts precisely when the local/global source type just before `u` is `r`. Empty-target clocks create no successful-skeleton boundary, so every effective one lies strictly inside the unique current patch on source line `i`. Its sign appears exactly once in the product `epsilon_empty(P)` of that patch.

A mismatching empty-target clock is ignored by the global dual and by the local patch recursion, so it contributes no sign on either side.

The diagonal coefficient `(r,r,emptyset)` is not a jump and has no sign jump; it is already included in the potential.

Since the initial signed state corresponding to `H_{xi_0}` has sign `+`, these two cases exhaust all sign changes and give

\[
\boxed{
\sigma_T
=
\prod_{P\in\mathcal P_T(g)}
\epsilon_{\rm out}(P)\epsilon_{\emptyset}(P).}
\tag{2.1}
\]

## 3. Potential factorization

Recall

\[
V(\xi_u)
=
\sum_{i\in\operatorname{supp}\xi_u}v_{i,\xi_u(i)}
=
\sum_i\bar v_{i,X_i(u)},
\tag{3.1}
\]

where `X_i(u)=0` when site `i` is dual-inactive and `bar v_{i,0}=0`.

The deterministic initial record places an incoming boundary at time zero on every initially active site. Thereafter, a site can become active only at an incoming successful boundary, and every successful record involving the site creates the next patch boundary. Consequently, for every site which is ever relevant through `T`, its patch intervals partition its source-time line from its first activation/boundary through `T`, up to boundary points. Times when the local state is `0` contribute zero by (1.1) of 003a. Sites with no patch and no activity contribute zero to (3.1).

On a noncemetery realization the local reconstruction agrees with the global typed state on each patch strip. Hence Fubini over the finite set of active/relevant site strips gives

\[
\boxed{
\int_0^T V(\xi_u)\,du
=
\sum_{P\in\mathcal P_T(g)}
\int_{b(P)}^{e(P)\wedge T}
\bar v_{i(P),X_u^P}\,du.}
\tag{3.2}
\]

Exponentiating (3.2) gives

\[
\exp\left(\int_0^T V(\xi_u)\,du\right)
=
\prod_P\Phi(P).
\tag{3.3}
\]

The source-type dependence of `v_{i,r}` causes no problem: retyping, survival, and deletion are all already reflected in the piecewise-constant local state `X^P`.

## 4. Terminal tensor factorization

At time `T`, distinct end patches lie on distinct sites. For each end patch on site `i`, its local state equals the global final source-line state:

\[
X_T^P=
\begin{cases}
\xi_T(i),&i\in\operatorname{supp}\xi_T,\\
0,&i\notin\operatorname{supp}\xi_T.
\end{cases}
\]

The reference-state basis has `h_0=1`. Therefore

\[
\boxed{
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal E_T(g)}
h_{X_T^P}(\eta_{i(P)}).}
\tag{4.1}
\]

Bulk patches carry no terminal factor.

## 5. Boundary checks specific to more than two states

The identities above include the cases which do not occur in the binary active-set geometry.

### Idempotent incoming merge

Suppose an incoming target of type `a` reaches a line with `X_{e-}=a`. The merge is idempotent. The preceding patch ends at type `a` and the next incoming-start patch begins at type `a`.

There is no additional sign on the incoming side: the selected branch sign is already assigned at the source outgoing patch. The potential integral is merely split at one time point of Lebesgue measure zero, so it is neither duplicated nor lost.

### Source deletion

If a selected or empty-target branch has outcome `0`, the new local state is inactive. The sign of that jump is still assigned at its unique source patch position, while the potential integrand becomes

\[
\bar v_{i,0}=0.
\]

It remains zero until a later compatible incoming boundary creates a new patch with nonzero type.

### Source retyping

If a branch changes type `r` to `s notin {0,r}`, its sign occurs exactly once at that jump and subsequent potential contribution uses `v_{i,s}` until the next effective local change.

### Incoming activation after inactivity

If a compatible incoming target of type `a` meets `X_{e-}=0`, the preceding patch contributes no potential immediately before the boundary and the next patch begins at type `a`. Again the incoming boundary itself carries no sign.

## 6. Proof of Theorem 1.1

Multiply (2.1), (3.3), and (4.1). By definition (7.1) of 003a, the resulting product is exactly

\[
\prod_{P\in\mathcal P_T(g)}w_P(\Sigma_P;\eta),
\]

which proves (1.1). `square`

## 7. Mandatory finite gate

The exact verifier `003-typed-representation-verifier.py` instantiates the same `d=3` two-record geometry as Assignment 002.

It represents each exponential exactly as the formal object

\[
c\,e^q,
\qquad c\in\{0,+1,-1\},\quad q\in\mathbb Q,
\]

so equality is checked by exact sign/terminal coefficient and exact rational exponent, with no floating-point evaluation.

The chosen potential values are

\[
v_{0,1}=2,\qquad v_{0,2}=5,\qquad v_{1,1}=-3,
\]

and the selected/empty branch signs include negative values. Thus the gate detects both incorrect sign placement and incorrect type-dependent potential segmentation.

The fixed two-record skeleton has five patches. The verifier checks:

- all 32 hidden configurations;
- all 8 incoming-target-conflict configurations;
- two terminal physical configurations;
- 18 direct pathwise identities on the 9 noncemetery exact-two-record hidden configurations;
- 64 killed/weighted representation cells;
- exact zero on every cemetery cell;
- one-copy sign ledgers for both selected outgoing interactions and for the effective empty-target `2->1` retyping;
- bulk independence of terminal physical data and one-site locality of end factors;
- a separate exact binary specialization.

The finite gate therefore gives no instance of `STOP-NONLOCAL-FK-WEIGHT`.