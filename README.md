# IPS Wiki

This repository is a source-of-truth wiki for interacting particle systems, spin systems, ergodicity, and related literature.

The wiki is article-first, not book-first. Each entry is a separate Markdown page under `docs/entries/`, with TeX math rendered in the web view and ordinary Markdown links between entries.

## Reading target

The intended reading target is the rendered MkDocs site, not a single compiled PDF.

- Source pages: `docs/`
- Entry pages: `docs/entries/`
- Meta/style pages: `docs/meta/`
- Site configuration: `mkdocs.yml`

GitHub Actions contains a `Build wiki site` workflow. It builds the site from `docs/` and deploys it through GitHub Pages when Pages is enabled for the repository.

## Current entries

- Spin system: `docs/entries/spin-system.md`
- Ergodicity: `docs/entries/ergodicity.md`

## Entry workflow

1. Draft a mock entry in chat.
2. Check terminology, notation, and proof status against existing entries.
3. Add literature references and cross-links.
4. Commit the approved entry to `docs/entries/`.
5. Rebuild the site.

## Mathematical status convention

Each entry should label its status as one of:

- `definition`
- `standard fact`
- `proved here`
- `conditional`
- `heuristic`
- `open`
- `obsolete`

Mathematical claims that are not definitions or standard facts should include a proof, citation, or explicit gap marker.
