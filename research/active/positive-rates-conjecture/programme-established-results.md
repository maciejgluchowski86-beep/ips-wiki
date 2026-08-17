# Positive-rates programme: established results

Date: 2026-08-17

The target was the positive-rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour IPS. On the normalized face `r11=0`, write

\[
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
\]

with residual chamber

\[
\mathcal R=\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
\]

The conjecture was **not proved**. What follows is the compact record of mathematics that the programme did establish and that is worth retaining independently of the stopped proof architectures.

## Certification convention

The principal reports having run all 25 committed verifier scripts. In their **current** form all 25 pass. Two initially failed only because SymPy retained algebraically equivalent symbolic forms: F012's original `Piecewise` assertion was repaired at `5494008`, and G010e's radical structural-equality assertion was repaired at `ce77c9c`. No mathematical identity changed in either repair.

Below, **verifier-backed** means that a committed executable checks the quoted scalar identities, finite algebra, or exact inequalities. Several depth-free arguments are analytic/operator derivations and have no executable checker; these are marked **proof-only**. A passing scalar verifier should not be read as machine verification of every surrounding infinite-depth argument.

## 1. Exact reductions and structural theorems

### Centered predecessor-trail reduction and the canonical `J` quantity

The principal's centered predecessor-trail decomposition gives an exact representation of the nonempty-exit contribution in which duration variables remain visible until the final modulus. For singleton depth `n`, the canonical absolute-duration quantity satisfies

\[
\boxed{J_n=\frac BgR_n=\frac gBN_n},
\qquad B=b+c-a,\quad g=b-a,
\]

so the three normalizations have the same exponential growth rate. More generally, decay of the corresponding `J_{x,r}` quantities is a sufficient condition for the predecessor-trail remainder to vanish. This is the main exact reduction connecting the later renewal analysis back to ergodicity. **Proof-only** for the full reduction; the normalization and finite calibration were checked by G009's exact verifier.

### Zero-boundary profile locality and damage-to-tail-shift theorem

For the projective zero-boundary invariant law `mu`, the stationary boundary discrepancy is exactly a spatial shift defect:

\[
\boxed{\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}}},
\qquad
\lim_{M\to\infty}\Delta_M=\|\theta\mu-\mu\|_{\mathcal T}.
\]

The coupling/profile comparison then gives

\[
\boxed{\Delta_M\le 2c\int_0^\infty \beta_{M-1}(t)\,dt.}
\]

Hence integrable zero-boundary Hamming susceptibility implies tail-shift agreement; in particular one finite-time contraction `alpha_0(T)<1` would imply explicit exponential decay of `Delta_M`. The shift identity is verifier-backed by `a845bf2`; the susceptibility estimate is verifier-backed in its repaired form `5494008`.

### Common-uniform coupling: local erasure and convective escape

For finite initial disagreement sets under the common-uniform coupling, disagreements are not created spontaneously to the right, the rightmost disagreement is nonincreasing, and the current rightmost disagreement has permanent-coalescence hazard at least

\[
\omega=1-c+a>0.
\]

Every fixed site therefore becomes permanently coupled almost surely; survival of the disagreement process is equivalent to convective escape to `-infinity`. The pointwise drift estimate is

\[
\boxed{\mathcal L^{\rm coup}D_i\le -\omega D_i+cD_{i+1}},
\]

which yields exponential contraction of a suitable moving-frame weighted disagreement whenever the spatial weight parameter satisfies `z>c/omega`. These statements are verifier-backed by `43f4bb1`.

At the hard near-East point

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

a separate exact finite-time certificate proves

\[
\alpha(t)>1\qquad(0<t\le47).
\]

The finite-window approximation of `alpha(T)` is itself controlled by explicit Poisson tails. This certificate uses exact rational interval arithmetic and finite uniformization and passed as committed.

### Stationary boundary-control hierarchy

For the `N`-site process with arbitrary state-dependent right-boundary control `u\in\{0,1\}`, define the stationary occupation polytope

\[
\mathcal K_N=\left\{m(x,u)\ge0:\ \sum m=1,\ \sum m(x,u)L_N^uF(x)=0\ \forall F\right\}.
\]

Every infinite-volume invariant law projects into `\mathcal K_N`; conversely every `m\in\mathcal K_N` is realized by a finite irreducible chain with randomized state-dependent boundary policy. The hierarchy projects consistently, so for local `h`

\[
D_N(h):=\sup_{m\in\mathcal K_N}m(h)-\inf_{m\in\mathcal K_N}m(h)
\]

is nonincreasing in `N`, and `D_N(h)\to0` for every local `h` would imply uniqueness of the invariant measure. Exact LP duality gives Bellman endpoints `U_N,\ell_N` with `D_N=U_N-\ell_N`.

F015 further proves the exact scale-extension identity

\[
\boxed{D_M=D_N-\inf_{\mathcal K_M}m(s_N^+)-\inf_{\mathcal K_M}m(s_N^-)},
\]

where the slacks are weighted adaptive boundary-action mismatches. There is also the controller-uniform unweighted mismatch bound

\[
\Pr(V\ne\pi(X))\ge \frac{r_*}{N+1+r_*},
\qquad r_*:=\min\{a,1-c\}.
\]

These are **proof-only**; no executable verifier was committed for the hierarchy.

### Exact trajectory-valued spatial kernel

The zero-boundary stationary trajectory field is an exact spatial Markov chain on one-site path space with transition kernel `Q`: conditional on the right-neighbour trajectory, the left trajectory is generated by independent reset/refresh marks. Throughout the residual chamber,

\[
\boxed{Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot)}.
\]

Consequently the full path-space Dobrushin TV coefficient is `1`; for mixtures of the two constant inputs, TV distance is preserved exactly and KL divergence is likewise preserved. This is a useful structural theorem about the actual residual model, not merely a failed coupling attempt. **Proof-only**; the Professor independently reconstructed the path-law argument, but there is no committed executable checker.

## 2. Renewal and positive-frequency structure

### Singular fixed-depth renewal theorem

Along

\[
a=\varepsilon,\qquad b=\frac1{10},\qquad 1-c=\frac\varepsilon{10},
\]

G009 proves, for every fixed depth `n`,

\[
\boxed{
\lim_{\varepsilon\downarrow0}\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=\left(\frac{499}{341}\right)^{n-1}},
\]

and therefore

\[
\boxed{
\lim_{\varepsilon\downarrow0}J_n(\varepsilon)
=\frac{2079}{341}\left(\frac{499}{341}\right)^{n-1}}.
\]

The base has the exact decomposition

\[
\frac{499}{341}=\frac{10}{11}+\frac{189}{341}>1.
\]

The short channel is governed by the all-depth East Green identity

\[
\boxed{\ell_{m-1}E_m(-L_m^E)^{-1}=\frac{10}{11}\ell_m}.
\]

This theorem is in the singular order of limits `epsilon -> 0` at fixed depth and does not imply fixed-rate growth. **Proof-only** for the convergence theorem; the accompanying verifier checks the exact constants and the East basis identity through depth nine.

### Exact fixed-filter connected renewal at the actual point `P_*`

At the actual strict residual point

\[
P_*=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
\]

fix

\[
\sigma(u)=1-2e^{-4u/125}.
\]

Writing `H_N^sigma=z_sigma Pi_N+Q_N^sigma` and expanding invariant projections exactly as renewal separators gives

\[
\boxed{V_n=\sum_{k=1}^n\lambda_kV_{n-k},\qquad V_0=1.}
\]

This is an exact fixed-rate connected-renewal recurrence for the **actual `P_*` dynamics**, not a reversible approximation. The first seven coefficients are exact rationals, with

\[
\lambda_1,\ldots,\lambda_5>0,\qquad \lambda_6,\lambda_7<0,
\]

and

\[
\sum_{k=1}^7\lambda_k\approx1.04715575732980380.
\]

Commit `e4452de` verifies the complete finite prefix exactly. The recurrence itself is **proof-only**.

The actual `P_*` terminal factor

\[
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}
\]

has a depth-independent signed-kernel estimate giving

\[
\boxed{
\operatorname{osc}\!\left(R_{N+1}Q_{N+1}(Y_{N+1}f)\right)
\le q_\sharp\operatorname{osc}(f)},
\]

with

\[
q_\sharp=B\Theta_\sharp\approx0.9807372831525678<1.
\]

The exact scalar certificate is the repaired running verifier `ce77c9c`; the all-depth operator inequality uses the semigroup argument in the report.

A complementary decomposition removes the artificial positive-frequency zero of `R_N`:

\[
\boxed{R_N=m_0I+g_0(I-K_N)},
\qquad K_N=(1+b)((1+b)I-L_N)^{-1}.
\]

The genuine high-pass `I-K_N` vanishes only at zero frequency. The two channels have uniform one-step bounds and, after one insertion, even their channelwise triangle estimate is strictly below one. This is a real one-step contraction statement but not yet an iterable vector norm.

### Frozen-weight reversible reference theorem

The nearby reversible point

\[
P_0=\left(\frac1{10000},\frac1{10},\frac{999}{1000}\right)
\]

was used only as a **generator/insertion reference**. The actual `P_*` duration weight and filter are held frozen externally; preserving `B` and `omega` does not preserve the canonical duration law.

In `L^2(mu_0)`, with `A_{0,N}=-L_{0,N}`, the fixed scalar multiplier `q(x)` satisfies

\[
|xq(x)|<1\qquad(x>0),
\]

and the fresh centered insertion obeys

\[
\boxed{M_X^*A_{0,N}^{-1}M_X\le\frac{998001}{11000000}I}.
\]

Consequently

\[
\boxed{
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le\left(\sqrt{\frac{998001}{11000000}}+\frac9{400}\right)\|f\|_2<\|f\|_2.}
\]

Verifier `56d47cb` checks the exact rational multiplier inequalities and the strict margin. The variational inequality is **proof-only**.

The same reference model also has an exact orthogonal left-slice recursion

\[
L_{0,N}=L_{0,N-1}\oplus G_{N-1},
\]

so the complete frozen-reference transfer norm reduces to a single killed self-adjoint channel family `H^sigma(G_n)J_n`. This reduction is **proof-only** and does not by itself transport to the actual nonreversible `P_*` process.

## 3. Reusable class-level obstruction theorems

The programme proved several no-go statements broad enough to be worth retaining as theorems rather than merely failed attempts.

At the hard near-East point `P_h`, an exact rational balanced circulation rules out **every nearest-neighbour scalar edge-product/coboundary Foster certificate** in the 16-phase class. The circulation has positive exposure-entry flux but zero circulation of every scalar edge potential, so weighted AM-GM gives a contradiction. This is verifier-backed by `3963d86`.

A separate mode-growth theorem shows that no depth-uniform finite linear generator-mode closure can contain the common-mass transfer: on `N` sites,

\[
L_N^j h_{p_*}(\eta_1)=q_*^{-1}B^j\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
\]

so the cyclic dimension grows at least linearly with `N`. The associated symbolic checks were committed with the F009 verifier; the depth-free degree argument is analytic.

For the actual `P_*` coefficient generator, even the natural two-parameter refinement

\[
\|f\|_{\theta,\phi}=\sum_{A\ne\varnothing}\theta^{|A|}\phi^{\kappa(A)}|x_A|
\]

cannot make the raw nonconstant semigroup uniformly nonexpansive in depth. Long blocks, separated dimers, and separated singletons force incompatible necessary inequalities. The decisive rational inequalities are verifier-backed by `adf50d9`. Thus cancellation has to remain at the signed filter/resolvent level rather than being postponed until after a positive raw-semigroup estimate.

The stationary Bellman framework also gives a general additive-corrector obstruction: an appended correction of the form `F_N(x)+G(z)` cannot improve the Bellman endpoints; any genuine scale improvement must use cross-block dependence. This is **proof-only**.

## 4. The single residual object of the connected-renewal route

At `P_*`, recenter the fresh insertion by

\[
r=\frac{11}{10},\qquad \varepsilon=\frac9{10000},\qquad X_N=Y_N+\varepsilon,\qquad g_0=\frac{999}{10000}.
\]

The exact intertwining is

\[
A_NM_{X_N}=M_{X_N}(A_{N-1}+r)-g_0B M_{\eta_N}P_{N-1}.
\]

After regrouping `Y=X-\varepsilon`, the fresh shifted and scalar branches are individually subcritical:

\[
\boxed{BZ_{\omega+r}=\frac{1065933}{1068400}<1},
\qquad
\boxed{\varepsilon Z=\frac{1719}{3100}<1}.
\]

These exact scalars are checked by the running verifier `adf50d9`. What remains is the signed right-boundary transmission Volterra operator

\[
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{24mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt,
\end{aligned}}
\]

where

\[
h(t)=w_*(t)\sigma(t),\qquad \sigma(t)=1-2e^{-4t/125}.
\]

For the renewal problem the input is the **actual connected orbit**. Both `h(t)` and `g_0e^{-rs}-\varepsilon` change sign, so taking absolute values before the two integrations destroys exactly the remaining cancellation. No depth-uniform estimate retaining this two-time cancellation was proved.

This formulation is strictly narrower than the old unrestricted tail-shift problem: the stationary marginal-discrepancy functional can be eliminated algebraically from the connected coefficient before estimating it.

## 5. What remains open and what would restart the programme

The positive-rates conjecture in the residual chamber remains open. So do `(J-SPEC)`, the sufficient connected-tail bound

\[
\sum_{k\ge8}|\lambda_k|<\sum_{k=1}^7\lambda_k-1,
\]

and the sign-cancelling estimate for `\mathcal V_N` on the actual connected orbit. Common-uniform extinction versus convective survival, stationary diameter collapse `D_N(h)\to0`, and one-/two-step shift agreement for the zero-boundary invariant law also remain unresolved.

For this particular connected-renewal branch, the restart bar is now specific: new input must control `\mathcal V_N` on the actual connected orbit strongly enough to make the connected renewal coefficients summable/geometric, while retaining its two-time cancellation. A materially different proof architecture would also qualify. Another finite coefficient table, filter optimization, generic norm search, reversible comparison, bare tail-shift argument, common-coupling occupation variant, or generic Bellman-corrector search does not by itself clear that bar.
