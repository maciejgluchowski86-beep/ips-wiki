# PDE branching manuscript

This directory contains a standalone manuscript on integrability and cancellation in branching representations with derivative weights. It is separate from `paper/`, which is the facilitated-spin-system manuscript.

Compile from this directory with

```bash
latexmk -pdf main.tex
```

The manuscript contains full proofs of the audited results included in the paper: the repeated-Hessian obstruction and Gevrey-1/2 necessity, the NPP/HLOTW representation-level dichotomy, finite Hessian patch regrouping, the construction and finiteness of the canonical raw signed measure for every fixed finite quadratic-Hessian tree, the auxiliary deterministic iteration, Theorem C-prime, the fixed-datum raw-faithful obstruction, the structured time-spine coarsening theorem, and the exact residual-signed-variation characterization of skeleton-preserving coarsenings.

For `phi'' in C^alpha`, the preliminaries construct an explicit standard-Borel raw mark space and a finite signed measure `mu_tau^{t,x}` for each finite tree, prove

```text
mu_tau^{t,x}(Omega_tau) = F_tau(t,x),
```

and prove that decorated maximal-left-patch skeletons are a bijective reindexing once ordered side-attachment slots are included in the decoration. No smallness condition is used in this finite-tree construction.

The final theorem identifies the exact first-moment invariant:

```text
residual variation = total variation after pushforward
                   = L1 norm of the conditional raw signed barycenter.
```

It also records explicit counterexamples showing that retaining Gaussian marks is not intrinsically bad and retaining only branch times is not intrinsically safe.

The manuscript deliberately does not modify or share source files with the facilitated-spin-system paper under `paper/`.
