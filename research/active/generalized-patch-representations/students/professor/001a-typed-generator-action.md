# 001a: typed indicator algebra and exact generator action

Date: 2026-08-17

This note executes Parts A--B of Assignment 001. No patch claim is made here.

## 1. Typed tensor basis

Let

\[
E=\{0,1,\ldots,d-1\},
\qquad
E_*=E\setminus\{0\}.
\]

The distinguished state `0` is only a reference state for the algebra. For one site define

\[
h_0\equiv1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

For a finite set `K`, let `T(K)` be the family of typed partial maps

\[
\tau:A\to E_*,
\qquad A\subseteq K.
\]

Write `supp tau=A` and

\[
H_\tau(\eta)=\prod_{j\in A}1_{\{\eta_j=\tau(j)\}}.
\]

There are

\[
\sum_{A\subseteq K}(d-1)^{|A|}=d^{|K|}
\]

such functions, exactly the dimension of the real functions on `E^K`.

They are a basis. More explicitly, for `f:E^K->R` and `tau:A->E_*`, define `z^{tau,B}` for `B subseteq A` by

\[
z_j^{\tau,B}=
\begin{cases}
\tau(j),&j\in B,\\
0,&j\notin B.
\end{cases}
\]

Then the unique coefficient of `H_tau` is

\[
\boxed{
\widehat f(\tau)
=
\sum_{B\subseteq A}(-1)^{|A|-|B|}f(z^{\tau,B}).}
\tag{1.1}
\]

Indeed, if `eta` has nonzero support `R` and `rho=eta|_R`, then

\[
\sum_{A\subseteq R}\widehat f(\rho|_A)=f(\eta)
\]

by ordinary Boolean-lattice Mobius inversion. Hence

\[
f=\sum_{\tau\in T(K)}\widehat f(\tau)H_\tau.
\tag{1.2}
\]

## 2. Compatible merge and the zero state

For typed partial maps `xi,tau`, define `xi sqcup tau` when their labels agree on the overlap, by taking the union. If they disagree at some common site, define

\[
\xi\sqcup\tau=\dagger.
\]

Set

\[
H_\dagger=0.
\]

Then exactly

\[
\boxed{H_\xi H_\tau=H_{\xi\sqcup\tau}.}
\tag{2.1}
\]

Thus the only new algebraic feature relative to binary monomials is a cemetery/zero outcome for incompatible colors. Equal labels remain idempotent.

## 3. General single-site replacement dynamics

Consider

\[
L f(\eta)
=
\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr],
\tag{3.1}
\]

where each rate depends on a finite neighbourhood not containing `i`.

Expand

\[
c_i^{x\to y}
=
\sum_{\tau\in T(N(i))}
\widehat c_i^{x\to y}(\tau)H_\tau.
\tag{3.2}
\]

Fix a typed active configuration `xi` and a site `i in supp xi`. Put

\[
r=\xi(i),
\qquad
\xi^{-i}=\xi|_{\operatorname{supp}\xi\setminus\{i\}}.
\]

If `i notin supp xi`, the site contributes zero to `L H_xi`.

For `i in supp xi`, only physical transitions into or out of the color `r` matter. Directly,

\[
\begin{aligned}
&\sum_{x\ne y}1_{\{\eta_i=x\}}c_i^{x\to y}
\bigl[h_r(y)-h_r(x)\bigr]
\\
&\qquad=
1_{\{\eta_i=0\}}c_i^{0\to r}
+
\sum_{s\in E_*\setminus\{r\}}
1_{\{\eta_i=s\}}c_i^{s\to r}
-
1_{\{\eta_i=r\}}\sum_{y\ne r}c_i^{r\to y}.
\end{aligned}
\tag{3.3}
\]

Using

\[
1_{\{\eta_i=0\}}=1-\sum_{s\in E_*}h_s(\eta_i),
\tag{3.4}
\]

this becomes one branch for each possible **dual source outcome** `s in E`.

For `tau in T(N(i))`, define

\[
\boxed{
a_{i,r}^{0}(\tau)
=\widehat c_i^{0\to r}(\tau),}
\tag{3.5}
\]

\[
\boxed{
a_{i,r}^{s}(\tau)
=\widehat c_i^{s\to r}(\tau)
-
\widehat c_i^{0\to r}(\tau),
\qquad s\in E_*\setminus\{r\},}
\tag{3.6}
\]

and

\[
\boxed{
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)
-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).}
\tag{3.7}
\]

Interpret `s=0` as deleting the active source. For `s in E_*`, interpret `s` as leaving the source active with type `s`.

Define the local typed map

\[
\Theta_{i;s,\tau}(\xi)
=
\begin{cases}
\bigl(\xi^{-i}\cup\{i\mapsto s\}\bigr)\sqcup\tau,&s\ne0,\\
\xi^{-i}\sqcup\tau,&s=0,
\end{cases}
\tag{3.8}
\]

with the convention that an incompatible merge is `dagger`.

Then the exact generator action is

\[
\boxed{
L H_\xi
=
\sum_{i\in\operatorname{supp}\xi}
\sum_{\tau\in T(N(i))}
\sum_{s\in E}
 a_{i,\xi(i)}^{s}(\tau)
 H_{\Theta_{i;s,\tau}(\xi)}.}
\tag{3.9}
\]

### Proof

Equation (3.3) is the exact one-site difference because `h_r(y)-h_r(x)` is nonzero precisely for transitions entering or leaving `r`. Equation (3.4) separates the reference-state predecessor into the constant branch and one negative branch for every non-reference source type. This gives (3.5)--(3.7). Expanding each rate by (3.2), multiplying by `H_{xi^{-i}}`, and using (2.1) gives (3.9).

No coefficient in (3.5)--(3.7) depends on the rest of `xi`. All dependence on an already active target is through the deterministic compatible-merge map (3.8).

## 4. Structural interpretation

The binary death/split versus birth dichotomy becomes a finite **source-outcome mark**:

- `s=0`: source deletion;
- `s=r`: source survival;
- `s in E_*\{r}`: source retyping.

The neighbour mark `tau` is a typed target rather than an untyped subset.

The formula already shows why `d>2` is not obtained by simply replacing subsets with colored subsets: transitions `s->r` produce genuine retyping branches with coefficient

\[
\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau).
\]

The next checkpoint is to turn (3.9) into fixed signed Poisson clocks and verify it exhaustively at `d=3`.
