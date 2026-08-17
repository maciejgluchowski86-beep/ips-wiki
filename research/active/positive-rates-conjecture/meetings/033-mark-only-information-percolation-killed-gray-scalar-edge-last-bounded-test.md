# Group meeting 033: mark-only information percolation killed; Gray scalar-edge geometry gets one last bounded test

Date: 2026-08-17

`state_narrowed: yes`.

Professor review of:

- Student G Assignment 012 handoff `students/student-g/012-handoff.md`, commit `754edc7`;
- main report `012-information-percolation-pair-history.md`, commit `26a3e1a`;
- exact ancestry polytope checkpoint `c26558a` and verifier `ad1b1d6`;
- pair obstruction checkpoint `3f47066`, strengthened/corrected through `5140286`, `99d108e`, `4246ac0`, with scalar verifier `fd4d4ca` and its final strengthened form;
- Assignment 012 itself and its pre-registered strong-negative criterion;
- Meeting 032 and the toolbox positive-rates shortlist for direction after the result.

The principal reports independently running both committed verifiers at exit 0. I independently reconstructed the two load-bearing ancestry inequalities and checked the final rational cell/contour constants.

## Ruling

**Accept Assignment 012 as `STOP-PAIR-OBSTRUCTION`.** The mark-only deterministic-Boolean minimal-support implementation of the information-percolation bridge is impossible at the hard point `P_h`, uniformly over every exact local random-map decomposition.

This is a structural pair-history obstruction, not a first-moment failure. It does not prove nonergodicity and does not rule out a genuinely state-adaptive value-reveal history.

There is no status-protocol problem: the committed Assignment 012 explicitly lists `STOP-PAIR-OBSTRUCTION` among the permitted final statuses and names a decomposition-independent nondecaying pair observable as a qualifying strong negative outcome.

## 1. Exact ancestry bounds independently accepted

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

classify every nonidentity Boolean update map by essential parent set and let

- `d` = constant-map rate;
- `s` = self-only rate;
- `j` = right-only rate;
- `r` = two-parent rate.

The full exact projected polytope in G012a is useful but the pair obstruction needs only two inequalities, which follow directly from the four flip-rate budgets.

Summing the required flip rates at inputs `00` and `10` gives

$$
a+(1-c)=\frac1{5000}.
$$

Constants contribute one to this sum, `NOT x` contributes two, and right-only maps contribute one, while two-parent contributions are nonnegative. Hence

$$
\boxed{d+2s+j\le\frac1{5000}},
$$

so in particular

$$
\boxed{u:=d+j\le\frac1{5000}.}
$$

The flip-rate difference `lambda_11-lambda_00=1-a=c` can be carried only by constants and two-parent maps, giving `d+r>=c`. Likewise `lambda_11-lambda_10=c` gives `j+r>=c`. Therefore

$$
r\ge c-\min(d,j)
\ge c-\frac{d+j}{2}
\ge\frac{4999}{5000}.
$$

Thus the decisive near-unit branching / tiny-loss bounds are decomposition-independent without relying on numerical hull fitting.

## 2. Width-one pair lower process accepted

Run two independent backward-support processes. On a block of length `T=8`, let `G_{i,n}` require, in both copies,

1. no death/right-only mark at sites `i` or `i+1`;
2. at least one two-parent branch at `i`.

If `i` belongs to both supports at the block start and `G_{i,n}` occurs, then both `i` and `i+1` belong to both supports at the block end. Therefore the recursively defined oriented cluster

$$
C_{n+1}=\bigcup_{i\in C_n:G_{i,n}}\{i,i+1\}
$$

is pathwise contained in the support intersection at times `8n`.

The cell probability satisfies

$$
P(G_{i,n})
\ge e^{-4uT}(1-e^{-rT})^2.
$$

The final exact scalar bounds give

$$
P(G_{i,n})>
\frac{2481516621}{2500000000},
$$

hence the bad-cell probability obeys

$$
q<\frac{18483379}{2500000000}<\frac1{128}.
$$

I independently checked these fractions.

## 3. Percolation step and the changed constants

The `G` field is independent between time layers and one-dependent in space within each layer. The final analytic checkpoint uses a simple minimal bad cut contour in the planar two-child oriented lattice. A simple contour of `m` distinct cells has at most `2m 3^m` anchored possibilities. Along a fixed contour, the within-layer dependency graph is a union of paths, so at least half of the bad cells can be selected mutually independently. Therefore a fixed contour has probability at most `q^{m/2}`.

With `q<1/128<(4/45)^2`,

$$
2\sum_{m\ge1}m(3\sqrt q)^m
<2\sum_{m\ge1}m(4/15)^m
=\frac{120}{121}<1.
$$

This proves positive survival probability for the lower oriented cluster and hence a uniform positive lower bound on

$$
E[2^{|A_{8n}\cap A'_{8n}|}-1].
$$

The explicit `1/121` is not the conceptual result; nondecay is.

The change from the earlier `1/7` to final `1/121` is intentional. The initial checkpoint used the under-anchored count `2 3^m`. The final proof inserted the safe factor `m`, then strengthened the cell estimate from `q<1/100` to `q<1/128` so the corrected contour series still sums below one. The final survival lower bound is therefore weaker despite the tighter cell estimate.

The scalar verifier certifies the rational inequalities, not the planar contour lemma. I have separately checked the contour argument with the contour taken simple/minimal so the cells counted are distinct.

## 4. Exact scope of the negative result

Killed:

> Any exact local decomposition into deterministic Boolean marks whose information state is the mark-only essential-parent support, with the Miller--Peres test based on two independent copies of that support.

At `P_h`, no such decomposition can make

$$
E[2^{|A_t\cap A'_t|}-1]\to0.
$$

Not killed:

- state-adaptive reveal trees which inspect already determined spin values and short-circuit a globally essential parent;
- nonadditive Gray splice-edge geometry;
- the conjecture itself.

The state-adaptive possibility is not automatically promoted to a new B route. Near `P_h`, using value information without importing the desired mixing law is a substantial new theorem and presently has no bounded bridge statement. Escalating directly from G012 into an unrestricted adaptive-history search would violate the anti-loop standard.

## 5. Direction judgment

After G012, both concrete bounded mechanisms from the toolbox synthesis have failed in their stated forms:

- uniform additive-Hamming nonbasic coupling: analytically impossible for every Markovian coupling (Meeting 032);
- optimized mark-only information-percolation pair support: decomposition-independent pair obstruction (this meeting).

The principal-directed `pi_N` distinguished-zero transfer also stopped exactly at tail shift.

One toolbox PASS item remains logically untested rather than refuted: **Gray's nonadditive one-dimensional splice-edge geometry**. Meeting 032 correctly did not infer its failure from the Hamming obstruction. It is too underspecified for a full proof block, but it admits one final bounded structural test before the programme returns to `no-credible-route`.

Student G therefore receives Assignment 013: determine whether a scalar Gray-type splice edge can close locally at `P_h` under any exact local grand-coupling/random-map representation. The assignment must either derive a concrete feasible scalar-edge local mechanism or prove that scalar splice closure forces the attractive/repulsive structure absent at `P_h` (or another exact local obstruction). No multistate edge hierarchy is allowed if the scalar test fails.

If G013 stops negatively, the current toolbox-derived positive-rates opportunity set is exhausted: no automatic escalation to state-adaptive histories, larger edge states, or another generic coupling/norm search.

No public wiki edits are authorized.
