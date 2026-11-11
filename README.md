# IPS Wiki

This repository contains two public artifacts:

1. the IPS wiki, published at <https://maciejgluchowski86-beep.github.io/ips-wiki/>;
2. the paper on patch-positive spin systems, currently titled *Ergodicity without monotonicity: patch-positive spin systems*.

## Wiki

The wiki source is under `docs/`. Site configuration is in `mkdocs.yml`, and the GitHub Pages workflow is in `.github/workflows/build-wiki-site.yml`.

To build it locally:

```bash
python -m pip install -r requirements.txt
mkdocs build
```

## Paper

**The current Overleaf-maintained manuscript is `new_main.tex`, not `main.tex`.**
The Overleaf-to-GitHub updates of November 2026, including the relocation of
`\mathcal G_T` to the patch-factorization subsection, were pushed to
`new_main.tex`. The older `main.tex` is retained in the repository for reference;
do not treat it as the latest manuscript.

The current manuscript is self-contained in `new_main.tex`, including its TikZ
figures. Its repository-local support files are:

- `references.bib`;
- `amsplain-fullnames.bst`;
- `ejpecp.cls`.

To compile the current manuscript locally:

```bash
latexmk -pdf new_main.tex
```

**Editing workflow:** The live Overleaf version takes precedence. Before
editing the manuscript through GitHub, first bring in the latest Overleaf
changes, then inspect and modify `new_main.tex` while preserving those
changes. Do not independently edit the older `main.tex`.
