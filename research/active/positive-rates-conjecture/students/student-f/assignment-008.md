# Student F assignment 008: bounded-height signed mass/disagreement kernel

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/008-restart-tail-and-empty-supnorm-region.md`;
- your `007-block-mass-disagreement-contraction.md` and verifier;
- Student G `003-restart-count-block-bridge.md`;
- Meetings 006--007 and the two principal trail notes.

The scientific target remains the positive rates conjecture for simple IPS.

## Correction now entered into the spine

Your Phase-A endpoint proof is accepted:

$$
\boxed{cZ>1\text{ throughout the residual chamber}.}
$$

Thus the crude condition `max{c,g}Z<1` gives no residual subregion. Do not spend more time on that scalar criterion.

Student G has independently proved a same-parent restart tail

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1}
$$

and an explicit restart pgf. Its full global Foster/product-corrector lift is **not yet Professor-verified**; G is assigned to make that step rigorous. You may use the following as an explicitly conditional premise:

> `(FL)`: arbitrary-depth disagreement/restart excursions outside a finite stack-height/phase set are returned with a strict multiplicative factor, so the remaining block problem is the signed transfer on a finite bounded-height phase set.

Your task is to solve that finite signed problem, or show that even under `(FL)` it cannot contract.

## Objective

Construct the exact or dominating **bounded-height signed mass/disagreement transfer kernel** associated with

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f),
$$

including the right weight

$$
w(u)=e^{-\omega u}s_1(u).
$$

You need a finite type description on stack heights/phases up to a finite cutoff `H_0`, with signed mass types and disagreement types distinguished. Determine whether some finite block has spectral radius `<1` in a norm compatible with the mass signs.

A successful result should look like one of:

1. an explicit finite matrix/kernel `K_{H_0}` and a proof that `rho(K_{H_0})<1` throughout the residual chamber, with parameter-dependent `H_0` allowed;
2. a finite family of inequalities giving a weighted norm and `m_0<infinity`, `theta<1` for the bounded kernel;
3. a renewal calculation showing that each return from the disagreement sector to the mass sector loses enough signed mass to dominate the finite branching;
4. an exact residual parameter/state obstruction showing the bounded signed kernel has spectral radius `>=1` for every natural finite summary compatible with `(MD)`.

## Near-East test

Near East, the crude scalar factor is expansive (`cZ>1`) while the equilibrium mass multiplier tends to `2/5`. The finite signed kernel must therefore use cancellation/regeneration; an absolute-value matrix that simply reproduces `cZ` is not the target.

Student G's algebraic large-height stress factor tends to `16/21`, but this is **not** itself a multiplier for the global trail quantity `J_{x,r}`. Your finite kernel must supply the missing signed factor.

## Required interface to `J_{x,r}`

If you prove bounded-kernel contraction conditional on `(FL)`, state explicitly how the two estimates combine to give

$$
J_{x,r}\to0.
$$

Do not yet claim full ergodicity unless the predecessor-trail factorization and no-exit term are also audited.

## What not to do

Do not:

- return to `max{c,g}Z<1`;
- rescue one-step `(T)`;
- replace `mu^1-mu^0` by unrestricted total variation;
- compute a few scalar depths without extracting a finite kernel or spectral statement;
- assume G's full Foster lift is proved rather than naming it as conditional;
- treat `16/21` as the signed block multiplier.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/008-bounded-signed-kernel.md`

with exact code/certificates if useful.

End with one of:

- `bounded signed kernel contracts conditional on FL: ...`;
- `finite block spectral radius proved <1: ...`;
- `bounded signed kernel obstructed because: ...`;
- `unresolved after substantive work; exact finite-kernel blocker: ...`.
