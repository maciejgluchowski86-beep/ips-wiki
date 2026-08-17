# 009b: exact typed specialization of the two-stage contact process

Date: 2026-08-17

This note executes Part B of Assignment 009 for the model selected independently in `009a-literature-driven-model-selection.md`.

## 1. Physical generator and reference state

Use local states

\[
E=\{0,1,2\}
\]

with

- `0`: vacant;
- `1`: juvenile;
- `2`: adult.

The reference state is `0`. This is canonical for the indicator tensor basis because vacancy is the state against which the neighbour-dependent birth rate is expanded, and it agrees with the natural absorbing state of the growth process.

For site `i` with finite neighbour set `N(i)`, the nonzero physical replacement rates are

\[
c_i^{0\to1}(\eta_{N(i)})
=\lambda\sum_{j\in N(i)}1_{\{\eta_j=2\}},
\tag{1.1}
\]

\[
c_i^{1\to0}=1+\delta,
\qquad
c_i^{1\to2}=\gamma,
\qquad
c_i^{2\to0}=1,
\tag{1.2}
\]

with

\[
\lambda,\gamma,\delta\ge0.
\]

Every other `c_i^{x->y}` is zero.

## 2. Typed tensor coefficients of the physical rates

Write

\[
\tau_j=\{j\mapsto2\},\qquad j\in N(i).
\]

Since (1.1) is linear in the type-2 neighbour indicators, its only nonzero nonempty tensor coefficients are

\[
\widehat c_i^{0\to1}(\tau_j)=\lambda.
\tag{2.1}
\]

There are no higher-order target coefficients.

The constant coefficients are

\[
\widehat c_i^{1\to0}(\emptyset)=1+\delta,
\qquad
\widehat c_i^{1\to2}(\emptyset)=\gamma,
\qquad
\widehat c_i^{2\to0}(\emptyset)=1.
\tag{2.2}
\]

## 3. Exact dual coefficient table

For active source type `r`, Assignment 001 gives

\[
a_r^0(\tau)=\widehat c^{0\to r}(\tau),
\]

\[
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau),
\qquad s\in E_*\setminus\{r\},
\]

\[
a_r^r(\tau)
=-\widehat c^{0\to r}(\tau)
-\sum_{y\ne r}\widehat c^{r\to y}(\tau).
\]

### Empty target

For source type `1`,

\[
\boxed{
\mathbf a_{1,\emptyset}
=(0,-(1+\delta+\gamma),0).}
\tag{3.1}
\]

For source type `2`,

\[
\boxed{
\mathbf a_{2,\emptyset}
=(0,\gamma,-1).}
\tag{3.2}
\]

Thus the exact signed interior transfer is

\[
\boxed{
K=
\begin{pmatrix}
0&0&0\\
0&-(1+\delta+\gamma)&0\\
0&\gamma&-1
\end{pmatrix}.}
\tag{3.3}
\]

The physical interpretation of the off-diagonal entry `K(2,1)=gamma` is the backward typed effect of forward juvenile maturation `1->2`.

### Nonempty target

For each neighbour `j`, only source type `1` has a nonzero row:

\[
\boxed{
\mathbf a_{1,\tau_j}
=(\lambda,-\lambda,-\lambda).}
\tag{3.4}
\]

Every nonempty row with source type `2` is zero.

The direct generator check for (3.4) is

\[
\lambda
\left(
H_{\tau_j}
-H_{\{i\mapsto1\}\cup\tau_j}
-H_{\{i\mapsto2\}\cup\tau_j}
\right)
\]

\[
=\lambda\,1_{\{\eta_j=2\}}
\left(1-1_{\{\eta_i=1\}}-1_{\{\eta_i=2\}}\right)
\]

\[
=\lambda\,1_{\{\eta_i=0\}}1_{\{\eta_j=2\}},
\tag{3.5}
\]

which is exactly the forward `0->1` contribution to the indicator observable `1_{eta_i=1}`.

Similarly, (3.2) gives

\[
\gamma 1_{\{\eta_i=1\}}-1_{\{\eta_i=2\}},
\]

which is exactly the action of `1->2` at rate `gamma` and `2->0` at rate one on `1_{eta_i=2}`.

## 4. Successful records and hidden outcome

For `lambda>0`, each nonempty row (3.4) has coarse successful rate

\[
\Lambda_{1}(\tau_j)
=|\lambda|+|-\lambda|+|-\lambda|
=3\lambda.
\tag{4.1}
\]

Hence every successful record has the form

\[
\boxed{(i,t,1,\tau_j),\qquad \tau_j=\{j\mapsto2\}.}
\tag{4.2}
\]

It reveals:

- source site `i`;
- record time `t`;
- pre-source active type `1`;
- target neighbour `j` with target type `2`;

and hides the post-source outcome

\[
S\in\{0,1,2\}.
\]

Conditional on the selected record, the three outcomes have equal reference probabilities `1/3`, with signs

\[
+1,-1,-1
\]

respectively.

This is a genuinely nonbinary hidden mark: the selected record does not merely hide source survival versus deletion, but distinguishes deletion, persistence as juvenile, and retyping to adult.

## 5. Realizable cemetery conflict

An incoming selected record places target type `2` on its target patch. The terminal compatibility condition on that patch is therefore

\[
X_{e-}\in\{0,2\}.
\]

If instead

\[
X_{e-}=1,
\]

the incoming type-2 target conflicts with an existing type-1 active label and the global typed dual enters cemetery.

This conflict is realizable. Type `1` may be present on the target patch because:

1. the initial typed observable may carry type `1` there;
2. an earlier selected successful record at that site may choose hidden outcome `S=1`;
3. an empty-target dual transition from type `2` to type `1` occurs at rate `gamma` by (3.2).

Therefore the cemetery-aware killed factorization is not vacuous in this application.

## 6. Realized patch boundary types

The selected model realizes the following local boundary data.

### Incoming starts

At time zero, an initial typed observable may start a patch with type `1` or `2`.

### Outgoing starts

Every selected record starts the post-record source patch with hidden state

\[
S\in\{0,1,2\}.
\]

### Incoming terminals

Every incoming selected target carries type `2`.

### Outgoing terminals

Every outgoing selected record requires pre-source type `1`.

Thus the realized bulk orientations use only incoming-terminal label `2` and outgoing-terminal source label `1`; the artificial boundary-complete family from Assignments 005--007 is not imposed here.

## 7. Exact-rate gate point

For the mandatory finite gate, a convenient interior physical parameter point is

\[
\boxed{\lambda=1,\qquad\gamma=1,\qquad\delta=1.}
\tag{7.1}
\]

All physical replacement rates are nonnegative and all genuinely three-state mechanisms are active:

- adult-driven birth `0->1`;
- juvenile maturation `1->2`;
- juvenile death `1->0`;
- adult death `2->0`.

No transition structure has been changed from the published model.
