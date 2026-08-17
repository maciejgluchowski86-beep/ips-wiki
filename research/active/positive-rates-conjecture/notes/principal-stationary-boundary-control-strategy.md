# Principal stationary boundary-control strategy

Date: 2026-08-17

Provenance: this note records the load-bearing content of a separate principal ChatGPT exploration supplied verbatim to the Professor after Meeting 022. The original request was to propose a proof strategy after the earlier target-hierarchy calculation. Numerical values below are research evidence only until independently reproduced. The finite-dimensional occupation-measure facts in Sections 2--3 are independently checked by the Professor in Meeting 023.

## 1. Proposed architecture

The proposed route is a **stationary boundary-control hierarchy**. It does not use the centered predecessor-trail composition, common-uniform global coalescence, or path-space contraction of the trajectory kernel `Q`.

For clarity, the principal's displayed flip rates use the complemented spin

$$
\xi_i=1-\eta_i,
$$

so that `1` is the East facilitator. Put

$$
g=b-a,\qquad k=1-c.
$$

Then the residual flip rates are

$$
0\to1\text{ at rate }a+g\xi_{i+1},
\qquad
1\to0\text{ at rate }k+c\xi_{i+1}.
$$

Equivalently, in the programme's usual `eta` convention one has neighbour-independent reset-to-one marks of rate `k`, reset-to-zero marks of rate `a`, and when the right neighbour is zero an additional rate-`B=b+c-a` Bernoulli-`c/B` refresh.

For a block of `N` sites and a fixed right-boundary control `u in {0,1}`, let

$$
L_N^u
$$

be the corresponding finite-volume generator.

## 2. Stationary occupation polytope

Define

$$
\boxed{
\mathcal K_N
=
\left\{
 m(x,u)\ge0:
 \sum_{x,u}m(x,u)=1,
 \quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0
 \ \forall F:\{0,1\}^N\to\mathbb R
\right\}.
}
\tag{K}
$$

For a local observable `h` on the left part of the block, define its stationary boundary-control diameter

$$
\boxed{
D_N(h)
=
\sup_{m\in\mathcal K_N}m(h)
-
\inf_{m\in\mathcal K_N}m(h).
}
\tag{D}
$$

Every invariant law `mu` of the infinite IPS yields a feasible occupation measure

$$
m_\mu(x,u)
=
\mu\bigl((\xi_0,\ldots,\xi_{N-1})=x,\ \xi_N=u\bigr),
$$

because stationarity of every function depending only on the first `N` sites gives exactly the constraints `(K)`.

Conversely, every `m in K_N` is the stationary occupation measure of a finite controlled chain with a randomized state-dependent right-boundary policy. If

$$
\bar m(x)=\sum_u m(x,u),
$$

define on states with `bar m(x)>0`

$$
\pi(u\mid x)=\frac{m(x,u)}{\bar m(x)}.
$$

Then `bar m` is stationary for the averaged generator

$$
L_N^\pi F(x)=\sum_u\pi(u\mid x)L_N^uF(x).
$$

Thus `K_N` is an exact finite-dimensional adversarial relaxation of all stationary boundary behavior.

The hierarchy is nested: if `m in K_{N+1}`, project it to the first `N` sites and take the old `N`th spin as the new control. The resulting measure lies in `K_N`. Hence

$$
D_{N+1}(h)\le D_N(h)
$$

for any fixed local `h` contained in the left part of the block.

The proposed static target is

$$
\boxed{D_N(h)\longrightarrow0\quad\text{for every local }h.}
\tag{S}
$$

Since every infinite-volume invariant law projects into `K_N`, `(S)` implies uniqueness of the invariant measure.

## 3. Exact LP dual

Finite-dimensional linear-programming duality gives

$$
U_N(h)
=
\inf_F\max_{x,u}
\bigl(h(x)-L_N^uF(x)\bigr),
$$

$$
\ell_N(h)
=
\sup_F\min_{x,u}
\bigl(h(x)-L_N^uF(x)\bigr),
$$

with

$$
\boxed{D_N(h)=U_N(h)-\ell_N(h).}
\tag{LP}
$$

(The sign of `F` is immaterial.) Thus static screening can be certified by upper and lower Poisson/Bellman correctors which are valid **simultaneously for both boundary controls at every block state**.

## 4. Principal finite-box evidence

The principal reports the following uncontrolled-by-translation-invariance LP widths for `h(x)=x_0`:

| `(a,b,c)` | `D_5(h)` | `D_9(h)` |
|---|---:|---:|
| `(10^-4,10^-2,0.9999)` | `0.16055` | `0.01185` |
| `(0.002,0.1,0.9999)` | `0.28486` | `0.02100` |
| `(0.001,0.1,0.9999)` | `0.40101` | `0.04863` |

Two-site event diameters reportedly shrink similarly. At the hard-East boundary the corresponding relaxation does not shrink at the tested depths; very small softness produces a delayed crossover.

These are numerical observations, not yet Professor-verified certificates.

## 5. Proposed multiscale theorem

The load-bearing proposed estimate is a dyadic stationary screening inequality

$$
\boxed{
D_{2N}(h)
\le
(1-\rho)D_N(h)+Ce^{-\gamma N},
\qquad N\ge N_*(a,b,c),
}
\tag{R}
$$

with parameter-dependent constants `rho,gamma>0`. Iteration over `N,2N,4N,...` would prove `(S)`.

The intended mechanism is:

1. a neighbour-independent reset creates a fresh facilitator inside a large block;
2. behind such a facilitator, hard-East dynamics relax a macroscopic subblock before the far-right boundary can retain information;
3. repeated seeds produce a positive screening probability;
4. failed propagation and finite-speed effects are exponentially small.

The principal pointed to the East-model relaxation results in the attached KCM book. The Professor checked the cited statements:

- Theorem 7.6 gives exponential convergence of local observables for the hard East model once an empty/facilitating site is present in the oriented future of the observable;
- Theorem 7.8 gives linear finite-volume mixing time for East with completely empty boundary, and also with ergodic boundary conditions.

These theorems support the **hard-East ingredient** but do not themselves prove `(R)` for the noisy chain with an arbitrary state-dependent boundary controller. A robustness/concatenation step is still required.

## 6. Proposed dynamic upgrade

Static collapse gives uniqueness but not convergence from every initial state. The principal proposes a later uniform distributional screening quantity `S_N(h)` measuring the maximal influence on `P_t h` of discrepancies farther than distance `N`, uniformly in `t`, and a bound of the schematic form

$$
S_N(h)
\le
C_h\bigl(D_{\lfloor N/2\rfloor}(h)+e^{-\gamma N}\bigr).
\tag{ZF}
$$

If `(ZF)` and `(S)` hold, splice two arbitrary initial configurations at distance `N`. The far-right discrepancy is controlled by `S_N(h)`, while the finite remaining discrepancy disappears locally by the already established finite-seed common-coupling theorem. Taking first `t->infinity` and then `N->infinity` gives convergence from every initial law.

This dynamic step is **not active yet**. The immediate issue is whether the static LP correctors admit a repeatable multiscale concatenation proving `(R)` or a genuine substitute.

## 7. Immediate decision problem

The first concrete task suggested by the principal is:

> extract exact/rational finite-box dual correctors and determine whether their structure concatenates into a theorem of the form `(R)`.

A larger finite-box LP calculation with no repeatability theorem does not establish the route. The load-bearing question is whether there is a block composition valid uniformly over the adversarial state-dependent boundary control.
