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

The frozen-wall route and the cellwise nonnegative scaffold-transfer route are closed.

## E1. Direct coupling inputs retained

For the common-uniform coupling, every disagreement site has predictable coalescence intensity at least

$$
q:=1-c+a>0.
$$

This yields true one- and two-generation regeneration and finite-depth ordered clearing. The crude finite-depth clearing gaps are summable and do not prove arbitrary-depth extinction.

The local disagreement drift is

$$
\mathcal L^{\rm coup}D_i
\le
-qD_i+(b-a)D_{i+1}+(c-b+a)J_i.
$$

Student G's transient zero-density and adjacent-`11` estimates remain available but do not close this drift marginally.

**Status:** reusable direct dynamics; no finite-generation escalation.

## E2. Centered predecessor-trail reduction

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's centered-dual decomposition gives, on the nonempty-exit event, a canonical predecessor trail of depth `n=r-x+1` whose selected residual interactions are births and whose complete vertical factor is

$$
\boxed{e^{-\omega\tau}.}
$$

After conditioning on the decorated trail, spacetime splits into left region, trail, and right region. The exact Poisson-Mecke identity is an active working lemma and still requires independent audit before a closing proof.

The no-exit complementary term must also be retained in the final convergence reconstruction.

**Status:** active reduction, not yet independently audited as a final theorem.

## E3. Segmentwise right-region killing

The right contribution has the stronger bound

$$
\boxed{|R_{\gamma,t}(\eta)|\le C_A\prod_{k=1}^n s_1(u_k),}
$$

where `s_1(u)` is survival of the killed two-state chain

$$
K=\begin{pmatrix}-a&a\\1&-(1+B)\end{pmatrix}
$$

started from one.

Define

$$
w(u)=e^{-\omega u}s_1(u)
$$

and

$$
\boxed{
Z=\int_0^\infty w(u)\,du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a}.
}
$$

Since

$$
g|h_{p_*}(0)|=c,\qquad g|h_{p_*}(1)|=g,
$$

a direct sup-norm argument gives exponential trail-depth decay whenever

$$
\boxed{\max\{c,g\}Z<1.}
$$

**Status:** new proved parameter subregion, conditional on the trail decomposition. It excludes the hard near-East regime.

## E4. Meeting 005 one-step target is false

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

let

$$
m_\varepsilon=-\frac{\varepsilon}{1+\varepsilon},
$$

and

$$
M_{2,\varepsilon}
=\frac{(1+\varepsilon)(2\varepsilon-1)}{2\varepsilon^2+5\varepsilon+1}.
$$

The exact two-level invariant scalar is

$$
\boxed{
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}(M_{2,\varepsilon}-m_\varepsilon^2).
}
$$

It changes sign from negative at short time to positive at long time. The absolute-value ratios satisfy

$$
\boxed{
\frac{g}{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du
\to\frac32,
}
$$

and, even with right killing,

$$
\boxed{
\frac{g}{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du
\to\frac75.
}
$$

**Status:** exact obstruction. The one-generation centered-transfer contraction `(T)` adopted at Meeting 005 is closed. Pointwise regional positivity and simple one-step `L^1` iteration are also closed near East.

## E5. Correct right-weighted invariant criterion

Finite left-region mixing after the final trail time and E3 reduce the nonempty-exit term to

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_{k=1}^n w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
}
$$

The trail representation gives

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le C_A\sum_{x\in A}J_{x,r}.
$$

Thus

$$
\boxed{J_{x,r}\to0\quad(n=r-x+1\to\infty)}
$$

is sufficient for the nonempty-exit term.

At exact East the invariant expectation itself is zero by the final centered birth factor under Bernoulli product equilibrium. This remains structural evidence, not a strict-positive-rate proof.

## E6. Exact mass/disagreement channel decomposition

Let `mu` be a probability measure, `r=mu(eta_y=1)`, `bar mu` its left marginal, and `mu^1,mu^0` its conditional left laws. Then

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).}
$$

Each centered insertion therefore creates:

1. a signed **mass channel**, coefficient `Br-c`;
2. a positive **disagreement channel**, coefficient `Br(1-r)`.

For zero-boundary equilibrium,

$$
Br_0-c=\frac{b(1-c)-a}{1+b},
$$

and

$$
Br_0(1-r_0)=\frac{Bb}{(1+b)^2}.
$$

Near East, the mass channel is order `epsilon^2`, the disagreement channel order `epsilon`. Moreover

$$
\boxed{|Br_0-c|Z\to\frac25.}
$$

Thus every genuine regeneration of the disagreement structure creates a strict scalar loss in the mass channel.

**Status:** active structural identity explaining both the depth-two expansion and the possibility of later contraction.

## E7. Negative drift of unresolved disagreement-stack height

For the reset coupling attached to E6, let `K` be the number of consecutive unresolved levels removed during an independent zero-boundary segment. The principal construction gives

$$
\mathbb P(K\ge1)\ge\frac{B+\omega}{B+2\omega},
$$

and for `j>=1`,

$$
\mathbb P(K\ge j)
\ge
\frac{B+\omega}{B+2\omega}2^{-(j-1)}.
$$

Hence

$$
\boxed{
\mathbb EK\ge\frac{2(B+\omega)}{B+2\omega}>1.
}
$$

If `H` is unresolved stack height and one transfer adds at most one level,

$$
H'\le(H-K)_+ +1,
$$

so for large height

$$
\boxed{
\mathbb E(H'-H)
\le-\frac{B}{B+2\omega}<0.
}
$$

Therefore the unweighted stack has an exponential Lyapunov function and geometrically returns to bounded height.

**Status:** structural bridge to Student F's coupling work. It does not by itself control signed mass branching.

## E8. Current load-bearing edge: block mass/disagreement contraction

Meeting 005's one-step norm is false. The remaining plausible theorem is a **block** contraction on the trail-generated mass/disagreement decomposition.

Find a norm on decompositions into signed mass components and coupled disagreement pairs, weighted by unresolved stack height, and finite constants

$$
m_0=m_0(a,b,c),\qquad \theta<1,
$$

such that the complete right-weighted transfer satisfies

$$
\boxed{
\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*
}
$$

for every trail-generated signed measure.

The unresolved issue is branching under E6: repeated transfers produce both `bar mu` mass components and conditional-law differences `mu^1-mu^0`. Replacing the latter by unrestricted total variation destroys the structure and reproduces the exact `3/2` / `7/5` expansion.

A successful block theorem must imply `J_{x,r}->0` and then be inserted into the full trail convergence proof, including the no-exit term.

Student F Assignment 006 is superseded by `students/student-f/assignment-007.md`. Student G remains on Assignment 002.

## Anti-circularity checkpoint

The principal update refutes the exact one-step target adopted at Meeting 005 and replaces it by a materially different all-depth mechanism: regeneration-weighted block contraction of a branching mass/disagreement stack. Do not rescue `(T)` by renaming the norm or enumerate fixed depths as a substitute for the block theorem.

## Current direction

Attack E8 while preserving the fixed positive-rates target.
