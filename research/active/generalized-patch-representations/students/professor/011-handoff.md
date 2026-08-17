# Assignment 011 handoff

Date: 2026-08-17

Outcome: **`STOP-CANCELLATION-NO-QUALITATIVE-GAIN`**.

## What was proved

1. In finite volume, the killed typed patch representation defines a positive patch-variation kernel `R_t` satisfying
   \[
   |Q_t|\le R_t\le A_t,
   \]
   where `Q_t` is the exact signed FK kernel and `A_t` is the raw absolute-FK kernel.

2. The inequality can be strict on the verified Potts model. Exact normalized local factors at the positive-length gate are
   \[
   10178204/38671875
   <
   17919551/38671875.
   \]

3. The envelope is composable:
   \[
   R_{t+s}\le R_tR_s.
   \]

4. Additive support weight turns the patch envelope into a finite multitype renewal first-moment majorant. A subcritical exponentially tilted kernel implies volume-uniform exponential oscillation decay.

5. Exact one-neighbour Potts structural gate:
   \[
   \rho(G)=17/6,
   \qquad
   \rho(\bar G)=3.
   \]
   Scaling nonempty target modes by `epsilon=17/50` gives
   \[
   289/300<1<51/50.
   \]
   Thus patch averaging can cross a contraction threshold that raw absolute FK does not.

## Why the programme nevertheless stops

The downstream oscillation/contraction and multitype renewal machinery is established theory. The principal's own Głuchowski--Menz 2025 paper already gives finite-alphabet representational-seminorm criteria implying exponential covariance decay. The exact separation gate demonstrates mechanism but is not a new natural-model theorem.

No equivalent prior source was identified for the particular killed-skeleton majorant `R_t`; it remains a plausible corollary/extension of the killed typed patch factorization. That is not enough, by itself, to justify another model search or generic `d>3` work.

## Decisive files

- `011a-unnormalized-patch-variation-envelope.md` (`59115cb7`)
- `011b-potts-strict-hidden-mark-cancellation.md` (`4df18585`)
- `011c-submultiplicative-patch-variation-kernel.md` (`070598bc`)
- `011d-oscillation-renewal-majorant.md` (`85b8145b`)
- `011e-prior-work-and-value-ruling.md` (`f07a8c15`)
- `011-cancellation-envelope-verifier.py` (`6dab532c`)
- `011-oscillation-renewal-verifier.py` (`c1ffaafb`)
- final report `011-killed-patch-cancellation-envelope.md` (`78e725f7`)

## Final direction

Close the generalized-patch programme deliberately. Preserve the representation/factorization theorem stack and negative application lemmas. Do not queue Assignment 012, generic `d>3`, or another application search.