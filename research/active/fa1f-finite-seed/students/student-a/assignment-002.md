# Graduate Student A assignment 002: unnormalized hard-FA patch skeleton

Work on branch `research/fa1f-finite-seed`.

Read first:

- `research/active/fa1f-finite-seed/state.md`;
- `research/active/fa1f-finite-seed/proof-spine.md`;
- `research/active/fa1f-finite-seed/meetings/001-h-transform-review.md`;
- your `001-centered-h-transform.md`;
- the canonical patch paper `paper/`, especially Theorem 4.4 and its Mecke/Radon--Nikodym proof, the proof of Theorem A, Appendix B, Section 6, Section 7.1, and Section 8.2.

The `h`-transform E1 is now retained as a verified identity but is no longer the main proof strategy. Your present task is proof-spine edge E2: determine whether the *unnormalized* successful-skeleton expansion contains useful hard-model geometry that the normalized patch representation hides.

This is a decisive test, not an instruction to make the patch route work.

## 1. Derive the unnormalized expansion exactly

Starting from the actual proof of Theorem 4.4, define

$$
\widehat C(P)
=
\mathbf E_P\!\left[F(P)\mathbf 1_{\operatorname{Con}(P)}\right]
=
\mathbf P_P(\operatorname{Con}(P))C(P),
$$

and for an end patch

$$
\widehat C(z,P)
=
\mathbf E_P\!\left[F(z,P)\mathbf 1_{\operatorname{Con}(P)}\right].
$$

Write an exact finite-horizon representation in which the reference successful-skeleton measure `m_t(dg)` from the Mecke proof is explicit and the product contains `widehat C` rather than normalized `C`.

Do not assume that every consistency probability can simply be multiplied patchwise without checking the source-record type probabilities and the skeleton intensity factors. I want the exact Radon--Nikodym bookkeeping.

## 2. Specialize every local factor to one-dimensional hard FA-1f

Use the canonical paper's convention `p=1-q`, target `N(i)={i-1,i+1}`. Derive from first principles the signed-dual rates, signs, `alpha`, `V`, `phi`, `psi`, every consistency probability, and the unnormalized amplitudes for all realized boundary types.

Produce a compact table covering at least:

- `II`, `IO`, `OI`, `OO` full patches;
- `IE`, `OE` end patches;
- the affine constant and centered slope of every end amplitude;
- the combined record intensity `delta(N)+beta(N)` that belongs to `m_t`.

A Professor-side heuristic suggested factors of order `e^{-Delta}` after consistency probabilities are restored. Check that rather than inheriting it.

## 3. Work in the actual target deviation, not a chain surrogate

For the singleton observable, use equilibrium invariance to write

$$
D_t
:=
P_t\eta(0)(\eta^0)-p
=
P_t\chi_{\{0\}}^*(\eta^0).
$$

Derive an exact unnormalized-skeleton formula for `D_t` by subtracting the Bernoulli(`p`) product initial law inside the patch expansion. Since end-patch sites are distinct, the equilibrium end factors should be expressible by evaluating at terminal density `p`; verify the exact formula.

Then compute explicitly the complete contribution to `D_t` from:

1. skeletons with no ordinary successful record before `t`;
2. skeletons with exactly one ordinary successful record;
3. skeletons with exactly two ordinary successful records.

For items 2 and 3, include the **full patch family created by each record**. A successful FA-1f record has the two-neighbour target; a calculation along only one backward ancestry chain is not the quantity we need. Sum over all admissible source choices and record kinds through the unnormalized patch weights/skeleton measure. You may use a short symbolic or exact-enumeration script if that is cleaner, but the mathematical object being summed must be written explicitly.

The two-record calculation is the first composition test. Reduce it to a transparent closed form or a small integral/operator expression whose sign and long-time scale can actually be read.

## 4. Decide whether the apparent chain criticality is real or misleading

The Professor's pre-meeting heuristic was that an outgoing-chain factor may become a unit-mass exponential renewal kernel after multiplying consistency probability by record intensity. That calculation ignores the other patches born at the same records.

After the full one- and two-record calculations, answer precisely:

- Is there a genuine decay factor in the full target deviation that is absent from the normalized representation?
- Is the first composition subcritical, critical, or supercritical in the quantity that actually contributes to `D_t`?
- Does the gain, if any, come from consistency probability, spatial overlap/coalescence, terminal centering, or something else?
- Does the full calculation algebraically resum to the verified `h`-transform process from assignment 001? If yes, identify the map explicitly and explain whether the patch route has added any usable structure.
- Does any attempted gain reduce to the closed two-sibling algebra `a=-p/q`, `(p+qa)^2=0` followed by absolute-value majorization? If yes, mark that subroute closed immediately.

Do not infer the behavior of arbitrarily many records from the first two unless you have an actual operator/renewal identity supporting it.

## 5. What would justify continuing

A useful outcome is any one of the following:

- an exact positive/contractive transfer object for the *full* skeleton, in the centered target quantity, whose first composition has genuine margin;
- a critical transfer object with an identified one-dimensional geometric mechanism (overlap, recurrence, coalescence) that is absent from the chain-only picture and is concrete enough for the next theorem;
- a proof that the unnormalized expansion is just E1 in different coordinates and provides no new handle;
- a first-composition obstruction showing that consistency probabilities do not produce a target-level gain.

The last two are successful negative outcomes because they decide whether E2 should remain on the proof spine.

## Durable output

Commit the decisive mathematics to

`research/active/fa1f-finite-seed/students/student-a/002-unnormalized-patches.md`

with any code or auxiliary calculation in the same student directory. End with a short handoff pointing to the exact equations or countercalculation that should change the Professor's spine.

Do not switch scientific targets. If the patch route is sterile, establish that as sharply as you can and return it.