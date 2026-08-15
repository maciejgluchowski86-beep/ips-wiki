# Graduate Student B assignment 002: edge speed to finite-seed convergence

Work on branch `research/babp-finite-seed`.

Read first:

- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`;
- your `001-threshold-and-dfp.md` and `edge-corrector-certificate.py`;
- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`.

The edge-corrector result at `lambda=1/40` is now a claimed project result pending fresh independent audit. Do not strengthen its status yourself.

Your next task is the theorem bridge. Do **not** assume that positive outward edge speed already implies local convergence.

## Target for this assignment

Determine whether the following implication is valid for one-dimensional BABP from a finite nonempty seed:

> strictly positive right-edge speed and strictly negative left-edge speed, together with the known invariant-law classification and available all-parameter growth facts, imply local convergence to the nontrivial Bernoulli equilibrium.

First work at the single concrete parameter

```text
lambda = 1/40.
```

If the implication is valid without another parameter-dependent input, prove it carefully. Then the current certificate immediately yields a genuine improvement of the finite-seed convergence theorem.

If it is false or incomplete, identify the exact additional statement needed.

## 1. Reconstruct the historical bridge as far as possible

Obtain and read the full relevant arguments of:

- Mountford (1993), *A coupling of finite particle systems*;
- Sudbury (1999), *Hunting submartingales in the jumping voter model and the biased annihilating branching process*;
- Neuhauser--Sudbury (1993) and Sudbury (1997) where needed.

Use any legitimate accessible copy you can find. If a publisher interface blocks the paper, search repositories, author pages, scans, citing papers, and theorem restatements. Do not infer an internal lemma merely from an abstract.

Produce a dependency map that distinguishes:

- subsequential-limit invariance;
- classification of invariant laws;
- exclusion of the empty invariant component;
- edge-speed/spreading input;
- any local recurrence, coupling, parity, or occupation estimate;
- any second parameter restriction.

State exactly where `lambda>0.0347` is used.

## 2. Reprove the bridge directly if the literature remains inaccessible

A likely skeleton is:

1. every subsequential local weak limit from a finite initial configuration is invariant;
2. every invariant law in one dimension is a mixture of the empty law and Bernoulli equilibrium;
3. prove that the empty component has coefficient zero.

The third point is the load-bearing one. Positive edge speed only says the hull expands; it does not by itself rule out particles escaping from every fixed window.

So derive the strongest statement actually implied by the edge corrector and combine it with all-parameter cardinality growth. Check whether these facts force a positive lower bound on local occupation, recurrence of particles to the origin, or another criterion excluding the empty subsequential limit.

If not, isolate a precise missing lemma. Examples of acceptable forms are:

```text
For every finite nonempty initial B and every lambda>0 satisfying the edge-corrector condition,
liminf_{t->infinity} P_B(B(t) cap [-M,M] != empty) > 0
```

for some fixed `M`, or a stronger return/coupling statement. Do not adopt this example unless it is actually sufficient.

## 3. Keep `lambda=1/40` separate from the all-parameter goal

There are now two potential results:

A. **near-term theorem improvement:** finite-seed convergence at `lambda=1/40`, or on an explicit interval below `0.0347`;

B. **main theorem:** finite-seed convergence for every `lambda>0`.

Do not let the all-parameter ambition obscure A. If the historical bridge uses only positive edge speed, write the `lambda=1/40` theorem proof first and say exactly how far the certificate extends numerically.

Only after the bridge is settled should you begin the next analytic question

```text
lambda_k -> 0
```

or an explicit family of finite-window correctors.

## 4. Check whether the finite-window corrector gives more than speed

The corrector is a function of the environment seen from the edge. Investigate whether its construction or the associated finite-state chain yields a recurrence/minorization fact behind the edge that could supply the missing local statement.

This is secondary to reconstructing the known proof, but it may matter if positive speed alone is insufficient.

Do not return to DFP basis changes unless the bridge itself forces that route.

## Durable output

Commit the decisive mathematics to

`research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`.

If you obtain full copies of historically inaccessible papers, record precise theorem/lemma/page references in the note, but do not commit copyrighted PDFs unless the repository policy explicitly permits it.

End with a short handoff stating one of:

- `bridge proved; lambda=1/40 convergence follows`;
- `bridge requires Lemma X`, with Lemma X stated precisely;
- `edge speed is not the historical load-bearing input after all`, with the exact correction.
