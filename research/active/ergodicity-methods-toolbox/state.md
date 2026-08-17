# Programme state

## Direction

Title: ergodicity methods toolbox for spin systems and IPS

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Principal target: compile a broad, concise, self-contained literature toolbox of rigorous methods used to prove ergodicity, uniqueness/convergence to equilibrium, coupling agreement, positive spectral gap, logarithmic Sobolev inequalities, mixing, or closely related relaxation statements for spin systems, interacting particle systems, KCSM, and closely adjacent interacting Markov models.

Breadth is intentional and model-specific methods are in scope.

Latest meeting: `meetings/014-wave-five-structural-verification.md`.

## Publication status

All **57** staged entries have passed Professor source audit, all 57 have live counterparts under `docs/entries/`, and the full wave-one-through-five public layer has now passed structural verification.

The principal/orchestrator reports on the integrated tree at `aa28743`:

```text
Checked 57 entries; 0 failed mechanical validation.
```

and `mkdocs build --strict` exits 0 with no warnings and no broken internal links. The only INFO output is unchanged legacy material: seven pre-existing pages absent from navigation and one pre-existing absolute-link note on the coarsened-patches page.

Completeness is exact: 57 staged entries, 57 promoted pages, 57 hub links, zero unresolved links, no promoted page missing from the hub, and no hub link without a page. Every promoted toolbox page contains `status:` and `audit:` metadata, and all 154 MkDocs `.md` navigation targets resolve to real files.

Legacy safety also passes. `git diff origin/main..research/ergodicity-methods-toolbox -- docs/` remains additions-only with zero non-additions. Wave five has exactly thirteen added method pages plus modifications confined to `docs/ergodicity-methods.md` and `mkdocs.yml`.

`validate_entries.py` and the MkDocs checks are structural only. Source/claim acceptance is the Professor audit recorded in Meetings 002--005, 010, and 013.

The repository-wide article layout remains unchanged for this programme: toolbox pages live in `docs/entries/`. The separate principal-level directory question is not reopened by the Professor.

## Wave-five ruling

All thirteen wave-five entries were accepted. Two semantic target corrections were made before publication:

- successful finite-dual coupling now targets `invariant-law-classification`, not global uniqueness/convergence;
- second-class product-shock coupling now targets `shock-dynamics` and `interface-stability`, not coupling agreement.

Both anti-padding substitutions were accepted:

- F did not manufacture an artificial-Nummelin page after a second failed targeted search; the accepted substitute is the super-Poincare reaction/diffusion decomposition;
- G did not manufacture a boundary-uniform dynamic projective-coupling page; the accepted substitute is Hairer's asymptotic binding coupling.

Those two failed generic targets are closed absent a concrete named source that changes the evidence.

## Workers

- Student F: **active** on `students/student-f/assignment-006.md`.
- Student G: **active** on `students/student-g/assignment-005.md`.

Every finished method entry is committed immediately as its own artifact. Students stage under this research workspace and do not edit `docs/` or `mkdocs.yml`.

## Wave-six targets

### Student F

Full Cheeger/conductance positive relaxation in a spin system; one bounded spectral-profile/evolving-set search; genuinely infinite-system Harris/Lyapunov ergodicity; exact projective-consistency invariant-law construction; renormalisation-group spectral-gap recursion for hierarchical spin models; and direct constrained-to-unconstrained refresh comparison or a source-supported substitute.

Artificial Nummelin and generic nonreversible sector/hypocoercive searches are not reopened absent named new evidence.

### Student G

Coupling independence/coarse-grained local-to-global coupling for spin systems; sticky coupling for McKean--Vlasov/weakly interacting particle systems; componentwise reflection with particle-number-uniform estimates; essential-hitting/restart complete convergence; moving-frame invariant laws seen from a second-class particle; and regeneration of an actual disagreement front, with a structured-finite-dual or other graphical substitution if the bounded search fails.

Generic boundary-uniform projective coupling and generic common/basic coupling remain closed absent named new evidence.

## Current live coverage

Fifty-seven source-audited and mechanically verified methods are live. Wave five added bootstrap/legal-path KCSM transfer, long-range good-path Poincare, nested mobile-droplet renormalisation, CBSEP auxiliary comparison, super-Poincare reaction/diffusion decomposition, tightness/compactness construction of infinite-particle dynamics, successful coupling of fixed-size finite duals, second-class microscopic shocks, maximal local Potts coupling, competition-interface regeneration, two-level contact restart complete convergence, asymptotic binding coupling, and asymptotic reflection coupling.

## Next Professor action

Source-audit the next completed wave-six handoff. Do not promote a wave-six entry before its primary theorem chain and proof-interface distinctness have been checked.
