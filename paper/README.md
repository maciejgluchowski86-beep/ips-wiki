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

The current version is a paper scaffold: the theorem statements, logical
dependencies, and proof architecture are present, while several local
calculations are intentionally collected in the appendices for later
expansion.
