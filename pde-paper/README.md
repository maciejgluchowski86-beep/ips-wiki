# PDE branching manuscript

This directory contains a standalone manuscript on integrability and cancellation in branching representations with derivative weights. It is separate from `paper/`, which is the facilitated-spin-system manuscript.

Compile from this directory with

```bash
latexmk -pdf main.tex
```

The manuscript contains full proofs of the audited results included in the paper: the repeated-Hessian obstruction and Gevrey-1/2 necessity, the NPP/HLOTW representation-level dichotomy, finite Hessian patch regrouping, the construction and finiteness of the canonical raw signed measure for every fixed finite quadratic-Hessian tree, the auxiliary deterministic iteration, Theorem C-prime, the fixed-datum raw-faithful obstruction, the exact residual-signed-variation characterization, sparse fixed-target retention, failure of naive patchwise Gaussian bridges, the explicit derivative-cluster patch estimate, and the target-uniform time-spine representation corollary.

For `phi'' in C^alpha`, the preliminaries construct an explicit standard-Borel raw mark space and a finite signed measure `mu_tau^{t,x}` for each finite tree, prove

```text
mu_tau^{t,x}(Omega_tau) = F_tau(t,x),
```

and prove that decorated maximal-left-patch skeletons are a bijective reindexing once ordered side-attachment slots are included in the decoration. No smallness condition is used in this finite-tree construction.

The time-spine argument is split into two logically separate statements. The analytic derivative-cluster proposition proves, with explicit constants, that the absolute-time patch norm grows at most geometrically in the patch length; it has no smallness hypothesis. The following representation corollary uses the C-prime and geometric-series smallness conditions to sum those finite-patch bounds over all trees.

The final measure-theoretic theorem identifies the exact first-moment invariant at a fixed target:

```text
residual variation = total variation after pushforward
                   = L1 norm of the conditional raw signed barycenter.
```

This fixed-target characterization does not by itself produce one target-uniform coarsening architecture. Sparse full-state retention is pointwise in the target, while the time-spine construction gives one target-uniform architecture on its stronger small-data regime. The examples showing that the full Gaussian vector may be retained on small pieces and that retaining only a time coordinate may fail are abstract signed-measure examples unless explicitly stated otherwise.

There are no proof placeholders in the manuscript source. The explicitly labeled final subsection lists open structural problems rather than unfinished arguments.

The manuscript deliberately does not modify or share source files with the facilitated-spin-system paper under `paper/`.
