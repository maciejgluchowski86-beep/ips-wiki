# Literature map

## Primary open-problem source

Frank den Hollander, *Evolution of Discordance*, Mathematical Physics, Analysis and Geometry 28 (2025), article 21, DOI `10.1007/s11040-025-09518-y`, especially Section 2.4.

The source explicitly states that it remains open to extend the regular-random-graph discordance theorems to the configuration model with unequal vertex degrees and that there is not even a conjecture there for the heterogeneous analogues of the regular diffusion constant `theta_d` and short-time profile `f_d(t)`.

This is the present source-level novelty anchor. It is not authority for what later or older literature may imply; Student E must check that independently.

## Regular-graph baseline

Luca Avena, Rangel Baldasso, Rajat Subhra Hazra, Frank den Hollander, Matteo Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, DOI `10.30757/ALEA.v21-18`, arXiv:`2209.01037`.

This supplies the regular benchmark: fixed-time profile through two-walk nonmeeting on the infinite `d`-regular tree, moderate/long-time behavior, and the random-walk meeting inputs used in that setting.

Important protocol lesson from the closed predecessor programme: read the actual proof ingredients, not only the theorem/open-problem prose. Proposition 4.1 proof (4.2), (5.5)--(5.6), and (5.8) contained an immediate variance corollary not stated by the authors.

## General finite-voter diffusion framework

Yu-Ting Chen, Jihyeok Choi, J. Theodore Cox, *On the convergence of densities of finite voter models to the Wright--Fisher diffusion*, Annales de l'Institut Henri Poincare / arXiv:`1311.5786`.

The paper develops general criteria for voter-density convergence to Wright--Fisher through meeting/mixing properties of the underlying voting kernels. Student E must determine the correct density for a nonregular undirected graph, the exact time normalization, and whether the theorem already identifies the consensus-scale limit once the stationary meeting-time asymptotics are known.

Do not assume the regular unweighted opinion density is the correct coordinate. For the vertex-rate-one voter model on an undirected heterogeneous graph the stationary random-walk measure is degree-biased.

## Directed heterogeneous comparison

Federico Capannoli, *Evolution of discordant edges in the voter model on random sparse digraphs*, EJP 30 (2025), arXiv:`2407.06318`.

Luca Avena, Federico Capannoli, Rajat Subhra Hazra, Diego Garlaschelli, *Voter model on heterogeneous directed networks*, arXiv:`2506.12169`.

These works treat directed heterogeneous configuration models and related consensus/discordance quantities. They are useful for techniques and candidate forms but do not settle the undirected problem singled out by den Hollander (2025).

The 2025 directed-network work reports numerical evidence for Wright--Fisher behavior also in some undirected ensembles; this is heuristic evidence only for the present target unless a theorem there directly applies.

## Older heterogeneous-network heuristics

V. Sood, S. Redner, *Voter Model on Heterogeneous Graphs*, arXiv:`cond-mat/0412599`, and related statistical-physics work give mean-field predictions for consensus times on heterogeneous networks, typically involving degree moments.

These are important predecessor heuristics. Student E must distinguish rigorous configuration-model asymptotics from heterogeneous mean-field approximations and must not promote a moment formula merely because it matches simulations or physics predictions.

## Classical graphical/partition background

Voter/coalescing-walk duality and the ancestral partition are classical. Any contribution claim must concern the heterogeneous asymptotic identification, not the existence of the genealogy itself.

## Current literature questions

1. Is `E_{pi tensor pi} tau_meet / n` already known to converge on bounded-degree undirected configuration models, and with what constant?
2. Is a Wright--Fisher limit for the degree-weighted voter density already an immediate application of a general theorem once that meeting constant is supplied?
3. Has fixed-time discordance on undirected configuration models already been treated under terminology such as interface density, active links, boundary size, or edge disagreement?
4. What is the exact edge-rooted local weak limit relevant to a uniformly sampled edge, and what changed rooting is induced by the bracket weight `d_x+d_y`?
5. Does one scalar local nonmeeting profile control both raw discordance and the diffusion bracket, or are two distinct degree-biased profiles unavoidable?

These are assignments, not established gaps.
