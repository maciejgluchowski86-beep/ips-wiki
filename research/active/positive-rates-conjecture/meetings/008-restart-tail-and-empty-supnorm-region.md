# Group meeting 008: same-parent restart tail is geometric; crude sup-norm region is empty on the residual chamber

Date: 2026-08-16

Professor review of:

- Student G, commit `0ca3fd1`, `students/student-g/003-restart-count-block-bridge.md`;
- Student G verifier commit `75b700f`, `students/student-g/003-restart-count-verifier.py`;
- Student F Phase-A verifier commit `0755d22`, `students/student-f/007-block-mass-disagreement-verifier.py`;
- Student F completed write-up commit `3cb6ac9`, `students/student-f/007-block-mass-disagreement-contraction.md`;
- Meetings 006--007 and the current block mass/disagreement proof spine.

state_narrowed: yes

Evidence pointer: `students/student-g/003-restart-count-block-bridge.md`, especially Sections 2--8; `students/student-f/007-block-mass-disagreement-contraction.md`, especially Sections 5--7; and both exact verifier files.

## Previous bottleneck

Meeting 007 established exact control of one live exposure edge but left repeated exposure re-entry/restart count as the coupling-side obstruction to an all-depth mass/disagreement block theorem. Meeting 006 also recorded a crude right-weighted sufficient condition `max{c,g}Z<1` as giving an already-proved residual subregion.

Both points are now sharpened. G proves a genuine geometric tail for **same-parent** re-entries. F proves that the claimed crude residual subregion is actually empty.

## Professor verification: G's same-parent restart tail

Let an exposed parent disagreement at site `i+1` be fixed, and let `N` be the number of entries of the edge `(i,i+1)` into the exposure state `D_i=0,D_{i+1}=1` before that same parent disagreement first coalesces. Meeting 007 gives, at every exposure entry,

$$
P(\text{child before parent coalescence}\mid\mathcal F)\le h_1=:h<1,
$$

uniformly over orientation and all deeper ancestry.

For `N>=n+1`, the `n`th exposure must end by child creation before parent coalescence, and the child must later disappear while the parent remains alive so that another exposure can occur. The first requirement alone has conditional probability at most `h`; the second only lowers the probability. Therefore strong Markov gives

$$
\boxed{
P(N\ge n\mid\mathcal F)\le h^{n-1},\qquad n\ge1.
}
$$

This is correct and is a genuine all-reentry theorem for one parent episode.

For `1\le s<h^{-1}`, the tail-sum identity gives

$$
\boxed{
E[s^N\mid\mathcal F]
\le M(s):=\frac{(1-h)s}{1-hs}.
}
$$

The verifier checks the corresponding pgf algebra.

## Height minorant and the `16/21` diagnostic

From the accepted stack-clearing tail, write

$$
\alpha=\frac{B+\omega}{B+2\omega},
$$

and use the geometric minorant `kappa` with

$$
P(\kappa=0)=1-\alpha,
\qquad
P(\kappa=j)=\alpha2^{-j},\quad j\ge1.
$$

Then

$$
\phi(\lambda)
=
\lambda\left(1-\alpha+\frac{\alpha}{2\lambda-1}\right),
$$

and the exact factorization

$$
\phi(\lambda)-1
=
\frac{(\lambda-1)(-B+2\lambda\omega-2\omega)}
{(B+2\omega)(2\lambda-1)}
$$

shows `phi(lambda)<1` for

$$
1<\lambda<\frac{B+2\omega}{2\omega}.
$$

Combining the **scalar** same-parent pgf cost with this height minorant gives the algebraic candidate factor `M(s)phi(lambda)`. Along the near-East path, the proposed choice `lambda=2`, `s=1+epsilon^2/4` indeed satisfies

$$
M(s)\phi(2)\longrightarrow\frac{16}{21}<1.
$$

This calculation is correct as a stress test.

I do **not** yet promote G's full Proposition 5.1 / Corollary 6.1 to Professor-verified status. The report compresses the restart histories of all simultaneously unresolved parent levels into a product corrector `C_s` and then states the global Foster inequality (5.4). To carry a closing proof, this needs an explicit global phase state and a transition-by-transition superharmonicity argument showing that inactive/exposed/child-alive phases and new-parent reinfections are all prepaid by the claimed factors. The exact verifier checks the scalar pgf, height minorant, truncation algebra, and near-East limit, but not this global product-corrector step.

Thus the **same-parent restart bundle is closed**, while the lift to a global restart-corrected stack remains a sharply defined technical lemma.

## Professor verification: F's correction to the crude right-weighted region

Put

$$
B=b+c-a,
\qquad
g=b-a,
\qquad
\omega=1-c+a,
$$

and

$$
Z=
\frac{a+b+2}{2ab+3a-bc+b-2c+2}.
$$

In the residual chamber, `c>=a+b` and `a>0` imply

$$
c>b>g,
$$

so `max{c,g}=c`.

F proves, by the change of variables `x=1-c` and a complete split according to whether `2b+x<=1` or `>=1`, that

$$
\boxed{cZ>1\quad\text{throughout }\mathcal R.}
$$

I checked the endpoint argument. The key quantity

$$
F(a,b,c)
=
2ab-ac+3a-2bc+b-4c+2
$$

is increasing in `a`; maximizing under the residual constraints reduces to the two boundary functions treated in F's Sections 6.1--6.2, and both are strictly negative. Hence

$$
\boxed{\max\{c,g\}Z<1\text{ has no solution in the residual chamber}.}
$$

This corrects Meeting 006 and all later state files that described the condition as proving a residual subregion. The conditional implication `max{c,g}Z<1 => crude trail-depth decay` remains true, but it contributes nothing on the unresolved chamber.

## No conflict between `cZ>1` and `16/21<1`

These are different multipliers.

- `cZ` is the worst-case **raw scalar centered-insertion magnitude** after segmentwise right killing. It ignores the mass/disagreement decomposition and is expansive everywhere on the residual chamber.
- `M(s)phi(lambda)` is a **coupling-side restart/height Lyapunov factor** after same-parent re-entries are bundled and stack clearing is charged. It does not contain the signed mass coefficient or the bounded-height mass/disagreement branching kernel.

Therefore F's endpoint theorem does not contradict G's near-East `16/21` calculation. Conversely, `16/21<1` does **not** imply decay of the global trail quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

Even if G's global Foster lift is completed, the bounded-height signed branching kernel still has to contract. This is exactly where the raw scalar estimate fails and where mass/disagreement cancellation must enter.

## Revised decomposition of the remaining block theorem

The current block target now separates into two finite tasks.

1. **Global restart-corrector lemma.** Upgrade G's verified same-parent geometric tail and height minorant to a rigorously defined global phase process with a true Foster inequality and a finite-state reduction outside bounded height.
2. **Bounded-height signed kernel.** On the resulting bounded height/phase set, compute or estimate the right-weighted mass/disagreement transfer, including the coefficients
   $$
   (Br-c)\bar\mu
   \quad\text{and}\quad
   Br(1-r)(\mu^1-\mu^0),
   $$
   and prove block spectral radius `<1` or exhibit an exact obstruction.

These tasks are complementary. Neither the empty crude region nor the verified same-parent restart tail decides the bounded signed kernel.

## Ruling

The programme has narrowed again.

- The purported easy residual region from Meeting 006 is removed completely.
- Same-parent exposure re-entry is no longer an unbounded mystery: it has a uniform geometric tail and exponential moment at every strict residual point.
- The remaining coupling-side issue is the global product/phase corrector across different parent episodes and stack levels.
- Conditional on that reduction, the remaining analytic issue is finite: the bounded-height signed mass/disagreement kernel.

Student F should attack the bounded-height signed kernel, taking the global Foster reduction as an explicitly named conditional premise until G completes it. Student G should formalize the global restart-corrector state and prove or refute the Foster lift. No further crude scalar sup-norm or single-exposure calculations count as progress.
