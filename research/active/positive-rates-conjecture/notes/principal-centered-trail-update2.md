# Principal centered-trail update 2

Date: 2026-08-16

Source: rendered-text capture supplied by the principal from their separate centered-monomial-duality exploration. Subscripts/superscripts in the capture were mangled by rendering; formulas below have been normalized to the current residual notation. This note records research input, not an independently audited final theorem.

This note supersedes the **one-generation contraction target (T)** from `notes/principal-centered-trail-reduction.md`. It does not supersede the canonical predecessor-trail decomposition itself.

## Residual notation

On the normalized residual family write

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The previous trail formula and left/right factorization remain the starting point.

## 1. Segmentwise right-region survival

During a right-region segment of length `u`, the trail refresh resets the relevant boundary spin to one. The boundary spin is killed at rate `B` while it is zero. A dominating killed two-state chain has generator

$$
K=\begin{pmatrix}-a&a\\1&-(1+B)\end{pmatrix}
$$

and, started from one, survival

$$
s_1(u)=\frac{\rho_+e^{-\rho_-u}-\rho_-e^{-\rho_+u}}{\rho_+-\rho_-},
$$

where

$$
\rho_\pm=\frac{a+1+B\pm\sqrt{(a+1+B)^2-4aB}}2.
$$

Hence the right-region factor has the depth-sensitive product bound

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_{k=1}^n s_1(u_k).
\tag{16}
$$

Set

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z:=\int_0^\infty w(u)\,du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a}.
\tag{17}
$$

A direct sup-norm bound gives decay whenever

$$
\max\{c,g\}Z<1.
\tag{18}
$$

This proves a genuine residual subregion but excludes the difficult near-East regime.

## 2. Exact depth-two obstruction to one-step contraction

On the residual near-East path

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

one has

$$
p_* = \frac{1+\varepsilon}{1+2\varepsilon},\qquad
q_* = \frac{\varepsilon}{1+2\varepsilon},\qquad
g=\varepsilon(1-\varepsilon),\qquad
\omega=2\varepsilon^2.
$$

For the one-site and two-site zero-boundary invariant laws,

$$
m_\varepsilon:=\pi_1^0(h_{p_*})=-\frac{\varepsilon}{1+\varepsilon},
$$

and

$$
M_{2,\varepsilon}:=\pi_2^0(h_{p_*}(\eta_1)h_{p_*}(\eta_2))
=\frac{(1+\varepsilon)(2\varepsilon-1)}{2\varepsilon^2+5\varepsilon+1}.
$$

Since the one-site zero-boundary chain relaxes at rate `1+epsilon`, the depth-two invariant integrand is

$$
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}(M_{2,\varepsilon}-m_\varepsilon^2).
\tag{19}
$$

It changes sign: `A_{2,epsilon}(0)` tends to `-1`, while the long-time limit is the positive number `m_epsilon^2`.

The exact Laplace-`L^1` ratios satisfy

$$
\frac{g}{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du
\longrightarrow \frac32,
\tag{20}
$$

and, even after the segmentwise right survival factor,

$$
\frac{g}{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du
\longrightarrow \frac75.
\tag{21}
$$

Thus the following are false near East:

- pointwise regional positivity;
- the left-only one-step `L^1` contraction proposed as (T) at Meeting 005;
- a one-step contraction obtained merely by multiplying by the segmentwise right survival factor.

This is an exact depth-two obstruction, not a loose estimate.

## 3. Corrected sufficient quantity

With the stronger right weight, the quantity to control is

$$
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_{k=1}^n w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
\tag{22}
$$

The trail reduction gives

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le C_A\sum_{x\in A}J_{x,r}.
\tag{23}
$$

Hence `J_{x,r}->0` as the trail depth grows is sufficient for the nonempty-exit term.

The capture reports exact finite-volume diagnostics at `epsilon=0.01`: after normalizing depth one to one, depths `1,...,8` are approximately

$$
1,\ 1.32,\ 1.02,\ 0.97,\ 0.83,\ 0.72,\ 0.66,\ 0.58.
$$

These are numerical evidence only: they show initial expansion followed by decay.

## 4. Exact mass/disagreement decomposition

Let `mu` be a probability law whose rightmost spin has density

$$
r=\mu(\eta_y=1),
$$

let `\bar\mu` be its left marginal, and let `\mu^1,\mu^0` be its conditional left laws given `eta_y=1,0`. Then

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\,\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).
\tag{24}
$$

Thus each centered insertion splits into

1. a signed **mass channel**, coefficient `Br-c`;
2. a positive **disagreement channel**, coefficient `Br(1-r)`.

Under zero-boundary evolution,

$$
r(u)=\frac1{1+b}
+\left(r(0)-\frac1{1+b}\right)e^{-(1+b)u}.
\tag{25}
$$

At equilibrium,

$$
Br_0-c=\frac{b(1-c)-a}{1+b},
$$

and

$$
Br_0(1-r_0)=\frac{Bb}{(1+b)^2}.
\tag{26}
$$

Near East the mass channel is order `epsilon^2`, while the disagreement channel is order `epsilon`. The right-weighted equilibrium mass multiplier satisfies

$$
|Br_0-c|Z\longrightarrow \frac25.
\tag{27}
$$

So genuine regeneration of the disagreement structure produces a strict loss in the mass channel.

## 5. Disagreement-stack drift

Use the reset coupling described in the capture. Neighbour-independent common resets occur at total rate `omega`; when the right neighbour is zero there is an additional interaction reset at rate `B`.

During an independent interval `U~Exp(omega)`, let `K` be the number of consecutive unresolved sites coupled from the right. The stated coupling gives

$$
\mathbb P(K\ge1)\ge\frac{B+\omega}{B+2\omega},
$$

and for `j>=1`,

$$
\mathbb P(K\ge j)
\ge
\frac{B+\omega}{B+2\omega}\,2^{-(j-1)}.
\tag{28}
$$

Therefore

$$
\mathbb EK\ge
\frac{2(B+\omega)}{B+2\omega}>1.
\tag{29}
$$

If `H` is unresolved stack height, one trail step obeys

$$
H'\le(H-K)_+ +1,
$$

so for large `H`,

$$
\mathbb E(H'-H)
\le -\frac{B}{B+2\omega}<0.
\tag{30}
$$

Thus the unweighted stack admits an exponential Lyapunov function and returns geometrically to bounded height.

This connects directly to Student F's live-coupling work: the centered transfer creates a disagreement channel, while the coupling supplies a mechanism for unresolved disagreement depth to retreat.

## 6. Revised remaining lemma

The one-step norm contraction from Meeting 005 is false. The plausible surviving theorem is a **block contraction** on mass/disagreement decompositions.

Seek a norm on decompositions into mass components and coupled disagreement pairs, weighted by unresolved stack height, and constants

$$
m_0<\infty,\qquad \theta<1,
$$

such that the complete right-weighted transfer satisfies

$$
\boxed{
\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*.
}
\tag{31}
$$

for every signed measure generated from the zero-boundary invariant laws by the predecessor-trail transfer.

The unresolved issue is to control the branching into `\bar\mu` and `\mu^1-\mu^0` under repeated applications of (24) without replacing the disagreement channel by unrestricted total variation, which reproduces the exact depth-two expansion factor `3/2` (or `7/5` with right killing).

The active research target is therefore **block contraction of the mass/disagreement stack**, not one-cell centered-transfer contraction.