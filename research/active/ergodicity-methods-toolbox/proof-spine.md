# Proof spine

This file is now the current proof spine for the post-toolbox **FA-1f Bernoulli-quench** research direction. The 74-method inventory itself remains frozen and source-audited; its detailed coverage map is preserved in Git history and the live method pages. No breadth collection is active.

## Main target

For one-dimensional hard FA-1f, with equilibrium vacancy density

$$
q\in(0,1),
$$

and homogeneous Bernoulli initial vacancy density

$$
q_0>0,
$$

prove for every local function `f`

$$
\mu_{q_0}P_t(f)\longrightarrow\mu_q(f).
$$

The high-vacancy nonequilibrium theorem and positive equilibrium spectral gap are background; the present target is the unresolved all-density Bernoulli quench. The all-ones configuration is absorbing, so no proof may require convergence from every initial state.

## E0. Current architecture status

The hostile toolbox review retained exactly two independent FA architectures:

1. **FA-SCREEN** — an East-inspired two-sided physical causal screen;
2. **FA-INFO** — a quench-specific state-adaptive causal information history.

`FA-SCREEN-001` has now stopped as `STOP-SCALING-OBSTRUCTION` for the registered fixed-final-interval vacancy-boundary implementation. `FA-INFO` is the queued next bounded experiment. No full proof architecture is presently reopened.

## E1. Downstream equilibrium relaxation is not the blocker

For every `q>0`, one-dimensional FA-1f has positive finite-volume/infinite-volume equilibrium coercivity in the relevant ergodic component. The toolbox audit therefore treats the spectral gap as **downstream**.

A screen with a final protected interval `I_t`, relaxation time `s_t`, fresh interior marks, and conditional density cost at most `exp(C_q|I_t|)` would lead schematically to

$$
\exp(C_q|I_t|-\gamma(q)s_t),
$$

so `|I_t|=o(s_t)` would suffice once the causal screen exists.

The missing theorem is memory erasure/screening, not a stronger gap.

## E2. Exact local failure of the East distinguished vacancy

At a proposed right boundary, let the protected neighbour be `l`, the boundary spin `x`, its exterior neighbour `r`, and the refresh coin `z`. A boundary ring gives

$$
U(l,x,r;z)=
\begin{cases}
z,&l=0\text{ or }r=0,\\
x,&l=r=1.
\end{cases}
$$

The output depends on the protected side exactly when

$$
\boxed{r=1,\quad z\ne x.}
$$

For example

$$
U(0,0,1;1)=1,
\qquad
U(1,0,1;1)=0.
$$

Thus the literal East marker path is not measurable from the unscreened side. This is the exact local defect caused by two-sided facilitation.

Checkpoint: `students/professor/001a-fa-screen-local-leakage.md`.

## E3. Dimer gives only a killed local screen

An adjacent exterior vacancy dimer `00` can become `01` when the outer vacancy refreshes to `1`; this transition is legal without consulting the protected side. The next inner refresh-to-1 is the dangerous context above.

Therefore a dimer cannot be an exact failure-free regeneration boundary. It can remain **faithful** only by declaring failure before/at a dangerous mark. This passes the local leakage gate as a killed primitive, so the remaining question was lifetime/scaling.

## E4. Width-three vacancy-screen age obstruction

The decisive theorem is

`students/professor/001c-fa-screen-width3-scaling-obstruction.md`.

A width-at-most-three exterior-measurable screen state is active if it certifies at least one vacancy among its first three exterior sites. There are seven states. From every one, a four-unit event using only those exterior sites has the following properties:

1. by the end of phase 3 the first two exterior spins are `(0,1)`;
2. the adjacent exterior site has remained vacant throughout phase 3, so the protected endpoint is legal throughout that phase;
3. hidden protected refresh marks therefore leave positive conditional probability for either protected endpoint value;
4. a phase-4 boundary refresh-to-1 has different output for those two hidden protected values.

The forcing probability is uniformly at least

$$
\boxed{
\delta_3(q)=e^{-12}q^2(1-q)^2>0.
}
$$

Hence any faithful fixed active endpoint has age tail

$$
\boxed{
P(T>4n)\le(1-\delta_3(q))^n.
}
$$

The exact width-three verifier checks all seven states. At `q=1/10`,

$$
\delta_3(1/10)>\frac{81}{2000000000}.
$$

The explicit constant is only a certificate of strict positivity.

## E5. Why the registered FA-SCREEN cannot scale

The registered bridge fixes a final interval `I_t` and a time `tau_t<=t-s_t`, and requires the screen event/data to be determined without revealing future marks in

$$
I_t\times(\tau_t,t].
$$

Searches and handoffs may occur before `tau_t`. But a post-`tau_t` handoff triggered by a mark at a site later absorbed into final `I_t` consumes a mark that the freshness condition requires to remain protected. An endpoint change also means a fixed-volume gap stage of length `s_t` can begin only after the final change.

Thus the selected endpoint must have valid age at least `s_t`.

Even allowing `C s_t` possible endpoints,

$$
P(\exists\text{ valid endpoint of age }s_t)
\le
C s_t(1-\delta_3(q))^{\lfloor s_t/4\rfloor}
\to0.
$$

Therefore the fixed-final-interval screen built from exterior-measurable single-vacancy/dimer finite boundary automata cannot satisfy simultaneously:

- `s_t->infinity`;
- exact protected-future freshness;
- sublinear final width;
- screen probability tending to one.

This is `STOP-SCALING-OBSTRUCTION`. The positive spectral gap is never reached.

## E6. Scope of the FA-SCREEN stop

The theorem does **not** rule out:

1. a materially different relaxation theorem for a genuinely moving/adaptive boundary whose conditioning does not reveal marks later declared protected;
2. a causal-information proof which reveals protected information selectively rather than constructing a long-lived exterior boundary.

The first would require a new upstream bridge; do not obtain it by merely increasing marker width/phases. The second is exactly `FA-INFO`.

## E7. Next bounded edge: FA-INFO adaptive reveal

The remaining PASS architecture uses the actual Bernoulli quench rather than worst-case initial states.

At a legal-ring decision, the FA constraint is the OR

$$
1_{\{\eta_{i-1}=0\text{ or }\eta_{i+1}=0\}}.
$$

A causal reveal procedure may inspect one neighbour first. If it is vacant, legality is certified and the second neighbour need not be revealed. If it is occupied, the second neighbour must be inspected. Histories may merge, and once a legal refresh coin fixes the new spin the old-site history may be discarded.

This is different from:

- the mark-only support process, which must retain all globally essential parents;
- the conservative centered/harmonic dual, whose coefficient mass is exactly preserved;
- a worst-case ancestor-extinction proof, which the hard all-ones trap forbids.

### Required first theorem/test

Before any multiscale argument:

1. define an exact adaptive decision/reveal algorithm on the smallest one/two-block space-time slab;
2. derive the law of its residual time-zero information under `mu_{q0}` without using the desired mixing conclusion;
3. derive a **pair-level** likelihood/intersection statistic sufficient for a local total-variation or chi-square comparison, rather than using only expected leaf count;
4. test whether adaptive short-circuiting/merging creates a strict finite-block contraction or another iterable inequality at low-`q` stress values.

A merely smaller first moment than the naive branching tree is evidence only, not a continuation criterion.

## E8. Anti-circularity and stopped routes

Do not:

- strengthen equilibrium gap/entropy estimates instead of proving memory erasure;
- freeze or exogenize FA boundary facilitation;
- enlarge the stopped vacancy screen through arbitrary marker phases;
- identify the adaptive reveal object with the conservative transformed dual;
- quote the Ising Miller--Peres estimate without deriving the needed conditional independence/likelihood identity for the actual FA reveal rule;
- use product-background disagreement transmission as an iteratable bound after conditioning on a surviving path;
- demand worst-case convergence from the absorbing all-ones state.

The earlier FA positive-dual/patch-transfer and finite-seed programmes remain closed at their recorded conservative-transfer obstructions.

## Frozen toolbox note

The source-audited method inventory remains frozen at 74 live entries. The current proof spine changes only the problem-specific research state; it does not reopen collection or alter the public wiki.
