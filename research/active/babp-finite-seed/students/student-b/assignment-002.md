# Graduate Student B assignment 002: ballistic edge bounds to finite-seed convergence

Work on branch `research/babp-finite-seed`.

Read first:

- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`;
- your `001-threshold-and-dfp.md` and `edge-corrector-certificate.py`;
- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

## Audit correction to the assignment language

The hostile audit has completed and `BABP-EDGE-001` is now `verified` with a narrower theorem boundary.

At `lambda=1/40` the corrector proves

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge \frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le -\frac{1033}{40000000}
\quad\text{a.s.}
$$

for every finite nonempty initial configuration. Do **not** assume that either ratio has a limit unless you separately prove or cite speed existence.

The audit also found that literal identity of the present `k=8` LP with Sudbury's internal 1999 computation is not source-verified. Treat the numerical calibrations as strong mechanism-level evidence, not as a line-by-line historical fact.

Your next task remains the theorem bridge. Do **not** assume that the verified ballistic hull bounds already imply local convergence.

## Target for this assignment

Determine whether the following implication is valid for one-dimensional BABP from a finite nonempty seed:

> the verified strictly outward `liminf/limsup` ballistic edge bounds, together with the known invariant-law classification and available all-parameter growth facts, imply local convergence to the nontrivial Bernoulli equilibrium.

First work at the single concrete parameter

```text
lambda = 1/40.
```

If the implication is valid without another parameter-dependent input, prove it carefully. Then the current verified certificate supplies the missing edge input for a genuine improvement of the finite-seed convergence theorem.

If it is false or incomplete, identify the exact additional statement needed.

## 1. Reconstruct the historical bridge as far as possible

Obtain and read the full relevant arguments of:

- Mountford (1993), *A coupling of finite particle systems*;
- Sudbury (1999), *Hunting submartingales in the jumping voter model and the biased annihilating branching process*;
- Neuhauser--Sudbury (1993) and Sudbury (1997) where needed.

Use any legitimate accessible copy you can find. If a publisher interface blocks the paper, search repositories, author pages, scans, citing papers, and theorem restatements. Do not infer an internal lemma merely from an abstract.

The full Sudbury text is worth pursuing because it may contain the bridge. It is **not** necessary merely to prove that Sudbury literally used the same `k=8` LP. Historical provenance is secondary to the theorem dependency.

Produce a dependency map that distinguishes:

- subsequential-limit invariance;
- classification of invariant laws;
- exclusion of the empty invariant component;
- ballistic-edge/spreading input;
- any local recurrence, coupling, parity, or occupation estimate;
- any second parameter restriction.

State exactly where `lambda>0.0347` is used if the source permits that statement. If the full text remains unavailable, mark the provenance gap rather than guessing.

## 2. Reprove the bridge directly if the literature remains inaccessible

A likely skeleton is:

1. every subsequential local weak limit from a finite initial configuration is invariant;
2. every invariant law in one dimension is a mixture of the empty law and Bernoulli equilibrium;
3. prove that the empty component has coefficient zero.

The third point is the load-bearing one. The verified ballistic edge bounds only say the hull expands linearly; they do not by themselves rule out particles escaping from every fixed window.

So derive the strongest statement actually implied by the edge corrector and combine it with all-parameter cardinality growth. Check whether these facts force a positive lower bound on local occupation, recurrence of particles to the origin, or another criterion excluding the empty subsequential limit.

If not, isolate a precise missing lemma. An acceptable form, if genuinely sufficient, would be something like

```text
For every finite nonempty initial B and every lambda satisfying the edge-corrector condition,
liminf_{t->infinity} P_B(B(t) cap [-M,M] != empty) > 0
```

for some fixed `M`, or a stronger return/coupling statement. Do not adopt this example unless you prove that it closes the mixture coefficient.

## 3. Keep `lambda=1/40` separate from the all-parameter goal

There are two potential results:

A. **near-term theorem improvement:** finite-seed convergence at `lambda=1/40`, or on an explicit interval below `0.0347`;

B. **main theorem:** finite-seed convergence for every `lambda>0`.

Do not let the all-parameter ambition obscure A. If the bridge uses only the verified ballistic edge bounds and parameter-free literature inputs, write the `lambda=1/40` theorem proof first.

Only after the bridge is settled should you begin the next analytic question

```text
lambda_k -> 0
```

or an explicit family of finite-window correctors.

## 4. Check whether the finite-window corrector gives more than the ballistic bound

The corrector is a function of the environment seen from the edge. Investigate whether its construction or the associated finite-state chain yields a recurrence/minorization fact behind the edge that could supply the missing local statement.

This is secondary to reconstructing the known proof, but it may matter if hull expansion alone is insufficient.

Do not return to DFP basis changes unless the bridge itself forces that route.

## Durable output

Commit the decisive mathematics to

`research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`.

The existing output filename may remain unchanged for continuity even though the precise current phrase is “ballistic edge bounds”.

If you obtain full copies of historically inaccessible papers, record precise theorem/lemma/page references in the note, but do not commit copyrighted PDFs unless the repository policy explicitly permits it.

End with a short handoff stating one of:

- `bridge proved; lambda=1/40 convergence follows`;
- `bridge requires Lemma X`, with Lemma X stated precisely;
- `the verified ballistic edge bound is not the historical load-bearing input after all`, with the exact correction.
