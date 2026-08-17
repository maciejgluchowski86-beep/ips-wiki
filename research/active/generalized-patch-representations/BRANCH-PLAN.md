# Generalized patch representations: branch and section plan

Date: 2026-08-17

## Principal direction

The active programme is to investigate extensions of the patch-positivity construction from binary flip spin systems to more general interacting particle systems: larger local state spaces, more general local updates, the corresponding duality and dual process, the analogue of successful interactions and hidden marks, generalized patches and patch positivity, and applications.

This is a new programme. It does not reopen any previously stopped positive-rates or FA-1f architecture.

## Repository layout

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- hub: `docs/generalized-patch-representations.md`;
- section pages: `docs/generalized-patch-representations/`.

The existing canonical binary patch paper under `paper/` and the existing patch wiki pages under `docs/entries/` are source material. They are not to be rewritten merely to fit the new notation.

No change from this programme is to be published to `main` unless the principal later gives a separate publication instruction. In particular, no merge of this research branch to `main` is part of the current work.

## Promotion rule inside the branch

Raw calculations, assignments, counterexamples, and tentative definitions live under the research workspace.

A definition/construction may be copied into the branch-only wiki section only after it has survived the current mathematical block well enough to be useful as a stable notation/reference page. Such branch-only wiki pages are still research artifacts, not published claims.

## First block decision

The first block is **definitions/notation plus exact algebraic duality existence**, with definitions first.

Reason: for more than two local states there is no unique analogue of the binary monomial until a local function basis is fixed. The dual state space and the meaning of an interaction target depend on that choice. Asking for the dual process before fixing this algebraic layer is therefore under-specified.

The first bounded target is finite local state space and general single-site replacement dynamics. It asks whether a canonical indicator/tensor basis gives:

1. an exact signed Feynman--Kac dual on finite typed active configurations;
2. a graphical interaction language in which each relevant event has a source, a finite typed target, and a hidden local mark analogous to the binary source-survival choice;
3. a binary specialization exactly recovering the paper's monomial dual after an explicit identification.

Only after this is settled should the programme enlarge to simultaneous multi-site updates or attempt generalized patch positivity.
