# 008: novelty and closest-prior-work audit for generalized patch representations

Date: 2026-08-17

## Outcome

\[
\boxed{\texttt{CONTINUE-TO-APPLICATIONS}.}
\]

This is not a blanket novelty verdict. The fixed package contains both directly known mathematics and a mechanism for which no equivalent prior source was found. The programme-level continuation rests on the latter.

## 1. Executive ruling

The audit materially narrows the contribution claim.

The following are **not** independent project contributions:

- finite-state/product graphical duality in structured IPS classes;
- signed Feynman--Kac duality with finite types;
- backward Poisson ancestor/skeleton constructions and partial graphical revelation;
- finite-dimensional positive-semigroup/Metzler theory;
- third-order nonnegative matrix-exponential response criteria;
- the Assignment-006 `d=3` critical-point calculation as a standalone theorem.

The strongest surviving novelty candidate is the exact finite-state **killed typed patch factorization and representation**:

1. arbitrary finite-state single-site replacement IPS is expanded into a signed typed FK dual;
2. a nonempty successful record reveals source/time/pre-source type/typed target but hides the post-source outcome;
3. one-site source-time patches carry the hidden signed local histories;
4. incoming typed target conflicts create cemetery and make bare conditioning on the coarse record list fail;
5. multiplying by the noncemetery indicator restores an exact weighted product factorization;
6. averaging the local signed FK weight on each consistent patch gives the exact bulk/end representation;
7. the bulk factors induce local finite-dimensional external-positivity problems.

Every major ingredient has predecessors, but no source found contains this combined interface in equivalent form. This supports a **plausibly new mechanism** status, not a claim of established historical priority.

## 2. Required component statuses

| Item | Status | Closest prior work / reason |
|---|---|---|
| 1. finite-state typed signed duality | **known ingredients, assembly plausibly new** | Lloyd--Sudbury/Sudbury product duality; Sturm--Swart and Latz--Swart finite-state pathwise duals; Dawson--Greven signed FK duals; general FK genealogies and finite-matrix multiplicative functionals. Exact arbitrary-replacement typed assembly not found, but ingredients are too standard for a standalone novelty claim. |
| 2. killed typed patch factorization / representation | **plausibly new theorem/mechanism** | Fernández--Ferrari--Garcia clans of ancestors and Lubetzky--Sly information percolation are close predecessors for partial revelation; signed FK is known separately. No equivalent source found for hidden signed source outcomes + typed cemetery conflicts + failure of bare factorization + exact killed/noncemetery patchwise repair. |
| 3. transfer-matrix bulk positivity formulation | **known ingredients, assembly plausibly new** | External/internal positive-systems theory already studies `C e^{tA}B`. What appears project-specific is the derivation `K=A^emptyset` from FK cancellation and the patch-boundary input/output dictionary. |
| 4. exact boundary-complete `d=3` finite spectral criterion | **known / directly subsumed** | After multiplying by `e^{-dt}`, each `OI` numerator is the impulse response of a stable third-order SISO linear system with real poles. Lin--Fang (1997) gave necessary-and-sufficient real-pole third-order monotone-step/nonnegative-impulse criteria; Weller--Martin (2020) explicitly gives exact third-order external positivity. |
| 5. exchange-symmetric exact algebraic criterion | **known ingredients, assembly plausibly new** | Exact IPS coefficient translation not found, but scalar content is a structured third-order external-positivity consequence using standard symmetry/eigenmode ordering. Useful, genuinely nonbinary, but not a primary novelty anchor. |
| 6. combined framework | **plausibly new theorem/mechanism** | No source found subsuming the full arbitrary-finite-state signed-dual -> hidden successful skeleton -> killed typed patch factorization -> bulk/end representation -> local positivity chain. |

## 3. Closest predecessor reconstruction

### 3.1 Classical/product and finite-state graphical duality

Lloyd--Sudbury (1995, 1997), Sudbury (2000), and later algebraic-duality treatments systematically derive product-form dualities from local generator algebra. Sturm--Swart (2018) treats monotone/additive pathwise duality for finite local state spaces through Poisson random mappings. Latz--Swart (2023) develops commutative-monoid/semiring duality and explicitly produces genuinely multistate (`3+`) IPS dualities.

These sources directly remove novelty from the broad statements "finite-state IPS have product dualities" and "multistate IPS have graphical duals".

They do not treat arbitrary replacement generators by the current signed indicator-basis expansion and do not contain the later hidden-outcome patch factorization.

### 3.2 Signed Feynman--Kac duality

Dawson--Greven, arXiv:1007.5462, Proposition 3.2, explicitly states a **signed with Feynman--Kac dual** for a finite-type Fisher--Wright model. Selection produces a signed function-valued branch update and an exponential FK weight. Their subsequent spatial Fleming--Viot work, arXiv:1104.1099, develops extensive finite-type function/set/tableau-valued duals.

Thus signed cancellation plus an FK exponential is directly prior art. Assignment 001 cannot claim novelty on that basis.

### 3.3 Partial graphical revelation and ancestor skeletons

Fernández--Ferrari--Garcia (SPA 2002; arXiv:math/9911162) uses a two-stage procedure: generate the finite relevant portion of a marked spacetime Poisson process by tracing ancestors, then run a cleaning procedure according to interactions.

Lubetzky--Sly information percolation (JAMS 2016; arXiv:1401.6065) tracks backward update dependencies and decomposes the spacetime history into information-flow clusters, separating dependency geometry from additional update randomness.

Therefore "reveal a coarse spacetime dependency object and process hidden marks later" is not new as a broad probabilistic strategy.

The distinction in the current mechanism is that the hidden mark is a signed dual source outcome, local patch averaging acts on an FK multiplicative weight, and typed target conflicts create a cemetery branch whose future record constraints disappear. That last fact makes the **bare** coarse-skeleton conditional law nonproduct and necessitates the killed/noncemetery repair. No counterpart was found in the predecessor sources.

### 3.4 Positive systems and external positivity

Positive-systems theory classically gives

\[
e^{tA}\ge0\text{ for all }t\ge0
\iff A\text{ is Metzler}.
\]

More importantly for this project, continuous-time **external positivity** of a SISO realization is exactly

\[
C e^{tA}B\ge0\qquad(t\ge0).
\]

This is precisely the mathematical form of a fixed patch-boundary `OI` numerator once Assignment 004 supplies `K,p,f`.

For `d=3`, choose any scalar `d_0>0`. Since

\[
p e^{tK}f\ge0
\iff
p e^{t(K-d_0I)}f\ge0,
\]

the problem is a stable third-order SISO external-positivity problem. Lin--Fang (IEEE TAC 1997) already gives necessary-and-sufficient real-pole third-order monotone-step criteria; Weller--Martin (IFAC 2020) explicitly characterizes third-order external positivity. This directly subsumes Assignment 006 as an independent scalar positivity theorem.

Recent control literature states that general external-positivity characterization becomes difficult at higher order and uses approximate/sufficient methods, reinforcing the decision not to launch generic `d>3` positivity algebra by default.

## 4. Chronology and successor check

The closest ingredients predate the generalized programme by years or decades:

- graphical/additive duality: classical Harris/Griffeath/Liggett;
- product-form local duality: Lloyd--Sudbury/Sudbury;
- clans of ancestors: 1999/2002;
- third-order monotone/nonnegative response criterion: 1997;
- signed finite-type FK duality: 2010;
- information percolation: 2014--2016;
- systematic finite-state pathwise duality: 2018;
- commutative-monoid multistate duality: 2021/2023.

Modern successor searches included multistate epidemic dualities (Franceschini--Saada--Schütz--Velasco, arXiv:2408.15613) and current positive-systems literature. These reinforce that multistate duality and finite-dimensional positivity are active, established subjects, but no direct successor containing the typed killed-patch mechanism was located.

## 5. Why the ruling is not `STOP-GENERALIZATION-SUBSUMED`

A stop would require the generalized representation/positivity mechanism itself to be directly present in prior work in equivalent form. The audit found direct subsumption of **one package item** (the `d=3` scalar spectral criterion) and strong prior art for most ingredients, but not of the killed typed patch factorization/representation.

That surviving item is load-bearing rather than cosmetic: without it there is no exact patch representation for finite-state replacement dynamics and no route from signed dual cancellation to local patch factors. It is also mathematically distinct from the binary paper because typed target conflicts force a new killed/noncemetery construction; bare factorization is false and the project has an exact finite counterexample establishing this.

Accordingly the core framework is not judged subsumed.

## 6. Why the ruling is not `NARROW-TO-SPECIFIC-NEW-THEOREM`

The novelty does concentrate around item 2, but item 2 is the structural bridge supporting the arbitrary-finite-state representation rather than an isolated side theorem. The natural research object remains the generalized patch framework, now framed correctly:

> a new-looking way to extend patch averaging to arbitrary finite-state replacement IPS despite signed retyping branches and typed cemetery conflicts.

The later transfer formulation is part of demonstrating what this mechanism buys. The `d=3` spectral calculation is no longer part of the novelty claim.

Therefore a separate narrowing phase before applications would add little. The next useful test is whether the surviving representation applies to a natural genuinely nonbinary IPS.

## 7. Next block

Per Meeting 007 and the pre-registered Assignment-008 sequencing rule, the next active mathematical block is **applications**.

It should seek a genuinely nonbinary finite-state single-site replacement IPS from existing probability/statistical-mechanics models, not an artificial coefficient table, and determine:

1. whether the typed successful-skeleton representation specializes naturally;
2. whether its bulk patch positivity can be certified by the exact exchange-symmetric/refresh criterion or, if needed, the general `d=3` external-positivity test;
3. whether the representation yields a useful statement not already standard for that model.

Generic `d>3` positivity algebra remains deferred unless a natural application requires it or literature later indicates that arbitrary-`d` tractability is independently important.

## 8. Sources carrying the ruling

Most load-bearing sources:

- Lloyd, Sudbury (1995, 1997); Sudbury (2000): product-form IPS duality;
- Jansen--Kurt (2014): general Markov duality framework;
- Sturm--Swart (2018): finite-state monotone/additive pathwise duality;
- Latz--Swart (2023): commutative-monoid multistate pathwise duality;
- Dawson--Greven (2010, arXiv:1007.5462): signed FK finite-type duality;
- Dawson--Greven (2011, arXiv:1104.1099): finite-type spatial Fleming--Viot duals;
- Fernández--Ferrari--Garcia (2002, arXiv:math/9911162): ancestor/cleaning marked-Poisson construction;
- Lubetzky--Sly (2016, arXiv:1401.6065): information-percolation partial graphical revelation;
- Foxall (2016, arXiv:1410.4809): multitype additive duality and positive-correlation criterion;
- Lin--Fang (1997), DOI 10.1109/9.623097: exact third-order real-pole monotone-step criterion;
- Weller--Martin (2020), DOI 10.1016/j.ifacol.2020.12.509: exact third-order external positivity;
- Weller (2023), DOI 10.1016/j.ifacol.2023.10.1289: higher-order external-positivity characterization remains difficult in general;
- Franceschini--Saada--Schütz--Velasco, arXiv:2408.15613: recent multistate epidemic IPS dualities.

Detailed source comparisons are in `008a`--`008e`.