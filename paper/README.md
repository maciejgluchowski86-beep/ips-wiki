# Paper source

The Overleaf main file is `paper/main.tex`.

The source is organized as follows:

- `main.tex`: title, abstract, section order, and bibliography;
- `preamble.tex`: packages, theorem environments, and notation;
- `sections/`: the paper body and appendices;
- `figures/`: source for paper figures;
- `references.bib`: bibliography.

From the repository root, compile locally with:

```bash
latexmk -cd -pdf paper/main.tex
```

The current version is a paper scaffold: the theorem statements, logical
dependencies, and proof architecture are present, while several local
calculations are intentionally collected in the appendices for later
expansion.
