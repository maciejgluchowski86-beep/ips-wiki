---
title: Chronology-averaged sign route for one-dimensional FA-1f
status: conditional
tags:
  - FA-1f
  - out of equilibrium
  - duality
  - chronology
  - negative fugacity
---

# Chronology-averaged sign route for one-dimensional FA-1f

This entry records a conditional route to the unresolved all-density
out-of-equilibrium problem for the one-dimensional [FA-1f
model](fa-1f-model.md). The exact reductions below are proved; the punctured
positivity statement is a proposed lemma. In particular, this page does not
claim a proof of all-density convergence.

**Status reference.** Martinelli, Shapira, and Toninelli, *Long time behaviour
of one facilitated kinetically constrained models: results and open problems*,
[arXiv:2510.20461](https://arxiv.org/abs/2510.20461), state the all-density
Bernoulli convergence assertion as an open conjecture.

Use vacancy variables \(z_x\in\{0,1\}\), where \(z_x=1\) is vacant. The
equilibrium vacancy density is \(q\in(0,1)\), and \(p=1-q\). The process starts
from product Bernoulli vacancy density \(q_0\), and

$$
r=1-q_0,
\qquad
a=1-\frac{q_0}{q}=\frac{r-p}{q}.
$$

The unresolved regime is \(q_0\geq2q\), or equivalently
\(a\in[-p/q,-1]\) and \(0\leq r\leq p-q\).

## The positive set dual and the sign target

Let \((A_t)_{t\geq0}\) be the finite-set process in which every \(x\in A\)
rings at rate one, retains \(x\), and overwrites membership of \(x-1\) and
\(x+1\) by two independent Bernoulli-\(q\) variables. This process is a
positive dual for the centered functions

$$
H(A,z)=\prod_{x\in A}\left(1-\frac{z_x}{q}\right).
$$

In particular,

$$
\nu_{q_0}P_tH(A,\cdot)
=
\mathbb E_A\left[a^{|A_t|}\right].
\tag{1}
$$

For the singleton initial set, put \(N_t=|A_t|\) and

$$
G_t(r)
=
\frac{1}{a}\mathbb E_{\{0\}}\left[a^{N_t}\right],
\tag{2}
$$

with the value at \(a=0\) interpreted by polynomial continuation. The basic
finite-time sign target is

$$
G_t(r)\geq0,
\qquad 0\leq r\leq p,\ t\geq0.
\tag{3}
$$

Indeed, if \(\rho_t=(\nu_{q_0}P_t)(z_0)\), then (1) gives

$$
1-\frac{\rho_t}{q}
=
\mathbb E_{\{0\}}[a^{N_t}]
=
aG_t(r).
$$

Since \(p-r=q_0-q\), this also gives the exact normalization

$$
G_t(r)=\frac{\rho_t-q}{q_0-q}
\tag{4}
$$

away from \(q_0=q\), with the equilibrium value again obtained by
continuation.

For \(q_0\geq q\), one has \(a\leq0\), so (3) implies
\(\rho_t\geq q\). The limit-point theorem and stationary-measure
classification used in the cited review say that every weak limit point is a
mixture of the equilibrium product law and the fully occupied trap. The
vacancy lower bound excludes a nonzero trap component. Together with the
already proved range \(q_0<2q\), (3) would therefore prove convergence from
every nontrivial Bernoulli initial law.

## A sufficient shield inequality

Return to occupied variables \(\eta_x=1-z_x\). Define

$$
g(t)=\mathbb E[p-\eta_0(t)]=\rho_t-q
$$

and the minimal shield moment

$$
S(t)
=
\mathbb E\left[
(p-\eta_0(t))\eta_{-1}(t)\eta_1(t)
\right].
\tag{5}
$$

The generator gives the exact scalar equation

$$
g'(t)=-g(t)+S(t).
\tag{6}
$$

Consequently, \(S(t)\geq0\) for all \(t\) is sufficient for (3), since then
\(g(t)\geq e^{-t}g(0)\). Notice that only the two occupied neighbours in (5)
are needed. Coefficientwise positivity with arbitrary additional occupied
sites is a strictly stronger statement and is false.

## A weaker adjacent-repulsion criterion

There is a strictly weaker sufficient condition that involves only the
two-point function. In vacancy variables, set

$$
\rho(t)=\mathbb E[z_0(t)],
\qquad
b(t)=\mathbb E[z_0(t)z_1(t)],
\qquad
y(t)=\rho(t)^2-b(t).
\tag{7}
$$

The two adjacent sites have a closed evolution equation. Indeed, on the
event \(z_1=1\), site \(0\) is facilitated, and conversely. Hence

$$
b'(t)=2q\rho(t)-2b(t),
\tag{8}
$$

and therefore

$$
b(t)
=
e^{-2t}q_0^2
+2q\int_0^t e^{-2(t-s)}\rho(s)\,ds.
\tag{9}
$$

It follows that

> **Adjacent-repulsion criterion.** If
> \(\operatorname{Cov}(z_0(t),z_1(t))\leq0\), equivalently \(y(t)\geq0\),
> for every \(t\geq0\), then \(\rho(t)\geq q\) for every \(t\geq0\).

To prove the assertion, suppose that \(q_0>q\) and let \(t_*\) be a first
time at which \(\rho(t_*)=q\). Formula (9) and
\(\rho(s)>q\) for \(0\leq s<t_*\) give

$$
\begin{aligned}
b(t_*)
&>
e^{-2t_*}q_0^2
+2q^2\int_0^{t_*}e^{-2(t_*-s)}\,ds
\\
&=
q^2+e^{-2t_*}(q_0^2-q^2)
>q^2.
\end{aligned}
$$

This contradicts \(b(t_*)\leq\rho(t_*)^2=q^2\). The case \(q_0=q\) is
stationary.

The criterion is weaker than pointwise shield positivity. Combining (6) with
\(\rho'=q-\rho+S\) and (8) gives the exact identity

$$
y'(t)=2\rho(t)S(t)-2y(t),
\qquad
y(0)=0,
\tag{10}
$$

or

$$
y(t)
=
2\int_0^t e^{-2(t-s)}\rho(s)S(s)\,ds.
\tag{11}
$$

Thus adjacent repulsion asks only for an exponentially smoothed shield
inequality. It neither asserts nor requires full negative association; that
stronger property fails in finite-cycle tests, where distance-two vacancy
covariances can be positive.

The stationary-mixture test is especially sharp for (7). A stationary law
\(\lambda\mu_q+(1-\lambda)\delta_{\mathbf 1}\) has

$$
\rho=\lambda q,
\qquad
b=\lambda q^2,
\qquad
\operatorname{Cov}(z_0,z_1)
=
\lambda(1-\lambda)q^2.
\tag{12}
$$

Every nontrivial mixture therefore has strictly positive adjacent covariance.

### A two-site invariant cone and the endogenous-boundary gap

The adjacent-repulsion criterion has a useful two-site comparison behind it.
This comparison is exact, but its hypothesis is not automatically available
for the FA-1f marginal.

Let \((X,Y)\in\{0,1\}^2\) be vacancy variables. Suppose that \(X\) refreshes
to Bernoulli-\(q\) at rate

$$
\alpha+(1-\alpha)Y,
$$

and \(Y\) refreshes at rate \(\beta+(1-\beta)X\), where
\(\alpha,\beta\in[0,1]\) are exogenous parameters. Thus a vacancy at the
other central site gives rate one, while an exterior signal supplies the
remaining refreshes. Put

$$
u=\mathbb P(X=1),
\qquad
v=\mathbb P(Y=1),
\qquad
\Delta
=
\mathbb P(00)\mathbb P(11)-\mathbb P(01)\mathbb P(10).
\tag{12a}
$$

For a binary pair, \(\Delta=\operatorname{Cov}(X,Y)\). The region

$$
u\geq q,
\qquad
v\geq q,
\qquad
\Delta\leq0
\tag{12b}
$$

is forward invariant, also for time-dependent exogenous parameters. Indeed,
on the face \(u=q\),

$$
u'
=(1-\alpha)\bigl(qv-\mathbb E[XY]\bigr)
\geq0
$$

under \(\Delta\leq0\), and the analogous assertion holds on \(v=q\). On the
face \(\Delta=0\), the pair law is the product law with marginals \(u,v\),
and direct differentiation gives

$$
\Delta'
=
(1-\alpha)v(1-v)(q-u)
+
(1-\beta)u(1-u)(q-v)
\leq0.
\tag{12c}
$$

This proves the claimed invariance by the first-exit argument.

For the actual FA-1f pair \((z_0,z_1)\), the exterior signals are endogenous.
For example, when \(z_1=0\), define

$$
\alpha_x
=
\mathbb P(z_{-1}=1\mid z_0=x,z_1=0),
\qquad x\in\{0,1\}.
$$

The transitions out of pair states \(00\) and \(10\) then involve
\(\alpha_0\) and \(\alpha_1\), respectively, rather than one common
exogenous rate. At \(\Delta=0\), the left-boundary contribution to
\(\Delta'\) is exactly

$$
v(1-v)
\left[
q(1-\alpha_0)(1-u)
-p(1-\alpha_1)u
\right].
\tag{12d}
$$

Since \(u\geq q\), this term is nonpositive if

$$
\mathbb P(z_{-1}=1\mid z_0=0,z_1=0)
\geq
\mathbb P(z_{-1}=1\mid z_0=1,z_1=0).
\tag{12e}
$$

The reflected inequality controls the right-boundary contribution. Hence
(12e) and its reflection, needed only at a first boundary point
\(\Delta=0\), would close the adjacent-repulsion proof. Inequality (12e) is a
conditional adjacent-vacancy repulsion statement with the next site fixed
occupied. It holds with equality at time zero, but its preservation has not
been proved. This identifies the precise endogenous-boundary gap; replacing
the outer paths by independent or deterministic enabling signals would erase
the main difficulty.

## An isolated-insertion formulation

In a finite cycle, identify a configuration with its vacancy set \(A\), and
write \(\pi=\mu_q\). For \(0<q_0<1\), the initial likelihood with respect to
\(\pi\) is, up to a positive constant,

$$
f_0(A)=\theta^{|A|},
\qquad
\theta=\frac{q_0p}{q(1-q_0)}.
\tag{13}
$$

Reversibility gives \(f_t=P_tf_0\). Consider the following pointwise
strengthening of the shield inequality:

> **Isolated-insertion inequality.** If
> \(i,i-1,i+1\notin A\), then
> $$
> f_t(A\cup\{i\})\geq f_t(A).
> \tag{14}
> $$

For \(q_0\geq q\), (14) holds at time zero because \(\theta\geq1\). If it
were preserved by the semigroup, it would imply \(S(t)\geq0\). In fact, sum
over exterior configurations \(A\) with \(i-1,i+1\notin A\). Since
\(\pi(A\cup\{i\})=(q/p)\pi(A)\), their contribution to the shield moment is

$$
q\,\pi(A)\bigl(f_t(A\cup\{i\})-f_t(A)\bigr),
\tag{15}
$$

which is nonnegative under (14).

The remaining obstruction can be stated exactly. Put

$$
D_i f(A)=f(A\cup\{i\})-f(A),
$$

where \(i\notin A\), and suppose that \(i,i\pm1\notin A\). For the adjacent
update \(j=i+1\), write \(k=i+2\). At a boundary point
\(D_i f(A)=0\), the contribution of this update to
\(D_i\mathcal Lf(A)\) is

$$
\begin{cases}
qD_i f(A\cup\{j\}), & k\in A,\\
qD_j f(A\cup\{i\}), & k\notin A.
\end{cases}
\tag{16}
$$

These are cluster-extension gradients, not isolated-insertion gradients, and
they do not have a fixed sign. Consequently the cone defined only by (14) is
not manifestly generator-invariant. A proof by this route needs an enlarged
interval-discrepancy hierarchy whose boundary terms reduce to (14), or a
chronology pairing that cancels the two terms in (16) after averaging.

There is also a useful reversible interpretation. In a finite volume, let
\(\mu_p\) be equilibrium and let \(f_r=d\mu_r/d\mu_p\). Up to a positive
constant,

$$
f_r(\eta)=\lambda^{|\eta|},
\qquad
\lambda=\frac{rq}{p(1-r)}\leq1.
$$

Multiplication of \(\mu_p\) by the integrand in (5) gives equal positive and
negative masses to the local patterns \(101\) and \(111\), respectively.
Self-adjointness therefore turns (5) into a comparison of a radial decreasing
function after starting with one fewer occupied site at a site whose two
neighbours are occupied. Ordinary coordinatewise attractiveness is not
required; the relevant order is an order of total occupied-site counts after
chronology averaging.

## Fixed-count chronology averaging

Let \(T_j\) be the one-ring heat-bath operator at \(j\), and let
\(\chi_A=\prod_{x\in A}\eta_x\). For \(j\in A\),

$$
T_j\chi_A
=
p\chi_{A\setminus\{j\}}
-p\chi_{(A\setminus\{j\})\cup\{j-1,j+1\}}
+\chi_{A\cup\{j-1,j+1\}},
\tag{17}
$$

while \(T_j\chi_A=\chi_A\) for \(j\notin A\). Conditional on the number of
rings at every site, continuous time averages (17) uniformly over all words
with that site content. Thus the sign question is intrinsically a shuffled
word question, not a question about a single chronological word.

A homogeneous three-colour expansion uses

$$
R=r,
\qquad
S=p-r,
\qquad
Q=q,
\qquad
p=R+S,
\qquad
1=R+S+Q.
$$

If \(F_B^{\boldsymbol n}\) denotes the unnormalised fixed-count shuffle
polynomial for \(\chi_B\), the minimal shield polynomial is

$$
(R+S)F_{\{i-1,i+1\}}^{\boldsymbol n}
-(R+S+Q)F_{\{i-1,i,i+1\}}^{\boldsymbol n}.
\tag{18}
$$

Coefficientwise nonnegativity of (18) for every finite count vector would imply
(5). A binary history interpretation adds one independent equilibrium
“ghost” bit at \(i\). Positive histories end in \(101\) with ghost \(1\),
and negative histories end in \(111\) with ghost \(0\). The strongest tested
combinatorial form asks for an injection from negative to positive histories
that preserves the total number of one-tokens in every site column and does
not increase the number of initially occupied sites. Permuting clock order
and proposal order within site columns is therefore part of the proposed
comparison.

There is an exact oriented factorisation behind this formulation. If
\(E_i^-\) refreshes \(i\) only when \(i-1\) is vacant and \(E_i^+\) refreshes
\(i\) only when \(i+1\) is vacant, then

$$
T_i=E_i^-E_i^+=E_i^+E_i^-.
\tag{19}
$$

Formula (19) avoids expanding the two-sided constraint as an oriented term
minus an overlap term. It does not by itself prove (18), because oriented
factors at adjacent sites still have to be chronologically interleaved.

## Last-ring reduction and the punctured source

The sharpest surviving reduction is obtained directly from the positive dual.
For \(0\leq r\leq p\), define

$$
J_t(r)
=
\mathbb E_{\{0\}}\left[
\sum_{x\in A_t}
a^{|A_t\setminus\{x-1,x+1\}|-1}
\right].
\tag{20}
$$

Since \(x\in A_t\), the exponent in (20) counts precisely the particles at
distance at least two from \(x\):

$$
a^{|A_t\cap(-\infty,x-2]|}
a^{|A_t\cap[x+2,\infty)|}.
\tag{21}
$$

An exact generator calculation gives

$$
\partial_tG_t(r)
=
-G_t(r)+(p-r)\partial_rG_t(r)+r^2J_t(r),
\qquad
G_0(r)=1.
\tag{22}
$$

Let

$$
\Phi_u(r)=p+(r-p)e^{-u}.
$$

Solving (22) along characteristics yields

$$
G_t(r)
=
e^{-t}
+\int_0^t
e^{-(t-s)}
\Phi_{t-s}(r)^2
J_s\bigl(\Phi_{t-s}(r)\bigr)
\,ds.
\tag{23}
$$

Formula (23) also has a direct chronological meaning. The first term is the
history with no dual ring. In the integral, expose the globally last ring.
The retained source cancels the one factor \(a\) divided out in (2), while its
two independently refreshed neighbours give the positive square
\(\Phi_{t-s}(r)^2\). What remains is exactly the left-right punctured moment
(20)--(21).

This isolates the proposed lemma:

> **Rooted punctured positivity.** For the one-dimensional two-sided dual,
> \(J_t(r)\geq0\) for every \(t\geq0\) and \(0\leq r\leq p\).

By (23), rooted punctured positivity implies (3) and hence the qualitative
all-density convergence theorem. A coefficientwise strengthening in powers
of \(r\) would also imply the observed Bernoulli-thinning representation

$$
G_t(r)=\sum_{k\geq0}d_k(t)r^k,
\qquad
d_k(t)\geq0,
\qquad
\sum_kd_k(t)=1.
\tag{24}
$$

The geometry in (21) is genuinely two-sided: the last source leaves a product
of a left and a right punctured fugacity. The analogous one-sided East
reduction leaves only one half-line factor, so the same prospective pairing is
not available.

## Ruled-out strengthenings

The following facts delimit the proposed lemma.

1. Deterministic update words, arbitrary extra occupied shields, word-reversal
   pairs, and simple one-sided comparisons all have counterexamples. Exact
   enumeration has not found a counterexample for the minimal shield under
   the full fixed-count shuffle in the tested finite ranges; this is evidence,
   not a proof. On three update sites, the minimal shield also survived every
   deterministic word through length seven, so known deterministic-word
   failures use a stronger shield event.

2. Merely averaging the ranks of the last outgoing updates is insufficient.
   On a three-site path, a uniform permutation has one local maximum in four
   orders and two local maxima in two orders. Even after cancelling one root
   sign, its naive peak weight is

   $$
   4r^2+2ar.
   $$

   For \(q=1/3\), this is \(2r(5r-2)\), which is negative for
   \(0<r<2/5\). The no-ring term and the last-ring square in (23) cannot be
   discarded.

3. A pathwise representation by one forced particle plus independent
   Bernoulli-\(q\) optional particles is not invariant. If an optional site
   far from the forced particle rings, its count generating factor contains

   $$
   p+qzb^2=p-pb^2+b^3,
   \qquad
   b=p+qz,
   $$

   whose \(b^2\) coefficient is negative. Any successful thinning proof must
   average which active site rings; it cannot condition on a single optional
   ring.

4. The two one-sided refresh projections in (19) commute at one site, but the
   transformed synchronized kernel still has negative entries. Dirichlet-form
   comparison with BABP therefore controls equilibrium relaxation but not the
   negative-fugacity moment.

The remaining task is consequently narrower than full patch positivity and
broader than a local rank count: prove the rooted, two-sided chronology average
in (20), preferably in the per-site-column refinement of (18). That formulation
keeps the order permutation explicit while avoiding the false dual-sign and
one-forced-profile closures.
