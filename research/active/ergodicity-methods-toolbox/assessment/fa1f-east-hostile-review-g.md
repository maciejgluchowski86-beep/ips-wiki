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

## 2. Refined non-diagonal discrepancy coupling

**RULING:** DEMOTE

**Attack**

The checked Gobron--Saada theorem does not provide the claimed FA bridge. Its non-diagonal coupling is built for conservative exclusion-type moves and is available only after rate inequalities guaranteeing monotonicity. The redistribution of jump mass between different microscopic moves is the mechanism by which the marginals and order are simultaneously preserved. Hard FA-1f is nonconservative, not attractive in the natural occupancy/vacancy order, and has state-dependent zero legal rates. Therefore none of the theorem's discrepancy monotonicity or invariant-law conclusions transfer.

The Professor's proposed replacement is a global measure-preserving chronology switch on two independent FA graphical histories. That proposal has a more basic problem. On an atomless pair-history space, existence of an unrestricted measure-preserving injection from

`{000 in replica 1, 110 in replica 2}`

into

`{100 in replica 1, 010 in replica 2}`

is essentially another formulation of the desired probability inequality `P(000)P(110) <= P(100)P(010)`. To become a proof architecture rather than a restatement, the admissible map has to be restricted to a local/predictable class with a closure rule that can be checked inductively through the graphical chronology.

The chronology record identifies the missing closure exactly. A fixed vertical replica swap fails at a two-sided constrained update. The isolated-insertion calculation gives the same warning algebraically: at a boundary point, an adjacent update creates cluster-extension gradients such as `D_i f(A union {j})` or `D_j f(A union {i})` whose sign is uncontrolled. Merely allowing a different mark or site in the other replica does not say how the swap interface evolves after the next adjacent update, nor how the transformation remains injective and measure-preserving after repeated encounters. No finite switch-state space or invariant switching rule is supplied.

This is not an exact counterexample to the cross-product inequality itself; the Professor's finite-cycle tests found no violation. It is a failure of the claimed *method-level bridge*: the source theorem's structural hypotheses fail, while the replacement bridge currently encodes the target inequality globally rather than reducing it to a closed local mechanism.

**Load-bearing reason**

The missing object is a locally specified chronology-switch dynamics whose state space closes under every neighboring FA update and whose predictable permutations preserve the two independent Poisson/coin laws. Without such a closure theorem, "pair different microscopic updates" is only freedom in how one searches for a proof; it does not yet constitute a target-level architecture.

**If DEMOTE:** The strongest remaining auxiliary use is as a finite local feasibility framework: formulate predictable permutations/coupled transition rates on a bounded switch state, impose exact marginal-law and legality constraints, and use the result either to discover a closed chronology rule or to certify that a proposed class of switches is impossible.

**Cheapest next check**

Choose a specific finite switch-state description (interface location plus the smallest neighboring spin/mark data claimed to be sufficient). Enumerate every possible next graphical ring and coin in both replicas. Require that the switch state updates within the same finite class, reconstructed histories remain legal, and the permutation is predictable and bijective on equal-rate Poisson/coin marks. Failure of closure on a single adjacent-update pattern kills that proposed switch class immediately. A global endpoint injection without this local closure check should not be counted as progress.

## 3. Information percolation / backward histories

**RULING:** PASS

**Attack**

The Lubetzky--Sly mechanism cannot be imported literally. In their Glauber setting an update can be genuinely oblivious: after the graphical mark is fixed, the new spin may no longer depend on any previous spin. Hard FA has no state-independent oblivious update of that kind. If a graphical rule set a site independently of its neighbors with positive probability, it would move the all-ones configuration, contradicting the hard trap. Hence any update support defined solely from the Poisson/coin marks and required to determine the output for **all** possible initial states cannot have the high-temperature dying-history behavior used in the source.

The Professor's bridge survives only because it explicitly changes the object. The proposed history is state-adaptive and quench-specific. At a ring, proving that one neighboring history is vacant certifies legality and can short-circuit the other neighboring branch; an effective dependency may also disappear after repeated refreshes or merge with another branch. Conversely, to certify an illegal ring one may have to know both neighbors are occupied and retain the old site's history. The naive branching estimate is therefore indeed supercritical-looking (`1+p+p^2>1` in the primary audit), but it is not an exact reproduction number for the minimal adaptive reveal process.

This adaptive object is not the closed positive finite-set dual. The transformed dual is a linear/algebraic Markov chain whose complete `h`-weighted coefficient transfer is stochastic and conservative. A minimal causal reveal tree can delete nominal branches when their values become logically irrelevant, can merge branches, and is conditioned on actual vacancy discoveries under the Bernoulli start. Conservation of the linear dual mass therefore does not imply conservation of adaptive causal information.

There is one necessary correction to the source analogy. The red/blue/green Miller--Peres estimate from Lubetzky--Sly relies on a history construction with special conditional independence properties and cannot simply be quoted for this state-dependent reveal process. The bridge should instead be judged by its direct target statement: with the same graphical marks, the pushforwards of `mu_{q0}` and `mu_q` to a fixed observation block have total-variation distance tending to zero, or an explicitly dominated reveal event implies that statement. That conclusion is exactly strong enough for the infinite-volume Bernoulli quench and does not assert convergence from the trapped all-ones state.

**Load-bearing reason**

No exact obstruction in the chronology or finite-seed records identifies adaptive minimal causal support with the conservative transformed dual. The hard-trap obstruction kills uniform mark-only ancestor extinction, but it does not kill a law-dependent reveal process that exploits actual vacancies and only has to forget a Bernoulli initial condition. The remaining task is a genuine probabilistic theorem about adaptive history sparsity, not a known-false coefficient contraction.

**If PASS:** The bridge remains genuinely open because quench-specific adaptive causal histories can exploit logical short-circuiting and mergers that are absent from the conservative linear dual, while their vanishing influence would directly compare the Bernoulli quench to the stationary Bernoulli start without requiring worst-case history extinction.

**Cheapest next check**

On a finite space-time slab, compute the exact minimal decision tree for one terminal site under product initial vacancies and graphical marks, allowing short-circuit evaluation of the FA `OR` constraint. Record the distribution of unresolved time-zero leaves after one and two temporal blocks and compare it with the naive branching majorant. If adaptive pruning/merging does not reduce a natural exponential or block reproduction statistic below one in any low-`q` test regime, the architecture should be demoted before attempting a multiscale proof. The statistic must be defined from the actual reveal algorithm, not from the transformed dual particle count.
