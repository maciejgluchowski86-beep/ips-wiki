# Student F assignment 010: profile regeneration / truncation of the growing mass hierarchy

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/011-finite-mode-closure-refuted-profile-truncation-target.md`;
- your `009-mode-resolved-l1-block.md` and verifier;
- Meeting 010 and Student G `assignment-005.md`;
- Meetings 006--009 and the principal trail notes as needed.

The scientific target remains the positive rates conjecture for simple IPS.

## What is now accepted

Your Assignment 009 conclusions are Professor-checked.

For

$$
r_0=\frac1{1+b},
$$

the equilibrium mass type has

$$
\kappa_E=|Br_0-c|Z<\frac23.
$$

The first transient type has

$$
\boxed{
\kappa_T
=B Z_{\omega+1+b}<1,
}
$$

with exact gap, writing `k=1-c`,

$$
a^2+5ab+ak+7a+4bk+6k>0.
$$

Near East,

$$
\kappa_T
=1-\frac{13}{3}\varepsilon^2
+\frac{38}{9}\varepsilon^3
+O(\varepsilon^4).
$$

The exact one-segment signed object is the operator-valued transfer

$$
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S\bigl(\boldsymbol\nu e^{u\mathbb Q_y}\bigr),
$$

with all duration variables kept visible until the `J`-compatible `L^1(w)` norm.

You also proved that on an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

so the cyclic mode dimension is at least `N`. Therefore **depth-uniform finite linear mode closure is closed**, even at disagreement height zero.

Do not enlarge the finite mode alphabet.

## Objective

Attack a quantitative **profile regeneration / truncation theorem** for the common-mass hierarchy.

The aim is to replace impossible exact finite closure by an approximation whose error tends to zero in the norm actually used by the trail criterion.

The preferred result is one of the following equivalent forms.

### A. Spatial truncation theorem

Construct projections or truncation maps `Pi_M` which retain only the dependence within `M` sites of the moving trail boundary, and prove a depth-uniform estimate of the form

$$
\|\mathfrak T^{\rm block}(\nu)
-\mathfrak T^{\rm block}(\Pi_M\nu)\|_{L^1(w)}
\le \delta_M\|\nu\|_*,
$$

with

$$
\delta_M\to0
\qquad(M\to\infty),
$$

uniformly over the remaining spatial/trail depth and over the finite coupling phases allowed by G, at each fixed strict residual parameter point.

### B. Ancestry-tail theorem

Give an equivalent graphical formulation. Decompose the common-mass contribution according to whether its dependence reaches farther than `M` sites into the left block. Prove that the right-weighted `J`-compatible mass of the `>M` ancestry part tends to zero as `M->infinity`, uniformly in total remaining trail depth.

Environment-independent reset clocks of rates

$$
a
\qquad\text{and}\qquad
1-c
$$

are the natural regeneration mechanism to test. A successful proof should make explicit why a sufficiently placed reset erases dependence on deeper common-mass ancestry and how this interacts with the segment weight `w(u)`.

### C. Exact obstruction

If such depth-uniform truncation is false, exhibit a mathematically explicit obstruction showing that the common-mass hierarchy carries non-negligible `J`-weighted dependence arbitrarily far from the moving boundary.

## Required norm discipline

The Meeting 009 norm-order obstruction remains mandatory.

Do not integrate a duration before an absolute value if the actual trail quantity keeps that duration visible. In particular, any truncation error must be estimated in a profile norm compatible with

$$
\int\prod_j w(u_j)\,|\cdot|\,du,
$$

not by a signed duration average followed by absolute value.

Coefficientwise total variation is also not automatically admissible: the already-audited `cZ>1` and `7/5` examples show that taking absolute values too early can destroy the cancellation needed for the route.

## Use the favorable scalar modes

The truncation argument should exploit, rather than discard,

$$
\kappa_E<\frac23,
\qquad
\kappa_T<1.
$$

One plausible strategy is to identify regeneration times at which a deep profile is projected onto the equilibrium/transient sector plus a shorter residual hierarchy, then iterate the strict losses. Another is to prove that repeated independent resets create an exponentially decaying influence cone for the common-mass law after integration against `w`.

Do not assume either mechanism works without proving the exact conditioning and norm estimates.

## Interface with Student G

Student G is still in flight on Assignment 005, solving or refuting the finite 16-phase coupling Foster feasibility problem.

Do not interrupt or depend on its success.

Your theorem should be formulated so that, if G later supplies a valid finite coupling cocycle/return mechanism, the profile truncation can be tensorized or conditioned on those finite phases.

A successful truncation result must explain explicitly how the following would combine:

1. G's hypothetical all-height coupling Foster return;
2. finite-`M` signed/profile control;
3. a truncation error `delta_M->0`;

to yield a strict block contraction for sufficiently large but finite `M`, and hence

$$
J_{x,r}\to0.
$$

Do not claim this final implication unless every required estimate is actually stated.

## What not to do

Do not:

- enlarge the exact finite generator-mode space;
- report only computations at larger finite `M`;
- use the degree-raising hierarchy itself as evidence of truncation without a quantitative tail bound;
- integrate duration before the `L^1(w)` norm;
- replace the common-mass law by unrestricted total variation;
- assume G Assignment 005 succeeds;
- revisit one-step `(T)`, the empty `max{c,g}Z<1` criterion, or the exposed-only Foster product.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/010-profile-regeneration-truncation.md`

with exact code/certificates beside it if useful.

End with one of:

- `profile regeneration/truncation proved: ...`;
- `ancestry tail proved: ...`;
- `profile hierarchy obstructs truncation because: ...`;
- `unresolved after substantive work; exact profile-tail blocker: ...`.
