# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal.

## E0. Residual chamber

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Closed mechanisms include the frozen-wall route, cellwise nonnegative scaffold transfer, one-step centered `L^1` transfer, the crude scalar criterion `max{c,b-a}Z<1`, G's exposed-only global Foster product, G's full nearest-neighbour scalar edge-product/coboundary Foster class, and F's depth-uniform finite linear common-mass mode closure.

## E1. Centered predecessor trail

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's working reduction gives a canonical predecessor trail with selected interactions all births and vertical factor

$$
e^{-\omega\tau}.
$$

The exact Poisson--Mecke factorization and no-exit complement remain to be independently audited before a closing proof.

## E2. Segmentwise right killing and global criterion

The right contribution obeys

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

Define

$$
w(u)=e^{-\omega u}s_1(u),
\qquad
Z=\int_0^\infty w(u)du.
$$

The nonempty-exit term is reduced to

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Proving `J_{x,r}->0` with depth is sufficient for that term.

The crude absolute-value criterion is unusable on the residual chamber: `c>b-a` and `cZ>1` throughout `R`.

## E3. Exact mass/disagreement decomposition

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

This is the active signed branching identity. The first channel is common signed mass; the second is represented by a coupling of two conditional laws.

## E4. One-step and norm-order obstruction

Near East,

$$
a=\varepsilon^2,\quad b=\varepsilon,\quad c=1-\varepsilon^2,
$$

the exact depth-two profile changes sign. The normalized absolute-value factors tend to `3/2` without right killing and `7/5` with it. Moreover

$$
\frac g{|m_\varepsilon|}
\left|\int w(u)A_{2,\varepsilon}(u)du\right|
\to\frac35<1,
$$

while

$$
\boxed{
\frac g{|m_\varepsilon|}
\int w(u)|A_{2,\varepsilon}(u)|du
\to\frac75>1.
}
$$

Therefore duration integration cannot precede the block absolute-value norm. Pointwise positivity, one-step centered `L^1`, and duration-integrated finite-matrix iteration are closed.

## E5. Common-mass equilibrium and first transient modes contract

Let

$$
r_0=\frac1{1+b}.
$$

Student F proves

$$
\boxed{|Br_0-c|Z<\frac23}
$$

throughout the strict residual chamber.

For a signed mass component with total mass `A` and centered rightmost moment `C`, zero-boundary evolution gives

$$
M_{A,C}(u)=(Br_0-c)A+BCe^{-(1+b)u}.
$$

The pure transient cost is

$$
\boxed{
\kappa_T=B Z_{\omega+1+b}<1.
}
$$

Writing `k=1-c`, the exact denominator gap is

$$
a^2+5ab+ak+7a+4bk+6k>0.
$$

Near East,

$$
\kappa_T
=1-\frac{13}{3}\varepsilon^2
+\frac{38}{9}\varepsilon^3+O(\varepsilon^4).
$$

These are genuine profile-level damping inputs, not a proof of `J->0`.

## E6. Exact common-mass transfer is operator-valued

Slice a signed law by the current rightmost spin, `boldnu=(nu_0,nu_1)`. If `L^0,L^1` are the left-block generators with boundary spin fixed to zero or one, then

$$
\frac d{du}\boldsymbol\nu
=oldsymbol\nu
\begin{pmatrix}
L^0-I&I\\
bI&L^1-bI
\end{pmatrix}.
$$

With

$$
\mathcal S(\nu_0,\nu_1)=-c\nu_0+g\nu_1,
$$

the one-segment transfer is

$$
\boxed{
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S\bigl(\boldsymbol\nu e^{u\mathbb Q_y}\bigr).
}
$$

All duration variables must remain visible until the final `L^1(w)` norm.

## E7. Depth-uniform finite linear common-mass mode closure is impossible

On an `N`-site zero-boundary interval,

$$
\boxed{
c(x,y)(1-2x)=1-cy-(1+b)x+Bxy.}
$$

The only degree-raising term is `Bxy`. Therefore for `0<=j<N`,

$$
\boxed{
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j.
}
$$

The vectors `h_1,L_Nh_1,...,L_N^{N-1}h_1` are linearly independent. Any exact semigroup-invariant linear mode space containing `h_1` has dimension at least `N`.

**Status:** exact obstruction. Bounded disagreement/restart height does not imply bounded common-mass mode dimension. Student F Assignment 010 attacks profile regeneration/truncation instead.

## E8. Coupling inputs that remain valid

Under the common-uniform coupling every disagreement site has a positive coalescence probability at its own update. For one fixed parent disagreement, repeated exposure re-entry before that parent's first coalescence has a geometric tail and explicit exponential pgf. The principal stack-clearing construction separately gives negative height drift and an exponential height factor.

These are reusable local/renewal facts. They do not automatically compose into a global Foster theorem.

## E9. Exposed-only global Foster product is false

On a reachable all-`01` disagreement stack of height `H`, the Assignment-003 exposed-only product has exact tilted drift

$$
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
$$

For `s>1`, `e_0>=1`, finite `lambda>1`, the positive bulk term grows linearly in `H`. With the old near-East choices the drift tends to `(H-2)/7`.

**Status:** exact refutation of the exposed-only independent-level product. The old `16/21` number remains diagnostic only.

## E10. Full nearest-neighbour scalar product/coboundary Foster class is false

Let

$$
\mathcal A=\{00,11,01,10\}
$$

and consider every positive nearest-neighbour scalar edge product

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i}.
$$

At the strict residual point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

Student G gives an exact normalized rational circulation `mu` on the 64 triple phases with:

1. spatial flow conservation;
2. zero expected exponent change in all 16 edge-weight coordinates;
3. positive exposure-entry flux `R_mu` and changing-update mass `C_mu`.

For every positive `Q` and every `s>1`, weighted AM--GM yields

$$
\boxed{
\sum_e\mu_eG_Q(e)
\ge
C_\mu\left(s^{R_\mu/C_\mu}-1\right)>0.
}
$$

Any coboundary inequality would force the circulation average to be nonpositive. Hence no positive `Q` and potential `psi` can satisfy the 64 bulk inequalities. Equivalently some repeatable spatial cycle has positive mean bulk drift for every `Q,s`.

Because this is a repeatable bulk obstruction, finite boundary/height/insertion corrections cannot repair the class.

**Status:** exact refutation of the entire nearest-neighbour scalar product/coboundary Foster class at one strict residual point. Matrix-product/nonlocal correctors and other finite temporal states are not ruled out.

## E11. Current common-mass target: profile truncation

Student F Assignment 010 seeks a depth-uniform quantitative truncation/ancestry-tail theorem for the operator-valued common-mass profile in the exact `J`-compatible norm. The preferred mechanism is regeneration by environment-independent reset clocks, with constants allowed to deteriorate arbitrarily near East.

A success must show that dependence extending more than `M` sites from the moving boundary has weighted mass `delta_M->0` uniformly in remaining trail depth. A failure should exhibit a non-negligible deep ancestry obstruction.

## E12. Current coupling target: viability of the common-uniform coupling

After two structural failures of scalar local global-corrector classes, do not enlarge local scalar phase alphabets mechanically.

Student G Assignment 006 asks whether a finite disagreement seed under the common-uniform coupling survives forever with positive probability at a strict near-East residual point.

- **If survival is proved:** global coalescence/regeneration of this synchronous coupling is unavailable as a proof mechanism at that point; local coupling identities may still be used inside the signed representation.
- **If extinction is proved:** the needed theorem must be genuinely nonlocal, bundling interior restart creation before charging the norm.

This is a structural viability test for the coupling route, not a test of ergodicity itself.

## E13. Composition target

The active route can reach `J_{x,r}->0` only if the common-mass profile hierarchy is quantitatively controlled and the disagreement channel is handled by a mechanism compatible with the outcome of E12. No finite local scalar Foster state or depth-uniform finite common-mass matrix remains available.

## E14. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not use `16/21` as a global Foster theorem, enlarge scalar local corrector contexts mechanically, integrate duration before absolute value, revive a depth-uniform finite common-mass mode state, iterate diagnostic duration-integrated matrices as the proof kernel, return to one-step `(T)`, or replace the signed mass/disagreement structure by unrestricted total variation.
