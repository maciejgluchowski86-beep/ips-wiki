# Student F 010: profile regeneration / truncation of the growing mass hierarchy

## Verdict

Meeting 011 asks for a quantitative replacement for the impossible depth-uniform finite mode closure. Meeting 012 has since accepted Student G's refutation of the complete nearest-neighbour scalar edge-product/coboundary Foster class. That correction changes the eventual composition target, but it does not invalidate the common-mass truncation problem itself. I therefore continue Assignment 010 independently of any finite scalar coupling cocycle.

I obtain three exact positive results.

1. **Projective suffix locality.** The duration-resolved reverse transfer commutes exactly with right-suffix marginalization. Consequently the first `M` reverse trail transfers depend only on the rightmost `M` sites of the incoming signed measure, uniformly in the total interval depth.
2. **Invariant one-insertion profile truncation.** The zero-boundary invariant laws form a projective suffix family. If
   \[
   Y=B\eta_0-c,
   \]
   then the exact reverse conditional coefficient
   \[
   K_M=E[Y\mid \eta_{-M},\ldots,\eta_{-1}]
   \]
   converges in `L^1` to the full-past coefficient, and the tail is uniformly Cauchy. Therefore a single invariant centered insertion admits a genuine depth-uniform finite-context truncation for **arbitrary bounded left functions**, not only for separated supports.
3. **Quantitative separated-gap regeneration.** If a bounded test function is at least `M` sites left of the zero boundary, the non-equilibrium part of one invariant insertion is exponentially small:
   \[
   \left|
   \pi_N^0\bigl((B\eta_N-c)f\bigr)
   -(Br_0-c)\pi_N^0(f)
   \right|
   \le
   \frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\,\|f\|_\infty.
   \]
   This is obtained from an exact resolvent identity plus finite propagation, with the absolute value taken before any time integration.

These results show that exact finite modes were the wrong state space but that finite-context approximation at the **first invariant insertion** is real.

The full Assignment-010 theorem remains unresolved. After the first centered insertion, the left object is a signed nonstationary profile, not another zero-boundary invariant law. The static martingale truncation no longer applies directly. The mass branch carries the left marginal of `pi_N^0`, which is not `pi_{N-1}^0`, and the discrepancy has the exact zero-frequency boundary-response representation

\[
\bar\pi_N(f)-\pi_{N-1}^0(f)
=
\pi_N^0\left[
\eta_N D
\int_0^\infty
P_t^{N-1,0}\bigl(f-\pi_{N-1}^0(f)\bigr)\,dt
\right].
\]

Finite speed controls the integrand only on bounded time windows. There is no positive Laplace parameter in this boundary-response formula, so the finite-speed bound is not integrable at infinity without an additional uniform mixing/cancellation estimate. This is precisely the profile-tail step still missing.

The analogous **one-segment** semigroup truncation is easy and quantitative:

\[
\int_0^\infty
w(u)\,
\|P_u f-P_u^{(M)}f\|_\infty\,du
\le
\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.
\]

But iterating this estimate through centered insertions in a scalar absolute-value norm costs the already-refuted factor `cZ>1`. Meeting 012 additionally removes the proposed nearest-neighbour scalar coupling cocycle as a repair. Thus the remaining theorem needs a genuinely signed/nonlocal profile norm or a matrix-product/nonlocal coupling mechanism; local finite-speed plus scalar variation cannot close it.

The exact blocker is therefore narrower than in Assignment 009: **equilibrium insertion truncates; post-insertion signed boundary profiles do not yet have a depth-uniform truncation estimate.**

Supporting algebra/projective checks are in

`students/student-f/010-profile-regeneration-verifier.py`.

## 1. Notation and the Meeting 012 correction

Work in the strict residual chamber. Put

\[
B=b+c-a,
\qquad
 g=b-a,
\qquad
\omega=1-c+a,
\qquad
r_0=\frac1{1+b}.
\]

The normalized centered insertion is

\[
gh_{p_*}(\eta_y)=B\eta_y-c.
\tag{1.1}
\]

Recall

\[
w(u)=e^{-\omega u}s_1(u),
\qquad
Z=\int_0^\infty w(u)\,du.
\]

Assignments 008--009 and Meetings 009--011 establish

\[
|Br_0-c|Z<\frac23,
\tag{1.2}
\]

and

\[
\kappa_T=B Z_{\omega+1+b}<1.
\tag{1.3}
\]

Meeting 012 now also establishes that the complete nearest-neighbour scalar edge-product/coboundary coupling Foster class is false at the strict near-East point

\[
(a,b,c)=\left(10^{-4},10^{-2},1-10^{-4}\right).
\]

I use none of the refuted Foster conclusions. In particular, the paragraph of Assignment 010 describing a future tensorization with G's hypothetical finite scalar Foster phase is obsolete. A positive profile theorem would now have to interface with some strictly stronger nonlocal/matrix-product coupling mechanism, or with a different route altogether.

## 2. Exact reverse transfer and suffix projectivity

Let

\[
\Lambda_N=\{1,\ldots,N\}
\]

with fixed zero boundary at `N+1`. Let `P_t^N` be the zero-boundary semigroup and `pi_N` its unique invariant law.

For a signed measure `nu` on `Lambda_N`, define the centered insertion/drop map

\[
(\mathcal J_N\nu)(f)
:=\nu\bigl((B\eta_N-c)f\bigr),
\qquad
f=f(\eta_1,\ldots,\eta_{N-1}).
\tag{2.1}
\]

The duration-resolved reverse transfer is

\[
\mathcal T_N(u)\nu
:=\mathcal J_N(\nu P_u^N).
\tag{2.2}
\]

This is the measure-side form of Assignment 009's operator-valued transfer.

For `M<=N`, let `R_{N,M}` denote marginalization onto the rightmost `M` sites, relabelled as `Lambda_M`.

### Proposition 2.1 (exact suffix intertwining)

For every `N>=M>=1`,

\[
\boxed{
R_{N,M}(\nu P_u^N)
=(R_{N,M}\nu)P_u^M.
}
\tag{2.3}
\]

For `M>=2`,

\[
\boxed{
R_{N-1,M-1}(\mathcal J_N\nu)
=
\mathcal J_M(R_{N,M}\nu).
}
\tag{2.4}
\]

Consequently

\[
\boxed{
R_{N-1,M-1}\mathcal T_N(u)
=
\mathcal T_M(u)R_{N,M}.
}
\tag{2.5}
\]

#### Proof

The rightmost `M` sites form an autonomous subsystem: every flip rate depends only on the current site and its right neighbour, which is either another site in the suffix or the common fixed zero boundary. Hence the suffix generator is exactly the `M`-site zero-boundary generator. This proves (2.3).

For (2.4), a test function on the rightmost `M-1` surviving sites depends, before deletion of site `N`, only on the rightmost `M` sites. Multiplication by `B eta_N-c` and summation over `eta_N` therefore commute with marginalization of all sites farther left. Combining the two identities gives (2.5). `square`

### Corollary 2.2 (finite transfer delay)

If two signed measures on `Lambda_N` have the same rightmost `M`-site marginal, then after any `k<=M` reverse transfers, with arbitrary durations, their rightmost `M-k` marginals agree. In particular, after `M` transfers their total signed masses are identical.

Thus a perturbation outside the retained `M`-site suffix is **exactly invisible to scalar trail output for the next `M` reverse transfers**. The issue in Assignment 010 is not local Markov closure over a finite number of steps. It is whether the profile which remains after those `M` transfers has sufficiently small future effect uniformly in the number of still-unprocessed sites.

## 3. Projective zero-boundary invariant law

Proposition 2.1 has an important invariant consequence.

### Proposition 3.1 (suffix consistency)

For every `N>=M`,

\[
\boxed{
R_{N,M}\pi_N=\pi_M.
}
\tag{3.1}
\]

#### Proof

The marginal `R_{N,M} pi_N` is invariant for the autonomous `M`-site suffix process by (2.3). Strict positive rates make that finite chain irreducible, so its invariant law is unique and equals `pi_M`. `square`

Relabel the rightmost site as `0`. The family `(pi_M)` therefore defines by Kolmogorov consistency a probability law

\[
\pi_\infty^0
\quad\text{on}\quad
\{0,1\}^{\mathbb Z_{\le0}}
\tag{3.2}
\]

whose rightmost `M`-site marginal is `pi_M`.

This projective half-line law is not asserted to be translation invariant. The fixed zero boundary is still visible near site `0`.

## 4. Depth-uniform truncation of one invariant centered insertion

Set

\[
Y:=B\eta_0-c.
\tag{4.1}
\]

For `M>=0`, let

\[
\mathcal F_M
=\sigma(\eta_{-M},\ldots,\eta_{-1}),
\]

with `F_0` trivial, and define

\[
K_M
:=E_{\pi_\infty^0}[Y\mid\mathcal F_M].
\tag{4.2}
\]

Let

\[
K_\infty
:=E_{\pi_\infty^0}
[Y\mid\sigma(\eta_j:j\le-1)].
\tag{4.3}
\]

### Theorem 4.1 (equilibrium profile truncation)

The finite-context coefficients satisfy

\[
K_M\longrightarrow K_\infty
\quad\text{in }L^1(\pi_\infty^0).
\tag{4.4}
\]

Moreover, defining

\[
\varepsilon_M
:=
\sup_{n\ge M}
\|K_n-K_M\|_{L^1(\pi_\infty^0)},
\tag{4.5}
\]

one has

\[
\boxed{
\varepsilon_M\longrightarrow0.
}
\tag{4.6}
\]

For every finite `N>=M+1` and every bounded function `F` of all sites strictly left of the rightmost site,

\[
\boxed{
\left|
\pi_N\bigl((B\eta_N-c)F\bigr)
-
\pi_N\bigl(K_M^{(N)}F\bigr)
\right|
\le
\varepsilon_M\|F\|_\infty,
}
\tag{4.7}
\]

where `K_M^{(N)}` is the translated copy of `K_M` depending only on

\[
\eta_{N-M},\ldots,\eta_{N-1}.
\]

#### Proof

The sequence `K_M` is the bounded martingale obtained by conditioning the fixed bounded variable `Y` on the increasing sigma-fields `F_M`. Levy's upward theorem gives (4.4) in `L^1`.

Hence the sequence is uniformly Cauchy in `L^1`: for `n>=M`,

\[
\|K_n-K_M\|_1
\le
\|K_n-K_\infty\|_1
+
\|K_M-K_\infty\|_1,
\]

and the supremum of the right side over `n>=M` tends to zero. This proves (4.6).

Under `pi_N`, the exact conditional expectation of `B eta_N-c` given the entire left block is the translated `K_{N-1}`, by the suffix consistency (3.1). Therefore

\[
\pi_N((B\eta_N-c)F)
=
\pi_N(K_{N-1}^{(N)}F).
\]

Subtract the local `K_M` approximation and use `|F|<=||F||_infty`. `square`

### Interpretation

This is a genuine depth-uniform profile truncation theorem at the first invariant insertion. It is stronger than a finite-order Markov approximation:

- `K_infty` may depend on the entire left half-line;
- Assignments 008--009 already show that no fixed finite static order is exact;
- nevertheless its finite-context conditional expectations approximate it uniformly in `L^1` over all finite interval depths.

No rate is claimed in (4.6). Martingale convergence supplies truncability but not the summable quantitative modulus needed for arbitrary repeated signed transfers.

## 5. A quantitative separated-gap theorem

The preceding theorem allows an arbitrary left function but gives no explicit rate. If the left function is actually separated from the rightmost site by a gap, there is an explicit exponential estimate.

Write

\[
\phi_N:=\eta_N-r_0,
\qquad
q_0:=1-r_0=\frac b{1+b}.
\tag{5.1}
\]

For a function `f` independent of `eta_N`, decompose the full generator as

\[
L_N f=L^0 f+\eta_N Df,
\tag{5.2}
\]

where `L^0` is the `(N-1)`-site generator with zero right boundary and `D=L^1-L^0` is the difference between boundary spin one and boundary spin zero at site `N-1`.

The rightmost spin is autonomous under zero boundary and

\[
L_N\phi_N=-(1+b)\phi_N.
\tag{5.3}
\]

Also

\[
\phi_N\eta_N=q_0(\phi_N+r_0).
\tag{5.4}
\]

Define

\[
\bar L:=L^0+q_0D.
\tag{5.5}
\]

This is again a Markov generator: its boundary flip rates are the convex combination of the fixed-zero and fixed-one boundary rates with weights `r_0,q_0`.

Stationarity applied to `phi_N g` gives the exact identity

\[
\boxed{
\pi_N\left[
\phi_N\bigl((1+b)-\bar L\bigr)g
\right]
=q_0r_0\,\pi_N[Dg].
}
\tag{5.6}
\]

For any bounded `f`, put

\[
g=((1+b)-\bar L)^{-1}f
=
\int_0^\infty e^{-(1+b)t}\bar P_t f\,dt.
\tag{5.7}
\]

Then

\[
\pi_N(\phi_N f)=q_0r_0\pi_N(Dg).
\tag{5.8}
\]

On the residual chamber `c>g=b-a`, and the two boundary-rate differences in `D` have magnitudes `c` and `g`. Hence

\[
|Dg|\le c\,\operatorname{osc}_{N-1}(g).
\tag{5.9}
\]

Suppose now that `f` is supported on sites at most `N-M`. A disagreement initially at site `N-1` can affect that support by time `t` only after crossing `M-1` successive nearest-neighbour edges. Under the rate-one graphical construction,

\[
\operatorname{osc}_{N-1}(\bar P_t f)
\le
2\|f\|_\infty
P(\operatorname{Pois}(t)\ge M-1).
\tag{5.10}
\]

For `lambda>0` and integer `m>=0`,

\[
\int_0^\infty
e^{-\lambda t}
P(\operatorname{Pois}(t)\ge m)\,dt
=
\frac1{\lambda(1+\lambda)^m}.
\tag{5.11}
\]

Putting `lambda=1+b` in (5.7)--(5.10) gives

\[
\boxed{
|\pi_N(\phi_N f)|
\le
\frac{2bc}
{(1+b)^3(2+b)^{M-1}}
\|f\|_\infty.
}
\tag{5.12}
\]

Since

\[
B\eta_N-c=(Br_0-c)+B\phi_N,
\]

we obtain:

### Theorem 5.1 (quantitative equilibrium defect localization)

If `supp(f) subset {1,...,N-M}`, then

\[
\boxed{
\left|
\pi_N\bigl((B\eta_N-c)f\bigr)
-(Br_0-c)\pi_N(f)
\right|
\le
\frac{2Bbc}
{(1+b)^3(2+b)^{M-1}}
\|f\|_\infty.
}
\tag{5.13}
\]

The estimate is uniform in `N` and decays exponentially in the spatial gap at every strict residual point.

This theorem shows concretely that the conditional/disagreement defect created by an equilibrium rightmost insertion is spatially localized. It does **not** yet control a trail profile carrying centered factors on every intervening site; in that case there is no blank gap to which (5.10) can be applied directly.

## 6. One-segment weighted spatial truncation is also easy

The standard one-sided finite-speed estimate gives, for a local function `f` and a semigroup in which the truncation boundary is `M` dependency steps away,

\[
\|P_u f-P_u^{(M)}f\|_\infty
\le
2\|f\|_\infty
H_M(u),
\qquad
H_M(u):=P(\operatorname{Pois}(u)\ge M).
\tag{6.1}
\]

Because `s_1(u)<=1`,

\[
\begin{aligned}
\int_0^\infty
w(u)H_M(u)\,du
&\le
\int_0^\infty
e^{-\omega u}H_M(u)\,du\\
&=
\frac1{\omega(1+\omega)^M}.
\end{aligned}
\tag{6.2}
\]

Therefore

\[
\boxed{
\int_0^\infty
w(u)
\|P_u f-P_u^{(M)}f\|_\infty\,du
\le
\frac{2}{\omega(1+\omega)^M}
\|f\|_\infty.
}
\tag{6.3}
\]

This estimate is pointwise in `u` before integration and therefore respects the Meeting 009 norm-order rule.

The obstruction is composition. Multiplication by the normalized centered insertion has sup norm

\[
\|B\eta-c\|_\infty=c
\]

on the residual chamber, so scalar telescoping of (6.3) through unrestricted later segments naturally introduces the one-step factor

\[
cZ>1,
\]

which Assignment 007 proves everywhere on the residual chamber. Thus one-segment finite propagation does not tensorize into the required all-depth profile estimate by scalar absolute values.

## 7. Where invariant truncation stops: the left marginal is not regenerated

Let

\[
\bar\pi_N
\]

denote the marginal of `pi_N` on sites `1,...,N-1`, and let `pi_N^1,pi_N^0` be the conditional left laws given `eta_N=1,0`. Since the rightmost density is `r_0`, the exact mass/disagreement decomposition gives

\[
\boxed{
\mathcal J_N\pi_N
=(Br_0-c)\bar\pi_N
+B r_0(1-r_0)(\pi_N^1-\pi_N^0).
}
\tag{7.1}
\]

The first coefficient is the uniformly contracting equilibrium mass coefficient, and Theorem 5.1 localizes the conditional difference on observables separated from the boundary.

However

\[
\boxed{
\bar\pi_N\ne\pi_{N-1}
}
\tag{7.2}
\]

generically. Assignment 008's two-site calculation is already an explicit example: the left-site density under `pi_2` differs from the one-site zero-boundary density `r_0` unless `a=b(1-c)`.

Thus even the **mass** branch returns not to the zero-boundary invariant family but to the next nonstationary boundary profile. This is the source of the growing common-mass hierarchy.

The projective martingale argument in Section 4 cannot simply be restarted after (7.1), because the new signed/profile measure is not `pi_{N-1}`.

## 8. Exact zero-frequency boundary-response formula

The failure in (7.2) has an exact representation which identifies the remaining analytic difficulty.

Let `f` be a function on `Lambda_{N-1}` and set

\[
h=f-\pi_{N-1}(f).
\]

Since the finite zero-boundary chain is irreducible, the Poisson integral

\[
G
:=
\int_0^\infty P_t^{N-1,0}h\,dt
\tag{8.1}
\]

is finite and solves

\[
-L^0G=h.
\tag{8.2}
\]

For `G` viewed as a function independent of `eta_N`, stationarity of `pi_N` and (5.2) give

\[
0=\pi_N(L^0G+\eta_NDG).
\]

Hence

\[
\boxed{
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND
\int_0^\infty
P_t^{N-1,0}
\bigl(f-\pi_{N-1}(f)\bigr)dt
\right].
}
\tag{8.3}
\]

Compare this with (5.7). The favorable equilibrium conditional-correlation estimate contains the resolvent parameter `1+b`; the mass boundary-shift formula (8.3) is a **zero-frequency resolvent**.

For a test function at distance `M` from the boundary, finite speed gives a factor

\[
P(\operatorname{Pois}(t)\ge M)
\]

for bounded `t`, but that probability tends to one as `t to infinity`. Thus

\[
\int_0^\infty
P(\operatorname{Pois}(t)\ge M)dt
=\infty.
\]

To make (8.3) uniformly small as `M to infinity`, one needs an additional uniform-in-volume temporal decay, a signed cancellation in the Green kernel, or a different nonlocal regeneration estimate. Finite speed and independent reset clocks alone, at the scalar variation level, do not supply it.

This is the precise point at which the easy profile truncation ends.

## 9. Relation to the favorable scalar modes

The zero-frequency obstruction does **not** mean that the mass hierarchy is expansive. The two scalar outputs already proved in Assignment 009 remain strictly damped:

\[
\kappa_E<\frac23,
\qquad
\kappa_T<1.
\]

What is missing is a norm on the entire boundary-response hierarchy in which these two losses dominate the flow of higher modes into the next rightmost transient. Equation (8.3) is the first higher-mode response.

A successful continuation could therefore take one of two forms.

1. Prove a profile Green-kernel estimate strengthening (8.3), with a spatial tail summable uniformly in volume and compatible with the `L^1(w)` transfer.
2. Construct a genuinely nonlocal/matrix-valued signed norm in which the boundary-profile response and the conditional-law disagreement excursion are controlled together.

The first option would be a direct profile truncation theorem. The second would merge F's profile side with whatever stronger coupling mechanism survives G's current viability test.

## 10. Effect of G Assignment 005 / Meeting 012

Meeting 011's proposed three-way composition was:

1. G finite all-height coupling Foster return;
2. finite-`M` signed control;
3. profile truncation error `delta_M to 0`.

The first item no longer exists in the nearest-neighbour scalar class. Meeting 012 proves by an exact balanced circulation that every positive scalar edge matrix and every restart tilt `s>1` has a positive bulk cycle at one strict residual point.

Therefore Assignment 010 should **not** be weakened or abandoned, but its eventual interface changes:

- the common-mass truncation theorem remains independently necessary;
- there is no finite scalar coupling phase over which to demand uniformity;
- any eventual tensorization must use a stronger noncommutative/nonlocal coupling state, if the common-uniform coupling survives G's new extinction test at all.

The results of Sections 2--8 are independent of that coupling decision.

## 11. What is proved versus open

### Proved here

1. exact suffix/projective intertwining for the duration-resolved signed transfer;
2. projective consistency of the finite zero-boundary invariant laws;
3. depth-uniform `L^1` finite-context truncation of the **first invariant centered insertion**;
4. an explicit exponentially decaying separated-gap bound for its conditional/disagreement defect;
5. an explicit `J`-weighted one-segment finite-speed truncation bound;
6. the exact zero-frequency boundary-response formula for the mass-profile shift.

### Still open

The Assignment-010 target requires a depth-uniform estimate after arbitrary signed profile evolution. Equivalently, one must control the repeated post-insertion boundary-response hierarchy in a norm which preserves the fixed-duration cancellations and does not reduce to the expansive scalar factor `cZ`.

G's two refuted local Foster architectures show that the missing norm cannot simply be supplied by a commutative local restart credit system.

## 12. Handoff

`unresolved after substantive work; exact profile-tail blocker: the equilibrium reverse insertion itself is depth-uniformly truncatable. The zero-boundary invariant laws are suffix-projective, so K_M=E[B eta_0-c | eta_{-M},...,eta_{-1}] converges in L1 to the full-past coefficient with sup_{n>=M}||K_n-K_M||_1 -> 0, and therefore every finite-depth invariant insertion can be replaced by its M-context coefficient with an error epsilon_M||F||_infty uniform in the total interval depth. There is also the explicit separated-gap estimate |pi_N((B eta_N-c)f)-(Br_0-c)pi_N(f)| <= 2Bbc[(1+b)^3(2+b)^{M-1}]^{-1}||f||_infty and the one-segment weighted finite-speed tail 2/[omega(1+omega)^M]. The obstruction is iteration: after the first insertion the mass branch carries the nonstationary left marginal bar pi_N rather than pi_{N-1}, with exact zero-frequency boundary response bar pi_N(f)-pi_{N-1}(f)=pi_N[eta_N D int_0^infty P_t^{N-1,0}(f-pi_{N-1}f)dt]. Finite speed has no integrable long-time factor here, while scalar L1 composition costs cZ>1. Meeting 012 also refutes the complete nearest-neighbour scalar coupling product/coboundary class, so no finite scalar Foster phase remains to control this post-insertion hierarchy. A genuinely signed profile Green-kernel estimate or a nonlocal/matrix-product coupling/profile norm is still required.`
