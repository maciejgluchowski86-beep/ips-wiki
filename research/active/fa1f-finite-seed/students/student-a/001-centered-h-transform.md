# Student A 001: centered FA-1f transform

## Verdict

Proof-spine edge E1 is correct. The displayed generator is a genuine Markov generator on finite nonempty subsets of `Z`, the generator identity with the centered kernel holds exactly, the finite-set process is nonexplosive from every finite initial set, and the generator duality extends to the infinite-volume semigroups. There is no missing integrability hypothesis. For the one-vacancy physical initial condition, the Professor's specialization to a one-site occupation probability of the transformed process is also exact.

The more important qualification is structural. On a finite cycle, the duality kernel is invertible and conjugates the transpose FA-1f generator to the transformed generator. Thus E1 is, algebraically, an exact similarity transform rather than a reduction of state-space complexity. The transformed process has useful positive structure -- Bernoulli(`q`) reversibility and a close Dirichlet-form comparison with BABP -- but it is neither attractive nor additive, and its front identities are exactly the same as the corresponding FA-1f vacancy-front identities. I do not yet see an E2 mechanism that is genuinely easier than the original finite-seed problem.

There is also an exact overlap with the *local algebra* of the closed Bernoulli-quench sibling route. The same parameter

$$
a=-\frac{p}{q}
$$

appears, the same two-neighbour factorization gives `(p+qa)^2=0`, and the simultaneous two-neighbour term contains the same maximal two-sibling event with absolute size `q^2|a|^2=p^2`. The active finite-seed programme is nevertheless not itself a retry of the closed route: after E1, the one-vacancy observable becomes a bounded one-site occupation event, not a generation-by-generation signed sibling majorant. Any future attempt to extract a contraction by taking absolute values of the two refreshed sibling weights would, however, reproduce the closed route and should be stopped.

## 1. Exact generator duality

Write

$$
\chi_A^*(\eta)=\prod_{j\in A}(\eta(j)-p),
\qquad
H(A,\eta)=q^{-|A|}\chi_A^*(\eta),
\qquad p=1-q.
$$

For hard one-dimensional FA-1f,

$$
L f(\eta)
=
\sum_i \bigl(1-\eta(i-1)\eta(i+1)\bigr)
\bigl(E_{i,p}f(\eta)-f(\eta)\bigr).
$$

If `i notin A`, the Bernoulli refresh at `i` leaves `chi_A^*` unchanged. If `i in A`, it kills the centered factor. Hence

$$
L\chi_A^*(\eta)
=
\sum_{i\in A}
\bigl(\eta(i-1)\eta(i+1)-1\bigr)\chi_A^*(\eta).
\tag{1}
$$

For a finite nonempty set `A`, let a source `i in A` ring at rate one and replace the membership indicators of `i-1,i+1` by independent Bernoulli(`q`) variables, retaining `i`. Its generator is

$$
\mathcal Gg(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq N(i)}q^{|R|}p^{2-|R|}
 g\bigl((A\setminus N(i))\cup R\bigr)-g(A)
\right],
\qquad N(i)=\{i-1,i+1\}.
\tag{2}
$$

Fix `i in A`. Independence of the two refreshed neighbour indicators gives

$$
\begin{aligned}
&\sum_{R\subseteq N(i)}q^{|R|}p^{2-|R|}
H\bigl((A\setminus N(i))\cup R,\eta\bigr)\\
&\qquad=
q^{-|A\setminus N(i)|}\chi_{A\setminus N(i)}^*(\eta)
\prod_{j\in N(i)}
\left(p+q\frac{\eta(j)-p}{q}\right)\\
&\qquad=
q^{-|A\setminus N(i)|}\chi_{A\setminus N(i)}^*(\eta)
\eta(i-1)\eta(i+1).
\end{aligned}
\tag{3}
$$

If `j in A cap N(i)`, then

$$
\eta(j)(\eta(j)-p)=q\eta(j).
$$

Consequently the last expression in (3) equals

$$
q^{-|A|}\eta(i-1)\eta(i+1)\chi_A^*(\eta).
$$

Subtracting `H(A,eta)` and summing over sources gives

$$
\mathcal G_AH(A,\eta)
=
q^{-|A|}L\chi_A^*(\eta)
=
L_\eta H(A,\eta).
\tag{4}
$$

Thus the formal generator identity is exact, including when one or both neighbours of a source already belong to `A`.

## 2. Nonexplosion and exponential moments

The only issue hidden by (4) is that the first variable lives on a countable state space and `H` is not uniformly bounded in `A` when `q<1/2`.

Let

$$
\ell(A)=\min A,
\qquad
r(A)=\max A,
\qquad
D(A)=r(A)-\ell(A).
$$

An outward extension of the current hull can occur only when a current endpoint rings. At all times there are at most two endpoint sources. Let `M_t` count rings of current endpoint sources, counting a singleton source once. Its predictable intensity is at most two, so it is stochastically dominated by a Poisson random variable `N_t` of mean `2t`. One endpoint ring can increase the span by at most two -- the factor two is only needed for a singleton which can create both neighbours at once. Therefore, pathwise under the natural graphical construction,

$$
D(\mathcal A_t)
\leq D(A)+2M_t,
\qquad
|\mathcal A_t|
\leq D(A)+2M_t+1.
\tag{5}
$$

In particular the process cannot explode from a finite initial set. More quantitatively, for every `theta>0`,

$$
\mathbf E_A e^{\theta|\mathcal A_t|}
\leq
\exp\left(
\theta(D(A)+1)+2t(e^{2\theta}-1)
\right).
\tag{6}
$$

Put

$$
c_q=\max\left\{1,\frac{p}{q}\right\}.
$$

Since `eta(j)-p` is either `q` or `-p`, we have

$$
|H(B,\eta)|\leq c_q^{|B|}.
\tag{7}
$$

Equations (6)-(7) give all exponential integrability needed below, including for `q<1/2`.

## 3. Infinite-volume semigroup duality

A finite-volume argument makes the interface precise. Let `C_m` be a cycle of odd length tending to infinity, identify a central interval with the corresponding sites of `Z`, and use the cyclic versions `L^{(m)}` and `G^{(m)}`. For every sufficiently large `m`, the same local calculation as (4) gives the finite matrix identity

$$
G^{(m)}H^{(m)}=H^{(m)}(L^{(m)})^{\mathsf T}.
\tag{8}
$$

Exponentiating the finite matrices yields

$$
P_t^{(m)}H(A,\cdot)(\eta^{(m)})
=
\mathbf E_A^{(m)}H(\mathcal A_t^{(m)},\eta^{(m)}),
\tag{9}
$$

where `eta^(m)` agrees with the chosen infinite configuration on the growing central interval.

It remains to pass to `Z`. For the physical process, a discrepancy at the cyclic seam can affect the local observable `H(A,.)` by time `t` only if there is a chronological nearest-neighbour dependency path from the seam to `A`. If the graph distance is `d_m`, a standard graphical expansion bounds this probability by a constant depending on `A` times

$$
\sum_{k\geq d_m}\frac{(2t)^k}{k!},
\tag{10}
$$

which tends to zero as `m` tends to infinity.

For the transformed process, couple the cycle and line with the same source clocks and refresh coins until the line hull reaches the seam. To reach graph distance `d_m` from its initial hull requires at least `d_m` outward endpoint extensions, hence at least `d_m` endpoint rings. Thus the disagreement probability is bounded by a Poisson(`2t`) tail. The integrands are uniformly integrable despite (7): on the line, (5) gives

$$
|H(\mathcal A_t,\eta)|
\leq c_q^{D(A)+1+2M_t},
$$

and the Poisson variable dominating `M_t` has exponential moments of every order. On the cycle, the crude bound `|H| <= c_q^{|C_m|}` multiplied by the factorial Poisson tail for reaching the seam still tends to zero. Hence both sides of (9) converge to their infinite-volume counterparts.

Therefore, for every finite `A`, every `eta in {0,1}^Z`, and every `t>=0`,

$$
P_t H(A,\cdot)(\eta)
=
\mathbf E_A H(\mathcal A_t,\eta).
\tag{11}
$$

Equivalently,

$$
P_t\chi_A^*(\eta)
=
q^{|A|}\mathbf E_A
\left[q^{-|\mathcal A_t|}\chi_{\mathcal A_t}^*(\eta)\right].
\tag{12}
$$

Thus E1 has no missing nonexplosion or integrability assumption for finite initial `A`.

## 4. Single-vacancy specialization

Let `eta^0(0)=0` and `eta^0(x)=1` for `x != 0`. For every finite nonempty `B`,

$$
H(B,\eta^0)
=
\begin{cases}
1,&0\notin B,\\
-p/q,&0\in B,
\end{cases}
=
1-q^{-1}\mathbf 1_{\{0\in B\}}.
\tag{13}
$$

Substituting (13) into (12) gives exactly

$$
P_t\chi_A^*(\eta^0)
=
q^{|A|}
\left(1-q^{-1}\mathbf P_A(0\in\mathcal A_t)\right).
\tag{14}
$$

Consequently the centered-monomial target is exactly equivalent to

$$
\mathbf P_A(0\in\mathcal A_t)\longrightarrow q
$$

for every finite nonempty initial `A`.

## 5. Vacancy-set form of the duality kernel

Let `B(eta)={x:eta(x)=0}` be the physical vacancy set and put

$$
a=-\frac{p}{q}.
$$

At a site not in `B(eta)`, the normalized centered factor is one; at a vacancy it is `a`. Hence

$$
H(A,\eta)=a^{|A\cap B(\eta)|}.
\tag{15}
$$

This is a product/intersection duality kernel of Lloyd--Sudbury type. It is also exactly the parameter appearing in the standard BABP self-duality: with `lambda=q/p`, the BABP kernel in Martinelli--Shapira--Toninelli Section 5 is `(-1/lambda)^{|A cap B|}=(-p/q)^{|A cap B|}`. Equality of the kernel does **not** mean equality of the two Markov processes; the transformed FA process below differs from BABP by a simultaneous-neighbour term.

At `q=1/2`, (15) becomes the ordinary parity kernel `(-1)^{|A cap B|}`.

## 6. Exact small-configuration transitions

All rates below are continuous-time rates obtained from a rate-one source ring followed by the two independent Bernoulli(`q`) neighbour refreshes. Outcomes equal to the starting state are listed as self outcomes where useful but do not appear as off-diagonal generator rates.

### 6.1 One isolated source

From `A={0}`, a ring at zero gives

| result | probability |
|---|---:|
| `{0}` | `p^2` |
| `{-1,0}` | `pq` |
| `{0,1}` | `pq` |
| `{-1,0,1}` | `q^2` |

Thus the three off-diagonal rates are `pq,pq,q^2`.

### 6.2 Two adjacent sources

From `A={0,1}`, source zero gives

| result | probability |
|---|---:|
| `{0}` | `p^2` |
| `{-1,0}` | `pq` |
| `{0,1}` | `pq` |
| `{-1,0,1}` | `q^2` |

and source one gives

| result | probability |
|---|---:|
| `{1}` | `p^2` |
| `{1,2}` | `pq` |
| `{0,1}` | `pq` |
| `{0,1,2}` | `q^2` |

Thus a source can delete its active neighbour. This is already enough to rule out attractiveness.

### 6.3 Two sources at distance two

From `A={0,2}`, source zero gives

| result | probability |
|---|---:|
| `{0,2}` | `p^2` |
| `{-1,0,2}` | `pq` |
| `{0,1,2}` | `pq` |
| `{-1,0,1,2}` | `q^2` |

and source two gives the reflected outcomes. In particular

$$
\{0,2\}\longrightarrow\{0,1,2\}
$$

has total rate `2pq` because either source may create the middle site.

### 6.4 A finite contiguous interval

Let `A=[a,b] cap Z` with at least three sites. If `a<i<b`, both neighbours of `i` are active before its ring. The four outcomes at source `i` are

$$
\begin{array}{c|c}
\text{result}&\text{probability}\\ \hline
A&q^2\\
A\setminus\{i+1\}&pq\\
A\setminus\{i-1\}&pq\\
A\setminus\{i-1,i+1\}&p^2.
\end{array}
\tag{16}
$$

At the left endpoint `a`, the inside neighbour `a+1` and outside neighbour `a-1` are both refreshed:

$$
\begin{array}{c|c}
\text{result}&\text{probability}\\ \hline
A\setminus\{a+1\}&p^2\\
(A\setminus\{a+1\})\cup\{a-1\}&pq\\
A&pq\\
A\cup\{a-1\}&q^2.
\end{array}
\tag{17}
$$

The right endpoint is symmetric. In particular, intervals are not an invariant class: an interior source can create holes, and an endpoint can expand outward while deleting the adjacent inside site.

## 7. Geometry: cardinality, pairs, and fronts

Let

$$
N(A)=|A|,
\qquad
J(A)=\sum_x\mathbf 1_{\{x,x+1\subseteq A\}},
$$

and also

$$
J_2(A)=\sum_x\mathbf 1_{\{x,x+2\subseteq A\}},
\qquad
T(A)=\sum_x\mathbf 1_{\{x,x+1,x+2\subseteq A\}}.
$$

At a ring of source `i`, the two neighbours have expected post-ring occupancy `2q`, while their pre-ring contribution is `1_A(i-1)+1_A(i+1)`. Therefore

$$
\mathcal GN(A)=2qN(A)-2J(A).
\tag{18}
$$

Thus particle number has positive drift for a sparse set but can have strongly negative drift in a dense interval. For an interval of length `n>=2`,

$$
\mathcal GN=2qn-2(n-1)=2(1-pn).
\tag{19}
$$

For the adjacent-pair count, only the four edges incident to the refreshed neighbours of a source can change. Summing their conditional expected increments gives

$$
\mathcal GJ(A)
=
2qN(A)+2qJ_2(A)-2J(A)-2T(A).
\tag{20}
$$

The hierarchy therefore does not close even at the first pair observable.

For a nonempty finite set, define left and right fronts `ell(A)=min A`, `r(A)=max A`. A direct endpoint calculation gives

$$
\mathcal G\ell(A)
=-q+p\mathbf 1_{\{\ell(A)+1\in A\}},
\tag{21}
$$

$$
\mathcal Gr(A)
=q-p\mathbf 1_{\{r(A)-1\in A\}},
\tag{22}
$$

and hence

$$
\mathcal G(r-\ell)(A)
=
2q-p\left(
\mathbf 1_{\{\ell(A)+1\in A\}}
+
\mathbf 1_{\{r(A)-1\in A\}}
\right).
\tag{23}
$$

These are exactly the corresponding generator identities for the vacancy fronts of the original hard FA-1f process: an outside neighbour of the rightmost vacancy becomes vacant at rate `q`, while the rightmost vacancy can heal at rate `p` exactly when its inside neighbour is vacant. Thus the most obvious front observable is not simplified by E1.

For a single coordinate `X_x(A)=1_{\{x\in A\}}`, the simultaneous-neighbour term below disappears and

$$
\mathcal GX_x
=(q-X_x)(X_{x-1}+X_{x+1}).
\tag{24}
$$

This is the same one-site generator identity as BABP. It is not closed at the level of expectations because the right-hand side contains adjacent correlations.

## 8. Bernoulli product measure is reversible

Let `nu_q` be Bernoulli(`q`) product measure on `{0,1}^Z`, now for transformed-set occupancy variables. Write `E_x` for conditional expectation / Bernoulli(`q`) heat-bath resampling at coordinate `x`, and `X_i` for multiplication by the source indicator. On local functions,

$$
\mathcal G
=
\sum_i X_i\bigl(E_{i-1}E_{i+1}-I\bigr).
\tag{25}
$$

The sum is finite on every local function. Under `nu_q`, each `E_x` is an orthogonal projection on `L^2(nu_q)`. The projections `E_{i-1},E_{i+1}` commute, and their product commutes with `X_i` because the source coordinate is distinct from both refreshed coordinates. Hence every summand in (25) is self-adjoint. It also annihilates constants. Therefore

$$
\nu_q(f\mathcal Gg)=\nu_q(g\mathcal Gf),
\qquad
\nu_q(\mathcal Gf)=0
\tag{26}
$$

for local `f,g`. Thus `nu_q` is reversible and invariant for the infinite-volume transformed process.

On a finite cycle, the empty set is an absorbing communicating class and the nonempty sector is closed. Since finite-volume Bernoulli(`q`) product measure is reversible, its conditioning on the nonempty sector is reversible there as well.

## 9. The transformed process is not attractive or additive

### 9.1 Not attractive

Take `A={0}` and `B={0,1}`, so `A subset B`, and the increasing function

$$
f(C)=\mathbf 1_{\{0\in C\}}.
$$

We have `f(A)=f(B)=1`. From `A`, source zero is retained at every ring, so

$$
\mathcal Gf(A)=0.
$$

From `B`, source one refreshes site zero and deletes it with probability `p`, while source zero cannot delete itself. Therefore

$$
\mathcal Gf(B)=-p.
$$

If the semigroup were attractive, `P_tf(A)<=P_tf(B)` for all `t>=0`; equality at `t=0` would force `Gf(A)<=Gf(B)`, i.e. `0<=-p`, impossible. Hence the transformed process is not attractive for any `q in (0,1)`.

### 9.2 Not additive

Use the standard random-map meaning of additivity: every elementary map must preserve unions. The transformed chain has the transition

$$
\{0,1\}\longrightarrow\{1\}
$$

at rate `p^2>0`. Any additive map `Phi` producing this transition would satisfy

$$
\Phi(\{0\})\cup\Phi(\{1\})
=
\Phi(\{0,1\})
=
\{1\}.
$$

Thus `0 notin Phi({0})`. But the actual transformed process started from the singleton `{0}` has zero rate for every transition that removes zero: a source is always retained. A nonnegative-rate decomposition into additive maps therefore cannot contain such a `Phi`. This contradicts the positive pair-to-singleton rate, so the process is not additive.

The failure is already visible in the natural refresh map. If `Phi_{i,R}` acts only when `i` is active, then with `i=1`, `R=emptyset`, `A={0}` and `B={1}`,

$$
\Phi_{1,\varnothing}(A\cup B)=\{1\}
\neq
\{0,1\}
=
\Phi_{1,\varnothing}(A)\cup\Phi_{1,\varnothing}(B).
$$

## 10. Cancellative only at the symmetric point

In the standard random-map sense, a cancellative system is generated by maps linear under symmetric difference, equivalently linear over `F_2` in occupancy variables.

At `q=p=1/2`, the process is cancellative. A fair refresh of a neighbour `j` of an active source `i` can be implemented by an independent fair bit `B` and

$$
X_j' = X_j\oplus(BX_i).
\tag{27}
$$

If the source is inactive nothing changes; if it is active, the target is toggled with probability one half and is therefore a fresh fair bit. Applying independent bits to `i-1` and `i+1` gives exactly one source ring of the transformed process, and for fixed bits the map (27) is `F_2`-linear. At this point the duality kernel (15) is the parity kernel.

For `q\neq1/2`, a cancellative random-map representation is impossible. One can see this without relying on the natural maps. Any positive-rate linear map must send a singleton only to states which have positive transition rate from that singleton (or leave it fixed), because map rates are nonnegative.

For `q<1/2`, the transition

$$
\{0,1\}\to\{0\}
$$

has rate `p^2`. If a linear map `Phi` produces it, then

$$
\Phi(\{0\})\triangle\Phi(\{1\})=\{0\}.
$$

Given the allowed singleton transition supports, the only possibility is

$$
\Phi(\{0\})=\{0,1\},
\qquad
\Phi(\{1\})=\{1\}.
$$

Hence the total rate of maps producing the pair transition is at most the singleton rate `\{0\}->\{0,1\}`, which is `pq`. But `p^2>pq` when `p>q`, contradiction.

For `q>1/2`, use instead

$$
\{0,1\}\to\{-1,0,1\},
$$

whose rate is `q^2`. The only compatible singleton images are

$$
\Phi(\{0\})=\{-1,0\},
\qquad
\Phi(\{1\})=\{1\},
$$

so its total rate is at most the singleton rate `\{0\}->\{-1,0\}=pq`. Since `q^2>pq` when `q>p`, this is again impossible.

Thus the process is cancellative exactly at `q=1/2`, among `q in (0,1)`.

## 11. Exact decomposition around BABP

Let

$$
\Delta_x=E_x-I.
$$

Since the two heat-bath projections commute,

$$
E_{i-1}E_{i+1}-I
=
\Delta_{i-1}+\Delta_{i+1}+\Delta_{i-1}\Delta_{i+1}.
$$

Therefore

$$
\mathcal G
=
\mathcal G_{\mathrm{BABP}}+\mathcal S,
\tag{28}
$$

where

$$
\mathcal G_{\mathrm{BABP}}
=
\sum_i X_i(\Delta_{i-1}+\Delta_{i+1})
=
\sum_x (X_{x-1}+X_{x+1})\Delta_x
\tag{29}
$$

is exactly the BABP generator in vacancy/particle variables with Bernoulli(`q`) refresh, and

$$
\mathcal S
=
\sum_i X_i\Delta_{i-1}\Delta_{i+1}
\tag{30}
$$

is the genuinely simultaneous two-neighbour cross term. The cross term is not itself a Markov generator. It vanishes on every one-coordinate observable, explaining (24), but not on pair observables.

There is a useful quadratic-form comparison. Under `nu_q`, set `P=E_{i-1}`, `Q=E_{i+1}`. These are commuting orthogonal projections. On each joint eigenspace,

$$
\frac12\bigl[(I-P)+(I-Q)\bigr]
\leq I-PQ
\leq (I-P)+(I-Q).
$$

Multiplication by `X_i` commutes with both projections. Summing gives, for local `f`,

$$
\frac12\mathcal D_{\mathrm{BABP}}(f)
\leq
\mathcal D_{\mathcal G}(f)
\leq
\mathcal D_{\mathrm{BABP}}(f).
\tag{31}
$$

So the transformed process and BABP have comparable equilibrium Dirichlet forms. This is genuine structure, but it does not solve E2: Martinelli--Shapira--Toninelli explicitly note that finite-seed BABP convergence is known only in a restricted parameter range (historically `lambda>1/3`, improved to `lambda>0.0347`), while their all-parameter result concerns other aspects such as growth and Bernoulli initial laws. Thus reducing E2 to generic BABP finite-seed theory would merely replace one open difficulty by another.

## 12. Finite-volume similarity: E1 is exactly a coordinate transform

This is the strongest obstruction-level probe of whether E1 is a genuine simplification.

On a finite cycle `V`, index the physical configurations by their vacancy sets `B subseteq V`. By (15), the duality matrix is

$$
\mathbf H(A,B)=a^{|A\cap B|},
\qquad a=-p/q.
\tag{32}
$$

It is a tensor product over sites of the two-by-two matrix

$$
K=
\begin{pmatrix}
1&1\\
1&a
\end{pmatrix}.
$$

Since

$$
\det K=a-1=-\frac1q\neq0,
$$

`H` is invertible. The finite generator identity (8) is therefore equivalent to

$$
G^{(V)}
=
\mathbf H (L^{(V)})^{\mathsf T}\mathbf H^{-1}.
\tag{33}
$$

Thus the transformed process is exactly similar to finite-volume FA-1f. In particular the two finite generators have the same spectrum, including the same nonzero eigenvalues with multiplicity. E1 turns the centered coefficient dynamics into a positive Markov process, but it does not remove the finite-volume spectral obstruction by itself.

Together with the exact front identities (21)-(23), non-attractiveness, and non-additivity, this is substantial evidence that E1 is currently a **positive reformulation**, not yet a theorem-level reduction in difficulty. Its possible value must come from some probabilistic structure of `G` that is unavailable or opaque in the original coordinates, not from a generic spectral, front, or monotone-coupling improvement.

## 13. Exact overlap with the closed sibling algebra

The old closed Bernoulli-quench screen used the normalized centered vacancy factor

$$
a=1-\frac1q=-\frac{p}{q}.
\tag{34}
$$

For two Bernoulli(`q`) sibling coins, its complete one-ring signed average was

$$
(p+qa)^2=0,
\tag{35}
$$

while the obstruction-selected event in which both siblings are born had absolute weight

$$
q^2|a|^2=p^2,
\tag{36}
$$

which tends to one as `q` tends to zero. The later multigeneration calculation then restored the critical scaling and closed that route.

Equations (34)-(36) are **literally the local algebra of E1**. In (15), each dual/physical intersection contributes the same `a=-p/q`. At one transformed source ring, the two neighbours are independent Bernoulli(`q`) refreshes; applying the kernel to the two refreshed coordinates produces exactly the factors `p+qa`. The simultaneous cross term `S` in (30) is the operator-level location of the two-sibling coupling. The event that both refreshed neighbours are present has probability `q^2`; evaluating two corresponding vacancy intersections produces magnitude `|a|^2`, giving exactly (36).

Therefore the new programme must not claim a fresh contraction from grouping these two refreshed neighbours before absolute values. Any pathwise or generation-by-generation argument whose gain is precisely (35) and which then majorizes descendant weights by absolute value has returned to the closed sibling mechanism.

What is different is the finite-seed observable after the transform. For the physical one-vacancy initial state, the whole product kernel collapses by (13) to

$$
1-q^{-1}\mathbf 1_{\{0\in\mathcal A_t\}},
$$

so the theorem asks for the *positive* one-site density limit of `A_t`, not for absolute integrability or contraction of products of `a` over sibling generations. E1 itself therefore does not reopen the closed route. It identifies exactly where a forbidden future subroute would begin.

## 14. Prior-work check

I searched the current literature under FA-1f duality, quasi-duality, branching/coalescing, neighbour refresh, and related terminology.

1. **Martinelli--Shapira--Toninelli (2025), Sections 5-6.** Their BABP self-duality uses the same intersection kernel parameter `-p/q`, as noted above. Section 6 treats FA-1f from finitely many infections and proves linear-order growth of the infection hull/span for every `q`, but does not state the local convergence theorem. I did not find the exact source-centred simultaneous two-neighbour-refresh process (2) stated there.

2. **Sudbury--Lloyd / Swart duality literature.** Product kernels of the form `a^{|A cap B|}` are classical in the Lloyd--Sudbury algebraic duality framework, including branching/coalescing/annihilating relatives of the contact process. Thus the form (15) is not a new style of duality kernel.

3. **Jack--Mayer--Sollich (J. Stat. Mech. 2006, P03006; arXiv:cond-mat/0601529).** They give an exact mapping of the FA model to reaction-diffusion systems and analyze the resulting symmetries. This makes it especially unsafe to claim novelty merely from the existence of an invertible product similarity transform such as (33). I did not identify their mapped process with the exact Markov generator (2) from the sources checked.

4. **Hartarsky--Martinelli--Toninelli, CBSEP (Ann. Appl. Probab. 2022; arXiv:2006.01426).** CBSEP is a reversible coalescing/branching exclusion process used to recover and sharpen finite-volume FA-1f mixing estimates. It is not the same process as (2): its elementary mechanism and, importantly, its attractive structure differ. It should not be conflated with the present transformed process.

The safe literature conclusion is therefore: the *duality technology and product kernel are classical*, and FA has prior exact similarity mappings; I did not locate the exact generator (2) in the specific sources checked. Novelty of (2) should not be asserted without a dedicated literature audit, and novelty is not needed for the present programme.

## 15. What E1 does and does not buy for E2

E1 buys an exact positive representation of the target:

$$
P_t\chi_A^*(\eta^0)
\longleftrightarrow
\mathbf P_A(0\in\mathcal A_t)-q.
$$

It also gives a reversible product equilibrium, the exact BABP decomposition (28), the form comparison (31), and a finite-particle graphical process that may admit probabilistic arguments not visible in the original spin coordinates.

But the first obstruction-level probes are negative:

- finite-volume `G` is exactly similar to finite-volume FA-1f;
- the transformed process is not attractive;
- it is not additive;
- except at `q=1/2`, it is not cancellative;
- its front drift identities are exactly the same as the original FA vacancy-front identities;
- the one-site equation agrees with BABP but does not close because pair correlations enter;
- the genuinely new local ingredient relative to BABP is precisely the simultaneous sibling term, which is also where the old closed cancellation algebra reappears.

My present assessment is therefore that E1 is **mathematically correct and worth retaining, but not yet a real reduction of E2**. The next useful E2 step must exploit a structure stronger than the facts above. A proposal based only on front motion, finite-volume spectra/Dirichlet forms, or the local sibling cancellation does not yet cross that threshold.

A plausible sharply testable next question, if the Professor wishes to keep E1 active, is whether the positive process admits a finite-window equilibration/coupling statement behind its expanding hull that uses the simultaneous refresh in a genuinely probabilistic way. Such a statement would have to add something beyond the existing finite-volume FA mixing problem; otherwise (33) shows that the transform has only renamed the difficulty.

## Sources checked

- Canonical project paper, `paper/`, especially Theorem B, the FA-1f application, and the discussion of finite facilitating seeds.
- Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025), especially Conjecture 1 and Sections 5-6.
- Ivailo Hartarsky, Fabio Martinelli, Cristina Toninelli, *Coalescing and branching simple symmetric exclusion process*, Ann. Appl. Probab. 32 (2022), 2841-2859; arXiv:2006.01426.
- Robert L. Jack, Peter Mayer, Peter Sollich, *Mappings between reaction-diffusion and kinetically constrained systems: A+A <-> A and the Fredrickson-Andersen model have upper critical dimension d_c=2*, J. Stat. Mech. (2006) P03006; arXiv:cond-mat/0601529.
- Jan M. Swart, *Duals and thinnings of some relatives of the contact process*, Prague Stochastics 2006; arXiv:math/0604335, for the Lloyd--Sudbury duality context.
- Repository history: commit `c095b0f04c7dbae0d715d4a9a401d7de9b663a0e` for the old two-sibling Gate-6 calculation and commit `37dad4042dcf9377fd8a58fd0731c387ce9a5a2c` for closure of that screen.

## Handoff to the Professor

The decisive file is this note:

`research/active/fa1f-finite-seed/students/student-a/001-centered-h-transform.md`.

Two proof-spine changes are justified.

1. **E1 is correct**: the exact positive finite-set dual and the single-vacancy specialization hold in infinite volume for every finite initial dual set, with nonexplosion and the semigroup passage supplied above. The Professor may move E1 from `claimed` to the appropriate post-student status, subject to whatever independent audit it wants for a central reduction.

2. **E2 should record that E1 is not yet a simplification**: on finite volumes it is an invertible similarity transform of FA-1f, and the simplest probabilistic handles (fronts, attractiveness/additivity, generic BABP comparison) do not solve the finite-seed problem. The old sibling algebra reappears exactly in the simultaneous two-neighbour term, so any future absolute-weight sibling-contraction argument is the already closed route. Continuing with E1 requires a genuinely new positive-process mechanism for local equilibration.