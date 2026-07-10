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

Determine whether the request is one of the following:

- a new entry;
- a content edit to an existing entry;
- a notation or style-convention edit;
- a navigation/placement edit;
- a link-audit or cross-reference edit;
- a metadata/state update;
- a deletion or merger.

For mixed requests, separate the parts and apply the relevant procedure to each one.

## 3. Locate the authoritative files

For every edit, identify which files are authoritative for the change.

- Mathematical or expository content belongs in `docs/entries/`.
- Durable notation belongs in `docs/meta/notation.md`.
- Durable prose/style decisions belong in `docs/meta/style-decisions.md`.
- Reusable entry skeletons belong in `docs/meta/entry-template.md`.
- Site navigation belongs in `mkdocs.yml`.
- Public index listings belong in `docs/index.md`.
- Repository state summaries belong in `project-state.md`.
- Repository overview listings belong in `README.md`.

Do not encode durable style or notation choices in this file.

## 4. Decide whether a new entry is needed

Before creating a new entry, check whether the concept already has a natural home. Prefer editing or linking an existing general entry when the concept is already covered there.

Create a new entry only when it will be a stable reference page with a clear scope. If the requested material is a special case of an existing entry, make the new entry a compact specialization and link to the parent entry instead of reproducing the parent construction.

## 5. Draft the edit against existing structure

Use the existing wiki graph. A new or edited entry should fit into the current dependency structure and link to the nearest relevant entries.

Before writing, identify:

- the parent entries the page depends on;
- sibling entries that should be cross-linked;
- downstream entries that should link back to the new or edited page;
- whether navigation or index listings should change.

## 6. Apply the edit

Make the smallest coherent set of file changes. Avoid unrelated cleanup in the same edit unless the user asked for a broad cleanup pass.

For new entries, usually update:

1. the new file in `docs/entries/`;
2. `mkdocs.yml`, if the entry should appear in navigation;
3. `docs/index.md`, if it should appear on the public index;
4. `README.md`, if it belongs in the current-entry lists;
5. `project-state.md`, if the repository structure or active entry set changes;
6. nearby entries that should link to the new page.

For ordinary content edits, do not update navigation or project state unless the edit changes structure, scope, or public entry lists.

## 7. Check consistency before committing

Before committing, check:

- the edited files still satisfy the conventions recorded in `docs/meta/`;
- all internal Markdown links point to existing files;
- navigation paths in `mkdocs.yml` match actual paths;
- front matter is present for new entries;
- no private research notes or raw scratch work were added to public pages;
- the edit does not duplicate material that should be linked instead;
- every edited math page has been fetched again from GitHub after writing and its TeX delimiters and backslashes have been inspected in the stored source;
- commands such as `\\nu`, `\\Omega`, `\\text`, `\\ge`, and `\\int` were not altered by JSON, JavaScript, shell, or API string escaping;
- when content is generated programmatically, TeX-bearing text is passed through a raw or otherwise byte-preserving string representation;
- no standalone single-dollar math delimiters remain in an entry.

## 8. Commit and report

Use focused commit messages describing the actual change. If several unrelated changes are required, split them into separate commits when practical.

In the final report, state:

- which files were created or changed;
- the substantive effect of the edit;
- the commit SHA or SHAs;
- any checks that were not run or any uncertainty that remains.
