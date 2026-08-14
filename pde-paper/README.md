# PDE branching manuscript

This directory contains a standalone manuscript on integrability and cancellation in branching representations with derivative weights. It is separate from `paper/`, which is the facilitated-spin-system manuscript.

Compile from this directory with

```bash
latexmk -pdf main.tex
```

The manuscript now contains full proofs of the audited results included in the paper: the repeated-Hessian obstruction and Gevrey-1/2 necessity, the NPP/HLOTW representation-level dichotomy, finite Hessian patch regrouping, the auxiliary deterministic iteration, Theorem C-prime, the fixed-datum raw-faithful obstruction, and the coarsening hierarchy. The hierarchy includes the failure of naive patchwise Gaussian-bridge coarsening and the positive time-spine representation which retains continuous branch-time randomness under an additional geometric smallness condition.

The manuscript deliberately does not modify or share source files with the facilitated-spin-system paper under `paper/`.
