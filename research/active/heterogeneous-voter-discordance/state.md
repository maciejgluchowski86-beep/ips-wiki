# Programme state

## Direction

Title: voter-model discordance on undirected heterogeneous configuration models

Branch: `research/heterogeneous-voter-discordance`

Professor lineage: persistent ChatGPT Professor

Graduate Student E: new persistent student for this direction

Graduate Students A, B, C, D: idle with prior lineages

Workspace: `research/active/heterogeneous-voter-discordance/`

Latest group meeting: none yet

## Target

Extend the regular-random-graph discordance theory to an **undirected configuration model with unequal degrees**.

The initial bounded version is deliberately controlled: empirical degree distributions converge to a fixed probability law `p` supported on

$$
\{3,4,\dots,D\}
$$

for fixed finite `D`, and the configuration model is conditioned to be simple when needed. The voter model updates each vertex at rate one and copies a uniformly chosen neighbour. Initial opinions are i.i.d. Bernoulli(`u`).

The programme seeks the correct analogues of the regular-graph short/moderate-time discordance profile and consensus-time diffusion constant, and then a theorem proving them on this bounded heterogeneous ensemble.

## Open-status evidence

Frank den Hollander, *Evolution of Discordance* (2025), Section 2.4, states explicitly that extending the regular-graph results to the configuration model with unequal vertex degrees remains open and that there is not even a conjecture for the analogues of `theta_d` and `f_d(t)`.

Directed heterogeneous configuration models have been treated separately; that does not resolve the undirected problem.

## First structural distinction from the regular case

For a fixed undirected graph with degrees `d_x`, the conserved voter coordinate is the degree-weighted density

$$
B^\pi(\eta)=\sum_x\pi_x\eta_x
=\frac1{2m}\sum_x d_x\eta_x,
\qquad
\pi_x=\frac{d_x}{2m},
$$

not the unweighted density. Indeed `L B^pi=0`.

If `k_x` is the number of neighbours disagreeing with `x`, then the predictable bracket density of this martingale is

$$
\Gamma(B^\pi)(\eta)
=\frac1{4m^2}\sum_x d_x k_x
=\frac1{4m^2}
\sum_{\{x,y\}\in E:\eta_x\ne\eta_y}(d_x+d_y).
$$

Thus on a heterogeneous graph the diffusion-scale observable is a **degree-weighted discordant-edge sum**, not simply the number of discordant edges. The regular case hides this distinction because all degrees are equal.

This is the first proof-spine edge: identify the correct local-limit profiles and constants for both the raw discordance and the bracket-weighted discordance before attempting a global theorem.

## Candidate local object

For Bernoulli(`u`) initial opinions and a fixed edge `{x,y}`, voter duality gives

$$
\mathbf P_u(\eta_t(x)\ne\eta_t(y))
=2u(1-u)\,\mathbf P_{x,y}(\tau_{\rm meet}>t).
$$

A uniformly sampled configuration-model edge is locally seen as an edge-rooted size-biased Galton--Watson tree. This suggests a short-time raw-discordance profile obtained by averaging the nonmeeting probability of two rate-one random walks started from the two root-edge endpoints. A different degree bias enters the bracket-weighted observable.

These are candidate definitions only until Student E derives the exact rooting laws and checks predecessor literature.

## First assignment

Graduate Student E must source-check the open problem and derive the exact heterogeneous bookkeeping before trying to prove an asymptotic theorem. In particular:

- identify the precise local weak limits under the rootings relevant to raw and weighted discordance;
- derive candidate profile functions and their regular-graph reduction;
- determine what is already known about stationary two-walk meeting times and Wright--Fisher limits on bounded-degree undirected configuration models;
- isolate the single genuinely open estimate or identification that would convert those candidates into a theorem.

Assignment: `students/student-e/assignment-001.md`.

## Novelty discipline

A special-case computation for one two-point degree law, a numerical constant, or a routine invocation of a general existing theorem does not count as a project result. The first assignment is diagnostic. A qualifying eventual result must identify/prove the heterogeneous constants/profile or establish a structural obstruction not already encoded in prior configuration-model voter theory.

## Direction

`continue`.
