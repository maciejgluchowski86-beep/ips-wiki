# Student F Assignment 003: analytic breadth wave three

## Objective

Continue the ergodicity-methods toolbox by filling six analytic method families that are still absent from the accepted staging set. This remains source-compilation work, not a new proof programme.

Read first:

- root `CHATGPT.md`;
- `research/active/ergodicity-methods-toolbox/state.md`;
- `proof-spine.md`;
- `entry-template.md`;
- `meetings/004-f-wave-two-source-audit-and-analytic-wave-three.md`.

## Durability rule — mandatory

**Commit each finished method entry immediately.** One completed method entry per substantive entry commit. Do not batch entries in a final response. A session/rendering failure should cost at most the current unfinished entry.

Stage only under:

`research/active/ergodicity-methods-toolbox/entries/`

Do not edit `docs/` or `mkdocs.yml`.

## Source rule

For each entry:

- inspect at least one primary source;
- give an exact theorem/proposition/lemma/section/page pinpoint and stable URL/DOI/arXiv identifier;
- if the general theorem is not itself an IPS/spin theorem, include a primary concrete IPS/spin/KCSM/Glauber application;
- distinguish spectral gap, LSI/mLSI, total-variation mixing, local ergodicity, and hydrodynamic replacement conclusions;
- do not make an origin/priority claim unless the origin source was actually inspected;
- keep the proof interface distinct from already accepted entries and state the relation in `Limitations` when overlap is close.

## Wave-three targets

Produce six entries unless source structure forces a substitution.

1. **Bakry--Emery / Bochner / Gamma-calculus coercivity.** Find a discrete or continuous spin/IPS application where a curvature/commutation/Bochner identity proves entropy decay, Poincare, or LSI. State the actual curvature or quadratic-form criterion, not merely the slogan `Gamma_2>=rho Gamma`.

2. **Two-scale / coarse-graining coercivity for conservative spins.** Source a theorem that decomposes microscopic conditional relaxation and macroscopic/coarse-grained relaxation to obtain a uniform or scaling-sharp Poincare/LSI estimate. Keep this distinct from Lu--Yau filtration recursion.

3. **Aldous/interchange spectral-gap reduction.** Explain the theorem equating the interchange-process spectral gap with the underlying random-walk gap and the resulting exclusion consequence. Make clear what is exact equality and what depends on the graph/rates.

4. **Nash inequality / heat-kernel or spectral-profile smoothing with an IPS application.** The entry must expose an inequality that yields polynomial or non-exponential relaxation/smoothing when a positive uniform gap is not the correct scale. A concrete exclusion, zero-range, or Glauber-type application is required.

5. **Nonreversible coercivity via symmetric part, sector condition, or hypocoercive comparison.** Include only if a clean primary IPS/spin application exists. State exactly what estimate on the nonreversible generator transfers decay or a gap. Do not write a generic finite-dimensional hypocoercivity page with no IPS application.

6. **Conductance / Cheeger / isoperimetric lower bound for a spin-system chain.** State the conductance-to-gap/mixing criterion and give a concrete Glauber/spin application where a positive isoperimetric bound is actually used to prove relaxation. Keep it distinct from canonical-path congestion.

### Allowed substitution

If target 4, 5, or 6 does not admit a clean source-supported IPS entry in the available literature, substitute one genuinely distinct analytic/model-specific method from the uncovered coverage spine. Preferred substitutes include comparison with unconstrained refresh dynamics, a sharp finite-volume-to-infinite-volume transfer theorem, or a model-specific coercive inequality. State the substitution and reason in the final handoff.

## Completion

Run `validate_entries.py` if available. Final handoff should list filenames and SHAs, source/attribution qualifications, and additional uncovered analytic families. Do not include long summaries in chat; the committed entries are the durable record.
