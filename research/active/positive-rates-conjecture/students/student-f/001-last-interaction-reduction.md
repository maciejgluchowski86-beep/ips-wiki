# Student F 001: last-successful-interaction / trail / Duhamel reconstruction

## Executive conclusion

I reconstructed the principal's old route far enough to identify the exact three-generator algebra, the exact trail factor, the boundary convention hidden in the barrier--scaffold picture, and the sign that the remembered "high density" statement would actually have to control.

The main new point is stronger than a qualitative density guess but does not yet close the proof. In the complemented spin convention, put

\[
B=b+c-a,
\qquad
\rho=\frac{c}{B}.
\]

At a successful rightward dual interaction, if the birth-versus-jump type is *not* revealed, its signed type average is exactly

\[
B\eta_i-c=B(\eta_i-\rho).
\]

After deleting the environment-independent noise of rate `a`, the resulting spin system `L^-` has an explicit one-sided conditional high-density estimate: for every initial configuration, every site `i`, and every realization of the graphical history strictly to the right of `i`,

\[
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
q(t):=\frac{1-e^{-(1-c)t}}{1+b-a}.
\]

In particular, after the finite burn-in

\[
T_\rho
=
\frac{1}{1-c}
\log\frac{B}{(b-a)(1-c)},
\]

one has `q(t)>=rho`, hence

\[
\mathbb E^-[(B\eta_i(t)-c)F]\ge0
\]

for every nonnegative `F` measurable with respect to the right-hand history. This is a genuine finite-time estimate and does not assume ergodicity.

What remains unresolved is exactly whether the last-exit/scaffold regrouping turns the companion factor at the hidden successful interaction into such a right-measurable nonnegative functional. The raw Duhamel gradient does not have this property: even for the one-site observable `f(eta)=eta_{i-1}`, its first-order gradient at site `i` already depends on `eta_{i-1}`. A patchwise fallback is impossible in the hard subregion `a>b(1-c)`, because sufficiently long outgoing-to-incoming patches of the original system have negative averaged contribution even at terminal value `1`.

Thus the old route is not disproved, but the vague density premise has been replaced by a precise conditional insertion threshold and a precise missing regional-factorization statement.

## 1. Source-normalized residual chamber

The authoritative target is the positive-rates conjecture for simple IPS. On the normalized face used in the active proof spine,

\[
r_{11}=0,
\qquad
r_{10}=c,
\qquad
r_{01}=b,
\qquad
r_{00}=a,
\]

and the source-corrected unresolved chamber is

\[
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
\tag{1.1}
\]

In the principal's old spin convention `xi`, the actual flip rates are

\[
q_{00}=a,
\qquad q_{01}=b,
\qquad q_{10}=1-c,
\qquad q_{11}=1.
\tag{1.2}
\]

The signed monomial duality function in the barrier--scaffold note is

\[
H(A,\sigma,\xi)
=
\sigma\prod_{i\in A}(1-\xi_i).
\tag{1.3}
\]

I will also use the complemented spin

\[
\eta_i=1-\xi_i,
\tag{1.4}
\]

so that `H` becomes the canonical monomial duality function `prod eta_i` of the patch paper.

Set throughout

\[
B:=b+c-a.
\tag{1.5}
\]

Since `a<b`, one has `B>c>0` and hence

\[
0<\rho:=\frac{c}{B}<1.
\tag{1.6}
\]

### 1.1 Primary-source boundary check

I rechecked the two load-bearing published statements rather than using the 2026 paper's prose summary of the older region. The 2025 Głuchowski--Menz Corollary 7.2 applies, on the normalized face `r11=0`, when `b<=a`; hence the live chamber must indeed lie on `a<b`. The 2026 long-lived-state theorem, applied to state `0` in the residual ordering where `c` is the largest update probability and `b>a`, has

\[
\beta=1-c,
\qquad
\delta=b,
\]

and therefore covers `b<sqrt(2)(1-c)`. Thus the active chamber's opposite inequality `b>=sqrt(2)(1-c)` is the correct side of that theorem. The remaining reductions `c>=a+b` and `c>=1/2` are inherited from the source-corrected time-scaling/state-symmetry reduction already audited in the preceding programme; none of the arguments below relaxes them.

## 2. Literal correction to the surviving barrier--scaffold calculation

The supplied `sips_barrier_scaffold_polished.tex` contains the right dual rates and the right Feynman--Kac potential, but the displayed raw formula for `L_i H` omits one diagonal term.

For `i in A`, the correct identity is

\[
\begin{aligned}
\mathcal L_i H(A)
={}&
 c_{11}H(A\setminus\{i\})
 +(c_{11}-c_{10}+c_{01}-c_{00})H(A\cup\{i+1\})
\\
&+(c_{10}-c_{11})H((A\setminus\{i\})\cup\{i+1\})
-(c_{11}+c_{01})H(A).
\end{aligned}
\tag{2.1}
\]

The note has only `-c_{01}H(A)` in the last line. The missing `-c_{11}H(A)` is forced, for example, by evaluating at `xi_i=0,xi_{i+1}=1`: the actual flip `0->1` occurs at rate `c_{01}`, so the local generator must equal `-c_{01}H(A)`, while the displayed formula in the note gives `(c_{11}-c_{01})H(A)`.

The later potential in the note is nevertheless already the corrected one,

\[
V(A)=(-c_{11}-c_{01}+\delta+\beta+\lambda)|A|,
\]

so this is a local derivation error rather than a change to the subsequent dual parameters.

There is also a small barrier-interval typo. If consecutive barrier times satisfy `u_{i+1}<=u_i`, the certified absence interval is `(u_{i+1},u_i]` (up to endpoint convention), not `[u_i,u_{i+1})`.

## 3. Exact signed dual and the three spin generators

Substituting (1.2) into (2.1), the signed dual has at each active site

\[
\delta=1,
\qquad
\beta=B=b+c-a,
\qquad
\lambda=c,
\tag{3.1}
\]

with signs

\[
\sigma_\delta=+,
\qquad
\sigma_\beta=+,
\qquad
\sigma_\lambda=-.
\tag{3.2}
\]

The original Feynman--Kac potential is

\[
V(A)=(2c-a)|A|.
\tag{3.3}
\]

The two auxiliary flip-rate tables from the old note become

\[
q^-_{00}=0,
\quad q^-_{01}=b-a,
\quad q^-_{10}=1-c,
\quad q^-_{11}=1,
\tag{3.4}
\]

and

\[
q^+_{00}=0,
\quad q^+_{01}=b+2c-a,
\quad q^+_{10}=1+c,
\quad q^+_{11}=1.
\tag{3.5}
\]

The `-` system has the same signed set process and potential

\[
V^-(A)=2c|A|,
\tag{3.6}
\]

whereas the `+` system has the same set-valued transitions with all signs positive and no Feynman--Kac potential.

There is a more useful spin-side formulation. Define, in the old `xi` convention,

\[
(N^\uparrow f)(\xi)
=
\sum_i 1_{\{\xi_i=0\}}
\bigl(f(\xi^i)-f(\xi)\bigr),
\tag{3.7}
\]

and the one-sided copy-right generator

\[
(Cf)(\xi)
=
\sum_i 1_{\{\xi_i\ne\xi_{i+1}\}}
\bigl(f(\xi^i)-f(\xi)\bigr).
\tag{3.8}
\]

At a domain wall, the flip in (3.8) is exactly `xi_i <- xi_{i+1}`. Direct comparison of the four local rates gives

\[
\boxed{L=L^-+aN^\uparrow},
\qquad
\boxed{L^+=L^-+2cC}.
\tag{3.9}
\]

Thus the two perturbations appearing in the remembered argument are elementary:

- deleting the `a`-noise gives `L^-`;
- erasing the negative dual sign adds copy-right updates at domain walls and gives `L^+`.

This is not a change of representation; it identifies the exact Markov generators whose semigroups have to be compared after duality is undone.

## 4. Exact boundary dictionary for undoing duality

The corrected monomial formula also identifies the spin boundary rules in the scaffold picture.

Suppressing every successful dual interaction from site `i` to `i+1` leaves, for an active source `i`,

\[
c_{11}H(A\setminus\{i\})-(c_{11}+c_{01})H(A).
\tag{4.1}
\]

This is exactly the local monomial generator of the original spin system with the right neighbour fixed to `xi_{i+1}=1`, equivalently `eta_{i+1}=0`.

On the other hand, when a predecessor tube forces the target `i+1` to remain dual-active, factoring the common target monomial gives the source generator

\[
c_{10}H(A\setminus\{i\})-(c_{10}+c_{00})H(A),
\tag{4.2}
\]

which is the spin system with right neighbour fixed to `xi_{i+1}=0`, equivalently `eta_{i+1}=1`.

Therefore the white regions in a repaired scaffold decomposition do not all have the same frozen boundary. Their right boundary pieces switch between canonical boundary values `eta=0` and `eta=1` according to whether the drawn edge certifies no crossing or a forced-active predecessor tube. This is the dynamic-boundary rule that later appears in the Duhamel identity.

## 5. The trail factor is exactly the deleted-noise survival factor

The original and noise-reduced systems have the same signed dual jump process. Only the potential changes:

\[
V=V^- - a|A|.
\]

Hence for every realization of the signed dual,

\[
\sigma_t
\exp\left(\int_0^t V(A_s)\,ds\right)
=
\exp\left(-a\int_0^t |A_s|\,ds\right)
\sigma_t
\exp\left(\int_0^t V^-(A_s)\,ds\right).
\tag{5.1}
\]

If a revealed ancestry trail certifies at least one active dual site at every time in an interval of length `u`, (5.1) supplies the factor

\[
e^{-au}.
\tag{5.2}
\]

The patch paper gives an exact patchwise statement. In the complemented convention the original process is

\[
L=L^-+a\mathcal N^0,
\]

where `a N^0` is a uniform `eta:1->0` pure-death component. For every patch `P` whose terminal boundary is outgoing,

\[
C_L(P)
=
e^{-a(e(P)-s(P))}C_{L^-}(P).
\tag{5.3}
\]

Along a backward predecessor chain of outgoing-terminal patches, the patch lifetimes add. If the chain spans time `u`, then

\[
\prod_{P\in\Gamma} C_L(P)
=
e^{-au}
\prod_{P\in\Gamma} C_{L^-}(P).
\tag{5.4}
\]

This is precisely the positive exponential trail term in the principal's recollection.

## 6. Exact Duhamel identity and a directional-wall refinement

Let `I` be a finite interval, and prescribe an arbitrary cadlag right-boundary path `z(u) in {0,1}` in the canonical `eta` convention. Use the same path for `L^-` and `L^+`. Let `U^-_{s,t}` and `U^+_{s,t}` be the resulting time-inhomogeneous evolution operators, and let `C_u` denote copy-right with the boundary value `z(u)` at the endpoint.

From (3.9), differentiation of

\[
u\longmapsto U^-_{s,u}U^+_{u,t}
\]

gives the exact identity

\[
\boxed{
U^-_{s,t}-U^+_{s,t}
=
-2c\int_s^t U^-_{s,u}C_uU^+_{u,t}\,du.
}
\tag{6.1}
\]

This is the ordinary spin-semigroup remainder that remains after the signed dual is undone.

There is a useful refinement of the crude absolute-value bound. In canonical spins, `L^+` has local rates

\[
\begin{array}{c|cc}
\eta_{i+1} & 0\to1 & 1\to0\\ \hline
0 & 1 & B+c\\
1 & 1+c & 0,
\end{array}
\]

so `L^+` is attractive. Hence if `f` is increasing, so is `g=U^+_{u,t}f`. At a wall `01`, copy-right changes the source from `0` to `1`, while at a wall `10` it changes it from `1` to `0`. Therefore

\[
C_ug(\eta)
\le
\sum_i
1_{\{\eta_i=0,\eta_{i+1}=1\}}
\operatorname{osc}_i g
\le
\sum_i1_{\{01\}_i}
\tag{6.2}
\]

for `0<=g<=1`. Thus, for increasing `0<=f<=1`,

\[
U^-_{s,t}f
\ge
U^+_{s,t}f
-
2c\int_s^t
U^-_{s,u}
\left(\sum_i1_{\{01\}_i}\right)
\,du.
\tag{6.3}
\]

The naive Duhamel error is therefore controlled by **oriented domain walls**, not by a generic local discrepancy. This makes precise one part of the principal's memory: a high density of canonical `1` spins can make the bad term small. It does not yet make the last-exit expansion summable.

## 7. The hidden successful-interaction type exposes the exact density threshold

The canonical monomial action of the original generator is, for `i in A`,

\[
\begin{aligned}
L_i\chi_A
={}&
\chi_{A\setminus\{i\}}
-(1+b)\chi_A
-c\chi_{(A\setminus\{i\})\cup\{i+1\}}
+B\chi_{A\cup\{i+1\}}.
\end{aligned}
\tag{7.1}
\]

The noise-reduced generator has the same nonempty-target terms:

\[
\begin{aligned}
L^-_i\chi_A
={}&
\chi_{A\setminus\{i\}}
-(1+b-a)\chi_A
-c\chi_{(A\setminus\{i\})\cup\{i+1\}}
+B\chi_{A\cup\{i+1\}}.
\end{aligned}
\tag{7.2}
\]

At a revealed successful interaction `i -> i+1`, there are two local dual types:

- the source-retaining type has coefficient `+B`;
- the source-removing type has coefficient `-c`.

If the interaction time/source/target is revealed but its type is left hidden, the common target factor can be pulled out and the type average at the source is

\[
B\eta_i-c
=
B(\eta_i-\rho),
\qquad
\rho=\frac{c}{B}.
\tag{7.3}
\]

This is the exact algebraic content of "high density" in the old route.

For a nonnegative companion factor `F`, the required sign is

\[
\mathbb E[\eta_iF]
\ge
\rho\,\mathbb E[F].
\tag{7.4}
\]

Thus a marginal lower bound `E eta_i >= rho` is sufficient only when `F` is independent of, or appropriately measurable away from, the source. In general the correct object is a **monomial insertion inequality**.

A sufficient cone is the centered-moment cone

\[
\mathcal M_\rho
=
\left\{
\mu:
\mu\!\left(\prod_{j\in S}(\eta_j-\rho)\right)\ge0
\text{ for every finite }S
\right\}.
\tag{7.5}
\]

Indeed, if `i notin A`, then

\[
\begin{aligned}
\mu(\chi_{A\cup\{i\}})-\rho\mu(\chi_A)
&=
\mu\!\left((\eta_i-\rho)\prod_{j\in A}\eta_j\right)
\\
&=
\sum_{S\subseteq A}
\rho^{|A|-|S|}
\mu\!\left(\prod_{j\in S\cup\{i\}}(\eta_j-\rho)\right)
\ge0.
\end{aligned}
\tag{7.6}
\]

The point is not to replace the problem by the cone (that would be another reformulation). The next section gives a direct finite-time estimate at exactly the threshold `rho`.

## 8. Uniform right-conditioned high density for the noise-reduced system

This is the strongest positive result of this block.

### Lemma 8.1 (right-conditioned one-site lower bound)

Consider the noise-reduced system `L^-` in canonical spins. For a site `i`, let `F^+_{i,t}` be the sigma-field generated by the initial spins strictly to the right of `i` and by all graphical marks at sites `j>=i+1` up to time `t`. Then, for every deterministic initial configuration,

\[
\boxed{
\mathbb P^-_\eta
\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
q(t)
:=
\frac{1-e^{-(1-c)t}}{1+b-a}
}
\tag{8.1}
\]

almost surely. The same bound holds for any initial law after conditioning on its initial configuration.

#### Proof

One-sidedness is essential: the right-hand graphical history is autonomous and, once it is fixed, `eta_i` is a two-state time-inhomogeneous Markov chain driven by the prescribed path

\[
z(u)=\eta_{i+1}(u)\in\{0,1\}.
\]

Write

\[
p(u)=
\mathbb P^-(\eta_i(u)=1\mid\mathcal F^+_{i,u}).
\]

From the rate table (3.4) after complementing spins:

- when `z=0`, the source rates are `0->1` at rate `1` and `1->0` at rate `b-a`, so
  \[
  p'=1-(1+b-a)p;
  \tag{8.2}
  \]
- when `z=1`, the rates are `0->1` at rate `1-c` and `1->0` at rate `0`, so
  \[
  p'=(1-c)(1-p).
  \tag{8.3}
  \]

Put

\[
p_0=\frac1{1+b-a},
\qquad
k=1-c,
\qquad
q(u)=p_0(1-e^{-ku}).
\tag{8.4}
\]

The worst initial condition has `p(0)=0=q(0)`. At a first contact `p=q`, the drift in (8.2) is

\[
1-(1+b-a)q=e^{-ku}
\ge kp_0e^{-ku}=q'(u),
\tag{8.5}
\]

and the drift in (8.3) is

\[
k(1-q)
\ge kp_0e^{-ku}=q'(u).
\tag{8.6}
\]

Scalar comparison, valid across the switching times of `z`, gives `p(u)>=q(u)` for all `u`. This proves (8.1). `square`

### Corollary 8.2 (explicit burn-in to the hidden-type threshold)

One has

\[
p_0-\rho
=
\frac{(b-a)(1-c)}{B(1+b-a)}>0.
\tag{8.7}
\]

Consequently

\[
q(t)\ge\rho
\qquad\text{for all }t\ge T_\rho,
\tag{8.8}
\]

where

\[
\boxed{
T_\rho
=
\frac1{1-c}
\log\frac{B}{(b-a)(1-c)}.
}
\tag{8.9}
\]

Therefore for every nonnegative `F` measurable with respect to `F^+_{i,t}`,

\[
\boxed{
\mathbb E^-_\eta[(B\eta_i(t)-c)F]
\ge
B(q(t)-\rho)\,\mathbb E^-_\eta[F]
\ge0,
\qquad t\ge T_\rho.
}
\tag{8.10}
\]

This is an actual one-way quantitative estimate. It is uniform in the initial configuration and in the complete realized right-hand history, and it is proved by a one-site ODE. No invariant measure, finite-volume mixing, or ergodicity input is used.

A useful fixed-time consequence is that, for any finite set `A` lying strictly to the right of `i`,

\[
\mathbb E^-_\eta[\eta_i(t)\chi_A(\eta(t))]
\ge q(t)\mathbb E^-_\eta[\chi_A(\eta(t))].
\tag{8.11}
\]

Iterating from the leftmost site gives

\[
\mathbb E^-_\eta[\chi_A(\eta(t))]
\ge q(t)^{|A|}
\tag{8.12}
\]

for every finite `A`. The direction matters: (8.11) is automatic when all factors are to the right of the inserted source, but it says nothing by itself about factors lying to the left.

## 9. Dynamic-boundary centered cone for `L^-`

The same threshold `rho` appears in a second independent calculation.

Consider `L^-` on a finite interval with an arbitrary prescribed right-boundary path `z(t) in {0,1}`. Put `g_j=eta_j-rho`. In the interior, the patch-positivity calculation for `L^-` implies that the generator matrix in the centered-monomial basis has nonnegative off-diagonal coefficients.

At the right endpoint the only extra calculation is one-dimensional. If `z=0`,

\[
L^-g_r
=
h-(1+b-a)g_r,
\]

while if `z=1`,

\[
L^-g_r
=
h-(1-c)g_r,
\]

with the same source term in both cases:

\[
\boxed{
h
=
\frac{(b-a)(1-c)}{B}>0.
}
\tag{9.1}
\]

Thus every instantaneous finite-volume generator, for either boundary value, is Metzler in the `rho`-centered monomial basis. Products of the corresponding positive evolution operators show:

> If the initial finite-volume law belongs to `M_rho`, then it remains in `M_rho` under `L^-` for every prescribed switching right-boundary path.

This is stronger than a fixed-boundary statement and matches the scaffold geometry exactly. It is still not enough for the original process, because the original dynamics does not preserve this cone in the hard subregion.

Indeed the corresponding original boundary source coefficient is

\[
h_{\mathrm{orig}}
=
\frac{b(1-c)-a}{B},
\tag{9.2}
\]

again independent of whether the boundary is `0` or `1`. Hence it is nonnegative exactly when

\[
a\le b(1-c).
\tag{9.3}
\]

Moreover

\[
h-h_{\mathrm{orig}}=a\rho.
\tag{9.4}
\]

This is the generator-level reason the deleted noise repairs the sign.

## 10. Patch audit: why patchwise absolute values cannot complete the hard subregion

For the original process in canonical spins,

\[
c^0(\varnothing)=1,
\quad c^0(\{1\})=-c,
\qquad
c^1(\varnothing)=b,
\quad c^1(\{1\})=a-b.
\tag{10.1}
\]

The no-successful-interaction one-site relaxation is

\[
\psi(\Delta,z)
=
\frac{1}{1+b}
+
\left(z-\frac{1}{1+b}\right)e^{-(1+b)\Delta}.
\tag{10.2}
\]

For an outgoing patch ending incoming (or as an end patch), the sign is controlled by

\[
N(\Delta,z)
=-c+B\psi(\Delta,z).
\tag{10.3}
\]

For a completed OI patch, `z=1`, and

\[
\lim_{\Delta\to\infty}N(\Delta,1)
=
\frac{b(1-c)-a}{1+b}.
\tag{10.4}
\]

Therefore the original process is patch positive exactly on the side

\[
a\le b(1-c),
\tag{10.5}
\]

whereas in the hard side

\[
a>b(1-c)
\tag{10.6}
\]

sufficiently long OI patches have negative averaged weight even with terminal value `1`.

The zero occurs at

\[
\Delta_*
=
\frac1{1+b}
\log\frac{bB}{a-b(1-c)}.
\tag{10.7}
\]

For example,

\[
(a,b,c)=(0.001,0.011,0.999)\in\mathcal R
\]

has `B=1.009` and `Delta_* about 2.392`.

This does **not** disprove a coarser scaffold cancellation. It proves a narrower and useful negative statement: after conditioning on the full successful skeleton, one cannot take patchwise absolute values or dominate each original patch by a positive `L^-` patch on the hard side. Any surviving old proof must leave enough interaction information hidden to cancel across more than one patch/region.

For `L^-`, in contrast, the patch criterion holds throughout `R` and its threshold profile is exactly

\[
p_*^-=\rho=\frac{c}{B}.
\tag{10.8}
\]

The agreement of (7.3), (9.1), and (10.8) is not accidental: the same insertion threshold controls hidden interaction types, centered moments, and long-patch signs.

## 11. What the barrier--scaffold conditioning can safely reveal

The old note conditions on the barrier, scaffold, interaction **types**, and certifying absence intervals. That is too much information for the sign argument.

The canonical patch construction keeps the successful interaction time/source/target but does not reveal whether the outgoing mark was the positive source-retaining type or the negative source-removing type. The average of those two types is exactly (7.3). Revealing the type first destroys this cancellation.

A repaired scaffold construction should therefore reveal:

- the successful interaction locations and times needed to define the barrier;
- predecessor relations and the forced-active tubes;
- the certified no-crossing intervals;

but should leave the birth-versus-jump kind hidden at least until the relevant regional spin expectation has been formed.

The canonical patch factorization justifies conditional independence after refining spacetime into local patches. It does not automatically identify each coarse white scaffold region with a standard spin semigroup. For that, one still has to assign the shared successful boundary marks and prove the exact dynamic-boundary evolution operator produced by summing the hidden patch histories.

## 12. The exact remaining obstruction: the companion factor is not automatically right-measurable

Corollary 8.2 would close the local sign at a hidden interaction if its nonnegative companion factor were measurable with respect to the right-hand history. The barrier geometry makes this plausible for the branch that continues through the target, but other active branches can remain to the left of the source.

The raw Duhamel formula shows that this is a real issue rather than a formal concern.

Take the increasing local observable

\[
f(\eta)=\eta_{i-1}.
\]

For `L^+`, a direct generator calculation gives

\[
L^+\eta_{i-1}
=
1-(1+B+c)\eta_{i-1}
+c\eta_i
+B\eta_{i-1}\eta_i.
\tag{12.1}
\]

Hence, with `D_i g(eta)=g(eta^{i,1})-g(eta^{i,0})`,

\[
D_i(U_t^+f)
=
t(c+B\eta_{i-1})+O(t^2).
\tag{12.2}
\]

Already at first order the Duhamel gradient at source `i` depends on the **left** spin `eta_{i-1}`. Therefore the right-conditioned estimate (8.10) cannot simply be inserted into the ungrouped Duhamel integral.

This pinpoints the first missing theorem in the old route:

> **Regional measurability/cancellation problem.** After revealing only the barrier/scaffold geometry and no-crossing data, while keeping the successful birth-versus-jump types hidden, does summing the remaining histories in the region adjacent to a trail interaction produce a nonnegative companion kernel depending only on the right-hand history of the source (or, more generally, a kernel satisfying the insertion inequality (7.4))?

If yes, the explicit burn-in `T_rho` makes the hidden interaction nonnegative. If no, the old high-density route needs a different cancellation mechanism.

This is finite-region mathematics. It can be tested on the smallest scaffold cell containing one trail interaction and one left predecessor branch; no infinite-time or invariant-measure statement is needed to formulate it.

## 13. A secondary finite-box estimate on the subregion `B<1`

There is another genuine high-density estimate for `L^-` that may be useful if the Professor chooses to keep this route alive.

Return to old spins `xi` and let `I=[ell,r]`. Include the prescribed right boundary value `y(t)=xi_{r+1}(t)` when counting oriented pairs. Write `n_{01},n_{10},n_{11}` for the numbers of corresponding adjacent patterns with source in `I`, and let

\[
N=\sum_{i\in I}\xi_i=n_{10}+n_{11}.
\]

Telescoping the binary string gives

\[
n_{01}-n_{10}=y-\xi_\ell.
\tag{13.1}
\]

For `L^-`, births of old `1` occur on `01` at rate `b-a`, while deaths occur on `10` at rate `1-c` and on `11` at rate `1`. Hence

\[
\begin{aligned}
L^-N
&=(b-a)n_{01}-(1-c)n_{10}-n_{11}
\\
&=(B-1)n_{10}-n_{11}+(b-a)(y-\xi_\ell).
\end{aligned}
\tag{13.2}
\]

If `B<1`, put `kappa=1-B>0`. Since then `kappa<1`,

\[
\boxed{
L^-N\le -\kappa N+(b-a)y.
}
\tag{13.3}
\]

Thus for arbitrary boundary path,

\[
\mathbb E N_t
\le
e^{-\kappa(t-s)}\mathbb E N_s
+
\frac{b-a}{\kappa}.
\tag{13.4}
\]

With boundary `y=0` the second term vanishes; with arbitrary boundary it is `O(1)` independent of `|I|`. Therefore after burn-in the old-`1` density in a large box is `O(1/|I|)` uniformly in the boundary path.

This is the sort of finite-box density statement the principal remembered. It is independently provable and strictly weaker than ergodicity. At present it does not close the full route because the regional kernel problem in Section 12 remains upstream of any density estimate.

## 14. Consistency check: the Bernoulli slice is exactly the sign boundary

This is a by-product, not the main route.

Suppose the normalized original process has a homogeneous Bernoulli invariant law with old-spin one-density `p`. The stationarity equations for `xi_0` and `xi_0xi_1` give

\[
p=\frac{b}{1+b},
\qquad
\boxed{a=b(1-c)}.
\tag{14.1}
\]

Conversely, on the slice `a=b(1-c)`, the Bernoulli law with `p=b/(1+b)` is invariant: conditional on either right-neighbour value, an asynchronous local update preserves the same one-site Bernoulli marginal.

Thus the following four boundaries coincide:

1. Bernoulli stationarity of the normalized simple IPS;
2. patch positivity of the original process;
3. nonnegativity of the dynamic-boundary centered source coefficient (9.2);
4. the limiting OI-patch sign in (10.4).

A 2026 entropy theorem of Marcovici--Taati proves exponential ergodicity for finite-range positive-rate IPS that admit a stationary Bernoulli measure. The normalized representative has a zero one-step output probability at the `11` environment, but replacing its local transition rule by

\[
P_\theta=\theta P+(1-\theta)I,
\qquad 0<\theta<1,
\tag{14.2}
\]

makes every output probability strict while multiplying the continuous-time generator by `theta`. Therefore the codimension-one slice (14.1) is already exponentially ergodic by that theorem after this harmless time rescaling.

This does not resolve an open subset of `R`, but it is a useful independent check of the algebra and removes the equality case from any future sign analysis.

## 15. Anti-circularity audit

### 15.1 What exact previous statement does this replace?

The previous live statement was the principal's unverified recollection

\[
\text{eventual high density of one state}
\Longrightarrow
\text{ergodicity}.
\]

The present block replaces "high density" by the exact hidden-type factor `B(eta_i-rho)` and proves the uniform right-conditioned lower bound (8.1)--(8.10) for `L^-`.

### 15.2 What implication is one-way rather than definitional?

The proved implication

\[
t\ge T_\rho,
\quad F\ge0\text{ right-history measurable}
\quad\Longrightarrow\quad
\mathbb E^-[(B\eta_i(t)-c)F]\ge0
\tag{15.1}
\]

is a real estimate, not a change of variables. It follows from a scalar comparison ODE and is uniform over initial configurations and right-boundary histories.

I have **not** proved `Q => ergodicity`, because the scaffold has not yet been shown to produce a companion factor to which (15.1) applies.

### 15.3 Why is the remaining premise technically easier or more local?

The missing statement in Section 12 is a finite scaffold-cell identity/inequality. It concerns integration of finitely many Poisson marks in a bounded spacetime region with prescribed boundary data. It can be proved or falsified without knowing any invariant measure.

### 15.4 What estimate would prove it without already proving ergodicity?

Take the smallest scaffold cell in which a hidden successful interaction has a left predecessor branch. Sum all unrecorded interaction kinds and local marks while fixing the revealed successful times and no-crossing data. Prove that the resulting companion kernel is either

\[
F\ge0\quad\text{and right-history measurable},
\]

or at least satisfies

\[
\mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F]
\tag{15.2}
\]

for `t>=T_rho`. This is finite-dimensional.

### 15.5 What concrete calculation distinguishes this from disguised convergence?

At `(a,b,c)=(0.001,0.011,0.999)`, a single OI patch becomes negative at length about `2.392`, so the missing regional grouping is already nontrivial on a bounded cell. Conversely, (8.10) is already valid after the explicit finite burn-in `T_rho`, independently of whether the infinite system converges.

## 16. Recommended next block

Do **not** return to fixed frozen walls or optimize one-attack constants.

The next calculation should be the minimal two-branch scaffold cell suggested by Section 12:

1. reveal a successful interaction `i->i+1` and the predecessor relation that makes its source active;
2. keep the successful birth-versus-jump type hidden;
3. sum every other mark in the two adjacent white regions using the corrected boundary dictionary of Section 4;
4. express the result as a finite spin kernel under `L^-`;
5. test whether its companion factor is right-measurable/nonnegative, or whether it obeys (15.2);
6. if it fails, produce the smallest explicit counterexample and close the old route; if it succeeds, iterate the same kernel along the ancestry trail and combine with the exact `e^{-au}` factor.

The key point is that the density part is no longer conjectural: (8.10) supplies it whenever the regional kernel has the required one-sided measurability.

## Handoff

`unresolved after substantive work; exact blocker: the noise-reduced one-sided system satisfies an explicit uniform right-conditioned insertion estimate after T_rho, but the last-exit/scaffold decomposition has not yet been proved to turn the hidden successful-interaction companion factor into a right-measurable (or rho-insertion-positive) regional kernel; the raw Duhamel gradient already depends on left spins, while patchwise absolute-value domination is impossible for a>b(1-c) because long OI patches are negative.`
