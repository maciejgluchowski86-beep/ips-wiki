# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

The scientific target remains fixed:

> Prove the positive rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/031-distinguished-zero-transfer-reopens-one-bounded-screening-test.md`, `state_narrowed: yes`.

## Active work

Student G is active on

`students/student-g/assignment-011.md`

at commit `6efcf60ab43782cf48058484f86f2faca3a7f093`.

Assignment 011 is a bounded test of a new principal-directed architecture: whether an East-style distinguished-zero screening argument can be transferred to the residual positive-rates problem by replacing the known Bernoulli equilibrium behind the East marker with the finite zero-boundary invariant family `pi_N`.

Student F remains idle. No F016 is active.

This is **not** a general reopening of the proof programme. The connected-renewal, common-coupling occupation, Bellman, scalar Foster, generic coupling/norm, and long coefficient-table routes remain stopped at their recorded obstructions.

## Distinguished-zero transfer test

For the `N`-site chain with fixed zero boundary at `N+1`, let `pi_N` be its unique invariant law. One-sidedness gives the accepted right-suffix projectivity

$$
R_{N,M}\pi_N=\pi_M.
$$

The old profile work also identified the left-prefix defect

$$
\delta_{N+1}=\bar\pi_{N+1}-\pi_N.
$$

Far from the boundary, its uniform magnitude is the tail-shift quantity `Delta_M`; on the projective half-line law `mu=pi_infty^0`,

$$
\Delta_M
=\|\theta\mu-\mu\|_{\mathcal F_{M-1}},
$$

and

$$
\lim_M\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
$$

Therefore merely naming the zero-boundary invariant marginals does not automatically reproduce East's conditional-equilibrium induction. If a distinguished marker moves one site right using only marker/right-side history and leaves the old protected `N`-site block untouched, exact post-move law `pi_{N+1}` requires

$$
\bar\pi_{N+1}=\pi_N.
$$

Assignment 011 first tests this finite compatibility exactly at the hard point

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

and symbolically if feasible. It then tests whether a buffered or regenerative release of a finite boundary layer yields a genuinely new screening object or merely assumes tail-shift agreement upstream.

Permitted final statuses are:

- `STOP-EQUIVALENT`;
- `STOP-LOCAL-OBSTRUCTION`;
- `CONTINUE-NEW-BRIDGE`.

The pre-registered stop rule is strict: do not enlarge marker states if every repair requires as an input `Delta_M->0`, the abandoned common-uniform all-depth occupation theorem, Meeting 030's signed boundary-transmission estimate, or another already-stopped generic contraction object.

Continue only if the distinguished-zero construction produces a new graphical/invariant-family quantity strictly upstream of those blockers, with an explicit implication chain to local forgetting and one bounded next test.

## Previous connected-renewal route remains stopped

Assignment 010 is complete unresolved. At

$$
P_*=(1/1000,1/10,9999/10000),
$$

the accepted fixed-filter renewal, positive-frequency terminal contraction, complementary channel split, reversible-reference Sobolev estimates, and fresh-coordinate intertwining remain valid.

The sharp residual object of that route is still the signed boundary-transmission Volterra operator

$$
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
$$

No depth-uniform actual-orbit estimate retaining its two-time cancellation has been proved. Meeting 030's restart bar remains operative for that architecture.

The exact Bellman/stationary-control hierarchy, common-coupling fixed-site/local-erasure results, actual-front first-discovery theorem, projective zero-boundary invariant law, trajectory-valued spatial kernel, and G009/G010 renewal mathematics remain retained background. Their stopped implementations are not automatically reopened by Assignment 011.

## Toolbox synthesis interface

The completed ergodicity-methods applicability assessment had recommended two bounded positive-rates feasibility experiments:

1. an exact non-diagonal coupled-rate/Gray LP;
2. an optimized information-percolation pair-support calculation.

Meeting 031 **defers, but does not kill**, those experiments while the principal-directed distinguished-zero test runs. The screening question has higher immediate value because it directly probes whether the accepted zero-boundary invariant family supplies a new spatial memory-erasure architecture.

The separate FA `FA-SCREEN` theorem remains an authorized programme direction and is not canceled; the two problems now share a screening/sigma-field theme.

## Unresolved target-level facts

Open:

- whether the distinguished-zero/zero-boundary invariant-family transfer gives a new screening bridge;
- one-/two-step tail-shift agreement off the product surface;
- `(J-SPEC)` and connected-tail `(CT)`;
- the actual-orbit signed boundary-transmission estimate `(V)`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research. No `docs/` or `mkdocs.yml` edits are authorized by this reopening.
