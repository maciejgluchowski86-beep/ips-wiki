# Paper source

The Overleaf main file is the repository-level `main.tex`. It is a thin
wrapper around `paper/main.tex`, where the paper source remains.

`paper/main.tex` is currently an empty document shell. The shared
packages, theorem environments, and notation are in
`paper/preamble.tex`. No title, framing, section order, or paper content
has yet been chosen.

From the repository root, compile locally with:

```bash
latexmk -pdf main.tex
```
