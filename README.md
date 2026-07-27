# IPS Wiki

This repository is a public-facing wiki for interacting particle systems, spin systems, ergodicity, duality, and related literature.

The wiki is article-first. Each entry is a separate Markdown page under `docs/entries/`, with TeX math rendered in the web view and ordinary Markdown links between entries. Cross-links should usually be inline links through relevant words and phrases, not top-level related-page lists.

## Paper draft

The LaTeX template for the paper lives under `paper/`. The
repository-level `main.tex` is the Overleaf main file and loads
`paper/main.tex`. The paper body contains the agreed structural
scaffold. Introduction Sections 1.1--1.3 have been drafted in prose;
they motivate the calm--facilitating tendency, distinguish interaction
strength from persistence, and introduce patches as the source of a
recovered moment order. The remaining sections contain short drafting
notes and links to the relevant wiki entries. The draft contains no
settled theorem statements or proofs. Shared macros and theorem
environments live in `paper/preamble.tex`.

## Reading target

The intended reading target is the rendered MkDocs site.

- Source pages: `docs/`
- Entry pages: `docs/entries/`
- Meta/style pages: `docs/meta/`
- Site configuration: `mkdocs.yml`

GitHub Actions contains a `Build wiki site` workflow. It builds the site from `docs/` and deploys it through GitHub Pages after every push to `main` when Pages is enabled for the repository.

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
- Monomial duality for FA-1f: `docs/entries/monomial-duality-for-fa-1f.md`
- Patch contributions for FA-1f: `docs/entries/patch-contributions-for-fa-1f.md`
- Patch positivity for FA-1f: `docs/entries/patch-positivity-for-fa-1f.md`
- Patch critical density for FA-1f: `docs/entries/patch-critical-density-for-fa-1f.md`
- Monomial duality for BABP: `docs/entries/monomial-duality-for-babp.md`
- Patch contributions for BABP: `docs/entries/patch-contributions-for-babp.md`
- Patch positivity for BABP: `docs/entries/patch-positivity-for-babp.md`
- Patch critical density for BABP: `docs/entries/patch-critical-density-for-babp.md`
- KCSM relaxation and mixing: `docs/entries/kcsm-relaxation-and-mixing.md`
- KCSM out of equilibrium: `docs/entries/kcsm-out-of-equilibrium.md`
- FA-1f out of equilibrium: `docs/entries/fa-1f-out-of-equilibrium.md`
- East out of equilibrium: `docs/entries/east-out-of-equilibrium.md`
- BABP out of equilibrium: `docs/entries/babp-out-of-equilibrium.md`

## Entry workflow

1. Draft a mock entry in chat.
2. Check terminology, notation, proof status, and inline links against existing entries.
3. Add literature references where appropriate.
4. Commit the approved entry to `docs/entries/`.
5. The site deploys automatically after the push to `main`.

## Public-content rule

This repository is intended to be safe for public viewing. Do not add private research strategy, raw scratch work, credentials, personal information, copyrighted source text, or unpublished claims stated without proof status.

## Mathematical status convention

Each entry should label its status in front matter as one of:

- `definition`
- `standard fact`
- `proved here`
- `conditional`
- `heuristic`
- `open`
- `obsolete`

Mathematical claims that are not definitions or standard facts should include a proof, citation, or explicit gap marker.
