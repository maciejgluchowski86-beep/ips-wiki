# Outside consultation 001: actual disagreement front versus convective survival

This is a bounded outside consultation, not a graduate-student assignment and not a new scientific direction.

Work from branch `research/positive-rates-conjecture`.

Read first:

- root `project-state.md`, `README.md`, `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- Meetings 015--017;
- Student G `006-common-coupling-survival.md` and `007-random-map-hamming-contraction.md`;
- Student F `012-tail-shift-agreement.md` only for the interface showing why a useful front theorem would matter.

The principal-fixed target remains the positive rates conjecture for simple IPS. Do not change target and do not edit the repository.

## Why this consultation exists

At the hard strict residual point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

for the actual common-uniform coupling:

1. every fixed site eventually becomes permanently coupled from every finite disagreement seed;
2. survival, if it occurs, is exactly convective escape to `-infinity`;
3. the moving-frame weight `V_z=\sum_i z^iD_i` contracts for `z>c/(1-c+a)`;
4. the full Hamming coefficient
   $$
   \alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i)
   $$
   is submultiplicative;
5. one `alpha(T)<1` would imply exponential extinction;
6. `alpha(T)` has a two-sided convergent fixed-boundary approximation
   $$
   B_{L,R}^e(T)-r_{L,R}(T)
   \le\alpha(T)\le
   B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T);
   $$
7. nevertheless an explicit protected-source event proves
   $$
   \alpha(t)>1\qquad(0<t\le47),
   $$
   while the causal Poisson errors at that time already force raw windows of order the elapsed time.

The raw finite-window certificate implementation has therefore been stopped. The unresolved structural alternatives are:

- prove a sharp tail/front theorem for the **actual** disagreement process that retains the common-spin history before first exposure and makes finite-time contraction tractable; or
- prove genuine convective survival from a finite seed.

The central anti-circularity warning is that the predecessor-trail reset-height drift is not an embedded chain of the actual common-uniform disagreement process and may not be imported as such.

## Consultation objective

Assess whether either structural alternative has a credible short mathematical route, and if possible prove the strongest bounded theorem you can.

This is not a request for another large computation. The consultation should answer whether the next substantial internal research block should exist at all.

### Route A: actual-front upper tail

Look for a theorem substantially sharper than the causal Poisson cone, for example a statement of the form

$$
\sup_{\eta}
P_\eta(\text{single-flip disagreement reaches }-m\text{ by time }T)
\le \varepsilon_{m,T},
$$

where `\varepsilon_{m,T}` reflects the true near-East exposure dynamics and is useful for `T>47` with `m` much smaller or more structured than the raw causal cutoff.

A useful theorem must preserve enough pre-exposure common-spin history to avoid the known invalid adversarial/favorable fresh-spin simplifications. If a regeneration state, renewal structure, subadditive front speed, killed exploration, or information-percolation object does this, define it exactly and prove the comparison.

Do not merely restate the desired front tail or quote fixed-site coupling.

### Route B: convective survival

Try to construct a legitimate finite-seed survival mechanism. A block/oriented-percolation comparison is welcome if the block state includes the common-spin information needed at first exposure and the dependence between neighboring blocks is controlled.

A successful theorem may be only at the hard rational point. It need not cover the full residual chamber.

Do not infer survival from `alpha(t)>1` on a finite interval, from failure of upper certificates, or from a favorable fresh-spin approximation.

### Route C: route-killing obstruction

If neither theorem looks plausible, identify a precise reason that the actual-front problem is essentially as hard as the original positive-rates problem or would not materially help the signed predecessor-trail quantity even if solved.

The Professor needs an expected-value judgment, not a catalogue of imaginable norms.

## Questions the final report must answer

1. Is convective survival near the hard point more plausible than eventual global extinction under the common-uniform coupling? Give mathematical reasons, not intuition alone.
2. Is there a concrete state/process that retains pre-exposure common-spin history and admits a tractable Markov or renewal description?
3. Can one prove any nontrivial front-speed, front-tail, block-survival, or extinction estimate beyond the already accepted causal Poisson cone and fixed-site coalescence?
4. Would such a theorem actually interface with the centered predecessor-trail programme, or only settle an auxiliary coupling question?
5. Recommend exactly one of `continue-front`, `continue-survival`, or `abandon-common-coupling-interface`.

## Scope discipline

Do not:

- run larger raw `L,R,T` finite-state enumeration as the main result;
- introduce a generic matrix-product norm without a theorem that changes the proof spine;
- revive the exposed-only or 16-phase scalar Foster classes;
- import the trail reset-height drift into the actual coupling;
- assume the positive rates conjecture, a uniform spectral gap, or the desired tail-shift theorem;
- treat numerical evidence as proof.

Literature search is allowed if it directly informs the front/survival mechanism; distinguish literature facts from new derivations.

## Output

Return a concise consultant report with:

- `RECOMMENDATION: continue-front | continue-survival | abandon-common-coupling-interface`;
- `ESTABLISHED`;
- `KEY ARGUMENT`;
- `FATAL OBJECTIONS / GAPS`;
- `INTERFACE WITH J_{x,r}`;
- `ONE NEXT INTERNAL TASK`.

Do not edit GitHub.
