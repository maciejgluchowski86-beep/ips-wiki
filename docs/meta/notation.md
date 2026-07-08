---
title: Notation
---

# Notation

This page is the human-readable notation ledger for the IPS wiki. The rendered site uses MathJax macros configured in `docs/javascripts/mathjax.js`.

| Symbol | Meaning | Default scope |
|---|---|---|
| \(\Lambda\) | countable index set, usually \(\Z^d\) or \(\Z\) | spin-system entries |
| \(E\) | single-site spin space, usually finite | spin systems |
| \(\Omega\) | configuration space \(E^\Lambda\) | Markov processes |
| \(\eta,\xi\) | configurations | IPS/spin systems |
| \(\eta^x\) | configuration obtained by flipping at site \(x\) | two-state spin systems |
| \(c(x,\eta)\) | flip rate at site \(x\) in configuration \(\eta\) | spin systems |
| \(\cL\) | generator | Markov processes |
| \(S(t)\) | Markov semigroup | ergodicity |
| \(\nu\) | invariant measure, when unique or distinguished | ergodicity |
| \(\mu S(t)\) | law at time \(t\) started from law \(\mu\) | ergodicity |

## Current convention

Unless a page says otherwise, a spin system is a continuous-time Markov process on \(\Omega=E^\Lambda\), usually with \(E=\{0,1\}\) or \(E=\{-1,+1\}\) and local transition rates. For two-state flip systems, the default generator is

\[
\cL f(\eta)=\sum_{x\in\Lambda} c(x,\eta)\bigl(f(\eta^x)-f(\eta)\bigr).
\]
