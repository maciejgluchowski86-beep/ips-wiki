# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Positive-rates programme: bounded restart tests exhausted

Branch: `research/positive-rates-conjecture`.

Workspace: `research/active/positive-rates-conjecture/`.

Target remains unresolved:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS with positive rates is ergodic.

Latest meeting: `research/active/positive-rates-conjecture/meetings/034-gray-scalar-edge-obstructed-toolbox-positive-rates-set-exhausted.md`, `state_narrowed: yes`.

There is **no active positive-rates proof architecture**. The present group-level status is `no-credible-route` after all bounded toolbox-derived PASS tests failed in their direct forms.

### G013: direct Gray scalar edge is locally obstructed

At

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

a common local graphical event represented by a deterministic Boolean rule `F` can preserve the two extremal half-line hybrids as a single scalar splice only if

\[
F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.
\]

This implies eventwise flip-indicator inequalities

\[
v_{11}\le v_{00}+v_{10},
\qquad
v_{00}\le v_{01}+v_{11}.
\]

After arbitrary nonnegative mixing of event types, the ordinary gauge would require

\[
1\le a+(1-c)=\frac1{5000},
\]

and the alternating/checkerboard gauge would require

\[
b\le a+(1-c),
\]

where at `P_h`, `1/100>1/5000`. Thus neither ordinary nor checkerboard scalar Gray closure is feasible even at the first splice-boundary event.

Assignment 013 is therefore `STOP-SCALAR-EDGE-OBSTRUCTION`. Full report: `students/student-g/013-gray-scalar-edge-feasibility.md`, commit `0744788e`; exact verifier final commit `f5a104d1`.

The obstruction is specific to the direct scalar/two-type Gray interface. It does not prove that every larger interface state is impossible, but the pre-registered experiment forbids escalating to such larger edge-state hierarchies after scalar failure.

### Other bounded PASS tests

- **Uniform additive-Hamming nonbasic coupling:** Meeting 032 proves the required negative drift impossible for every Markovian coupling at `P_h`.
- **Optimized mark-only information percolation:** G012/Meeting 033 prove a decomposition-independent nondecaying two-copy support intersection at `P_h`.
- **`pi_N` distinguished-zero transfer:** G011 proves exact transfer only on the product surface `a=b(1-c)`; buffered repairs are exactly the old tail-shift defect.

No positive structural signal remains from the bounded restart tests.

### Connected-renewal restart bar retained

The sharp residual object remains the signed boundary-transmission operator on the actual connected orbit,

\[
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
(g_0e^{-rs}-\varepsilon)e^{sL_{N-1}}f\,ds\,dt.
\]

No depth-uniform estimate retaining the two-time cancellation is known. A future positive-rates restart needs new input on this object or a materially different architecture with an explicit upstream mechanism and bounded falsification test.

Do not automatically restart larger Gray states, adaptive information histories, generic coupling/norm engineering, common-coupling occupation, tail shift, Bellman/Foster variants, reversible/filter searches or longer coefficient tables.

## Next active direction: FA-1f Bernoulli quench / FA-SCREEN

The completed 74-method toolbox assessment independently recommended a narrow reopening of the FA-1f Bernoulli-quench problem on **FA-SCREEN**, a two-sided causal-screen theorem inspired by East distinguished-zero screening.

The first gate is a finite 5--7-site graphical leakage/measurability test of a concrete left/right screen rule. A viable screen must be determined without revealing the protected future interior marks, must block exterior influence on the protected interval except through admissible boundary data, and leave enough relaxation time relative to screen size for the known positive finite-volume FA gap to erase the conditional initial law.

This direction had been deferred while the available execution capacity was used on the principal-directed positive-rates distinguished-zero question and the subsequent bounded positive-rates tests. With G013 negative, **FA-SCREEN is now the queued next active research direction; it is not withdrawn.**

Student G is currently unavailable due to an operational session failure. No other student is executing. The Professor session is the available execution session.

## Retained mathematics

The positive-rates predecessor-trail reduction, projective zero-boundary invariant family, exact tail-shift identity, common-coupling local-erasure/front results, stationary boundary-control hierarchy, trajectory-valued spatial-kernel obstruction, G009/G010 renewal/positive-frequency structure, G011 product-surface transfer obstruction, universal Hamming-coupling obstruction, G012 ancestry/pair obstruction, and G013 Gray scalar-edge obstruction remain retained background.

The frozen ergodicity-method toolbox contains 74 live/source-audited methods; no public taxonomy/navigation changes follow from the private applicability rankings.

## Wiki freeze

The live wiki remains frozen during active research. No `docs/` or `mkdocs.yml` edits are authorized by the current work.
