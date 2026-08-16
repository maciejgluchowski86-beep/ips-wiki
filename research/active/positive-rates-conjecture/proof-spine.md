# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal. Proof routes may be abandoned; the target does not change.

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

The frozen-wall route, cellwise nonnegative scaffold transfer, and one-step centered `L^1` transfer are closed.

## E1. Direct coupling inputs

Every disagreement site under the common-uniform coupling has predictable coalescence intensity at least

$$
q:=1-c+a>0.
$$

The local disagreement drift is

$$
\mathcal L^{\rm coup}D_i
\le-qD_i+(b-a)D_{i+1}+(c-b+a)J_i.
$$

Student G's single-exposure calculation gives exact weighted control of the local high-risk state `J_i`; crude global summation fails near East because of repeated exposure restarts.

**Status:** reusable coupling machinery.

## E2. Centered predecessor-trail reduction

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's centered-dual working reduction gives a canonical predecessor trail of depth `n=r-x+1`, selected residual interactions all births, and vertical factor

$$
\boxed{e^{-\omega\tau}.}
$$

The exact Poisson-Mecke factorization and the no-exit complementary term still require independent audit before a closing proof.

**Status:** active working reduction.

## E3. Segmentwise right-region killing and correction

The right contribution obeys

$$
\boxed{|R_{\gamma,t}(\eta)|\le C_A\prod_{k=1}^n s_1(u_k),}
$$

where `s_1` is survival of the killed two-state chain

$$
K=\begin{pmatrix}-a&a\\1&-(1+B)\end{pmatrix}.
$$

Define

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
\boxed{
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{2ab+3a-bc+b-2c+2}.
}
$$

The crude absolute-value criterion would be

$$
\max\{c,g\}Z<1.
$$

Student F Assignment 007 proves throughout the residual chamber

$$
c>g
\qquad\text{and}\qquad
\boxed{cZ>1}.
$$

Hence the crude criterion has **no residual solutions**. This corrects Meeting 006, which had described it as an already-proved residual subregion.

**Status:** segmentwise right bound valid; crude scalar contraction useless on the unresolved chamber.

## E4. Exact depth-two obstruction to one-step contraction

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the exact two-level invariant scalar changes sign and the absolute-value ratios satisfy

$$
\frac{g}{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|du\to\frac32,
$$

and with segmentwise right killing

$$
\frac{g}{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|du\to\frac75.
$$

**Status:** exact obstruction. Pointwise regional positivity and one-step centered `L^1` contraction are closed.

## E5. Correct global right-weighted invariant criterion

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

The working trail representation gives

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le C_A\sum_{x\in A}J_{x,r}.
$$

Thus `J_{x,r}->0` with depth is sufficient for the nonempty-exit term.

## E6. Exact mass/disagreement decomposition

For a probability law `mu`, rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

This splits each transfer into a signed mass channel and a positive conditional-law disagreement channel. Near East, the equilibrium mass multiplier after right weighting tends to `2/5`, while unrestricted absolute values expand.

**Status:** active structural identity.

## E7. Stack-clearing height drift

The accepted reset-coupling construction gives a clearing variable `K` with

$$
P(K\ge j\mid\mathcal F)
\ge
\alpha2^{-(j-1)},
\qquad
\alpha=\frac{B+\omega}{B+2\omega},
$$

and one transfer adds at most one unresolved level:

$$
H'\le(H-K)_++1.
$$

Consequently the unweighted height has negative drift. The geometric minorant `kappa` gives, for

$$
\phi(\lambda)
=\lambda\left(1-\alpha+\frac{\alpha}{2\lambda-1}\right),
$$

an interval of `lambda>1` on which `phi(lambda)<1`.

**Status:** accepted height control; does not itself control signed branching.

## E8. Student G same-parent restart theorem

Let `h=h_1<1` be the worst single-exposure child-before-parent-coalescence probability from Meeting 007. Fix one parent disagreement and let `N` be the number of entries of its left edge into exposure before that same parent first coalesces.

Strong Markov gives

$$
\boxed{P(N\ge n\mid\mathcal F)\le h^{n-1},\qquad n\ge1.}
$$

Hence for `1<=s<h^{-1}`,

$$
\boxed{E[s^N\mid\mathcal F]\le M(s):=\frac{(1-h)s}{1-hs}.}
$$

This sums arbitrarily many deaths/reinfections while the same parent remains alive.

Along the near-East path, the algebraic stress choice `lambda=2`, `s=1+epsilon^2/4` gives

$$
M(s)\phi(2)\to\frac{16}{21}<1.
$$

**Status:** same-parent geometric tail and pgf Professor-checked. `16/21` is a coupling-side height/restart factor, not a multiplier for `J_{x,r}`.

## E9. Unverified lift from scalar restart bounds to a global product corrector

Student G proposes a finite local phase corrector `C_s` over all unresolved levels and a global Foster inequality

$$
E[s^{\Delta R}V_s(\Sigma')\mid\mathcal F]
\le\theta V_s(\Sigma),
\qquad
V_s(\Sigma)=\lambda^{H(\Sigma)}C_s(\Sigma),
$$

outside a finite height set.

The scalar pgf, height minorant, finite-height correction, and near-East algebra check. The missing proof is the global phase bookkeeping: inactive/exposed/child-alive states and later new-parent reinfections must be explicitly represented, and the proposed corrector must be shown transition by transition to be superharmonic for simultaneous unresolved levels.

**Status:** open technical lemma. Student G Assignment 004 attacks exactly this point.

## E10. Conditional finite bounded-height signed kernel

Assume E9 in the following explicit conditional form:

> arbitrary-height restart/disagreement excursions outside a finite stack-height/phase set return with a strict multiplicative factor.

Then the remaining block problem is finite: on bounded height/phases, combine the signed mass coefficient `Br-c`, disagreement coefficient `Br(1-r)`, and right weight `w(u)` into a finite signed kernel. The target is a finite block/spectral-radius statement

$$
\rho(K_{H_0}^{m_0})<1
$$

or an equivalent weighted norm estimate.

The fact `cZ>1` shows that an absolute-value scalar kernel cannot work; the bounded kernel must use the mass/disagreement cancellation.

**Status:** Student F Assignment 008 attacks this finite signed problem conditional on E9.

## E11. Composition to the trail criterion

If E9 and E10 both hold, combine the large-height Foster contraction and bounded-height signed kernel to obtain

$$
J_{x,r}\to0.
$$

Only after that should the full trail factorization and no-exit contribution be reconstructed into an ergodicity proof.

## Anti-circularity checkpoint

Meeting 008 eliminates the purported easy residual region and proves that same-parent restart count has a uniform geometric tail. The block theorem is now split into two precise complementary lemmas: the global restart-corrector lift and the bounded-height signed kernel. No further one-step scalar criteria or finite-depth enumeration count as progress.
