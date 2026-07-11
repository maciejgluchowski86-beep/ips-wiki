# Compilation procedure for IPS wiki edits

This file records the general operating procedure for adding or editing entries. It is not a style guide and should not duplicate notation, writing conventions, or entry templates. Those live in:

- `docs/meta/style-decisions.md`
- `docs/meta/notation.md`
- `docs/meta/entry-template.md`

## 1. Bootstrap the repository context

Before a substantive edit, read:

1. `project-state.md`.
2. `README.md`.
3. `docs/meta/style-decisions.md`.
4. `docs/meta/notation.md`.
5. `docs/meta/entry-template.md` when creating a new entry.
6. The existing entries that are direct parents, children, or close neighbours of the requested change.

Do not start from memory alone when the edit depends on current repository structure or current conventions.

## 2. Classify the requested change

Determine whether the request is a new entry, a content edit, a notation or style edit, a navigation edit, a link audit, a metadata update, or a deletion or merger. For mixed requests, separate the parts and apply the relevant procedure to each one.

## 3. Locate the authoritative files

- Mathematical or expository content belongs in `docs/entries/`.
- Durable notation belongs in `docs/meta/notation.md`.
- Durable prose and style decisions belong in `docs/meta/style-decisions.md`.
- Reusable entry skeletons belong in `docs/meta/entry-template.md`.
- Site navigation belongs in `mkdocs.yml`.
- Public index listings belong in `docs/index.md`.
- Repository state summaries belong in `project-state.md`.
- Repository overview listings belong in `README.md`.

## 4. Decide whether a new entry is needed

Create a new entry only when it will be a stable reference page with a clear scope. If the requested material is a special case of an existing entry, make the new entry a compact specialization and link to the parent entry instead of reproducing it.

## 5. Draft against the existing structure

Before writing, identify the parent entries, sibling entries, downstream entries that should link back, and any navigation or index changes.

## 6. Apply the edit

Make the smallest coherent set of changes. For new entries, usually update:

1. the new file in `docs/entries/`;
2. `mkdocs.yml`;
3. `docs/index.md`;
4. `README.md`;
5. `project-state.md`;
6. nearby entries that should link to the new page.

## 7. Check consistency before committing

Check that:

- edited files satisfy the conventions in `docs/meta/`;
- internal links and navigation paths resolve;
- new entries have front matter;
- no private notes or unpublished claims without proof status were added;
- no standalone single-dollar math delimiters remain;
- TeX-bearing source preserved commands such as `\nu`, `\Omega`, `\text`, `\ge`, and `\int`;
- generated TeX text used a raw or otherwise byte-preserving representation;
- every edited math page is fetched again after publication and its stored delimiters and backslashes are inspected;
- if JavaScript `String.replace` inserts TeX, a function replacement is used so dollar signs are not interpreted as replacement patterns.

Run the strict site build before committing:

```bash
mkdocs build --strict
```

## 8. Commit and report

Use a focused commit message. Report the files changed, the substantive effect, the commit SHA, and any checks that were not run or any remaining uncertainty.
