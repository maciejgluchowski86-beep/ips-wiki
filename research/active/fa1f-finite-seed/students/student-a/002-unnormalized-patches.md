# Student A 002: unnormalized hard-FA patch skeleton

## Verdict

The unnormalized successful-skeleton expansion is exact and particularly simple for one-dimensional hard FA-1f. Restoring the patch consistency probabilities does expose factors of order `exp(-Delta)`, and the full one-record contribution to the single-vacancy deviation has a strictly smaller **same-source chain** renewal mass than the chain-only normalized picture suggests.

That apparent gain does **not** survive the complete first branching composition. Once the two target descendants and the possibility that the next successful record is sourced by either descendant are included, the missing same-source mass is exactly rerouted into the child-source sector. In the natural `h`-weighted coefficient norm the full transfer has mass exactly one.

More strongly, after every end factor is expanded about the equilibrium density `p` and the coefficient of each centered monomial is collected, the full unnormalized patch expansion is exactly the verified `h`-transform semigroup from E1:

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B),
$$

where `K_t(A,B)` is the centered-monomial coefficient produced by the patch expansion and `Q_t=e^{t\mathcal G}` is the Markov semigroup of Assignment 001. Thus the recovered consistency probabilities do not create an additional global geometric loss that was hidden by normalization. They give a different decomposition of the same conservative positive coefficient dynamics.

This is a decisive negative result for the proposed E2 mechanism. The chain-only loss is real inside one routing sector, but it is not a contraction of the full target transfer. Any continuation of the patch strategy would need genuinely spatial one-dimensional information beyond the local unnormalized weights -- recurrence, overlap/coalescence, a regeneration structure, or another mechanism that is not already E1 in different coordinates.

The calculation does **not** reproduce the forbidden Bernoulli-quench absolute-sibling argument. No use is made of `|a|=p/q` to contract two signed siblings. The obstruction here is different and stronger: the complete unnormalized centered transfer is a conservative Markov transfer after the already verified `h`-transform. The old sibling boundary remains in force, but it is not the reason this E2 test fails.

## 1. Exact unnormalized Mecke representation

Fix a finite initial dual-active set `A`. For a candidate successful skeleton

$$
g=((i_k,t_k,N(i_k)))_{k=1}^n,
\qquad
0<t_1<\cdots<t_n<t,
$$

write `P_t(g)` for the finite-horizon patch family determined by the initial record and these ordinary records. As in the proof of Theorem 4.4, the discrete source list is restricted by

$$
i_k\in A\cup\bigcup_{\ell<k}N(i_\ell),
$$

which is the necessary reachability condition before consistency is imposed. For hard FA-1f there is only one nonempty target at each source, namely

$$
N(i)=\{i-1,i+1\}.
$$

For a bulk patch put

$$
\widehat C(P)
=
\mathbf E_P\left[F(P)\mathbf 1_{\operatorname{Con}(P)}\right],
$$

and for an end patch at horizon `t`,

$$
\widehat C(z,P)
=
\mathbf E_P\left[F(z,P)\mathbf 1_{\operatorname{Con}(P)}\right].
$$

The Mecke identity in the proof of Theorem 4.4 gives directly, before taking any Radon--Nikodym quotient,

$$
P_t\chi_A(\eta)
=
\sum_{n\geq0}
\sum_{(i_1,\ldots,i_n)}
\int_{0<t_1<\cdots<t_n<t}
\prod_{P\in\mathcal B_t(g)}\widehat C(P)
\prod_{P\in\mathcal E_t(g)}\widehat C(\eta(i(P)),P)
\,m_t(dg),
\tag{1}
$$

where

$$
m_t(dg)
=
\prod_{k=1}^n
\bigl(\delta_{i_k}(N(i_k))+\beta_{i_k}(N(i_k))\bigr)
\,dt_1\cdots dt_n.
\tag{2}
$$

There is no additional consistency factor in `m_t`. It is already contained in every `widehat C`. Conversely there is no denominator in (1): the conditional normalizers from the usual patch representation are precisely what has been put back into the local amplitudes.

To see (1) directly from the paper, apply the multivariate Mecke formula to the pathwise factorization of the Feynman--Kac random variable and take `f_P=F(P)` or `F(eta(i(P)),P)`. The integrand in the Mecke formula is then

$$
\prod_P
\mathbf E_P\left[f_P(\Sigma_P)\mathbf 1_{\operatorname{Con}(P)}\right],
$$

which is exactly the product in (1). Taking `f_P=1` instead gives the skeleton marginal

$$
\mathbf P_A(G_t\in dg)
=
\prod_{P\in\mathcal P_t(g)}
\mathbf P_P(\operatorname{Con}(P))\,m_t(dg),
$$

and dividing these two formulas is the normalized representation. Thus (1) is the same Mecke/Radon--Nikodym calculation before the division.

## 2. Hard FA-1f signed-dual data

Write `p=1-q`. In one-dimensional hard FA-1f the only nonzero multilinear rate coefficients are

$$
c^0(\varnothing)=p,
\qquad
c^1(\varnothing)=q,
\qquad
c^0(N)=-p,
\qquad
c^1(N)=-q,
\tag{3}
$$

with `N={-1,+1}` relative to the source. Therefore

$$
a^\delta(\varnothing)=p,
\qquad
\delta(\varnothing)=p,
\qquad
\sigma^\delta(\varnothing)=+,
\tag{4}
$$

$$
a^\delta(N)=-p,
\qquad
\delta(N)=p,
\qquad
\sigma^\delta(N)=-,
\tag{5}
$$

and

$$
a^\beta(N)=-c^0(N)-c^1(N)=1,
\qquad
\beta(N)=1,
\qquad
\sigma^\beta(N)=+.
\tag{6}
$$

The empty-target birth coefficient is not a jump:

$$
a^\beta(\varnothing)
=-c^0(\varnothing)-c^1(\varnothing)
=-1.
\tag{7}
$$

Hence the total outgoing marked rate and Feynman--Kac potential per active site are

$$
\alpha
=
\delta(\varnothing)+\delta(N)+\beta(N)
=1+2p,
\tag{8}
$$

$$
V
=
\alpha+a^\beta(\varnothing)
=2p.
\tag{9}
$$

The combined intensity of an ordinary successful record is

$$
\lambda
:=
\delta(N)+\beta(N)
=1+p.
\tag{10}
$$

Conditional on a selected skeleton record, the hidden kind is

$$
\mathbf P(\delta\mid\text{record})=\frac{p}{1+p},
\qquad
\mathbf P(\beta\mid\text{record})=\frac1{1+p}.
\tag{11}
$$

For a patch length `Delta`, Appendix B gives

$$
\varphi(\Delta)
=
e^{-(1+2p)\Delta}
+p\int_0^\Delta e^{-(1+2p)u}\,du
=
\frac{p+(1+p)e^{-(1+2p)\Delta}}{1+2p},
\tag{12}
$$

and

$$
\psi(\Delta,z)
=
p\int_0^\Delta e^{-u}\,du+ze^{-\Delta}
=
p+(z-p)e^{-\Delta}.
\tag{13}
$$

It is convenient to write

$$
f(\Delta):=\psi(\Delta,1)=p+qe^{-\Delta}.
\tag{14}
$$

## 3. Consistency probabilities and unnormalized amplitudes

All formulas below follow by multiplying the normalized Appendix-B contribution by its actual consistency probability.

### Incoming start

For an incoming patch ending incoming or at the horizon, consistency means either no outgoing mark before the endpoint or an empty-target death before every possible nonempty-target success. Hence

$$
\mathbf P(\operatorname{Con}(II))
=
\mathbf P(\operatorname{Con}(IE))
=\varphi(\Delta).
\tag{15}
$$

The unnormalized amplitudes are

$$
\widehat C(II)=f(\Delta),
\tag{16}
$$

$$
\widehat C(z,IE)
=p+(z-p)e^{-\Delta}.
\tag{17}
$$

For an incoming patch ending outgoing, the source must remain active throughout, so there can be no outgoing mark before the selected terminal record:

$$
\mathbf P(\operatorname{Con}(IO))
=e^{-(1+2p)\Delta},
\tag{18}
$$

and therefore

$$
\widehat C(IO)
=e^{-(1+2p)\Delta}e^{2p\Delta}
=e^{-\Delta}.
\tag{19}
$$

### Outgoing start

For an outgoing patch ending incoming or at the horizon, an initial split makes the source inactive immediately and is automatically consistent; an initial birth leaves it active and then contributes the incoming-start consistency factor. Thus

$$
\mathbf P(\operatorname{Con}(OI))
=
\mathbf P(\operatorname{Con}(OE))
=
\frac{p+\varphi(\Delta)}{1+p}.
\tag{20}
$$

Using the signs in (5)-(6),

$$
\widehat C(OI)
=
\frac{-p+\psi(\Delta,1)}{1+p}
=
\frac{q e^{-\Delta}}{1+p},
\tag{21}
$$

and

$$
\widehat C(z,OE)
=
\frac{-p+\psi(\Delta,z)}{1+p}
=
\frac{(z-p)e^{-\Delta}}{1+p}.
\tag{22}
$$

For an outgoing patch ending outgoing, consistency forces the initial kind to be a birth and then forces no outgoing mark before the endpoint:

$$
\mathbf P(\operatorname{Con}(OO))
=
\frac{e^{-(1+2p)\Delta}}{1+p},
\tag{23}
$$

so

$$
\widehat C(OO)
=
\frac{e^{-\Delta}}{1+p}.
\tag{24}
$$

The requested table is therefore

| type | consistency probability | unnormalized amplitude |
|---|---:|---:|
| `II` | `phi(Delta)` | `f(Delta)=p+q e^{-Delta}` |
| `IO` | `e^{-(1+2p)Delta}` | `e^{-Delta}` |
| `OI` | `(p+phi(Delta))/(1+p)` | `q e^{-Delta}/(1+p)` |
| `OO` | `e^{-(1+2p)Delta}/(1+p)` | `e^{-Delta}/(1+p)` |
| `IE` | `phi(Delta)` | `p+(z-p)e^{-Delta}` |
| `OE` | `(p+phi(Delta))/(1+p)` | `(z-p)e^{-Delta}/(1+p)` |

For the two end types, the affine constant and centered slope about terminal density `p` are

$$
\widehat C(z,IE)
=p+e^{-\Delta}(z-p),
\tag{25}
$$

$$
\widehat C(z,OE)
=0+\frac{e^{-\Delta}}{1+p}(z-p).
\tag{26}
$$

Thus the Professor-side heuristic that restoring consistency produces `e^{-Delta}` factors is correct, but the skeleton intensity must still be included.

## 4. Absorbing the skeleton intensity once per record

Every ordinary record has exactly one outgoing-start patch, namely the patch beginning at its source. Therefore the factor `lambda=1+p` in `m_t(dg)` may be assigned to that unique patch. Define

$$
\widetilde C(P)
=
\begin{cases}
\widehat C(P),&X(P)=I,\\
(1+p)\widehat C(P),&X(P)=O.
\end{cases}
\tag{27}
$$

Then the ordinary-record measure becomes plain ordered Lebesgue measure and the local table simplifies to

| type | intensity-absorbed amplitude |
|---|---:|
| `II` | `f(Delta)` |
| `IO` | `e^{-Delta}` |
| `OI` | `q e^{-Delta}` |
| `OO` | `e^{-Delta}` |
| `IE` | `p+(z-p)e^{-Delta}` |
| `OE` | `(z-p)e^{-Delta}` |

This is the cleanest bookkeeping for the first branching calculation. In particular, an outgoing-to-outgoing ancestry edge by itself has kernel

$$
e^{-\Delta},
\tag{28}
$$

whose integral over `Delta>=0` is one. This is the chain-only criticality noted by the Professor. The question is whether the patches created at the targets of the same record produce a genuine loss after all possible next sources are included.

## 5. Exact single-vacancy deviation formula

For the physical initial configuration `eta^0`,

$$
\eta^0(0)=0,
\qquad
\eta^0(x)=1\quad(x\neq0).
$$

Equilibrium invariance and the product-law form of the patch representation give

$$
D_t
:=
P_t\eta(0)(\eta^0)-p
=
P_t\eta(0)(\eta^0)-(\mu_pP_t)(\eta(0)).
$$

Using (1) for the first term and the fact that distinct end patches have distinct sites for the product equilibrium term,

$$
\begin{aligned}
D_t
={}&
\sum_g
\left[
\prod_{P\in\mathcal B_t(g)}\widehat C(P)
\right]
\\
&\quad\times
\left[
\prod_{P\in\mathcal E_t(g)}
\widehat C(\eta^0(i(P)),P)
-
\prod_{P\in\mathcal E_t(g)}
\widehat C(p,P)
\right]
m_t(dg).
\end{aligned}
\tag{29}
$$

This is the exact unnormalized-skeleton formula for the target deviation.

There is a useful simplification. If a skeleton contains at least one ordinary successful record, let the last record have source `j`. Because `j` is not in its own target `N(j)` and there is no later record, the patch beginning at `j` at the last record is necessarily an `OE` end patch. By (26),

$$
\widehat C(p,OE)=0.
$$

Hence every skeleton with at least one ordinary record has zero equilibrium product. Therefore

$$
D_t^{(n)}
=
\int_{\{\#\text{ ordinary records}=n\}}
\prod_{P\in\mathcal B_t}\widehat C(P)
\prod_{P\in\mathcal E_t}
\widehat C(\eta^0(i(P)),P)
\,m_t(dg),
\qquad n\geq1,
\tag{30}
$$

whereas the zero-record layer retains the equilibrium subtraction.

## 6. Zero ordinary records

With no ordinary record, there is a single `IE` end patch at site zero of length `t`. Thus

$$
D_t^{(0)}
=
\widehat C(0,IE_t)-\widehat C(p,IE_t)
=
p(1-e^{-t})-p
=-p e^{-t}.
\tag{31}
$$

## 7. Exactly one ordinary record: the complete first branch

The only possible source is zero. Let the record occur at time `s` and put

$$
r=t-s.
$$

The full patch family is:

- site `0`: `IO` on `[0,s)` and `OE` on `[s,t)`;
- sites `-1,+1`: one `IE` end patch each on `[s,t)`.

The raw product is

$$
e^{-s}
\cdot
\frac{-p e^{-r}}{1+p}
\cdot
f(r)^2,
$$

and the one-record skeleton intensity is `1+p`. Hence

$$
D_t^{(1)}
=
-p e^{-t}
\int_0^t f(r)^2\,dr.
\tag{32}
$$

Equivalently,

$$
D_t^{(1)}
=-p e^{-t}
\left[
 p^2t
 +2pq(1-e^{-t})
 +\frac{q^2}{2}(1-e^{-2t})
\right].
\tag{33}
$$

The complete target descendants are essential: the square `f(r)^2` comes from the two incoming target end patches. A one-lineage calculation would miss it.

Introduce the positive kernel

$$
k_{\mathrm s}(r)
:=
e^{-r}f(r)^2
=
p^2e^{-r}+2pq e^{-2r}+q^2e^{-3r}.
\tag{34}
$$

Its mass is

$$
m_{\mathrm s}
:=
\int_0^\infty k_{\mathrm s}(r)\,dr
=
p^2+pq+\frac{q^2}{3}
=p+\frac{q^2}{3}
=\frac{1+p+p^2}{3}
<1.
\tag{35}
$$

At this point a same-source chain looks strictly subcritical. The next section shows why that conclusion is false for the complete branching transfer.

## 8. Exactly two ordinary records

Let the first record occur at time `s`, the second at time `u`, and write

$$
b=u-s,
\qquad
c=t-u.
$$

After the first source-zero record the only possible second sources are `0,-1,+1`. There are therefore two geometric cases.

### 8.1 The second record is again sourced at zero

The full patch family is:

- site `0`: `IO` of length `s`, then `OO` of length `b`, then `OE` of length `c`;
- sites `-1,+1`: `II` of length `b`, then `IE` of length `c`.

Multiplying all raw amplitudes and the two factors of `1+p` from the skeleton measure gives

$$
-p e^{-t}f(b)^2f(c)^2.
$$

Thus

$$
D_{t,\mathrm{same}}^{(2)}
=
-p e^{-t}
\int_{\substack{b>0,c>0\\b+c<t}}
f(b)^2f(c)^2\,db\,dc.
\tag{36}
$$

In convolution notation, if `e_1(t)=e^{-t}`, then

$$
D_{t,\mathrm{same}}^{(2)}
=-p\,(e_1*k_{\mathrm s}*k_{\mathrm s})(t).
\tag{37}
$$

Its Laplace transform is

$$
-\frac1p\mathcal L D_{\mathrm{same}}^{(2)}(z)
=
\frac1{z+1}
\left(
\frac{p^2}{z+1}
+\frac{2pq}{z+2}
+\frac{q^2}{z+3}
\right)^2.
\tag{38}
$$

### 8.2 The second record is sourced at a child

Take source `+1`; source `-1` is its reflection. The full patch family is:

- site `0`: `IO` of length `s`, then `OI` of length `b`, then `IE` of length `c`;
- site `+1`: `IO` of length `b`, then `OE` of length `c`;
- site `-1`: one `IE` end patch of length `b+c`;
- site `+2`: one `IE` end patch of length `c`.

At the physical initial configuration,

$$
\widehat C(0,IE_c)=p(1-e^{-c}),
$$

$$
\widehat C(1,OE_c)=\frac{q e^{-c}}{1+p},
$$

$$
\widehat C(1,IE_r)=f(r).
$$

The two skeleton intensities cancel the two `1+p` denominators from the `OI` and final `OE` patches. The contribution of one chosen child is therefore

$$
pq^2 e^{-t}e^{-b}(1-e^{-c})f(b+c)f(c).
$$

Summing the two children gives

$$
D_{t,\mathrm{child}}^{(2)}
=
2pq^2 e^{-t}
\int_{\substack{b>0,c>0\\b+c<t}}
e^{-b}(1-e^{-c})f(b+c)f(c)
\,db\,dc.
\tag{39}
$$

This term is nonnegative, whereas the same-source term is nonpositive. The exact two-record layer is

$$
D_t^{(2)}
=
D_{t,\mathrm{same}}^{(2)}
+
D_{t,\mathrm{child}}^{(2)}.
\tag{40}
$$

For fixed `p,q in (0,1)`, the large-time scales are

$$
D_{t,\mathrm{same}}^{(2)}
=-\frac{p^5}{2}t^2e^{-t}+O(te^{-t}),
\tag{41}
$$

$$
D_{t,\mathrm{child}}^{(2)}
=2p^3q^2te^{-t}+O(e^{-t}).
\tag{42}
$$

These fixed-record layers all decay. That does not imply convergence after summing arbitrarily many records.

For reference, their time-integrated absolute masses are also finite. The same-source part has mass `p m_s^2`. Elementary integration of (39) gives

$$
\int_0^\infty D_{t,\mathrm{child}}^{(2)}\,dt
=
p\,m_{\mathrm{child},2},
$$

with

$$
m_{\mathrm{child},2}
=
\frac{q^2(5q^2-13q+9)}{18}
=
\frac{q^2(5p^2+3p+1)}{18}.
\tag{43}
$$

The fact that `m_s^2+m_child,2<1` is not an iterative contraction: the child term is not generated by the scalar kernel `k_s`, and the number and geometry of live lineages change at every record. The correct full-transfer test is below.

## 9. Complete first branching composition is exactly critical

The strict inequality in (35) is precisely the trap in a chain-only calculation.

Consider the first record and then ask which source produces the next record. Use the intensity-absorbed table and include every patch between the two record times.

### Next record at the original source

If the next record is again sourced at the original site after a delay `r`, then

- the source has an `OO` patch, contributing `e^{-r}`;
- both target descendants have `II` patches, each contributing `f(r)`.

Thus the same-source transfer density is exactly

$$
k_{\mathrm s}(r)
=e^{-r}f(r)^2.
\tag{44}
$$

Its mass is `m_s<1` from (35).

### Next record at one of the two children

If the next source is a specified child, then between the two records

- the old source is hit incoming by the child's target and contributes an `OI` factor `q e^{-r}`;
- the chosen child contributes an `IO` factor `e^{-r}`;
- the untouched sibling remains an incoming end line and contributes `f(r)` in the `h`-weighted coefficient-mass calculation.

Hence one child has transfer density

$$
q e^{-2r}f(r),
$$

and the two children together have

$$
k_{\mathrm c}(r)
=
2q e^{-2r}f(r)
=
2pq e^{-2r}+2q^2e^{-3r}.
\tag{45}
$$

Its mass is

$$
m_{\mathrm c}
=
\int_0^\infty k_{\mathrm c}(r)\,dr
=pq+\frac{2q^2}{3}
=q-\frac{q^2}{3}.
\tag{46}
$$

Therefore

$$
m_{\mathrm s}+m_{\mathrm c}
=
\left(p+\frac{q^2}{3}\right)
+
\left(q-\frac{q^2}{3}\right)
=1.
\tag{47}
$$

This is the complete first branching composition. The apparent chain margin

$$
1-m_{\mathrm s}
=q-\frac{q^2}{3}
$$

is **exactly** the mass routed to child-source records. There is no geometric loss.

The pointwise sum is

$$
\begin{aligned}
k_{\mathrm s}(r)+k_{\mathrm c}(r)
&=
p^2e^{-r}+4pq e^{-2r}+3q^2e^{-3r}.
\end{aligned}
\tag{48}
$$

Its integral is one.

Thus the answer to the Professor's first-composition question is: **critical**, not subcritical. Consistency probabilities suppress a fixed ancestry chain, but full branching restores the missing mass exactly.

## 10. Why the critical identity is the E1 Markov process

The equality (47) is not accidental. It is the first explicit manifestation of the verified `h`-transform.

After one ring of the E1 process from an isolated source, the source is retained and each of its two neighbours is independently retained with probability `q`. Let

$$
K\sim\operatorname{Binomial}(2,q)
$$

be the number of active children after that ring. Conditional on `K`, there are `1+K` active sources, each with a rate-one clock. The density that the **next** ring is at the original source after delay `r` is

$$
e^{-(1+K)r},
$$

so averaging over `K` gives

$$
\mathbf E[e^{-(1+K)r}]
=e^{-r}(p+qe^{-r})^2
=k_{\mathrm s}(r).
\tag{49}
$$

The density that the next ring is at one of the children is

$$
K e^{-(1+K)r},
$$

and averaging gives

$$
\mathbf E[K e^{-(1+K)r}]
=2q e^{-2r}(p+qe^{-r})
=k_{\mathrm c}(r).
\tag{50}
$$

The identity

$$
\int_0^\infty
\mathbf E[(1+K)e^{-(1+K)r}]\,dr
=1
$$

is exactly (47). The chain-only deficit is simply the probability that the next clock belongs to a child rather than the original source.

The zero-, one-, and two-record target-deviation layers in Sections 6--8 agree with the corresponding zero-, one-, and two-ring expansion of E1. For example, E1 gives the bounded terminal observable

$$
w(B)=q-\mathbf 1_{\{0\in B\}},
\qquad
D_t=\mathbf E_{\{0\}}[w(\mathcal A_t)].
\tag{51}
$$

The zero-ring term is `-p e^{-t}`. For one ring at time `s`, the origin is retained and the post-ring set has size `1+K`; conditioning on no further ring until `t` gives exactly (32). For two rings, splitting according to whether the second source is the original source or one of the children gives (36) and (39). In the child case the second ring refreshes the origin, and the dependence of the subsequent no-ring probability on that refreshed value is exactly the factor `(1-e^{-c})` in (39).

## 11. Global algebraic resummation to E1

There is an operator-level identification which does not rely on extrapolating the two-record calculation.

On a finite cycle, expand the centered semigroup in the centered-monomial basis:

$$
P_t\chi_A^*
=
\sum_B K_t(A,B)\chi_B^*.
\tag{52}
$$

The unnormalized patch formula computes these coefficients by expanding every affine end amplitude about `p` and collecting the coefficient of each product of `(eta(i)-p)`. Because the end sites are distinct, this collection is unambiguous.

E1 gives independently

$$
P_t\chi_A^*(\eta)
=
q^{|A|}
\sum_B Q_t(A,B)q^{-|B|}\chi_B^*(\eta),
\tag{53}
$$

where `Q_t=e^{t\mathcal G}` is the transformed finite-set Markov semigroup. Comparing the unique centered-basis coefficients in (52)-(53) gives

$$
K_t(A,B)
=q^{|A|-|B|}Q_t(A,B),
\tag{54}
$$

or equivalently

$$
Q_t(A,B)
=q^{|B|-|A|}K_t(A,B).
\tag{55}
$$

Thus the `h`-weighted full patch transfer is exactly stochastic:

$$
\sum_B q^{|B|-|A|}K_t(A,B)
=
\sum_BQ_t(A,B)
=1.
\tag{56}
$$

Equation (56) is the global version of the first-composition identity (47). It proves that restoring consistency probabilities cannot by itself yield a strict contraction of the complete centered coefficient mass. Any loss seen after restricting to one ancestry geometry must be compensated elsewhere in the full branching skeleton.

The same identity can also be read directly by evaluating (52) at the all-occupied configuration. There

$$
\chi_B^*(\mathbf 1)=q^{|B|},
$$

and hard FA-1f leaves `mathbf 1` absorbing, so

$$
P_t\chi_A^*(\mathbf 1)=q^{|A|}.
$$

This is exactly (56).

The infinite-volume statement for finite initial `A` follows by the same finite-volume passage already verified in Assignment 001. For the present strategic conclusion, the finite-cycle identity is already decisive: the complete unnormalized patch transfer is E1 in a different decomposition.

## 12. Where the normalization-hidden-gain heuristic fails

There are three levels which should not be conflated.

1. **One outgoing chain.** After assigning the record intensity to the outgoing-start patch, an `OO` segment contributes `e^{-Delta}`. Its mass is one. This is critical.

2. **Same-source continuation with both target descendants retained.** The two target `II` factors produce the kernel `k_s=e^{-r}f(r)^2`, whose mass is strictly below one. This looks like a useful branching gain.

3. **Complete next-record composition.** The two child-source sectors carry exactly the missing mass `1-m_s`. The sum has unit mass. This is the actual full skeleton transfer.

Therefore the consistency probabilities do not supply a target-level geometric loss. They redistribute mass among source choices.

This also explains why the first two fixed-record layers decay while the theorem remains open: a fixed event-count layer is transient in time, but the total conservative Markov transfer continuously moves mass to larger and differently shaped active sets. Summing all record counts is exactly the unresolved local-mixing problem of E1.

## 13. Relation to the closed sibling route

The closed Bernoulli-quench route used the normalized centered vacancy factor

$$
a=-\frac pq
$$

and the signed two-sibling identity

$$
(p+qa)^2=0,
$$

then tested whether absolute values of sibling descendants gave a generation-by-generation contraction. That route is not used here.

The local unnormalized amplitudes in Sections 3--4 are positive except for the terminal centered sign carried by an `OE` patch evaluated at the unique physical vacancy. The first-composition identity (47) is obtained before any absolute value of signed sibling factors is taken. Its criticality is conservation of the E1 Markov transfer, not failure of the old signed cancellation.

The algebraic overlap with Assignment 001 remains true: after centering and `h`-weighting, the patch expansion is exactly the same simultaneous-neighbour refresh process. Therefore trying to recover a contraction by expanding those two neighbour refreshes into normalized signed sibling weights and taking their absolute values would cross the already recorded closed-route boundary. Nothing in the present calculation reopens that option.

## 14. Consequence for E2 and E3

The exact part of E2 is now settled:

- the Radon--Nikodym bookkeeping is explicit;
- every hard-FA consistency probability and unnormalized local amplitude is explicit;
- the ordinary-record intensity is `1+p`;
- the zero-, one-, and two-record contributions to the actual single-vacancy deviation are explicit;
- the complete first branching composition is exactly critical;
- the full centered coefficient transfer algebraically resums to E1.

What fails is the proposed mechanism that normalization was hiding a useful probability penalty on long hard-model skeletons. A fixed ancestry chain is penalized, but the full branch conserves the `h`-weighted mass.

Accordingly I do not see a route from these local weights alone to E3a or E3b. A late-interaction bound based only on multiplying unnormalized consistency factors along the skeleton cannot gain geometric mass, because the complete transfer has row sum one after the exact `h`-weighting. Likewise terminal relaxation of individual end factors does not control the full number and geometry of end patches without an additional spatial theorem.

A continuation of the patch viewpoint would therefore have to add genuinely one-dimensional information absent from this calculation -- for example, a recurrence/overlap theorem forcing many nominal descendant lines to coalesce, or a regeneration event that controls the location of the unique physical vacancy relative to the skeleton. That would be a new E3 mechanism, not a consequence of unnormalizing the canonical patch formula.

Under the kill condition stated in Meeting 001, the normalization-hidden-gain subroute should be downgraded or closed: its first complete composition is critical and the full transfer is exactly the already-demoted E1 process in different coordinates.

## Handoff to the Professor

Decisive file:

`research/active/fa1f-finite-seed/students/student-a/002-unnormalized-patches.md`

The two conclusions which should change the spine are:

1. **E2 exact algebra is settled, but the hoped-for hidden skeleton loss is refuted.** Equations (1), (12)--(26), and (29)--(40) give the exact unnormalized hard-FA expansion and the complete zero/one/two-record target deviation. The full first branching transfer is critical: equations (44)--(47) show that the strict same-source mass deficit is exactly the mass routed to child-source records.

2. **The full patch transfer is E1 in different coordinates.** Equations (52)--(56) identify the centered patch coefficient matrix with the verified `h`-transform Markov semigroup. There is no consistency-probability contraction of total centered coefficient mass. I recommend closing the unnormalization-only route to E3. Any further patch work should require a new one-dimensional spatial mechanism, not more local patch-weight algebra.