# IPS Wiki

This repository is a public-facing wiki for interacting particle systems, spin systems, ergodicity, duality, probabilistic representations for nonlinear PDEs, and related literature.

The rendered wiki is published at <https://maciejgluchowski86-beep.github.io/ips-wiki/>.

The wiki is article-first. Each entry is a separate Markdown page under `docs/entries/`, with TeX math rendered in the web view and ordinary Markdown links between entries. Cross-links should usually be inline links through relevant words or phrases, not top-level related-page lists.

## Paper drafts

The facilitated-spin-system manuscript lives under `paper/`. The repository-level `main.tex` is its Overleaf entry point and loads `paper/main.tex`; the EJP/ECP class is supplied by the repository-level `ejpecp.cls`. Shared macros and theorem environments for that manuscript live in `paper/preamble.tex`, and its bibliography is `paper/references.bib`. `STYLE.md` records its typography and prose conventions.

A separate nonlinear-PDE manuscript lives under `pde-paper/`. Its entry point is `pde-paper/main.tex`, with an independent preamble, bibliography, and section tree. This manuscript studies cancellation before absolute values in branching representations with derivative weights. It does not modify or replace the facilitated-spin-system paper.

## Reading target

The intended wiki reading target is the rendered MkDocs site at
<https://maciejgluchowski86-beep.github.io/ips-wiki/>.

- Source pages: `docs/`
- Entry pages: `docs/entries/`
- Meta/style pages: `docs/meta/`
- Site configuration: `mkdocs.yml`

GitHub Actions contains a `Build wiki site` workflow. It checks live-wiki curation metadata, builds the site from `docs/`, and deploys through GitHub Pages after every push to `main` when Pages is enabled for the repository.

## Current core entries

- Lattice and graph: `docs/entries/lattice-and-graph.md`
- Polynomial-growth lattice: `docs/entries/polynomial-growth-lattice.md`
- Local functions: `docs/entries/local-functions.md`
- Monomials: `docs/entries/monomials.md`
- Bernoulli product measure: `docs/entries/bernoulli-product-measure.md`
- Interacting particle system: `docs/entries/interacting-particle-system.md`
- Spin system: `docs/entries/spin-system.md`
- Pure noise spin system: `docs/entries/pure-noise-spin-system.md`
- Oriented spin system: `docs/entries/oriented-spin-system.md`
- Invariant measure: `docs/entries/invariant-measure.md`
- Ergodicity: `docs/entries/ergodicity.md`

## Current duality entries

- Duality: `docs/entries/duality.md`
- Monomial duality for spin systems: `docs/entries/monomial-duality-for-spin-systems.md`
- Duality noise lemma: `docs/entries/duality-noise-lemma.md`

## Current signed additive set process entries

- Signed additive set process: `docs/entries/signed-additive-set-process.md`
- Graphical construction of signed additive set process: `docs/entries/graphical-construction-of-signed-additive-set-process.md`
- Successful interaction: `docs/entries/successful-interaction.md`

## Current patch entries

- Patch: `docs/entries/patch.md`
- Interaction cone: `docs/entries/interaction-cone.md`
- Patch consistency event: `docs/entries/patch-consistency-event.md`
- Patch factorization: `docs/entries/patch-factorization.md`
- Patch contribution: `docs/entries/patch-contribution.md`
- Patch positivity property: `docs/entries/patch-positivity-property.md`
- Patch critical density: `docs/entries/patch-critical-density.md`
- High-density measure: `docs/entries/high-density-measure.md`
- Patch representation of spin systems: `docs/entries/patch-representation-of-spin-systems.md`
- Undoing duality under confined interactions: `docs/entries/undoing-duality-under-confined-interactions.md`
- Finite propagation for zero-boundary restrictions: `docs/entries/finite-propagation-for-zero-boundary-restrictions.md`
- Exponential relaxation under confined late interactions: `docs/entries/exponential-relaxation-under-confined-late-interactions.md`
- Monomial monotonicity for high-density measures: `docs/entries/monomial-monotonicity-for-high-density-measures.md`
- Pure-death comparison under patch positivity: `docs/entries/pure-death-comparison-under-patch-positivity.md`
- Common invariant limit under uniform pure deaths: `docs/entries/common-invariant-limit-under-uniform-pure-deaths.md`

## Current KCSM entries

- Bernoulli refresh operator: `docs/entries/bernoulli-refresh-operator.md`
- Update family: `docs/entries/update-family.md`
- Kinetically constrained spin model: `docs/entries/kinetically-constrained-spin-model.md`
- Soft KCSM: `docs/entries/soft-kcsm.md`
- Legal update: `docs/entries/legal-update.md`
- FA-1f model: `docs/entries/fa-1f-model.md`
- East model: `docs/entries/east-model.md`
- Biased annihilating branching process: `docs/entries/babp-model.md`
- KCSM relaxation and mixing: `docs/entries/kcsm-relaxation-and-mixing.md`
- KCSM out of equilibrium: `docs/entries/kcsm-out-of-equilibrium.md`
- FA-1f out of equilibrium: `docs/entries/fa-1f-out-of-equilibrium.md`
- East out of equilibrium: `docs/entries/east-out-of-equilibrium.md`
- BABP out of equilibrium: `docs/entries/babp-out-of-equilibrium.md`

## PDE and branching representations

The pedagogical entry point for the PDE side is `docs/pde-reading-path.md`. The advanced research map is `docs/pde-branching-representations.md`.

The PDE core path now treats the surviving audited material from the terminated quadratic-Hessian programme only as reusable background and mechanism notes.

## Entry workflow

The live wiki is not scratch space. See `docs/meta/wiki-quality-and-pruning.md`.

1. Draft or revise material in a ChatGPT session, not directly in `docs/`.
2. Check terminology, notation, dependency links, mathematical status, and sources.
3. Run the status-appropriate wiki-quality review.
4. Admit the page to `docs/entries/` only with `audit: current`.
5. Periodic Wiki Curator sweeps keep, rewrite, demote, or delete older material.
6. Git history is the default archive of pruned pages.

During the legacy migration, old pages without `audit: current` are review debt rather than grandfathered content. Any legacy page that is materially edited must be brought to the current standard in the same change.

## Public-content rule

The rendered wiki should contain only useful, well-written material that is reliable at its stated status. Do not add private research strategy, raw scratch work, worker dispatches, tentative proof attempts, credentials, personal information, copyrighted source text, or unaudited project claims. Delete obsolete/scaffolding material from the live wiki rather than maintaining a public research archive.

## Mathematical status and audit convention

`status` describes the mathematical role of an entry. `audit: current` separately records that the page has passed the present live-wiki quality gate.

Allowed status labels are:

- `definition`
- `standard fact`
- `proved here`
- `observation`
- `literature`
- `conditional`
- `conjecture`
- `heuristic`
- `open`

`proved here` is reserved for a project-specific theorem that is `verified` under the current autonomous verification protocol. A legacy `proved here` label does not itself establish verification.

`obsolete` may occur only as legacy migration metadata. Once identified, obsolete material should be deleted from `docs/`; Git history preserves it.
