# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical paper lives under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of FA-1f proof search unless explicitly requested.

The paper is *Patch representations and convergence for facilitated spin systems*. Its current theorem order is: patch representation, coefficient/centered-moment comparison, then common invariant-limit theorem. Shared notation and theorem environments are in `paper/preamble.tex`; paper style conventions are in `STYLE.md`.

## Current FA-1f Bernoulli-quench problem

Target: prove for one-dimensional two-sided OR-rate FA-1f that

$$
\mu_{q_0}P_t\Longrightarrow\mu_q
$$

for every equilibrium vacancy density `q>0` and every initial Bernoulli vacancy density `q_0>0`.

The positive centered dual already proves the range `q_0<2q`. The unresolved range has `q_0>=2q`, hence `q_0>=q`.

Stationary-limit classification reduces the remaining problem to excluding the fully occupied trap component. Two sufficient terminal targets are:

1. the sharp density inequality `P(eta_t(0)=0) >= q`, or
2. vacancy-gap tightness, equivalently that the probability of a large occupied interval around the origin tends uniformly to zero.

The current route audit is `docs/entries/fa-1f-bernoulli-convergence-route-audit.md`.

## Primary route: terminal-singleton discrepancy zipper

The primary target is the single marked discrepancy

$$
D_0(\varnothing,t)=p-\mathbb E_{\mu_{q_0}}[\eta_0(t)]\ge0.
$$

Updates touching the marked zipper satisfy exact positive local identities; only separated background chronology is signed. The intended proof reveals a two-sided zipper plus predecessor scaffold, leaves the complete chronology in detached regions hidden, and integrates each region either as a nonnegative bulk patch or by undoing the signed dual to an ordinary confined FA semigroup.

The missing theorem is a **two-sided zipper factorization** with the correct Poisson conditional law. The older one-sided barrier--scaffold construction is only a template; it cannot be quoted directly for two-sided FA geometry.

Relevant files:

- `docs/entries/discrepancy-zipper-route-for-fa-1f.md`
- `docs/entries/undoing-duality-under-confined-interactions.md`
- `docs/entries/patch-factorization.md`
- `docs/entries/patch-positivity-for-fa-1f.md`

Work on this route until the factorization is proved or a structural counterexample shows it cannot have the required terminal geometry.

## Secondary route: all-density analogue of the front wake

The literature gives a clear benchmark. For one-dimensional East at every `q>0`, the process seen from the front has a unique invariant law whose tail is exponentially close in total variation to the Bernoulli equilibrium. The proof uses a distinguished zero: conditional on its entire monotone path, the swept region behind it is exactly at equilibrium. This exact conditional property is orientation-specific.

For high-vacancy FA-1f, Blondel--Deshayes--Toninelli prove the analogous front invariant-law theorem by replacing the distinguished-zero argument with two separate inputs: a threshold-contact-process comparison that generates many vacancies behind the front, and a non-equilibrium relaxation estimate once vacancy spacing is controlled. See `docs/entries/front-growth-and-vacancy-density-for-fa-1f.md`.

The all-density program should preserve this separation:

1. **vacancy production:** prove an all-density zeros lemma/gap-tightness statement behind a mobile vacancy/front;
2. **regional relaxation:** given a suitable nonempty moving-boundary region, prove loss of dependence on its incoming configuration.

The local chronology-averaging mechanism for step 1 is established:

- `docs/entries/moving-edge-cbsep-resampling-for-fa-1f.md`
- `docs/entries/iterated-moving-edge-splitting-for-fa-1f.md`
- `docs/entries/separated-vacancy-reproduction-for-fa-1f.md`

These give random-time local reproduction with exponential time and spatial tails, uniformly over exterior FA history. The unresolved issue is deterministic-time global bookkeeping: distinct descendants can collide, and random-time daughters do not yet give a standard oriented-percolation block kernel.

For step 2, modern one-dimensional general-KCM bisection gives useful finite-volume input. On an arbitrary irreducible component,

$$
T_{\rm rel}\le (2/q)^{C\log\min\{|\Lambda|,2/q\}},
$$

so at fixed `q` the relaxation-time bound is uniform in interval length once the interval is large. The obstacle is therefore not a volume-diverging spectral gap. It is obtaining a conditional moving/nonempty region whose internal graphical randomness has not been biased by the path used to select its vacancy boundary.

The tagged-vacancy bridge and vacancy-lens factorizations are possible replacements for East orientation: conditional on a path plus auxiliary bridge variables, they retain the interior chronology as a positive regional transfer operator. A useful stronger target is an approximate distinguished-boundary estimate showing that the normalized moving-boundary transfer operator loses dependence on initial data a distance `L` behind the boundary.

All-density finite-seed linear span is already known from Martinelli--Shapira--Toninelli, but it does not imply vacancy-gap tightness and cannot be inserted by deleting exterior vacancies because FA-1f is not attractive.

## Supporting identities, not standalone proof routes

- `docs/entries/fa-1f-babp-xor-decomposition.md`: exact `L_FA = 1/2 L_BABP + L_xor`; the residual layer transports domain walls, but BABP quasi-duality does not remain positive after adding it.
- `docs/entries/vacancy-lens-factorization-for-fa-1f.md`: exact prescribed-lens factorization; useful for replacing East's orientation-specific conditional independence, but no proved contraction of the moving lens operator.
- `docs/entries/chronology-averaged-sign-route-for-fa-1f.md`: exact centered-dual formulas and diagnostics; the rooted punctured-positivity conjecture is no longer the main proof target.

## Retired directions

Do not restart these without genuinely new input:

- fixed-count or deterministic-word positivity;
- coefficientwise shuffle/punctured polynomial positivity;
- broad multi-discrepancy or negative-association cones;
- direct stochastic attractiveness/domination;
- microscopic contact-process domination at all `q`;
- the exact FA--reaction-diffusion similarity transform, which applies to the additive-rate/BABP convention rather than OR-rate FA-1f;
- inferring vacancy-gap tightness from front speed alone;
- a direct transplantation of the East distinguished-zero identity to FA-1f: conditioning on an FA vacancy path reads clocks on both sides and does not leave an exact product-equilibrium wake.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic claims as theorems.
- Use `0` as the facilitating state in KCSM entries, with vacancy density `q` and `p=1-q`.
- Prefer complete chronology averages, regional semigroups, or proved stopping-time kernels over deterministic update-word inequalities.
- Do not add new positivity cones merely because finite computations suggest them; identify the mechanism that averages update order first.
