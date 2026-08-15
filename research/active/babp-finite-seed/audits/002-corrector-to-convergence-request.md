# Independent audit request 002: BABP corrector-to-convergence proof

You are a fresh independent mathematical auditor. You have not participated in the development of this proof. Audit hostilely. Do not treat the Professor's acceptance, Student B's conclusions, or the prior edge-certificate audit as evidence for any step beyond the exact statement it verified.

Branch: `research/babp-finite-seed`.

Read:

- `research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`;
- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md` only as needed for the exact corrector definition;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md` only to know the already verified hypothesis `BABP-EDGE-001`;
- `research/active/babp-finite-seed/notes/professor-corrector-to-convergence-verification.md` only after you have independently analyzed the proof, so that it cannot seed your reconstruction;
- `research/claim-registry.md`, entry `BABP-CONV-001`, for the exact claim boundary.

The candidate theorem is:

> For fixed `lambda>0`, if there exist `k`, a bounded `phi:{0,1}^k -> R`, and `v>0` such that the exact finite-window right-edge drift satisfies `D_{k,lambda}(u,z;phi)>=v` for every edge state `(u,z)`, then one-dimensional BABP started from every finite nonempty deterministic set converges locally to Bernoulli equilibrium.

The concrete corollary uses the already verified ten-site corrector at `lambda=1/40`.

Your primary job is **proof-internal correctness**. Rebuild the bridge rather than merely checking displayed algebra.

## Load-bearing checks

1. **Tagged-gap dynamics.** Starting directly from the BABP transition rules, verify or refute that, until closure of a tagged internal vacant gap, the populations on its two sides can be equipped with the same right/left edge correctors and that the corrected gap width has generator drift at most `-2v`. Check width one separately. Check singleton side populations, all possible boundary deaths/births, and whether any transition simultaneously affects both sides in a way omitted by the product-generator argument.

2. **Gap genealogy.** Prove or refute the claims that internal gaps are born at width one, cannot split while positive, and distinct positive gaps cannot merge. Pay special attention to a separating block shrinking from several particles to one and to events at distance one from both gaps.

3. **Exponential tilting.** Verify the uniform jump-size and event-rate bounds for the corrected gap width and the killed-generator inequality for `exp(theta Z)`. Check carefully that replacing closure transitions by killing has the stated sign. Derive the lifetime and maximum-width tails with constants genuinely uniform over the surrounding finite configuration and birth location.

4. **Spatial displacement.** Verify the claimed Poisson domination of the number of gap-boundary shifts. Check the endpoint shift rates in every possible local configuration and whether one update can move an endpoint by more than one. Prove the spatial summability bound used after taking the one-third power of the Poisson tail.

5. **Nucleation sum.** Reconstruct rigorously the compensator/strong-Markov union bound over all gap births in infinite space and time. Check that the sum over sites is legitimate, that each genealogy is counted in a harmless way, and that no merge/split mechanism invalidates tagging. Determine whether the resulting estimate is genuinely uniform in late time:

   `limsup_{t->infinity} P(origin lies in an internal gap of width >=m) <= C exp(-c m)`.

6. **Nonescape.** Check the passage from the internal-gap estimate and the already verified statewise corrector hypothesis to

   `limsup_{t->infinity} P_B(B_t cap [-M,M] = empty) <= C exp(-cM)`.

   Do not replace the statewise corrector by bare asymptotic edge bounds unless you prove that replacement.

7. **Initial-state scope.** Identify exactly where finiteness and nonemptiness of the deterministic initial configuration are used. Report any additional hidden assumption, including parity, connectedness, or number of particles.

8. **Compactness/subsequence step.** Assuming the two external inputs stated in `BABP-CONV-001`, verify that the nonescape estimate indeed forces the empty-mixture coefficient to zero and gives convergence of the full trajectory rather than only selected subsequences.

## Independence requirement

Do not use Student B's intermediate lemmas as black boxes. Re-derive the key generator and genealogy statements from the physical process. You may use the independently audited `BABP-EDGE-001` only as the hypothesis that a statewise corrector exists at `lambda=1/40` with the recorded positive drift.

## Output

Commit the audit to

`research/active/babp-finite-seed/audits/002-corrector-to-convergence-audit.md`.

End with one of:

- `VERIFIED`;
- `VERIFIED WITH CORRECTIONS`, stating the exact corrected theorem;
- `NOT VERIFIED`, identifying the first fatal or unresolved step.

Separate theorem-breaking gaps from cosmetic exposition issues. If you find a repair, prove it rather than merely suggesting it.