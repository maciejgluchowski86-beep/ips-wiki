# Programme state

Date: 2026-08-17

## Active direction

Generalize the patch-representation / patch-positivity framework of the canonical paper `paper/` beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

## Principal questions

The programme should determine, as far as possible:

1. what replaces binary monomials for larger local state spaces;
2. what class of local IPS updates still admits a useful signed dual;
3. what the dual state and graphical interaction are;
4. what should be revealed in a generalized successful-interaction skeleton and what mark should remain hidden;
5. what the resulting patches are;
6. what generalized patch contributions and patch positivity mean;
7. what preservation/comparison/convergence statements follow;
8. which concrete non-binary or non-flip models satisfy the resulting criterion.

The core mechanism to preserve is conditional averaging before taking signs/absolute values, not any particular binary notation.

## Canonical source

For the existing binary construction, the paper `Patch representations and convergence for facilitated spin systems` under `paper/` is authoritative.

Key source files for the first block:

- `paper/sections/spin-systems.tex`;
- `paper/sections/signed-dual.tex`;
- `paper/sections/patches-body.tex`;
- `paper/sections/representation.tex`;
- `paper/sections/patch-positivity.tex`;
- `paper/appendices/monomial-dual.tex`.

Existing main-wiki patch pages are expository source material and should not be silently generalized in place.

## First bounded block

Assignment: `students/professor/assignment-001-finite-state-duality.md`.

Scope: finite local state space with a distinguished reference state and general bounded single-site replacement rates depending on a finite neighbourhood.

The first task is to fix a canonical tensor basis and decide whether it gives a fixed local signed Feynman--Kac graphical dual on finite typed active configurations, with an exact reduction to the binary paper.

Simultaneous multi-site updates, generalized patch factorization, positivity inequalities, and applications are downstream and are not to be attacked before this algebraic layer is settled.

## Previous programmes

The stopped positive-rates and FA-1f programmes remain closed exactly as previously recorded. This new direction does not reopen them.
