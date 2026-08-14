---
title: L1 random-patch conjecture for the quadratic Hessian PDE
status: conjecture
tags:
  - PDE
  - branching process
  - patch
  - integrability
  - conjecture
  - Hessian
  - Gaussian analysis
---

# L1 random-patch conjecture for the quadratic Hessian PDE

The quadratic-Hessian programme now has a proved integrable endpoint and a proved negative theorem on the most direct raw-marked endpoint.

- [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) integrates all continuous variables inside a decorated skeleton before the skeleton is sampled. Under an explicit small-data condition, it gives an unbiased \(L^1\) skeleton-only estimator.
- The [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) shows that one cannot keep the canonical raw signed marked integrand as the conditional barycenter of an estimator and still obtain \(L^1\), even after arbitrary proposal changes and even for one fixed arbitrarily small \(C^\infty\) datum.

These two results do **not** close the literal conjecture on this page. The reason is a scope distinction that is now part of the statement: an estimator may continue to use continuous interior marks randomly while changing the conditional barycenter of the canonical raw marked state. Antithetic couplings, bridge/Rao--Blackwell averaging that leaves some randomness, control variates across raw states, and coupled multi-sample constructions are examples of mechanisms that are not covered by the raw-barycenter theorem.

Accordingly, the honest remaining question is no longer whether the canonical raw integrand can simply be importance-sampled into \(L^1\). It cannot. The open question is whether one can **redistribute signed mass across raw marked states while retaining nontrivial continuous interior randomness** and thereby construct an integrable exact representation.

The [PDE branching-representations overview](../pde-branching-representations.md) gives the section-level map.

## Concrete PDE and proved small-data regime

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\lambda\in\mathbb R,
\qquad
\phi\in C^{2+\alpha}(\mathbb T),
\qquad
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

For the forward equation

$$
\partial_tv
=
\frac12v_{xx}
+\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

write \(z=v_{xx}\). Then

$$
z(t)
=
P_t\phi''
+\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{1}
$$

Put

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M
=
\|P_\cdot\phi''\|_{X_{\alpha,T}},
$$

and let \(C_{\mathcal D}(\alpha,T)\) be the constant in the [parabolic Hölder bound for the Hessian Duhamel operator](parabolic-holder-bound-for-hessian-duhamel-operator.md). Assume

$$
4|\lambda|C_{\mathcal D}(\alpha,T)M<1.
\tag{2}
$$

Under (2), Theorem C-prime constructs the unique small fixed point \(z_*\in X_{\alpha,T}\) in its Catalan fixed-point ball and an unbiased skeleton-only \(L^1\) estimator of \(z_*\).

## Conjecture C: literal surviving formulation

Under the hypotheses above, does there exist a patch-first randomization of the Hessian Duhamel expansion with the following properties?

1. Maximal consecutive left-spine Hessian events are organized into complete multi-event patches.
2. Conditional on an exposed patch skeleton, different descendant patches may use auxiliary randomness with appropriate [importance-sampling compensators](importance-sampling-compensators.md).
3. Nontrivial continuous Gaussian/Hermite, branch-time, or descendant randomness remains inside the sampled patches rather than **all** such variables being deterministically integrated out.
4. The resulting infinite-depth random functional \(H_{\mathrm{patch}}(t,x)\) belongs to \(L^1\) for every \((t,x)\in[0,T]\times\mathbb T\).
5. Its expectation is the C-prime solution,
   $$
   \mathbb E[H_{\mathrm{patch}}(t,x)]
   =
   z_*(t,x).
   \tag{3}
   $$

The conjecture deliberately does **not** require the canonical raw signed marked integrand to remain the conditional mean after all of its raw marks have been exposed. Adding that requirement produces the stronger statement below, which is false.

## A stronger formulation is false: raw-barycenter C

For one centered Hessian edge, the canonical raw transfer is

$$
\widehat K_rF(x,Z)
=
\frac{He_2(Z)}r
\left[
F(x+\sqrt rZ)-F(x)
\right].
\tag{4}
$$

At finite depth, the canonical genealogy, durations, Gaussian/Hermite marks, and terminal Brownian marks define an intrinsic signed marked measure after the positive proposal factors and their reciprocal compensators are cancelled.

A candidate estimator is *raw-barycenter-retaining* if, after those canonical raw variables are exposed, any further proposal change or auxiliary randomization has the canonical raw signed contribution as its conditional barycenter. In measure-theoretic form, on a raw comb cylinder \(\Gamma_m\), if \(Q_m\) is the chosen positive proposal and \(\nu_m\) is the intrinsic signed raw comb measure, this means

$$
\mathbb E_Q[Y\mid\text{raw marks}]
=
\frac{d\nu_m}{dQ_m}.
\tag{5}
$$

The [raw-barycenter obstruction theorem](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) constructs one fixed \(C^\infty\) datum, arbitrarily small in every fixed Hölder norm relevant to (2), for which every estimator satisfying (5) has

$$
\mathbb E|Y|=\infty.
\tag{6}
$$

The result is proposal invariant. The lifetime law, genealogy probabilities, Gaussian importance-sampling law, dependence among proposal variables, and auxiliary conditionally unbiased randomness may all be changed. Conditional Jensen reduces every such proposal to the total variation of the same intrinsic signed comb measure.

Thus the following strengthening of C is **false**:

> Keep the canonical raw marked state and require its raw signed contribution to remain the conditional barycenter of the estimator, while allowing arbitrary importance sampling and auxiliary conditionally unbiased randomization.

This is the mathematically precise version of “retain the raw integrand and only change how it is sampled.”

## Why the literal conjecture survives

Random dependence on the marks is weaker than raw-barycenter retention. A natural example already appears at one Hessian edge. Define

$$
\widetilde K_rF(x,Z)
=
\frac{He_2(Z)}{2r}
\left[
F(x+\sqrt rZ)
+F(x-\sqrt rZ)
-2F(x)
\right].
\tag{7}
$$

The Gaussian mark \(Z\) is still sampled and used. Since \(Z\) and \(-Z\) have the same law and \(He_2\) is even,

$$
\mathbb E\widetilde K_rF
=
\partial_x^2P_rF.
\tag{8}
$$

But, conditional on the sampled value of \(Z\), (7) is not the raw transfer (4). The signed contribution has been redistributed between the raw states \(Z\) and \(-Z\). Hence this antithetic construction is outside the raw-barycenter class while satisfying the ordinary-language statement that the Gaussian mark remains random.

The same distinction covers several other possible escape mechanisms:

- bridge or Rao--Blackwell averaging of some, but not all, interior Gaussian coordinates;
- antithetic or ghost couplings across several marked trajectories;
- control variates whose mean is zero only after averaging over different raw states;
- coupled multi-sample or multi-genealogy estimators;
- a representation whose natural random coordinates are coarser than the canonical raw marked coordinates.

No theorem on this wiki currently proves that any of these mechanisms gives a full infinite-depth \(L^1\) representation for the quadratic Hessian equation.

## The four routes and what each settled

The route history is useful because each failure isolates a different piece of structure.

### Route 1: fixed pathwise Hölder or same-regularity Besov norms

For the raw edge (4), the expected sup norm gains the usual Hölder power of the edge length, but the pathwise same-regularity Hölder seminorm has the short-edge scale \(r^{-1}\). A high-frequency packet at frequency \(r^{-1/2}\) makes this sharp. A fixed same-regularity Besov norm has the same translation obstruction.

**What it rules out:** a fixed pathwise regularity norm propagated edge by edge.

### Route 2: a decreasing Banach scale

If an edge spends a Hölder increment \(\delta\), the sharp time-integrated first-moment cost is \(1/\delta\). For losses \(\delta_1,\ldots,\delta_n\) with

$$
\sum_{k=1}^n\delta_k\le\Delta,
$$

the [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md) forces

$$
c^n\prod_{k=1}^n\delta_k^{-1}
\ge
c^n\left(\frac n\Delta\right)^n.
\tag{9}
$$

The equal allocation is optimal; nonuniform allocations are worse. The theorem applies to **stepwise first-moment Banach-scale arguments**, not to every frequency-aware smoothing scheme.

**What it rules out:** repairing route 1 merely by budgeting a bounded total loss of derivatives.

### Route 3: condition all patch interiors

If every continuous variable inside a decorated skeleton is integrated out first, deterministic Hermite/Hölder cancellation is strong enough to close. Theorem C-prime gives an absolutely convergent Catalan skeleton series under (2) and hence an unbiased \(L^1\) estimator.

**What it proves:** integrability after complete interior averaging.

**What it gives up:** continuous interior randomness.

### Route 4: joint centered marks

The [joint centered-mark theorem](joint-centered-mark-dichotomy-for-raw-pde-patches.md) delays the first absolute value across several centered Gaussian marks. Two marks give a genuine non-stepwise gain, so this route really escapes the hypothesis of route 2. At length \(m\), however, the uniform retained-mark block norm has the sharp scale

$$
c^m m!
\le
\mathfrak R_m
\le
C^m m!.
\tag{10}
$$

Signedly averaging the internal Gaussian bridge coordinates collapses the bare derivative chain to one \(He_{2m}\) endpoint weight and restores geometric growth; with spatial multipliers, the commutator/cluster expansion gives the corresponding deterministic geometric estimate.

**What it shows:** postponing the absolute value across a block removes the derivative-loss ladder, but full canonical mark retention has factorial total variation; signed averaging repairs that growth only by changing the raw marked object.

### Fixed-datum closure of the raw-barycenter route

The earlier sharp lower bounds used a frequency depending on \(n\) or \(m\), so they were proof-architecture barriers rather than fixed-datum nonintegrability results. The raw-barycenter theorem closes exactly this gap.

It chooses exponentially separated frequencies \(N_m=K^m\) and coefficients

$$
b_m=(m!)^{-1/2}
$$

inside one smooth terminal Hessian datum. Each length-\(m\) comb then sees its own frequency \(N_m\). The comb total variation contains \(m\) logarithmic Hessian factors and obeys a lower bound of the form

$$
\|\nu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}},
\tag{11}
$$

which is not summable. This turns the retained-block barrier into a genuine no-\(L^1\) theorem for one fixed datum, but only for the raw-barycenter class.

## What is now settled and what remains open

Three statements should be kept separate.

**Settled positive theorem.** Complete interior averaging gives the C-prime \(L^1\) representation under (2).

**Settled negative theorem.** Retaining the canonical raw signed integrand as the conditional barycenter is impossible in \(L^1\), even after arbitrary proposal changes, for one fixed arbitrarily small smooth datum.

**Open intermediate regime.** It is unknown whether an estimator can retain nontrivial continuous interior randomness while changing the raw barycenter through signed coupling, partial averaging, antithetic pairing, or another nonlocal reorganization of the marked states.

The negative theorem therefore proves that **some departure from raw-barycenter retention is necessary**. It does not prove that all continuous marks must be averaged out. In particular, it does not prove that C-prime is minimal or optimal among every conceivable escape mechanism. C-prime is the fully averaged endpoint for which a complete \(L^1\) theorem is currently proved.
