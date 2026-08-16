# Student F 008: bounded-height signed mass/disagreement kernel

## Verdict

Meeting 008 splits the remaining block theorem into a coupling-side Foster lift `(FL)` and a bounded-height signed kernel. I treat `(FL)` only as the conditional premise authorized in Assignment 008.

The bounded signed problem does have a new favorable exact estimate:

\[
\boxed{
|B r_0-c|\,Z<\frac23
}
\]

at every strict residual parameter point, where

\[
r_0=\frac1{1+b}
\]

is the one-site zero-boundary equilibrium density. Thus a **fully regenerated mass component** always has a strict right-weighted scalar loss. This strengthens the near-East observation `|Br_0-c|Z -> 2/5` to the whole residual chamber.

However, `(FL)` plus bounded disagreement height does **not yet define a finite signed kernel**. There is an additional mass-relaxation mode which is already visible at depth two. Compressing that mode by integrating the trail duration before taking the norm is invalid: on the near-East path the signed right-weighted depth-two integral has normalized magnitude tending to

\[
\frac35,
\]

while the quantity actually required by `J_{x,r}`, with absolute value retained before the duration integral, tends to

\[
\frac75.
\]

So an averaged finite matrix can display a fake contraction even where the correct `L^1` transfer expands.

I construct the exact **fully-regenerated height-one signed phase kernel** `K^(1)`. It has genuine signed cancellation: along the near-East path its spectral radius tends to

\[
\sqrt{\frac25}<1.
\]

At the strict residual point `(a,b,c)=(1/10,3/10,4/5)` its spectral radius is about `0.10325`. This is positive evidence that the bounded signed mechanism can contract.

But `K^(1)` cannot be iterated as the sought global finite kernel. Two independent obstructions are exact:

1. the duration profile cannot be averaged before the final absolute value;
2. the zero-boundary invariant law is not even first- or second-order spatial Markov at the strict residual point above, so the current spin (or a short static spin word) does not close the mass phase.

The missing finite state is therefore more specific than “bounded disagreement height”: it must also retain the **mass relaxation / reset-history mode** needed to postpone duration cancellation until the end of a block. The scalar premise `(FL)` does not supply that return state.

I therefore do **not** claim a bounded-kernel contraction. I give below an exact finite-resolvent template showing what kernel becomes computable once G supplies a genuine global phase state.

Supporting exact checks are in

`students/student-f/008-bounded-signed-kernel-verifier.py`.

## 1. Conventions

Put

\[
B=b+c-a,
\qquad
g=b-a,
\qquad
\omega=1-c+a,
\]

and

\[
k:=1-c.
\]

The residual chamber is

\[
0<a<b,
\qquad
\frac12\le c<1,
\qquad
c\ge a+b,
\qquad
b\ge\sqrt2(1-c).
\tag{1.1}
\]

In the centered-trail spin convention the local flip rates are

\[
c_{00}=1,
\qquad
c_{01}=1-c=k,
\qquad
c_{10}=b,
\qquad
c_{11}=a.
\tag{1.2}
\]

Equivalently, there are neighbour-independent resets to `1` at rate `k` and to `0` at rate `a`, together with an additional rate-`B` Bernoulli-`p_*` reset when the right neighbour is zero, where

\[
p_* = \frac cB,
\qquad
1-p_* = \frac gB.
\tag{1.3}
\]

The right-region segment weight is

\[
w(u)=e^{-\omega u}s_1(u),
\]

with

\[
Z:=\int_0^\infty w(u)\,du
=\frac{a+b+2}{a(2b+3)+k(b+2)}.
\tag{1.4}
\]

The last form follows from the Meeting 006 resolvent after substituting `c=1-k`.

Throughout this report, `(FL)` means only the conditional statement authorized by Assignment 008:

> excursions of the restart/disagreement state outside some finite bounded-height phase set are returned with a strict multiplicative Foster factor.

I do not assume a particular return distribution or finite phase generator unless it is written explicitly.

## 2. Exact regenerated mass contraction throughout the residual chamber

For one site with zero right boundary,

\[
0\xrightarrow{1}1,
\qquad
1\xrightarrow{b}0,
\]

so the invariant density is

\[
r_0=\frac1{1+b}.
\tag{2.1}
\]

The mass coefficient in `(MD)` is therefore

\[
B r_0-c
=\frac{b(1-c)-a}{1+b}
=\frac{bk-a}{1+b}.
\tag{2.2}
\]

Define the fully-regenerated right-weighted mass multiplier

\[
\kappa_M
:=
|B r_0-c|Z
=
\frac{|bk-a|(a+b+2)}
{(1+b)[a(2b+3)+k(b+2)]}.
\tag{2.3}
\]

### Proposition 2.1

At every strict residual parameter point,

\[
\boxed{
\kappa_M<\frac23.
}
\tag{2.4}
\]

### Proof

There are two signs of the equilibrium mass coefficient.

If `a>=bk`, then

\[
\kappa_M
<
\frac{a(a+b+2)}{(1+b)a(2b+3)}
=
\frac{a+b+2}{(1+b)(2b+3)}.
\]

Now

\[
2(1+b)(2b+3)-3(a+b+2)
=4b^2+7b-3a.
\]

Since `a<b`,

\[
4b^2+7b-3a
>
4b^2+4b>0.
\]

Hence the last ratio is `<2/3`.

If `a<bk`, then

\[
\kappa_M
<
\frac{bk(a+b+2)}{(1+b)k(b+2)}
=
\frac{b(a+b+2)}{(1+b)(b+2)}.
\]

The right side is increasing in `a`, so use `a<b`:

\[
3b(a+b+2)
<
3b(2b+2).
\]

But

\[
2(1+b)(b+2)-3b(2b+2)
=4(1+b)(1-b)>0,
\]

because `b<c<1`. Again the ratio is `<2/3`. `square`

This result is independent of `(FL)`. It identifies a genuine signed loss every time the mass branch has fully returned to the zero-boundary equilibrium mode.

## 3. The mass branch has its own relaxation state

The point of Proposition 2.1 is not that every mass component is already at `r_0`. It is not.

Let `pi_2^0` be the two-site zero-boundary invariant law, with the left site listed first. Write

\[
S
=ab+2a+b^2-bc+2b-2c+2.
\tag{3.1}
\]

A direct four-state invariant calculation gives

\[
\pi_2^0(\eta_1=1)
=
\frac{ab+b^2-3bc+4b-2c+2}
{(1+b)S},
\tag{3.2}
\]

while the autonomous right site has density `r_0`. Hence

\[
\boxed{
\pi_2^0(\eta_1=1)-r_0
=
-\frac{2[a-b(1-c)]}{(1+b)S}.
}
\tag{3.3}
\]

Take the mass branch after the right site is removed and let it evolve for a trail segment of length `u` under the one-site zero-boundary semigroup. Its density is

\[
r_M(u)
=r_0+
\bigl(\pi_2^0(\eta_1=1)-r_0\bigr)e^{-(1+b)u}.
\tag{3.4}
\]

Thus even a pure mass branch carries a nonconstant relaxation mode unless

\[
a=b(1-c).
\]

At the strict residual point

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
\tag{3.5}
\]

one has

\[
B=1,
\qquad
r_0=\frac{10}{13},
\qquad
\pi_2^0(\eta_1=1)=\frac{250}{351}.
\]

Therefore

\[
\boxed{
r_M(u)
=\frac{10}{13}
-\frac{20}{351}e^{-13u/10},
}
\tag{3.6}
\]

and the total signed mass produced by the next centered insertion is

\[
B r_M(u)-c
=-\frac2{65}
-\frac{20}{351}e^{-13u/10}.
\tag{3.7}
\]

So there is already a continuum of distinct trail-generated mass states between two consecutive centered insertions. A phase variable which records only “mass” and disagreement height does not determine the next signed coefficient.

Near East this mode is not perturbatively negligible. On

\[
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
\tag{3.8}
\]

one finds

\[
\overline\pi_2^0(h_{p_*})
=-
\frac{2\varepsilon^3+\varepsilon^2+3\varepsilon+2}
{(1+\varepsilon)(2\varepsilon^2+5\varepsilon+1)}
\longrightarrow -2,
\tag{3.9}
\]

whereas

\[
\pi_1^0(h_{p_*})
=-\frac{\varepsilon}{1+\varepsilon}
\longrightarrow0.
\tag{3.10}
\]

The transient mass mode is order one while the regenerated constant mode is small. Any finite kernel that simply replaces the mass branch by its equilibrium coefficient loses exactly the hard near-East effect.

## 4. The depth-two obstruction is also an obstruction to premature phase averaging

Meeting 006 and Assignment 007 give

\[
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}
\bigl(M_{2,\varepsilon}-m_\varepsilon^2\bigr),
\tag{4.1}
\]

with

\[
m_\varepsilon=-\frac{\varepsilon}{1+\varepsilon},
\]

and

\[
M_{2,\varepsilon}
=\frac{(1+\varepsilon)(2\varepsilon-1)}
{2\varepsilon^2+5\varepsilon+1}.
\]

Write

\[
C_\varepsilon=m_\varepsilon^2-M_{2,\varepsilon}>0,
\qquad
\lambda_\varepsilon=1+\varepsilon.
\]

The signed right-weighted integral is

\[
S_\varepsilon^R
:=
\int_0^\infty
w(u)A_{2,\varepsilon}(u)\,du
=
 m_\varepsilon^2 Z_\omega
-C_\varepsilon Z_{\omega+\lambda_\varepsilon},
\tag{4.2}
\]

where

\[
Z_\alpha=\int_0^\infty e^{-\alpha u}s_1(u)\,du.
\]

The exact asymptotics are

\[
S_\varepsilon^R\longrightarrow-\frac35,
\tag{4.3}
\]

and

\[
\frac g{|m_\varepsilon|}\longrightarrow1.
\]

Therefore **if one integrates the duration before taking absolute values**, the apparent normalized factor is

\[
\boxed{
\frac g{|m_\varepsilon|}
\left|
\int_0^\infty w(u)A_{2,\varepsilon}(u)du
\right|
\longrightarrow\frac35<1.
}
\tag{4.4}
\]

But `A_{2,epsilon}` changes sign. The actual quantity occurring in `J_{x,r}` is

\[
\boxed{
\frac g{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|du
\longrightarrow\frac75>1.
}
\tag{4.5}
\]

Thus the operation

\[
\int w(u)\,[\text{signed phase at }u]\,du
\]

cannot be used to define the finite phase state **before** the block norm is taken. It creates a false `3/5` contraction precisely where the exact transfer is `7/5` expansive.

This is the main bounded-kernel bookkeeping constraint I did not see recorded explicitly in Meetings 006--008.

## 5. Minimal mode-resolved state at height one

For one mass-relaxation level, the correct duration profile lies in the two-dimensional mode space

\[
\mathcal E_1
=\operatorname{span}\{1,e^{-(1+b)u}\}.
\tag{5.1}
\]

The natural norm is not the absolute value of its integrated coefficient. It is

\[
\|(A,C)\|_{L^1(w)}
:=
\int_0^\infty
w(u)\left|A+C e^{-(1+b)u}\right|du.
\tag{5.2}
\]

For `(A,C)=(m_\varepsilon^2,M_{2,\varepsilon}-m_\varepsilon^2)`, (5.2) is exactly the quantity in (4.5).

Thus a correct bounded signed kernel may be finite-dimensional, but its phase must retain the coefficients of these relaxation modes until the end of the chosen block. “Mass sign plus disagreement height” is not enough.

At bounded height `H_0`, an exact finite construction can in principle use the zero-boundary generators on the finitely many phase configurations. If `Q` is the finite generator for one such phase, the segmentwise right weight gives the exact matrix resolvent

\[
\boxed{
\mathcal R_w(Q)
:=
\int_0^\infty w(u)e^{uQ}du
=
\frac{
 \rho_+[(\omega+\rho_-)I-Q]^{-1}
 -\rho_-[(\omega+\rho_+)I-Q]^{-1}
}{\rho_+-\rho_-},
}
\tag{5.3}
\]

where `rho_+`, `rho_-` are the two right-killing exponents from Meeting 006.

Equation (5.3) gives an exact, non-discretized way to build every entry of the bounded phase kernel **once the phase generator and insertion/branching maps are specified**.

The missing issue is not how to integrate a known finite CTMC. It is identifying the phase state on which the trail-generated mass law and the conditional-law disagreement both close without premature integration of the duration modes.

## 6. Fully-regenerated height-one signed phase kernel

There is one exact finite kernel which can already be written down and is useful as a diagnostic.

Take the two-site zero-boundary invariant law and condition on the current right spin `z`. Put

\[
q_z
:=
\pi_2^0(\eta_1=1\mid\eta_2=z).
\]

The four-state invariant calculation gives

\[
q_0
=\frac{a+b-2c+2}{S},
\tag{6.1}
\]

and

\[
q_1
=\frac{2b-bc-2c+2}{S},
\tag{6.2}
\]

with

\[
q_1-q_0
=-\frac{a-b(1-c)}S.
\tag{6.3}
\]

After the right site is removed, the adjacent site evolves under the one-site zero-boundary chain. Hence

\[
p_z(u)
:=P(\eta_1(u)=1\mid\eta_2(0)=z)
=r_0+(q_z-r_0)e^{-(1+b)u}.
\tag{6.4}
\]

Set

\[
I_z(1)
=r_0 Z+(q_z-r_0)Z_{\omega+1+b},
\qquad
I_z(0)=Z-I_z(1).
\tag{6.5}
\]

Because

\[
gh_{p_*}(0)=-c,
\qquad
gh_{p_*}(1)=g,
\tag{6.6}
\]

the right-weighted signed phase kernel is

\[
\boxed{
K^{(1)}
=
\begin{pmatrix}
-cI_0(0)&-cI_0(1)\\
 gI_1(0)& gI_1(1)
\end{pmatrix}.
}
\tag{6.7}
\]

This kernel retains cancellation between the two deterministic spin phases. It is exact for the adjacent fully-regenerated phase calculation. It is **not** asserted to be the full bounded-height trail kernel.

At the strict residual point (3.5),

\[
\boxed{
K^{(1)}
=\frac1{333207}
\begin{pmatrix}
-184712&-595480\\
47695&147353
\end{pmatrix}.
}
\tag{6.8}
\]

Its trace and determinant are

\[
\operatorname{tr}K^{(1)}=-\frac{593}{5289},
\qquad
\det K^{(1)}=\frac{1184}{111069},
\]

and

\[
(\operatorname{tr}K^{(1)})^2-4\det K^{(1)}
=-\frac{654225}{21757183}<0.
\]

Therefore

\[
\rho(K^{(1)})
=\sqrt{\frac{1184}{111069}}
\approx0.10325<1.
\tag{6.9}
\]

More importantly, along the near-East path (3.8), exact symbolic simplification gives

\[
\operatorname{tr}K^{(1)}\longrightarrow-\frac25,
\qquad
\det K^{(1)}\longrightarrow\frac25,
\tag{6.10}
\]

and the discriminant tends to

\[
-\frac{36}{25}.
\]

Thus for all sufficiently small positive `epsilon` the two eigenvalues are a complex conjugate pair and

\[
\boxed{
\rho(K^{(1)})
\longrightarrow
\sqrt{\frac25}<1.
}
\tag{6.11}
\]

This is the bounded signed cancellation that the raw scalar factor `cZ>1` completely misses. It is also why I do not regard the empty crude region as evidence against the block route.

## 7. Why `K^(1)` is not the answer

There are two independent reasons.

### 7.1 It averages a duration mode too early if iterated as an ordinary matrix

The entries in (6.7) integrate `u`. A single phase transition has a fixed sign, so this is harmless for that transition. But matrix multiplication of `K^(1)` would then sum over the previous duration before the next block norm is taken.

Equation (4.4) versus (4.5) proves that this operation can change a true `7/5` expansion into a fictitious `3/5` contraction. Therefore

\[
\rho(K^{(1)})<1
\]

is only a local signed-phase diagnostic. It cannot be substituted for the `L^1` block kernel required by `J_{x,r}`.

### 7.2 The invariant spatial law does not close on the current spin

At the strict residual point (3.5), let `pi_3^0` be the three-site zero-boundary invariant law. If the spatial law were first-order Markov, the outer spins would be conditionally independent given the middle spin. Exact calculation gives

\[
\pi(000)\pi(101)-\pi(001)\pi(100)
=\frac{6715}{52606827}\ne0,
\tag{7.1}
\]

and

\[
\pi(010)\pi(111)-\pi(011)\pi(110)
=-\frac{34675}{52606827}\ne0.
\tag{7.2}
\]

So one current-spin phase is not spatially Markov.

Nor does a two-spin static context fix the issue. For `pi_4^0`, conditioning on the middle word `00`, second-order spatial Markovity would require

\[
\pi(0000)\pi(1001)-\pi(0001)\pi(1000)=0.
\]

Instead

\[
\boxed{
\pi(0000)\pi(1001)-\pi(0001)\pi(1000)
=-\frac{1097085304370}{627742107775979469}\ne0.
}
\tag{7.3}
\]

Thus an exact bounded kernel cannot be obtained merely by replacing the reset-history stack with a short word of present spins.

The temporal reset phase which G is now formalizing is not cosmetic: it is needed to make the finite state Markovian.

## 8. Exact interface with `(FL)`

Meeting 008 deliberately allows F to assume only that large restart/height excursions have a strict Foster return factor. That scalar statement is not enough to specify the signed bounded kernel.

For the finite calculation one needs, for every return phase:

1. the signed mass component carried back into the small set;
2. the coupled conditional-law difference carried back into the small set;
3. the zero-boundary reset/relaxation phase determining the coefficients before the next centered insertion;
4. the rule saying which duration modes have already been integrated and which must remain visible until the block norm is taken.

Two return operators can obey the same scalar Foster bound and still feed different signs/modes into (MD), hence have different bounded spectral radii. Therefore no spectral conclusion about the signed kernel follows from the scalar `(FL)` premise alone.

Once G supplies an explicit finite Markov return state `Sigma`, the remaining computation is concrete. Form its finite zero-boundary generator `Q_Sigma`, attach the signed insertion/branching matrices from

\[
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f),
\]

and use the exact resolvent (5.3). The block norm must be applied **before** any integration which would mix opposite signs of a duration mode.

That is the finite kernel which should be tested for spectral radius `<1`.

## 9. Relation to `J_{x,r}`

If a future phase-resolved Foster theorem supplies a finite return state and the corresponding correct bounded kernel has a block norm with

\[
\|K_{H_0}^{m_0}\|_*\le\theta_B<1,
\]

while excursions outside the small set have Foster multiplier `theta_F<1`, the standard renewal decomposition at successive returns to the small set gives a geometric bound on the total phase-resolved block weight. In particular there is a parameter-dependent `vartheta<1` and `C<infinity` such that the right-weighted left invariant integral is bounded by

\[
J_{x,r}\le C\vartheta^{n/m_0},
\]

up to the finite initial/final partial blocks. Hence

\[
J_{x,r}\longrightarrow0.
\]

I am not claiming this implication is presently available, because the required finite return state and bounded signed kernel have not both been proved.

Even after `J->0`, the complete proof would still need the independent audit of the predecessor-trail Poisson--Mecke factorization and the complementary no-exit term recorded in Meetings 005--008.

## 10. What has actually been narrowed

The bounded signed problem is not blocked by the raw `cZ>1` multiplier. The exact height-one signed kernel contracts strongly at a representative strict residual point and remains contractive in the singular near-East limit.

The obstacle is instead one of **state closure at the correct norm level**:

- disagreement/restart height must be finite, as Meeting 008 already recognized;
- the mass branch also carries zero-boundary relaxation modes;
- those modes cannot be averaged before the final absolute value;
- present-spin words do not form an exact spatial Markov state.

Therefore the finite kernel must use the reset-history phase (or an equivalent finite mode representation), not merely `(mass sign, disagreement height, current exposure spin)`.

This is compatible with G's current Assignment 004: its explicit global Markov phase state should determine whether the missing mass/reset mode is already encoded in the proposed corrector or has to be added.

## Exact handoff

```text
unresolved after substantive work; exact finite-kernel blocker: conditional FL supplies a scalar return contraction for large disagreement/restart excursions but does not specify the signed mass/reset-history phase needed on return. A fully regenerated mass branch has the new uniform loss |B/(1+b)-c| Z<2/3 throughout the residual chamber, and the exact fully-regenerated height-one signed phase kernel has rho->sqrt(2/5)<1 near East, so bounded signed cancellation is viable. But the mass branch carries a nontrivial zero-boundary relaxation mode even at depth two; integrating that mode before the block norm gives a false near-East factor 3/5 whereas the required L1 factor is 7/5. Moreover the strict residual invariant law is neither first- nor second-order spatial Markov at (1/10,3/10,4/5). Thus a correct bounded kernel must retain a reset-history/mass-relaxation mode, or an equivalent finite CTMC phase, until the block absolute value is taken. The scalar FL premise alone is insufficient to define its spectral radius.
```
