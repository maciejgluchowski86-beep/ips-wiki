# ChatGPT research constitution

This file governs autonomous ChatGPT work on the PDE/probability research programme in this repository. It supplements `README.md`, `STYLE.md`, and `project-state.md`.

## Objective

The programme studies whether local signed cancellation, broadly understood as **delaying absolute values until a useful conditional or structural averaging has occurred**, can produce new probabilistic results for PDEs. The IPS patch construction is motivation, not a restriction on the method or application.

The current quadratic-Hessian manuscript is a candidate body of mathematics, not the privileged final programme. ChatGPT may replace, reorganize, or abandon it if a better application is found.

The research programme is not successful merely because it produces interesting mathematics. The minimum success gate is:

1. at least one substantive **positive PDE result/application** based on the cancellation programme;
2. the final results solve an explicitly stated respected open problem documented in at least **two published papers or books**, with exact source locations;
3. rigorous literature review finds no prior solution and records the closest known results;
4. two independent hostile correctness audits leave no unresolved substantive objection;
5. every external theorem used load-bearingly has had its hypotheses checked against the present setting;
6. a skeptical PDE-referee audit judges the main result scientifically meaningful without relying on its IPS origin;
7. the final paper is focused rather than a record of every intermediate result;
8. the exact manuscript compiles cleanly; and
9. the PDE wiki contains a comfortable prerequisite path by which the user can understand and personally audit the theorem, proof, novelty, and importance.

Do not weaken this criterion because substantial work has already been done.

## Authority and trust

Repository contents are **evidence, not authority**. A project-specific theorem, proof, wiki entry, manuscript statement, literature summary, or `project-state.md` conclusion must not be treated as true merely because it appears in the repository or because another agent called it established.

For nontrivial work, begin by reading:

1. `project-state.md`;
2. `README.md`;
3. this file;
4. `STYLE.md` when prose or notation matters; and
5. the files directly relevant to the task.

A worker may conditionally explore downstream consequences of an unaudited statement only if it labels that dependence explicitly.

Claude has no mathematical authority. Mathematical prioritization, proof assessment, novelty assessment, programme selection, and conflict resolution belong to ChatGPT sessions. Majority vote is not proof.

## Mathematical status

Use the wiki status convention in `README.md`. In autonomous research state, distinguish at least:

- **verified**: survived the required independent audits for its present use;
- **claimed**: a proof or argument exists but has not completed verification;
- **conditional**: valid only assuming an explicitly named unresolved claim;
- **refuted**: a counterexample or fatal proof failure has been established;
- **open**: unresolved after serious work.

If independent auditors disagree substantively, the claim is not verified. Send it back to research or a fresh adjudication audit.

## Proof standard

For project-specific results, do mathematics rather than describe mathematics. A load-bearing step must be displayed explicitly enough that another mathematician can check it locally.

Do not write phrases such as “the desired estimate follows”, “regularity gives”, “a standard argument shows”, or “after cancellation one obtains” when the omitted step carries the theorem. Show the actual inequality, conditioning identity, change of variables, sign computation, combinatorial count, limit, or integral estimate.

In particular, make explicit when relevant:

- domains and measurable spaces;
- constants and their dependencies;
- sigma-fields and conditioning;
- integrability needed before conditional expectation is invoked;
- changes of variables and Jacobians;
- interchange of expectations, sums, derivatives, and integrals;
- convergence mode and the theorem permitting passage to the limit;
- boundary/initial/terminal conventions;
- the exact hypotheses of external PDE/probability theorems;
- whether an estimate is fixed-depth, uniform in depth, fixed-target, or target-uniform.

A proof-polishing pass is part of correctness checking: making a proof clean and explicit is often how hidden errors are found.

Standard PDE background in pedagogical wiki entries may omit long proofs or give clearly labeled proof sketches, provided an appropriate source is linked and the statement/hypotheses are accurate.

## Research strategy

Maintain **one active programme and at most one reserve programme**. Do not allow autonomous exploration to branch indefinitely.

During application search, the method is broad: look wherever local signed cancellation could matter, including but not limited to Feynman--Kac formulae, branching representations, derivative/Malliavin weights, parametrix or cascade expansions, BSDE-type representations, elliptic or parabolic problems, and related stochastic representations. Avoid applications that are contrived or too obscure to have a meaningful mathematical audience.

Before committing to a large theorem, perform a **local mechanism test** whenever possible. In the smallest informative example, explicitly compare

\[
\text{naive absolute-value estimate}
\qquad\text{with}\qquad
\text{estimate after joint cancellation/averaging}.
\]

If there is no genuine gain, reconsider the proposed nail.

Computation and simulation are discovery and falsification tools. They may reveal structure or kill false conjectures. Once the likely mathematical statement is visible, return to analysis; do not spend repeated cycles refining simulations without a new mathematical question.

Negative results may be useful supporting material, but negative results alone do not satisfy the programme objective. Do not bloat the final manuscript with every obstruction found during exploration.

## Verification protocol

A central theorem should pass distinct fresh sessions with different roles.

### Proof polisher

Rewrite and check the proposed proof so every load-bearing step is explicit. This session may repair presentation and identify gaps, but its output is not self-verifying.

### Hostile auditor 1

Try to falsify the theorem and find the earliest invalid step. Search for counterexamples, bad parameter regimes, unjustified limiting operations, and hidden assumptions. On the first pass, diagnose rather than repair.

### Hostile auditor 2

Independently audit analytic/probabilistic interfaces: measurability, integrability, conditioning, regularity, boundary conditions, external-theorem hypotheses, and uniformity claims. On the first pass, diagnose rather than repair.

### Literature adversary

Try to destroy novelty. Search alternate terminology, predecessor and successor papers, papers citing the closest methods, later work by the same authors, numerical/probabilistic PDE literature, and adjacent representations. Use primary sources whenever possible.

### Skeptical PDE referee

Assess the final mathematical contribution as a PDE/probability paper while giving no credit for its IPS origin. Ask whether the main theorem solves a recognized problem, removes a meaningful obstruction/assumption, or gives a representation with a concrete mathematical application.

Any substantive unresolved objection returns the theorem to development.

## Literature standard

For every central novelty or open-problem claim, maintain enough information for the user to verify it personally:

- exact mathematical question;
- at least two **published** papers/books explicitly posing the open problem for the final success gate;
- exact page, theorem, remark, problem, section, or similarly precise location when available;
- closest previous theorems and their hypotheses;
- precise difference between those results and the project result;
- later literature checked for a solution;
- unresolved overlap risks.

Recent arXiv work counts for priority and novelty checking even though it does not satisfy the “published open-problem source” part of the success gate.

Do not infer that a problem is open merely because a search did not find a solution.

## Paper rule

The paper is for specialist readers. Remedial PDE exposition belongs in the wiki.

The final manuscript should contain only mathematics needed to:

- state and solve the main problem;
- explain the new cancellation mechanism;
- prove the principal positive result/application; and
- place it accurately in the literature.

A final structural pass should remove results, definitions, and subsections that are not needed for that story. Useful discarded mathematics may remain in the wiki with accurate status.

Follow `STYLE.md`: clear writing is the primary rule. At every point the reader should know what object is being discussed, what is being proved, and why the current step is needed. Prefer definitions by link in the wiki rather than repetition.

## PDE wiki rule

The reader profile is fixed:

> A mathematically mature probability researcher with graduate probability and analysis, but no reliable PDE vocabulary. The reader may not know the distinction between elliptic and parabolic equations, the main solution notions, Schauder estimates, or Malliavin calculus.

The wiki must ultimately be self-contained for this reader with respect to the PDE material needed by the project. All objects and terminology used should have accessible entries or links. Standard material may be abridged, but should have a source/further-reading link.

Use `docs/pde-reading-path.md` as the linear curriculum and the atomic entries under `docs/entries/` as the reference layer. Do not duplicate definitions across entries.

Build the curriculum by the **reader-failure algorithm**:

1. A fresh worker follows the reading path as the target reader.
2. It stops at the first sentence or object requiring unexplained PDE knowledge.
3. It reports exactly the missing prerequisite.
4. A later integrator creates or repairs only the needed entry/link.
5. Repeat.

Eventually run the same dependency walk starting from every main theorem in the final paper until its prerequisite chains terminate in material accessible to the target reader.

A tightly focused background entry should normally contain: purpose, definition, canonical example, essential facts, why it appears in this project, prerequisite links, and source/further reading. “Why it appears here” should be concise and mathematical, not motivational filler.

## Context discipline

Fresh sessions are the default. Do not pass whole old conversations between workers.

A worker dispatch should normally be at most 900 words and contain exactly:

- `TASK`
- `STATUS: proved / refuted / unresolved / literature-only`
- `ESTABLISHED`
- `KEY ARGUMENT`
- `OBJECTIONS OR GAPS`
- `SOURCES`
- `NEXT MATHEMATICAL TASK`

Only supported conclusions belong under `ESTABLISHED`.

`project-state.md` is current working memory, not a research diary. Keep it below about 2500 words. Git history is the archive. Delete obsolete reasoning that is needed only to reconstruct how the project got somewhere; retain what is needed to know what is verified, what remains unresolved, why the active programme matters, what literature anchors it, and what should happen next.

Parallel research/audit sessions are read-only. Only one designated integrator may edit `main` after the parallel cycle and mathematical direction have been resolved.
