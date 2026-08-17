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

Latest meeting: `meetings/032-distinguished-zero-transfer-stops-and-hamming-coupling-killed.md`, `state_narrowed: yes`.

## Active work

Student G is active on

`students/student-g/assignment-012.md`

at commit `be3d4e0ba6a81a6019de42d86a15858d47cefcb2`.

Assignment 012 is the bounded information-percolation / backward-history pair-intersection experiment retained by the toolbox synthesis. It does **not** reopen a full proof architecture.

Student F remains idle. No F016 is active.

## G011 distinguished-zero transfer: closed as `STOP-EQUIVALENT`

The principal-directed question was whether East distinguished-zero screening could be transferred to the residual positive-rates system by replacing Bernoulli equilibrium with the finite zero-boundary invariant family `pi_N`.

Meeting 032 accepts Student G Assignment 011 as `STOP-EQUIVALENT`.

### Exact one-move obstruction

If a right-measurable marker move leaves the old protected `N`-site block untouched and exact post-move law is required to be `pi_{N+1}`, then necessarily

$$
\bar\pi_{N+1}=\pi_N.
$$

Already at `N=1 -> 2`,

$$
\bar\pi_2(1)-\pi_1(1)
=-\frac{2a\,[a-b(1-c)]}
{(a+1-c)\,[2ab-ac+3a-bc+b+c^2-3c+2]}.
$$

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
$$

this equals

$$
-\frac{4950}{15151}\ne0.
$$

The principal independently ran the committed exact verifier; the Professor independently recomputed the symbolic factorization.

### Compatibility locus

Exact compatibility holds on

$$
a=b(1-c).
$$

With `rho=b/(1+b)`, this is precisely the product/reversible surface on which

$$
\pi_N=\operatorname{Ber}(\rho)^{\otimes N}
$$

for every zero-boundary box. Thus the literal East induction transfers exactly where the surrogate family has reverted to a product-consistent family, and fails off that surface already at depth two.

### Buffered and regenerative repairs

If the last `m` sites are declared contaminated, the exact protected-prefix mismatch is

$$
S_m=\Delta_{m+1}.
$$

An arbitrary fresh width-`m` release kernel that cannot inspect or modify the protected prefix requires `Delta_{m+1}=0` for exact output and has approximate error bounded below by the same prefix discrepancy. Hence a growing buffered/release screen requires `Delta_M->0` upstream.

Therefore marker-existence Part D is closed as **moot for this architecture**. Marker geometry cannot repair a marginal incompatibility that remains after every released coordinate is marginalized out. A future distinguished-zero-inspired idea would have to introduce a new dynamical boundary-defect erasure theorem rather than continue G011's `pi_N` induction.

## New exact obstruction: uniform additive-Hamming coupling bridge is false for every Markovian coupling

Meeting 032 proves a general coupling fact. For additive Hamming distance

$$
H(x,y)=\sum_i\mathbf1_{\{x_i\ne y_i\}},
$$

pairing a flip at site `i` in one copy with a flip at a **different** site `j` in the other cannot improve instantaneous drift: the Hamming increment is additive across distinct coordinates and the off-diagonal joint rates collapse under the marginal constraints.

The optimal contribution at an agreed site is the absolute difference of the two marginal flip rates; at a disagreeing site it is minus their sum. Thus

$$
\inf_{\text{Markovian couplings}}\bar L H
=
\sum_{i:x_i=y_i}|\lambda_i(x)-\lambda_i(y)|
-
\sum_{i:x_i\ne y_i}(\lambda_i(x)+\lambda_i(y)).
$$

At `P_h`, take one disagreement at site zero with common right spin zero and common left spin one. The best possible drift is

$$
c-(a+1-c)=\frac{9997}{10000}>0.
$$

Hence the toolbox refined-coupling bridge requiring

$$
\bar L H\le-\kappa H
$$

for some uniform `kappa>0` is impossible at the hard point for **all** Markovian couplings, not merely the common-uniform coupling. The proposed non-diagonal Hamming LP is therefore canceled as redundant.

This does not refute a Gray-type nonadditive edge geometry.

## Active bounded experiment: information percolation

Assignment 012 tests whether an exact random-map decomposition of the residual generator yields a pair of minimal backward supports with a genuine intersection-decay mechanism.

The experiment first derives the exact Boolean-map decomposition polytope and ancestry-rate region, then studies two independent support processes through the pair observable

$$
\Psi(A,A')=2^{|A\cap A'|}-1.
$$

A naive supercritical ancestor first moment is not a kill criterion. Continue only if a pair-level state/inequality shows strict contraction or a concrete decomposition-independent pair obstruction is proved. Computation is capped at relative width `W<=8` unless a structural recursion is found.

Permitted final statuses:

- `STOP-PAIR-OBSTRUCTION`;
- `STOP-NO-PAIR-SIGNAL`;
- `UNRESOLVED-BOUNDED`;
- `CONTINUE-PAIR-BRIDGE`.

## Previous connected-renewal route remains stopped

Assignment 010 remains complete unresolved. Its sharp residual object is still the signed boundary-transmission Volterra operator

$$
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
$$

No depth-uniform actual-orbit estimate retaining the two-time cancellation has been proved. Meeting 030's restart bar remains operative for that route.

Bare tail shift, common-uniform all-depth occupation, Bellman/joint-corrector, scalar Foster, reversible-comparison continuation, generic norm searches, and longer coefficient tables remain stopped at their recorded obstructions.

## Retained exact mathematics

The projective zero-boundary invariant family and tail-shift identity, common-coupling fixed-site/local-erasure results, actual-front first-discovery theorem, stationary-control hierarchy, exact trajectory-valued spatial kernel, predecessor-trail reduction, and G009/G010 positive-frequency/renewal structure remain valid retained background.

## Unresolved target-level facts

Open:

- whether the optimized information-percolation pair-history mechanism gives a real bypass;
- whether a nonadditive Gray-type splice-edge geometry can exist;
- one-/two-step tail-shift agreement off the product surface;
- `(J-SPEC)` and connected-tail `(CT)`;
- the actual-orbit signed boundary-transmission estimate `(V)`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research. No `docs/` or `mkdocs.yml` edits are authorized.
