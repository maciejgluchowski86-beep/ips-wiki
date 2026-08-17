# Applicability assessment protocol

Date: 2026-08-17

This protocol governs the phase **after wave seven is source-audited and integrated**. Wave seven is the final breadth-collection wave. The final method inventory is then frozen for this assessment; no new generic literature sweep is part of the phase.

The principal's new question is not which methods are important in general, but which of the source-audited toolbox methods are most useful for either of two concrete problems:

1. one-dimensional FA-1f / East out-of-equilibrium convergence, with the unresolved one-dimensional FA-1f Bernoulli-quench problem as the main target and East as the closest solved benchmark;
2. the positive-rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS.

The public wiki remains frozen during the assessment. Work belongs under this research workspace. No `docs/` restructuring is authorized while the separate directory question remains with the principal.

## 1. Assessment standard

A method is not promoted in the ranking because it is powerful, fashionable, or thematically close. It must make contact with an **exact unresolved object** in the target programme.

Every final toolbox method receives one of five dispositions for the assigned problem:

- **A — actionable:** there is a concrete bridge lemma or short theorem chain, not known false and not already exhausted, whose proof would materially advance the target.
- **B — plausible architecture:** the method gives a coherent proof architecture and avoids known obstructions, but requires several substantial new bridges before reaching a live target.
- **C — auxiliary/diagnostic:** the method may prove a useful sublemma, supply a comparison, or falsify another route, but is not itself a credible target-level architecture.
- **X — blocked:** a specific established obstruction, theorem-hypothesis failure, or previously exhausted equivalent route blocks the method in the present form.
- **N — no credible contact:** no mathematically specific route from the method to a live target was found.

For every A/B/C/X disposition, the auditor must name the target interface and give a repository pointer or theorem pointer supporting the judgment. An A or B rating is invalid without a written bridge statement.

Do not assign numerical success probabilities. The final ranking is by expected research value: directness to the exact residual object, compatibility with known obstructions, amount of new mathematics required, exploitation of model geometry, and availability of a cheap first falsification test.

## 2. Positive-rates target ledger

The authoritative compact record is `research/active/positive-rates-conjecture/programme-established-results.md` on branch `research/positive-rates-conjecture`, together with final `state.md` and Meetings 025--030 there.

The conjecture remains open in the residual chamber. The sharpest active connected-renewal residual object is the signed two-time boundary-transmission operator

\[
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
 \bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt,
\]

on the **actual connected orbit**. Both scalar kernels change sign. A useful method for this route must preserve that two-time cancellation strongly enough to yield summable/geometric connected renewal coefficients. Taking absolute values before the two integrations is not an acceptable bridge.

Other live unresolved interfaces are:

- `(J-SPEC)` / connected-tail summability;
- common-uniform disagreement extinction versus convective escape to `-infinity`;
- stationary boundary-control diameter collapse `D_N(h)->0`;
- one-/two-step zero-boundary shift agreement and the associated `Gamma_M`/`J_{x,r}` decay.

Exact or durable obstructions that must be treated as hard evidence include:

- nearest-neighbour scalar edge-product/coboundary Foster certificates are ruled out at a hard residual point by a balanced-circulation certificate;
- no depth-uniform finite linear generator-mode closure can contain the common-mass transfer;
- the natural positive raw coefficient norms, including the two-parameter component-count refinement, cannot be uniformly nonexpansive in depth;
- the exact trajectory-valued spatial kernel has Dobrushin TV coefficient one;
- additive Bellman correctors without cross-block dependence cannot improve the stationary endpoints;
- the stopped programme does not restart for another generic norm, reversible comparison, filter optimization, larger finite coefficient table, bare tail-shift argument, common-coupling occupation variant, or generic Bellman-corrector search.

A toolbox method may still be highly ranked if it supplies a **materially different architecture** that bypasses these objects entirely, but the bridge statement must say exactly how.

## 3. FA-1f / East target ledger

The main unresolved benchmark is the one-dimensional hard FA-1f Bernoulli-quench problem: prove convergence to Bernoulli equilibrium throughout the remaining all-density regime. The older chronology/sign record gives several exact sufficient targets for the unresolved regime, including:

- the finite-time sign inequality `G_t(r)>=0` for the positive finite-set dual;
- shield positivity `S(t)>=0`;
- the weaker adjacent-vacancy repulsion condition `Cov(z_0(t),z_1(t))<=0`;
- the corresponding endogenous-boundary conditional cross-product inequality on three-site words;
- rooted punctured positivity `J_t(r)>=0`, which the last-ring Duhamel decomposition reduces to the remaining left-right punctured moment.

These are alternative bridge targets, not assumptions that a new method must use. The auditor should prefer the weakest target naturally produced by the method.

The existing programme also records important negative evidence:

- full coefficientwise positivity is stronger than needed and fails;
- the isolated-insertion cone is not manifestly generator-invariant because adjacent updates generate cluster-extension gradients of uncontrolled sign;
- replacing the endogenous exterior facilitation signals by independent/deterministic signals removes the actual difficulty and is not a valid closure;
- the centered positive `h`-transform and the complete `h`-weighted patch transfer are exact but conservative/stochastic reformulations, so a generation-by-generation positive contraction of that same transfer is not a new route;
- the finite-seed programme likewise closed because its two exact patch/dual implementations collapse to the same conservative coefficient dynamics. A genuinely new one-dimensional spatial mechanism, especially regeneration/screening behind vacancy fronts, remains a legitimate route.

East is used as a **solved structural benchmark**, not as another open target: its distinguished-vacancy/oriented-screening proof shows what a successful spatial-memory erasure mechanism can look like. A candidate FA-1f method should state exactly which two-sided obstruction prevents direct East transplantation and what new lemma would overcome it.

## 4. Primary audit assignments after wave seven

After wave seven is audited/integrated and the final inventory count is fixed:

### Student F — FA-1f / East applicability audit

Read every final source-audited toolbox method page, the FA-1f/East target ledger above, `docs/entries/fa-1f-out-of-equilibrium.md`, `docs/entries/east-out-of-equilibrium.md`, the chronology/sign route on branch `agent/fa1f-chronology-sign-route`, and the closed finite-seed `state.md`/`proof-spine.md` on branch `research/fa1f-finite-seed`.

Produce `assessment/fa1f-east-method-audit.md` containing:

1. a complete method-by-method disposition table;
2. at most six A/B methods, ranked;
3. for each shortlisted method, an explicit bridge lemma stated mathematically;
4. a short implication chain showing why that bridge advances or solves the target;
5. the exact existing obstruction it avoids;
6. a cheapest-first falsification test: a finite-volume computation, generator calculation, coupling sanity check, or sharply bounded source inspection that could kill the route quickly;
7. a separate note if the method is substantially more promising for the finite-seed problem than for the Bernoulli quench.

No broad new literature collection. Open primary sources only when the toolbox page is insufficient to formulate the adaptation precisely.

### Student G — positive-rates applicability audit

Read every final source-audited toolbox method page, `programme-established-results.md`, final positive-rates `state.md`, and Meetings 025--030 on branch `research/positive-rates-conjecture`.

Produce `assessment/positive-rates-method-audit.md` containing the same seven items, with each A/B method tied explicitly to one of:

- the signed boundary-transmission operator `V` / connected renewal;
- common-coupling convective escape;
- stationary diameter collapse;
- shift/connected-tail decay;
- or a genuinely different architecture that bypasses all four.

An A/B rating is invalid if it merely renames one of the stopped architectures.

## 5. Hostile cross-review

After both primary audits are committed, swap only the shortlists, not the full matrices.

- Student G reviews F's at-most-six FA-1f/East candidates.
- Student F reviews G's at-most-six positive-rates candidates.

For each candidate return exactly one ruling: **PASS**, **DEMOTE**, or **KILL**. The reviewer must attack hidden theorem hypotheses, equivalence to an exhausted route, conflict with an exact obstruction, and mismatch between the method's actual conclusion and the target.

A KILL ruling needs a precise reason. A PASS ruling needs one sentence explaining why the bridge remains genuinely open after the attack.

## 6. Professor synthesis

The Professor then produces `assessment/final-method-priorities.md` with:

- a ranked shortlist for each problem;
- the strongest bridge lemma for each surviving candidate;
- explicit killed methods whose failure is informative enough to prevent future loops;
- at most **two recommended first proof experiments per problem**;
- a recommendation whether to reopen a proof programme on either target, and on which exact bridge.

The assessment phase ends with a principal decision. It does not itself modify the public toolbox taxonomy or navigation.
