# Student G 011c: finite regenerative release kernels cannot bypass tail shift

## Result

Allowing a distinguished marker move to resample a fixed-width boundary layer does not repair the invariant-family mismatch unless one assumes a finite tail-shift identity that is at least as strong as the stopped `Delta_M` theorem.

Fix a width `m>=0`. Split the old `N`-site screened block as

$$
(U,V)
\in
\{0,1\}^{N-m}\times\{0,1\}^{m},
$$

where `U` is the protected left prefix and `V` is the boundary layer that may be discarded or resampled. Let `K` be an arbitrary Markov kernel which, using `V` and any fresh marker/right-side randomness, outputs a new boundary layer `W` of whatever finite size is needed after the marker move. The kernel is not allowed to inspect or modify `U`.

Starting from `pi_N`, the output law has the form

$$
\nu(du,dw)
=
\sum_v \pi_N(du,dv)K(v,dw).
\tag{1}
$$

If the desired exact post-move law is `pi_{N+1}`, then necessarily

$$
\boxed{
\pi_N|_U=\pi_{N+1}|_U.
}
\tag{2}
$$

If such an exact width-`m` release works for every `N>m`, then

$$
\boxed{\Delta_{m+1}=0.}
\tag{3}
$$

Thus no fixed-width exact release state can evade prefix/tail-shift compatibility. In fact `(3)` is only necessary: even when the untouched-prefix marginals agree, an `U`-blind kernel still has to reproduce the correct target conditional distribution of the new layer given `U`.

For approximate release, the same obstruction is quantitative. Since the output law `(1)` has `U`-marginal exactly `pi_N|_U`,

$$
\|\nu-\pi_{N+1}\|_{\sigma(U)}
=
\|\pi_N-\pi_{N+1}\|_{\sigma(U)}.
\tag{4}
$$

Consequently any uniform width-`m` release error is bounded below by `Delta_{m+1}` in the same variation normalization. A sequence of growing buffers with error tending to zero therefore requires `Delta_M->0` upstream.

## Proof

Marginalize `(1)` over `w`. Since `K(v,\cdot)` has total mass one,

$$
\nu_U(du)
=
\sum_v\pi_N(du,dv)
=
(\pi_N)_U(du).
$$

If `nu=pi_{N+1}`, this proves `(2)`.

For `U={1,...,N-m}`, `(2)` says that `bar pi_{N+1}` and `pi_N` agree on every bounded function supported in `{1,...,N-m}`. Taking the supremum over `N` and using the indexing identity in `011b-buffered-screen-equivalence.md` gives `(3)`.

Equation `(4)` follows for the same reason: restriction to `sigma(U)` is unaffected by any kernel acting only on the complementary boundary layer.

## Stronger conditional factorization gate

Prefix equality is not sufficient for a local release kernel. If regular conditional laws are written as

$$
\pi_N(dv\mid U=u),
\qquad
\pi_{N+1}(dw\mid U=u),
$$

then exact release requires one `U`-blind kernel `K` satisfying

$$
\boxed{
\pi_{N+1}(dw\mid U=u)
=
\sum_v \pi_N(dv\mid U=u)K(v,dw)
}
\tag{5}
$$

for every protected-prefix state `u` of positive probability.

Thus a finite release state has two gates:

1. the untouched-prefix law must already be correct;
2. all dependence of the target new boundary layer on the protected prefix must factor through the old finite boundary layer `V`.

The first gate alone is enough to trigger Assignment 011's pre-registered stop condition.

## Exact hard-point checks

The verifier `011a-distinguished-zero-one-move-verifier.py` checks the most generous small-depth versions of the untouched-prefix gate at

$$
P_h=(1/10000,1/100,9999/10000).
$$

- **Append only:** `N=1 -> 2`, no old site is resampled. The untouched one-site marginal changes by
  $$
  -\frac{4950}{15151}\ne0.
  $$
- **One-site boundary-layer release:** `N=2 -> 3`, allow the old rightmost site and all new release randomness to be replaced while protecting only the leftmost site. The protected first-site marginal changes by
  $$
  -\frac{7466519657025}{108705150384068}\ne0.
  $$
- **Two-site boundary-layer release:** `N=3 -> 4`, allow the two old rightmost sites to be replaced while protecting only the leftmost site. The protected first-site marginal again changes, now by
  $$
  \frac{76953453677050193761435735134480075}
  {763517320575043491796008444141593548}\ne0.
  $$

These are not intended as a search over release kernels. They simply verify at the first three depths that even a maximally generous finite boundary resampling cannot change the untouched prefix to the required `pi_{N+1}` prefix.

## Why state-independent reset representations do not help

The one-site zero-boundary dynamics admits reset representations, so one can certainly generate fresh randomness at the released coordinate or within a finite boundary layer. But freshness only controls the **conditional kernel on coordinates being resampled**. It cannot alter the law of the untouched protected prefix. Therefore state-independent reset marks do not address gate `(2)`.

One could instead wait long enough for the protected prefix itself to evolve after the move. That is no longer an exact release kernel. Quantitatively controlling whether the boundary defect then disappears before reaching a remote observable is precisely a dynamical boundary-response/screening problem. The existing uniform measure-level formulation is `Delta_M`; the stopped dynamical alternatives are the common-uniform all-depth route or, on the connected-renewal architecture, the signed boundary-transmission operator `(V)`.

## Stop-rule consequence

C2 supplies no new object `S`. Every fixed-width exact release requires the stronger identity `Delta_{m+1}=0`; every approximate/growing-width release requires `Delta_M->0` if its error is to vanish. Assignment 011 therefore forbids enlarging the release state further.
