# Paper source

The Overleaf main file is the repository-level `main.tex`. It is a thin
wrapper around `paper/main.tex`, where the paper source remains.

The source is organized as follows:

- `main.tex`: title, abstract, section order, and bibliography;
- `preamble.tex`: packages, theorem environments, and notation;
- `sections/`: the paper body and appendices;
- `figures/`: source for paper figures;
- `references.bib`: bibliography.

From the repository root, compile locally with:

```bash
latexmk -pdf main.tex
```

The current version is a paper scaffold rather than a prose draft.
Definitions, results, cited results, proofs, figures, and notation are
written in formal environments. Every passage requiring authorial
motivation, interpretation, literature positioning, or discussion is
represented by a gray `discussion` blurb listing the information to
convey there.

Recurring concepts have labeled definitions and clickable internal
links. In particular, every use of ergodicity terminology links to its
definition in the setup section.
