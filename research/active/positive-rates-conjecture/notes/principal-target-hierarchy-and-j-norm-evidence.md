# Principal target-hierarchy study: finite-box evidence for the absolute-duration `J` route

Date recorded: 2026-08-17

Provenance: the principal supplied a verbatim capture of a separate ChatGPT calculation made after asking what the next target statement should be, before attempting another proof. The capture timestamp is `2026-08-16T23:15:31.615Z`. This note normalizes the target hierarchy and numerical evidence into the workspace.

**Status:** research evidence only. The Professor has not independently reproduced the finite-box computations in this note, and no asymptotic conclusion below is treated as proved merely because it is numerically well separated at depths up to ten.

## 1. Why this evidence matters

The current predecessor-trail reduction uses an absolute value at fixed duration vector before integrating those durations. The principal's calculation tested that exact `J`-compatible duration norm on singleton trails and found finite-depth growth at strict residual parameter points, while signed duration-resolvent pairings at the same points are much smaller.

This raises a logically prior question:

> Is the absolute-duration `J` criterion itself true throughout the residual chamber?

Until this is decided, proving increasingly elaborate contraction statements for that norm has low expected value.

## 2. Canonical normalization

Let `J_n` denote the singleton depth-`n` specialization of the canonical predecessor-trail absolute-duration quantity in `proof-spine.md` / `principal-centered-trail-reduction.md`. The principal capture uses a normalized quantity `N_n` satisfying

$$
J_n=\frac{g}{B}N_n,
\qquad
B=b+c-a,
\qquad
g=b-a.
$$

The factor `g/B` is independent of depth, so

$$
\limsup_{n\to\infty}J_n^{1/n}
=
\limsup_{n\to\infty}N_n^{1/n}.
$$

The capture's intermediate profile notation was partially mangled by rendering. Future rigorous work must therefore reconstruct `N_n` from the canonical `J_n` definition rather than trust the rendered intermediate symbol names.

Define the route-growth exponent

$$
\boxed{
\rho_J(a,b,c)
:=
\limsup_{n\to\infty}N_n^{1/n}
=
\limsup_{n\to\infty}J_n^{1/n}.
}
$$

The principal proposes the immediate route-decision target

$$
\boxed{
\text{either prove }\rho_J<1\text{ throughout the residual chamber,
 or prove }\rho_J>1\text{ at one strict residual point.}
}
\tag{J-SPEC}
$$

A proof of the second alternative would refute the present absolute-duration `J->0` strategy at that point. It would not refute the positive-rates conjecture or the exact predecessor-trail identity.

## 3. Finite-box numerical evidence

The principal calculation used exact `2^n`-state zero-boundary generators through depth ten, invariant laws from the finite generators, spectral semigroup evaluation, and importance sampling of duration integrals. It reports deterministic composite Gaussian quadrature checks through depth four and Krylov checks of depth-ten profile semigroups.

The four tested strict residual points were:

| name | `a` | `b` | `1-c` | reported `rho_{7,10}` |
|---|---:|---:|---:|---:|
| near-East | `10^-4` | `10^-2` | `10^-4` | `0.882` |
| borderline | `0.003` | `0.1` | `0.0003` | `0.987` |
| rational growth point | `0.002` | `0.1` | `0.0001` | `1.070` |
| strong-growth point | `0.001` | `0.1` | `0.0001` | `1.153` |

Here the capture defines

$$
\rho_{7,10}=\left(\frac{N_{10}}{N_7}\right)^{1/3}.
$$

The reported depth-ten Monte Carlo standard errors, in the same order, were

$$
0.00115,\quad0.00205,\quad0.00411,\quad0.01794.
$$

For three points the capture also reports

| point | `N_10` |
|---|---:|
| near-East | `0.1740` |
| rational growth point | `1.2969` |
| strong-growth point | `2.3975` |

At the two growing points, the finite zero-boundary temporal spectral gap was reported as already approximately stabilized by depth five:

$$
\operatorname{gap}\approx0.00677
$$

at `(a,b,1-c)=(0.002,0.1,0.0001)`, and

$$
\operatorname{gap}\approx0.00389
$$

at `(0.001,0.1,0.0001)`.

Small positive block-renewal diagnostics were reported as

$$
\lambda_1^{(2)}+\lambda_2^{(2)}\approx1.1385
$$

at the rational growth point and

$$
\lambda_1^{(2)}+\lambda_2^{(2)}\approx1.2929
$$

at the strong-growth point. These are diagnostics only; no asymptotic lower theorem was supplied.

## 4. Signed duration-resolvent evidence

The principal then retained cancellation between duration sectors and considered a signed multivariate Laplace/resolvent pairing `L_n(lambda)` obtained by inserting independent factors `exp(-lambda_j u_j)` before integrating the duration variables.

The weight `w` is a difference of two exponentials, so the one-segment weighted resolvent has the exact form

$$
W_k(\lambda)
=
A(\omega+\rho_-+\lambda-L_k)^{-1}
-D(\omega+\rho_++\lambda-L_k)^{-1},
$$

with the constants inherited from the accepted right-killed chain decomposition.

At zero Laplace shift the reported depth-ten comparison is

| point | `N_10` | `|L_10(0)|` |
|---|---:|---:|
| near-East | `0.1740` | `0.00941` |
| rational growth point | `1.2969` | `0.000893` |
| strong-growth point | `2.3975` | `0.00325` |

Thus at the strong-growth point the signed integral is reported to cancel more than `99.8%` of the absolute-duration mass.

The principal also sampled independent nonnegative real Laplace shifts and complex shifts with nonnegative real parts. The largest sampled real values through depth ten were:

| depth | near-East | rational growth | strong growth |
|---|---:|---:|---:|
| `6` | `0.0549` | `0.0579` | `0.0463` |
| `8` | `0.0260` | `0.0200` | `0.0178` |
| `10` | `0.0102` | `0.0064` | `0.0083` |

These are sampled suprema, not certified upper bounds.

The capture reports a structured alternating-sign pattern when duration vectors are binned by the number of short gaps. That is consistent with cancellation between equilibrium and transient relaxation modes, but it is not yet a theorem.

## 5. Principal-proposed hierarchy after `(J-SPEC)`

The principal proposes three later targets. They are recorded here as hypotheses for future route selection, not as active assignments.

### Scalar resolvent proxy `(ML)`

Let `M_n` be the supremum of `|L_n(lambda)|` over admissible independent Laplace shifts. A candidate theorem is

$$
M_n\le C\theta^n,
\qquad\theta<1.
\tag{ML}
$$

The finite evidence suggests a two-step contraction may be more natural than one-step contraction. However `(ML)` is only a proxy until it is linked to the exact right-region contribution in the predecessor-trail identity.

### Actual sufficient target `(JT)`

Let `R_{n,u}(eta)` denote the exact final-coin-averaged right-region contribution for a depth-`n` trail at duration vector `u`. The proof needs decay of the full signed duration integral in which `R_{n,u}` remains inside the integral. The present `J` reduction replaces `R_{n,u}` by a uniform absolute survival bound; the principal's data suggest that this replacement may destroy decisive cancellation.

The next formal object, if the absolute `J` route is refuted, should therefore be the exact duration-dependent class

$$
\mathcal R_n
=\{u\mapsto R_{n,u}(eta):eta\},
$$

with its recursion made explicit.

### Matrix-resolvent target `(MR)`

If the exact right-region recursion closes into a finite family of sub-Markov segment operators `K(u)`, the natural all-depth statement is a matrix-resolvent estimate that keeps the left signed profile and right-region operators inside the same duration integral and proves exponential decay only after that integration.

The scalar `(ML)` problem is then the one-dimensional proxy. It should not be promoted to a proof target before the exact right-region class is shown to admit such a representation.

## 6. Professor-use rule

The present numerical evidence is strong enough to change **what should be tested next**, but not strong enough to settle `(J-SPEC)`.

Do not respond by merely computing `N_n` at larger depths. A rigorous route-decision block must produce an asymptotic mechanism: for example a positive/block lower certificate implying `rho_J>1`, or a theorem implying `rho_J<1` on a genuine parameter region.

If `rho_J>1` is proved at one strict residual point, the current absolute-duration `J` criterion is not a viable global sufficient target. Future work must retain additional signed duration/right-region cancellation rather than dominate it away.
