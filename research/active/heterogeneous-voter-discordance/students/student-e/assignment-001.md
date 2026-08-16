# Graduate Student E assignment 001: heterogeneous voter constants and local-profile reduction

Work on branch `research/heterogeneous-voter-discordance`.

Read first:

- root `project-state.md`;
- `CHATGPT.md`, especially the standing novelty standard;
- `research/active/heterogeneous-voter-discordance/state.md`;
- `research/active/heterogeneous-voter-discordance/proof-spine.md`;
- `research/active/heterogeneous-voter-discordance/literature.md`;
- Student A's earlier candidate analysis at `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md` on branch `research/babp-finite-seed`;
- Frank den Hollander, *Evolution of Discordance* (2025), especially the regular results and Section 2.4 open problem;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), *Discordant edges for the voter model on regular random graphs*;
- Chen--Choi--Cox, *On the convergence of densities of finite voter models to the Wright--Fisher diffusion*;
- the most relevant rigorous work you can identify on meeting/coalescence times and voter models on undirected configuration models;
- directed heterogeneous papers only where they clarify which steps cease to work in the undirected model.

Do not infer novelty merely from den Hollander's open-problem statement. The immediately preceding programme failed novelty audit because the target source itself already contained an unstated short corollary. Inspect proof ingredients and general theorems before treating any candidate formula as new.

## Model for the first bounded programme

Take an undirected configuration model on `n` vertices with empirical degree distribution converging to a fixed law `p` supported on

$$
\{3,4,\dots,D\}
$$

for fixed finite `D`. State carefully whether you work with the pairing multigraph or condition on simplicity; distinguish statements that are insensitive to that choice.

The voter model has rate-one clocks at vertices; when `x` rings it copies a uniformly chosen neighbour. Initial opinions are i.i.d. Bernoulli(`u`).

## Goal of this assignment

Determine the **correct theorem statement to attack** before attempting its proof. In particular, derive the heterogeneous analogues of the regular short-time profile and consensus-scale constant as far as existing mathematics permits, and isolate one genuinely open interface.

A useful assignment may end by showing that part of the apparent open problem is already an immediate consequence of prior work. That is a successful outcome.

## Task A: source and closest-prior-work audit

1. Transcribe precisely what den Hollander's 2025 Theorems 2.1--2.2 assert in the regular case and exactly what Section 2.4 calls open.
2. Search predecessor and successor literature under alternate terminology:
   - voter model on configuration models / random graphs with given degrees;
   - consensus time, coalescing random walks, meeting time;
   - active links, discordant/disagreeing edges, interface density, edge boundary;
   - finite voter Wright--Fisher limits with nonuniform stationary measure;
   - locally tree-like unimodular/random rooted graphs.
3. Determine whether a general theorem already supplies the consensus-scale Wright--Fisher limit after verifying standard mixing/meeting hypotheses. If yes, isolate exactly what constant remains unidentified rather than reproving the general theorem.
4. Determine whether fixed-time expected discordance on an undirected configuration model is already in the literature, perhaps without being advertised as the den Hollander open problem.

Use primary sources and theorem/equation numbers. Do not count physics mean-field predictions as rigorous prior art, but record them as conjectural benchmarks.

## Task B: exact conserved coordinate and bracket

Re-derive from the generator. With `d_x` the degree, `m=|E|`, and

$$
\pi_x=\frac{d_x}{2m},
$$

check that

$$
B_t^\pi=\sum_x\pi_x\eta_t(x)
$$

is the martingale conserved density.

If `k_x` is the number of neighbours disagreeing with `x`, compute the predictable quadratic-variation density with all constants. The current Professor calculation is

$$
\Gamma(B^\pi)(\eta)
=\frac1{4m^2}\sum_xd_xk_x
=\frac1{4m^2}
\sum_{\{x,y\}\in E:\eta_x\ne\eta_y}(d_x+d_y).
\tag{B1}
$$

Independently verify or correct (B1), then match its normalization to the exact finite-voter Wright--Fisher theorem you intend to use.

Explain precisely why the raw discordant-edge density and the bracket-weighted discordance coincide up to a constant in the regular case but not in general.

## Task C: derive the relevant local weak rootings

Do not write merely "size-biased Galton--Watson tree". Specify the law.

For limiting vertex-degree law `p`, derive the rooted local weak law seen from:

1. a uniformly chosen **unoriented edge** and its two endpoints;
2. an edge sampled with weight `d_x+d_y`, as induced by (B1);
3. a stationary random-walk starting vertex `pi`;
4. any pair/rooting actually required for the stationary meeting-time constant.

State whether the two endpoint degrees are asymptotically independent with the size-biased law and what offspring distribution is seen beyond the root edge. Account for conditioning on simplicity if it matters.

## Task D: candidate short-time profiles

For a fixed edge `{x,y}`, verify the exact voter-duality formula

$$
\mathbf P_u^G(\eta_t(x)\ne\eta_t(y))
=2u(1-u)\mathbf P_{x,y}^G(\tau_{\rm meet}>t).
\tag{D1}
$$

Use the rootings from Task C to formulate, with no unspecified bias, the candidate limiting profile for:

- raw discordant-edge density, call it `f_p^raw(t)`;
- bracket-weighted discordance, call it `f_p^br(t)`.

Prove that both reduce to the known regular profile when `p=delta_d`.

Then answer the structural question:

> Are `f_p^raw` and `f_p^br` the same scalar profile up to a deterministic moment factor, or do heterogeneity and the edge reweighting force genuinely different time-dependent profiles?

A proof that they differ for some nondegenerate bounded degree law would be useful structural information, but a single numerical example is not enough. Seek an analytic identity or obstruction.

## Task E: consensus-scale meeting constant

Let

$$
\gamma_n(G)=\mathbf E_{\pi\otimes\pi}^G[\tau_{\rm meet}].
$$

Determine what is rigorously known for bounded-degree undirected configuration models.

1. Is `gamma_n/n` already known to converge in probability to a deterministic constant?
2. If so, give the exact formula and source, and check all assumptions for the present degree laws.
3. If not, derive a credible candidate using the local tree/Green-function picture and state exactly which interchange or mixing estimate is missing.
4. Relate the constant to the Wright--Fisher coefficient under the exact clock normalization. Do not import a regular formula by replacing `d` with `E D`.
5. Compare carefully with heterogeneous mean-field predictions such as `N mu_1^2/mu_2` and explain whether they match, contradict, or concern a different normalization/regime.

## Task F: choose one theorem-scale next edge

End by selecting **one** of the following kinds of outputs, or a more precise equivalent:

- a source-grounded theorem statement for fixed-time raw and bracket-weighted profile convergence whose only missing ingredient is explicitly named;
- a source-grounded theorem statement identifying `gamma_n/n` and the Wright--Fisher constant, with one explicit missing random-walk estimate;
- a proof that one of these objects is already prior art, leaving a strictly narrower genuine open problem;
- a structural obstruction showing that the regular one-profile/one-constant picture cannot extend literally.

Do not end with a list of five speculative routes.

## Novelty guardrail

The following do **not** count as a project result by themselves:

- evaluating a candidate formula for one degree law such as `{3,4}`;
- replacing `d` by a degree moment in a known heuristic;
- checking a larger finite graph numerically;
- restating a general voter theorem after routine verification of hypotheses;
- giving a better numerical approximation to a meeting constant.

A useful first assignment may be entirely diagnostic. The eventual programme needs a new identification/proof of the heterogeneous profile or constant, or a genuine structural theorem about why the regular picture splits.

## Durable output

Commit the report to

`research/active/heterogeneous-voter-discordance/students/student-e/001-heterogeneous-constants.md`

and any exact symbolic/numerical verifier under the same directory.

End with exactly one recommendation:

- `develop local-profile theorem`;
- `meeting constant already prior art — isolate remaining open interface`;
- `heterogeneous one-constant picture structurally false — reformulate target`;
- `target already substantially solved — close`.

Do not edit `main`.
