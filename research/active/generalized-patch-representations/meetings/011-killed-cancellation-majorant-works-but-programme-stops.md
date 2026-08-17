# Meeting 011: killed cancellation majorant works, but programme stops

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- pre-registered Assignment 011: `students/professor/assignment-011-killed-patch-cancellation-envelope.md`, commit `c4299330`;
- exact patch-variation theorem `011a-unnormalized-patch-variation-envelope.md`, commit `59115cb7`;
- strict Potts hidden-mark cancellation `011b-potts-strict-hidden-mark-cancellation.md`, commit `4df18585`;
- submultiplicativity `011c-submultiplicative-patch-variation-kernel.md`, commit `070598bc`;
- oscillation/renewal theorem and exact separation gate `011d-oscillation-renewal-majorant.md`, commit `85b8145b`;
- prior-work/value ruling `011e-prior-work-and-value-ruling.md`, commit `f07a8c15`;
- exact verifiers `011-cancellation-envelope-verifier.py` (`6dab532c`) and `011-oscillation-renewal-verifier.py` (`c1ffaafb`);
- final report `011-killed-patch-cancellation-envelope.md`, commit `78e725f7`;
- handoff `011-handoff.md`, commit `d8489a9b`.

## Ruling

Assignment 011 ends

**`STOP-CANCELLATION-NO-QUALITATIVE-GAIN`.**

The generalized-patch programme is **closed deliberately on opportunity-cost grounds**. This is not an exhaustion claim and does not retract the verified representation theorem stack.

## 1. The final bounded continuation found genuine mathematics

For the finite-volume signed FK kernel `Q_t`, raw absolute-FK kernel `A_t`, and the new killed patch-variation kernel `R_t`, Assignment 011 proves

\[
\boxed{|Q_t|\le R_t\le A_t}
\]

entrywise. `R_t` is obtained by averaging each hidden killed patch first and only then taking its absolute value.

The gain is strict on the already-verified Potts model. At the exact positive-length gate,

\[
\frac{10178204}{38671875}
<
\frac{17919551}{38671875},
\]

with exact gap

\[
\frac{2580449}{12890625}.
\]

The gain also survives deterministic time cuts:

\[
\boxed{R_{t+s}\le R_tR_s}.
\]

Thus the killed successful-skeleton grouping produces a genuine positive submultiplicative majorant, not merely a local triangle inequality.

## 2. It yields a checkable renewal/oscillation criterion

Using support weight and suppressing spatial collisions gives a finite multitype patch-tree renewal kernel built from source-line responses

\[
|b_u e^{tK}e_r|.
\]

A subcritical exponentially tilted next-generation kernel gives a volume-uniform exponential oscillation bound for local indicator tensors.

An exact one-neighbour Potts interpolation separates this from the raw absolute-FK criterion. Before interpolation,

\[
\rho(G)=17/6,
\qquad
\rho(\bar G)=3.
\]

Scaling only nonempty target modes by

\[
\varepsilon=17/50
\]

gives

\[
\boxed{289/300<1<51/50.}
\]

So delayed hidden-mark averaging can cross a first-moment contraction threshold that the raw absolute process does not.

## 3. Why this still closes the programme

The final prior-work/value check distinguishes the new-looking majorant from its downstream consequences.

The specific killed-skeleton majorant `R_t` and its submultiplicativity were not found in equivalent form and remain a plausible corollary/extension of the killed typed factorization mechanism.

However, once a positive coefficient/oscillation contraction kernel is available, exponential ergodicity/covariance-decay conclusions are established Dobrushin/representational-seminorm territory. Multitype renewal and next-generation spectral-radius arguments are also standard machinery. In particular the principal's existing Głuchowski--Menz finite-alphabet criterion already turns coefficient/seminorm contraction into exponential covariance decay.

The exact separation family above was deliberately constructed as a structural gate after the natural-model application blocks. It is not a new theorem for a difficult published model.

Therefore Assignment 011 does not meet its pre-registered continuation bar. It found a stronger representation majorant, but not a sufficiently independent natural-model or model-independent consequence to justify another research block.

## 4. Final retained research status

Retain as verified mathematics:

1. arbitrary finite-state typed signed FK duality for bounded finite-range single-site replacement IPS;
2. the exact finite counterexample to bare successful-skeleton factorization;
3. cemetery-aware killed/noncemetery patch factorization;
4. exact finite-state bulk/end patch representation;
5. local transfer description of bulk factors;
6. the short-`OO` contrast obstruction explaining both natural application failures;
7. the patch-variation majorant
   \[
   |Q_t|\le R_t\le A_t,
   \qquad R_{t+s}\le R_tR_s.
   \]

Contribution status remains narrower than mathematical status:

- killed typed factorization/representation: **plausibly new theorem/mechanism** after the bounded Assignment-008 audit;
- patch-variation majorant: **plausibly new corollary/extension**, historical priority not established;
- `d=3` spectral criterion: **known / directly subsumed** by third-order external positivity;
- downstream oscillation/renewal contraction machinery: established ingredients.

## 5. Closure

Do not queue Assignment 012.

Do not reopen:

- positivity-driven model search;
- generic `d>3` external-positivity algebra;
- cosmetic variants of the cancellation envelope.

A future principal decision may reuse individual verified lemmas or promote mature material, but autonomous work on this scientific direction stops here.