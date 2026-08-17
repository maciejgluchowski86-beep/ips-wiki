# Student G assignment 010: prove the connected dual-renewal tail bound

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/026-dual-renewal-connected-tail-reopens-one-bounded-j-spec-block.md`;
- your `009b-dual-renewal-checkpoint.md`;
- your `009a-canonical-j-recursion-checkpoint.md` and final `009-j-norm-growth-route-decision.md`;
- current `state.md` and `proof-spine.md`;
- F009 only for the growing-mode obstruction;
- F013/F014 only to keep the new connected problem distinct from the stopped zero-frequency tail-shift interface.

This assignment exists because the late 009b checkpoint contains genuinely new post-stop input. It is one bounded block. Do not broaden it into another general search over predecessor-profile architectures.

## 1. Fixed data

Work at

$$
P_*=(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
$$

with the **fixed** admissible filter

$$
\boxed{
\sigma(u)=1-2e^{-\tau u},
\qquad \tau=\frac4{125}.
}
$$

Do not optimize `sigma` in this block.

Let

$$
H_N^\sigma=\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma=\int_0^\infty w(u)\sigma(u)\,du,
$$

$$
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N,
$$

and

$$
c_1=m_0,
$$

$$
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2.
$$

Set

$$
a_k=z_\sigma c_k^\sigma,
\qquad
\lambda_k=(-1)^ka_k.
$$

The exact renewal recurrence is

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1,
$$

and the fixed-filter witness lower-bounds the canonical `J` norm.

## 2. First mandatory checkpoint: bank the missing exact verifier

Your 009b report refers to a verifier which was not committed before the Meeting-025/026 overlap.

Before relying on the finite margin, commit an exact verifier that reconstructs from the finite generators and rational resolvent formula:

- `z_sigma=114559900/205809`;
- exact rational `lambda_1,...,lambda_7`;
- their sign pattern;
- the exact strict inequalities
  $$
  \sum_{k=1}^3\lambda_k>1,
  \qquad
  \sum_{k=1}^7\lambda_k>1;
  $$
- the exact value
  $$
  \delta_7:=\sum_{k=1}^7\lambda_k-1>0.
  $$

Commit this immediately as a durability checkpoint. If it disagrees with 009b, stop and report the discrepancy before doing further analysis.

## 3. Primary objective

Prove the all-depth connected-tail estimate

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7.
}
\tag{T}
$$

This proves

$$
\rho_J(P_*)>1
$$

through the exact renewal generating function and the `L^1` witness.

A different rigorous bound for the **same fixed filter and exact recurrence** is also acceptable if it directly implies

$$
\limsup_n|V_n|^{1/n}>1.
$$

## 4. What kind of theorem can prove `(T)`

The load-bearing operator is

$$
\mathcal K_N^\sigma=Q_N^\sigma J_N.
$$

Unlike the stopped long-reset argument, each `Q_N^sigma` has the exact invariant projection removed:

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

So do **not** approximate a long segment by equilibrium and then ask for tail-shift agreement. The separator/invariant contribution has already been extracted exactly into the scalar renewal.

You may seek, for example:

1. a depth-uniform seminorm `||.||_*` on the actual connected orbit such that insertion followed by `Q_N^sigma` contracts after a bounded number of steps;
2. an exact resolvent/Poisson identity showing geometric decay of `c_k^sigma` without finite-dimensional closure;
3. a cluster or finite-propagation expansion in which connected length `k` forces a quantitatively rare chain of non-equilibrium transmission events;
4. a two- or multi-step bound
   $$
   |c_{k+m}^\sigma|\le q|c_k^\sigma|
   $$
   or a vector analogue with `q<1`, valid uniformly in depth;
5. another rigorous tail estimate strong enough to beat the explicit margin `delta_7`.

A finite prefix plus a theorem for the remaining tail is allowed. The theorem, not the prefix size, must carry the all-depth conclusion.

## 5. Important caveat: projection removal is not automatic contraction

Do not argue merely that `Q_N^sigma Pi_N=0` and therefore the connected tail decays.

On a centered nonzero spectral mode, `Q_N^sigma` acts through the corresponding resolvent multiplier. Slow nonzero modes may still matter. You need a theorem controlling the **actual connected orbit** created by alternating `J_N` and `Q_N^sigma`, uniformly in `N`.

This is exactly the feasibility question of the block.

## 6. Existing obstructions that remain in force

Do not posit a fixed finite-dimensional mode closure: F009 proves the exact cyclic mode dimension grows with depth.

Do not seek an exact finite-cylinder reproduction eigenprofile for an invertible factorized resolvent: your G009 Proposition 6.1 already rules that out.

Do not return to:

- bare one-/two-step tail-shift;
- common-uniform occupation;
- larger raw `J_n` numerics;
- generic matrix-product/HJB searches;
- filter optimization;
- the stationary Bellman route;
- `(ML)/(JT)/(MR)` as separate targets.

## 7. What finite computation is allowed

Exact computation may be used to discover the correct norm or estimate and to bank a finite prefix.

It is not a positive outcome to report `lambda_8,...,lambda_K` as tiny for a larger `K` without an all-depth theorem after `K`.

If the natural tail theorem starts only after some finite `K>8`, certify the finite contribution `sum_{8<=k<K}|lambda_k|` exactly and prove a rigorous bound for `sum_{k>=K}|lambda_k|` which together beats `delta_7`.

## 8. Negative outcome

A substantive negative result should identify a structural obstruction to `(T)` or to the connected positive-frequency mechanism. Examples:

- a proved family of slow connected modes preventing any depth-uniform geometric estimate of the required strength;
- an exact reduction showing that control of the connected tail is actually equivalent to one of the already stopped zero-frequency spatial-memory quantities;
- a rigorous lower bound on the connected tail incompatible with `(T)`;
- another theorem showing the fixed-filter renewal witness cannot be made supercritical.

It is not enough to say that the mode space grows or that no simple norm was found; those facts are already known.

## 9. Stopping rule

End with exactly one of:

- `J-SPEC refuted absolute-duration route: connected renewal proves rho_J >= ... > 1 at P*`;
- `fixed dual-renewal filter fails: ...` with a rigorous obstruction or contrary tail theorem;
- `unresolved after substantive work; connected-tail blocker: ...` where the blocker is sharper than F009's growing mode hierarchy and sharper than the old tail-shift problem.

If the third outcome contains only more finite coefficients or a generic request for a better norm, the connected-renewal continuation stops and the programme returns to Meeting 025's `no-credible-route` state.

## 10. Durability

Because this student lineage has repeatedly suffered session freezes, commit nontrivial intermediate theorems/certificates as soon as they are stable. In particular the missing exact verifier is the first checkpoint, not something to defer until the final report.
