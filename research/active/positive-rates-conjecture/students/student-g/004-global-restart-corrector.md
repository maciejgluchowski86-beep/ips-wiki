# Student G 004: the exposed-only product corrector fails; exact finite phase reduction

## Verdict

The global Foster lift claimed in Assignment 003 is **false as stated**. The failure is not in the Professor-verified same-parent tail. It is in the product rule used to combine simultaneously unresolved levels.

Assignment 003 assigned a factor `v_x(s)>=1` to an exposed parent level and factor `1` to every nonexposed unresolved level, then asserted that same-parent restart histories were thereby prepaid. A reachable same-orientation disagreement stack gives an exact counterexample to that assertion. For a stack of height `H` with coupled pair state

$$
\sigma_i=(X_i,Y_i)=(0,1),\qquad 0\le i\le H-1,
$$

between coupled zero bookkeeping boundaries, the tilted generator of the proposed corrector satisfies

$$
\boxed{
\frac{\mathscr L_s V}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1),
}
\tag{0.1}
$$

where

$$
\omega=1-c+a,
$$

`e_0` is the exposed factor when the agreed child spin is zero, and

$$
V=\lambda^H C,
\qquad
s>1,
\qquad
\lambda>1.
$$

Every Assignment-003 remaining-restart factor has `e_0>=1`. Hence the coefficient of `H-2` in (0.1) is strictly positive. For every fixed strict residual parameter point, every `s>1`, every finite `lambda`, and every such exposed-only factor,

$$
\frac{\mathscr L_s V}{V}>0
$$

for all sufficiently large `H`. Thus no transition-by-transition superharmonicity can hold uniformly in stack height for the product corrector actually proposed in Assignment 003.

The state is not artificial. Starting from a rightmost disagreement of orientation `(0,1)`, a child born from an agreed zero has the same orientation, and this can repeat at rate `b-a>0`; therefore arbitrarily long `(0,1)` runs occur with positive probability in the strict residual chamber.

On the near-East stress path

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

with the Assignment-003 choices

$$
\lambda=2,
\qquad
s=1+\frac{\varepsilon^2}{4},
$$

the old exposed factor satisfies

$$
e_0\longrightarrow\frac87,
$$

and therefore

$$
\boxed{
\frac{\mathscr L_s V}{V}
\longrightarrow
\frac{H-2}{7}>0
\qquad(H\ge3).
}
\tag{0.2}
$$

So the checked scalar diagnostic

$$
M(s)\phi(2)\to\frac{16}{21}
$$

does not lift to the old global `C_s`: already at fixed depth `H=3`, its infinitesimal tilted drift is positive for sufficiently small positive `epsilon`.

This does **not** refute the centered-trail route, the same-parent geometric tail, the stack-height minorant, or every possible global corrector. It refutes the exposed-only independent-level product and identifies exactly what is missing: child-alive and susceptible/reinfected phases must carry nontrivial credit.

I give below a fully explicit finite Markov phase reduction. It replaces the informal parent-level product by the 16 nearest-neighbour coupled-pair phases. Any local product/coboundary proof of the desired Foster lift is equivalent to a finite no-positive-cycle problem on a 16-vertex graph, plus the finite right-boundary height and trail-insertion inequalities. The old corrector fails this finite test by a positive self-loop.

A symbolic verifier is committed beside this report as

`students/student-g/004-global-restart-corrector-verifier.py`.

## 1. Inputs retained from Meetings 007--008

Work on the residual chamber

$$
0<a<b,
\qquad
\frac12\le c<1,
\qquad
c\ge a+b,
\qquad
b\ge\sqrt2(1-c).
$$

Set

$$
d=b-a>0,
\qquad
\omega=1-c+a>0,
\qquad
B=b+c-a.
$$

The following remain accepted.

### 1.1 Same-parent bundle

For one fixed exposed parent episode, if `N` is the number of entries of its child edge into exposure before that parent first coalesces, then

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1}.
$$

Hence

$$
E[s^N\mid\mathcal F]
\le
M(s)=\frac{(1-h_1)s}{1-h_1s},
\qquad
1\le s<h_1^{-1}.
\tag{1.1}
$$

This is a correct one-parent renewal statement.

### 1.2 Height minorant

The principal stack-clearing construction gives

$$
\phi(\lambda)
=
\lambda\left(1-\alpha+\frac{\alpha}{2\lambda-1}\right)<1
$$

on the accepted interval of `lambda>1`.

The error in Assignment 003 was to multiply these two scalar statements without proving that the restart cost of all inherited levels is represented by the proposed product phase.

### 1.3 F's correction

The crude right-weighted scalar criterion gives no residual region:

$$
\boxed{cZ>1\quad\text{throughout }\mathcal R.}
$$

Nothing below uses that criterion. In particular the obstruction (0.1) is purely on the coupling/restart side.

## 2. Exact global state and tilted generator

For a finite zero-boundary coupling, write the pair state at site `i` as

$$
\sigma_i=(X_i,Y_i)
\in
\mathcal A:=\{00,11,01,10\}.
$$

A pair is **diagonal** if it is `00` or `11`, and **off-diagonal** if it is `01` or `10`.

For adjacent pair states `alpha,beta`, define the exposure indicator

$$
E(\alpha,\beta)
=
1_{\{\alpha\text{ diagonal},\ \beta\text{ off-diagonal}\}}.
\tag{2.1}
$$

Thus `E(sigma_{i-1},sigma_i)=1` means that site `i` is a live parent disagreement whose immediate left child is agreed.

At a rate-one update of site `i`, write

$$
\beta=\sigma_i=(x,y),
\qquad
\gamma=\sigma_{i+1}=(u,v).
$$

Put

$$
p=r_{x u},
\qquad
\widetilde p=r_{y v},
$$

with

$$
r_{00}=a,
\qquad
r_{01}=b,
\qquad
r_{10}=c,
\qquad
r_{11}=0.
$$

Under the common-uniform coupling the new pair `beta'` has probabilities

$$
\begin{array}{c|c}
\beta' & \Pi_{\beta,\gamma}(\beta')\\ \hline
11 & \min(p,\widetilde p)\\
00 & 1-\max(p,\widetilde p)\\
10 & (p-\widetilde p)_+\\
01 & (\widetilde p-p)_+.
\end{array}
\tag{2.2}
$$

Only the two exposure edges touching site `i` can change. Define the exposure-entry increment

$$
\begin{aligned}
\rho(\alpha,\beta,\gamma;\beta')
={}&1_{\{E(\alpha,\beta)=0,\ E(\alpha,\beta')=1\}}\\
&+1_{\{E(\beta,\gamma)=0,\ E(\beta',\gamma)=1\}}.
\end{aligned}
\tag{2.3}
$$

For an update of one site this is `0` or `1`.

If `R_t` counts such exposure entries, the natural tilted generator acting on a positive corrector `F` is

$$
(\mathscr L_sF)(\sigma)
=
\sum_{\sigma'\ne\sigma}
q(\sigma,\sigma')
\left[s^{\rho(\sigma,\sigma')}F(\sigma')-F(\sigma)\right].
\tag{2.4}
$$

A true transition-by-transition Foster proof must make

$$
s^{R_t}F(\sigma(t))
$$

a supermartingale, possibly after including the height factor and the trail-step boundary correction.

## 3. The product from Assignment 003

The product used in Assignment 003 has the following form.

For a live parent at site `i` with an agreed child at `i-1`, assign a factor

$$
e_x=v_x(s)\ge1
$$

according to the common child spin `x`. Every other unresolved level, including a child-alive parent relation, has factor `1`.

Thus

$$
C_{\rm old}(\sigma)
=
\prod_i
\begin{cases}
 e_0,&\sigma_{i-1}=00,\ \sigma_i\in\{01,10\},\\
 e_1,&\sigma_{i-1}=11,\ \sigma_i\in\{01,10\},\\
 1,&\text{otherwise}.
\end{cases}
\tag{3.1}
$$

The exact Assignment-003 values were

$$
e_x
=s[(1-h_x)+h_xM(s)],
$$

with `e_1=M(s)`, so indeed `e_x>=1`.

The problem is now visible: when an interior disagreement coalesces, an old child-alive relation of weight `1` can become a new exposed relation of weight `e_x>1`, while also creating the restart count charged by `s`. There is no local credit in (3.1) to pay for that transition.

## 4. Exact reachable counterexample family

Fix `H>=3`. Take coupled bookkeeping boundaries `sigma_{-1}=00` and a coupled zero right boundary, and set

$$
\boxed{
\sigma_0=\sigma_1=\cdots=\sigma_{H-1}=01.
}
\tag{4.1}
$$

Only site `0` is exposed, so

$$
C_{\rm old}=e_0.
$$

Let

$$
V=\lambda^H C_{\rm old}.
$$

We compute every nontrivial contribution to `mathscr L_s V/V`.

### 4.1 Leftmost site

At site `0`, the local pair states are `(01,01)`. The update probabilities are

$$
01\to00\text{ with probability }1-a,
\qquad
01\to10\text{ with probability }a.
$$

If `01->00`, the unique exposure simply moves from site `0` to site `1`; the product remains `e_0`, but one new exposure entry is created. Hence the tilted ratio is `s`.

The `01->10` outcome leaves the old product unchanged. Therefore site `0` contributes

$$
(1-a)(s-1).
\tag{4.2}
$$

### 4.2 Interior sites

For every

$$
1\le i\le H-2,
$$

the same local transition probabilities hold. If site `i` coalesces to `00`, the original leftmost exposure survives and a **second** exposed edge is created at `(i,i+1)`. Thus

$$
C_{\rm old}: e_0\longmapsto e_0^2,
$$

and one new exposure entry is counted. The tilted ratio is therefore

$$
s e_0.
$$

The orientation-flip outcome `01->10` leaves every exposed-only factor unchanged. Each interior site contributes

$$
(1-a)(s e_0-1).
\tag{4.3}
$$

This is strictly positive for every `s>1` and `e_0>=1`.

### 4.3 Rightmost site

At the rightmost disagreement, the right neighbour is coupled zero. The pair `01` coalesces at its update with probability

$$
1-c+a=\omega.
$$

When that happens the rightmost unresolved level is permanently removed, so the height factor changes by `lambda^{-1}`. No new exposure is created at the right boundary and `C_old` is unchanged. Hence the rightmost contribution is

$$
\omega(\lambda^{-1}-1).
\tag{4.4}
$$

Combining (4.2)--(4.4) proves (0.1):

$$
\boxed{
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
}
\tag{4.5}
$$

Since the last term is a fixed boundary gain while the middle term grows linearly in `H`, the proposed corrector cannot be superharmonic at all heights.

A sufficient explicit violating depth is any integer satisfying

$$
H>
2+
\frac{\omega(1-\lambda^{-1})}
{(1-a)(s e_0-1)}.
\tag{4.6}
$$

The omitted leftmost term in (4.6) is positive, so this is conservative.

### 4.4 Reachability

The family (4.1) is compatible with the genuine coupling. If a parent disagreement has orientation `01` and its agreed left child is zero, then a child-creation update produces another disagreement of orientation `01` with probability `d=b-a>0`. Repeating this event before the existing disagreements coalesce creates an arbitrary finite run (4.1) with positive probability.

So (4.5) is a genuine live-stack obstruction, not a state excluded by the coupling geometry.

## 5. Near-East evaluation of the old factors

On

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

Assignment 003 used

$$
s=1+\frac{\varepsilon^2}{4},
\qquad
\lambda=2.
$$

The accepted one-exposure formulas give

$$
1-h_0=2\varepsilon+O(\varepsilon^2),
$$

$$
1-h_1=2\varepsilon^2+O(\varepsilon^3),
$$

and

$$
M(s)\longrightarrow\frac87.
$$

Since

$$
e_0=s[(1-h_0)+h_0M(s)],
$$

one also has

$$
\boxed{e_0\longrightarrow\frac87.}
\tag{5.1}
$$

Substituting into (4.5), while `omega=2 epsilon^2`, gives

$$
\boxed{
\frac{\mathscr L_sV}{V}
\longrightarrow
\frac{H-2}{7}.
}
\tag{5.2}
$$

Thus the old global product has order-one positive drift on a fixed three-level same-orientation stack as `epsilon->0`, even though the separately checked scalar expression `M(s)phi(2)` tends to `16/21`.

This identifies exactly why the multiplication used in Assignment 003 was invalid: `phi` pays for right-boundary height removal, whereas interior coalescences create extra exposed components at every level. Those interior components were assigned no child-alive credit before they appeared.

## 6. Minimal stronger Markov phase state

The defect cannot be repaired by merely changing `e_0,e_1` while retaining factor `1` on every nonexposed level. Equation (4.3) remains positive for every `e_0>=1`.

A correct local state must at least distinguish the complete ordered adjacent coupled-pair phase

$$
(\sigma_{i-1},\sigma_i)
\in\mathcal A^2.
$$

There are only `16` such phases. They automatically distinguish:

- inactive/susceptible parent: `sigma_i` diagonal;
- exposed parent with agreed child zero or one;
- child-alive parent with the two disagreement orientations equal or opposite;
- a parent that has coalesced while a deeper disagreement remains, through the neighbouring phase `(sigma_i,sigma_{i+1})`;
- reinfection of that site, which is simply a diagonal-to-off-diagonal transition of `sigma_i`;
- permanent removal, represented by trimming a coupled right suffix from the unresolved height.

No historical parent label is needed once these current pair states are recorded: after a parent coalesces, a later reinfection is a new episode by the strong Markov property.

Let

$$
Q=(q_{\alpha\beta})_{\alpha,\beta\in\mathcal A},
\qquad
q_{\alpha\beta}>0,
$$

and define the nearest-neighbour phase product

$$
C_Q(\sigma)
=
\prod_i q_{\sigma_{i-1},\sigma_i}.
\tag{6.1}
$$

This strictly contains the old corrector (3.1).

## 7. Exact 64-transition bulk criterion

For a triple

$$
(\alpha,\beta,\gamma)\in\mathcal A^3,
$$

define

$$
\boxed{
G_Q(\alpha,\beta,\gamma)
=
\sum_{\beta'\ne\beta}
\Pi_{\beta,\gamma}(\beta')
\left[
 s^{\rho(\alpha,\beta,\gamma;\beta')}
 \frac{q_{\alpha\beta'}q_{\beta'\gamma}}
 {q_{\alpha\beta}q_{\beta\gamma}}
 -1
\right].
}
\tag{7.1}
$$

For a fixed interior word, the tilted generator of `C_Q` is exactly the sum of these local terms:

$$
\boxed{
\frac{\mathscr L_sC_Q}{C_Q}
=
\sum_i
G_Q(\sigma_{i-1},\sigma_i,\sigma_{i+1}),
}
\tag{7.2}
$$

apart from the finite boundary/height terms. Thus all simultaneous inactive, exposed, child-alive and reinfected phases are now accounted for transition by transition.

Two load-bearing examples are worth recording.

### 7.1 Same-orientation disagreement bulk

For

$$
(\alpha,\beta,\gamma)=(01,01,01),
$$

one obtains

$$
\boxed{
\begin{aligned}
G_Q(01,01,01)
={}&(1-a)
\left[
 s\frac{q_{01,00}q_{00,01}}{q_{01,01}^2}-1
\right]\\
&+a
\left[
 \frac{q_{01,10}q_{10,01}}{q_{01,01}^2}-1
\right].
\end{aligned}
}
\tag{7.3}
$$

The first ratio is exactly the cluster-splitting/restart transition that invalidates the old product. A valid phase weight must therefore put nontrivial credit on the child-alive phase `q_{01,01}` and, in general, on the susceptible phase `q_{01,00}`.

Under the old assignment

$$
q_{00,01}=e_0,
\qquad
q_{\alpha\beta}=1
\quad\text{for every other phase appearing in (7.3)},
$$

and (7.3) reduces to

$$
G_Q(01,01,01)=(1-a)(s e_0-1)>0.
\tag{7.4}
$$

This is a positive self-loop in the finite phase graph.

### 7.2 Opposite-orientation disagreement bulk

For

$$
(\alpha,\beta,\gamma)=(01,10,01),
$$

the middle disagreement coalesces to common one at rate `b`, to common zero at rate `1-c`, and otherwise remains off-diagonal. Hence

$$
\boxed{
\begin{aligned}
G_Q(01,10,01)
={}&b
\left[
 s\frac{q_{01,11}q_{11,01}}
 {q_{01,10}q_{10,01}}-1
\right]\\
&+(1-c)
\left[
 s\frac{q_{01,00}q_{00,01}}
 {q_{01,10}q_{10,01}}-1
\right].
\end{aligned}
}
\tag{7.5}
$$

Thus same- and opposite-orientation child-alive phases cannot be collapsed without checking both constraints.

## 8. Finite no-positive-cycle reduction

The global bulk question associated with (7.1) is finite.

Construct the directed de Bruijn graph `G_phase` whose vertices are the `16` ordered pairs

$$
(\alpha,\beta)\in\mathcal A^2,
$$

and whose `64` directed edges are

$$
(\alpha,\beta)\longrightarrow(\beta,\gamma),
$$

one for each triple `(alpha,beta,gamma)`. Give that edge weight

$$
G_Q(\alpha,\beta,\gamma).
$$

Define its maximal cycle mean

$$
\boxed{
\kappa_s(Q)
=
\max_{\text{directed cycles }C}
\frac1{|C|}\sum_{e\in C}G_Q(e).
}
\tag{8.1}
$$

### Proposition 8.1 (finite phase criterion)

For a nearest-neighbour product corrector `C_Q`, the following are equivalent.

1. Every spatial cycle has nonpositive total bulk drift:
   $$
   \kappa_s(Q)\le0.
   $$
2. There exists a finite potential
   $$
   \psi:\mathcal A^2\to\mathbb R
   $$
   such that for every triple
   $$
   \boxed{
   G_Q(\alpha,\beta,\gamma)
   \le
   \psi(\alpha,\beta)-\psi(\beta,\gamma).
   }
   \tag{8.2}
   $$
3. For every finite stack word, the sum of all **interior** tilted phase drifts is bounded by a constant depending only on the two end phases, not on the height `H`.

#### Proof

`(2) => (3)` follows by summing (8.2): the right side telescopes.

`(3) => (1)` follows by repeating any directed spatial cycle arbitrarily many times. A positive cycle mean would produce positive drift linear in the number of repetitions.

`(1) => (2)` is the standard finite difference-constraints lemma: on a finite directed graph, absence of a positive cycle is equivalent to the existence of a potential satisfying (8.2). One may take `psi` to be the maximal path weight to a fixed root after reversing signs. `square`

This proposition is the rigorous replacement for the undefined product statement in Assignment 003. It reduces the all-height **bulk phase bookkeeping** to finitely many variables and finitely many inequalities.

The remaining boundary conditions are also finite:

- rightmost coalescence changes the height factor `lambda^H` and the terminal edge phase;
- a new trail insertion adds one unresolved level and one edge phase;
- a completely removed suffix is trimmed from the word.

If some `Q,psi,lambda,s` satisfy (8.2) together with those finite boundary inequalities with strict net gain, then the desired global Foster lift follows by the tilted-generator supermartingale argument. Conversely, if `kappa_s(Q)>0`, no fixed boundary height gain can compensate at arbitrary `H`.

I have **not** proved that a suitable `Q` exists throughout the residual chamber. That finite feasibility problem is materially stronger than the scalar same-parent pgf and is the exact global-corrector blocker left by this assignment.

## 9. Consequences for the current block programme

### 9.1 What is now definitely false

The following implication from Assignment 003 cannot be used:

> same-parent pgf `M(s)` + scalar height factor `phi(lambda)`
> automatically gives a product Foster corrector over all unresolved levels.

Equation (4.5) is an explicit counterexample.

Therefore Student F should **not** treat `(FL)` from Assignment 003 as proved.

### 9.2 What remains usable

The following inputs remain intact:

- the Professor-verified same-parent geometric tail and pgf;
- the exact one-exposure `J_i` resolvent and compensator;
- the principal stack-height clearing minorant;
- the mass/disagreement identity
  $$
  g\,\mu(h_{p_*}(\eta_y)f)
  =(Br-c)\bar\mu(f)
  +Br(1-r)(\mu^1-\mu^0)(f);
  $$
- the near-East `16/21` scalar calculation, only as a scalar stress diagnostic;
- F's theorem `cZ>1` showing the crude raw-supnorm criterion is empty on the residual chamber.

### 9.3 Exact stronger state required

A viable local global lift must keep at least the edge phase

$$
(\sigma_{i-1},\sigma_i)\in\mathcal A^2,
$$

or an equivalent state distinguishing:

1. exposed common spin zero/one;
2. child-alive same/opposite disagreement orientation;
3. susceptible diagonal zero/one after parent coalescence;
4. reinfection into a new parent episode.

The 16-state edge description is Markovian and has no hidden parent-history bookkeeping. The finite criterion (8.2) is the concrete next object to solve or refute.

It is plausible that an even richer matrix-product/nonlocal corrector is needed if the 16-state scalar edge product has a positive cycle for every `Q`. I do not claim either outcome here.

## 10. Interface with the centered trail

This report does not alter the global centered-trail target

$$
J_{x,r}
=B g^{n-1}
\int
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
$$

In particular:

- `cZ>1` says raw scalar absolute values cannot prove its decay;
- `16/21<1` says only that the separately bundled same-parent/height scalars are compatible near East;
- (4.5) shows those scalars do not define a valid global restart norm;
- the bounded signed mass/disagreement kernel remains conditional on an actual global Foster lift.

Only after a valid phase corrector and bounded signed kernel are both established can one infer `J_{x,r}->0`; the full trail factorization and no-exit term would still need their closing audit.

## Handoff

`product corrector fails at: the reachable same-orientation stack sigma_i=(0,1) for 0<=i<H. For every s>1, finite lambda>1 and exposed-only factor e_0>=1 with all nonexposed phases assigned weight 1, the exact tilted drift is (1-a)(s-1)+(H-2)(1-a)(s e_0-1)+omega(lambda^{-1}-1), hence is positive for all sufficiently large H. With the Assignment-003 near-East choices it tends to (H-2)/7, so the checked 16/21 scalar factor is not a global Foster theorem. The minimum stronger Markov state is the 16 edge phases (sigma_{i-1},sigma_i) in {00,11,01,10}^2; for a nearest-neighbour product corrector the all-height bulk problem is exactly the finite no-positive-cycle condition kappa_s(Q)<=0 on the associated 16-vertex/64-edge de Bruijn graph, plus finite boundary height/insertion inequalities. Existence of such a Q throughout the residual chamber remains unresolved.`
