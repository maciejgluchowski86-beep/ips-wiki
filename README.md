# IPS Wiki

This repository contains two public artifacts:

1. the IPS wiki, published at <https://maciejgluchowski86-beep.github.io/ips-wiki/>;
2. the paper *Patch positive spin systems*.

## Wiki

The wiki source is under `docs/`. Site configuration is in `mkdocs.yml`, and the GitHub Pages workflow is in `.github/workflows/build-wiki-site.yml`.

To build it locally:

```bash
python -m pip install -r requirements.txt
mkdocs build
```

## Paper

The Overleaf entry point is the repository-level `main.tex`. The manuscript is self-contained in that file, including its TikZ figures. Its only repository-local support files are:

- `references.bib`;
- `amsplain-fullnames.bst`;
- `ejpecp.cls`.

To compile it locally:

```bash
latexmk -pdf main.tex
```
