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

Near East, duration integration before the absolute value gives a false apparent contraction `3/5`, whereas the actual `J`-compatible depth-two factor tends to `7/5`:

$$
\frac g{|m_\varepsilon|}\left|\int wA_{2,\varepsilon}\right|\to\frac35,
\qquad
\frac g{|m_\varepsilon|}\int w|A_{2,\varepsilon}|\to\frac75.
$$

Therefore all duration variables must remain visible until the final `L^1(w)` norm.

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

These are genuine damping inputs, not an all-depth theorem.

## E5. Exact common-mass transfer is operator-valued

The duration-resolved one-segment transfer has the operator form

$$
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S(\boldsymbol\nu e^{u\mathbb Q_y}),
$$

where the entries of `Q_y` contain the left-block generators. No depth-uniform finite matrix replaces this exact object.

## E6. Depth-uniform finite linear common-mass mode closure is impossible

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence the cyclic subspace has dimension at least `N`.

**Status:** exact obstruction. Do not enlarge finite common-mass alphabets.

## E7. Exact suffix projectivity and first-insertion truncation

Rightmost suffixes are autonomous, so semigroup evolution and centered insertion/drop intertwine with suffix marginalization. Consequently

$$
R_{N,M}\pi_N=\pi_M.
$$

For the projective half-line law, the first invariant centered insertion has conditional coefficient

$$
K_M=E[B\eta_0-c\mid\eta_{-M},\ldots,\eta_{-1}],
$$

with

$$
\sup_{n\ge M}\|K_n-K_M\|_1\to0.
$$

This is a genuine depth-uniform finite-context approximation, not finite Markov order.

## E8. Explicit equilibrium localization and one-segment tail

For a bounded test function separated by `M` sites from the boundary,

$$
\left|\pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
$$

One weighted semigroup segment also satisfies

$$
\int_0^\infty w(u)\|P_uf-P_u^{(M)}f\|_\infty du
\le\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.
$$

Scalar iteration is unavailable because it reintroduces `cZ>1`.

## E9. Zero-frequency boundary response and tail-shift reduction

After one insertion the mass branch is `bar pi_N`, not `pi_{N-1}`. Its exact discrepancy is the zero-frequency response

$$
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].
$$

Let `mu=pi_infty^0`, let `theta` drop the boundary-nearest spin, and define

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m.
$$

For the far-left boundary-response norm `Delta_M`, F proves

$$
\boxed{
\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
}
$$

and reverse-martingale convergence yields

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Thus zero-frequency locality is exactly the tail-shift theorem

$$
\boxed{
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
\tag{TS}
$$

Separate tail 0--1 laws do not imply `(TS)`.

**Status:** exact reduction, unresolved. Student F Assignment 012 decides `(TS)` or produces a genuinely stronger structural criterion.

## E10. Conditional one-next-segment mass lift

Let `m_0=Br_0-c` and `kappa_E=|m_0|Z`. If `Delta_M->0`, then for `1<=d<M`,

$$
\boxed{
\int_0^\infty w(u)
|m_0(\bar\pi_N-\pi_{N-1})(P_u f)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
$$

Choosing `d~M/2` makes the first post-insertion mass-branch truncation error vanish. Arbitrary signed-profile iteration still remains open.

## E11. Closed scalar coupling architectures

The same-parent geometric restart theorem and separate stack-clearing minorant remain valid. The exposed-only product fails on long all-`01` stacks. The entire nearest-neighbour scalar edge-product/coboundary class is refuted at a strict near-East point by the balanced-circulation AM--GM certificate.

No finite local scalar Foster state remains.

## E12. Actual common-uniform coupling: local erasure and convective alternative

For every finite initial disagreement seed, no disagreement can be created to the right of an already coupled right half-line. The current rightmost disagreement coalesces permanently with hazard at least

$$
q=1-c+a.
$$

Hence every fixed site becomes permanently coupled almost surely.

If `sigma_m` is the first discovery time of the `m`-th new site to the left, then

$$
P(\sigma_m\le t)\le P(\operatorname{Pois}(t)\ge m).
$$

Therefore

$$
\boxed{
\{D_t\ne\varnothing\ \forall t\ge0\}
=
\{\sigma_m<\infty\ \forall m\ge1\}
\quad\text{a.s.}
}
$$

Finite-seed survival, if it occurs, is purely convective escape to `-infinity`.

## E13. Moving-frame contraction of actual disagreement

The common-uniform transition table gives

$$
\boxed{
\mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1}.
}
$$

Thus for every `z>c/q`,

$$
\boxed{
E\sum_i z^iD_i(t)
\le e^{-(q-c/z)t}\sum_i z^iD_i(0).
}
$$

This proves exponential stabilization of every fixed spatial window. It does not rule out a cloud translating left.

At the strict rational point `(a,b,c)=(1/10000,1/100,9999/10000)`, `q=1/5000`; `z=10000` gives rate `10001/100000000`.

## E14. Finite-time random-map Hamming criterion

Let `Phi_t` be one graphical slab and

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

G proves path extension and

$$
\boxed{
\alpha(t+s)\le\alpha(t)\alpha(s).
}
$$

If

$$
\boxed{\alpha(T)<1}
$$

for one finite `T`, then every finite seed becomes extinct with exponential block-time tail:

$$
E|D_{nT}|\le\alpha(T)^n|D_0|,
\qquad
P(\tau>nT)\le\alpha(T)^n|D_0|.
$$

This is a genuine nonlocal time-block criterion, not a spatial product corrector.

## E15. Exact finite controlled-CTMC certificate hierarchy

For finite `L,R`, let `A_{L,R}(T)` be the maximal expected disagreement count in `[-L,0]` at time `T` in the finite controlled chain that keeps full pair states on `[-L,0]`, common spins on `[1,R]`, and allows an adversarial predictable common boundary spin at `R+1`.

Then

$$
\boxed{
\alpha(T)
\le
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+].
}
$$

A verified right side below one proves global extinction.

At the hard rational point, the single-seed geometry with an `01` source, common right spin zero, and common left spin one has

$$
\left.\frac d{dt}E|D_t|\right|_{t=0}
=c-q=\frac{9997}{10000}>0.
$$

Thus any eventual Hamming contraction must emerge only after finite-time nonlocal clearing.

**Status:** no certificate below one yet; no survival theorem. Student G Assignment 007 executes this exact finite diagnostic and may tighten the finite hierarchy if the controlled boundary is too pessimistic.

## E16. Route-level checkpoint

The active route is now split into two precise nonlocal decision theorems:

1. F012: prove or refute tail-shift agreement `(TS)` on the common-mass side;
2. G007: prove `alpha(T)<1` at the hard near-East point, prove genuine convective survival, or sharpen the finite random-map approximation enough to decide which is plausible.

Do not authorize general matrix-product/nonlocal norm construction. The promised route-level expected-value review is due when F012 returns; G007 is allowed in parallel only because it executes the exact diagnostic produced by G006.

## E17. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is actually proved should the group audit the exact predecessor-trail Poisson--Mecke factorization, complementary no-exit term, and final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; use `16/21` as a global Foster theorem; enlarge scalar local coupling products mechanically; revive a finite common-mass mode state; replace the signed structure by unrestricted total variation; assume an unproved uniform spectral gap / positive rates conjecture; infer tail-shift agreement from separate tail triviality; import the predecessor-trail reset-height drift into the actual common-uniform disagreement process; infer global extinction from fixed-site coalescence or moving-frame contraction; or infer survival from failure of a finite upper certificate.
