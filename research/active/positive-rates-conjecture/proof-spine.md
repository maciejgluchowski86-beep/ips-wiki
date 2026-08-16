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
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Closed mechanisms: frozen finite walls; cellwise nonnegative scaffold transfer; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; exposed-only global Foster product; complete nearest-neighbour scalar edge-product/coboundary Foster class; depth-uniform finite linear common-mass mode closure.

## E1. Centered predecessor trail and global criterion

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The working predecessor-trail reduction leaves

$$
\boxed{
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Proving `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits after `J` decay is proved.

## E2. Exact signed branching identity

For a law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first channel is signed common mass; the second is a conditional-law disagreement channel.

## E3. Norm-order obstruction

Near East,

$$
a=\varepsilon^2,\quad b=\varepsilon,\quad c=1-\varepsilon^2,
$$

the exact depth-two profile changes sign. The signed duration average gives an apparent normalized `3/5`, but the actual `J`-compatible quantity gives `7/5`:

$$
\frac g{|m_\varepsilon|}\left|\int wA_{2,\varepsilon}\right|\to\frac35,
\qquad
\boxed{
\frac g{|m_\varepsilon|}\int w|A_{2,\varepsilon}|\to\frac75.}
$$

Therefore duration integration cannot precede the block absolute-value norm. Duration-integrated finite matrices are diagnostic only.

## E4. Common-mass scalar damping

Let

$$
r_0=\frac1{1+b}.
$$

The equilibrium and first transient mass modes satisfy

$$
\boxed{|Br_0-c|Z<\frac23,}
\qquad
\boxed{\kappa_T=BZ_{\omega+1+b}<1.}
$$

Writing `k=1-c`, the exact transient denominator gap is

$$
a^2+5ab+ak+7a+4bk+6k>0.
$$

Near East,

$$
\kappa_T=1-\frac{13}{3}\varepsilon^2+rac{38}{9}\varepsilon^3+O(\varepsilon^4).
$$

These are genuine damping inputs, not a proof of all-depth contraction.

## E5. Exact common-mass transfer is operator-valued

Slice a signed law by the current rightmost spin, `boldnu=(nu_0,nu_1)`. With left generators `L^0,L^1`,

$$
\frac d{du}\boldsymbol\nu
=oldsymbol\nu
\begin{pmatrix}
L^0-I&I\\
bI&L^1-bI
\end{pmatrix}.
$$

The centered insertion projection is

$$
\mathcal S(\nu_0,\nu_1)=-c\nu_0+g\nu_1,
$$

so

$$
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S(\boldsymbol\nu e^{u\mathbb Q_y}).
$$

All duration variables remain visible until the final `L^1(w)` norm.

## E6. Depth-uniform finite linear mode closure is impossible

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence the cyclic subspace has dimension at least `N`. Bounded disagreement height does not imply bounded common-mass mode dimension.

**Status:** exact obstruction. Do not enlarge finite common-mass alphabets.

## E7. Assignment 010: exact suffix projectivity

Let `R_{N,M}` marginalize onto the rightmost `M` sites. One-sidedness gives

$$
R_{N,M}(\nu P_u^N)=(R_{N,M}\nu)P_u^M,
$$

and insertion/drop commutes with suffix marginalization. Consequently

$$
R_{N,M}\pi_N=\pi_M.
$$

A perturbation outside the retained `M`-site suffix is exactly invisible to scalar reverse-trail output for the next `M` transfers.

**Status:** Professor-accepted.

## E8. First invariant insertion is depth-uniformly truncatable

Under the projective half-line invariant law, put

$$
Y=B\eta_0-c,
\qquad
K_M=E[Y\mid\eta_{-M},\ldots,\eta_{-1}].
$$

Then

$$
K_M\to K_\infty\quad\text{in }L^1,
$$

and

$$
\varepsilon_M:=\sup_{n\ge M}\|K_n-K_M\|_1\to0.
$$

Thus for all finite depths `N>=M+1` and bounded left functions `F`,

$$
\boxed{
|\pi_N((B\eta_N-c)F)-\pi_N(K_M^{(N)}F)|
\le\varepsilon_M\|F\|_\infty.}
$$

This is finite-context approximation, not finite Markov order.

## E9. Explicit equilibrium gap localization

If `f` is supported at least `M` sites left of the zero boundary, Assignment 010 proves

$$
\boxed{
\left|\pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.}
$$

The proof uses a positive resolvent parameter `1+b` and one-sided finite propagation.

Likewise one semigroup segment obeys

$$
\boxed{
\int_0^\infty w(u)\|P_uf-P_u^{(M)}f\|_\infty du
\le\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.}
$$

Scalar iteration is unavailable because it reintroduces `cZ>1`.

## E10. Current common-mass blocker: zero-frequency boundary response

After one insertion the mass branch is `bar pi_N`, not `pi_{N-1}`. The exact discrepancy is

$$
\boxed{
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].}
$$

This is a zero-frequency resolvent. Finite speed alone is not integrable at long times.

Define, for `M>=2`,

$$
\Delta_M
=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
|\bar\pi_N(f)-\pi_{N-1}(f)|.
$$

**Current question:** does

$$
\boxed{\Delta_M\to0?}
$$

Student F Assignment 011 must prove this throughout the strict residual chamber, refute it at one strict residual point, or reduce it to one explicit theorem. If positive, it must be lifted at least to one post-insertion mass-branch truncation estimate.

## E11. Coupling facts that survive

The same-parent geometric restart theorem and separate stack-clearing minorant remain valid. They do not compose into a scalar local global Foster theorem.

G's exposed-only product is refuted by long all-`01` stacks. The complete nearest-neighbour scalar edge-product/coboundary class is refuted at a strict near-East point by an exact balanced circulation with positive restart flux and zero scalar `Q`-energy change.

**Status:** no finite local scalar Foster state remains.

## E12. Current coupling viability test

Student G Assignment 006 asks whether the common-uniform disagreement process survives forever with positive probability from a finite seed at a strict near-East residual point.

- Survival closes any proof requiring global coalescence of this synchronous coupling.
- Extinction must be accompanied by a genuinely nonlocal quantitative regeneration theorem.

This is a structural viability test, not an ergodicity test.

## E13. Route-level checkpoint

Both active lines now point to nonlocal structure. Do not authorize open-ended matrix-product/nonlocal norm construction until F011 and G006 return.

- If F011 refutes zero-frequency boundary locality, the current profile-truncation implementation closes.
- If G006 proves finite-seed survival, the current global-coalescence coupling implementation closes.
- If one or both are positive, use the exact theorem obtained rather than restarting generic norm engineering.

After both returns, hold a route-level expected-value review.

## E14. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value, use `16/21` as a global Foster theorem, enlarge scalar local coupling products mechanically, revive a finite common-mass mode state, replace the signed structure by unrestricted total variation, or assume the positive rates conjecture / an unproved uniform spectral gap in E10.
