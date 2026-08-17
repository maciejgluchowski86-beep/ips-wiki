# Student G hostile cross-review of FA-1f / East shortlist

Date: 2026-08-17

Scope: hostile review of the Professor's five A/B candidates from `assessment/fa1f-east-method-audit.md` under Section 5 of `assessment-protocol.md`. I did not rerate the 74-method inventory. The target is one-dimensional hard FA-1f Bernoulli-quench convergence; the chronology/sign and closed finite-seed records are treated as evidence to be rechecked, not authority.

## 1. East distinguished-zero screening

**RULING:** PASS

**Attack**

The source theorem does **not** transfer directly. East Lemma 8.2 relies on strict orientation: the future path of the distinguished vacancy is measurable from the unscreened side and does not inspect the region it leaves behind. In symmetric FA-1f, legality of a ring at a proposed marker is an OR of the two neighboring vacancy states, so a naive distinguished vacancy can have its next legal event determined by the very region it is supposed to screen. Conditioning on such a marker path can therefore reveal interior information and destroy the claimed regeneration. The all-ones trap also rules out any version that would screen uniformly over all initial configurations.

The Professor's bridge, however, is stronger and avoids those shortcuts. It requires a random bracket `I_t`, a time `tau_t <= t-s_t`, a high-probability event `E_t`, and screen variables for which the interior evolution on `[tau_t,t]` uses genuinely fresh interior marks and is causally insulated from the exterior. It does not assume exact conditional equilibrium at `tau_t`. On a finite interval with a legal vacancy boundary, product Bernoulli equilibrium has full support; an arbitrary conditioned initial law has an `L^2(mu_q^{I_t})` density cost at most `exp(C_q |I_t|)`. A volume-uniform positive FA-1f gap then gives an error bounded schematically by `exp(C_q |I_t|-gamma(q)s_t)`. Thus `|I_t|=o(s_t)`, `s_t->infinity`, and `P(E_t^c)->0` are quantitatively sufficient, provided the screen conditioning really leaves the interior marks fresh and the boundary process is one for which the gap comparison applies.

This bridge is not equivalent to the closed positive-dual/patch routes: it asks for a new causal sigma-field in the physical graphical process, whereas the finite-seed obstruction is conservation of the complete `h`-weighted coefficient transfer. Nor is it equivalent to the original convergence assertion: the proposed screen is a stronger geometric event with independently testable measurability and leakage requirements.

**Load-bearing reason**

No existing FA obstruction rules out a two-sided *approximate* causal screen. The exact East screen fails because of two-sided facilitation, but the bridge explicitly makes overcoming that failure the new theorem rather than silently assuming one-sided independence. Once the screen exists with fresh marks and sublinear width, the remaining relaxation step is genuinely supplied by known FA coercivity.

**If PASS:** The bridge remains genuinely open because a two-sided high-probability causal screen with fresh interior randomness is a new spatial statement not implied by, or contradicted by, the conservative dual/patch obstructions, and it would close the quench using the already-known positive FA gap.

**Cheapest next check**

Before any tail estimate, fix the simplest proposed two-sided marker/corridor rule on 5--7 sites and exhaustively compare two exterior continuations that agree on all declared screen data. If either continuation changes (i) the legality of an interior ring during the claimed screened interval, (ii) the law of a future screen variable, or (iii) which interior Poisson/coin marks have been revealed by the conditioning, the rule is not regenerative and should be discarded immediately. This is the right first check because the main danger is sigma-field leakage, not the downstream gap estimate.
