# Student G 002: one-cell regional insertion and a three-site composition theorem

## Executive conclusion

Meeting 001 reduced the old last-exit route to a weighted insertion problem. I obtain a positive verdict on the minimal one-left-spin cell and a stronger three-site conditional estimate that controls every **nonnegative two-left-spin terminal companion**. The exact composition of two hidden signed interaction types across a shared scaffold boundary still needs one piece of bookkeeping, stated precisely below; I do not identify that unresolved bookkeeping with the proved terminal-polynomial statement.

Work in Student F's complemented canonical spins. Put

$$
d=b-a,
\qquad
k=1-c,
\qquad
B=c+d=b+c-a,
\qquad
\rho=\frac{c}{B}.
$$

Thus `d,k>0`, `B=c+d`, and `0<rho<1`. The noise-reduced process `L^-` has local rates, for source spin `s` and right neighbour `r`,

$$
0\to1\text{ at rate }1-cr,
\qquad
1\to0\text{ at rate }d(1-r).
\tag{0.1}
$$

At a successful interaction whose source-retaining/source-removing kind is hidden, the signed source insertion is

$$
B\eta_i-c=B(\eta_i-\rho).
\tag{0.2}
$$

The two new estimates are:

1. If the companion at the hidden source has one unresolved left spin,
   $$
   F=A+C\eta_{i-1},\qquad A,C\ge0,
   $$
   then, uniformly over initial configurations and arbitrary prescribed right-boundary histories,
   $$
   \mathbb E^-[(B\eta_i(t)-c)F]\ge0
   $$
   for
   $$
   t\ge T_2:=T_\rho+\frac{B}{dk}.
   $$
   This is an exact two-site correlation estimate.

2. On three consecutive sites with an arbitrary prescribed right-boundary history, there is an explicit `T_3(a,b,c)<infinity` after which the conditional `L^-` law lies in the full `rho`-centered moment cone on those three sites. Consequently, for every
   $$
   F=A+C_0\eta_{i-2}+C_1\eta_{i-1}
   +C_{01}\eta_{i-2}\eta_{i-1},
   \qquad C_*\ge0,
   $$
   one has
   $$
   \mathbb E^-[(B\eta_i(t)-c)F\mid\text{right history}]\ge0,
   \qquad t\ge T_3.
   $$

The second statement is exactly the weighted estimate needed **if** the first two-cell regional integration leaves a nonnegative standard-monomial companion on the two predecessor terminal spins. Unsigned `L^+` evolutions, `0/1` boundary substitutions, positive consistency scalars, products, and source gradients all preserve that polynomial cone. What I have not proved is that, after the first hidden signed type itself is integrated and a shared successful boundary mark is passed to the next cell, no additional path-dependent signed term remains. That is now the precise two-cell bookkeeping blocker.

A supporting exact symbolic verifier is

`students/student-g/002-regional-moment-verifier.py`.

## 1. Positive-monomial cone for the unsigned regional pieces

For a finite variable set `J`, write

$$
\mathcal P_J^+
=
\left\{
\sum_{A\subseteq J}\alpha_A\chi_A:
\alpha_A\ge0
\right\},
\qquad
\chi_A(\eta)=\prod_{j\in A}\eta_j.
\tag{1.1}
$$

Student F and Meeting 001 verified that `L^+` has the same set-valued dual transitions with all signs positive and no Feynman--Kac potential. Hence an `L^+` evolution sends every standard monomial to a nonnegative mixture of standard monomials and therefore preserves `P_J^+`.

The other operations appearing in one repaired unsigned region also preserve this cone:

- fixing a boundary spin to `0` or `1`;
- multiplying by a positive geometry/consistency scalar;
- multiplying two positive-monomial polynomials;
- taking the source gradient
  $$
  D_iG=G(\eta^{i,1})-G(\eta^{i,0}).
  $$

Indeed, if

$$
G=\sum_A\alpha_A\chi_A,
\qquad \alpha_A\ge0,
$$

then

$$
D_iG
=
\sum_{A\ni i}\alpha_A\chi_{A\setminus\{i\}},
\tag{1.2}
$$

again with nonnegative coefficients.

Thus, once the minimal unsigned white-region marks have been integrated, a companion with only one unresolved predecessor spin is necessarily affine with nonnegative coefficients. With two unresolved predecessor terminal spins, every unsigned terminal companion belongs to the four-dimensional cone displayed in the executive conclusion. The calculations below prove insertion positivity uniformly over the coefficients of those cones, so the exact positive coefficients and cell lengths do not need to be computed.

## 2. One-cell insertion: exact two-site ODE

Let

$$
x=\eta_{i-1},
\qquad
y=\eta_i,
$$

and prescribe an arbitrary cadlag right-boundary path `z(t) in {0,1}` for `y`. Write

$$
m=\mathbb E[y],
\qquad
n=\mathbb E[x],
\qquad
w=\mathbb E[xy],
\qquad
H=w-\rho n=\mathbb E[(y-\rho)x].
\tag{2.1}
$$

A direct generator calculation from (0.1) gives

$$
\boxed{
H'
=
-(2+d-Bz)H
-\rho
+\frac{d}{B}n
+\left(1-\frac{cd}{B}\right)m.
}
\tag{2.2}
$$

The damping coefficient is positive for both boundary values:

$$
2+d-Bz
=
\begin{cases}
2+d,&z=0,\\
2-c,&z=1.
\end{cases}
$$

Student F's conditional one-site estimate gives

$$
m(t),n(t)\ge\rho
\qquad (t\ge T_\rho),
\tag{2.3}
$$

where

$$
T_\rho
=
\frac1k\log\frac{B}{dk}.
\tag{2.4}
$$

At the lower corner `m=n=rho`, the non-`H` forcing in (2.2) is

$$
\varepsilon
:=-\rho+\rho\frac dB
+\rho\left(1-\frac{cd}{B}\right)
=
\boxed{\frac{cdk}{B^2}}>0.
\tag{2.5}
$$

Since `w>=0` and `n<=1`, one always has `H(T_rho)>=-rho`. While `H<0` after `T_rho`, (2.2)--(2.5) give

$$
H'\ge\varepsilon.
$$

Hence `H` reaches zero no later than

$$
\boxed{
T_2
=T_\rho+\frac{\rho}{\varepsilon}
=T_\rho+\frac{B}{dk}.
}
\tag{2.6}
$$

At a zero of `H` the derivative is at least `epsilon`, so it cannot cross back to the negative side.

### Proposition 2.1

Uniformly over deterministic initial configurations and prescribed right-boundary histories,

$$
\boxed{
\mathbb E^-[(\eta_i(t)-\rho)\eta_{i-1}(t)]\ge0,
\qquad t\ge T_2.
}
\tag{2.7}
$$

Together with Student F's one-site insertion estimate, this gives for every `A,C>=0`

$$
\boxed{
\mathbb E^-[(B\eta_i(t)-c)(A+C\eta_{i-1}(t))]\ge0,
\qquad t\ge T_2.
}
\tag{2.8}
$$

Because the constants are uniform in the prescribed boundary path, (2.8) also holds after conditioning on the actual complete graphical history strictly to the right.

This is a positive verdict on the minimal one-left-spin weighted kernel. It directly controls the left dependence that invalidated a naive use of Student F's right-measurable lemma.

## 3. Density alone cannot prove even Proposition 2.1

The correlation equation above is essential. At the genuine residual point

$$
(a,b,c)=\left(\frac1{1000},\frac{11}{1000},\frac{999}{1000}\right),
\tag{3.1}
$$

one has

$$
d=\frac1{100},
\qquad
B=\frac{1009}{1000},
\qquad
\rho=\frac{999}{1009}.
$$

Even the limiting one-site floor for `L^-` is

$$
p_0=\frac1{1+d}=\frac{100}{101}>\rho.
$$

Take an abstract two-bit law with both marginals `p_0` and the smallest feasible overlap

$$
w=2p_0-1=\frac{99}{101}.
$$

For the first-order companion found in Student F's Duhamel expansion,

$$
F=c+Bx,
$$

the weighted sign is

$$
\begin{aligned}
\mathbb E[(y-\rho)(c+Bx)]
&=c(p_0-\rho)+B(w-\rho p_0)\\
&=\boxed{-\frac{4041}{50954500}}<0.
\end{aligned}
\tag{3.2}
$$

Thus no theorem based only on one-time marginal lower bounds, even at the stronger floor `p_0>rho`, can imply the required one-cell sign. The new input is genuinely correlation control tied to the regional kernel.

## 4. Exact three-site centered system

For the first composition test, take

$$
v=\eta_{i-2},
\qquad
x=\eta_{i-1},
\qquad
y=\eta_i,
$$

with arbitrary prescribed right boundary `z(t)`. Put

$$
g_j=\eta_j-\rho,
\qquad
r=1-\rho=\frac dB,
\qquad
h=\frac{dk}{B}>0,
\tag{4.1}
$$

and, for nonempty `S subset {0,1,2}`,

$$
u_S(t)=\mathbb E\prod_{j\in S}g_j(t),
$$

where `0,1,2` correspond to `v,x,y`.

Direct generator calculation gives

$$
\begin{aligned}
\dot u_2
&=-(1+d-Bz)u_2+h,\\
\dot u_1
&=B u_{12}-(k+d)u_1+h,\\
\dot u_0
&=B u_{01}-(k+d)u_0+h,\\
\dot u_{12}
&=-(2+d-Bz)u_{12}+r u_1+h u_2,\\
\dot u_{01}
&=B u_{012}-(2+d-c)u_{01}+r u_0+h u_1,\\
\dot u_{02}
&=B u_{012}-(2+2d-c-Bz)u_{02}+h(u_0+u_2),\\
\dot u_{012}
&=-(3+d-Bz)u_{012}+r(u_{01}+u_{02})+h u_{12}.
\end{aligned}
\tag{4.2}
$$

Every off-diagonal coefficient and every source term is nonnegative. All diagonal damping coefficients are strictly positive for both boundary values; for the least obvious one,

$$
2+2d-c-B=2(1-c)+d=2k+d>0.
$$

Hence the positive orthant in the seven centered moments is forward invariant under every switching boundary path.

The supporting verifier derives (2.2) and all seven equations in (4.2) symbolically from the four local rates.

## 5. Uniformly interior all-one reference

Start the three-site process from the all-one configuration. Then

$$
u_S(0)=r^{|S|}>0.
$$

Define

$$
\delta_1=\frac{h}{1+d},
$$

$$
\delta_2
=
\min\left\{r^2,\frac{h\delta_1}{2+2d}\right\},
$$

and

$$
\delta_3
=
\min\left\{r^3,\frac{h\delta_2}{3+d}\right\},
\qquad
\delta_*:=\min\{\delta_1,\delta_2,\delta_3\}>0.
\tag{5.1}
$$

Because all coupling terms in (4.2) are nonnegative, scalar comparison gives, uniformly over `z(t)`,

$$
u_j(t)\ge\delta_1,
\qquad
u_{jk}(t)\ge\delta_2,
\qquad
u_{012}(t)\ge\delta_3
\tag{5.2}
$$

for all times. Indeed, for singletons use

$$
\dot u_j\ge-(1+d)u_j+h;
$$

for pairs use

$$
\dot u_{jk}\ge-(2+2d)u_{jk}+h\delta_1;
$$

and for the triple use

$$
\dot u_{012}\ge-(3+d)u_{012}+h\delta_2.
$$

The initial values are respectively `r,r^2,r^3`, exactly accounting for the minima in (5.1).

## 6. Uniform finite-time entrance into the three-site centered cone

The rates (0.1) admit the graphical decomposition

- rate `k` baseline marks that set the source to `1` regardless of the right neighbour;
- rate `c` extra birth marks that set the source to `1` when the right neighbour is `0`;
- rate `d` death-candidate marks that set the source to `0` when the right neighbour is `0`.

On any time block of length `3`, split the block into three unit subintervals and consider the event `E` that

1. the rightmost site `y` receives no death-candidate mark in the whole block;
2. `y` receives a baseline mark in the first unit;
3. `x` receives a baseline mark in the second unit;
4. `v` receives a baseline mark in the third unit.

On `E`, **every** initial three-site state is mapped to `111` at the end of the block, for every prescribed right-boundary path. After `y` is reset it cannot die on `E`; after `x` is reset its right neighbour is permanently `1`, so later death candidates at `x` are ineffective, and similarly for `v`.

The common reset probability is

$$
\boxed{
p_3=e^{-3d}(1-e^{-k})^3>0.
}
\tag{6.1}
$$

Couple an arbitrary initial state to the all-one initial state with the same graphical marks. Repeating the reset attempt on successive three-unit blocks gives

$$
\mathbb P(\eta^{(1)}(3m)\ne\eta^{(2)}(3m))
\le(1-p_3)^m.
\tag{6.2}
$$

A centered monomial takes values in `[-1,1]`, so its expectation differs between the two copies by at most `2(1-p_3)^m`.

Set

$$
m_3
=
\left\lceil
\frac{\log(4/\delta_*)}{-\log(1-p_3)}
\right\rceil,
\qquad
\boxed{T_3=3m_3.}
\tag{6.3}
$$

At time `T_3`, every nonempty centered moment from every initial state is at least `delta_*/2>0`. The Metzler system (4.2) preserves nonnegativity thereafter.

### Proposition 6.1 (three-site dynamic-boundary cone entrance)

For every deterministic initial configuration, every prescribed cadlag right-boundary path, every nonempty `S subset {i-2,i-1,i}`, and every `t>=T_3`,

$$
\boxed{
\mathbb E^-\left[
\prod_{j\in S}(\eta_j(t)-\rho)
\right]\ge0.
}
\tag{6.4}
$$

The estimate is uniform in the entire boundary path. Therefore it also holds conditionally on the complete graphical history strictly to the right of the three-site interval.

## 7. Consequence for every two-left-spin terminal companion

Let

$$
F=A+C_0\eta_{i-2}+C_1\eta_{i-1}
+C_{01}\eta_{i-2}\eta_{i-1},
\qquad C_*\ge0.
\tag{7.1}
$$

For `A subset {i-2,i-1}`,

$$
\begin{aligned}
\mathbb E^-[(\eta_i-\rho)\chi_A]
&=
\sum_{S\subseteq A}
\rho^{|A|-|S|}
\mathbb E^-\left[
\prod_{j\in S\cup\{i\}}(\eta_j-\rho)
\right]
\ge0
\end{aligned}
\tag{7.2}
$$

for `t>=T_3`, by Proposition 6.1. Linear combination with the nonnegative coefficients in (7.1) gives

$$
\boxed{
\mathbb E^-[(B\eta_i(t)-c)F]\ge0,
\qquad t\ge T_3.
}
\tag{7.3}
$$

This is a genuine composition-level estimate: **any** terminal companion produced by two unsigned predecessor regions and lying in the positive standard-monomial cone is safe. The durations and switching right-boundary rules have disappeared from the sign problem.

## 8. Exact remaining two-cell bookkeeping issue

I do not promote (7.3) to a complete proof of two hidden-type scaffold composition without one further identification.

If the two-cell repaired scaffold can be written so that, after the first hidden signed type is averaged and the shared successful boundary mark is assigned, the companion passed to the second hidden source is obtained only through the unsigned operations in Section 1, then Lemma 1.1 places it in (7.1) and (7.3) proves two-cell insertion positivity outright.

What is not yet written in the project record is that exact shared-boundary identity. Student F's first report explicitly warned that canonical patch factorization alone does not automatically identify a coarse white scaffold region with a standard spin semigroup; shared successful boundary marks have to be assigned correctly. My calculation removes the **sign** problem once that finite kernel is shown to be in the positive terminal-polynomial cone, but it does not by itself perform that assignment for two hidden signed cells.

Thus the old route survives the minimal-cell falsification test. The next falsifiable point is narrower:

> Does the exact two-hidden-cell shared-boundary kernel lie in the positive two-left-spin terminal cone of (7.1), or does the first hidden type create an additional signed/path-dependent term before the second insertion?

A negative answer there would be a genuine composition failure. A positive answer immediately plugs into Proposition 6.1.

## 9. Anti-circularity audit

**Previous blocker.** Left dependence of the companion made Student F's right-history insertion lemma inapplicable even on the smallest cell.

**New irreversible estimate.** Proposition 2.1 proves the one-left-spin weighted insertion directly, uniformly over the right history. Proposition 6.1 proves finite-time entrance into the complete three-site centered cone and therefore controls every nonnegative two-left-spin terminal companion.

**Why this is not another density estimate.** The exact law (3.2) has each marginal above `rho` but gives the wrong sign for the first-order cell kernel. Correlation/centered-moment control is indispensable.

**What is now strictly narrower.** One-cell sign is no longer open. For two cells, only the exact shared-hidden-type kernel identification remains; if it lands in the positive terminal cone, its sign is already settled by (7.3).

## Handoff

`weighted regional estimate proved: the minimal one-left-spin companion is insertion-positive after the explicit T_2=T_rho+B/(dk), uniformly over the full right-boundary history; moreover after an explicit T_3 the three-site L^- law is in the full rho-centered cone, so every nonnegative two-left-spin terminal companion is insertion-positive. Exact two-hidden-cell composition is reduced to one remaining finite bookkeeping question: whether assigning the shared successful boundary mark keeps the composed companion inside that positive terminal-polynomial cone.`
