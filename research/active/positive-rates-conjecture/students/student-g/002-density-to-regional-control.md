# Student G 002: regional insertion positivity through two cells

## Executive conclusion

Meeting 001 narrowed the old last-exit route to a finite weighted insertion test. That test is positive on the first nontrivial cell, and it remains positive after one composition step.

Work in the complemented canonical spins of Student F. Put

$$
d=b-a,
\qquad
k=1-c,
\qquad
B=c+d=b+c-a,
\qquad
\rho=\frac cB.
$$

Thus `d,k>0`, `B=c+d`, and `0<rho<1`. The noise-reduced dynamics `L^-` has local rates, for a source spin `s` and its right neighbour `r`,

$$
0\to1\text{ at rate }1-cr,
\qquad
1\to0\text{ at rate }d(1-r).
\tag{0.1}
$$

The signed average at a hidden successful interaction is

$$
B\eta_i-c=B(\eta_i-\rho).
\tag{0.2}
$$

The new results are:

1. **One-cell weighted insertion.** If the unsigned companion contains one unresolved left predecessor spin, hence has the form
   $$
   F=A+C\eta_{i-1},\qquad A,C\ge0,
   $$
   then for every initial configuration and every prescribed right-hand history,
   $$
   \mathbb E^-[(\eta_i(t)-\rho)F]\ge0
   $$
   after the explicit burn-in
   $$
   T_2=T_\rho+\frac{B}{dk}.
   $$
   This is proved by an exact two-site moment ODE, not by an unweighted density bound.

2. **Two-cell composition.** On three consecutive sites, for every prescribed right-boundary history, there is an explicit finite time `T_3(a,b,c)` after which the conditional `L^-` law belongs to the full `rho`-centered moment cone on those three sites. Consequently
   $$
   \mathbb E^-[(\eta_i(t)-\rho)F\mid\text{right history}]\ge0
   $$
   for every polynomial
   $$
   F=A+C_0\eta_{i-2}+C_1\eta_{i-1}+C_{01}\eta_{i-2}\eta_{i-1},
   \qquad A,C_0,C_1,C_{01}\ge0,
   $$
   and every `t>=T_3`.

3. The unsigned `L^+` regional evolution and source gradients preserve the cone of polynomials with nonnegative standard-monomial coefficients. Therefore the minimal one-cell companion lies in the affine cone in (1), while the first two-cell composition lies in the four-dimensional cone in (2), independently of the exact cell lengths and of the `0/1` switching boundary produced by the corrected scaffold rules.

Thus the regional insertion test in E6 does **not** fail on the minimal cell, and the first composition step does **not** fail either. What remains is an unbounded-composition problem: the present finite-volume entrance time deteriorates with the number of unresolved predecessor sites, and I have not proved a uniform-in-trail-length insertion theorem.

A supporting exact symbolic verifier is

`students/student-g/002-regional-moment-verifier.py`.

## 1. What exactly is being tested

Student F and Meeting 001 established two pieces that I use as input.

First, at a revealed successful dual interaction whose source-retaining/source-removing kind remains hidden, the signed source factor is exactly (0.2).

Second, after the negative dual sign is erased, the comparison system `L^+` has the same set-valued dual transitions with all signs positive and no Feynman--Kac potential. Hence its action on a standard monomial is a nonnegative linear combination of standard monomials.

For a finite set `J`, define

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

The following elementary closure properties are the useful finite-kernel statement.

### Lemma 1.1 (unsigned regional companion cone)

The following operations preserve `P_J^+`, with the obvious change of variable set:

- an `L^+` evolution with any prescribed `0/1` right-boundary path;
- fixing a boundary spin to `0` or `1`;
- multiplication of two members of `P^+`;
- multiplication by a positive geometry/consistency scalar;
- the source gradient
  $$
  D_iG=G(\eta^{i,1})-G(\eta^{i,0}).
  $$

In the last item, `D_iG` is a polynomial with nonnegative coefficients in the variables other than `i`.

### Proof

For a monomial, the all-positive, zero-potential dual for `L^+` writes its evolved value as a positive mixture of monomials. Linearity proves the first item. Substitution of `0` or `1`, products, and positive scalar multiplication plainly preserve nonnegative coefficients.

Finally, if

$$
G=\sum_A\alpha_A\chi_A,
\qquad \alpha_A\ge0,
$$

then

$$
D_iG
=
\sum_{A\ni i}\alpha_A\chi_{A\setminus\{i\}},
$$

which again has nonnegative coefficients. `square`

This avoids having to compute the cell-specific coefficients. For the **minimal** cell there is only one unresolved left predecessor spin after the source gradient, so its companion is necessarily

$$
A+C\eta_{i-1},\qquad A,C\ge0.
\tag{1.2}
$$

After one further predecessor cell, the unresolved terminal variables are at most `eta_{i-2},eta_{i-1}`, so the unsigned companion is necessarily

$$
A+C_0\eta_{i-2}+C_1\eta_{i-1}
+C_{01}\eta_{i-2}\eta_{i-1},
\qquad C_*\ge0.
\tag{1.3}
$$

The corrected dynamic-boundary rule only changes the prescribed right-boundary path between `0` and `1`; it does not change this coefficient cone.

Thus E6 reduces, for one and two cells, to proving insertion positivity for (1.2) and (1.3) under `L^-` uniformly over that boundary path.

## 2. One-cell positivity by an exact two-site ODE

Let

$$
x=\eta_{i-1},
\qquad
y=\eta_i,
$$

and let `z(t) in {0,1}` be an arbitrary prescribed right-neighbour path for `y`. Write

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
-\lambda_z H
-ho
+\frac dB n
+\left(1-\frac{cd}{B}\right)m,
}
\tag{2.2}
$$

where

$$
\lambda_z=2+d-Bz
=
\begin{cases}
2+d,&z=0,\\
2-c,&z=1.
\end{cases}
\tag{2.3}
$$

In particular `lambda_z>0`.

Student F's right-history one-site estimate applies at both sites. For

$$
T_\rho
=
\frac1k\log\frac{B}{dk},
\tag{2.4}
$$

one has, uniformly over initial states and prescribed right histories,

$$
m(t),n(t)\ge\rho,
\qquad t\ge T_\rho.
\tag{2.5}
$$

The non-`H` forcing in (2.2) is increasing in `m,n`. At the lower corner `m=n=rho` it equals

$$
\varepsilon
=
-\rho+\rho\frac dB
+\rho\left(1-\frac{cd}{B}\right)
=
\boxed{\frac{cdk}{B^2}}>0.
\tag{2.6}
$$

Also `H(T_rho)>=-rho`, simply because `w>=0` and `n<=1`. Therefore whenever `H<0` after `T_rho`,

$$
H'\ge\varepsilon.
\tag{2.7}
$$

It follows that `H` must reach zero by

$$
\boxed{
T_2
=T_\rho+\frac{\rho}{\varepsilon}
=T_\rho+\frac{B}{dk}.
}
\tag{2.8}
$$

At a zero of `H`, (2.2) and (2.6) give `H'>=epsilon`, so `H` cannot cross back to the negative side.

### Proposition 2.1 (one-cell weighted insertion)

For every deterministic initial configuration and every prescribed right-boundary history,

$$
\boxed{
\mathbb E^-[(\eta_i(t)-\rho)\eta_{i-1}(t)]\ge0,
\qquad t\ge T_2.
}
\tag{2.9}
$$

Since Student F already gives `E(eta_i-rho)>=0` for `t>=T_rho`, every affine companion (1.2) satisfies

$$
\boxed{
\mathbb E^-[(B\eta_i(t)-c)F]\ge0,
\qquad t\ge T_2.
}
\tag{2.10}
$$

The statement is uniform in the entire prescribed right history. Hence it remains true conditionally on the actual right graphical history in the one-sided process.

This resolves the minimal one-left-branch obstruction that made the raw Duhamel gradient non-right-measurable.

## 3. Why a stronger marginal density estimate would not have proved Proposition 2.1

The preceding argument genuinely uses a two-site correlation equation. It cannot be replaced by a theorem using only one-time marginal lower bounds.

Take the genuine residual point

$$
(a,b,c)=\left(\frac1{1000},\frac{11}{1000},\frac{999}{1000}\right).
\tag{3.1}
$$

Then

$$
d=\frac1{100},
\qquad
B=\frac{1009}{1000},
\qquad
\rho=\frac{999}{1009}.
$$

Even the limiting one-site floor of the `L^-` comparison ODE is

$$
p_0=\frac1{1+d}=\frac{100}{101}>\rho.
\tag{3.2}
$$

Consider an abstract two-bit law with both marginals equal to `p_0` and the smallest feasible overlap

$$
w=2p_0-1=\frac{99}{101}.
$$

For the first-order unsigned companion from Student F,

$$
F=c+B x,
$$

the weighted insertion is

$$
\begin{aligned}
\mathbb E[(y-\rho)(c+Bx)]
&=c(p_0-\rho)+B(w-\rho p_0)\\
&=\boxed{-\frac{4041}{50954500}}<0.
\end{aligned}
\tag{3.3}
$$

Thus even a marginal theorem at the stronger floor `p_0>rho` cannot control the actual infinitesimal one-cell kernel without correlation information. This is why (2.2), rather than another unweighted density estimate, is the relevant bridge.

## 4. Three-site centered dynamics

To test the first composition step, use three consecutive sites

$$
v=\eta_{i-2},
\qquad
x=\eta_{i-1},
\qquad
y=\eta_i,
$$

again with an arbitrary prescribed right boundary `z(t)` for `y`.

Put

$$
g_j=\eta_j-\rho,
\qquad
r=1-\rho=\frac dB,
\qquad
h=\frac{dk}{B}>0,
\tag{4.1}
$$

and for nonempty `S subset {0,1,2}` write

$$
u_S(t)=\mathbb E\prod_{j\in S}g_j(t),
$$

where `0,1,2` correspond to `v,x,y`.

Direct generator calculation gives the exact closed system

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

All off-diagonal coefficients and all source terms are nonnegative. The diagonal damping coefficients are strictly positive for both `z=0` and `z=1`; for example

$$
2+2d-c-B
=2(1-c)+d=2k+d>0.
$$

Thus the positive orthant in the seven centered moments is forward invariant for every switching boundary path. This is the explicit three-site instance of the dynamic-boundary centered-cone observation in Student F's first report.

The supporting script checks (2.2), (2.6), and all seven equations in (4.2) symbolically.

## 5. A uniformly interior reference law

Start the three-site `L^-` process from the all-one configuration. Then

$$
u_S(0)=r^{|S|}>0.
$$

Because (4.2) is Metzler, every centered moment remains nonnegative. More is true: all of them remain a fixed positive distance from zero, uniformly over the right-boundary path and over time.

Define

$$
\delta_1=\frac{h}{1+d},
\tag{5.1}
$$

$$
\delta_2
=
\min\left\{
r^2,
\frac{h\delta_1}{2+2d}
\right\},
\tag{5.2}
$$

and

$$
\delta_3
=
\min\left\{
r^3,
\frac{h\delta_2}{3+d}
\right\},
\qquad
\delta_*=\min\{\delta_1,\delta_2,\delta_3\}>0.
\tag{5.3}
$$

For the singletons, drop the nonnegative coupling terms in (4.2) and use the largest possible damping `1+d`:

$$
\dot u_j\ge-(1+d)u_j+h.
$$

Since `u_j(0)=r` and `delta_1<=r`, scalar comparison gives

$$
u_j(t)\ge\delta_1.
\tag{5.4}
$$

For every pair, drop its nonnegative couplings except one `h u_j` input and use the crude common damping bound `2+2d`:

$$
\dot u_{jk}\ge-(2+2d)u_{jk}+h\delta_1.
$$

Together with `u_{jk}(0)=r^2`, this yields

$$
u_{jk}(t)\ge\delta_2.
\tag{5.5}
$$

Finally

$$
\dot u_{012}
\ge-(3+d)u_{012}+h\delta_2,
$$

and `u_{012}(0)=r^3`, giving

$$
u_{012}(t)\ge\delta_3.
\tag{5.6}
$$

Hence every nonempty centered moment of the all-one reference process is at least `delta_*` for every time and every prescribed right-boundary history.

## 6. Uniform finite-time entrance into the centered cone

The remaining step is to remove the special all-one initial condition. For this there is a simple finite-volume regeneration/coupling event.

Rewrite (0.1) graphically at each site as the superposition of

- rate `k` **baseline birth** marks that set the site to `1` regardless of its right neighbour;
- rate `c` extra birth marks that set the site to `1` when the right neighbour is `0`;
- rate `d` death-candidate marks that set the site to `0` when the right neighbour is `0`.

This gives exactly the rates (0.1).

Consider any time block of length `3`. Divide it into three unit subintervals. Let `E` be the event that

1. there is no death-candidate mark at the rightmost site `y` anywhere in the block;
2. `y` receives a baseline-birth mark in the first unit interval;
3. `x` receives a baseline-birth mark in the second unit interval;
4. `v` receives a baseline-birth mark in the third unit interval.

On `E`, every trajectory, regardless of its state at the beginning of the block and regardless of the prescribed boundary path, is in the all-one configuration at the end of the block. Indeed, after `y` is reset to one it cannot be killed on `E`; after `x` is reset, its right neighbour is permanently one, so its later death-candidate marks are ineffective; the same holds for `v` after the third reset.

The probability of this common reset event is

$$
\boxed{
p_3=e^{-3d}(1-e^{-k})^3>0.
}
\tag{6.1}
$$

Couple two copies with arbitrary initial states using the same graphical marks and the same prescribed right boundary. In every three-unit block, conditionally on the past, `E` coalesces the copies with probability `p_3`. Hence after `m` blocks

$$
\mathbb P(\eta^{(1)}(3m)\ne\eta^{(2)}(3m))
\le(1-p_3)^m.
\tag{6.2}
$$

Every centered monomial takes values in `[-1,1]`. Coupling an arbitrary initial state to the all-one reference therefore gives

$$
\left|
u_S^{\eta}(3m)-u_S^{\mathbf 1}(3m)\right|
\le2(1-p_3)^m.
\tag{6.3}
$$

Choose

$$
m_3
=
\left\lceil
\frac{\log(4/\delta_*)}{-\log(1-p_3)}
\right\rceil,
\qquad
\boxed{T_3=3m_3.}
\tag{6.4}
$$

Then (5.4)--(5.6) and (6.3) give, for every nonempty `S`,

$$
u_S^{\eta}(T_3)\ge\frac{\delta_*}{2}>0.
\tag{6.5}
$$

After `T_3`, the Metzler system (4.2) preserves nonnegativity. We have proved:

### Proposition 6.1 (three-site dynamic-boundary cone entrance)

For every deterministic initial configuration and every prescribed cadlag right-boundary path,

$$
\boxed{
\mathbb E^-\left[
\prod_{j\in S}(\eta_j(t)-\rho)
\right]\ge0
\quad
\text{for every }S\subseteq\{i-2,i-1,i\},
\qquad t\ge T_3.
}
\tag{6.6}
$$

The constants are explicit and depend only on `(a,b,c)`, not on the initial state or the boundary history.

Because the estimate is uniform in the prescribed boundary path, it holds after conditioning on the complete graphical history strictly to the right of the three-site interval.

## 7. Two-cell weighted insertion

Let

$$
F
=
A+C_0\eta_{i-2}+C_1\eta_{i-1}
+C_{01}\eta_{i-2}\eta_{i-1},
\qquad C_*\ge0.
\tag{7.1}
$$

For any `A subset {i-2,i-1}`,

$$
\begin{aligned}
\mathbb E^-[(\eta_i-\rho)\chi_A]
&=
\mathbb E^-\left[
(\eta_i-\rho)
\prod_{j\in A}\bigl((\eta_j-\rho)+\rho\bigr)
\right]\\
&=
\sum_{S\subseteq A}
\rho^{|A|-|S|}
\mathbb E^-\left[
\prod_{j\in S\cup\{i\}}(\eta_j-\rho)
\right].
\end{aligned}
\tag{7.2}
$$

Every term on the last line is nonnegative after `T_3` by Proposition 6.1. Therefore

$$
\boxed{
\mathbb E^-[(B\eta_i(t)-c)F]
\ge0,
\qquad t\ge T_3,
}
\tag{7.3}
$$

uniformly over all coefficients in (7.1), all initial states, and all prescribed right-boundary histories.

Combining Lemma 1.1 and (7.3) gives the finite regional verdict requested by E6:

### Theorem 7.1 (one-cell and first two-cell regional insertion positivity)

After integrating the unsigned `L^+` histories in the minimal scaffold cell, while keeping the successful source-retaining/source-removing type hidden, the companion lies in the affine cone (1.2), and its hidden-type average is nonnegative after `T_2`.

After one further predecessor-cell composition, the unsigned companion lies in the two-left-spin cone (1.3), and its hidden-type average is nonnegative after `T_3`.

Both statements remain valid under the corrected dynamic `0/1` scaffold boundary rules, because `T_2` and `T_3` are uniform over the entire prescribed right-boundary history.

Thus the minimal cell does **not** kill the principal's old last-exit route, and the first composition step does **not** exhibit a sign failure.

## 8. What this does and does not close

This block changes the bottleneck in a one-way way.

Before this assignment, left dependence in the regional companion was an uncontrolled sign obstruction. It is now controlled through two predecessor cells:

$$
\text{one left predecessor}
\Longrightarrow
\text{weighted insertion after }T_2,
$$

and

$$
\text{two left predecessors}
\Longrightarrow
\text{weighted insertion after }T_3.
$$

The proof is not an unweighted density estimate. Section 3 shows that marginal density alone can fail on the actual first-order cell kernel even when each marginal is above `rho`.

I have **not** proved the full PRC or the full last-exit expansion. The next obstruction is unbounded composition. The argument in Sections 4--7 is finite-dimensional; its coupling constant is already

$$
p_3=e^{-3d}(1-e^{-k})^3,
$$

and an analogous `m`-site reset probability deteriorates rapidly with `m`. Therefore this calculation does not by itself supply a trail-length-uniform burn-in or a summable estimate for an arbitrary scaffold.

A viable next step would be one of:

1. prove that actual scaffold composition never requires a companion whose unresolved left support grows beyond a fixed size;
2. prove a uniform-in-support centered-cone entrance mechanism for `L^-` substantially sharper than the crude simultaneous-reset coupling;
3. combine a support-dependent entrance time with the exact trail factor `e^{-au}` and the distribution of scaffold depth, so that large-support cells are paid for probabilistically rather than uniformly.

The key new fact is that there is no local sign counterexample at depth one or two.

## Anti-circularity audit

**Previous unresolved statement.** The regional companion after a hidden interaction could depend on left spins, and it was unknown whether this destroyed the insertion sign even on the smallest nontrivial cell.

**New estimate.** Proposition 2.1 proves the weighted one-left-spin insertion directly. Proposition 6.1 proves uniform finite-time entrance into the full three-site centered cone, and Theorem 7.1 uses it to prove the first two-cell composition.

**Why strictly narrower.** The remaining issue is no longer one-cell or two-cell positivity. It is growth of the unresolved predecessor support / scaffold depth. A counterexample must now occur at depth at least three or exploit genuinely unbounded composition.

**Why not density language.** The exact counterexample (3.3) shows that even a one-site marginal above `rho` is insufficient for the actual first-order companion. The successful estimate uses correlations and a finite-dimensional cone.

## Handoff

`one-cell and two-cell insertion positivity proved: for the noise-reduced process L^- and arbitrary prescribed right-boundary history, the minimal affine one-left-spin companion is insertion-positive after T_2=T_rho+B/(dk); moreover an explicit three-site coupling plus the exact Metzler rho-centered moment system gives a finite T_3 after which every nonnegative two-left-spin monomial companion is insertion-positive. The next blocker is unbounded scaffold composition/support growth, not failure of the first two regional cells.`
