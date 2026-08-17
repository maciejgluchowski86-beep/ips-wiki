# Student F 015: stationary boundary-control screening

## Verdict

Assignment 015 asks whether the exact stationary occupation hierarchy

\[
\mathcal K_N
=
\left\{
 m(x,u)\ge0:\ \sum m=1,\quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0\ \forall F
\right\}
\]

admits a repeatable Bellman/Poisson corrector concatenation forcing

\[
D_N(h)\to0.
\]

I do **not** obtain such a scale contraction. I do obtain an exact structural reduction of the concatenation problem, a controller-uniform tracking lemma, and a maximum-principle obstruction showing that independently solved block correctors do not concatenate at all.

The main exact identity is this. Let `F_N^+` be an optimal upper corrector and put

\[
s_N^+(x,u)
:=U_N(h)-h(x)+L_N^uF_N^+(x)\ge0.
\]

Let `F_N^-` be an optimal lower corrector and put

\[
s_N^-(x,u)
:=h(x)-L_N^uF_N^-(x)-\ell_N(h)\ge0.
\]

For every `M>=N+1`, interpret `s_N^\pm` on an `M`-site controlled chain by feeding the physical spin `X_N` into the old boundary-control slot. Then

\[
\boxed{
U_N(h)-U_M(h)
=
\inf_{m\in\mathcal K_M}m(s_N^+),
}
\tag{0.1}
\]

\[
\boxed{
\ell_M(h)-\ell_N(h)
=
\inf_{m\in\mathcal K_M}m(s_N^-),
}
\tag{0.2}
\]

and hence

\[
\boxed{
D_M(h)
=D_N(h)
-
\inf_{m\in\mathcal K_M}m(s_N^+)
-
\inf_{m\in\mathcal K_M}m(s_N^-).
}
\tag{0.3}
\]

Thus a dyadic recursion of the form proposed by the principal is exactly a theorem saying that the `N`-scale upper and lower Bellman slacks have unavoidable stationary occupation under **every** `2N`-site state-dependent controller.

The slack has a sharp control interpretation. One may choose optimal correctors satisfying a pointwise Bellman equality: for every block state `x`, at least one boundary action is tight. Since the two actions differ only through the flip rate of the rightmost spin,

\[
\left|(L_N^1-L_N^0)F(x)\right|
=d(x_{N-1})
\left|F(x^{N-1})-F(x)\right|,
\]

where

\[
d(0)=g=b-a,
\qquad
d(1)=c.
\]

If `pi_F(x)` is a tight boundary action, then

\[
\boxed{
s_F(x,u)
=w_F(x)\,1_{\{u\ne\pi_F(x)\}},
\qquad
w_F(x)
=d(x_{N-1})|F(x^{N-1})-F(x)|.
}
\tag{0.4}
\]

Therefore the exact block gain in `(0.1)`--`(0.3)` is a **weighted tracking error**: the next physical spin must fail to track the old optimal instantaneous boundary action on states carrying enough Bellman boundary gradient.

There is a controller-uniform unweighted tracking theorem. Put

\[
r_*:=\min\{a,1-c\}>0.
\]

For any Boolean target `pi:{0,1}^N->{0,1}` and every stationary controlled extension containing a physical interface spin `V=X_N`,

\[
\boxed{
P(V\ne\pi(X_0,\ldots,X_{N-1}))
\ge
\frac{r_*}{N+1+r_*}.
}
\tag{0.5}
\]

This is valid uniformly over arbitrary state-dependent boundary control. It follows by applying stationarity to the mismatch indicator. When matched, a flip of `V` creates a mismatch at rate at least `r_*`; when mismatched, repair can occur only through the flip of `V` or one of the `N` old spins, at total rate at most `N+1`.

Equation `(0.5)` is not enough for `(R)`. The Bellman occupation in `(0.4)` is weighted by the global, `N`-dependent quantity `w_F(x)`. The controller may force its unavoidable mismatch time onto states where this weight is small. A theorem preventing that weighted avoidance is the actual missing robustness statement.

There is also an exact obstruction to the most natural corrector concatenation. Let `F_N` be a pointwise Bellman-optimal corrector. Both boundary actions occur as tight actions somewhere. If, for example, action `1` were never tight, action `0` would be tight at every state. Pairing states which differ only in the rightmost spin gives simultaneously

\[
g\bigl(F(z,1)-F(z,0)\bigr)\ge0,
\]

and

\[
c\bigl(F(z,0)-F(z,1)\bigr)\ge0,
\]

so the boundary gradient vanishes and action `1` is also tight, a contradiction. The same argument interchanges the actions and applies to lower correctors.

Now append any `r>=1` new sites `z` and try a blockwise additive corrector

\[
H(x,z)=F_N(x)+G(z),
\]

where `G` may be **any** function on the appended block, including translated/averaged correctors and arbitrary right-block supplements. If `z_*` maximizes `G`, then

\[
L_r^uG(z_*)\le0
\]

for both far-right actions `u`. Let `v=(z_*)_0`. Since action `v` is tight somewhere for the old corrector, choose `x_v` with `s_N(x_v,v)=0`. Then the enlarged upper Bellman residual at `(x_v,z_*)` is at least `U_N`. Hence

\[
\boxed{
\max_{x,z,u}
\left(h(x)-L_{N+r}^u(F_N+G)(x,z)\right)
\ge U_N.
}
\tag{0.6}
\]

No right-block additive supplement can improve the upper bound. At a minimum of `G` the same maximum-principle argument gives

\[
\boxed{
\min_{x,z,u}
\left(h(x)-L_{N+r}^u(F_N^-+G)(x,z)\right)
\le\ell_N.
}
\tag{0.7}
\]

Thus independently solved block correctors **do not concatenate**. Every strict improvement from `N` to a larger scale necessarily uses a corrector depending jointly on the old block and the newly appended block.

A conditional extension is useful. If a proposed fixed-width interface correction depends on a suffix `y` of the old block and the new block, and for every interface cylinder `y` and both old boundary actions there is a state in that cylinder where the corresponding action is tight, the same maximum-principle proof kills that interface correction. At the exact strict rational calibration

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
\qquad h(x)=x_0,
\]

the exact `N=2` upper and lower Bellman correctors have this property for the one-spin old interface. Hence even an arbitrary correction depending on that interface spin plus the entire appended block cannot improve the `N=2` endpoint.

The hard-East ingredient does not currently repair this. The state-dependent controller in `K_N` is feedback from the **entire old block** to the right boundary; it is not a fixed or exogenous ergodic East boundary. Already for one controlled spin,

\[
U_1(x_0)=\frac{b}{b+(1-c)},
\qquad
\ell_1(x_0)=\frac{a}{a+1},
\tag{0.8}
\]

obtained by choosing the facilitating boundary when the spin is `0` and the nonfacilitating boundary when it is `1` for the upper problem, and the opposite feedback for the lower problem. By contrast the two fixed boundary stationary densities are

\[
p_0=\frac{a}{a+1-c},
\qquad
p_1=\frac{b}{1+b}.
\tag{0.9}
\]

At the rational calibration,

\[
p_0=\frac13,
\qquad p_1=\frac3{13},
\qquad U_1=\frac35,
\qquad \ell_1=\frac1{11}.
\]

So arbitrary stationary feedback can bias the local law far outside the range generated by either fixed East boundary. A hard-East relaxation theorem with a fixed or exogenous boundary cannot simply be inserted into the occupation hierarchy. A successful robustness lemma must explicitly show that, after a macroscopic controlled block is interposed, this adaptive feedback cannot concentrate on the low-`w_F` mismatch states in `(0.4)`.

I independently reproduced the principal's finite-box shrinkage numerically. For `h=x_0`, my floating LP implementation gives

\[
\begin{array}{c|cc}
(a,b,c)&D_5&D_9\\ \hline
(10^{-4},10^{-2},0.9999)&0.16055069&0.01176400\\
(0.002,0.1,0.9999)&0.28485520&0.02099638\\
(0.001,0.1,0.9999)&0.40101358&0.04863173
\end{array}
\]

(the first `D_9` differs slightly from the rounded value in the principal note). These values are only reconnaissance and are not used in any theorem above.

At the rational calibration the exact `N=1 -> 2` identities are

\[
U_1=\frac35,
\qquad U_2=\frac38,
\qquad
U_1-U_2=\frac9{40},
\]

\[
\ell_1=\frac1{11},
\qquad \ell_2=\frac{31}{137},
\qquad
\ell_2-\ell_1=\frac{204}{1507}.
\]

Exact enumeration of all deterministic two-site boundary policies verifies that the two differences are precisely the minima of the corresponding `N=1` Bellman-slack occupation, as `(0.1)`--`(0.2)` require. The verifier also checks exact `N=2` Bellman correctors and the one-spin interface tight-action condition.

## 1. Independent derivation of the hierarchy and dual

Let `m in K_N` and write

\[
\bar m(x)=\sum_um(x,u).
\]

When `bar m(x)>0`, define

\[
\pi(u\mid x)=m(x,u)/\bar m(x).
\]

Then

\[
\sum_x\bar m(x)L_N^\pi F(x)
=
\sum_{x,u}m(x,u)L_N^uF(x)=0,
\]

so `K_N` is exactly the set of stationary occupation measures of randomized state-dependent boundary policies. Since all flip rates have the positive lower bounds `a` or `1-c`, every such controlled finite chain is irreducible and its stationary state marginal has full support.

If `m in K_{N+1}`, project to the first `N` spins and use the old `N`th spin as the new action. For a function of the first `N` spins,

\[
L_{N+1}^uF(x,v)=L_N^vF(x),
\]

so the projected occupation measure belongs to `K_N`. This independently gives the nesting and monotonicity of `D_N`.

The occupation LP maximizing `m(h)` has the standard finite dual

\[
U_N(h)=\inf_F\max_{x,u}(h-L_N^uF),
\]

and similarly for the lower endpoint. Strong duality holds because the finite occupation polytope is nonempty and bounded.

## 2. Exact scale-extension identity

Fix an optimal upper corrector `F_N^+` and define `s_N^+` as above. For `M>N`, every function `H` on the `M`-site state space can be written uniquely as

\[
H(x,z)=F_N^+(x)+G(x,z)
\]

for some unrestricted `G`. Since `F_N^+` depends only on the first `N` spins,

\[
L_M^uF_N^+(x,z)=L_N^{z_0}F_N^+(x).
\]

Therefore

\[
\begin{aligned}
h-L_M^uH
&=U_N-s_N^+(x,z_0)-L_M^uG.
\end{aligned}
\]

Taking the infimum over `G` and the maximum over states/actions gives

\[
\begin{aligned}
U_M
&=U_N-
\sup_G\min_{x,z,u}
\left(s_N^+(x,z_0)+L_M^uG\right)\\
&=U_N-\ell_M(s_N^+)\\
&=U_N-\inf_{m\in K_M}m(s_N^+).
\end{aligned}
\]

The sign of `G` in the lower dual is immaterial. This proves `(0.1)`. Repeating the calculation from a lower corrector proves `(0.2)`.

Thus corrector concatenation is not a question of whether some unspecified finite-box pattern repeats. It is exactly the question of whether the old Bellman slack has a scale-uniform unavoidable occupation after the physical controller has been moved farther right.

## 3. Pointwise Bellman slack and controller tracking

Let `m^+` be an optimal occupation measure for `U_N` and choose a complementary optimal dual `F_N^+`. The controlled chain associated with `m^+` is irreducible, so its state marginal is strictly positive. Hence for every state `x`, at least one action has positive occupation. Complementary slackness then gives

\[
\min_u s_N^+(x,u)=0
\qquad\forall x.
\tag{3.1}
\]

The same holds for the lower slack.

Only the rightmost-site flip rate changes between actions. If `x_{N-1}=0`,

\[
(L_N^1-L_N^0)F(x)
=g\bigl(F(x^{N-1})-F(x)\bigr),
\]

whereas if `x_{N-1}=1`,

\[
(L_N^1-L_N^0)F(x)
=c\bigl(F(x^{N-1})-F(x)\bigr).
\]

Together with `(3.1)` this gives `(0.4)`.

To prove `(0.5)`, let

\[
M=1_{\{V\ne\pi(X)\}}.
\]

At a matched state, the interface spin `V` flips at rate at least `r_*`, and that flip alone creates a mismatch. At a mismatched state, mismatch can be repaired only by a flip of `V` or by a flip of one of the `N` old spins which changes `pi`; every single-site rate is at most one, so the total repair rate is at most `N+1`. Therefore pointwise

\[
LM
\ge
r_*1_{\{M=0\}}-(N+1)1_{\{M=1\}}.
\]

Stationarity yields `(0.5)`.

The remaining gap is now explicit: `(0.5)` controls mismatch count, whereas `(0.1)` needs the **weighted** mismatch `w_FM`. The hard-East statements cited in Meeting 023 concern relaxation of fixed local observables behind facilitating boundaries. They do not control the `N`-dependent global Bellman gradient `w_F` under adaptive feedback.

## 4. Additive block concatenation is impossible

For a complementary upper corrector, both action values must be tight somewhere. Suppose action `1` were never tight. Then action `0` is tight at every state by `(3.1)`. Hence

\[
h-L_N^0F=U_N,
\qquad h-L_N^1F\le U_N.
\]

For each prefix `z`, evaluate this at `(z,0)` and `(z,1)`. The action inequalities give respectively

\[
g(F(z,1)-F(z,0))\ge0,
\]

and

\[
c(F(z,0)-F(z,1))\ge0.
\]

Thus `F(z,1)=F(z,0)`, so the two actions tie, contradiction. The other action and the lower problem are identical.

Now let `G` be arbitrary on any appended `r`-site right block. At a global maximum `z_*`, every controlled generator satisfies

\[
L_r^uG(z_*)\le0.
\]

Put `v=(z_*)_0` and choose an old state where action `v` is tight. The enlarged upper residual is then at least `U_N`, proving `(0.6)`. The lower statement follows from a global minimum of `G`.

This rules out every composition obtained by adding an independently constructed right-block corrector to the old one. A successful theorem must introduce joint dependence across the block interface. The exact scale identity `(0.1)` shows that such joint dependence is not cosmetic: it is precisely what is needed to exploit the unavoidable mismatch of the physical interface spin.

## 5. What the East ingredient would have to prove

A usable robustness theorem cannot merely say that a facilitator occurs with positive probability or that a hard-East block with a fixed facilitating boundary mixes in `O(N)` time. It must imply a weighted Bellman statement of the following type.

For upper and lower optimal `N`-block correctors, uniformly over every `m in K_{2N}`,

\[
m\left[
 w_N^\pm(X)
 1_{\{X_N\ne\pi_N^\pm(X)\}}
\right]
\]

must capture a fixed fraction of `D_N(h)` after the two signs are combined, up to a summable scale error. Equivalently, by `(0.3)`, one needs

\[
\inf_{K_{2N}}m(s_N^+)
+
\inf_{K_{2N}}m(s_N^-)
\ge
\rho D_N(h)-Ce^{-\gamma N}.
\tag{5.1}
\]

Equation `(5.1)` is not offered as a new notation for `(R)`; it identifies the concrete random object which the hard-East mechanism must control: **adaptive tracking of the global Bellman-optimal boundary action, weighted by the boundary gradient of the corrector**. The unweighted tracking loss `(0.5)` is proved, but no argument from the cited hard-East theorems upgrades it to `(5.1)`.

The one-site formulas `(0.8)`--`(0.9)` show why the boundary hypothesis matters. The controller can choose its action from the current state and thereby change holding times; this feedback is stronger than choosing between two fixed boundary laws. Moving the controller a macroscopic distance away may screen that feedback, as the finite LP data suggest, but proving that is exactly the missing theorem.

## 6. Status

Established in this block:

1. the occupation hierarchy, nesting, and LP dual are independently rederived;
2. the exact all-scale Bellman-slack extension identities `(0.1)`--`(0.3)`;
3. the pointwise weighted tracking representation `(0.4)`;
4. the controller-uniform mismatch lower bound `(0.5)`;
5. a maximum-principle theorem showing no additive appended-block corrector can improve either dual endpoint;
6. an exact strict-residual `N=1 -> 2` certificate verifying the slack identity and showing that even a one-spin cross-interface supplement is obstructed at that calibration;
7. exact one-site feedback formulas demonstrating that arbitrary state-dependent control is not covered by fixed-boundary East relaxation.

Not established:

- a lower bound converting unweighted mismatch `(0.5)` into weighted slack occupation `(5.1)`;
- a fixed-width joint interface corrector which repeats at all scales;
- the dyadic recursion `(R)` or any substitute forcing `D_N(h)->0`;
- static uniqueness or the later dynamic theorem `(ZF)`.

The finite LP shrinkage is therefore real but not yet a repeatable theorem. The exact dual algebra shows why simply concatenating finite correctors cannot provide one: strict scale improvement necessarily lives in a joint cross-block correction, while the only controller-uniform tracking estimate currently available loses the Bellman weight.

Supporting exact checks are in

`students/student-f/015-stationary-boundary-control-screening-verifier.py`.

`unresolved after substantive work; boundary-control blocker: exact scale extension gives D_M=D_N-inf_{K_M}m(s_N^+)-inf_{K_M}m(s_N^-), where each Bellman slack is a weighted mismatch between the physical interface spin and the old state-dependent optimal boundary action. The physical interface has a uniform unweighted tracking error at least min(a,1-c)/(N+1+min(a,1-c)), but no proved theorem prevents that mismatch from concentrating on states where the N-dependent Bellman boundary gradient is small. Moreover any corrector of the form old N-block corrector plus an arbitrary independently constructed appended-block corrector gives zero strict improvement by a maximum-principle argument; strict contraction necessarily requires a genuinely joint cross-block corrector. The cited hard-East fixed/ergodic-boundary relaxation does not control this adaptive weighted feedback. No repeatable recursion forcing D_N(h)->0 was obtained.`
