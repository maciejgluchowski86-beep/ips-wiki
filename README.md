# IPS Wiki

This repository is a source-of-truth wiki for interacting particle systems, spin systems, ergodicity, and related literature.

The working principle is:

1. Entries are written as small LaTeX source files in `wiki-src/entries/`.
2. Shared notation, macros, and style rules live in `wiki-meta/`.
3. `wiki-src/wiki-book.tex` compiles the entries into a readable PDF.
4. Changes should preserve explicit proof status, source status, and links between related entries.

The first stable reading target is the compiled PDF produced by the `Build wiki PDF` GitHub Actions workflow. The source files remain editable by hand, by Codex, or by a ChatGPT project with repository access.

## Current entries

- Spin system: `wiki-src/entries/spin-system.tex`
- Ergodicity: `wiki-src/entries/ergodicity.tex`

## Entry workflow

1. Draft a mock entry in chat.
2. Check terminology, notation, and proof status against existing entries.
3. Add literature references and cross-links.
4. Commit the approved entry to `wiki-src/entries/`.
5. Rebuild the PDF.

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
