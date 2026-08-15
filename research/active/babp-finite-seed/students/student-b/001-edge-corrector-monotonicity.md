# Addendum: exact nesting of the BABP edge-corrector LPs

This sharpens Section 10 of `001-threshold-and-dfp.md`: monotonicity of the finite-window hierarchy is not open.

For fixed `lambda>0`, define

```text
v_k(lambda)
 = sup_phi min_{u in {0,1}^k, z in {0,1}}
     D_{k,lambda}(u,z;phi),
```

with `D_{k,lambda}` as in `001-threshold-and-dfp.md` and the additive gauge on `phi` fixed arbitrarily.

## Lemma

For every `k>=1` and every `lambda>0`,

```text
v_{k+1}(lambda) >= v_k(lambda).
```

Consequently, for any threshold convention

```text
lambda_k = inf{lambda>0 : v_k(lambda)>0},
```

we have

```text
lambda_{k+1} <= lambda_k.
```

## Proof

Let

```text
phi_k : {0,1}^k -> R
```

be any corrector. Define its extension by ignoring the new last bit:

```text
phi_{k+1}(u_1,...,u_k,u_{k+1})
 = phi_k(u_1,...,u_k).
```

Fix an extended edge word

```text
u=(u_1,...,u_k,u_{k+1})
```

and the new exterior bit `z`.

Every term in the `(k+1)`-window generator which can change `phi_{k+1}` is exactly a term in the `k`-window generator for the truncated word

```text
u'=(u_1,...,u_k)
```

with old exterior bit equal to `u_{k+1}`:

1. The outward birth sends the first `k` coordinates to

   ```text
   (1,u_1,...,u_{k-1}),
   ```

   exactly as in the `k`-window formula.

2. If `u_1=1`, death of the rightmost particle sends the first `k` coordinates to

   ```text
   (u_2,...,u_k,u_{k+1}),
   ```

   which is `T_-^{u_{k+1}} u'`.

3. For flips at sites `j=1,...,k-1`, both the rate and the change of the corrector are unchanged.

4. For the flip at `j=k`, the extra neighbour is `u_{k+1}`. This is exactly the exterior bit used by the `k`-window drift.

5. A flip at the new site `j=k+1` changes neither the first `k` coordinates nor `phi_{k+1}`, so its contribution to the corrector drift is zero. Its rate may depend on the new exterior bit `z`, but that is irrelevant.

Therefore, identically for every extended state,

```text
D_{k+1,lambda}(
    (u_1,...,u_k,u_{k+1}), z; phi_{k+1}
)
=
D_{k,lambda}(
    (u_1,...,u_k), u_{k+1}; phi_k
).
```

Taking the minimum over the `(k+1)`-window states gives at least the minimum of the `k`-window drift. Taking the supremum over `phi_k` proves the claim.

## Consequences

- The numerical decrease

  ```text
  1/3, 0.265239..., ..., 0.0346195..., 0.0278105..., 0.0227326...
  ```

  is structurally consistent rather than accidental.

- The exact `k=10`, `lambda=1/40` certificate in `edge-corrector-certificate.py` automatically gives a positive-drift corrector for every larger window `k>=10` by this extension.

- The remaining analytic question is now clean: determine

  ```text
  lambda_infinity = lim_{k->infinity} lambda_k
  ```

  and prove `lambda_infinity=0`.

This is the natural main technical target if the Sudbury/Mountford convergence bridge is confirmed to require only positive two-sided edge speed beyond the already available stationary-law inputs.
