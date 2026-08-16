# Student G 005: a balanced-circulation obstruction refutes the 16-phase scalar product/coboundary Foster class

## Verdict

The 16-phase **nearest-neighbour scalar edge-product/coboundary corrector class is refuted**.

The obstruction occurs already in the infinite-height **bulk**, so no choice of right-boundary height factor, insertion factor, left-boundary correction, terminal phase weight, or suffix-trimming convention can repair this class.

At the strict residual point

$$
\boxed{
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
}
\tag{0.1}
$$

there is an explicit nonnegative spatial circulation `mu` on the 64 triple phases with the following two simultaneous properties:

1. the expected exponent change of **every** edge weight `q_{alpha beta}` is exactly zero;
2. the expected number of newly created exposure edges is strictly positive.

These two identities imply, by a single weighted AM--GM inequality, that for every positive phase matrix `Q=(q_{alpha beta})` and every restart tilt `s>1`,

$$
\boxed{
\sum_{\alpha,\beta,\gamma}
\mu_{\alpha\beta\gamma}
G_Q(\alpha,\beta,\gamma)>0.
}
\tag{0.2}
$$

But any coboundary certificate

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
\tag{C}
$$

would give a nonpositive left side after averaging against a spatial circulation. Hence `(C)` is impossible at (0.1) for **every** positive `Q` and **every** `s>1`.

Equivalently, because every finite circulation decomposes into directed cycles of the 16-vertex de Bruijn graph, for every `Q` and `s>1` at least one directed spatial cycle has strictly positive mean bulk drift.

Thus Assignment 005 ends negatively but decisively:

> scalar nearest-neighbour edge products cannot provide the global all-height Foster corrector throughout the residual chamber. Any continuation of the coupling-side Foster route requires a strictly richer corrector, such as a matrix-product/nonlocal state.

This does **not** affect the Professor-verified same-parent geometric restart tail. It also does not decide Student F's mode-resolved signed `L^1(w)` problem; that is a distinct signed temporal-mode interface.

An exact rational verifier is committed beside this report as

`students/student-g/005-16-phase-foster-feasibility-verifier.py`.

## 1. Setup

Let

$$
\mathcal A=\{00,11,01,10\}
$$

be the four coupled-pair states. For positive edge weights

$$
q_{\alpha\beta}>0,
\qquad (\alpha,\beta)\in\mathcal A^2,
$$

define

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i}.
$$

For a triple

$$
e=(\alpha,\beta,\gamma)\in\mathcal A^3,
$$

a rate-one update of the middle pair `beta=(x,y)` with right pair `gamma=(u,v)` uses

$$
p=r_{xu},
\qquad
\widetilde p=r_{yv},
$$

where

$$
r_{00}=a,
\qquad
r_{01}=b,
\qquad
r_{10}=c,
\qquad
r_{11}=0.
$$

Under the common-uniform coupling, the new middle pair `z` has probabilities

$$
\begin{array}{c|c}
z & p_e(z)\\ \hline
11 & \min(p,\widetilde p)\\
00 & 1-\max(p,\widetilde p)\\
10 & (p-\widetilde p)_+\\
01 & (\widetilde p-p)_+.
\end{array}
\tag{1.1}
$$

As in Assignment 004, write

$$
E(\alpha,\beta)
=1_{\{\alpha\text{ diagonal},\ \beta\text{ off-diagonal}\}}
$$

and let

$$
\rho_e(z)
=
1_{\{E(\alpha,\beta)=0,E(\alpha,z)=1\}}
+
1_{\{E(\beta,\gamma)=0,E(z,\gamma)=1\}}
\tag{1.2}
$$

be the number of newly created exposure edges in that update. For these local updates `rho_e(z)` is `0` or `1`.

The local tilted bulk drift is

$$
G_Q(e)
=
\sum_{z\ne\beta}p_e(z)
\left[
 s^{\rho_e(z)}
 \frac{q_{\alpha z}q_{z\gamma}}
 {q_{\alpha\beta}q_{\beta\gamma}}
 -1
\right].
\tag{1.3}
$$

Introduce log weights

$$
x_{\alpha\beta}=\log q_{\alpha\beta}
$$

and the exponent-change vector

$$
\Delta_e(z)
=
\mathbf e_{\alpha z}
+
\mathbf e_{z\gamma}
-
\mathbf e_{\alpha\beta}
-
\mathbf e_{\beta\gamma}
\in\mathbb Z^{16}.
\tag{1.4}
$$

Then

$$
\frac{q_{\alpha z}q_{z\gamma}}
{q_{\alpha\beta}q_{\beta\gamma}}
=
\exp\langle\Delta_e(z),x\rangle.
\tag{1.5}
$$

## 2. Balanced spatial circulations

A nonnegative family

$$
\mu=(\mu_{\alpha\beta\gamma})_{\mathcal A^3}
$$

is a normalized spatial circulation if

$$
\sum_e\mu_e=1
\tag{2.1}
$$

and, for every edge phase `(alpha,beta)`,

$$
\boxed{
\sum_{\gamma}\mu_{\alpha\beta\gamma}
=
\sum_{\delta}\mu_{\delta\alpha\beta}.
}
\tag{2.2}
$$

Condition (2.2) is exactly flow conservation on the de Bruijn graph

$$
(\alpha,\beta)\longrightarrow(\beta,\gamma).
$$

Call such a circulation **Q-balanced** if also

$$
\boxed{
\sum_e\mu_e
\sum_{z\ne\beta}p_e(z)\Delta_e(z)=0
\quad\text{in }\mathbb R^{16}.
}
\tag{2.3}
$$

Define its changing-update mass and exposure-entry rate by

$$
C_\mu
=
\sum_e\mu_e\sum_{z\ne\beta}p_e(z),
\tag{2.4}
$$

$$
R_\mu
=
\sum_e\mu_e\sum_{z\ne\beta}p_e(z)\rho_e(z).
\tag{2.5}
$$

The notation `Q-balanced` refers to cancellation of the exponents of an arbitrary `Q`; the circulation itself does not depend on `Q`.

## 3. General AM--GM obstruction lemma

### Lemma 3.1

Suppose a normalized nonnegative spatial circulation `mu` satisfies (2.3) and

$$
R_\mu>0.
$$

Then for every positive phase matrix `Q` and every `s>1`,

$$
\boxed{
\sum_e\mu_eG_Q(e)
\ge
C_\mu
\left(s^{R_\mu/C_\mu}-1\right)
>0.
}
\tag{3.1}
$$

Consequently no potential `psi` can satisfy `(C)` for all 64 triples.

#### Proof

Only terms with `z ne beta` occur in `G_Q`. Set

$$
\theta_{e,z}
=
\frac{\mu_ep_e(z)}{C_\mu}.
$$

After omitting zero-probability terms,

$$
\theta_{e,z}\ge0,
\qquad
\sum_{e,z}\theta_{e,z}=1.
$$

Using (1.5),

$$
\begin{aligned}
\sum_e\mu_eG_Q(e)
&=
C_\mu
\left[
\sum_{e,z}\theta_{e,z}
 s^{\rho_e(z)}
 e^{\langle\Delta_e(z),x\rangle}
-1
\right].
\end{aligned}
\tag{3.2}
$$

Weighted AM--GM gives

$$
\sum_{e,z}\theta_{e,z}
 s^{\rho_e(z)}e^{\langle\Delta_e(z),x\rangle}
\ge
s^{\sum\theta_{e,z}\rho_e(z)}
\exp\left\langle
\sum\theta_{e,z}\Delta_e(z),x
\right\rangle.
$$

By (2.3),

$$
\sum\theta_{e,z}\Delta_e(z)=0,
$$

while

$$
\sum\theta_{e,z}\rho_e(z)=\frac{R_\mu}{C_\mu}.
$$

This proves (3.1).

If `(C)` held, multiplying it by `mu_e` and summing would give

$$
\sum_e\mu_eG_Q(e)
\le
\sum_{\alpha,\beta,\gamma}
\mu_{\alpha\beta\gamma}
\bigl[\psi(\alpha,\beta)-\psi(\beta,\gamma)\bigr]
=0
$$

by the flow identity (2.2), contradicting (3.1). `square`

### Remark 3.2

The lemma is stronger than a numerical positive-cycle search. Once `mu` is given, it proves infeasibility simultaneously for all 16 positive phase weights and all `s>1`. No optimization over `Q` remains.

## 4. Exact strict-residual certificate

Take the near-East point

$$
\varepsilon=\frac1{100},
\qquad
(a,b,c)
=
(\varepsilon^2,\varepsilon,1-\varepsilon^2).
\tag{4.1}
$$

It lies strictly in the residual chamber:

$$
0<a<b,
\qquad
c>\frac12,
\qquad
c>a+b,
$$

and

$$
b^2=10^{-4}
>
2\cdot10^{-8}
=2(1-c)^2,
$$

so

$$
b>\sqrt2(1-c).
$$

Put

$$
D
=35378973959396206576874982782015790.
\tag{4.2}
$$

All unlisted triple weights below are zero, and for the listed triples set

$$
\mu_e=\frac{W_e}{D}.
$$

| triple `e` | integer weight `W_e` |
|---|---:|
| `00,00,01` | 4445398949312905081615855043064000 |
| `00,11,00` | 91095378005220269980796203014000 |
| `00,11,01` | 58736277707417592363434243646558 |
| `00,11,10` | 70630552927090213332617368110942 |
| `00,01,01` | 28448549891729378692982951213700 |
| `00,01,10` | 5718765235555301816115306641886300 |
| `00,10,01` | 2949418712365070463554452020574200 |
| `00,10,10` | 14672250265018942560267863425800 |
| `11,00,01` | 115914969605660652497282417211242 |
| `11,00,10` | 16536617826918181602523909538758 |
| `11,11,01` | 1764590729389757134240690903500 |
| `11,01,10` | 60500868436807349497674934550058 |
| `11,10,01` | 70630552927090213332617368110942 |
| `01,00,00` | 1858737959368023216913230451744429 |
| `01,00,10` | 2947554344803171224512195974461242 |
| `01,11,00` | 26683959162339621558742260310200 |
| `01,11,11` | 1764590729389757134240690903500 |
| `01,01,11` | 28448549891729378692982951213700 |
| `01,01,01` | 158346233425721318082272145 |
| `01,10,00` | 3993023065113075401074624538915829 |
| `01,10,01` | 2918915497745675337952683261246087 |
| `10,00,00` | 2586660989944881864702624591319571 |
| `10,00,11` | 220462208639728075676847814771500 |
| `10,00,01` | 1185899866528465460695152132824758 |
| `10,11,00` | 14672250265018942560267863425800 |
| `10,01,00` | 4806292304171194441425426426205671 |
| `10,01,10` | 1132672458866641573414326223725558 |
| `10,10,11` | 14672250265018942560267863425800 |

The verifier checks in exact rational arithmetic that

$$
\sum_eW_e=D,
$$

all 16 flow identities (2.2) hold, and all 16 exponent-balance identities (2.3) hold.

For this certificate,

$$
\boxed{
R_\mu
=
\frac{40097221742150361438903}
{4060682358517754276494700}
>0,
}
\tag{4.3}
$$

and

$$
\boxed{
C_\mu
=
\frac{10111075801610946800285497}
{812136471703550855298940000}
>0.
}
\tag{4.4}
$$

In particular

$$
\frac{R_\mu}{C_\mu}
=
\frac{8019444348430072287780600}
{10111075801610946800285497}
\approx0.7931346284.
\tag{4.5}
$$

Lemma 3.1 therefore gives the completely `Q`-independent lower bound

$$
\boxed{
\sum_e\mu_eG_Q(e)
\ge
C_\mu
\left(
 s^{8019444348430072287780600/
 10111075801610946800285497}
-1
\right)>0
}
\tag{4.6}
$$

for every `s>1`.

This proves infeasibility of the bulk coboundary system `(C)` at the strict residual point (4.1).

## 5. Why boundary corrections cannot rescue the class

Assignment 005 asked that a positive result also control rightmost coalescence, trail insertion, left boundary, terminal phases, and suffix trimming. The present negative result occurs before those questions arise.

Indeed a normalized circulation on a finite directed graph decomposes into a convex combination of directed cycle occupation measures. Equation (4.6) therefore implies that at least one directed spatial cycle `C=C(Q,s)` has

$$
\frac1{|C|}\sum_{e\in C}G_Q(e)>0.
\tag{5.1}
$$

Repeating that spatial cycle `m` times produces an interior tilted drift growing linearly in `m`. Every boundary/height correction in the nearest-neighbour product/coboundary architecture contributes only through finitely many endpoint transitions and is therefore `O(1)` in the repeated-cycle length.

Consequently no finite right-boundary height gain or endpoint potential can compensate (5.1) at arbitrary height.

This is exactly the same logic behind the no-positive-cycle criterion from Assignment 004, now with a `Q`-independent strict certificate.

## 6. How the certificate was found, and what is proof versus discovery

The certificate was discovered by solving the finite linear programme

$$
\max_\mu R_\mu
$$

subject to normalization, spatial flow conservation, exponent balance (2.3), and `mu>=0` at the rational point (4.1).

That optimization is **not** used as a black-box premise in the proof. The final verifier hard-codes the resulting integer weights `W_e` and checks every required linear identity exactly with `fractions.Fraction`. Lemma 3.1 then proves the obstruction analytically by weighted AM--GM.

Thus the final claim does not depend on floating-point optimization, solver tolerances, or an unverified numerical cycle search.

## 7. Relation to the same-parent theorem

Nothing here contradicts the accepted same-parent estimate

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1}.
$$

That theorem is a temporal renewal statement for one fixed parent before its first coalescence.

The present circulation obstruction says that no **scalar nearest-neighbour spatial product** can simultaneously prepay all exposure creations across arbitrary unresolved configurations. The positive circulation uses a mixture of inactive, exposed, child-alive, susceptible, and reinfection phases whose net `Q`-energy change is zero while restart production remains positive.

So the failure is genuinely at the global spatial composition level, exactly as Meeting 010 isolated.

## 8. Interface with Student F

Student F's theorem

$$
|Br_0-c|Z<\frac23
$$

and its mode-resolved `L^1(w)` assignment are independent of this refutation.

The consequence for combination is narrower:

- F should not tensor its signed temporal modes with a scalar 16-phase edge-product Foster state, because no such global Foster state exists throughout the residual chamber;
- if the centered-trail route continues through coupling, the coupling return mechanism must use a richer state than a scalar nearest-neighbour product/coboundary corrector;
- plausible next classes include matrix-product correctors, finite automaton/history states with noncommuting weights, or a nonlocal renewal construction tied directly to certified clearing episodes.

The present result does not prove that any of those stronger classes work.

## 9. Status

### Proved here

1. Lemma 3.1: any balanced circulation with positive restart flux is an all-`Q`, all-`s>1` obstruction to the product/coboundary inequalities.
2. At the strict residual point `(a,b,c)=(1/10000,1/100,9999/10000)`, the explicit 28-triple rational certificate satisfies the balance hypotheses and has `R_mu>0`.
3. Therefore the 16-phase nearest-neighbour scalar edge-product/coboundary Foster class is impossible at that residual point.
4. Hence it cannot prove a global Foster theorem throughout the residual chamber, regardless of boundary/height choices.

### Not proved here

- failure of matrix-product or nonlocal correctors;
- failure of every finite temporal coupling state;
- decay or nondecay of the global trail quantity `J_{x,r}`;
- the mode-resolved signed `L^1(w)` theorem assigned to Student F;
- the positive rates conjecture.

## Handoff

`nearest-neighbour product/coboundary corrector refuted because: at the strict near-East point (a,b,c)=(1/10000,1/100,9999/10000) there is an explicit normalized spatial circulation mu on the 64 triple phases with exact flow conservation and exact zero expected Q-exponent change, but positive exposure-entry rate R_mu. For every positive edge matrix Q and every s>1, weighted AM--GM gives sum_e mu_e G_Q(e) >= C_mu(s^(R_mu/C_mu)-1)>0. A coboundary potential would force the same circulation average to be <=0, contradiction. Equivalently at least one directed spatial cycle has positive mean for every Q,s. This is a bulk obstruction, so finite boundary/height corrections cannot repair the class. The same-parent geometric restart theorem remains valid; a stronger matrix-product/nonlocal coupling corrector is required if this route continues.`