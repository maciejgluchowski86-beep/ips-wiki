# Project claim registry

This file is the mechanical status index for project-specific mathematical claims that appear on `main` outside the scratch research workspace.

A manuscript or note being present on `main` does not by itself make its claims established. Before relying on a project-specific theorem, check this registry and the cited audit record.

Allowed registry statuses are:

- `claimed`: there is a project proof or serious argument, but required independent verification is incomplete;
- `verified`: the claim has completed the verification required by `CHATGPT.md` for its present use;
- `canonical`: the human principal has explicitly designated the cited project source as authoritative for this result.

A `verified` entry must cite the relevant `audit-log.md` record or other durable audit record. A `canonical` entry records the principal's explicit source-precedence decision and does not imply that Claude independently checked the proof.

## Canonical patch results

### PATCH-FACTOR-001

Status: `canonical`

Claim: conditional on the successful-interaction skeleton up to a finite horizon, the patch interaction data are independent with their consistent patch laws; equivalently, the patch factorization theorem holds.

Source: `paper/sections/representation.tex`, theorem `Patch factorization`.

Basis: the principal explicitly designated `paper/` as the correct and authoritative source for the patch construction and its proofs, superseding deprecated wiki pages that still call this result conditional.

### PATCH-REP-001

Status: `canonical`

Claim: the signed monomial Feynman--Kac representation factors over patches and yields the exact patch representation of the spin-system semigroup stated as Theorem A in the paper.

Source: `paper/sections/main-results.tex` and the proof in `paper/sections/representation.tex`.

Basis: the same principal designation of `paper/` as the canonical patch source.

## Active or later project claims

None yet under the professor-and-graduate-students architecture.

When a claim is added or materially strengthened on `main`, add or update an entry here in the same commit unless an existing entry already covers the exact claim.
