# Student G Assignment 011 handoff

## Status

`STOP-EQUIVALENT`

Assignment 011 is complete under its pre-registered stop rule. I did not enter marker-existence Part D, enlarge marker states, reopen Assignment 010, or start a generic coupling/norm search.

Main report:

- `students/student-g/011-distinguished-zero-transfer.md`, commit `07b8fcef1d3c6af458567b8fefe555e76abbf295`.

No `docs/` or `mkdocs.yml` files were edited.

## Decisive result

The finite zero-boundary invariant family does **not** provide the equilibrium-consistency direction needed by an East marker.

If a marker move is determined from marker/right-side information and leaves the old protected `N`-site block untouched, then exact post-move law `pi_{N+1}` forces

$$
\bar\pi_{N+1}=\pi_N.
$$

At the hard point

$$
P_h=(1/10000,1/100,9999/10000),
$$

this fails already at `N=1 -> 2`:

$$
\pi_1(1)=\frac12,
\qquad
\bar\pi_2(1)=\frac{5251}{30302},
$$

and

$$
\bar\pi_2(1)-\pi_1(1)=-\frac{4950}{15151}.
$$

Symbolically,

$$
\bar\pi_2(1)-\pi_1(1)
=
-\frac{2a[a-b(1-c)]}
{(a+1-c)[2ab-ac+3a-bc+b+c^2-3c+2]}.
$$

Thus exact prefix compatibility holds in the residual positive-rate setting only on

$$
a=b(1-c).
$$

That is exactly the product/reversible surface: with `rho=b/(1+b)`, the zero-boundary invariant law is `Ber(rho)^{otimes N}` for every `N`, so prefix consistency is restored at all depths there.

## Why the repair is equivalent to stopped tail shift

If a marker move leaves the old block untouched but discards its last `m` sites as a contaminated buffer, the sharp protected-prefix discrepancy is exactly

$$
S_m=\Delta_{m+1}.
$$

Hence a buffered screen with vanishing error is precisely the old theorem `Delta_M->0` (up to whether the new marker site is counted in the buffer width).

More generally, let a width-`m` release kernel resample the old boundary layer using arbitrary fresh right-side randomness while leaving the protected prefix untouched. Exact output `pi_{N+1}` necessarily preserves the old prefix marginal, so a uniform release theorem requires

$$
\Delta_{m+1}=0.
$$

Approximate release has error bounded below by the same prefix discrepancy. Thus growing-width approximate release again needs `Delta_M->0` upstream.

This is enough to trigger Assignment 011's stop condition. A finite-time single-observable boundary response can be weaker than full `Delta_M`, but the existing one-segment theorem already reduces that response to `Delta` plus finite propagation; turning it into an all-depth moving-screen induction would require a new dynamical boundary-error contraction. The distinguished-zero bookkeeping did not produce such a new object, and the concrete existing versions are among the stopped common-coupling / signed boundary-transmission routes.

## Durable commits

- exact symbolic/rational verifier — `7d46627b2a44aa1c4966b0ecd39c81bdeba43cbc`;
- exact one-move compatibility obstruction — `06e1dda041347ab797015da68fe660f2c1e291cb`;
- product-surface interpretation — `09649056037221b4317854daa6e0b2d4494f6293`;
- buffered-screen equals `Delta` — `645590a18c928d59fedce9f508ebcacb70cf6c37`;
- fixed release-kernel obstruction — `79c12a7c7065453506585e8af97899f0fdb3c584`;
- final report — `07b8fcef1d3c6af458567b8fefe555e76abbf295`.

The exact SymPy algebra used in the verifier was independently rerun during the assignment; the symbolic factorization and hard-point fractions agree with the committed assertions.

## Professor-facing interpretation

The useful obstruction is directional. Right-suffix projectivity of `pi_N` is real, but the East argument needs consistency in the opposite direction, the direction in which the marker releases new sites. Off the product surface, the failure of that prefix consistency is precisely the previously isolated boundary/tail-shift defect once one allows a buffer.

Therefore the principal's proposed use of `pi_N` does not clear the stopped positive-rates restart bar in this form. The bounded test succeeded by identifying the exact equivalence rather than by producing a new bridge.
