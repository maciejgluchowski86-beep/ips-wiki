# Professor initial reduction: centered FA-1f dual via an `h`-transform

Status: **claimed calculation, not yet independently checked**.

Purpose: this note records the exact calculation behind proof-spine edge E1 so it can be audited rather than reconstructed from conversation.

## Setup

Work with one-dimensional hard FA-1f. State `0` is vacant/facilitating and state `1` is occupied/calm. Let vacancy density be `q in (0,1)` and `p=1-q`. The equilibrium product law is `mu_p`.

For a finite set `A`, define the centered monomial

$$
\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p),
\qquad \chi_\varnothing^*=1.
$$

The FA-1f constraint at `i` is

$$
c_i(\eta)=1-\eta(i-1)\eta(i+1),
$$

and the Bernoulli(`p`) refresh at `i` kills the centered factor when `i in A`:

$$
E_{i,p}\chi_A^*=0 \qquad (i\in A).
$$

Therefore

$$
L\chi_A^*(\eta)
=
\sum_{i\in A}
\bigl(\eta(i-1)\eta(i+1)-1\bigr)\chi_A^*(\eta).
\tag{1}
$$

This is the FA-1f specialization of the nonnegative centered-basis generator in the canonical patch paper, Theorem B / Section 5.4.

## Candidate Markov dual

For finite nonempty `A`, define

$$
H(A,\eta)=q^{-|A|}\chi_A^*(\eta).
\tag{2}
$$

Define a process on finite nonempty subsets of `Z` as follows. Each `i in A` rings at rate one. At its ring, independently refresh membership of the two sites `i-1,i+1` to Bernoulli(`q`), leave every site outside `{i-1,i+1}` unchanged, and in particular retain `i`.

Equivalently, for a test function `g` on finite nonempty subsets,

$$
\mathcal G g(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq N(i)}
q^{|R|}p^{|N(i)\setminus R|}
\,g\bigl((A\setminus N(i))\cup R\bigr)
-g(A)
\right],
\tag{3}
$$

where `N(i)={i-1,i+1}`.

The process never becomes empty because the ringing site `i` is not in `N(i)` and is retained.

## Generator calculation

Fix `i in A`. Put `N=N(i)`. Under the Bernoulli(`q`) refresh of membership in `N`,

$$
\mathbf E_R
H\bigl((A\setminus N)\cup R,\eta\bigr)
=
\frac{\chi_{A\setminus N}^*(\eta)}{q^{|A\setminus N|}}
\prod_{j\in N}
\left(p+q\frac{\eta(j)-p}{q}\right).
$$

Since

$$
p+(\eta(j)-p)=\eta(j),
$$

this becomes

$$
\mathbf E_R
H\bigl((A\setminus N)\cup R,\eta\bigr)
=
\frac{\chi_{A\setminus N}^*(\eta)}{q^{|A\setminus N|}}
\prod_{j\in N}\eta(j).
\tag{4}
$$

On the other hand, for every `j in A cap N`,

$$
\eta(j)(\eta(j)-p)=q\eta(j).
$$

Hence

$$
q^{-|A|}
\left(\prod_{j\in N}\eta(j)\right)
\chi_A^*(\eta)
=
\frac{\chi_{A\setminus N}^*(\eta)}{q^{|A\setminus N|}}
\prod_{j\in N}\eta(j).
\tag{5}
$$

Combining (4) and (5), the `i`-summand of `\mathcal G H` is

$$
\mathbf E_R
H\bigl((A\setminus N(i))\cup R,\eta\bigr)-H(A,\eta)
=
q^{-|A|}
\bigl(\eta(i-1)\eta(i+1)-1\bigr)
\chi_A^*(\eta).
$$

Summing over `i in A` and comparing with (1) gives the formal generator duality

$$
\mathcal G_A H(A,\eta)=L_\eta H(A,\eta).
\tag{6}
$$

Because both processes are standard finite-range systems and the set-valued process started finite has finite size on bounded time intervals, the expected semigroup duality should be

$$
P_t\chi_A^*(\eta)
=
q^{|A|}\mathbf E_A
\left[
q^{-|\mathcal A_t|}\chi_{\mathcal A_t}^*(\eta)
\right].
\tag{7}
$$

The infinite-volume passage / nonexplosion interface in (7) still needs to be written carefully by Student A rather than assumed from the formal generator identity.

## Single-vacancy specialization

Let `eta^{0}` have `eta^{0}(0)=0` and `eta^{0}(x)=1` for `x != 0`.

For every finite nonempty `B`,

$$
q^{-|B|}\chi_B^*(\eta^{0})
=
\begin{cases}
1, & 0\notin B,\\[4pt]
-p/q, & 0\in B.
\end{cases}
$$

Since `p=1-q`, this is exactly

$$
q^{-|B|}\chi_B^*(\eta^{0})
=1-q^{-1}\mathbf 1_{\{0\in B\}}.
\tag{8}
$$

Substituting (8) into (7) gives

$$
P_t\chi_A^*(\eta^{0})
=
q^{|A|}
\left[
1-q^{-1}\mathbf P_A(0\in\mathcal A_t)
\right].
\tag{9}
$$

Therefore, conditional on the validity of (7),

$$
P_t\chi_A^*(\eta^{0})\to0
\quad\Longleftrightarrow\quad
\mathbf P_A(0\in\mathcal A_t)\to q.
\tag{10}
$$

Because the nonempty centered monomials span the local mean-zero functions under `mu_p`, (10) for every finite nonempty `A` is equivalent to the active single-vacancy convergence target.

## Immediate structural observations to check, not assume

1. The transformed process has the infinite Bernoulli(`q`) product law as an obvious candidate invariant law: conditional on an active source `i`, its two neighbours are already independent Bernoulli(`q`) under the product law, so the refresh leaves the product law unchanged. This needs a proper generator/invariance check.

2. The transformed process is not obviously attractive. If `A subset B` and a site is active only in `B`, its refresh may delete neighbours that remain untouched in `A`.

3. For an isolated active site `i`, one ring produces no change with probability `p^2`, one extra neighbour with total probability `2pq`, and both neighbours with probability `q^2`. Thus the effective continuous-time off-diagonal rates are `pq,pq,q^2` for the three nontrivial additions. This should be tested against any claimed identification with a known branching/coalescing process.

4. If one neighbour is already active, a ring at `i` can delete that neighbour. Multi-particle transitions therefore matter immediately; a single-particle branching heuristic is insufficient.

5. The process may already be known under another duality or quasi-duality construction. Novelty of the representation is not assumed and is not needed if it gives leverage on the open theorem.

## Relation to closed routes

This calculation does not use the closed Bernoulli-quench sibling-cancellation mechanism. There is no expansion in an initial Bernoulli density and no hoped-for contraction across sibling generations. The transformed process is positive and the active initial condition is a deterministic finite seed.

If subsequent work merely reproduces the old sibling-generation calculation in different notation, the Professor should close that subroute immediately.