# Independent audit request 001: BABP edge corrector

This is a bounded fresh audit, not a graduate-student development task.

Read:

- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`;
- `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`;
- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`;
- `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`;
- the primary BABP literature needed to check the historical comparison.

The central claimed project result is:

> For one-dimensional BABP in the convention where vacant sites are born at rate `lambda` per occupied neighbour and occupied sites die at rate `1` per occupied neighbour, at `lambda=1/40` there exists a bounded corrector depending on the first 10 sites behind the rightmost particle such that the generator drift of `R+phi` is uniformly at least `1033/40000000>0`. Hence the right and left edges have strictly positive outward asymptotic speeds.

Audit this independently and hostilely.

## Required checks

1. Derive the edge-window generator from the BABP dynamics without copying Student B's formula. Check every event that can alter `R+phi` and whether one unresolved exterior bit is sufficient.

2. Prove or refute the implication from uniform positive generator drift to almost-sure positive asymptotic edge speed. Check nonexplosion, jump bounds, martingale law of large numbers, and any hidden dependence on the total particle number.

3. Reproduce analytically the `k=1` feasibility threshold. Determine whether it is exactly `lambda>1/3`.

4. Run the exact certificate independently. Check the decompression/indexing, the state ordering, all 2048 `(u,z)` inequalities, and the exact minimum `1033/40000000` at `lambda=1/40`.

5. Independently solve or certify the `k=8` zero-drift threshold sufficiently accurately to decide whether `0.03461954...` is correct.

6. Historical-source audit. Using the full Sudbury (1999) paper if obtainable, determine whether the published `0.0347` threshold is in fact produced by the same finite-boundary submartingale/edge-speed mechanism and, if possible, whether the calculation corresponds literally to an eight-site window. If the full text cannot be obtained, separate what is proved from what is only strongly inferred from the title/abstract and numerical calibration.

7. Do **not** audit a stronger convergence theorem unless it follows directly from the materials. The current project explicitly does not claim that the `lambda=1/40` edge certificate by itself proves finite-seed convergence.

## Durable output

Commit the audit to

`research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

End with one of:

- `VERIFIED` for the exact project claim above;
- `REFUTED`, with the earliest failing step;
- `PARTIAL`, stating exactly which part remains unverified.

Also give a separate verdict on the historical identification with Sudbury's `0.0347` calculation.
