# Group meeting 009: regenerated mass contracts uniformly; bounded kernel must retain duration modes

Date: 2026-08-16

Professor review of:

- Student F, commit `ac7de96`, `students/student-f/008-bounded-signed-kernel.md`;
- Student F exact verifier commit `ff3c5d5`, `students/student-f/008-bounded-signed-kernel-verifier.py`;
- Meeting 008 and the current split between Student F's bounded signed kernel and Student G's still-in-flight Foster lift.

Student G remains in flight on `students/student-g/assignment-004.md`. This meeting does not wait for or interrupt that block.

state_narrowed: yes

Evidence pointer: `students/student-f/008-bounded-signed-kernel.md`, especially Sections 2--8, and `students/student-f/008-bounded-signed-kernel-verifier.py`.

## Previous bottleneck

Meeting 008 reduced the trail route to two conditional pieces:

1. a global restart-corrector Foster lift reducing arbitrary disagreement/restart height to a finite return set;
2. a bounded-height signed mass/disagreement kernel whose block norm must contract.

F was authorized to assume only the scalar Foster return statement `(FL)`, not an explicit signed return law.

F's return shows that this scalar premise is not enough to define the bounded signed kernel. The missing bounded state contains a mass-relaxation / reset-history mode, and the order in which duration integration and absolute value are taken is load-bearing.

## Professor verification: uniform regenerated mass loss

Write

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
\qquad k=1-c,
$$

and

$$
Z=\int_0^\infty e^{-\omega u}s_1(u)\,du
=\frac{a+b+2}{a(2b+3)+k(b+2)}.
$$

For the one-site zero-boundary equilibrium,

$$
r_0=\frac1{1+b},
$$

so the equilibrium mass coefficient from the exact mass/disagreement decomposition is

$$
Br_0-c=\frac{bk-a}{1+b}.
$$

F proves

$$
\boxed{
|Br_0-c|Z<\frac23
}
$$

at every strict residual parameter point.

I checked the two sign cases.

If `a>=bk`, then

$$
|Br_0-c|Z
<\frac{a+b+2}{(1+b)(2b+3)}<\frac23,
$$

because

$$
2(1+b)(2b+3)-3(a+b+2)
=4b^2+7b-3a
>4b^2+4b>0.
$$

If `a<bk`, then

$$
|Br_0-c|Z
<\frac{b(a+b+2)}{(1+b)(b+2)}<\frac23,
$$

using `a<b<1`, since at the worst endpoint `a=b`,

$$
2(1+b)(b+2)-3b(2b+2)
=4(1+b)(1-b)>0.
$$

Thus every mass component which has genuinely returned to the one-site zero-boundary equilibrium mode carries a strict right-weighted loss bounded by `2/3`. This is independent of `(FL)` and upgrades the earlier near-East limit `2/5` to the entire residual chamber.

## Mass relaxation is an additional state variable

The preceding estimate cannot be applied to every mass branch immediately. The rightmost density of a mass branch after dropping a site need not equal `r_0`; under the one-site zero-boundary semigroup it has the exact form

$$
r_M(u)=r_0+(r_M(0)-r_0)e^{-(1+b)u}.
$$

F computes this explicitly from the two-site invariant law and shows that the transient coefficient is nonzero generically. On the near-East path, the centered transient mass mode remains order one while the equilibrium centered mode tends to zero.

Therefore a bounded return state consisting only of mass sign, disagreement height, and current exposure spin does not determine the next signed mass coefficient. A mass/reset-history or equivalent relaxation-mode coordinate is required.

## Professor verification: `3/5` versus `7/5` is a structural norm-order obstruction

Along

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

let `A_{2,epsilon}(u)` be the exact depth-two invariant scalar already audited at Meetings 006--008. F records two different operations.

If one integrates the signed duration profile first and then takes absolute value,

$$
\frac g{|m_\varepsilon|}
\left|
\int_0^\infty w(u)A_{2,\varepsilon}(u)\,du
\right|
\longrightarrow\frac35<1.
$$

But the actual right-weighted criterion contains the absolute value before duration integration:

$$
\frac g{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du
\longrightarrow\frac75>1.
$$

This is not a sharpness issue. It fixes the admissible proof architecture. Cancellation among signed spin/mass/disagreement components at a fixed duration profile is usable; cancellation between different duration values cannot be manufactured by integrating the duration before the block norm.

Any finite matrix obtained by first integrating each segment duration can therefore show false contraction. A correct block theorem must retain the duration/reset mode until the relevant `L^1(w)` norm is taken.

## Height-one signed kernel: useful diagnostic, not an iterable proof kernel

F constructs an exact fully-regenerated height-one signed phase matrix

$$
K^{(1)}
=
\begin{pmatrix}
-cI_0(0)&-cI_0(1)\\
 gI_1(0)&gI_1(1)
\end{pmatrix}.
$$

At `(a,b,c)=(1/10,3/10,4/5)` the verifier gives

$$
K^{(1)}
=\frac1{333207}
\begin{pmatrix}
-184712&-595480\\
47695&147353
\end{pmatrix},
$$

with spectral radius about `0.10325`. Along the near-East path,

$$
\operatorname{tr}K^{(1)}\to-\frac25,
\qquad
\det K^{(1)}\to\frac25,
$$

so

$$
\rho(K^{(1)})\to\sqrt{\frac25}<1.
$$

I accept these calculations only as evidence that signed phase cancellation is substantial. `K^(1)` is not the bounded block kernel, because iterating it has already integrated the duration coordinate too early.

## Static short-word closure is false

At the same strict residual point, F computes exact nonzero conditional-independence determinants under the zero-boundary invariant laws:

$$
\pi(000)\pi(101)-\pi(001)\pi(100)
=\frac{6715}{52606827}\ne0,
$$

and, at four sites,

$$
\pi(0000)\pi(1001)-\pi(0001)\pi(1000)
=-\frac{1097085304370}{627742107775979469}\ne0.
$$

Thus the invariant spatial law is neither first- nor second-order Markov at this point. This rules out closure by the current spin or a two-spin static context. It does **not** rule out a finite temporal reset-history / generator-mode state.

## Relation to G's in-flight Foster lift

G's Assignment 004 is still useful and is not interrupted. However, even a correct scalar Foster inequality

$$
E[V(\Sigma')\mid\Sigma]\le\theta_F V(\Sigma)
$$

outside a finite set will not by itself settle the signed kernel. To interface with the trail criterion, the finite return state must either encode, or allow F to reconstruct, the mass relaxation/reset-history mode and which duration variables remain unintegrated.

When G returns, its proposed finite phase state will be tested against this new requirement. If it only controls disagreement/restart height while forgetting the signed return mode, that will be a coupling-side reduction but not yet the complete finite-state interface.

## Ruling

The block route remains live and the state has narrowed.

- A genuinely regenerated mass channel has a uniform residual contraction `<2/3`.
- The bounded-kernel difficulty is not raw scalar size; it is closure of the signed mass/reset mode at the correct `L^1` norm level.
- The exact `3/5` versus `7/5` calculation forbids premature duration integration.
- Short static spin words do not provide exact closure.
- The next bounded-kernel target is therefore a **mode-resolved `L^1(w)` block operator**, preferably built from reset-history / finite-generator modes and anchored by the `<2/3` regenerated-mass loss.

Student F is routed to this mode-resolved operator while G completes the global Foster phase construction.
