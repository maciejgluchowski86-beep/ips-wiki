# 003d: bulk/end separation and binary reduction

Date: 2026-08-17

This note executes Parts D--E of Assignment 003. It proves the structural separation required before any later definition of typed patch positivity.

## 1. Strip off the terminal physical factor

For every patch define the **intrinsic local weight**

\[
A_P(\Sigma_P)
=
\epsilon_{\rm out}(P)
\epsilon_{\emptyset}(P)
\exp\left(
\int_{b(P)}^{e(P)\wedge T}
\bar v_{i(P),X_u^P}\,du
\right).
\tag{1.1}
\]

Then the Assignment-003 local weight is simply

\[
w_P(\Sigma_P;\eta)
=
\begin{cases}
A_P(\Sigma_P),&P\text{ bulk},\\
A_P(\Sigma_P)h_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}
\tag{1.2}
\]

Neither `A_P` nor `Con(P)` contains the physical terminal configuration.

## 2. Exact patch descriptor

A finite typed patch is determined, for purposes of its reference law and consistency event, by the following local descriptor:

1. source site `i`;
2. interval length `ell`;
3. initial orientation and typed boundary data:
   - incoming start `I(a)` with incoming type `a`, or
   - outgoing start `O(r,tau)` with revealed pre-source type `r`, typed target `tau`, and hidden-outcome law
     \[
     q_{i,r,\tau}(s)=\frac{|a_{i,r}^s(\tau)|}{\Lambda_{i,r}(\tau)};
     \]
4. terminal orientation and typed boundary data:
   - incoming terminal `I(a_e)` with compatibility condition `X_{e-} in {0,a_e}`;
   - outgoing terminal `O(r_e,tau_e)` with condition `X_{e-}=r_e` (the target `tau_e` is part of the skeleton boundary record although the preceding patch consistency uses only `r_e`);
   - end terminal `E`;
5. the fixed local dual clock rates/signs and local potentials at site `i`.

Because the graphical clocks are time-homogeneous Poisson processes, translating a patch interval in absolute time does not change its reference law. Thus only its length, not its absolute starting time, enters the local contribution.

No state or hidden mark from another source-time strip is needed after these boundary labels are fixed.

## 3. Bulk contribution

For a bulk patch define

\[
\boxed{
C(P)=E_P^{\mathrm{con}}[A_P].}
\tag{3.1}
\]

### Theorem 3.1 (bulk locality)

`C(P)` depends only on the local descriptor in Section 2. In particular it is independent of the terminal physical configuration `eta`.

### Proof

The reference patch law consists only of:

- the independent local Poisson clocks originating at source site `i` in the patch interval;
- for an outgoing start, the hidden source outcome sampled from `q_{i,r,tau}`.

The local recursion `X^P`, the sign factors in (1.1), the potential factor in (1.1), and all three possible finite-terminal consistency conditions are measurable functions of exactly these variables and the typed boundary data in Section 2.

There is no terminal physical factor in (1.2) for a bulk patch. Therefore both numerator

\[
E_P[A_P1_{Con(P)}]
\]

and denominator

\[
P_P(Con(P))
\]

are functions only of the local descriptor. Their ratio (3.1) is independent of `eta`. `square`

This proves the required bulk/end separation on the bulk side; there is no hidden dependence on an end-patch variable.

## 4. End contribution and explicit one-site expansion

For an end patch `P` on site `i`, define for physical one-site value `x in E`

\[
\boxed{
C_T(x,P)
=
E_P^{\mathrm{con}}
\left[A_P h_{X_T^P}(x)\right].}
\tag{4.1}
\]

The reference-state basis satisfies

\[
h_0(x)=1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

Therefore pathwise

\[
h_{X_T^P}(x)
=
1_{\{X_T^P=0\}}
+
\sum_{a\in E_*}
1_{\{X_T^P=a\}}1_{\{x=a\}}.
\tag{4.2}
\]

Set

\[
B_a(P)
=
E_P^{\mathrm{con}}
\left[A_P1_{\{X_T^P=a\}}\right],
\qquad a\in E.
\tag{4.3}
\]

Then

\[
\boxed{
C_T(x,P)
=
B_0(P)
+
\sum_{a\in E_*}B_a(P)1_{\{x=a\}}.}
\tag{4.4}
\]

Thus an end contribution is a one-site function in exactly the same local tensor basis used to construct the dual. It depends on the physical terminal configuration only through

\[
x=\eta_{i(P)}.
\]

Changing any other physical coordinate leaves it unchanged.

Equation (4.4) is the finite-state replacement for the binary statement that the end contribution is affine in the one Bernoulli coordinate.

## 5. Bulk/end semigroup form

Writing the killed-skeleton patch family as

\[
\mathcal P_T(g)=\mathcal B_T(g)\cup\mathcal E_T(g),
\]

Theorem 5.1 of 003c becomes

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_T(g)}C(P)\right)
\left(\prod_{P\in\mathcal E_T(g)}C_T(\eta_{i(P)},P)\right)
\nu_T(dg).}
\tag{5.1}
\]

The first product contains **all intrinsic bulk signed averaging** and no physical terminal data. The second product carries all remaining dependence on `eta`, one end site at a time.

This is exactly the structural separation required by Assignment 003 before a later positivity condition can even be formulated.

## 6. Binary specialization

Take

\[
E=\{0,1\}.
\]

Then typed active configurations are ordinary finite subsets and the only active source type is `1`.

### 6.1 Hidden selected branch

For a nonempty target `S`, the source outcomes are

- `s=0`: source deletion, the canonical death/split branch;
- `s=1`: source survival, the canonical birth branch.

The corresponding signs and absolute rates are exactly the paper's

\[
\sigma_i^\delta(S),\ \delta_i(S),
\qquad
\sigma_i^\beta(S),\ \beta_i(S).
\]

Hence `epsilon_out(P)` is exactly the paper's initial outgoing-boundary sign `sigma(P)`.

### 6.2 Empty-target jumps

The only non-diagonal empty-target branch is source deletion `1->0`. Its coefficient is

\[
a_{i,1}^0(\emptyset)=c_i^0(\emptyset)\ge0,
\]

so its sign is `+`. Therefore

\[
\epsilon_{\emptyset}(P)=1
\]

identically in the binary specialization. These are precisely the binary pure-death marks inside a patch.

### 6.3 Potential

Assignment 001 gives

\[
v_{i,1}
=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\emptyset}}\beta_i(S)
+a_i^\beta(\emptyset)
=V_i
\]

of the canonical paper. Since `bar v_{i,0}=0`,

\[
\exp\left(\int\bar v_{i,X_u^P}\,du\right)
=
\exp\left(V_i\int X_u^P\,du\right).
\]

### 6.4 Terminal factor

For an end patch,

\[
h_{X_T^P}(\eta_i)
=
\eta_i^{X_T^P}.
\]

Consequently (1.2) becomes exactly the paper's

\[
F(P)=\sigma(P)
\exp\left(V_i\int X_u^P\,du\right)
\]

for a bulk patch, and

\[
F(\eta_i,P)=\sigma(P)
\exp\left(V_i\int X_u^P\,du\right)
\eta_i^{X_T^P}
\]

for an end patch.

### 6.5 Outer skeleton law

With only one active type, an incoming nonempty target can never conflict with a different active type. Thus the typed dual has no target-conflict cemetery mechanism, `tau_dagger=infinity` for this purpose, and the noncemetery skeleton measure `nu_T` is just the canonical successful-skeleton law.

Therefore (5.1) reduces mathematically to the canonical binary patch representation, not merely to an analogous formula.

## 7. Exact verifier interfaces

`003-typed-representation-verifier.py` checks the structural claims above in the mandatory `d=3` gate:

- the three bulk weights are unchanged between the two chosen terminal physical configurations;
- each end weight is invariant when the *other* physical coordinate is changed;
- source retyping changes the exact rational potential exponent on the correct subinterval;
- source deletion removes the corresponding later potential integral;
- the separate `d=2` routine compares the typed local weight directly with the canonical binary formula on all eight combinations of hidden selected outcome, optional binary death, and terminal bit.

No instance of `STOP-NO-BULK-END-SEPARATION` occurs.

## 8. Assignment-003 consequence

Parts A--E now have the required structure:

1. one explicit local weight;
2. exact pathwise product;
3. exact killed-skeleton semigroup representation;
4. strict bulk/end separation;
5. exact binary reduction;
6. an exact rational finite gate.

Subject to final report packaging, the registered Assignment-003 outcome is therefore

\[
\boxed{\texttt{CONTINUE-TYPED-POSITIVITY}.}
\]

The next mathematical question is precisely: **for which local finite-state replacement coefficients are all bulk typed patch contributions `C(P)` nonnegative?** No positivity criterion is defined in this note.