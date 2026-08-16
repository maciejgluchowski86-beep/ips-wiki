# Student F assignment 009: mode-resolved L1 block operator

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/009-regenerated-mass-loss-and-duration-mode-obstruction.md`;
- your `008-bounded-signed-kernel.md` and verifier;
- Student G `assignment-004.md` and, when it lands, G's return on the global Foster phase;
- Meetings 006--008 and the principal trail notes.

The scientific target remains the positive rates conjecture for simple IPS.

Student G is still in flight. Do not wait for it before doing the part of this assignment that is independent of the exact Foster phase.

## What is now accepted

Use

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
$$

and

$$
w(u)=e^{-\omega u}s_1(u),
\qquad
Z=\int_0^\infty w(u)du.
$$

Your new uniform regenerated-mass estimate is Professor-checked:

$$
\boxed{
\left|\frac{B}{1+b}-c\right|Z<\frac23
}
\tag{RM}
$$

throughout the strict residual chamber.

Also accepted is the structural norm-order warning. Near East,

$$
\frac g{|m_\varepsilon|}
\left|\int w(u)A_{2,\varepsilon}(u)du\right|
\to\frac35,
$$

while

$$
\frac g{|m_\varepsilon|}
\int w(u)|A_{2,\varepsilon}(u)|du
\to\frac75.
$$

Therefore the finite block proof may use signed cancellation at a fixed duration profile, but it may **not** integrate a duration variable and only then take the norm if the true `J_{x,r}` norm places the absolute value first.

Your exact `K^(1)` is a local diagnostic only. Do not iterate it as an ordinary matrix.

## Objective

Build the correct **mode-resolved block transfer at the `L^1(w)` level**.

The desired state should retain enough zero-boundary relaxation/reset-history information that the signed mass coefficient and conditional-law disagreement channel close under one transfer, while duration variables remain visible until the block norm is applied.

A successful structural result can be one of the following.

1. A finite-dimensional mode closure theorem at every fixed bounded disagreement/restart height `H`: trail-generated mass/disagreement profiles lie in an explicitly described finite mode space `E_H`, invariant under the zero-boundary semigroups and insertion/branching maps.
2. A vector-valued `L^1(w)` transfer operator on those modes and a parameter-dependent block norm with contraction `<1`, conditional only on G's eventual finite Foster return phase.
3. A regeneration/renewal theorem in which the equilibrium mass type loses by `(RM)` and every transient mass mode either decays into that type or is charged to a disagreement/reset phase with a controlled block cost.
4. An exact obstruction showing that the required mode dimension grows without bound even after disagreement/restart height is bounded, so the proposed finite-kernel route cannot close.

Do **not** count a finite-depth matrix calculation unless it proves or refutes one of these structural statements.

## First mandatory calculation: isolate the mass transient as a type

For a mass branch whose current rightmost density is `r`, zero-boundary evolution gives

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u},
\qquad
r_0=\frac1{1+b}.
$$

Hence

$$
Br(u)-c
=(Br_0-c)+B(r-r_0)e^{-(1+b)u}.
$$

Treat the constant equilibrium mass mode and the centered transient mode as distinct signed types rather than integrating them together.

Determine the exact right-weighted transfer costs of these two types in the norm that is actually compatible with

$$
\int w(u)|\cdot|du.
$$

The equilibrium type has the strict loss `(RM)`. Determine whether the transient type can be made subordinate to regeneration/disagreement over a finite block, or whether it creates a genuine obstruction.

## Finite-generator route

For any explicit finite return phase `Sigma` with zero-boundary generator `Q_Sigma`, you may use the exact resolvent identity from your report,

$$
\mathcal R_w(Q)
=\int_0^\infty w(u)e^{uQ}du
=
\frac{
\rho_+[(\omega+\rho_-)I-Q]^{-1}
-\rho_-[(\omega+\rho_+)I-Q]^{-1}
}{\rho_+-\rho_-}.
$$

But distinguish carefully between:

- this resolvent as a tool for coefficients with fixed sign/type; and
- an invalid operation which sums opposite-sign duration profiles before the `L^1` norm.

If useful, formulate the block operator as a matrix of signed profile functions or finite measures rather than a scalar matrix.

## Interface with G

G is trying to prove a finite global restart/Foster phase state. When its report becomes available, check whether that phase state determines:

1. the signed mass component on return;
2. the conditional-law disagreement component;
3. the mass relaxation/reset-history mode;
4. which duration coordinates remain unintegrated.

If yes, instantiate your mode-resolved operator on that phase state. If no, identify the minimal extra coordinate needed. Do not silently strengthen G's theorem.

## Stress tests

Your construction must survive both:

- the near-East path `a=epsilon^2,b=epsilon,c=1-epsilon^2`, where one-step `L^1` expands by `7/5` but the equilibrium mass type loses;
- the strict rational point `(1/10,3/10,4/5)`, where first- and second-order static spatial Markov closure are already refuted.

A contraction constant may depend on the parameter point and may tend to one at East.

## What not to do

Do not:

- average a duration before the norm and use the fictitious `3/5` factor;
- iterate `K^(1)` as if it were the true block kernel;
- replace the invariant law by a first- or second-order static Markov approximation;
- replace `mu^1-mu^0` by unrestricted total variation;
- assume `(RM)` applies before the mass transient has been separated;
- compute only another finite static word or finite ancestry depth.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/009-mode-resolved-l1-block.md`

with exact code/certificates beside it if useful.

End with one of:

- `mode-resolved L1 block contraction proved conditional on G phase: ...`;
- `finite mode closure proved; remaining spectral inequality: ...`;
- `regeneration/transient decomposition closes J: ...`;
- `finite mode route obstructed because: ...`;
- `unresolved after substantive work; exact mode blocker: ...`.
