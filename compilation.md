# Compilation instructions for IPS wiki entries

This file records working instructions for adding or editing entries in the IPS wiki. It is intended for ChatGPT/Codex-style agents editing the repository.

## Startup routine

Before a substantive entry edit, read:

1. `project-state.md`.
2. `README.md`.
3. `docs/meta/style-decisions.md`.
4. `docs/meta/notation.md`.
5. The nearest parent entries and adjacent entries relevant to the requested change.

For example, before writing a model-specific duality entry, read `docs/entries/duality.md`, `docs/entries/signed-additive-set-process.md`, `docs/entries/monomial-duality-for-spin-systems.md`, the model entry, and any general entry that the model-specific entry should specialize.

## General writing principle

Entries should be modular reference pages, not self-contained lecture notes. Use existing entries by inline links and specialize them. Do not rederive general theory in a model-specific page.

A model-specific entry should usually contain only the data needed to apply the general construction. A general-definition entry should define the concept once, so later entries can link to it.

## When to create a separate entry

Create or use a general entry when a concept is not model-specific. Examples:

- softening a constraint belongs in `soft-kcsm.md`, not only inside an FA-1f page;
- perturbations that preserve a dual process belong in `duality-noise-lemma.md`, not in every model page;
- finite-set signed dual processes belong in `signed-additive-set-process.md`, not in each example.

Then the model-specific entry should link to the general entry and record only the specialization.

## Entry structure

Use front matter:

```markdown
---
title: Entry title
status: definition | standard fact | proved here | conditional | heuristic | open | obsolete
tags:
  - tag
---
```

Write as a mathematical article. Avoid meta-commentary about the wiki except in meta files. Use inline links at the first natural mathematically useful occurrence. Do not add top-level "Related pages" sections.

## Specialization entries

For a specialization entry, use a compact, systematic format.

1. State the parent construction by link.
2. State the convention or model parameters.
3. List the final usable data.
4. Avoid derivations unless the entry is explicitly a proof entry.

For example, a model-specific monomial-duality entry should list the actual dual rates, signs, and Feynman--Kac weights. It should not list intermediate signed coefficients unless the entry is specifically about the derivation.

## Duality and signed-process conventions

Use the sign set

$$
\{+,-\},
$$

not \(\{+1,-1\}\), for signed process states and sign labels. Signs multiply by the usual sign rule and act on real numbers by \(+x=x\), \(-x=-x\).

For signed additive set processes, use the convention

$$
\beta_i(\vn)=0.
$$

The update maps should include the sign update:

$$
D_{i,S}Y=\left((A\setminus\{i\})\cup S,\sigma\sigma_i^\delta(S)\right),
$$

$$
B_{i,S}Y=\left(A\cup S,\sigma\sigma_i^\beta(S)\right).
$$

When a Feynman--Kac potential is site-local, write

$$
V(A)=\sum_{i\in A}V_i
$$

and then give the formula for \(V_i\).

## Model-specific duality template

For each case in a model-specific duality entry, list the following fields explicitly:

1. Nonzero source-killing rates \(\delta_i(S)\).
2. Source-killing signs \(\sigma_i^\delta(S)\in\{+,-\}\).
3. Nonzero source-keeping rates \(\beta_i(S)\).
4. Source-keeping signs \(\sigma_i^\beta(S)\in\{+,-\}\).
5. Site Feynman--Kac weight \(V_i\).

All omitted rates should be declared zero once. Signs attached to zero rates are irrelevant.

For perturbations covered by the duality noise lemma, do not restate the proof. State that the dual rates and signs are unchanged, and give only the changed \(V_i\).

## KCSM conventions

For KCSM entries:

- \(0\) is the facilitating or vacant state.
- \(q\) is the vacancy density.
- \(p=1-q\) is the density of state \(1\).
- The hard constraint is usually denoted \(c_i\).
- A soft constraint is

$$
c_i^\varepsilon(\eta)=\varepsilon_i+(1-\varepsilon_i)c_i(\eta).
$$

For FA-1f,

$$
c_i(\eta)=1-\chi_{N(i)}(\eta),
$$

so

$$
c_i^\varepsilon(\eta)=1-(1-\varepsilon_i)\chi_{N(i)}(\eta).
$$

The East model should be described as FA-1f on an oriented lattice, not merely as an analogue.

## Navigation and placement

Place entries where readers will look for them, not necessarily under the most abstract topic. For example, an FA-1f duality entry belongs in the KCSM section even though it uses duality.

When adding a new entry, update as needed:

1. `mkdocs.yml` navigation.
2. `docs/index.md`.
3. `README.md`.
4. `project-state.md`.
5. Nearby entries that should link to the new entry.

Do not update navigation for minor edits to existing entries unless placement changes.

## Style checks before committing

Before committing, check the entry for:

- no unnecessary rederivation of linked parent material;
- final operational objects stated directly;
- consistent notation from `docs/meta/notation.md`;
- no bare ambiguous subset command in polished prose;
- no `\epsilon`; use `\varepsilon`;
- no numeric sign-state convention \(\{+1,-1\}\) for signed processes;
- no top-level "Related pages" list;
- no private project strategy or raw scratch work.
