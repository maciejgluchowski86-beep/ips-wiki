# Group meeting 001: density estimates obtained; composition bottleneck is regional insertion positivity

Date: 2026-08-16

Professor review of:

- Student F, commit `db49c30`, `students/student-f/001-last-interaction-reduction.md`;
- Student G, commit `1f41488`, `students/student-g/001-independent-structural-attack.md`;
- the surviving principal barrier--scaffold note used by Student F;
- the inherited closed finite-wall route on `research/noisy-east-positive-rates`.

state_narrowed: yes

Evidence pointer: the two student reports above, especially F Sections 3--12 and G Sections 1--7.

## Previous bottleneck

At Meeting 000 the unresolved question was whether the principal's remembered last-successful-interaction construction yields any genuinely one-way high-density reduction rather than another equivalent representation.

## What has become strictly narrower

Two things are now established at finite time without assuming ergodicity.

First, Student F identified the exact signed insertion appearing when the successful birth-versus-jump type is hidden and proved a uniform conditional estimate for the noise-reduced dynamics that has exactly the required sign. The vague phrase "high density" is therefore no longer the missing mathematics.

Second, Student G proved independent transient finite-box density and pair-suppression estimates for the **original** normalized IPS. Thus there is now genuine density information on the actual residual dynamics, not merely a proposed density criterion.

The remaining obstruction is a much more local and falsifiable statement: after the last-exit/scaffold geometry is revealed but the successful interaction type is kept hidden, does the regional companion kernel satisfy the insertion inequality needed to use F's conditional estimate? The raw Duhamel kernel does not have the required one-sided measurability.

## Professor verification of Student F's load-bearing claims

Work on the normalized face

$$
r_{11}=0,\qquad r_{00}=a,\qquad r_{01}=b,\qquad r_{10}=c,
$$

and put

$$
B=b+c-a,\qquad \rho=\frac{c}{B}.
$$

I rederived the local monomial algebra. In the complemented variable used by the patch paper, the source-retaining successful dual type has coefficient `+B` and the source-removing type has coefficient `-c`. If the interaction location/time is revealed but its type is hidden, the signed type average is exactly

$$
B\eta_i-c=B(\eta_i-\rho).
$$

I also checked the three-generator identities from the local rate tables. In the old spin convention,

$$
L=L^-+aN^\uparrow,
$$

and after complementing spins this is deletion of an environment-independent pure-death component. The unsigned comparison system satisfies

$$
L^+=L^-+2cC,
$$

where `C` copies the right neighbour at a domain wall. Hence the Duhamel identity

$$
U^-_{s,t}-U^+_{s,t}
=-2c\int_s^t U^-_{s,u}C_uU^+_{u,t}\,du
$$

has the stated sign and normalization.

The uploaded barrier--scaffold note does contain the local derivation error F identified: its displayed formula for the monomial generator omits the diagonal `-c_{11}H(A)` term even though the later Feynman--Kac potential already contains the corrected `-c_{11}-c_{01}` contribution. The interval orientation typo in the barrier absence statement is also as F says. These are corrections to the old note, not new assumptions.

For `L^-`, condition on the complete graphical history strictly to the right of site `i`. The remaining spin at `i` is a two-state chain driven by the prescribed right-neighbour path. When that neighbour is `0`, its canonical-spin one-probability `p` satisfies

$$
p'=1-(1+b-a)p,
$$

and when the neighbour is `1`,

$$
p'=(1-c)(1-p).
$$

The scalar comparison in F is correct. Uniformly over initial configurations and right-hand histories,

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
q(t)=\frac{1-e^{-(1-c)t}}{1+b-a}.
$$

Moreover

$$
\frac1{1+b-a}-\rho
=
\frac{(b-a)(1-c)}{B(1+b-a)}>0,
$$

so for

$$
T_\rho=
\frac1{1-c}\log\frac{B}{(b-a)(1-c)}
$$

one has `q(t)>=rho` for `t>=T_rho`. Therefore for every nonnegative right-history-measurable `F`,

$$
\boxed{
\mathbb E^-[(B\eta_i(t)-c)F]\ge0,
\qquad t\ge T_\rho.
}
$$

This is a real target-relevant estimate and not a reformulation of ergodicity.

I also checked F's warning that one cannot insert this estimate directly into the raw Duhamel integral. For `f(eta)=eta_{i-1}`,

$$
D_i(U_t^+f)
=t(c+B\eta_{i-1})+O(t^2),
$$

so the companion factor already depends on a left spin at first order. The right-conditioned lemma therefore does not apply to the ungrouped Duhamel kernel.

Finally, F's long-patch sign calculation gives

$$
\lim_{\Delta\to\infty}N(\Delta,1)
=
\frac{b(1-c)-a}{1+b}.
$$

Thus on the hard side `a>b(1-c)` there are negative long OI patch contributions. This rules out completing the hard subregion by taking patchwise absolute values or demanding positivity patch by patch. It does **not** rule out a coarser regional cancellation after successful interaction types are left hidden.

## Professor verification of Student G's load-bearing claims

Student G works in the original normalized spin convention. Let

$$
m_i(t)=\mathbb E[\eta_i(t)],\qquad
q_i(t)=\mathbb P(\eta_i(t)=0,\eta_{i+1}(t)=0),
$$

and set

$$
k=1+b+c,\qquad A=b+c-a.
$$

Direct expansion of the four two-site states gives the exact identity

$$
\boxed{
\frac d{dt}m_i
=(b+c)-km_i-Aq_i+c(m_i-m_{i+1}).
}
$$

Summing over an interval telescopes the last term. Dropping the nonpositive `-A q_i` contribution yields, uniformly over initial condition and prescribed right-boundary history,

$$
\boxed{
\frac1L\sum_{i\in I}\mathbb P(\eta_i(t)=0)
\ge
\frac{1-e^{-kt}}{k}\left(1-\frac cL\right).
}
$$

This calculation is correct. It is a transient statement on the original dynamics; invariance is used only afterward for the invariant-law corollary.

The one-sided finite-propagation estimate is also correct: influence across `R` sites by time `t` requires an ordered chain of `R` rate-one clock rings, hence is bounded by

$$
H_R(t)=\mathbb P(\operatorname{Pois}(t)\ge R).
$$

The residue-class truncation then gives the stated finite-box concentration estimate; the disjoint truncated cones make each residue class independent conditional on the initial configuration.

For the adjacent pair observable `v_i=P(11)`, direct generator expansion gives

$$
v_i'(t)
\le b-(1+b)v_i(t),
$$

hence

$$
v_i(t)\le\frac{b+e^{-(1+b)t}}{1+b}.
$$

At

$$
t_b=\frac{\log(1/b)}{1+b},
$$

this yields `v_i(t_b)<=2b`, so a union bound gives the claimed mesoscopic no-`11` event on boxes of length `o(1/b)`. This is again genuine transient information, not an invariant-measure restatement.

## Do the two density results compose?

Not directly. This is important enough to record now so that the next block does not spend time combining incompatible statements by terminology alone.

F's insertion estimate concerns the **noise-reduced process `L^-`**, is conditional on the entire right-hand history, and must hold after weighting by a companion functional. G's estimate concerns the **original process `L`** and gives spatial-average/high-probability density information without the required conditional weighting.

There is also a numerical mismatch if one ignores that structural distinction. G's asymptotic guaranteed zero-density floor is

$$
\theta_G=\frac1{1+b+c},
$$

where G's zero is F's canonical spin `1`. F's hidden-type threshold is

$$
\rho=\frac{c}{b+c-a}.
$$

Throughout the residual chamber,

$$
\rho>\theta_G.
$$

Indeed

$$
c(1+b+c)-(b+c-a)
=a+c^2-b(1-c)>0,
$$

because `c>b` and `c>=1/2` imply `c^2>b(1-c)`. Likewise the hard-core event guarantees at least one half zeros, but

$$
\rho>\frac12
$$

because `b-a<c`, hence `B=c+b-a<2c`.

So neither of G's present density bounds reaches the threshold in F's insertion inequality, even before accounting for the fact that they concern different semigroups and different conditioning. The two reports converge conceptually on density, but they do **not** yet close each other's missing step.

## Ruling

The programme has narrowed. We now have two independently proved dynamical estimates and a finite regional obstruction rather than a vague high-density hope.

The next load-bearing question is **regional insertion positivity**:

> In the smallest scaffold cell containing a hidden successful interaction and a left predecessor branch, after summing the unrevealed histories with the corrected dynamic boundary rules, does the resulting companion kernel satisfy
> $$
> \mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F]
> $$
> after the required burn-in, or an equivalent one-sided inequality strong enough to make the hidden type average nonnegative?

Right-measurability is sufficient but not required. A weighted insertion inequality would be enough. This is a finite-region question and can be proved or falsified without solving the infinite-volume problem.

A negative answer on the minimal nontrivial cell closes the principal's old last-exit route in its present form. A positive answer is only useful if it survives composition along successive scaffold cells; the next assignment should therefore test one-cell positivity first and, if it passes, immediately test two-cell composition rather than declaring victory from a new representation.

## Direction

Continue on the fixed positive-rates target. Students F and G should both attack the regional-insertion/composition question with broad methodological freedom. Do not spend the next block merely strengthening unweighted density bounds unless the strengthened estimate is explicitly connected to the regional kernel or Duhamel error.
